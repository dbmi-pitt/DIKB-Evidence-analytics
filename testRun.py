import os,sys, string, cgi
from time import time, strftime, localtime

import sys

from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.ExportAssertions import *

##### must set log level, can be changed
os.environ["DIKB_LOG_LEVEL"] = "2" 

## current time and date
timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))

## Customize as you see fit
ident = "".join(["DIKB evidence July 27th 2016: ", timestamp])

ev = EvidenceBase("evidence",ident)
ev.unpickleKB("Drive-Experiment/dikb-pickles/ev-test.pickle")

dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("Drive-Experiment/dikb-pickles/dikb-test.pickle")
ev.renotifyObservers()

##assess evidence using some belief criteria and test exporting to the database 
reset_evidence_rating(ev, dikb) # reset the internal finit state
                                # machine or you will get unexpected
                                # behavior

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

exportAssertions(ev, dikb, "./Drive-Experiment/sandbox/assertions.lisp")
assessBeliefCriteria(dikb, ev, "./Drive-Experiment/sandbox/changing_assumptions.lisp")
