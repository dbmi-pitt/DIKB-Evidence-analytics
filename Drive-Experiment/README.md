##### ReadMe for Drive-Experiment Update Process
##### Author : Sam Rosko
##### Last Update : 2015-07-28

### Update the entities/evidence in the DIKB

(1) Run the "dikb-update.py" file

-- This file first loads the old evidence-base from the SQL server and unpickles the most recent version of the knowledge-base (from 2012-03-05)
-- The file then adds all the new drugs, chemicals, metabolites, and enzymes to the DIKB through a series of for loops
-- The file then removes all FDA 2006 evidence items and adds all the FDA 2012 evidence items
-- The file then renotifies observers, and repickles both the evidence-base and knowledge-base to the "dikb-pickles/" directory, located in this folder

(2) Run "create-SQL-DIKB-from-pickle.py", found in the "dikb-relational-to-object-mappings/" directory

-- This file takes the freshly pickled evidence-base and knowledge-bases and creates an sqlite3 file for them, named test.db
-- This file should be converted from ".db" format to ".sql" format so that it can be loaded into and browsed in "mysql-workbench"

(3) $ sqlite3 test.db dump > dikb-test.sql

-- This uses sqlite3 to convert the updated database to the correct format

(4) This dump must be adapted so that it can be loaded by MySQL

-- The changes that have to be made as as follows:

  - Replace " (double-quotes) with ` (grave accent)
  - Remove "BEGIN TRANSACTION;" "COMMIT;", and lines related to "sqlite_sequence"

(5) $ mysql --local-infile -u root -p (pw)

-- "--local-infile" is necessary in order to be able to load a file once in MySQL

(6) $ load data local infile '/path' into dikbEvidenceTest

-- This will load the new table, and you can browse it using either MySQL or MySQL-Workbench

