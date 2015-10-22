# Description - Sam Rosko's File to Update the DIKB
# Last Update - 10/22/2015

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

for i in ["acyclovir", "aliskiren", "allopurinol", "ambrisentan", "armodafinil", "atorvastatin", "atrasentan", "azithromycin", "bicalutamide", "boceprevir", "clobazam", "colchicine", "conivaptan", "crizotinib",  "cyclosporine", "dabigatran", "darifenacin", "darunavir", "digoxin", "dihydroergotamine", "dronedarone", "eltrombopag", "esomeprazole", "etravirine", "everolimus", "ezetimibe", "famotidine", "febuxostat", "fexofenadine", "fluticasone",  "gemfibrozil", "hydralazine", "lurasidone", "maraviroc", "melatonin", "nebivolol", "oxandrolone", "pazopanib", "phenylpropanolamine", "pilocarpine", "pitavastatin", "quercetin", "ramelteon", "ranitidine", "rifampin", "reserpine", "rosuvastatin", "saxagliptin", "sirolimus", "sitagliptin", "telaprevir", "ticagrelor", "tigecycline", "tipranavir", "tizanidine", "tolvaptan", "topotecan", "vemurafenib", "irinotecan", "diethyldithiocarbamate", "phencyclidine", "tacrolimus", "talinolol", "tranylcypromine", "valspodar", "zosuquidar", "elacridar", "sulfaphenazole", "dabigatran-etexilate"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	d = Drug(i)
	dikb.putObject(d)

for i in ["triazolam-4-hydroxylation", "terfenadine-C-hydroxylation", "testosterone-6b-hydroxylation", "theophylline-N-demethylation", "tolbutamide-methyl-hydroxylation", "phenytoin-4-hydroxylation", "propofol-hydroxylation", "rosiglitazone-para-hydroxylation", "simvastatin-acid", "tacrine-1-hydroxylation", "S-mephenytoin-4’-hydroxylation", "efavirenz-hydroxylase", "erythromycin-N-demethylation", "fluoxetine-O-dealkylation", "flurbiprofen-4’-hydroxylation", "midazolam-1-hydroxylation", "nicotine-C-oxidation", "nifedipine-oxidation", "omeprazole-5-hydroxylation", "phenacetin-O-deethylation", "S-mephenytoin-N-demethylation", "S-warfarin-7-hydroxylation", "amodiaquine-N-deethylation", "aniline-4-hydroxylation", "bupropion-hydroxylation", "caffeine-3-N-demethylation", "chlorzoxazone-6-hydroxylation", "coumarin-7-hydroxylation", "debrisoquine-4-hydroxylation", "dextromethorphan-N-demethylation", "dextromethorphan-O-demethylation", "diclofenac-4’-hydroxylation", "2-isopropenyl-2-methyl-adamantane", "7-ethoxyresorufin-O-deethylation", "bufuralol-1’-hydroxylation", "lauric-acid-11-hydroxylation", "p-nitrophenol-3-hydroxylation", "taxol-6-hydroxylation"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	m = Metabolite(i)
	dikb.putObject(m)

for i in ["tryptamine", "azamulin", "nootkatone"]:
	if i in dikb.objects.keys():
		print "%s seems to be present already!" % i
		continue

	c = Chemical(i)
	dikb.putObject(c)
	
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
            v.assert_by_default = 0
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            v.evidence_against.remove(it)
            v.assert_by_default = 0

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
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["methoxsalen", "mexiletine", "phenylpropanolamine", "vemurafenib", "zileuton"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["acyclovir", "allopurinol", "caffeine", "cimetidine", "disulfiram", "famotidine", "norfloxacin", "propafenone", "propranolol", "terbinafine", "ticlopidine", "verapamil"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2B6 "inhibitor" entries
for elt in ["clopidogrel", "ticlopidine", "prasugrel"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2B6. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C8 "inhibitor" entries
a = Assertion("gemfibrozil", "in_viVo_selective_inhibitor_of_enzyme", "cyp2c8")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C8. Gemfibrozil also inhibits OATP1B1. For more information, see Table 3 on page 41, footnote 6 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###### CYP2C9 "inhibitor" entries
for elt in ["amiodarone", "fluconazole", "miconazole", "oxandrolone"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["capecitabine", "cotrimoxazole", "etravirine", "fluvastatin", "fluvoxamine", "metronidazole", "sulfinpyrazone", "tigecycline", "voriconazole", "zafirlukast"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C19 "inhibitor" entries
a = Assertion("fluconazole", "in_viVo_selective_inhibitor_of_enzyme", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19 based on the AUC ratio of omeprazole, which is also metabolized by CYP3A. For more information, see Table 3 on page 41, footnote 7 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("fluvoxamine", "in_viVo_selective_inhibitor_of_enzyme", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Fluvoxamine strongly inhibits CYP1A2 and CYP2C19, but it also inhibits CYP2C8/CYP2C9 and CYP3A. For more information, see Table 3 on page 41, footnote 8 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("ticlopidine", "in_viVo_selective_inhibitor_of_enzyme", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Ticlopidine strongly inhibits CYP2C19, but it also inhibits CYP3A, CYP2B6, and CYP1A2. For more information, see Table 3 on page 41, footnote 9 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["esomeprazole", "fluoxetine", "omeprazole", "voriconazole"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["armodafinil", "cimetidine", "etravirine", "felbamate", "ketoconazole"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP3A4 "inhibitor" entries
for elt in ["boceprevir", "clarithromycin", "conivaptan", "indinavir", "itraconazole", "ketoconazole", "nefazodone", "nelfinavir", "posaconazole", "telaprevir", "telithromycin", "voriconazole"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A4. For more information, see Table 3 on pages 41/42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amprenavir", "aprepitant", "ciprofloxacin", "crizotinib", "diltiazem", "erythromycin", "fluconazole", "fosamprenavir", "imatinib", "verapamil"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alprazolam", "amiodarone", "amlodipine", "atorvastatin", "bicalutamide", "cilostazol", "cimetidine", "cyclosporine", "fluoxetine", "fluvoxamine", "isoniazid", "lapatinib", "nilotinib", "pazopanib", "ranitidine", "ranolazine", "zileuton"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 "inhibitor" entries
for elt in ["bupropion", "fluoxetine", "paroxetine", "quinidine"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["cinacalcet", "duloxetine", "terbinafine"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amiodarone", "celecoxib", "clobazam", "cimetidine", "desvenlafaxine", "diltiazem", "diphenhydramine",  "febuxostat", "gefitinib", "hydralazine", "hydroxychloroquine", "imatinib", "methadone", "pazopanib", "propafenone", "ranitidine", "sertraline", "telithromycin", "verapamil", "vemurafenib"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp2d6")
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
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp1a2")
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

a = Assertion("paclitaxel", "primary_total_clearance_enzyme", "cyp2c8")
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
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp2c9")
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

a = Assertion("S-mephenytoin", "primary_total_clearance_enzyme", "cyp2c19")
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
    a = Assertion(elt, "primary_total_clearance_enzyme", "cyp3a4")
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

a = Assertion("thioridazine", "primary_total_clearance_enzyme", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pimozide", "primary_total_clearance_enzyme", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
############### IN VIVO TRANSPORT PROTEINS  ###############
###########################################################

for elt in ["amiodarone", "captopril", "carvedilol", "clarithromycin", "conivaptan", "cyclosporine", "diltiazem", "dronedarone", "felodipine", "itraconazole", "quinidine", "ranolazine", "ticagrelor", "verapamil"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in digoxin AUC. For more information, see Table 6 on page 49, footnote 2 on page 49, and  Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["azithromycin", "ketoconazole"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in fexofenadine AUC. For more information, see Table 6 on page 49, footnote 4 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("erythromycin", "in_viVo_selective_inhibitor_of_enzyme", "p-glycoprotein")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of p-glycoprotein because this showed a >25% increase in talinolol AUC. For more information, see Table 6 on page 49, footnote 5 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["aliskiren", "ambrisentan", "colchicine", "dabigatran", "dabigatran-etexilate", "digoxin", "everolimus", "fexofenadine", "imatinib", "lapatinib", "maraviroc", "nilotinib", "posaconazole", "ranolazine", "saxagliptin", "sirolimus", "sitagliptin", "talinolol", "tolvaptan", "topotecan"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of p-glycoprotein. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### OATP1B1 inhibitors then substrates
for elt in ["cyclosporine", "eltrombopag", "gemfibrozil"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "oatp1b1")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("rifampin", "in_viVo_selective_inhibitor_of_enzyme", "oatp1b1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atrasentan", "atorvastatin", "bosentan", "ezetimibe", "fluvastatin", "glyburide", "rosuvastatin", "simvastatin-acid", "pitavastatin", "pravastatin", "repaglinide", "rifampin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "oatp1b1")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("irinotecan", "primary_total_clearance_enzyme", "oatp1b1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that the active metabolite of this drug, SN-38, is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### OATP1B3 inhibitors then substrates
a = Assertion("cyclosporine", "in_viVo_selective_inhibitor_of_enzyme", "oatp1b3")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3. For more information, see Table 6 on page 49, and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("rifampin", "in_viVo_selective_inhibitor_of_enzyme", "oatp1b3")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atorvastatin", "rosuvastatin", "pitavastatin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "primary_total_clearance_enzyme", "oatp1b3")
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
################ IN VITRO CYP INHIBITORS ##################
###########################################################

##### CYP1A2
a = Assertion("furafylline", "in_vitro_selective_inhibitor_of_enzyme", "cyp1a2")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP1A2 for in vitro experiments. Furafylline is a mechanism-based inhibitor and should be pre-incubated before adding substrate. See Table 1 and footnote 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("alpha-naphthoflavone", "in_vitro_selective_inhibitor_of_enzyme", "cyp1a2")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP1A2 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("furafylline", "inhibition_constant", "cyp1a2")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP1A2 for in vitro experiments at a K_i of 0.6micM. See Table 1 on the FDA website. \n\n0.6micM/L X 1M/10^6micM X 260.25g/M = 0.00015615g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015", val = "0.00015615")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("alpha-naphthoflavone", "inhibition_constant", "cyp1a2")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP1A2 for in vitro experiments at a K_i of 0.1micM. See Table 1 on the FDA website. \n\n0.1micM/L X 1M/10^6micM X 272.30g/M = 0.00002723g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/22/2015", val = "0.00002723")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2A6
a = Assertion("tranylcypromine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("methoxsalen", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments. Methoxsalen is a mechanism-based inhibitor and should be pre-incubated before adding substrate. See Table 1 and footnote 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pilocarpine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("tryptamine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments in cDNA expressing microsomes from human lymphoblast cells. See Table 1 and footnote 5 on the FDA website. ", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tranylcypromine", "inhibition_constant", "cyp2a6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments at a K_i of 0.02micM. See Table 1 on the FDA website. \n\n0.02micM/L X 1M/10^6micM X 133.19g/M = 0.0000026638g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015", val = "0.0000026638")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("methoxsalen", "inhibition_constant", "cyp2a6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments at a K_i of 0.01micM. See Table 1 on the FDA website. \n\n0.01micM/L X 1M/10^6micM X 260.25g/M = 0.00000216189g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015", val = "0.00000216189")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("pilocarpine", "inhibition_constant", "cyp2a6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments at a K_i of 4micM. See Table 1 on the FDA website. \n\n4micM/L X 1M/10^6micM X 208.2569g/M = 0.000833g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015", val = "0.000833")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tryptamine", "inhibition_constant", "cyp2a6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments in cDNA expressing microsomes from human lymphoblast cells at a K_i of 1.7micM. See Table 1 and footnote 5 on the FDA website. \n\n1.7micM/L X 1M/10^6micM X 966.763g/M = 0.00164349g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015", val = "0.00164349")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2B6
for elt in ["3-isopropenyl-3-methyl-diamantane", "2-isopropenyl-2-methyl-adamantane", "sertraline", "phencyclidine", "thiotepa", "clopidogrel", "ticlopidine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    if elt == "3-isopropenyl-3-methyl diamantane" or elt ==  "2-isopropenyl-2-methyl adamantane":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6. See Table 1 and footnote 4 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

a = Assertion_inhibition_constant("3-isopropenyl-3-methyl-diamantane", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6 at a K_i of 2.2micM. See Table 1 on the FDA website. \n\n2.2micM/L X 1M/10^6micM X 242.404g/M = 0.0005332888g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015", val = "0.0005332888")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("2-isopropenyl-2-methyl-adamantane", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6 at a K_i of 5.3 micM. See Table 1 on the FDA website. \n\n5.3micM/L X 1M/10^6micM X 190.324g/M = 0.0010087172g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015", val = "0.0010087172")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("sertraline", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at an IC50 of 3.2micM. See Table 1 on the FDA website. \n\n3.2micM/L X 1M/10^6micM X 306.229580g/M = 0.000979934656g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.000979934656")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("phencyclidine", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 10micM. See Table 1 on the FDA website. \n\n10micM/L X 1M/10^6micM X 243.387100g/M = 0.002433871g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.002433871")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("thiotepa", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 4.8micM. See Table 1 on the FDA website. \n\n4.8micM/L X 1M/10^6micM X 189.218342g/M = 0.0009082480416g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0009082480416")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("clopidogrel", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.5micM. See Table 1 on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 321.821740g/M = 0.00016091087g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00016091087")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ticlopidine", "inhibition_constant", "cyp2b6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.2micM. See Table 1 on the FDA website. \n\n0.2micM/L X 1M/10^6micM X 263.785660g/M = 0.000052757132g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.000052757132")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C8
for elt in ["montelukast", "quercetin"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c8")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["trimethoprim", "gemfibrozil", "rosiglitazone", "pioglitazone"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c8")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion_inhibition_constant("montelukast", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.1micM. See Table 1 on the FDA website. \n\n1.1micM/L X 1M/10^6micM X 586.183240g/M = 0.000644801564g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.000644801564")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quercetin", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.1micM. See Table 1 on the FDA website. \n\n1.1micM/L X 1M/10^6micM X 1701.19848g/M = 0.001871318328g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.001871318328")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("trimethoprim", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 32micM. See Table 1 on the FDA website. \n\n32micM/L X 1M/10^6micM X 290.317720g/M = 0.00929016704g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00929016704")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("gemfibrozil", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 69micM. See Table 1 on the FDA website. \n\n69micM/L X 1M/10^6micM X 250.33338g/M = 0.01727300322g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.01727300322")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("rosiglitazone", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 5.6micM. See Table 1 on the FDA website. \n\n5.6micM/L X 1M/10^6micM X 357.426760g/M = 0.002001589856g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.002001589856")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("pioglitazone", "inhibition_constant", "cyp2c8")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.7micM. See Table 1 on the FDA website. \n\n1.7micM/L X 1M/10^6micM X 356.438700g/M = 0.00060594579g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00060594579")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C9
a = Assertion("sulfaphenazole", "in_vitro_selective_inhibitor_of_enzyme", "cyp2c9")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C9 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["fluconazole", "fluvoxamine", "fluoxetine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
a = Assertion_inhibition_constant("sulfaphenazole", "inhibition_constant", "cyp2c9")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 1.3micM. See Table 1 on the FDA website. \n\n1.3micM/L X 1M/10^6micM X 314.36226g/M = 0.000408670938g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.000408670938")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluconazole", "inhibition_constant", "cyp2c9")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 7micM. See Table 1 on the FDA website. \n\n7micM/L X 1M/10^6micM X 306.270786g/M = 0.002143895502g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.002143895502")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluvoxamine", "inhibition_constant", "cyp2c9")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 6.4micM. See Table 1 on the FDA website. \n\n6.4micM/L X 1M/10^6micM X 318.334650g/M = 0.00203734176g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00203734176")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluoxetine", "inhibition_constant", "cyp2c9")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 18micM. See Table 1 on the FDA website. \n\n18micM/L X 1M/10^6micM X 309.326130g/M = 0.00556787034g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00556787034")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C19
for elt in ["ticlopidine", "nootkatone"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion_inhibition_constant("ticlopidine", "inhibition_constant", "cyp2c19")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments at a K_i of 1.2micM. See Table 1 on the FDA website. \n\n1.2micM/L X 1M/10^6micM X 263.785660g/M = 0.000316542792g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.000316542792")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("nootkatone", "inhibition_constant", "cyp2c19")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments at a K_i of 0.5micM. See Table 1 on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 218.334580g/M = 0.00010916729g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.00010916729")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2D6
a = Assertion("quinidine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2D6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "cyp2d6")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2D6 for in vitro experiments at a K_i of 0.27micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 324.416760g/M = 0.0000875925252g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0000875925252")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2E1
a = Assertion("diethyldithiocarbamate", "in_vitro_selective_inhibitor_of_enzyme", "cyp2e1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2E1 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("diethyldithiocarbamate", "inhibition_constant", "cyp2e1")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2E1 for in vitro experiments at a K_i of 9.8micM. See Table 1 on the FDA website. \n\n9.8micM/L X 1M/10^6micM X 148.269600g/M = 0.002139678884g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.002139678884")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP3A4/5
for elt in ["ketoconazole", "itraconazole"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["ketoconazole", "itraconazole"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a5")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A5 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)    
    
for elt in ["azamulin", "troleandomycin", "verapamil"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    if elt == "azamulin":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4 for in vitro experiments. Azamulin is a specific time-dependent inhibitor of CYP3A4. See Table 1 and footnote 6 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

for elt in ["azamulin", "troleandomycin", "verapamil"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a5")
    a.assert_by_default = True
    e = Evidence(ev)
    if elt == "azamulin":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A5 for in vitro experiments. Azamulin is a specific time-dependent inhibitor of CYP3A5. See Table 1 and footnote 6 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A5 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
        
a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "cyp3a4")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4 for in vitro experiments at a K_i of 0.0037micM. See Table 1 on the FDA website. \n\n0.0037micM/L X 1M/10^6micM X 531.430920g/M = 0.0000019662944g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0000019662944")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("itraconazole", "inhibition_constant", "cyp3a4")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4 for in vitro experiments at a K_i of 0.27micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 705.633420g/M = 0.0001905210234g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0001905210234")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("troleandomycin", "inhibition_constant", "cyp3a4")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4 for in vitro experiments at a K_i of 0.27micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 813.968380g/M = 0.0002197714626g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0002197714626")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "cyp3a4")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4 for in vitro experiments at a K_i of 10micM. See Table 1 on the FDA website. \n\n10micM/L X 1M/10^6micM X 454.601620g/M = 0.0045460162g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0045460162")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "cyp3a5")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A5 for in vitro experiments at a K_i of 0.0037micM. See Table 1 on the FDA website. \n\n0.0037micM/L X 1M/10^6micM X 531.430920g/M = 0.0000019662944g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0000019662944")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("itraconazole", "inhibition_constant", "cyp3a5")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A5 for in vitro experiments at a K_i of 0.27micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 705.633420g/M = 0.0001905210234g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0001905210234")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("troleandomycin", "inhibition_constant", "cyp3a5")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A5 for in vitro experiments at a K_i of 0.27micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 813.968380g/M = 0.0002197714626g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0002197714626")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "cyp3a5")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A5 for in vitro experiments at a K_i of 10micM. See Table 1 on the FDA website. \n\n10micM/L X 1M/10^6micM X 454.601620g/M = 0.0045460162g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/8/2015", val = "0.0045460162")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
################ IN VITRO CYP SUBSTRATES ##################
###########################################################

##### CYP1A2
a = Assertion("phenacetin-O-deethylation", "in_vitro_probe_substrate_of_enzyme", "cyp1a2")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP1A2 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["7-ethoxyresorufin-O-deethylation", "theophylline-N-demethylation", "caffeine-3-N-demethylation", "tacrine-1-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp1a2")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP1A2 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2A6
for elt in ["coumarin-7-hydroxylation", "nicotine-C-oxidation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2a6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2A6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2B6
for elt in ["efavirenz-hydroxylase", "bupropion-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2B6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["propofol-hydroxylation", "S-mephenytoin-N-demethylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2b6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2B6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C8
a = Assertion("taxol-6-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2c8")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C8 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["amodiaquine-N-deethylation", "rosiglitazone para-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c8")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C8 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C9
for elt in ["tolbutamide-methyl-hydroxylation", "S-warfarin 7-hydroxylation", "diclofenac 4’-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C9 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["flurbiprofen-4’-hydroxylation", "phenytoin-4-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c9")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C9 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C19
a = Assertion("S-mephenytoin-4’-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2c19")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C19 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["omeprazole-5-hydroxylation", "fluoxetine O-dealkylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c19")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C19 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6
for elt in ["( ± )-bufuralol-1’-hydroxylation", "dextromethorphan-O-demethylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2d6")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2D6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("debrisoquine-4-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2d6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2D6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2E1
a = Assertion("chlorzoxazone-6-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2e1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2E1 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["p-nitrophenol-3-hydroxylation", "lauric-acid-11-hydroxylation", "aniline-4-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2e1")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2E1 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP3A4
for elt in ["midazolam-1-hydroxylation", "testosterone-6-b-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP3A4/5 for in vitro experiments. See Table 2 on the FDA website. Guidelines also recommend use of 2 structurally unrelated CYP3A4/5 substrates for evaluation of in vitro CYP3A inhibition. If the drug inhibits at least one CYP3A substrate in vitro, then in vivo evaluation is warranted.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["erythromycin-N-demethylation", "dextromethorphan-N-demethylation", "triazolam-4-hydroxylation", "terfenadine-C-hydroxylation", "nifedipine-oxidation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP3A4/5 for in vitro experiments. See Table 2 on the FDA website. Guidelines also recommend use of 2 structurally unrelated CYP3A4/5 substrates for evaluation of in vitro CYP3A inhibition. If the drug inhibits at least one CYP3A substrate in vitro, then in vivo evaluation is warranted.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
###########################################################
############## IN VITRO TRANSPORT ENTRIES  ################
###########################################################
######## p-glycoprotein Substrates

for elt in ["digoxin", "loperamide", "quinidine", "vinblastine", "talinolol"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    if elt == "vinblastine":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of p-glycoprotein for in vitro experiments. Vinblastine is also a substrate for MRP2 that is constitutively expressed in Caco-2, and wild type MDCK and LL-CPK1 cells. See Table 8 and footnote 'a' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of p-glycoprotein for in vitro experiments. See Table 8 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

####### p-glycoprotein Inhibitors
for elt in ["cyclosporine", "ketoconazole", "zosuquidar trichloride", "nelfinavir", "quinidine", "tacrolimus", "valspodar", "verapamil", "elacridar", "reserpine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    if elt == "cyclosporine" or elt ==  "ketoconazole" or elt == "nelfinavir":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments. This chemical is also a CYP3A inhibitor. See Table 9 and footnote 'a' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    elif elt == "quinidine":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments. This chemical is also a CYP2D6 inhibitor. See Table 9 and footnote 'b' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments. See Table 9 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

a = Assertion_inhibition_constant("cyclosporine", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 0.5micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 1202.611240g/M = 0.00060130562g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.00060130562")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 5.3micM using a LLC-PK1-MDR1 permeability assay with vinblastine as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n5.3micM/L X 1M/10^6micM X 531.430920g/M = 0.002816583876g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.002816583876")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("zosuquidar", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at an IC50 of 0.024micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.024micM/L X 1M/10^6micM X 636.987066g/M = 0.000015287689584g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.000015287689584")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("nelfinavir", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at an IC50 of 1.4micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n1.4micM/L X 1M/10^6micM X 567.782400g/M = 0.00079489536g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.00079489536")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at an IC50 of 2.2micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n2.2micM/L X 1M/10^6micM X 324.416760g/M = 0.000713716872g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.000713716872")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tacrolimus", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at an IC50 of 0.74micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.74micM/L X 1M/10^6micM X 804.018160g/M = 0.0005949734384g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.0005949734384")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("valspodar", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at an IC50 of 0.11micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.11micM/L X 1M/10^6micM X 1214.621940g/M = 0.0001336084134g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.0001336084134")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 8micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n8micM/L X 1M/10^6micM X 454.601620g/M = 0.00363681296g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.00363681296")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("elacridar", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 0.4micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.4micM/L X 1M/10^6micM X 563.642920g/M = 0.000225457168g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.000225457168")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("elacridar", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 0.4micM using a MDCK-MDR1 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n0.4micM/L X 1M/10^6micM X 563.642920g/M = 0.000225457168g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.000225457168")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("reserpine", "inhibition_constant", "p-glycoprotein")
a.assert_by_default = True
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of p-glycoprotein for in vitro experiments at a Ki of 1.4micM using a Caco-2 permeability assay with digoxin as a p-glycoprotein substrate. See Table 9 and the footnotes on the FDA website. \n\n1.4micM/L X 1M/10^6micM X 608.678700g/M = 0.00085215018g/L", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015", val = "0.00085215018")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
#################### DUAL INHIBITORS ######################
###########################################################

for elt in ["itraconazole", "clarithromycin", "ketoconazole", "conivaptan", "voriconazole", "nefazodone"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    if (elt == "nefazodone"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A. For more information, see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)       

for elt in ["itraconazole", "clarithromycin", "ketoconazole", "conivaptan", "voriconazole", "nefazodone"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a5")
    a.assert_by_default = True
    e = Evidence(ev)
    if (elt == "nefazodone"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A. For more information, see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)           

for elt in ["verapamil", "erythromycin", "diltiazem", "dronedarone"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["verapamil", "erythromycin", "diltiazem", "dronedarone"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a5")
    a.assert_by_default = True
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A. For more information, see Table 8 on page 53 and also see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
for elt in ["lapatinib", "quinidine", "ranolazine", "amiodarone", "felodipine", "azithromycin", "cimetidine"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
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

for elt in ["lapatinib", "quinidine", "ranolazine", "amiodarone", "felodipine", "azithromycin", "cimetidine"]:
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "cyp3a5")
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
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "p-glycoprotein")
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
    a = Assertion(elt, "in_viVo_selective_inhibitor_of_enzyme", "p-glycoprotein")
    a.assert_by_default = True
    e = Evidence(ev)
    if(elt == "nefazodone"):
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is not an effective in vivo inhibitor of p-glycoprotein. This data was derived with digoxin. For more information, see Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("against",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is not an effective in vivo inhibitor of p-glycoprotein. This data was derived with digoxin. For more information, see Table 8 on page 53 of the FDA guidelines and Table 14 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "6/9/2015")
        a.insertEvidence("against",e)
        ev.addAssertion(a)

### RENOTIFY OBSERVERS AND PICKLE BOTH EV-BASE/KB
            
ev.renotifyObservers()

dikb.pickleKB("dikb-pickles/dikb-test.pickle")
ev.pickleKB("dikb-pickles/ev-test.pickle")
