# test_dikb.py
#
# 03062012
#
# a one off script to load evidence items present in a pickle from
# 2010 that never made it into the SQL dikb and add them to a pickle
# containing the current items so they can be loaded into the database
# using a different script

import os,sys, string, cgi
from time import time, strftime, localtime

import sys
sys.path = sys.path + ['.']

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *

timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
ident = "".join(["Rob's missing DIKB entries : ", timestamp])

dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
dikb.unpickleKB("../database/dikb-pickle-with-Robs-entries-fall-2010/dikb.pickle")
        
ev = EvidenceBase("evidence",ident)
ev.unpickleKB("../database/dikb-pickle-with-Robs-entries-fall-2010/ev.pickle")

ident = "".join(["Current SQL DIKB evidence : ", timestamp])
sqlEv = load_ev_from_db(ident)

# how many new assertions?
for k in ev.objects.keys():
    if not sqlEv.objects.has_key(k):
        print "%s not present in SQL DIKB" % k 

# new evidence items
# 1
nev = ev.objects["fluoxetine_increases_auc_alprazolam"].evidence_for[0]
sqlEv.objects["fluoxetine_increases_auc_alprazolam"].evidence_for.append(nev)

# 2
nev = ev.objects["cimetidine_increases_auc_venlafaxine"].evidence_for[0]
sqlEv.objects["cimetidine_increases_auc_venlafaxine"].evidence_for.append(nev)

# any new drug entities that we need to create?
for k,v in ev.objects.iteritems():
    if v.slot == "increases_auc":
        obj = v.object
        if not dikb.objects.has_key(obj):
            print obj

        val = v.value
        if not dikb.objects.has_key(val):
            print val

## entering new assertions
for k in ev.objects.keys():
    if not sqlEv.objects.has_key(k):
        print "Inserting %s into SQL evidence-base" % k 
        missingAsrt = ev.objects[k]
        sqlEv.addAssertion(missingAsrt)


# save evidence-base and DIKB
dikb.pickleKB("../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/dikb.pickle")
sqlEv.pickleKB("../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/ev.pickle")
