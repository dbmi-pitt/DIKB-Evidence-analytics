## compare-predictions.R
## a modified version created by Sam Rosko for working with his own data
## last updated: 2017-03-14

# july 2016 configuration
prfx = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/experiment_2/dikb-loe-experiments-scr25-results-colloquium.tsv"

# read into table
column_names = c("strategy","num_pairs","DIKB-ddi","DIKB-ddi-freq","DIKB-non-DDI","DIKB-non-DDI-freq","DIKB-unknown","DIKB-unknown-freq","both-unknown","val-set-only-unknown","DIKB-only-unknown","tp","fp","tn","fn","npv","ppv","sens","spec","f1","kappa","num-val-set-DDIs","num-val-set-non-DDIs","num-val-set-unknown")
ref_table = read.table(prfx, col.names = column_names)
ref_table$coverage = (ref_table$tp + ref_table$tn) / 158
ref_table$num_unknowns = (ref_table$DIKB.ddi + ref_table$DIKB.non.DDI) - (ref_table$tp + ref_table$tn + ref_table$fp + ref_table$fn)
ref_table$num_unknown_pddis = (ref_table$DIKB.ddi) - (ref_table$tp + ref_table$fn)
ref_table$num_unknown_nonpddis = (ref_table$DIKB.non.DDI) - (ref_table$fp + ref_table$tn)

# COMPARING IN VITRO DATA TO NOT USING IN VITRO DATA
## This function lets you run multiple regexs at once
include <- function (theList, toMatch){
  matches <- unique (grep(paste(toMatch,collapse="|"), 
                          theList, value=TRUE))
  return(matches)
}

both_iv_reg_list = c("strategy-.-.-2-3-.-.-.-.-.", "strategy-.-.-2-4-.-.-.-.-.", "strategy-.-.-2-5-.-.-.-.-.", "strategy-.-.-.-3-.-.-.-.-2", "strategy-.-.-.-4-.-.-.-.-2", "strategy-.-.-.-5-.-.-.-.-2", "strategy-.-.-2-.-.-.-.-3-.", "strategy-.-.-2-.-.-.-.-4-.", "strategy-.-.-2-.-.-.-.-5-.", "strategy-.-.-.-.-.-.-.-3-2", "strategy-.-.-.-.-.-.-.-4-2", "strategy-.-.-.-.-.-.-.-5-2")
both_iv_temp = include(theList = ref_table$strategy, toMatch = both_iv_reg_list)
both_iv_table = ref_table[ref_table$strategy %in% both_iv_temp, ]

iv_inh_reg_list = c("strategy-.-.-2-1-.-.-.-1-.", "strategy-.-.-.-1-.-.-.-1-2", "strategy-.-.-2-2-.-.-.-1-.", "strategy-.-.-.-2-.-.-.-1-2", "strategy-.-.-2-1-.-.-.-2-.", "strategy-.-.-.-1-.-.-.-2-2", "strategy-.-.-2-2-.-.-.-2-.", "strategy-.-.-.-2-.-.-.-2-2")
iv_inh_temp = include(theList = ref_table$strategy, toMatch = iv_inh_reg_list)
iv_inh_table = ref_table[ref_table$strategy %in% iv_inh_temp, ]

iv_sub_reg_list = c("strategy-.-.-1-3-.-.-.-.-1", "strategy-.-.-1-4-.-.-.-.-1", "strategy-.-.-1-5-.-.-.-.-1", "strategy-.-.-1-.-.-.-.-3-1", "strategy-.-.-1-.-.-.-.-4-1", "strategy-.-.-1-.-.-.-.-5-1")
iv_sub_temp = include(theList = ref_table$strategy, toMatch = iv_sub_reg_list)
iv_sub_table = ref_table[ref_table$strategy %in% iv_sub_temp, ]

no_iv_reg_list = c("strategy-.-.-1-1-.-.-.-1-1", "strategy-.-.-1-1-.-.-.-2-1", "strategy-.-.-1-2-.-.-.-1-1", "strategy-.-.-1-2-.-.-.-2-1")
no_iv_temp = include(theList = ref_table$strategy, toMatch = no_iv_reg_list)
no_iv_table = ref_table[ref_table$strategy %in% no_iv_temp, ]

#bug_fixer = c("strategy-.-.-2-3-.-.-.-.-.", "strategy-.-.-2-4-.-.-.-.-.", "strategy-.-.-2-5-.-.-.-.-.", "strategy-.-.-.-3-.-.-.-.-2", "strategy-.-.-.-4-.-.-.-.-2", "strategy-.-.-.-5-.-.-.-.-2", "strategy-.-.-2-.-.-.-.-3-.", "strategy-.-.-2-.-.-.-.-4-.", "strategy-.-.-2-.-.-.-.-5-.", "strategy-.-.-.-.-.-.-.-3-2", "strategy-.-.-.-.-.-.-.-4-2", "strategy-.-.-.-.-.-.-.-5-2", "strategy-.-.-2-1-.-.-.-1-.", "strategy-.-.-.-1-.-.-.-1-2", "strategy-.-.-2-2-.-.-.-1-.", "strategy-.-.-.-2-.-.-.-1-2", "strategy-.-.-2-1-.-.-.-2-.", "strategy-.-.-.-1-.-.-.-2-2", "strategy-.-.-2-2-.-.-.-2-.", "strategy-.-.-.-2-.-.-.-2-2", "strategy-.-.-1-3-.-.-.-.-1", "strategy-.-.-1-4-.-.-.-.-1", "strategy-.-.-1-5-.-.-.-.-1", "strategy-.-.-1-.-.-.-.-3-1", "strategy-.-.-1-.-.-.-.-4-1", "strategy-.-.-1-.-.-.-.-5-1", "strategy-.-.-1-1-.-.-.-1-1", "strategy-.-.-1-1-.-.-.-2-1", "strategy-.-.-1-2-.-.-.-1-1", "strategy-.-.-1-2-.-.-.-2-1")
#bug_t = include(theList = ref_table$strategy, toMatch = bug_fixer)
#bug_table = ref_table[ref_table$strategy %in% bug_t, ]

headers = c("mean_pred", "mean_unknowns", "mean_f1", "mean_npv", "mean_prec", "mean_recall","mean_coverage","mean_unknown_pddis", "mean_unknown_nonpddis")

overall_values = c(mean((ref_table$DIKB.ddi+ref_table$DIKB.non.DDI)), mean(ref_table$num_unknowns), mean(ref_table$f1), mean(ref_table$npv), mean(ref_table$ppv), mean(ref_table$sens), mean(ref_table$coverage), mean(ref_table$num_unknown_pddis), mean(ref_table$num_unknown_nonpddis))
both_values = c(mean((both_iv_table$DIKB.ddi+both_iv_table$DIKB.non.DDI)), mean(both_iv_table$num_unknowns), mean(both_iv_table$f1), mean(both_iv_table$npv), mean(both_iv_table$ppv), mean(both_iv_table$sens), mean(both_iv_table$coverage), mean(both_iv_table$num_unknown_pddis), mean(both_iv_table$num_unknown_nonpddis))
iv_subs_values = c(mean((iv_sub_table$DIKB.ddi+iv_sub_table$DIKB.non.DDI)), mean(iv_sub_table$num_unknowns), mean(iv_sub_table$f1), mean(iv_sub_table$npv), mean(iv_sub_table$ppv), mean(iv_sub_table$sens), mean(iv_sub_table$coverage), mean(iv_sub_table$num_unknown_pddis), mean(iv_sub_table$num_unknown_nonpddis))
iv_inh_values = c(mean((iv_inh_table$DIKB.ddi+iv_inh_table$DIKB.non.DDI)), mean(iv_inh_table$num_unknowns), mean(iv_inh_table$f1), mean(iv_inh_table$npv), mean(iv_inh_table$ppv), mean(iv_inh_table$sens), mean(iv_inh_table$coverage), mean(iv_inh_table$num_unknown_pddis), mean(iv_inh_table$num_unknown_nonpddis))
no_iv_values = c(mean((no_iv_table$DIKB.ddi+no_iv_table$DIKB.non.DDI)), mean(no_iv_table$num_unknowns), mean(no_iv_table$f1), mean(no_iv_table$npv), mean(no_iv_table$ppv), mean(no_iv_table$sens), mean(no_iv_table$coverage), mean(no_iv_table$num_unknown_pddis), mean(no_iv_table$num_unknown_nonpddis))

results = data.frame(headers,overall_values,both_values,iv_subs_values,iv_inh_values,no_iv_values)