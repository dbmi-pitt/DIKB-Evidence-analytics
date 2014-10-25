
## The Drug Interaction Knowledge Base (DIKB) is (C) Copyright 2005 by
## Richard Boyce

## Original Authors:
##   Richard Boyce

## This library is free software; you can redistribute it and/or
## modify it under the terms of the GNU Library General Public
## License as published by the Free Software Foundation; either
## version 2 of the License, or (at your option) any later version.

## This library is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Library General Public License for more details.

## You should have received a copy of the GNU Library General Public
## License along with this library; if not, write to the
## Free Software Foundation, Inc., 59 Temple Place - Suite 330,
## Boston, MA 02111-1307, USA.

## -----------------------------------------------------------------
## File:          ExportAssertions.py

import re, os, sys

from DIKB import *
from DrugModel import *
from EvidenceModel import *
from DIKB_Utils import *
from TranslationRules import *

# ev = EvidenceBase("evidence","123")
# dikb = DIKB("dikb","123", ev)
# dikb.unpickleKB("../var/DIKB/dikb.pickle")

## Currently not necessary
# ev.unpickleKB("../var/evidence-base/ev.pickle")
# ev.renotifyObservers()


# this is a list of assertion types that we will process
ASSERT_L = ['substrate_of', 'is_not_substrate_of', 'inhibits','bioavailability', 'first_pass_effect', 'fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration', 'does_not_inhibit', 'primary_total_clearance_mechanism', 'primary_metabolic_clearance_enzyme', 'primary_total_clearance_enzyme', 'in_vitro_probe_substrate_of_enzyme', 'in_vitro_selective_inhibitor_of_enzyme', 'pceut_entity_of_concern', 'does_not_permanently_deactivate_catalytic_function', 'permanently_deactivates_catalytic_function', 'sole_PK_effect_alter_metabolic_clearance', 'has_metabolite', 'controls_formation_of', 'polymorphic_enzyme', 'in_viVo_selective_inhibitor_of_enzyme', 'in_viVo_probe_substrate_of_enzyme', 'prodrug', 'metabolite', 'active_ingredient', 'minimum_therapeutic_dose', 'maximum_therapeutic_dose', 'assumed_effective_dose']

# this is a dict whose keys are assertions that have been exported to the jtms
exported_asrts = {}

def reset_evidence_rating(ev, dikb):
    """Reset the state of the evidence base to its initial state before
    any evidence has been classified """
    exported_asrts.clear()
    
    for key,obj in ev.objects.iteritems():
        ev.objects[key].evidence_rating = "none_assigned"

    for key, obj in dikb.objects.iteritems():
        for slot_name, slot_obj in obj.__dict__.iteritems():
            if (type(slot_obj) in ([EMultiSlot] + EMultiSlot().__class__.__subclasses__())):
                slot_obj.value = ["none_assigned"]

            elif (type(slot_obj) in ([ESlot] + ESlot().__class__.__subclasses__())):
                slot_obj.value = "none_assigned"

def importLOEs_and_bc(filename):
    l_d = {'loe_d':None, 'bc_d':None}
    try:
        execfile(filename, l_d)
    except IOError, err:
        error(" ".join(["ExportAssertions::importrules - Could not execute file containing levels-of-evidence and belief criteria at:", os.getcwd() + filename,
                          "Please make sure this file exists. Returning None"]))
        return (1, "ExportAssertions::importrules - Could not execute file containing levels-of-evidence and belief criteria at %s" % (os.getcwd() + filename))

    return (0, (l_d['loe_d'], l_d['bc_d']))

def getBeliefCriteria(assertion_str, loe_d, bc_d):
    """ returns a tuple containing two elements; the first element  contains the belief criteria for the evidence_for the assertion while the second contains belief criteria for evidence against
    """
    bc_lv = bc_d[assertion_str]
    if not (type(bc_lv) == type(())):
        # belief criteria are the same for evidence_for and
        # evidence_against
        bc_l = loe_d[assertion_str][0:bc_lv]
        bc_cm = reduce(lambda x,y: x + y, bc_l)
        return (bc_cm, bc_cm)

    # belief criteria are NOT the same for evidence_for and
    # evidence_against
    bc_ev_for_l = loe_d[bc_lv[0][0]][0:bc_lv[0][1]]
    bc_ev_for_cm = reduce(lambda x,y: x + y, bc_ev_for_l)

    bc_ev_against_l = loe_d[bc_lv[1][0]][0:bc_lv[1][1]]
    bc_ev_against_cm = reduce(lambda x,y: x + y, bc_ev_against_l)

    return (bc_ev_for_cm, bc_ev_against_cm)

def importRules(filename):
    """ DEPRECATED (11/17/2007), use importLOEs_and_bc
    """
    try:
        rulesF = open(filename, 'r')
    except IOError, err:
        error(" ".join(["ExportAssertions::importrules - Could not open file rule file at:", os.getcwd(),filename,
                          "Please make sure this file exists. Returning None"]))
        return None
    rules = []
    ln = rulesF.readline()
    while ln != "":
        rule = ln.split('\n')[0]
        if rule == '':
            break
        rules.append(rule)
        ln = rulesF.readline()
    
    rulesF.close()
    return rules

def importRankingCategories(filename):
    try:
        rankF = open(filename, 'r')
    except IOError, err:
        error(" ".join(["Could not open file containing ranking categories at:", os.getcwd(),filename,
                          "Please make sure this file exists. Returning None"]))
        return None
    
    """Import ranking categories"""
    ranking_categories = {}
    content = rankF.readline()
    while content != "":
        ln = content.split('-')
        cat_name = ln[0]
        str_ev_types = ln[1].split('\n')[0]
        l_ev_types = str_ev_types.split(',')
        ev_types = Set(l_ev_types)
        ranking_categories[cat_name] = ev_types

        content = rankF.readline()

    rankF.close()
    return ranking_categories

def exportAssertions(ev, dikb,  path_to_file, categoricals = "True", in_vitro_ok = "True"):
    """
    Export all categorical assertions in the evidence-base and dikb
    to the JTMS. 

    @param ev: and EvidenceBase object 
    @param dikb: a KB object 
    @param path_to_file:string - the path to a file where assertions will be written
    @param categoricals:bool - True if the function should export assertions for categorical slots
    
    """
    try:
        exportF = open(path_to_file, 'w')
    except IOError, err:
        error ("ExportAssertions::exportAssertions - can't open %s due to error:\n%s;\n no assertions will be exported." % (path_to_file, err))
        return 1

    a_list = []

    if in_vitro_ok:
        a_list.append("(assert! '(ACCEPT-IN-VITRO-BASED-ENZYME-MODULATION-ASSERTIONS) '(dikb-inference-configuration))")
    
    ## now, export categorical slots in the knowledge-base
    for ident, obj in dikb.objects.iteritems():
        name = obj._name

        for slot_name, slot_obj in obj.__dict__.iteritems():
         
            if slot_name in ASSERT_L:
                """MultiSlots and Slot instances are not
                evidence-based, so they do not have assertions in the
                evidence-base"""
                if (type(slot_obj) == MultiSlot) and categoricals == "True":
                    """multislots just pass values if they are assigned"""
                    for item in slot_obj.value:
                        if item != "none_assigned":
                            mp = get_asrt_to_jtms(ev, name, slot_name, item)
                            if not mp:
                                error("ExportAssertions::exportAssertions - Error, unable to get DIKB->JTMS mapping for %s_%s_%s " % (name, slot_name, item), 0)
                            else:
                                exported_asrts[name + slot_name + item] = None
                                a_list.append(mp + "\n")

                elif (type(slot_obj) == Slot and  categoricals == "True"):
                    """handle Slot type"""
                    if slot_obj.value != "none_assigned":
                        mp = get_asrt_to_jtms(ev, name, slot_name, slot_obj.value)
                        if not mp:
                            error("ExportAssertions::exportAssertions - Error, unable to get DIKB->JTMS mapping for %s_%s_%s " % (name, slot_name, slot_obj.value), 0)
                        else:
                            exported_asrts[name + slot_name + slot_obj.value] = None
                            a_list.append(mp + "\n")

    a_list.sort()
    for item in a_list:
        exportF.write(item + "\n")
        
    exportF.close()
    return None
    

def assessBeliefCriteria(dikb, ev, path_to_file, path_to_loes = "data/levels-of-evidence"):
    """
       Export currently believed assertions to a format readable by
       the inference engine. This function manages the belief state of
       assertions by assuming and retracting assumptions about belief
       criteria that are in the list of justifications for an
       assertion.

       This function iterates through all of the objects that are
       instances of classes inheriting from the EvidenceType class in
       the KB instance passed to it and:

       - constructs assertions for the inference engine; each
         assertion is linked to a justification representing the
         belief state of the evidence supporting an assertion. These
         belief state justifications are used to link evidence to
         assertions in the JTMS and enable the belief state of
         consequents to change as evidence meets, or fails to meet,
         the user-defined belief criteria for eachassertion type
       
       - has every evidence-based slot evaluate their evidence and
       assign themselves values.  Discrete and continuous valued slots
       combine their evidence to produce values. (TODO: This can lead
       to the problem of 'dangling' assertions - what happens if an
       assertion has been made for a continuous valued slot at one
       value and combining evidence produces another value. Shouldn't
       the assertion with the old value be deleted from the TMS?)

       - construct assume! and retract! statements to for the
         inference engine for each evidence-bases assertion whose
         belief state has changed. These statements change the label
         of the belief state justifications that are attached to each
         exported assertion

       Rules for assessing evidence come from a file containing two
       dictionaries; one holding levels-of-evidence (LOE) for each
       assertion and the other mapping each assertion to an LOE
       currently accepted as belief criteria. Thus, each slot type has
       its own rules for evaluating evidence. These rules are
       specified by regular expressions adhering to the syntax
       specified by the Python re module.
       
       Each regular expression contains patterns for combinations of
       *ranking categories*. Ranking categories are combinations of
       evidence types that are believed to have equivalent
       validity. For example, the ranking category 'non_random',
       standing for 'non-randomized clinical trial' might consist of
       evidence types case-control-1 (cc1), case-control-2 (cc2),
       fixed-order-1 (fo1), and cohort-study-1 (cs1) provided that
       these evidence types existed in the main evidence type file
       'evidence_types'. The ranking categories are stored in the file
       'ranking_categories' in the format:

       <ranking category>-<evidence type 1>,<evidence type 2>,...,<evidence type n>
       <ranking category>-<evidence type 1>,<evidence type 2>,...,<evidence type n>
       ...
       
       (NOTE: <ranking category> and the comma-seperated list of <evidence type>
        are seperated by a single '-' and no spaces)

       So, an example:

       assume the ranking categories:

       non_random-cc1,cc2,fo1,cs1
       iv-iv1,iv2
       label-lab1
       rct-rct1
       ex-ex1
       cr-cr1,cr2

       and the rules:

       (rct){1,}   (one or more randomized controlled trials)
       (lab){1,1}   (a single drug label evidence type)
       (iv){1,}.*(non_random){1,}   (one or more in vitro types AND one or more non-randomized trial types)

       and assume the set of evidence types for the relavant assertion is:
       ['fo1', 'iv2', 'rct1']

       Then, the the slot's assessEvidence method would return 'True' because
       there evidence meets the first and third rules for belief (ony one is necessary)

       NOTE: (TODO) as of 12/11/2007 you cannot specify conjuctive
       rules for any 'continuous valued' type such as bioavailability,
       max concentration, or inhibition constant. You can for any
       non-continous type such as inhibits, substrate_of, etc.

       NOTE: It is important that you specify conjunctive rules for
       belief criteria in alphabetical order. For example, the correct
       way to specify 'one or more in vitro types AND one or more
       non-randomized trial types' is:
         (iv){1,}.*(non_random){1,}

       NOT: (non_random){1,}.*(iv){1,}

       This is because the rules are applied as a regex search across
       a string that concatenates, in alphabetical order, all ranking
       categories from every evidence item that is linked to an
       assertion. For example, assuming the following evidence items
       are linked to an assertion:
          ['rct1', 'iv2',  'fo1', 'rct1']

       Then, the regex search for a belief criteria rule '(iv){1,}.*(rct){1,}'
       is applied to the following string:
           'label iv rct rct'

       Which will derive the following match objects: ('iv','rct')

       These correspond to the first set of evidence items that cause
       an assertion's evidence to meet belief criteria
       
       in: a KB object - dikb
       in: and evidence-base object - ev
       in: the path to a file where assume! and retract! statements will be written

       side-effect: assertions are written to file and values are assesed for assertions in the KB.
       
    """
    try:
        exportF = open(path_to_file, 'w')
    except IOError, err:
        error ("ExportAssertions::assessBeliefCriteria - can't open %s due to error:\n%s;\n no assertions will be exported." % (path_to_file, err))
        return 1

    ranking_categories = importRankingCategories("data/ranking_categories")
    warning("".join(["ExportAssertions::assessBeliefCriteria - loaded ranking_categories - ", str(ranking_categories)]), 3)

    (err, dat) = importLOEs_and_bc(path_to_loes)
    if err != 0:
        error ("ExportAssertions::assessBeliefCriteria - can't import LOEs and BCs due to error:\n%s;\n no assertions will be exported." % (err))
        return 1
    loe_d = dat[0]
    bc_d = dat[1]

    a_list = [] # the main list of assertions
    for ident, obj in dikb.objects.iteritems():
        name = obj._name

        for slot_name, slot_obj in obj.__dict__.iteritems():
         
            if slot_name in ASSERT_L:
                """Have the slots evaluate their evidence and assign themselves values,
                   create assertion for all values"""
                if (type(slot_obj) in ([EMultiSlot] + EMultiSlot().__class__.__subclasses__())):
                    (believable_ev_for, believable_ev_against) = getBeliefCriteria(slot_name, loe_d, bc_d)
                    warning("".join(["ExportAssertions::assessBeliefCriteria - loaded rules for believable - \nfor:",
                                     str(believable_ev_for), "\nagainst: ", str(believable_ev_against),
                                     " for slot ", slot_name]), 3)

                    changing_assumptions = []
                    changing_assumptions = slot_obj.assessEvidence(ranking_categories, believable_ev_for, believable_ev_against)
                    warning("ExportAssertions::assessBeliefCriteria - changing_assumptions = " + str(changing_assumptions), 3)

                    """if some change in belief occurred...write a
                       form for an enabled assumption for each of this
                       slot's values and their corresponding
                       assumptions
                    """
                    if len(changing_assumptions) > 0:
                        for item in changing_assumptions:
                            ## assume!, retract!, or 'can't decide'
                            action = ""
                            key = "_".join([name, slot_name, item])
                            warning( "ExportAssertions::assessBeliefCriteria - key = " + key, 3)
                            if ev.objects.has_key(key):
                                action = ev.objects[key].evidence_rating
                            else:
                                error("Error, no key in ev.objects for " + key,0)
                                action = "ERROR"

                            warning( "ExportAssertions::assessBeliefCriteria - action = " + action, 3)
                            if type(slot_obj) in ([type(EMultiContValSlot())] + EMultiContValSlot().__class__.__subclasses__()):
                                ev.objects[key].combineEvidence(slot_obj.mapping, ranking_categories, believable_ev_for)
                           
                            if action == "assume!":
                                ## We generate an assertion for slots after their evidence values have been combined
                                ## so that evidence assumptions are correctly linked to the assertion.
                                ## TODO: make sure that we remove previously asserted but no longer valid (retract!) assertions
                                if key not in exported_asrts.keys():
                                    exported_asrts[key] = None
                                    mp = get_asrt_to_jtms(ev, name, slot_name, item)
                                    if not mp:
                                        error("ExportAssertions::assessBeliefCriteria - Error, unable to get DIKB->JTMS mapping for %s_%s_%s " % (name, slot_name, item), 0)
                                    else:
                                        a_list.append(mp + "\n")

                                a_list.append(assume_bc_satisfied(ev.objects[key], True) + "\n")
                            else:
                                a_list.append(assume_bc_satisfied(ev.objects[key], False) + "\n")
                            
                            
                elif (type(slot_obj) in ([ESlot] + ESlot().__class__.__subclasses__())):
                    """handle ESlot and EContValSlot Types"""
                    (believable_ev_for, believable_ev_against) = getBeliefCriteria(slot_name, loe_d, bc_d)
                    warning("".join(["ExportAssertions::assessBeliefCriteria - loaded rules for believable - \nfor:",
                                     str(believable_ev_for), "\nagainst: ", str(believable_ev_against),
                                     " for slot ", slot_name]), 3)

                    changing_assumption = ""
                    changing_assumption = slot_obj.assessEvidence(ranking_categories, believable_ev_for, believable_ev_against)

                    warning("ExportAssertions::assessBeliefCriteria - changing_assumption = " + str(changing_assumption), 3)

                    ## if some change in belief occured...
                    if changing_assumption != "":
                        """write a form for an enabled assumption for this slot's evidence
                        """
                        # assume!, retract!, or 'can't decide'
                        action = ""
                        key = "_".join([name, slot_name, changing_assumption])
                        warning( "ExportAssertions::assessBeliefCriteria - key =" +  key, 3)
                        if ev.objects.has_key(key):
                                action = ev.objects[key].evidence_rating
                        else:
                            warning( "ExportAssertions::assessBeliefCriteria - Error, no key in ev.objects for " + key, 1)
                            action = "ERROR"
                        warning( "ExportAssertions::assessBeliefCriteria - action = " + action, 3)

                        if type(slot_obj) in ([type(EContValSlot())] + EContValSlot().__class__.__subclasses__()):
                            ev.objects[key].combineEvidence(slot_obj.mapping, ranking_categories, believable_ev_for)

                        if action == "assume!":
                            ## We generate an assertion for slots after their evidence values have been combined
                            ## so that evidence assumptions are correctly linked to the assertion.
                            ## TODO: make sure that we remove previously asserted but no longer valid (retract!) assertions
                            if key not in exported_asrts.keys():
                                exported_asrts[key] = None
                                mp = get_asrt_to_jtms(ev, name, slot_name, changing_assumption)
                                if not mp:
                                    error("Error, unable to get DIKB->JTMS mapping for %s_%s_%s " % (name, slot_name, changing_assumption), 0)
                                else:
                                    a_list.append(mp + "\n")
                            
                            a_list.append(assume_bc_satisfied(ev.objects[key], True) + "\n")
                        else:
                            a_list.append(assume_bc_satisfied(ev.objects[key], False) + "\n")
                            
    a_list.sort()
    for item in a_list:
        exportF.write(item)
        
    exportF.close()
