# Description - Sam Rosko's File to Update the DIKB
# Last Update - 2016-03-29

import os,sys, string, cgi
from time import time, strftime, localtime

import sys
sys.path = sys.path + ['../dikb-relational-to-object-mappings']

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.ExportAssertions import *

timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))

ident = "".join(["Current SQL DIKB evidence : ", timestamp])

### LOAD LATEST EV-BASE AND KB

ev = load_ev_from_db(ident)

dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("dikb-pickles/dikb-03052012.pickle")

### UPDATE ENTITY LIST

for i in ["acyclovir", "aliskiren", "allopurinol", "ambrisentan", "armodafinil", "atrasentan", "azithromycin", "bicalutamide", "boceprevir", "clobazam", "colchicine", "conivaptan", "crizotinib",  "dabigatran", "darifenacin", "dihydroergotamine", "dronedarone", "eltrombopag", "esomeprazole", "etravirine", "everolimus", "ezetimibe", "famotidine", "febuxostat", "fexofenadine", "fluticasone", "hydralazine", "lurasidone", "maraviroc", "melatonin", "nebivolol", "oxandrolone", "pazopanib", "phenylpropanolamine", "pitavastatin", "ramelteon", "ranitidine", "rifampin", "saxagliptin", "sirolimus", "sitagliptin", "telaprevir", "ticagrelor", "tigecycline", "tizanidine", "tolvaptan", "topotecan", "vemurafenib", "irinotecan", "tacrolimus", "talinolol", "dabigatran-etexilate"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	d = Drug(i)
	dikb.putObject(d)

for i in ["simvastatin-acid"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	m = Metabolite(i)
	dikb.putObject(m)
	
for i in ["p-glycoprotein", "oatp1b1", "oatp1b3"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	e = Enzyme(i)
	dikb.putObject(e)

### REMOVE ALL INFO FROM FDA 2006 GUIDELINES

for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            v.evidence_for.remove(it)
            #v.assert_by_default = False
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            v.evidence_against.remove(it)
            #v.assert_by_default = False

### REMOVE ALL ASSERTIONS THAT ARE UNSUPPORTED

delete_list = []

for e,v in ev.objects.iteritems():
	if len(v.evidence_for) == 0 and len(v.evidence_against) == 0:
		delete_list.append(v)

for assertion in delete_list:
        ev.deleteAssertion(assertion)

### ADD FDA 2012 EVIDENCE ITEMS

###########################################################
################ IN VIVO CYP INHIBITORS ###################
###########################################################

###### CYP1A2 inhibitor entries
for elt in ["ciprofloxacin", "fluvoxamine"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["methoxsalen", "mexiletine", "phenylpropanolamine", "vemurafenib", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["acyclovir", "allopurinol", "caffeine", "cimetidine", "disulfiram", "famotidine", "norfloxacin", "propafenone", "propranolol", "terbinafine", "ticlopidine", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2B6 "inhibitor" entries
for elt in ["clopidogrel", "ticlopidine", "prasugrel"]:
    a = Assertion(elt, "inhibits", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2B6. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C8 "inhibitor" entries
a = Assertion("gemfibrozil", "inhibits", "cyp2c8")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C8. Gemfibrozil also inhibits OATP1B1. For more information, see Table 3 on page 41, footnote 6 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###### CYP2C9 "inhibitor" entries
for elt in ["amiodarone", "fluconazole", "miconazole", "oxandrolone"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["capecitabine", "cotrimoxazole", "etravirine", "fluvastatin", "fluvoxamine", "metronidazole", "sulfinpyrazone", "tigecycline", "voriconazole", "zafirlukast"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C19 "inhibitor" entries
a = Assertion("fluconazole", "inhibits", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19 based on the AUC ratio of omeprazole, which is also metabolized by CYP3A. For more information, see Table 3 on page 41, footnote 7 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("fluvoxamine", "inhibits", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Fluvoxamine strongly inhibits CYP1A2 and CYP2C19, but it also inhibits CYP2C8/CYP2C9 and CYP3A. For more information, see Table 3 on page 41, footnote 8 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("ticlopidine", "inhibits", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Ticlopidine strongly inhibits CYP2C19, but it also inhibits CYP3A, CYP2B6, and CYP1A2. For more information, see Table 3 on page 41, footnote 9 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["esomeprazole", "fluoxetine", "omeprazole", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["armodafinil", "cimetidine", "etravirine", "felbamate", "ketoconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP3A4 "inhibitor" entries
for elt in ["boceprevir", "clarithromycin", "conivaptan", "indinavir", "itraconazole", "ketoconazole", "nefazodone", "nelfinavir", "posaconazole", "telaprevir", "telithromycin", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A4. For more information, see Table 3 on pages 41/42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amprenavir", "aprepitant", "ciprofloxacin", "crizotinib", "diltiazem", "erythromycin", "fluconazole", "fosamprenavir", "imatinib", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alprazolam", "amiodarone", "amlodipine", "atorvastatin", "bicalutamide", "cilostazol", "cimetidine", "cyclosporine", "fluoxetine", "fluvoxamine", "isoniazid", "lapatinib", "nilotinib", "pazopanib", "ranitidine", "ranolazine", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 "inhibitor" entries
for elt in ["bupropion", "fluoxetine", "paroxetine", "quinidine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["cinacalcet", "duloxetine", "terbinafine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amiodarone", "celecoxib", "clobazam", "cimetidine", "desvenlafaxine", "diltiazem", "diphenhydramine",  "febuxostat", "gefitinib", "hydralazine", "hydroxychloroquine", "imatinib", "methadone", "pazopanib", "propafenone", "ranitidine", "sertraline", "telithromycin", "verapamil", "vemurafenib"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
#### temporarily removed "escitalopram"

###########################################################
################ IN VIVO CYP SUBSTRATES ###################
###########################################################

###### CYP1A2 substrate entries
for elt in ["alosetron", "caffeine", "duloxetine", "melatonin", "ramelteon", "tacrine", "tizanidine"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP1A2. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["theophylline", "tizanidine"]:
    a = Assertion(elt, "substrate_of", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP1A2 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2B6 substrate entries
for elt in ["bupropion", "efavirenz"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2B6. The AUC of this compound was not increased by 5-fold or more with a CYP2B6 inhibitor, but it represents the most sensitive substrate studied with available inhibitors evaluated to date. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C8 substrates
a = Assertion("repaglinide", "primary_total_clearance_enzyme", "cyp2c8")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C8. Repaglinide is also a substrate for OATP1B1, and it is only suitable as a CYP2C8 substrate if the inhibition of OATP1B1 by the investigational drug has been ruled out. For more information, see Table 5 on page 44, footnote 5 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("paclitaxel", "substrate_of", "cyp2c8")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C8 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C9 substrates
a = Assertion("celecoxib", "primary_total_clearance_enzyme", "cyp2c9")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C9. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["warfarin", "phenytoin"]:
    a = Assertion(elt, "substrate_of", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C9 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C19 substrates
for elt in ["lansoprazole", "omeprazole", "S-mephenytoin"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C19. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("S-mephenytoin", "substrate_of", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C19 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP3A4 substrates
for elt in ["alfentanil", "aprepitant", "budesonide", "buspirone", "conivaptan", "darifenacin", "dasatinib", "dronedarone", "eletriptan", "eplerenone", "everolimus", "felodipine", "indinavir", "fluticasone", "lovastatin", "lurasidone", "maraviroc", "midazolam", "nisoldipine", "quetiapine", "sildenafil", "simvastatin", "sirolimus", "tolvaptan", "triazolam", "vardenafil", "ticagrelor"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP3A4. Because a number of CYP3A substrates (e.g. maraviroc) are also substrates of p-glycoprotein, the observed increase in exposure could be due to inhibition of both CYP3A and p-glycoprotein. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alfentanil", "cyclosporine", "dihydroergotamine", "ergotamine", "fentanyl", "pimozide", "quinidine", "sirolimus", "tacrolimus"]:
    a = Assertion(elt, "substrate_of", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP3A4 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 substrate entries
for elt in ["atomoxetine", "desipramine", "dextromethorphan", "metoprolol", "nebivolol", "perphenazine", "tolterodine", "venlafaxine"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2D6. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("thioridazine", "substrate_of", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pimozide", "substrate_of", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
############### IN VIVO TRANSPORT PROTEINS  ###############
###########################################################

for elt in ["amiodarone", "captopril", "carvedilol", "clarithromycin", "conivaptan", "cyclosporine", "diltiazem", "dronedarone", "felodipine", "itraconazole", "quinidine", "ranolazine", "ticagrelor", "verapamil"]:
    a = Assertion(elt, "inhibits", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in digoxin AUC. For more information, see Table 6 on page 49, footnote 2 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["azithromycin", "ketoconazole"]:
    a = Assertion(elt, "inhibits", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in fexofenadine AUC. For more information, see Table 6 on page 49, footnote 4 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("erythromycin", "inhibits", "p-glycoprotein")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in talinolol AUC. For more information, see Table 6 on page 49, footnote 5 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["aliskiren", "ambrisentan", "colchicine", "dabigatran", "dabigatran-etexilate", "digoxin", "everolimus", "fexofenadine", "imatinib", "lapatinib", "maraviroc", "nilotinib", "posaconazole", "ranolazine", "saxagliptin", "sirolimus", "sitagliptin", "talinolol", "tolvaptan", "topotecan"]:
    a = Assertion(elt, "substrate_of", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of p-glycoprotein. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### OATP1B1 inhibitors then substrates
for elt in ["cyclosporine", "eltrombopag", "gemfibrozil"]:
    a = Assertion(elt, "inhibits", "oatp1b1")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("rifampin", "inhibits", "oatp1b1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atrasentan", "atorvastatin", "bosentan", "ezetimibe", "fluvastatin", "glyburide", "rosuvastatin", "simvastatin-acid", "pitavastatin", "pravastatin", "repaglinide", "rifampin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "substrate_of", "oatp1b1")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("irinotecan", "substrate_of", "oatp1b1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that the active metabolite of this drug, SN-38, is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### OATP1B3 inhibitors then substrates
a = Assertion("cyclosporine", "inhibits", "oatp1b3")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3. For more information, see Table 6 on page 49, and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("rifampin", "inhibits", "oatp1b3")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atorvastatin", "rosuvastatin", "pitavastatin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "substrate_of", "oatp1b3")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of OATP1B3. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("telmisartan", "primary_total_clearance_enzyme", "oatp1b3")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate selective for OATP1B3. For more information, see Table 7 on page 51, footnote 2 on page 51, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
#################### DUAL INHIBITORS ######################
###########################################################

for elt in ["itraconazole", "clarithromycin", "ketoconazole", "conivaptan", "voriconazole", "nefazodone"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)       

for elt in ["verapamil", "erythromycin", "diltiazem", "dronedarone"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
for elt in ["lapatinib", "quinidine", "ranolazine", "amiodarone", "felodipine", "azithromycin", "cimetidine"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    if(elt == "lapatinib"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

for elt in ["itraconazole", "clarithromycin", "ketoconazole", "conivaptan", "verapamil", "erythromycin", "diltiazem", "dronedarone", "lapatinib", "quinidine", "ranolazine", "amiodarone", "felodipine", "azithromycin"]:
    a = Assertion(elt, "inhibits", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    if(elt == "ketoconazole" or elt == "erythromycin" or elt == "azithromycin"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein. This data was derived with fexofenadine. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    elif(elt == "lapatinib"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein. This data was derived with digoxin. For more information, see Table 8 on page 53.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein. This data was derived with digoxin. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)        
    
for elt in ["voriconazole", "nefazodone", "cimetidine"]:
    a = Assertion(elt, "inhibits", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is not an effective in vivo inhibitor of p-glycoprotein. This data was derived with digoxin. For more information, see Table 8 on page 53 of the FDA guidelines and Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
    a.insertEvidence("against",e)
    ev.addAssertion(a)

### RENOTIFY OBSERVERS AND PICKLE BOTH EV-BASE/KB
            
ev.renotifyObservers()

dikb.pickleKB("dikb-pickles/dikb-test-two.pickle")
ev.pickleKB("dikb-pickles/ev-test-two.pickle")
