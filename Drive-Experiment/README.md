##### ReadMe for Drive-Experiment Update Process
##### Author : Sam Rosko
##### Last Update : 2015-08-07

### Update the entities/evidence in the DIKB, run DDI prediction engine

(1) Run the "dikb-update.py" file

-- This file first loads the old evidence-base from the SQL server and unpickles the most recent version of the knowledge-base (from 2012-03-05)
-- The file then adds all the new drugs, chemicals, metabolites, and enzymes to the DIKB through a series of for loops
-- The file then removes all FDA 2006 evidence items and adds all the FDA 2012 evidence items
-- The file then renotifies observers, and repickles both the evidence-base and knowledge-base to the "dikb-pickles/" directory, located in this folder

(2) Modify the symbolic link to the 'levels-of-evidence' file of your choice in the '/data/' folder

-- EX: $ ln -s levels-of-evidence-most-rigorous-REVISED-07302015 levels-of-evidence
-- Currently, levels-of-evidence-most-rigorous-REVISED-07302015 is being used
-- Make sure that all the asseriton types that are used in the DIKB are included in your 'levels-of-evidence' file, if not, an error may occur in step 3

(3) Run "create-SQL-DIKB-from-pickle.py", found in the "dikb-relational-to-object-mappings/" directory

-- This file takes the freshly pickled evidence-base and knowledge-bases and creates an sqlite3 file for them, named test.db
-- This file should be eventually be converted from ".db" format to ".sql" format so that it can be loaded into and browsed in "mysql-workbench"
-- If this runs into an error in the final step, that is likely because of an issue with your 'levels-of-evidence', see step (2) for more details

(4) Follow the steps found in the overall DIKB-Evidence-analytics README for loading DDI predictions... I will summarize them here:

(4a) Edit the (assertions.lisp) and (changing_assumptions.lisp) files produced by the last step

-- For these files to work properly in lisp, all commas and parenthesis in drug, chemical, enzyme, or metabolite names must be backquoted
-- EXAMPLE: 4-(4-chlorophenyl)-4-hydroxypiperidine should be 4-\(4-chlorophenyl\)-4-hydroxypiperidine

(4b) Make sure the symbolic links in the "/jtms/" directory are pointing the the files you just made... they should be located in "/Drive-Experiment"

(4c) Open a SLIME interface in EMACS24 or any other inferior list mode that uses Common Lisp

-- Make sure you are in the "/jtms/" directory
-- $ (load "load")
-- $ (simple-dikb-rule-engine)
-- If this throws an error, check to make sure you did step (4a) appropriately

(4d) For each drug class, run the function call 'GET-PKI-TO-TSV'

-- Here is a test drug-class list, including only those classes which were tested in the original DIKB, but with updated drug lists

(setf drug-class-a-list '((statins . (SIMVASTATIN LOVASTATIN ROSUVASTATIN PRAVASTATIN FLUVASTATIN ATORVASTATIN PITAVASTATIN))
   (antidepressants . (BUPROPION CITALOPRAM R-CITALOPRAM ESCITALOPRAM FLUOXETINE FLUVOXAMINE PAROXETINE SERTRALINE DESVENLAFAXINE DULOXETINE VENLAFAXINE TRAZODONE MIRTAZAPINE NEFAZODONE DESIPRAMINE))
   (sedative-hypnotics . (ESZOPICLONE ZALEPLON ZOLPIDEM))
   (atypical-antipsych . (ARIPIPRAZOLE CLOZAPINE OLANZAPINE PALIPERIDONE QUETIAPINE RISPERIDONE ZIPRASIDONE ILOPERIDONE ASENAPINE LURASIDONE RESERPINE))
   (typical-antipsych . (DROPERIDOL HALOPERIDOL REDUCED-HALOPERIDOL PIMOZIDE THIOTHIXENE CHLORPROMAZINE FLUPHENAZINE PERPHENAZINE THIORIDAZINE TRIFLUOPERAZINE))
   (short-acting-bzd . (ALPRAZOLAM TRIAZOLAM CLOBAZAM))))

$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'statins)
$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'antidepressants)
$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'sedative-hypnotics)
$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'atypical-antipsych)
$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'typical-antipsych)
$ (GET-PKI-TO-TSV PKI-1 "PKI-1" "fourth-tier" 'short-acting-bzd)

-- All of the output from this step should be copied, cleaned up (all the quotes removed), and loaded into LibreOffice as a .tsv file
-- Use LibreOffice to make all of the drug names lowercase, and export as a .csv file
-- The .csv file should be named "DDI-predictions.csv", this file will be used in step 9

(5) $ sqlite3 test.db .dump > dikb-test.sql

-- This uses sqlite3 to convert the updated database to the correct format

(6) This dump must be adapted so that it can be loaded by MySQL

-- The changes that have to be made as as follows:

  - Replace " (double-quotes) with ` (grave accent)
  - Remove "BEGIN TRANSACTION;" "COMMIT;", and lines related to "sqlite_sequence"

(7) $ mysql --local-infile -u root -p (pw)

-- You should be in the "/dikb-relational-to-object-mappings" folder
-- "--local-infile" is necessary in order to be able to load a file once in MySQL

(8) If you have a test database set up, use that, if not, a new one:

-- $ create database dikbEvidenceTest;
-- $ use dikbEvidenceTest; 

(8) $ source dikb-test.sql;

-- This will load the new tables, and you can browse it using either MySQL or MySQL-Workbench
-- However, this does not include the generated DDI-Prediction and Observation tables, those must be added seperately

(9) Add DDI-Predictions

-- Open MySQL as described above while in the "/Drive-Experiment/sandbox" directory, run the following command:

$ CREATE TABLE `DDIPredictions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `OBJECT` varchar(100) DEFAULT NULL,
  `PRECIPITANT` varchar(100) DEFAULT NULL,
  `ENZYME` varchar(100) DEFAULT NULL,
  `LEVEL` varchar(10) DEFAULT NULL,
  `TIER` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- This creates the table, now to enter the data: 

$ LOAD DATA LOCAL INFILE './DDI-predictions.csv' INTO TABLE DDIPredictions FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (OBJECT, PRECIPITANT, ENZYME, LEVEL, TIER); 

(10) Add DDI-Observations

$ CREATE TABLE `DDIObservations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `precipitant` varchar(100) DEFAULT NULL,
  `object` varchar(100) DEFAULT NULL,
  `assertionId` int(11), 
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- This creates the table, now to enter the data on increases_auc assertions that are supported with evidence:

$ INSERT INTO `DDIObservations` (`precipitant`, `object`, `assertionId`) SELECT `Assertions`.`object`,  `Assertions`.`value`, `Assertions`.`id` FROM `Assertions` WHERE (`Assertions`.`slot` = "increases_auc" AND `Assertions`.`evidence_for` IS NOT NULL);