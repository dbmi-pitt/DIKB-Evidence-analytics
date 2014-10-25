# quickstartdikb.py
#
# 10/23/2014
#
# a quick-start script to load the DIKB knowledge base and evidence
# base from the SQL database

import os,sys, string, cgi
from time import time, strftime, localtime

import sys
sys.path = sys.path + ['./dikb-relational-to-object-mappings']

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.ExportAssertions import *

## current time and date
timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))

## Customize as you see fit
ident = "".join(["Current SQL DIKB evidence : ", timestamp])

## CODE TO RELOAD THE EB; SUFFICIENT FOR ADDING INFORMATION TO THE
## EB. IF YOU NEED TO ADD OBJECTS TO THE KB OR ACCESS EVIDENCE FROM
## THE DIKB'S DRUG MODEL, THEN USE THE CODE THAT RENOTIFIES OBSERVERS
ev = load_ev_from_db(ident)

## CODE TO RELOAD THE KB AND EB AND RESET ALL OBSERVERS; NOT NECESSARY
## IF ONLY ADDING INFORMATION TO THE EB 
#dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/dikb.pickle")
ev.renotifyObservers()

# NOTE: A test that this worked properly would be to compare
# dikb.objects['bupropion'].increases_auc.evidence with
# ev.objects['bupropion_increases_auc_desipramine'] to confirm that
# the two objects are the exactly the same in memory. For example,
#>>> dikb.objects['bupropion'].increases_auc.evidence
#[<DIKB.EvidenceModel.ContValAssertion object at 0x7fb4e76e2710>]
#>>> ev.objects['bupropion_increases_auc_desipramine']
#<DIKB.EvidenceModel.ContValAssertion object at 0x7fb4e76e2710>

for e,v in ev.objects.iteritems():
    # TODO: this bit of code fixes a bug whereby all assertions are
    # assumed true by default because the data value (which comes from
    # an SQL DIKB instance) is a string rather than a boolean. Make
    # the assert_by_default entry of the Assertion table a boolean and
    # change the values accordingly.
    if v.assert_by_default == '0':
        v.assert_by_default = False
    else:
        v.assert_by_default = True
    v.ready_for_classification = True

exportAssertions(ev, dikb, "/tmp/assertions.lisp")
assessBeliefCriteria(dikb, ev, "/tmp/changing_assumptions.lisp")


