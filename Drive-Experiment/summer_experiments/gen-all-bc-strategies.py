loe_d = {
    "bioavailability":  [["(pk_ct_pk){1,}","(label_statement){1,}"]],
    
    "controls_formation_of": [["(pk_ct_pk_genotype){1,}","(pk_ct_pk_phenotype){1,}"],
                              ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                              ["(iv_met_enz_id_Cyp450_with_inh){1,}"],
                              ["(label_statement){1,}"],
                              ["(na_substrate_of){1,}"]],
    
    "does_not_inhibit": [["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}","(iv_met_inh_microsomal){1,}","(iv_met_inh_recombinant){1,}"],
                         ["(label_statement){1,}"]],
    
    "first_pass_effect": [["(pk_ct_pk){1,}"],
                          ["(label_statement){1,}"]],

    "fraction_absorbed": [["(pk_ct_pk){1,}"],
                          ["(label_statement){1,}"]],
    
    "has_metabolite": [["(pk_ct_pk){1,}"],
                       ["(iv_met_enz_id_Cyp450_with_inh){1,}"],
                       ["(label_statement){1,}"],
                       ["(na_substrate_of){1,}"]],
    
    "increases_auc": [["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                      ["(label_statement){1,}"]],
    
    "inhibition_constant": [["(label_statement){1,}"],
			    ["(iv_met_inh_microsomal){1,}","(iv_met_inh_recombinant){1,}"]],
    
    "inhibits": [["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                 ["(iv_met_inh_microsomal){1,}","(iv_met_inh_recombinant){1,}","(label_statement){1,}"]],

    "is_not_substrate_of": [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                            ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                            ["(iv_met_enz_id_Cyp450_with_inh){1,}"],
                            ["(label_statement){1,}"],
                            ["(na_substrate_of){1,}"]],

    "maximum_concentration": [["(pk_ct_pk){1,}", "(label_statement){1,}"]],
    
    "primary_metabolic_clearance_enzyme": [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                                           ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                                           ["(label_statement){1,}"],
                                           ["(na_primary_metabolic_clearance_enzyme){1,}"]],

    "primary_total_clearance_enzyme": [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                                       ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                                       ["(label_statement){1,}"]],
    
    "primary_total_clearance_mechanism": [["(pk_ct_pk){1,}"],
                                          ["(label_statement){1,}"],
                                          ["(na_primary_total_clearance_enz){1,}"]],
    
    "substrate_of": [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                     ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                     ["(iv_met_enz_id_Cyp450_with_inh){1,}"],
                     ["(label_statement){1,}"],
                     ["(na_substrate_of){1,}"]],

    ## assertions below this line are 'default assumptions' for the current study. Their
    ## evidence is not evaluated so, these LOEs are not used
    "assumed_effective_dose": [["(label_statement){1,}"]],

    "does_not_permanently_deactivate_catalytic_function": [["(iv_met_enz_id_Cyp450_microsomal){1,}", "(iv_met_enz_id_Cyp450_recombinant){1,}"],
                                                           ["(label_statement){1,}"],
                                                           ["(nt_statement){1,}"]],

    'in_vitro_probe_substrate_of_enzyme':[["(iv_met_enz_id_Cyp450_microsomal){1,}", "(iv_met_enz_id_Cyp450_recombinant){1,}"],
                                          ["(label_statement){1,}"],
                                          ["(nt_statement){1,}"]],
    
    "in_vitro_selective_inhibitor_of_enzyme": [["(iv_met_inh_recombinant){1,}"],
                                               ["(iv_met_inh_microsomal){1,}"],
                                               ["(label_statement){1,}"],
                                               ["(nt_statement){1,}"]],
    
    'in_viVo_probe_substrate_of_enzyme':  [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                                            ["(pk_ddi_rndm){1,}","(pk_ddi_non_rndm){1,}"],
                                            ["(label_statement){1,}"],
                                            ["(nt_statement){1,}"]],

    "in_viVo_selective_inhibitor_of_enzyme": [["(pk_ddi_rndm){1,}"],
                                              ["(pk_ddi_non_rndm){1,}"],
                                              ["(label_statement){1,}"],
                                              ["(nt_statement){1,}"]],
    
    "maximum_therapeutic_dose": [["(label_statement){1,}"]],

    "minimum_therapeutic_dose": [["(label_statement){1,}"]],

    'pceut_entity_of_concern': [["(pk_ddi_rndm){1,}", "(pk_ddi_non_rndm){1,}", "(obs_eval){1,}", "(label_statement){1,}"],
                                ["(nt_statement){1,}"]],
    
    "permanently_deactivates_catalytic_function": [["(iv_met_enz_id_Cyp450_microsomal){1,}", "(iv_met_enz_id_Cyp450_recombinant){1,}"],
                                                   ["(label_statement){1,}"],
                                                   ["(nt_statement){1,}"]],
    
    "polymorphic_enzyme": [["(pk_ct_pk_phenotype){1,}", "(pk_ct_pk_genotype){1,}"],
                           ["(label_statement){1,}"],
                           ["(nt_statement){1,}"]],
    
    "sole_PK_effect_alter_metabolic_clearance": [["(pk_ddi_rndm){1,}"],
                                                 ["(pk_ddi_non_rndm){1,}"],
                                                 ["(label_statement){1,}"],
                                                 ["(nt_statement){1,}"]],
    }

bc_d = { 
    "bioavailability":  1,
    "controls_formation_of": 1,
    "does_not_inhibit": (('does_not_inhibit',1),('inhibits',1)),
    "first_pass_effect": 1,
    "fraction_absorbed": 1,
    "has_metabolite": 1,
    "increases_auc": 1,
    "inhibition_constant": 1,
    "inhibits": (('inhibits',1),('does_not_inhibit',1)),
    "is_not_substrate_of":1,
    "maximum_concentration": 1,
    "primary_metabolic_clearance_enzyme": 1,
    "primary_total_clearance_enzyme": 1,
    "primary_total_clearance_mechanism": 1,
    "substrate_of": 1,

    ## assertions below this line are 'default assumptions' for the current study. Their
    ## evidence is not evaluated so, these belief criteria are not used
    "assumed_effective_dose": 1,
    "does_not_permanently_deactivate_catalytic_function": 1,
    'in_vitro_probe_substrate_of_enzyme': 1,
    "in_vitro_selective_inhibitor_of_enzyme": 1,
    "in_viVo_probe_substrate_of_enzyme": 1,
    "in_viVo_selective_inhibitor_of_enzyme": 1,
    "maximum_therapeutic_dose": 1,
    "minimum_therapeutic_dose": 1,
    'pceut_entity_of_concern': 1,
    "permanently_deactivates_catalytic_function": 1,    
    "polymorphic_enzyme": 1,
    "sole_PK_effect_alter_metabolic_clearance": 1,
    }

## this removes all default assumptions and assertions for which
## varying levels of evidence will have no effect simply because all
## of the evidence for or against fall within the highest-ranked
## belief criteria
non_dflts = ["controls_formation_of", "has_metabolite", "inhibits", "is_not_substrate_of", "primary_metabolic_clearance_enzyme", "primary_total_clearance_enzyme", "primary_total_clearance_mechanism", "substrate_of", "inhibition_constant"]

# get a list of lists where each list holds a sequence from 0 to the
# len - 1 of the list referenced in the LOE dictionary by the key
a = []
for k in non_dflts:
    a.append(range(1, len(loe_d[k]) + 1))

# how many combinations?
n_comb = reduce(lambda x,y: x*y, map(lambda x: len(x), a))

# get all possible evidence combinations 
# Thans to Wensheng Wang : http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496807
r=[[]]
for x in a:
    t = []
    for y in x:
        for i in r:
            t.append(i+[y])
    r = t

## for each strategy, create a new folder and write out the loe and
## modified belief criteria dictionaries in that folder
pth_prfx = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/colloquium/"
f = open(pth_prfx + "belief-criteria-strategies", 'w')
for s in r:
    f.write(str(s) + "\n")
f.close()

import os
dirs = []
for s in r:
    d_nm = pth_prfx + "strategy-" + "-".join([str(x) for x in s])
    dirs.append(d_nm)
    
    # NOTE: code below commented out so that data is not destroyed - RDB
    os.mkdir(d_nm)

    # set up belief criteria according to the strategy
    for i in range(0, len(s)):
        k = non_dflts[i]
        v = s[i]
        bc_d[k] = v

    # write the LOE dict and belief criteria
    print "Writing strategy: %s/levels-of-evidence" % d_nm
    f = open(d_nm + "/levels-of-evidence", 'w')
    f.write("# Generated by [gen-all-bc-strategies.py]\n# Generated on 7/20/2016 by Sam Rosko \n#\n# key: %s, %s\n\n" % (str(non_dflts), str(s)))
    f.write("loe_d = %s\n\n" % str(loe_d))
    f.write("bc_d = %s\n\n" % str(bc_d))
    f.close()

f = open(pth_prfx + "paths-to-experiment-folders", 'w')
f.write("\n".join(dirs))
f.close()

        
    
    
    

