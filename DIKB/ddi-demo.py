## A simple demonstration

from DIKB import *
from DrugModel import *
from EvidenceModel import *
from ExportAssertions import *

ev = EvidenceBase("evidence","123")
dikb = DIKB("dikb","123", ev)
dikb.unpickleKB("../var/DIKB/dikb.pickle")
ev.unpickleKB("../var/evidence-base/ev.pickle")
ev.renotifyObservers()

reset_evidence_rating(ev,dikb)

##set evidence to ./switch_3 ,the weakest level
exportAssertions(dikb, ev, "data/assertions.lisp")
##should make many assertions including (assume! '(inhibits 'fluvastatin 'cyp2c9) '("http://localhost:8080/src/viewData.rpy#fluvastatin_inhibits_cyp2c9"))

##set evidence to ./switch_2 or ./switch_1, much stronger
exportAssertions(dikb, ev, "data/assertions.lisp", "True")
## should cause (retract! '(inhibits 'fluvastatin 'cyp2c9) '("http://localhost:8080/src/viewData.rpy#fluvastatin_inhibits_cyp2c9"))

##set evidence back to ./switch_3
exportAssertions(dikb, ev, "data/assertions.lisp", "True")
## back to (assume! '(inhibits 'fluvastatin 'cyp2c9) '("http://localhost:8080/src/viewData.rpy#fluvastatin_inhibits_cyp2c9"))

##ev.pickleKB("../var/evidence-base/ev.pickle")







# ## should evaluate 'True' because evidence types match rules
# ev.objects['simvastatin_substrate_of_cyp3a4'].ready_for_classification = True
# #ev.objects['simvastatin_level_of_first_pass_more_than_half'].assumptions.value = ['bogus_test_assumption_2','bogus_test_assumption_1']
# ev.objects['simvastatin_level_of_first_pass_more_than_half'].ready_for_classification = True
# ev.objects['simvastatin_primary_clearance_enzyme_cyp3a4'].ready_for_classification = True
# ev.objects['simvastatin_primary_clearance_mechanism_metabolism'].ready_for_classification = True

# ev.objects['fluvastatin_primary_clearance_mechanism_metabolism'].ready_for_classification = True
# ev.objects['fluvastatin_substrate_of_cyp3a4'].ready_for_classification = True

# ev.objects['fluvastatin_substrate_of_cyp2c8'].ready_for_classification = True
# ev.objects['fluvastatin_substrate_of_cyp2c9'].ready_for_classification = True

# ## should evaluate and be useful for testing basic inference
# ev.objects['diltiazem_inhibits_cyp3a4'].assumptions.value = ['sufficient_concentration_to_inhibit','saturable_concentration']
# ev.objects['diltiazem_inhibits_cyp3a4'].ready_for_classification = True

# ##should not evaulate due to meeting both for and against rules
# ev.objects['simvastatin_inhibits_cyp3a4'].assumptions.value = ['sufficient_concentration_to_inhibit','saturable_concentration']
# ev.objects['simvastatin_inhibits_cyp3a4'].ready_for_classification = True

# ## should not evaluate does to not meeting any of the rules
# ev.objects['simvastatin_substrate_of_cyp1a2'].ready_for_classification = True

# os.putenv("DIKB_LOG_LEVEL","3")
# exportAssertions(dikb, "data/assertions.lisp")
# os.putenv("DIKB_LOG_LEVEL","1")
