# Description - Sam Rosko's File to Update Entities in the DIKB
# Last Update - 6/30/2015
# To Do - run for final DB

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

ev = load_ev_from_db(ident)

dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("dikb-pickles/dikb-03052012.pickle")

for i in ["acyclovir", "aliskiren", "allopurinol", "ambrisentan", "armodafinil", "atrasentan", "azithromycin", "bicalutamide", "boceprevir", "clobazam", "conivaptan", "crizotinib", "dabigatran", "darifenacin", "darunavir", "dihydroergotamine", "dronedarone", "eltrombopag", "esomeprazole", "etravirine", "everolimus", "ezetimibe", "famotidine", "febuxostat", "fluticasone", "hydralazine", "lurasidone", "maraviroc", "melatonin", "nebivolol", "oxandrolone", "pazopanib", "phenylpropanolamine", "pilocarpine", "pitavastatin", "quercetin", "ramelteon", "ranitidine", "reserpine", "saxagliptin", "sitagliptin", "telaprevir", "ticagrelor", "tigecycline", "tipranavir", "tizanidine", "tolvaptan", "topotecan", "vemurafenib", "irinotecan", "diethyldithiocarbamate", "phencyclidine", "talinolol", "tranylcypromine", "valspodar", "zosuquidar", "elacridar", "sulfaphenazole", "dabigatran-etexilate"]:
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

ev.renotifyObservers()

dikb.pickleKB("dikb-pickles/dikb-test.pickle")
ev.pickleKB("dikb-pickles/ev-test.pickle")
