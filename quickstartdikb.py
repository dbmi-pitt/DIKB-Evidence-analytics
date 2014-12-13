# quickstartdikb.py
#
# 10/23/2014
#
# a quick-start script to load the DIKB knowledge base and evidence
# base from the SQL database

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

## CODE TO RELOAD THE KB AND EB AND RESET ALL OBSERVERS; NOT NECESSARY
## IF ONLY ADDING INFORMATION TO THE EB 
#dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/dikb.pickle")
ev.renotifyObservers()

# NOTE: A test that this worked properly would be to compare
# dikb.objects['bupropion'].increases_auc.evidence with
# ev.objects['bupropion_increases_auc_desipramine'] to confirm that
# the two objects are the exactly the same in memory. For example,
#>>> dikb.objects['bupropion'].increases_auc.evidence
#[<DIKB.EvidenceModel.ContValAssertion object at 0x7fb4e76e2710>]
#>>> ev.objects['bupropion_increases_auc_desipramine']
#<DIKB.EvidenceModel.ContValAssertion object at 0x7fb4e76e2710>

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

exportAssertions(ev, dikb, "/tmp/assertions.lisp")
assessBeliefCriteria(dikb, ev, "/tmp/changing_assumptions.lisp")

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
############################ END OF ANALYSIS TO SUPPORT SPINA REVIEWS ####################### 
