### SAM ROSKO'S TEST FILE FOR WORKING ON DIKB
### LAST UPDATED: 6/9/2015
### RECENTLY: Remaining evidence to be entered: Km values, dual inhibitors

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

###################################################################
# SAMPLE CODE IDEAS
###################################################################

#basic entry attempt for inhibition
for elt in ["cyp2d6", "cyp3a4"]:
    a = Assertion("rosko", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "samuel rosko's brain", q = "samuel rosko believes that this is a likely result", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom", revwr = "boycer", timestamp = "11132014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

#entry attempt for metabolite
a = Assertion("samuel", "has_metabolite", "rosko")
e = Evidence(ev)
e.create(doc_p = "rosko family tree", q = "Samuel has the middle name Charles and the last name of Rosko.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "roskos", timestamp = "11132014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("samuel", "has_metabolite", "rosko")
e = Evidence(ev)
e.create(doc_p = "krebs family tree", q = "Samuel's mother's last name is Krebs rather than Rosko.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "11142014")
a.insertEvidence("against",e)
ev.addAssertion(a)

#add assumption for inhibition entry from metabolite entry
ev.objects['rosko_inhibits_cyp2d6'].evidence_for[0].assumptions.addEntry(['samuel_has_metabolite_rosko'])

#deleting an assertion
ev.deleteAssertion(ev.objects['rosko_inhibits_cyp2d6'])

#deleting an evidence item
ev.objects['samuel_has_metabolite_charles'].evidence_for.pop()

#create a list of document pointers
doc_list = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        doc_list[it.doc_pointer] = e
    for it in v.evidence_against:
        doc_list[it.doc_pointer] = e

#sample evidence entry from 2012 data
a = Assertion("enoxacin", "inhibits", "cyp1a2")
e = Evidence(ev)
e.create(doc_p = "fda2012", q = "The FDA guidelines suggest that this is a strong in vivo inhibitor of CYP3A4. For more information, see Table 3, p. 41 and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "11252014")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
################ IN VIVO CYP INHIBITORS ###################
###########################################################

###### CYP1A2 inhibitor entries
for elt in ["ciprofloxacin", "fluvoxamine"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["methoxsalen", "mexiletine", "phenypropanolamine", "vemurafenib", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["acyclovir", "allopurinol", "caffeine", "cimetidine", "disulfiram", "famotidine", "norfloxacin", "propafeonone", "propranolol", "terbinafine", "ticlopidine", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2B6 "inhibitor" entries
for elt in ["clopidogrel", "ticlopidine", "prasugrel"]:
    a = Assertion(elt, "inhibits", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2B6. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C8 "inhibitor" entries
a = Assertion("gemfibrozil", "inhibits", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C8. Gemfibrozil also inhibits OATP1B1. For more information, see Table 3 on page 41, footnote 6 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###### CYP2C9 "inhibitor" entries
for elt in ["amiodarone", "fluconazole", "miconazole", "oxandrolone"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["capecitabine", "cotrimoxazole", "etravirine", "fluvastatin", "fluvoxamine", "metronidazole", "sulfinpyrazone", "tigecycline", "voriconazole", "zafirlukast"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C19 "inhibitor" entries
a = Assertion("fluconazole", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19 based on the AUC ratio of omeprazole, which is also metabolized by CYP3A. For more information, see Table 3 on page 41, footnote 7 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("fluvoxamine", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Fluvoxamine strongly inhibits CYP1A2 and CYP2C19, but it also inhibits CYP2C8/CYP2C9 and CYP3A. For more information, see Table 3 on page 41, footnote 8 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("ticlopidine", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Ticlopidine strongly inhibits CYP2C19, but it also inhibits CYP3A, CYP2B6, and CYP1A2. For more information, see Table 3 on page 41, footnote 9 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["esomeprazole", "fluoxetine", "omeprazole", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["armodafinil", "cimetidine", "etravirine", "felbamate", "ketoconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP3A4 "inhibitor" entries
for elt in ["boceprevir", "clarithromycin", "conivaptan", "indinavir", "itraconazole", "ketoconazole", "lopinavir/ritonavir", "nefazodone"
"nelfinavir", "posaconazole", "ritonavir", "saquinavir", "telaprevir", "telithromycin", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A4. For more information, see Table 3 on pages 41/42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amprenavir", "aprepitant", "atazanavir", "ciprofloxacin", "crizotinib", "darunavir/ritonavir", "diltiazem", "erythromycin", "fluconazole", "fosamprenavir", "imatinib", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alprazolam", "amiodarone", "amlodipine", "atorvastatin", "bicalutamide", "cilostazol", "cimetidine", "cyclosporine", "fluoxetine", "fluvoxamine", "isoniazid", "lapatinib", "nilotinib", "pazopanib", "ranitidine", "ranolazine", "tipranavir/ritonavir", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 "inhibitor" entries
for elt in ["bupropion", "fluoxetine", "paroxetine", "quinidine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["cinacalcet", "duloxetine", "terbinafine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amiodarone", "celecoxib", "clobazam", "cimetidine", "desvenlafaxine", "diltiazem", "diphenhydramine", "escitalopram", "febuxostat", "gefitinib", "hydralazine", "hydroxychloroquine", "imatinib", "methadone", "pazopanib", "propafenone", "ranitidine", "ritonavir", "sertraline", "telithromycin", "verapamil", "vemurafenib"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###########################################################
################ IN VIVO CYP SUBSTRATES ###################
###########################################################
##Dr. Boyce, we need to address how substrates are entered, do we use (substrate_of), (primary_clearance_enzyme), or (in_Vivo_selective_inhibitor)

###### CYP1A2 substrate entries
for elt in ["alosetron", "caffeine", "duloxetine", "melatonin", "ramelteon", "tacrine", "tizanidine"]:
    a = Assertion(elt, "substrate_of", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP1A2. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["theophylline", "tizanidine"]:
    a = Assertion(elt, "substrate_of", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP1A2 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2B6 substrate entries
for elt in ["bupropion", "efavirenz"]:
    a = Assertion(elt, "substrate_of", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2B6. The AUC of this compound was not increased by 5-fold or more with a CYP2B6 inhibitor, but it represents the most sensitive substrate studied with available inhibitors evaluated to date. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C8 substrates
a = Assertion("repaglinide", "substrate_of", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C8. Repaglinide is also a substrate for OATP1B1, and it is only suitable as a CYP2C8 substrate if the inhibition of OATP1B1 by the investigational drug has been ruled out. For more information, see Table 5 on page 44, footnote 5 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("paclitaxel", "substrate_of", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C8 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C9 substrates
a = Assertion("celecoxib", "substrate_of", "cyp2c9")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C9. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["warfarin", "phenytoin"]:
    a = Assertion(elt, "substrate_of", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C9 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C19 substrates
for elt in ["lansoprazole", "omeprazole", "S-mephenytoin"]:
    a = Assertion(elt, "substrate_of", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C19. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("S-mephenytoin", "substrate_of", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C19 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP3A4 substrates
for elt in ["alfentanil", "aprepitant", "budesonide", "buspirone", "conivaptan", "darifenacin", "darunavir", "dasatinib", "dronedarone", "eletriptan", "eplerenone", "everolimus", "felodipine", "indinavir", "fluticasone", "lopinavir", "lovastatin", "lurasidone", "maraviroc", "midazolam", "nisoldipine", "quetiapine", "saquinavir", "sildenafil", "simvastatin", "sirolimus", "tolvaptan", "tipranavir", "triazolam", "vardenafil", "ticagrelor"]:
    a = Assertion(elt, "substrate_of", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP3A4. Because a number of CYP3A substrates (e.g., darunavir, maraviroc) are also substrates of P-gp, the observed increase in exposure could be due to inhibition of both CYP3A and P-gp. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alfentanil", "cyclosporine", "dihydroergotamine", "ergotamine", "fentanyl", "pimozide", "quinidine", "sirolimus", "tacrolimus"]:
    a = Assertion(elt, "substrate_of", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP3A4 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 substrate entries
for elt in ["atomoxetine", "desipramine", "dextromethorphan", "metoprolol", "nebivolol", "perphenazine", "tolterodine", "venlafaxine"]:
    a = Assertion(elt, "substrate_of", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2D6. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("thioridazine", "substrate_of", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pimozide", "substrate_of", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
############### IN VIVO TRANSPORT PROTEINS  ###############
###########################################################
# Have to add these to the system as enzymes

###### P-gp both inhibitors and substrates
# also, need to replace the name P-gp
# do I need to make rules for 'increases AUC' for digoxin, fexofenadine, talinolol, see quote below... I believe I should

for elt in ["amiodarone", "captopril", "carvedilol", "clarithromycin", "conivaptan", "cyclosporine", "diltiazem", "dronedarone", "felodipine", "itraconazole", "quinidine", "ranolazine", "ticagrelor", "verapamil"]:
    a = Assertion(elt, "inhibits", "P-gp")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in digoxin AUC. For more information, see Table 6 on page 49, footnote 2 on page 49, and  Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["azithromycin", "ketoconazole"]:
    a = Assertion(elt, "inhibits", "P-gp")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in fexofenadine AUC. For more information, see Table 6 on page 49, footnote 4 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("erythromycin", "inhibits", "P-gp")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in talinolol AUC. For more information, see Table 6 on page 49, footnote 5 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["aliskiren", "ambrisentan", "colchicine", "dabigatran", "etexilate", "digoxin", "everolimus", "fexofenadine", "imatinib", "lapatinib", "maraviroc", "nilotinib", "posaconazole", "ranolazine", "saxagliptin", "sirolimus", "sitagliptin", "talinolol", "tolvaptan", "topotecan"]:
    a = Assertion(elt, "substrate_of", "P-gp")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of P-gp. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### OATP1B1 inhibitors then substrates
for elt in ["cyclosporine", "eltrombopag", "gemfibrozil"]:
    a = Assertion(elt, "inhibits", "OATP1B1")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

# these might not be includeable, have to look up ritonavir drug combinations
for elt in ["atazanavir", "lopinavir", "saquinavir", "tipranavir"]:
    a = Assertion(elt, "inhibits", "OATP1B1")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1. Separation of the in vivo inhibition effect from ritonavir is difficult because this drug is usually co-administered with ritonavir. For more information, see Table 6 on page 49, footnote 10 on page 49, and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("ritonavir", "inhibits", "OATP1B1")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1. The in vivo inhibition effect of ritonavir cannot be easily estimated because it is usually coadministered with other HIV protease inhibitors that are inhibitors for OATP as well. For more information, see Table 6 on page 49, footnote 11 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("rifampin", "inhibits", "OATP1B1")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atrasentan", "atorvastatin", "bosentan", "ezetimibe", "fluvastatin", "glyburide", "rosuvastatin", "simvastatin acid", "pitavastatin", "pravastatin", "repaglinide", "rifampin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "substrate_of", "OATP1B1")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

# Dr. Boyce, should I call it irinotecan or SN-38
a = Assertion("irinotecan", "substrate_of", "OATP1B1")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that the active metabolite of this drug, SN-38, is an in vivo substrate of OATP1B1. For more information, see Table 7 on page 51 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### OATP1B3 inhibitors then substrates
a = Assertion("cyclosporine", "inhibits", "OATP1B3")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3. For more information, see Table 6 on page 49, and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

# these might not be includeable, have to look up ritonavir drug combinations
for elt in ["atazanavir", "lopinavir", "saquinavir"]:
    a = Assertion(elt, "inhibits", "OATP1B3")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3. Separation of the in vivo inhibition effect from ritonavir is difficult because this drug is usually co-administered with ritonavir. For more information, see Table 6 on page 49, footnote 10 on page 49, and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("ritonavir", "inhibits", "OATP1B3")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3. The in vivo inhibition effect of ritonavir cannot be easily estimated because it is usually coadministered with other HIV protease inhibitors that are inhibitors for OATP as well. For more information, see Table 6 on page 49, footnote 11 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("rifampin", "inhibits", "OATP1B3")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B3 when given as a single dose. For more information, see Table 6 on page 49, footnote 9 on page 49, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["atorvastatin", "rosuvastatin", "pitavastatin", "valsartan", "olmesartan"]:
    a = Assertion(elt, "substrate_of", "OATP1B3")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of OATP1B3. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("telmisartan", "substrate_of", "OATP1B3")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate selective for OATP1B3. For more information, see Table 7 on page 51, footnote 2 on page 51, and Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
################ IN VITRO CYP INHIBITORS ##################
###########################################################
# we are using in_vitro_probe_substrate_of_enzyme and in_vitro_selective_inhibitor_of_enzyme for all of these
# also using inhibition_constant... in regards to this, i haven't seen any notes on how to handle Ki or Km ranges...
# so I have been using the lower bound... I checked your dissertation and the evidence taxonomy but couldn't find anything
# however, the evidence taxonomy suggest i need to link the inhibition constants with an assumption of the inhibitor rule
# do I manually do this or does the system do it when it processes the rules
# this data comes from fda website, not fda 2012, i used a reference to the website, but a secondary, permanent link may be preferable

##### CYP1A2
a = Assertion("furafylline", "in_vitro_selective_inhibitor_of_enzyme", "cyp1a2")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP1A2 for in vitro experiments. Furafylline is a mechanism-based inhibitor and should be pre-incubated before adding substrate. See Table 1 and footnote 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("alpha-naphthoflavone", "in_vitro_selective_inhibitor_of_enzyme", "cyp1a2")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP1A2 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("furafylline", "inhibition_constant", "cyp1a2")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP1A2 for in vitro experiments at a K_i range of 0.6micM-0.73micM. See Table 1 on the FDA website. \n\n0.6-0.73micM/L X 1M/10^6micM X 260.25g/M = 0.00015615g/L - 0.0001899825g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015", val = "0.00015615")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("alpha-naphthoflavone", "inhibition_constant", "cyp1a2")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP1A2 for in vitro experiments at a K_i of 0.1micM. See Table 1 on the FDA website. \n\n0.1micM/L X 1M/10^6micM X 272.30g/M = 0.00002723g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/22/2015", val = "0.00002723")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2A6
a = Assertion("tranylcypromine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("methoxsalen", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments. Methoxsalen is a mechanism-based inhibitor and should be pre-incubated before adding substrate. See Table 1 and footnote 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pilocarpine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("tryptamine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2a6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments in cDNA expressing microsomes from human lymphoblast cells. See Table 1 and footnote 5 on the FDA website. ", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tranylcypromine", "inhibition_constant", "cyp2a6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments at a K_i range of 0.02micM to 0.2micM. See Table 1 on the FDA website. \n\n0.02-0.2micM/L X 1M/10^6micM X 133.19g/M = 2.6638E-6g/L - 2.6638E-5g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015", val = "0.0000026638")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("methoxsalen", "inhibition_constant", "cyp2a6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2A6 for in vitro experiments at a K_i range of 0.01micM to 0.2micM. See Table 1 on the FDA website. \n\n0.01-0.2micM/L X 1M/10^6micM X 260.25g/M = 0.00000216189g/L - 0.0000432379g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015", val = "0.00000216189")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("pilocarpine", "inhibition_constant", "cyp2a6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments at a K_i of 4micM. See Table 1 on the FDA website. \n\n4micM/L X 1M/10^6micM X 208.2569g/M = 0.000833g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015", val = "0.000833")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tryptamine", "inhibition_constant", "cyp2a6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2A6 for in vitro experiments in cDNA expressing microsomes from human lymphoblast cells at a K_i of 1.7micM. See Table 1 and footnote 5 on the FDA website. \n\n1.7micM/L X 1M/10^6micM X 966.763g/M = 0.00164349g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015", val = "0.00164349")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2B6
# The names here probably need changed, there shouldn't be allowed to be a space in the diamantane or adamantane, and i cant find the drugs online to make conversions for the kI value
for elt in ["3-isopropenyl-3-methyl diamantane", "2-isopropenyl-2-methyl adamantane", "sertraline", "phencyclidine", "thiotepa", "clopidogrel", "ticlopidine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2b6")
    e = Evidence(ev)
    if elt == "3-isopropenyl-3-methyl diamantane" or elt ==  "2-isopropenyl-2-methyl adamantane":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6. See Table 1 and footnote 4 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

####################################################################################################
a = Assertion_inhibition_constant("3-isopropenyl-3-methyl diamantane", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6 at a K_i of 2.2micM. See Table 1 on the FDA website. \n\n2.2micM/L X 1M/10^6micM X g/M = g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("2-isopropenyl-2-methyl adamantane", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments in supersomes, microsomal isolated from insect cells transfected with baculovirus containing CYP2B6 at a K_i of 5.3 micM. See Table 1 on the FDA website. \n\n5.3micM/L X 1M/10^6micM X g/M = g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "")
a.insertEvidence("for",e)
ev.addAssertion(a)
####################################################################################################

a = Assertion_inhibition_constant("sertraline", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at an IC50 of 3.2micM. See Table 1 on the FDA website. \n\n3.2micM/L X 1M/10^6micM X 306.229580g/M = 0.000979934656g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.000979934656")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("phencyclidine", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 10micM. See Table 1 on the FDA website. \n\n10micM/L X 1M/10^6micM X 243.387100g/M = 0.002433871g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.002433871")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("thiotepa", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 4.8micM. See Table 1 on the FDA website. \n\n4.8micM/L X 1M/10^6micM X 189.218342g/M = 0.0009082480416g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0009082480416")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("clopidogrel", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.5micM. See Table 1 on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 321.821740g/M = 0.00016091087g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00016091087")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ticlopidine", "inhibition_constant", "cyp2b6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.2micM. See Table 1 on the FDA website. \n\n0.2micM/L X 1M/10^6micM X 263.785660g/M = 0.000052757132g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.000052757132")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C8
for elt in ["montelukast", "quercetin"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c8")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["trimethoprim", "gemfibrozil", "rosiglitazone", "pioglitazone"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c8")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion_inhibition_constant("montelukast", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.1micM. See Table 1 on the FDA website. \n\n1.1micM/L X 1M/10^6micM X 586.183240g/M = 0.000644801564g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.000644801564")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quercetin", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.1micM. See Table 1 on the FDA website. \n\n1.1micM/L X 1M/10^6micM X 1701.19848g/M = 0.001871318328g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.001871318328")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("trimethoprim", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 32micM. See Table 1 on the FDA website. \n\n32micM/L X 1M/10^6micM X 290.317720g/M = 0.00929016704g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00929016704")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("gemfibrozil", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i range of 69micM to 75 micM. See Table 1 on the FDA website. \n\n69micM/L X 1M/10^6micM X 250.33338g/M = 0.01727300322g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.01727300322")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("rosiglitazone", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 5.6micM. See Table 1 on the FDA website. \n\n5.6micM/L X 1M/10^6micM X 357.426760g/M = 0.002001589856g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.002001589856")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("pioglitazone", "inhibition_constant", "cyp2c8")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.7micM. See Table 1 on the FDA website. \n\n1.7micM/L X 1M/10^6micM X 356.438700g/M = 0.00060594579g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00060594579")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C9
a = Assertion("sulfaphenazole", "in_vitro_selective_inhibitor_of_enzyme", "cyp2c9")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C9 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["fluconazole", "fluvoxamine", "fluoxetine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
a = Assertion_inhibition_constant("sulfaphenazole", "inhibition_constant", "cyp2c9")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 1.3micM. See Table 1 on the FDA website. \n\n1.3micM/L X 1M/10^6micM X 314.36226g/M = 0.000408670938g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.000408670938")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluconazole", "inhibition_constant", "cyp2c9")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i of 7micM. See Table 1 on the FDA website. \n\n7micM/L X 1M/10^6micM X 306.270786g/M = 0.002143895502g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.002143895502")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluvoxamine", "inhibition_constant", "cyp2c9")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i range of 6.4micM to 19micM. See Table 1 on the FDA website. \n\n6.4micM/L X 1M/10^6micM X 318.334650g/M = 0.00203734176g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00203734176")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("fluoxetine", "inhibition_constant", "cyp2c9")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C9 for in vitro experiments at a K_i range of 18micM to 41micM. See Table 1 on the FDA website. \n\n18micM/L X 1M/10^6micM X 309.326130g/M = 0.00556787034g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00556787034")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C19
for elt in ["ticlopidine", "nootkatone"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/29/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion_inhibition_constant("ticlopidine", "inhibition_constant", "cyp2c19")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments at a K_i of 1.2micM. See Table 1 on the FDA website. \n\n1.2micM/L X 1M/10^6micM X 263.785660g/M = 0.000316542792g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.000316542792")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("nootkatone", "inhibition_constant", "cyp2c19")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2C19 for in vitro experiments at a K_i of 0.5micM. See Table 1 on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 218.334580g/M = 0.00010916729g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.00010916729")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2D6
a = Assertion("quinidine", "in_vitro_selective_inhibitor_of_enzyme", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP2D6 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "cyp2d6")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2D6 for in vitro experiments at a K_i range of 0.27micM to 0.4micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 324.416760g/M = 0.0000875925252g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0000875925252")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2E1
a = Assertion("diethyldithiocarbamate", "in_vitro_selective_inhibitor_of_enzyme", "cyp2e1")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2E1 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("diethyldithiocarbamate", "inhibition_constant", "cyp2e1")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP2E1 for in vitro experiments at a K_i range of 9.8micM to 34micM. See Table 1 on the FDA website. \n\n9.8micM/L X 1M/10^6micM X 148.269600g/M = 0.002139678884g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.002139678884")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP3A4/5
# I'm confused about these being listed as CYP3A4/5, we should discuss this. For now, I have listed them as cyp3a4 and mentioned CYP3A5 in the quote...
for elt in ["ketoconazole", "itraconazole"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4/5 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
for elt in ["azamulin", "troleandomycin", "verapamil"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "cyp3a4")
    e = Evidence(ev)
    if elt == "azamulin":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4/5 for in vitro experiments. Azamulin is a specific time-dependent inhibitor of CYP3A4/5. See Table 1 and footnote 6 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4/5 for in vitro experiments. See Table 1 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "cyp3a4")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4/5 for in vitro experiments at a K_i range of 0.0037micM to 0.18micM. See Table 1 on the FDA website. \n\n0.0037micM/L X 1M/10^6micM X 531.430920g/M = 0.0000019662944g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0000019662944")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("itraconazole", "inhibition_constant", "cyp3a4")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical inhibitor of CYP3A4/5 for in vitro experiments at K_i's of 0.27micM and 2.3micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 705.633420g/M = 0.0001905210234g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0001905210234")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("troleandomycin", "inhibition_constant", "cyp3a4")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4/5 for in vitro experiments at K_i's of 0.27micM and 2.3micM. See Table 1 on the FDA website. \n\n0.27micM/L X 1M/10^6micM X 813.968380g/M = 0.0002197714626g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0002197714626")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "cyp3a4")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of CYP3A4/5 for in vitro experiments at K_i's of 10micM and 24micM. See Table 1 on the FDA website. \n\n10micM/L X 1M/10^6micM X 454.601620g/M = 0.0045460162g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/8/2015", val = "0.0045460162")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
################ IN VITRO CYP SUBSTRATES ##################
###########################################################
# in_vitro_probe_substrate_of_enzyme is used here for substrate rules
# need to develop an affinity_constant assertion to be able to use all of the Km that we got from the FDA website
# also, all of these names seem like they need to be changed to work in the system, please let me know how/what do to about this

##### CYP1A2
a = Assertion("phenacetin-O-deethylation", "in_vitro_probe_substrate_of_enzyme", "cyp1a2")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP1A2 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["7-ethoxyresorufin-O-deethylation", "theophylline-N-demethylation", "caffeine-3-N-demethylation", "tacrine 1-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP1A2 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2A6
for elt in ["coumarin-7-hydroxylation", "nicotine C-oxidation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2a6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2A6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2B6
for elt in ["efavirenz hydroxylase", "bupropion-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2B6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["propofol hydroxylation", "S-mephenytoin-N-demethylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2B6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C8
a = Assertion("taxol 6-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C8 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["amodiaquine N-deethylation", "rosiglitazone para-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c8")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C8 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C9
for elt in ["tolbutamide methyl-hydroxylation", "S-warfarin 7-hydroxylation", "diclofenac 4’-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C9 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["flurbiprofen 4’-hydroxylation", "phenytoin-4-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C9 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C19
a = Assertion("S-mephenytoin 4’-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2C19 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["omeprazole 5-hydroxylation", "fluoxetine O-dealkylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2C19 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6
for elt in ["( ± )-bufuralol 1’-hydroxylation", "dextromethorphan O-demethylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2D6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("debrisoquine 4-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2D6 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2E1
a = Assertion("chlorzoxazone 6-hydroxylation", "in_vitro_probe_substrate_of_enzyme", "cyp2e1")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP2E1 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["p-nitrophenol 3-hydroxylation", "lauric acid 11-hydroxylation", "aniline 4-hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp2e1")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP2E1 for in vitro experiments. See Table 2 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP3A4
for elt in ["midazolam 1-hydroxylation", "testosterone 6 b -hydroxylation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is a preferred chemical substrate of CYP3A4/5 for in vitro experiments. See Table 2 on the FDA website. Guidelines also recommend use of 2 structurally unrelated CYP3A4/5 substrates for evaluation of in vitro CYP3A inhibition. If the drug inhibits at least one CYP3A substrate in vitro, then in vivo evaluation is warranted.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["erythromycin N-demethylation", "dextromethorphan N-demethylation", "triazolam 4-hydroxylation", "terfenadine C-hydroxylation", "nifedipine oxidation"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of CYP3A4/5 for in vitro experiments. See Table 2 on the FDA website. Guidelines also recommend use of 2 structurally unrelated CYP3A4/5 substrates for evaluation of in vitro CYP3A inhibition. If the drug inhibits at least one CYP3A substrate in vitro, then in vivo evaluation is warranted.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "2/2/2015")
    a.insertEvidence("for",e)
    ev.addAssertion(a)
    
###########################################################
############## IN VITRO TRANSPORT ENTRIES  ################
###########################################################
######## P-gp Substrates
######## still need a rule to put in the Km values

for elt in ["digoxin", "loperamide", "quinidine", "vinblastine", "talinolol"]:
    a = Assertion(elt, "in_vitro_probe_substrate_of_enzyme", "P-gp")
    e = Evidence(ev)
    if elt == "vinblastine":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of P-gp for in vitro experiments. Vinblastine is also a substrate for MRP2 that is constitutively expressed in Caco-2, and wild type MDCK and LL-CPK1 cells. See Table 8 and footnote 'a' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical substrate of P-gp for in vitro experiments. See Table 8 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

####### P-gp Inhibitors
####### Need help figuring out which inhibition constants to use?
for elt in ["cyclosporine A", "ketoconazole", "zosuquidar trichloride", "nelfinavir", "quinidine", "ritonavir", "saquinavir", "tacrolimus", "valspodar", "verapamil", "elacridar", "reserpine"]:
    a = Assertion(elt, "in_vitro_selective_inhibitor_of_enzyme", "P-gp")
    e = Evidence(ev)
    if elt == "cyclosporine A" or elt ==  "ketoconazole" or elt == "nelfinavir" or elt == "ritonavir" or elt == "saquinavir":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments. This chemical is also a CYP3A inhibitor. See Table 9 and footnote 'a' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else if elt == "quinidine":
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments. This chemical is also a CYP2D6 inhibitor. See Table 9 and footnote 'b' on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)
    else:
        e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments. See Table 9 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015")
        a.insertEvidence("for",e)
        ev.addAssertion(a)

a = Assertion_inhibition_constant("cyclosporine A", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 1.3micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n1.3micM/L X 1M/10^6micM X 1202.611240g/M = 0.001563394612g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.001563394612")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("cyclosporine A", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 0.5micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.5micM/L X 1M/10^6micM X 1202.611240g/M = 0.00060130562g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.00060130562")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("cyclosporine A", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 2.2micM using a MDCK-MDR1 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n2.2micM/L X 1M/10^6micM X 1202.611240g/M = 0.002645744728g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.002645744728")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("cyclosporine A", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 1.3micM using a LLC-PK1-MDR1 permeability assay with vinblastine as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n1.3micM/L X 1M/10^6micM X 1202.611240g/M = 0.001563394612g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.001563394612")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 1.2micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n1.2micM/L X 1M/10^6micM X 531.430920g/M = 0.000637717104g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000637717104")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ketoconazole", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 5.3micM using a LLC-PK1-MDR1 permeability assay with vinblastine as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n5.3micM/L X 1M/10^6micM X 531.430920g/M = 0.002816583876g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.002816583876")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("zosuquidar trihydrochloride", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 0.024micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.024micM/L X 1M/10^6micM X 636.987066g/M = 0.000015287689584g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000015287689584")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("nelfinavir", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 1.4micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n1.4micM/L X 1M/10^6micM X 567.782400g/M = 0.00079489536g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.00079489536")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 2.2micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n2.2micM/L X 1M/10^6micM X 324.416760g/M = 0.000713716872g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000713716872")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 3.2micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n3.2micM/L X 1M/10^6micM X 324.416760g/M = 0.001038133632g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.001038133632")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("quinidine", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 8.6micM using a MDCK-MDR1 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n8.6micM/L X 1M/10^6micM X 324.416760g/M = 0.002789984136g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.002789984136")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("ritonavir", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 3.8micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n3.8micM/L X 1M/10^6micM X 720.944220g/M = 0.002739588036g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.002739588036")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("saquinavir", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 6.5micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n6.5micM/L X 1M/10^6micM X 670.840800g/M = 0.0043604652g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.0043604652")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("tacrolimus", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 0.74micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.74micM/L X 1M/10^6micM X 804.018160g/M = 0.0005949734384g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.0005949734384")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("valspodar", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 0.11micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.11micM/L X 1M/10^6micM X 1214.621940g/M = 0.0001336084134g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.0001336084134")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at an IC50 of 2.1micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n2.1micM/L X 1M/10^6micM X 454.601620g/M = 0.000954663402g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000954663402")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 8micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n8micM/L X 1M/10^6micM X 454.601620g/M = 0.00363681296g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.00363681296")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 15micM using a MDCK-MDR1 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n15micM/L X 1M/10^6micM X 454.601620g/M = 0.0068190243g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.0068190243")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("verapamil", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 23micM using a LLC-PK1-MDR1 permeability assay with vinblastine as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n23micM/L X 1M/10^6micM X 454.601620g/M = 0.01045583726g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.01045583726")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("elacridar", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 0.4micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.4micM/L X 1M/10^6micM X 563.642920g/M = 0.000225457168g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000225457168")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("elacridar", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 0.4micM using a MDCK-MDR1 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n0.4micM/L X 1M/10^6micM X 563.642920g/M = 0.000225457168g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.000225457168")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("reserpine", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 1.4micM using a Caco-2 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n1.4micM/L X 1M/10^6micM X 608.678700g/M = 0.00085215018g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.00085215018")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion_inhibition_constant("reserpine", "inhibition_constant", "P-gp")
e = In_vitro_inhibition_study(ev)
e.create(doc_p = "http://www.fda.gov/drugs/developmentapprovalprocess/developmentresources/druginteractionslabeling/ucm093664.htm#cypEnzymes", q = "The FDA guidelines suggest that this is an acceptable chemical inhibitor of P-gp for in vitro experiments at a Ki of 11.5micM using a MDCK-MDR1 permeability assay with digoxin as a P-gp substrate. See Table 9 and the footnotes on the FDA website. \n\n11.5micM/L X 1M/10^6micM X 608.678700g/M = 0.00699980505g/L", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "6/9/2015", val = "0.00699980505")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
############### OTHER USEFUL CODE #########################
###########################################################

## Using 'http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf' as the doc_pointer for now
# We also have the file saved and can link to DropBox if these guidelines are removed from public access
## That link is as follows: 'https://dl.dropboxusercontent.com/u/4516186/FDA-guidance-to-industry-on-drug-interaction-studies-ucm292362-February2012.pdf'

#Sample for a change from 2006 to 2012 without removing the entry, test case is as follows: 
ev.objects['fluconazole_inhibits_cyp2c9'].evidence_for[1].doc_pointer
#Returns fda2006a, so to change it to 2012, we would simply use the following code:
ev.objects['fluconazole_inhibits_cyp2c9'].evidence_for[1].doc_pointer = 'http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf'
#And to correct the quote, we would use the following code:
ev.objects['fluconazole_inhibits_cyp2c9'].evidence_for[1].quote = '"The FDA guidelines suggest that this is a moderate in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website."'

#create a list of evidence items supported by data from fda2006 guidelines... there are so many 'or' statements to cover typos
doc_fda = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            doc_fda[v] = 'supports: ' + e
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            doc_fda[v] = 'supports: ' + e

#remove all the evidence based on fda2006 information
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            v.evidence_for.remove(it)
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            v.evidence_against.remove(it)

#create list of evidence that has fda2006 data as a supported assumption my guess for this is to create a list of all evidence claims that are supported by fda2006, then compare that to the assumptions for every item, and make a second list of those which have the fda2006 claims in their assumptions... should just be a for loop within a for loop
e_list = []
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            if e_list.count(e) == 0:
                e_list.append(e)
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a' or it.doc_pointer == 'http://dl.dropbox.com/u/4516186/FDA-Guidance-Drug-Interaction-Studies%E2%80%93Study%20Design-Data-Analysis-and-Implications-2006.pdf':
            if e_list.count(e) == 0:
                e_list.append(e)
dep_list = []
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if len(it.assumptions.getEntries()) > 0:
            for assum in it.assumptions.getEntries():
                if e_list.count(assum) > 0 and dep_list.count(assum) == 0:
                    dep_list.append(assum)
    for it in v.evidence_against:
         if len(it.assumptions.getEntries()) > 0:
            for assum in it.assumptions.getEntries():
                if e_list.count(assum) > 0 and dep_list.count(assum) == 0:
                    dep_list.append(assum)

# generate the local html output (incomplete)
##   make web-pages 
# use this command in Konsole

############################################################
# Examples of how to query statistics
############################################################

######### TALLYING EVIDENCE TYPES
non_default_asrts = {
    "bioavailability":  None,
    "controls_formation_of": None,
    "first_pass_effect": None,
    "fraction_absorbed": None,
    "has_metabolite": None,
    "increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    "maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    }

for asrt_tp in non_default_asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    for k,v in ev.objects.iteritems():                  
        if k.find(asrt_tp) != -1:
            if asrt_tp == 'substrate_of' and k.find("is_not") != -1:
                print "\tskipping %s because it is not the 'substrate_of' assertions\n" % k
                continue

            if asrt_tp == 'substrate_of' and k.find("in_vitro_probe") != -1:
                print "\tskipping %s because it is not the 'substrate_of' assertions\n" % k
                continue
            
            if v.assert_by_default == True:
                print "\tskipping %s because it is a default assumption\n" % k
                continue

            print "\t%s" % k
            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                print "\t\t(for) %s" % e.evidence_type.value
            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1
                print "\t\t(against) %s" % e.evidence_type.value
    tot = 0.0
    for k,v in et_for.iteritems():
        tot += v
        
    print "%d types found 'for' %s assertions (total items: %d):" % (len(et_for.keys()), asrt_tp, tot)
    for k,v in et_for.iteritems():
        print "\ttype: %s, %d/%d = %.2f" % (k, v, tot, float(v)/float(tot))

    tot = 0.0
    for k,v in et_against.iteritems():
        tot += v
    print "\n%d types found 'against' %s assertions (total items: %d):" % (len(et_against.keys()), asrt_tp, tot)
    for k,v in et_against.iteritems():
        print "\ttype: %s, %d/%d = %.2f" % (k, v, tot, float(v)/float(tot))


######### GET ALL DOC_POINTERS CURRENTLY IN THE DIKB ###############
doc_d = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        doc_d[it.doc_pointer] = None
    for it in v.evidence_against:
        doc_d[it.doc_pointer] = None



##################################################################################### 
#  identify and classify all non-redundant assertions including
#  default assumptions
#####################################################################################

clinical_types = ["EV_CT_PK_Genotype", "EV_PK_DDI_RCT", "EV_CT_Pharmacokinetic", "EV_PK_DDI_Par_Grps", "EV_PK_DDI_NR"]
non_traceable_types = ["Non_traceable_Drug_Label_Statement", "Non_Tracable_Statement"]
#non_traceable_types = ["Non_traceable_Drug_Label_Statement"]
in_vitro_types = ["EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Recom", "EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Microsome", "EV_EX_Met_Enz_ID", "EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem", "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom"]

asrts = {
    "bioavailability":  None,
    "controls_formation_of": None,
    "first_pass_effect": None,
    "fraction_absorbed": None,
    "has_metabolite": None,
    "increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    "maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    "polymorphic_enzyme":None,
    "does_not_permanently_deactivate_catalytic_function":None,
    "permanently_deactivates_catalytic_function":None,
    "in_vitro_probe_substrate_of_enzyme":None,
    "in_vitro_selective_inhibitor_of_enzyme":None,
    "in_viVo_selective_inhibitor_of_enzyme":None,
    "pceut_entity_of_concern":None,
    "sole_PK_effect_alter_metabolic_clearance":None,
    }


for asrt_tp in asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    (for_clin_cnt, for_non_trac_cnt, for_in_vitro_cnt) = (0,0,0)
    (against_clin_cnt, against_non_trac_cnt, against_in_vitro_cnt) = (0,0,0)
    a_cnt = 0
    default = 0
    
    for k,v in ev.objects.iteritems():                  
        if k.find(asrt_tp) != -1:
            if k.find("is_not_substrate_of") != -1 or k.find("does_not_inhibit") != -1:
                print "\tskipping %s because it is not a non-redundant or default evidence evidence item\n" % k
                continue

            if asrt_tp == "substrate_of" and k.find("in_vitro_probe_substrate_of_enzyme") != -1:
                continue
           
            if v.assert_by_default == True:
                default += 1

            a_cnt += 1
            print "\t%s" % k

            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                print "\t\t(for) %s" % e.evidence_type.value
                
                if e.evidence_type.value in clinical_types:
                    for_clin_cnt += 1
                elif e.evidence_type.value in non_traceable_types:
                    for_non_trac_cnt += 1
                elif e.evidence_type.value in in_vitro_types:
                    for_in_vitro_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               
         

            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1
                print "\t\t(against) %s" % e.evidence_type.value

                if e.evidence_type.value in clinical_types:
                    against_clin_cnt += 1
                elif e.evidence_type.value in non_traceable_types:
                    against_non_trac_cnt += 1
                elif e.evidence_type.value in in_vitro_types:
                    against_in_vitro_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               

    r_str = ""
                
    for_tot = 0.0
    for k,v in et_for.iteritems():
        for_tot += v
    print "%d types found 'for' %s assertions (total items: %d):" % (len(et_for.keys()), asrt_tp, for_tot)
    for k,v in et_for.iteritems():
        print "\ttype: %s, %d/%d = %.0f" % (k, v, for_tot, float(v)/float(for_tot))

    r_str +=  "%s & %s & %s & " % (asrt_tp, default, a_cnt)
    if for_tot == 0:
        r_str +=  "FOR: 0 & 0 & 0 & 0 &"
    else:
        r_str +=  "FOR: %s & %.0f & %.0f & %.0f \\\\" % (for_tot, float(for_clin_cnt)/float(for_tot) * 100, float(for_in_vitro_cnt)/float(for_tot) * 100, float(for_non_trac_cnt)/float(for_tot) * 100)

    against_tot = 0.0
    for k,v in et_against.iteritems():
        against_tot += v
    print "\n%d types found 'against' %s assertions (total items: %d):" % (len(et_against.keys()), asrt_tp, against_tot)
    for k,v in et_against.iteritems():
        print "\ttype: %s, %d/%d = %.0f" % (k, v, against_tot, float(v)/float(against_tot))

    r_str += "AGAINST: %s & " % against_tot
    if against_tot == 0:
        r_str +=  " 0 & 0 & 0 \\"
    else:
        r_str +=  " %.0f & %.0f & %.0f \\" % (float(against_clin_cnt)/float(against_tot) * 100, float(against_in_vitro_cnt)/float(against_tot) * 100, float(against_non_trac_cnt)/float(against_tot) * 100)

    print r_str
############################ END OF QUERIES TO SUPPORT STATISTICS OF THE EVIDENCE BASE ####################### 



