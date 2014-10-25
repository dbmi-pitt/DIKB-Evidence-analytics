import re, string

from HTMLcolors import *
from HTMLgen import *

import sys
sys.path = sys.path + ['../']
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.DIKB_Utils import *
from DIKB.TranslationRules import *
from DIKB.ExportAssertions import *

version = getVersion('..')
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)
datadir = '../data'
htmldir = '../html'

def createAssertionPage(ev):
    id_d = {}
    l = []
    for n,v in ev.objects.iteritems():
        id_d[v._id] = v._name
    
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Results of Inference Over the Current Drug Interaction Knowledge Base'
    try:
        f = open(os.path.join(datadir,"inference-results"))
    except IOError, err:
        error("".join(["Could not find inference results file: ", os.path.join(datadir,"inference-results")]))

    t = f.read()
    f.close()

    reg = re.compile("(ASSERTION_[0-9]+),")
    mtch_l = reg.findall(t)
    for mtch in mtch_l:
        t = t.replace(mtch, '''<A TARGET="new" HREF="./%s.html">%s</A>''' % (id_d[mtch.lower()], id_d[mtch.lower()]))
    t_s = t.split('<BR>')
    t_s.sort(reverse=True)
    t = "".join(t_s)
            
    doc.append('''<TABLE  BORDER="0" WIDTH="100%" CELLPADDING="15" CELLSPACING="1"''')
    doc.append(t)
    doc.append('''</TABLE>''')  
    doc.write(os.path.join(htmldir,"inference-results-page.html"))


#### STEP 1: loading databases
ev = EvidenceBase("evidence","123")
dikb = DIKB("dikb","123", ev)
dikb.unpickleKB("../var/DIKB/dikb.pickle")
ev.unpickleKB("../var/evidence-base/ev.pickle")

for e,v in ev.objects.iteritems():
    v.ready_for_classification = True

exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

## STEP 2: run (simple-dikb-rule-engine) in one of the files coding a
## JTMS in the src/lisp/jtms folder. NOTE: there are multiple JTMS
## files, test-dissertation-dikb.lisp holds the JTMS used for my
## dissertation and UPIA-dikb-jtms.lisp holds the JTMS used for the
## University of Pittsburgh Institute on Aging Pilot grant (2009).
createAssertionPage(ev)
## STEP 3: look at inference-results-page.html diltiazem-inhibits assertions

ev.objects['triazolam_primary_total_clearance_enzyme_cyp3a4'].assert_by_default = False
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")
## STEP 4: run (update-inference) in jtms
createAssertionPage(ev)
## STEP 5: look at inference-results.html diltiazem-inhibits assertions

ev.objects['triazolam_primary_total_clearance_enzyme_cyp3a4'].assert_by_default = True
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")
## STEP 6: run (update-inference) in jtms
createAssertionPage(ev)
## STEP 7: look at inference-results.html diltiazem-inhibits assertions
