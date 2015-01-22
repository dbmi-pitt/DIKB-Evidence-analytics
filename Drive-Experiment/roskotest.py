### SAM ROSKO'S TEST FILE FOR WORKING ON DIKB
### LAST UPDATED: 1/22/2015
### RECENTLY ADDED: Code to add new inhibitor data, started working with substrate data

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
############ TRIAL INHIBITOR DATA ENTRIES #################
###########################################################

###### CYP1A2 inhibitor entries
for elt in ["ciprofloxacin", "fluvoxamine"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["methoxsalen", "mexiletine", "phenypropanolamine", "vemurafenib", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["acyclovir", "allopurinol", "caffeine", "cimetidine", "disulfiram", "famotidine", "norfloxacin", "propafeonone", "propranolol", "terbinafine", "ticlopidine", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP1A2. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2B6 "inhibitor" entries
for elt in ["clopidogrel", "ticlopidine", "prasugrel"]:
    a = Assertion(elt, "inhibits", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2B6. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C8 "inhibitor" entries
a = Assertion("gemfibrozil", "inhibits", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C8. Gemfibrozil also inhibits OATP1B1. For more information, see Table 3 on page 41, footnote 6 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

###### CYP2C9 "inhibitor" entries
for elt in ["amiodarone", "fluconazole", "miconazole", "oxandrolone"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["capecitabine", "cotrimoxazole", "etravirine", "fluvastatin", "fluvoxamine", "metronidazole", "sulfinpyrazone", "tigecycline", "voriconazole", "zafirlukast"]:
    a = Assertion(elt, "inhibits", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C9. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP2C19 "inhibitor" entries
a = Assertion("fluconazole", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19 based on the AUC ratio of omeprazole, which is also metabolized by CYP3A. For more information, see Table 3 on page 41, footnote 7 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("fluvoxamine", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Fluvoxamine strongly inhibits CYP1A2 and CYP2C19, but it also inhibits CYP2C8/CYP2C9 and CYP3A. For more information, see Table 3 on page 41, footnote 8 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("ticlopidine", "inhibits", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2C19. Ticlopidine strongly inhibits CYP2C19, but it also inhibits CYP3A, CYP2B6, and CYP1A2. For more information, see Table 3 on page 41, footnote 9 on page 42, and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["esomeprazole", "fluoxetine", "omeprazole", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["armodafinil", "cimetidine", "etravirine", "felbamate", "ketoconazole"]:
    a = Assertion(elt, "inhibits", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2C19. For more information, see Table 3 on page 41 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###### CYP3A4 "inhibitor" entries
for elt in ["boceprevir", "clarithromycin", "conivaptan", "indinavir", "itraconazole", "ketoconazole", "lopinavir/ritonavir", "nefazodone"
"nelfinavir", "posaconazole", "ritonavir", "saquinavir", "telaprevir", "telithromycin", "voriconazole"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP3A4. For more information, see Table 3 on pages 41/42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amprenavir", "aprepitant", "atazanavir", "ciprofloxacin", "crizotinib", "darunavir/ritonavir", "diltiazem", "erythromycin", "fluconazole", "fosamprenavir", "imatinib", "verapamil"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alprazolam", "amiodarone", "amlodipine", "atorvastatin", "bicalutamide", "cilostazol", "cimetidine", "cyclosporine", "fluoxetine", "fluvoxamine", "isoniazid", "lapatinib", "nilotinib", "pazopanib", "ranitidine", "ranolazine", "tipranavir/ritonavir", "zileuton"]:
    a = Assertion(elt, "inhibits", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP3A4. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 "inhibitor" entries
for elt in ["bupropion", "fluoxetine", "paroxetine", "quinidine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'strong' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["cinacalcet", "duloxetine", "terbinafine"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'moderate' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["amiodarone", "celecoxib", "clobazam", "cimetidine", "desvenlafaxine", "diltiazem", "diphenhydramine", "escitalopram", "febuxostat", "gefitinib", "hydralazine", "hydroxychloroquine", "imatinib", "methadone", "pazopanib", "propafenone", "ranitidine", "ritonavir", "sertraline", "telithromycin", "verapamil", "vemurafenib"]:
    a = Assertion(elt, "inhibits", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'weak' in vivo inhibitor of CYP2D6. For more information, see Table 3 on page 42 and also see Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/05/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###########################################################
############ TRIAL SUBSTRATE DATA ENTRIES #################
###########################################################

###### CYP1A2 substrate entries
for elt in ["alosetron", "caffeine", "duloxetine", "melatonin", "ramelteon", "tacrine", "tizanidine"]:
    a = Assertion(elt, "substrate_of", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP1A2. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["theophylline", "tizanidine"]:
    a = Assertion(elt, "substrate_of", "cyp1a2")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP1A2 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2B6 substrate entries
for elt in ["bupropion", "efavirenz"]:
    a = Assertion(elt, "substrate_of", "cyp2b6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2B6. The AUC of this compound was not increased by 5-fold or more with a CYP2B6 inhibitor, but it represents the most sensitive substrate studied with available inhibitors evaluated to date. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C8 substrates
a = Assertion("repaglinide", "substrate_of", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C8. Repaglinide is also a substrate for OATP1B1, and it is only suitable as a CYP2C8 substrate if the inhibition of OATP1B1 by the investigational drug has been ruled out. For more information, see Table 5 on page 44, footnote 5 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("paclitaxel", "substrate_of", "cyp2c8")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C8 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP2C9 substrates
a = Assertion("celecoxib", "substrate_of", "cyp2c9")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C9. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["warfarin", "phenytoin"]:
    a = Assertion(elt, "substrate_of", "cyp2c9")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C9 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2C19 substrates
for elt in ["lansoprazole", "omeprazole", "S-mephenytoin"]:
    a = Assertion(elt, "substrate_of", "cyp2c19")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2C19. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("S-mephenytoin", "substrate_of", "cyp2c19")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2C19 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

##### CYP3A4 substrates
for elt in ["alfentanil", "aprepitant", "budesonide", "buspirone", "conivaptan", "darifenacin", "darunavir", "dasatinib", "dronedarone", "eletriptan", "eplerenone", "everolimus", "felodipine", "indinavir", "fluticasone", "lopinavir", "lovastatin", "lurasidone", "maraviroc", "midazolam", "nisoldipine", "quetiapine", "saquinavir", "sildenafil", "simvastatin", "sirolimus", "tolvaptan", "tipranavir", "triazolam", "vardenafil", "ticagrelor"]:
    a = Assertion(elt, "substrate_of", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP3A4. Because a number of CYP3A substrates (e.g., darunavir, maraviroc) are also substrates of P-gp, the observed increase in exposure could be due to inhibition of both CYP3A and P-gp. For more information, see Table 5 on page 44, footnote 6 from Table 5, and Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

for elt in ["alfentanil", "cyclosporine", "dihydroergotamine", "ergotamine", "fentanyl", "pimozide", "quinidine", "sirolimus", "tacrolimus"]:
    a = Assertion(elt, "substrate_of", "cyp3a4")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP3A4 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### CYP2D6 substrate entries
for elt in ["atomoxetine", "desipramine", "dextromethorphan", "metoprolol", "nebivolol", "perphenazine", "tolterodine", "venlafaxine"]:
    a = Assertion(elt, "substrate_of", "cyp2d6")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is a 'sensitive' in vivo substrate of CYP2D6. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("thioridazine", "substrate_of", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44 and also see Table 7 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("pimozide", "substrate_of", "cyp2d6")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of CYP2D6 with a narrow therapeutic range. For more information, see Table 5 on page 44.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/12/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

###########################################################
############ TRANSPORT PROTEIN DATA ENTRIES ###############
###########################################################

###### P-gp both inhibitors and substrates, going to have to add it to the system as an enzyme
##### also, going to need to replace the name P-gp

for elt in ["amiodarone", "captopril", "carvedilol", "clarithromycin", "conivaptan", "cyclosporine", "diltiazem", "dronedarone", "felodipine", "itraconazole", "lopinavir/ritonavir", "quinidine", "ranolazine", "ticagrelor", "verapamil"]:
    a = Assertion(elt, "inhibits", "P-gp")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in digoxin AUC. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

a = Assertion("azithromycin", "inhibits", "P-gp")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in fexofenadine AUC. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("erythromycin", "inhibits", "P-gp")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in talinolol AUC. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("ketoconazole", "inhibits", "P-gp")
e = Evidence(ev)
e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of P-gp because this showed a >25% increase in fexofenadine AUC. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
a.insertEvidence("for",e)
ev.addAssertion(a)

for elt in ["aliskiren", "ambrisentan", "colchicine", "dabigatran", "etexilate", "digoxin", "everolimus", "fexofenadine", "imatinib", "lapatinib", "maraviroc", "nilotinib", "posaconazole", "ranolazine", "saxagliptin", "sirolimus", "sitagliptin", "talinolol", "tolvaptan", "topotecan"]:
    a = Assertion(elt, "substrate_of", "P-gp")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo substrate of P-gp. For more information, see Table 7 on page 51 and also see Table 13 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

##### OATP1B1 inhibitors then substrates

for elt in ["cyclosporine", "eltrombopag", "gemfibrozil"]:
    a = Assertion(elt, "inhibits", "OATP1B1")
    e = Evidence(ev)
    e.create(doc_p = "http://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm292362.pdf", q = "The FDA guidelines suggest that this is an in vivo inhibitor of OATP1B1 because this showed a >25% increase in digoxin AUC. For more information, see Table 6 on page 49 and also see Table 12 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "hines", timestamp = "1/15/2014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

###########################################################
##################### USEFUL CODE #########################
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



