## code for generating an ROC scatterplot for the DIKB experiments

## The key for understanding the labels that I gave each belief criteria
#strategy can be found in all files named levels-of-evidence in the
# sub-folders in file://home/boycerd/UW_stuff/DrugInteractions/KnowledgeBase/di-modeling-theory/experiments/loe-experiment-spring-2006/belief-criteria-experiment/experiments/experiment-2-results/

# key: ['controls_formation_of', 'has_metabolite', 'inhibits', 'is_not_substrate_of',
#       'primary_metabolic_clearance_enzyme', 'primary_total_clearance_enzyme',
#        'primary_total_clearance_mechanism', 'substrate_of']

# the cut-off for the ROC will be 1.0 / average(LOE ranks) because
# this number increases with the stringency of the belief criteria
# strategy

tbl = read.delim("dikb-loe-experiments-REDO-06012008-results.tsv",na.strings =c("NA",""," "))
# we need to remove the first row because it is the evidence-board's
# belief criteria strategy. 
tbl <- tbl[-c(1),]

## We also need to throw out the bad data from one strategy that was
## incorrectly ran: strategy-1-4-2-1-1-1-3-3
tbl[19236,]
tbl <- tbl[-c(19236),]

cutoff_rng <- vector("numeric", length=35999)
sens_vec <-  vector("numeric", length=35999)
spec_vec <- vector("numeric", length=35999)
covrge_vec <- vector("numeric", length=35999)
nvl_vec <- vector("numeric", length=35999)
cnt = 1
for (i in seq(1,5)){ # controls_formation
  for (j in seq(1,4)){ # has_metabolite
    for (k in seq(1,2)){ # inhibits
      for (m in seq(1,5)){ # is_not_substrate_of
        for (n in seq(1,4)){ # primary_metabolic_clearance_enzyme
          for (p in seq(1,3)){ # primary_total_clearance_enzyme
            for (q in seq(1,3)){ # primary_total_clearance_mechanism
              for (r in seq(1,5)){ # substrate_of
                #print(cnt)
                
                cutoff_rng[cnt] = 1.0 / ((i+j+k+m+n+p+q+r) / 8.0)            
                nm = paste("strategy-", i, "-", j, "-", k, "-", m, "-", n, "-", p, "-", q, "-", r, sep="")
                
                if (nm == "strategy-1-4-2-1-1-1-3-3")
                  next
                
                sens_vec[cnt] <- tbl[tbl$strategy == nm,]$sens
                spec_vec[cnt] <- tbl[tbl$strategy == nm,]$spec
                covrge_vec[cnt] <- (tbl[tbl$strategy == nm,]$tp + tbl[tbl$strategy == nm,]$tn) / 48.0
                nvl_vec[cnt] <- (tbl[tbl$strategy == nm,]$DIKB.ddi + tbl[tbl$strategy == nm,]$DIKB.non.DDI) - (tbl[tbl$strategy == nm,]$tp + tbl[tbl$strategy == nm,]$tn + tbl[tbl$strategy == nm,]$fp + tbl[tbl$strategy == nm,]$fn)
                
                cnt = cnt + 1
              }
            }}}}}}}
  

## oops, I should have saved the string names of each strategy to a
## vector so that I could just create one table
nm_vec <- vector("character", length=35999)
cnt = 1
for (i in seq(1,5)){ # controls_formation
  for (j in seq(1,4)){ # has_metabolite
    for (k in seq(1,2)){ # inhibits
      for (m in seq(1,5)){ # is_not_substrate_of
        for (n in seq(1,4)){ # primary_metabolic_clearance_enzyme
          for (p in seq(1,3)){ # primary_total_clearance_enzyme
            for (q in seq(1,3)){ # primary_total_clearance_mechanism
              for (r in seq(1,5)){ # substrate_of

                nm = paste("strategy-", i, "-", j, "-", k, "-", m, "-", n, "-", p, "-", q, "-", r, sep="")
                if (nm == "strategy-1-4-2-1-1-1-3-3")
                  next
                
                nm_vec[cnt] <- nm
                
                cnt = cnt + 1
              }
            }}}}}}}

roc_df <- data.frame(cbind(nm_vec, cutoff_rng, sens_vec, spec_vec, covrge_vec, nvl_vec))
write.csv(roc_df, "DIKB-experiment-ROC-data-03032009.csv")
# roc_df <- read.csv("DIKB-experiment-ROC-data-03032009.csv")

## create the ROC scatterplot

length(roc_df$spec_vec[roc_df$spec_vec == "NaN"])
# [1] 10367
length(roc_df$sens_vec[roc_df$sens_vec == "NaN"])
# [1] 0

x = roc_df$spec_vec[roc_df$spec_vec != "NaN"] # 25632 elements
y = roc_df$sens_vec[roc_df$spec_vec != "NaN"]

plot(0:1, 0:1, type = "n", xlab="False Positive Rate", ylab="True Positive Rate")
points(1.0 - x, y, col="blue")
dev.copy2eps()

# IMPORTANT: the evidence board's strategy cannot be shown in the "ROC
# scatterplot" because it made no TN, FP, or FN DDI predictions

# an informative plot might be the sensitivity vs 1.0 minus the
# average LOE level

x = roc_df$cutoff_rng
y = roc_df$sens_vec

# add to the plot the proportion of validation interaction predicted
# by the DIKB 
z = roc_df$covrge_vec

plot(0:1, 0:1, type = "n", xlab="1.0 / (average LOE level)", ylab="")
points(x, y, col="blue")
points(x, z, pch=3)
abline(v=1, col="red")
legend(0.1,0.1, c("true positive rate", "proportion of predictions present in the validation set"), pch=c(1,3), col=c("blue","black"), bty="n")

#points(1, 1, pch=17, col="green")

dev.copy2eps()

## 03172009 : I realized that I need to plot accuracy instead of the TPR because
## it brings in the FP and FN

tbl = read.delim("dikb-loe-experiments-REDO-06012008-results.tsv",na.strings =c("NA",""," "))

# we need to remove the first row because it is the evidence-board's
# belief criteria strategy. 
tbl <- tbl[-c(1),]

## We also need to throw out the bad data from one strategy that was
## incorrectly ran: strategy-1-4-2-1-1-1-3-3
tbl[19236,]
tbl <- tbl[-c(19236),]

cutoff_rng <- vector("numeric", length=35999)
accuracy_vec <-  vector("numeric", length=35999)
covrge_vec <- vector("numeric", length=35999)
nm_vec <- vector("character", length=35999)
cnt = 1
for (i in seq(1,5)){ # controls_formation
  for (j in seq(1,4)){ # has_metabolite
    for (k in seq(1,2)){ # inhibits
      for (m in seq(1,5)){ # is_not_substrate_of
        for (n in seq(1,4)){ # primary_metabolic_clearance_enzyme
          for (p in seq(1,3)){ # primary_total_clearance_enzyme
            for (q in seq(1,3)){ # primary_total_clearance_mechanism
              for (r in seq(1,5)){ # substrate_of
                #print(cnt)
                
                cutoff_rng[cnt] <- 1.0 / ((i+j+k+m+n+p+q+r) / 8.0)            
                nm <- paste("strategy-", i, "-", j, "-", k, "-", m, "-", n, "-", p, "-", q, "-", r, sep="")
                
                if (nm == "strategy-1-4-2-1-1-1-3-3")
                  next

                nm_vec[cnt] <- nm
                accuracy_vec[cnt] <- (tbl[tbl$strategy == nm,]$tp + tbl[tbl$strategy == nm,]$tn) / (tbl[tbl$strategy == nm,]$tp + tbl[tbl$strategy == nm,]$tn + tbl[tbl$strategy == nm,]$fp + tbl[tbl$strategy == nm,]$fn)
                covrge_vec[cnt] <- (tbl[tbl$strategy == nm,]$tp + tbl[tbl$strategy == nm,]$tn) / 48.0
                
                cnt = cnt + 1
              }
            }}}}}}}
  

roc_df <- data.frame(cbind(cutoff_rng, nm_vec, accuracy_vec, covrge_vec))
write.csv(roc_df, "DIKB-experiment-ROC-data-REVISED-03172009.csv")
# roc_df <- read.csv("DIKB-experiment-ROC-data-REVISED-03172009.csv")

x = roc_df$cutoff_rng
y = roc_df$accuracy_vec
z = roc_df$covrge_vec

plot(0:1, 0:1, type = "n", xlab="1.0 / (average LOE level)", ylab="")
points(x, y, col="blue")
points(x, z, pch=3)
abline(v=1, col="red")
legend(0.1,0.1, c("accuracy", "coverage"), pch=c(1,3), col=c("blue","black"), bty="n")

#points(1, 1, pch=17, col="green")

dev.copy2eps()

## question: how many belief criteria strategies did not produce FP or
## TN predictions?
tbl = read.delim("dikb-loe-experiments-REDO-06012008-results.tsv",na.strings =c("NA",""," "))
# we need to remove the first row because it is the evidence-board's
# belief criteria strategy. 
tbl <- tbl[-c(1),]

## We also need to throw out the bad data from one strategy that was
## incorrectly ran: strategy-1-4-2-1-1-1-3-3
tbl[19236,]
tbl <- tbl[-c(19236),]

no_FP <- subset(tbl, tbl$fp == 0 | tbl$tn == 0)
dim(no_FP)
# answer: 28,511
