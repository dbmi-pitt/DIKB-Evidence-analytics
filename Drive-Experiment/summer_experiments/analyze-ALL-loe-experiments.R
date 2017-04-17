# analyze-ALL-loe-experiments.R
# made by dr. richard boyce and modified by sam rosko
# last update: 2016-07-20

# start timer
stm = Sys.time()

# folder configuration
prfx = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/experiment_2"

## grab paths to the data for each strategy
con <- file(paste(prfx, "/paths-to-experiment-folders", sep=""), "r")
buf <- readLines(con)
close(con)
pths <- strsplit(buf, "\n")

## open a log file
con <- file("/media/scr25/DATA/drive-logs/analyze-ALL-loes.log", 'a')

## using sam rosko's validation set
tbl = read.delim(paste(prfx, "/scr25-validation-set.tsv", sep=""), na.strings = c("NA",""," "))

for(p_ctr in 1:length(pths)){
  sb_pth <- as.character(pths[p_ctr])
  
  val_set_ddis <- subset(tbl$Pceut.entity.combination, !(is.na(tbl$VALIDATION_SET_DDI)))
  val_set_non_ddis <- subset(tbl$Pceut.entity.combination, !(is.na(tbl$VALIDATION_SET_NON_DDI)))

  inf_rslts =  read.delim(paste(sb_pth, "/experiment-results-tab.tsv", sep=""), na.strings =  c("NA",""," "))
  cntr = 1
  for (pr in inf_rslts$PAIR)
  {
    #print(as.character(inf_rslts$PAIR[cntr]))
    if (!(is.na(inf_rslts$DDI_DIKB[cntr]))){
      tbl$DDI_DIKB[as.vector(tbl$Pceut.entity.combination) == inf_rslts$PAIR[cntr]] <- as.character(inf_rslts$DDI_DIKB[cntr])
    }
    if(!(is.na(inf_rslts$NON_DDI_DIKB[cntr]))){
      tbl$NON_DDI_DIKB[as.vector(tbl$Pceut.entity.combination) == inf_rslts$PAIR[cntr]] <- as.character(inf_rslts$NON_DDI_DIKB[cntr])
    }
    cntr = cntr + 1                              
  }
  dikb_set_ddis <- subset(tbl$Pceut.entity.combination, (!(is.na(tbl$DDI_DIKB))))
  tbl$DIKB_NON_DDI_PREDICTION[(is.na(tbl$DDI_DIKB)) & (!(is.na(tbl$NON_DDI_DIKB)))] <- TRUE
  dikb_set_non_ddis <- subset(tbl$Pceut.entity.combination, tbl$DIKB_NON_DDI_PREDICTION == TRUE)
  
  tbl$True_pos <- (!(is.na(tbl$DDI_DIKB))) & (tbl$VALIDATION_SET_DDI == TRUE)
  tbl$True_neg <- (tbl$DIKB_NON_DDI_PREDICTION == TRUE) & (tbl$VALIDATION_SET_NON_DDI == TRUE)
  tbl$False_pos <- (!(is.na(tbl$DDI_DIKB))) & (tbl$VALIDATION_SET_NON_DDI == TRUE)
  tbl$False_neg <- tbl$DIKB_NON_DDI_PREDICTION == TRUE & tbl$VALIDATION_SET_DDI == TRUE
  
  strat <- strsplit(sb_pth,"/")
  write.table(tbl, paste(sb_pth, "/experiment-2-", strat[[1]][length(strat[[1]])], "-RESULTS.tsv", sep=""), sep="\t", row.names=FALSE)
  
  val_set_unknown <- subset(tbl$Pceut.entity.combination, is.na(tbl$VALIDATION_SET_DDI) & is.na(tbl$VALIDATION_SET_NON_DDI))
  dikb_unknown <- subset(tbl$Pceut.entity.combination, is.na(tbl$DDI_DIKB) & is.na(tbl$DIKB_NON_DDI_PREDICTION))
  both_unknown <- subset(tbl$Pceut.entity.combination, is.na(tbl$DDI_DIKB) & is.na(tbl$DIKB_NON_DDI_PREDICTION) & is.na(tbl$VALIDATION_SET_DDI) & is.na(tbl$VALIDATION_SET_NON_DDI))
  val_only_unkown <- subset(tbl$Pceut.entity.combination, ((!(is.na(tbl$DDI_DIKB)) | (!(is.na(tbl$DIKB_NON_DDI_PREDICTION))))) & is.na(tbl$VALIDATION_SET_DDI) & is.na(tbl$VALIDATION_SET_NON_DDI))
  dikb_only_unkown <- subset(tbl$Pceut.entity.combination, is.na(tbl$DDI_DIKB) & is.na(tbl$DIKB_NON_DDI_PREDICTION) & ((!(is.na(tbl$VALIDATION_SET_DDI))) | (!(is.na(tbl$VALIDATION_SET_NON_DDI)))))
  
  tp <- length(subset(tbl$True_pos, tbl$True_pos == TRUE)) 
  fp <- length(subset(tbl$False_pos, tbl$False_pos == TRUE))
  tn <- length(subset(tbl$True_neg, tbl$True_neg == TRUE)) 
  fn <- length(subset(tbl$False_neg, tbl$False_neg == TRUE))
  
  ppv <- tp / (tp + fp) 
  sens <- tp / (tp + fn) 
  spec <- tn / (fp + tn) 
  f1 <- ((2 * ppv * sens) / (ppv + sens))
  
  rslt_m <- matrix(nrow=length(tbl$Pceut.entity.combination), ncol=2, dimnames=list(1:length(tbl$Pceut.entity.combination),c("VAL_SET","DIKB")))
  cntr = 1
  for (pr in tbl$Pceut.entity.combination){
    if (!(is.na(tbl$VALIDATION_SET_DDI[cntr]))){
      rslt_m[cntr, 1] <- 1
    }
    else if (!(is.na(tbl$VALIDATION_SET_NON_DDI[cntr]))){
      rslt_m[cntr, 1] <- 2
    }
    else {
      rslt_m[cntr, 1] <- 3
    }
    
    if (!(is.na(tbl$DDI_DIKB[cntr]))){
      rslt_m[cntr, 2] <- 1
    }
    else if (!(is.na(tbl$DIKB_NON_DDI_PREDICTION[cntr]))){
      rslt_m[cntr, 2] <- 2
    }
    else{
      rslt_m[cntr, 2] <- 3
    }
    
    cntr = cntr + 1
  }
  library(psy)
  kap <- ckappa(rslt_m) 
  
  hdr <- paste("strategy",
               "num-pairs",
               "DIKB-ddi",
               "DIKB-ddi-freq",
               "DIKB-non-DDI",
               "DIKB-non-DDI-freq",
               "DIKB-unknown",
               "DIKB-unknown-freq",
               "both-unkown",
               "val-set-only-unkown",
               "DIKB-only-unknown",
               "tp",
               "fp",
               "tn",
               "fn",
               "ppv",
               "sens",
               "spec",
               "f1",
               "kappa",
               "num-val-set-DDIs",
               "num-val-set-NON-ddis",
               "num-val-set-unknown",
               sep ="\t")
  out_st <- paste(strat[[1]][length(strat[[1]])],
                  length(tbl$Pceut.entity.combination),
                  length(dikb_set_ddis),
                  length(dikb_set_ddis) / length(tbl$Pceut.entity.combination),
                  length(dikb_set_non_ddis),
                  length(dikb_set_non_ddis) / length(tbl$Pceut.entity.combination),
                  length(dikb_unknown),
                  length(dikb_unknown) / length(tbl$Pceut.entity.combination),
                  length(both_unknown),
                  length(val_only_unkown),
                  length(dikb_only_unkown),
                  tp,
                  fp,
                  tn,
                  fn,
                  ppv,
                  sens,
                  spec,
                  f1,
                  kap$kappa,
                  length(subset(tbl$VALIDATION_SET_DDI, tbl$VALIDATION_SET_DDI == TRUE)),
                  length(subset(tbl$VALIDATION_SET_NON_DDI, tbl$VALIDATION_SET_NON_DDI == TRUE)),
                  length(val_set_unknown),
                  sep="\t")
  
  anl_out <- paste(sb_pth, "/test-experiment-", strat[[1]][length(strat[[1]])], "-ANALYSIS.tsv", sep="")
  write(paste(hdr, out_st, sep="\n"),  anl_out)
  writeLines(paste(p_ctr, ": wrote analysis to ", anl_out), con)

  lcl_rslts <- paste(prfx, "/dikb-loe-experiments-scr25-results-colloquium.tsv", sep="")
  write(out_st, lcl_rslts,  append = TRUE)
  writeLines(paste(p_ctr, ": appended results of analysis on ", strat[[1]][length(strat[[1]])], " to ", lcl_rslts), con)
  print(Sys.time() - stm)
}
close(con)

## final timer
print(Sys.time() - stm)
