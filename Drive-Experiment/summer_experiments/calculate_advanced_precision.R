# calculate_advanced_precision.R
# made by by samuel rosko
# last update: 2017-03-13

# start timer
stm = Sys.time()

# folder configuration
prfx = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/experiment_3"

## grab paths to the data for each strategy
con <- file(paste(prfx, "/paths-to-experiment-folders", sep=""), "r")
buf <- readLines(con)
close(con)
pths <- strsplit(buf, "\n")
## grab ordering of belief criteria strategies
con2 <- file(paste(prfx, "/paths-to-experiment-folders-suffixes", sep=""), "r")
buf2 <- readLines(con2)
close(con2)
bcs <- strsplit(buf2, "\n")

rslts_tbl = read.table(paste(prfx, "/dikb-loe-experiments-scr25-results.tsv", sep=""), sep = ",")
rslts_tbl[,"average_precision"] = NA

for(p_ctr in 1:length(pths)){
  sb_pth <- as.character(pths[p_ctr])

  tbl = read.delim(paste(sb_pth, "/experiment-2-", buf2[p_ctr], "-RESULTS.tsv", sep=""), na.strings = c("NA",""," "))

  val_set_ddis_tbl <- subset(tbl, !(is.na(tbl$VALIDATION_SET_DDI)))
  val_set_non_ddis_tbl <- subset(tbl, !(is.na(tbl$VALIDATION_SET_NON_DDI)))

  count = 0
  prec_sum = 0

  for(ddi in 1:nrow(val_set_ddis_tbl)){  
    if( val_set_ddis_tbl[ddi, 6] == TRUE ){
     count = count + 1
     prec_sum = prec_sum + (count/ddi)
   }
  }
  rslts_tbl[p_ctr, "average_precision"] = (prec_sum / 102)
  print(p_ctr)
  print(Sys.time() - stm)
}

write.table(rslts_tbl, file=paste(prfx,"/test.tsv", sep=""), quote=FALSE, sep='\t', row.names = FALSE, col.names = FALSE)

## final timer
print(Sys.time() - stm)
