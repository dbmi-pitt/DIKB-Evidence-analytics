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

ev = EvidenceBase("evidence","May2017")
dikb = DIKB("dikb","May2017", ev)
dikb.unpickleKB("dikb-pickles/dikb-test-two.pickle")
ev.unpickleKB("dikb-pickles/ev-test-two.pickle")

ctpk = ["EV_CT_Pharmacokinetic"]
ctpk_f = 0
ctpk_a = 0

ctpkg = ["EV_CT_PK_Genotype"]
ctpkg_f = 0
ctpkg_a = 0

ctpkr = ["EV_PK_DDI_RCT"]
ctpkr_f = 0
ctpkr_a = 0

ctpknr = ["EV_PK_DDI_NR"]
ctpknr_f = 0
ctpknr_a = 0

ctpknrp = ["EV_PK_DDI_Par_Grps"]
ctpknrp_f = 0
ctpknrp_a = 0

ivr = ["EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Recom"]
ivr_f = 0
ivr_a = 0

ivhm = ["EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Microsome"]
ivhm_f = 0
ivhm_a = 0

ivei = ["EV_EX_Met_Enz_ID"]
ivei_f = 0
ivei_a = 0

iveihr = ["EV_EX_Met_Enz_ID_Cyp450_Hum_Recom"]
iveihr_f = 0
iveihr_a = 0

iveihm = ["EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem"]
iveihm_f = 0
iveihm_a = 0

nts = ["Non_Tracable_Statement"]
nts_f = 0
nts_a = 0

ntdls = ["Non_traceable_Drug_Label_Statement"]
ntdls_f = 0
ntdls_a = 0

for e,v in ev.objects.iteritems():
	for evid in v.evidence_for:
		if evid.evidence_type.value in ctpk:
			ctpk_f = ctpk_f + 1
		if evid.evidence_type.value in ctpkg:
			ctpkg_f = ctpkg_f + 1
		if evid.evidence_type.value in ctpkr:
			ctpkr_f = ctpkr_f + 1
		if evid.evidence_type.value in ctpknr:
			ctpknr_f = ctpknr_f + 1
		if evid.evidence_type.value in ctpknrp:
			ctpknrp_f = ctpknrp_f + 1
		if evid.evidence_type.value in ivr:
			ivr_f = ivr_f + 1
		if evid.evidence_type.value in ivhm:
			ivhm_f = ivhm_f + 1
		if evid.evidence_type.value in ivei:
			ivei_f = ivei_f + 1
		if evid.evidence_type.value in iveihr:
			iveihr_f = iveihr_f + 1
		if evid.evidence_type.value in iveihm:
			iveihm_f = iveihm_f + 1
		if evid.evidence_type.value in nts:
			nts_f = nts_f + 1
		if evid.evidence_type.value in ntdls:
			ntdls_f = ntdls_f + 1
	for evid in v.evidence_against:
		if evid.evidence_type.value in ctpk:
			ctpk_a = ctpk_a + 1
		if evid.evidence_type.value in ctpkg:
			ctpkg_a = ctpkg_a + 1
		if evid.evidence_type.value in ctpkr:
			ctpkr_a = ctpkr_a + 1
		if evid.evidence_type.value in ctpknr:
			ctpknr_a = ctpknr_a + 1
		if evid.evidence_type.value in ctpknrp:
			ctpknrp_a = ctpknrp_a + 1
		if evid.evidence_type.value in ivr:
			ivr_a = ivr_a + 1
        if evid.evidence_type.value in ivhm:
			ivhm_a = ivhm_a + 1
        if evid.evidence_type.value in ivei:
			ivei_a = ivei_a + 1
        if evid.evidence_type.value in iveihr:
			iveihr_a = iveihr_a + 1
        if evid.evidence_type.value in iveihm:
			ivr_a = ivr_a + 1
        if evid.evidence_type.value in nts:
			nts_a = nts_a + 1
        if evid.evidence_type.value in ntdls:
			ntdls_a = ntdls_a + 1

print ('cptk_f: ',ctpk_f,' ctpk_a: ', ctpk_a)
print ('ctpkg_f: ',ctpkg_f,' ctpkg_a: ', ctpkg_a)  
print ('ctpkr_f: ',ctpkr_f,' ctpkr_a: ', ctpkr_a)  
print ('ctpknr_f: ',ctpknr_f,' ctpknr_a: ', ctpknr_a)  
print ('ctpknrp_f: ',ctpknrp_f,' ctpknrp_a: ', ctpknrp_a)
print ('ivr_f: ',ivr_f,' ivr_a: ', ivr_a)	 
print ('ivhm_f: ',ivhm_f,' ivhm_a: ', ivhm_a)	 
print ('ivei_f: ',ivei_f,' ivei_a: ', ivei_a)	 
print ('iveihr_f: ',iveihr_f,' iveihr_a: ', iveihr_a)	 
print ('iveihm_f: ',iveihm_f,' iveihm_a: ', iveihm_a)		 
print ('nts_f: ',nts_f,' nts_a: ',nts_a)
print ('ntdls_f: ',ntdls_f,' ntdls_a: ',ntdls_a)
