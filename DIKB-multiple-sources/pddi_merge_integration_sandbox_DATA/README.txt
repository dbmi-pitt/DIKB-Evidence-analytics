The data and log files in this folder are from an analysis done on
3/5/15 to test the effect of integrating the merged PDDI dataset into
the Bui NLP pipeline.

The merged PDDI data was downloaded from: http://purl.org/net/drug-interaction-knowledge-base/PDDI-data-merged-non-conservative

NOTE: The original dataset is hosted in an SQL Server database from
which the file was created in the Fall of 2014 to support a different
analysis. However, we fould issues with the downloaded dataset that
seemed to prevent KEGG and Crediblemeds records from being loaded into
a mysql instance which was needed for the test (because it was done on
a linux machine). We decided to address the Crediblemeds issue but
just not include Kegg data in the test. We also excluded SemMedDB and
TWOSIDES. The exclusion of these three is justified because they are
each non-validated products of automated processes.


To fix Crediblemeds, we got the original Crediblemeds from a separate extract from the SQL Server database:
grep CredibleMeds ./CombinedDatasetNotConservativeAllsources-DUMP-WITH-FIXED-CREDIBLE-MEDS.csv > /tmp/CombinedDatasetNotConservative-JUST-CREDIBLEMEDS.csv

# drop a column not used
cat /tmp/CombinedDatasetNotConservative-JUST-CREDIBLEMEDS.csv | cut -f1-27 > ./CombinedDatasetNotConservative-JUST-CREDIBLEMEDS.csv

# pull out TWOSIDES and Crediblemeds
grep "DIKB\|Drugbank\|NDF-RT\|Kegg\|DDI-Corpus-2011\|DDI-Corpus-2013\|NLM-Corpus\|PK-Corpus\|ONC-HighPriority\|ONC-NonInteruptive\|OSCAR\|SemMedDB" CombinedDatasetNotConservative.csv > CombinedDatasetNotConservative-NO-TWOSIDES.csv

# add back in the credible meds data
cat CombinedDatasetNotConservative-JUST-CREDIBLEMEDS.csv >> CombinedDatasetNotConservative-NO-TWOSIDES.csv

# the data table schema 
CREATE TABLE `DDI_CONS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `drug1` varchar(200) COLLATE utf8_bin NOT NULL,
  `object` varchar(200) COLLATE utf8_bin NOT NULL,
  `drug2` varchar(200) COLLATE utf8_bin NOT NULL,
  `precipitant` varchar(200) COLLATE utf8_bin NOT NULL,
  `certainty` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `contraindication` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `dateAdded` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `ddiPkEffect` varchar(500) COLLATE utf8_bin DEFAULT NULL,
  `ddiPkMechanism` varchar(1000) COLLATE utf8_bin DEFAULT NULL,
  `effectConcept` varchar(1000) COLLATE utf8_bin DEFAULT NULL,
  `homepage` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `label` varchar(2000) COLLATE utf8_bin DEFAULT NULL,
  `numericVal` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `objectUri` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `pathway` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `precaution` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `precipUri` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `severity` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `uri` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `whoAnnotated` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `source` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `ddiType` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `evidence` varchar(5000) COLLATE utf8_bin DEFAULT NULL,
  `evidenceSource` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `evidenceStatement` varchar(5000) COLLATE utf8_bin DEFAULT NULL,
  `researchStatementLabel` varchar(1000) COLLATE utf8_bin DEFAULT NULL,
  `researchStatement` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

# loading statement
LOAD DATA LOCAL INFILE '/home/boycerd/DI_DIR/DIKB-Evidence-analytics/DIKB-multiple-sources/sandbox/CombinedDatasetNotConservative-NO-TWOSIDES.csv'
INTO TABLE DDI_CONS
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(drug1,object,drug2,precipitant,certainty,contraindication,dateAdded,ddiPkEffect,ddiPkMechanism,effectConcept,homepage,label,numericVal,objectUri,pathway,precaution,precipUri,severity,uri,whoAnnotated,source,ddiType,evidence,evidenceSource,evidenceStatement,researchStatementLabel,researchStatement);
