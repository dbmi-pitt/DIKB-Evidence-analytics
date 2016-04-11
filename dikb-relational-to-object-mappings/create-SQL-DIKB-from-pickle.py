'''
create-SQL-DIKB-from-pickle.py

A program to write DIKB entities to a SQLite database

Created on March 6th, 2012

@authors: Richard Boyce based on a file create by Hassen Khan from a test file created by Greg Gardner (gardnerga)

Load pickled drug objects into a new SQL DIKB database.  
'''

import inspect

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

import sys
sys.path = sys.path + ['.']

import tables
import modelmapper

import os
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.ExportAssertions import *

############################################################
# Functions for DIKB Program
############################################################

def evidenceSlotMap(slot, counter, asrtDict, esDAO, drugID):

    # List used to collect all the DAO's items
    DAOList = []
    Ctr = counter

    # Goes through each assertion for a slot item
    for asrt in slot:
        
        # Evidence Slot Mapping
        try:
            esmapDAO = modelmapper.Evidence_Slot_mapDAO()
            esmapDAO.id = counter
            esmapDAO.assert_id = asrtDict[asrt._name]
            esmapDAO.d_slot_id = esDAO.d_slot_id
        except KeyError:
            print "evidenceSlotMap -- Skipping asrt._name: %s because it could not be found in the evidence base." % asrt._name
            continue
        # Increment the counter
        counter += 1
    
        # Appends to the list of all assertions for the slot item
        DAOList.append(esmapDAO)

    # Takes the difference of the counters, to account for number of assertions done in the loop
    diff = counter - Ctr

    return DAOList, diff 

############################################################
# Open the existing drug model for the DIKB
############################################################

# Change log level if desired
os.environ["DIKB_LOG_LEVEL"] = "2"

## The DIKB to input into SQL 
#### THE LAST WORKING DIKB + EV BASE
#new_ev = EvidenceBase("evidence","UPIA+Hanlon-AJGP-2012")
#new_dikb = DIKB("dikb","Reconstitued UPIA", new_ev)
#new_dikb.unpickleKB('../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/dikb.pickle') # Drug model corresponding to Tier 4 BC evals from UPIA DIKB-runs-04202010 but reloaded from the SQl DIKB as stored in https://svn01.dbmi.pitt.edu/svn/linked-dikb/database/dikb-mysql-backup-03052012 
#new_ev.unpickleKB('../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/ev.pickle') # SQl DIKB as stored in https://svn01.dbmi.pitt.edu/svn/linked-dikb/database/dikb-mysql-backup-03052012, re-loaded into Python, and merged with https://svn01.dbmi.pitt.edu/svn/linked-dikb/database/dikb-pickle-with-Robs-entries-fall-2010/ev.pickle

## TESTING ADDING NEW DRUGS
new_ev = EvidenceBase("evidence","test-June2015")
new_dikb = DIKB("dikb","Test 2015", new_ev)
new_dikb.unpickleKB('../dikb-pickles/dikb-test.pickle') # adds a new metabolite
new_ev.unpickleKB('../dikb-pickles/ev-test.pickle') # no changes yet

##assess evidence using some belief criteria and test exporting to the database 
reset_evidence_rating(new_ev, new_dikb) # reset the internal finite
                                        # state machine or you will
                                        # get unexpected behavior

for e,v in new_ev.objects.iteritems():
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

############################## UNCOMMENT WHEN READY TO EXPORT ASSERTIONS TO THE REASONER #########################
exportAssertions(new_ev, new_dikb, "../assertions.lisp")
assessBeliefCriteria(new_dikb, new_ev, "../changing_assumptions.lisp")

# #new_dikb.pickleKB('../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/full-Tier-4-UPIA-Hanlon-AJGP2012-DIKB-EVALUATED.pickle')
# #new_ev.pickleKB('../database/dikb-pickle-merging-Robs-entries-fall-2010-with-SQL-030512/full-Tier-4-UPIA-Hanlon-AJGP2012-EV-EVALUATED.pickle')

# ## useful if we want to run over all instances of a specific class or
# ## classes in the DrugModel
clsL = []
for k,v in new_dikb.objects.iteritems():
    if type(v) == Drug or type(v) == Metabolite or type(v) == Chemical:
        clsL.append(k)

############################################################
# CREATE MAPPING BETWEEN DIKB CLASSES AND SQL TABLE '''
############################################################

# Removing the test database
try:
    os.remove('test.db')
    print 'Removed: test.db'
except OSError:
    pass

# Creating the engine for our database
def my_con_func():
    import sqlite3.dbapi2 as sqlite
    con = sqlite.connect("test.db")
    con.text_factory=str
    return con

#engine = create_engine('sqlite:///test.db', echo=False)
engine = create_engine('sqlite:///test.db', echo=False, creator=my_con_func)

# Mapping Style
# Retrieving the MetaData
md = MetaData()

# Creates the tables using MetaData and Tables.py
dbTables = tables.make_tables(md)

# Save the Evidence, Assertion and Evidence Mapping tables
dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table =  dbTables[0], dbTables[1], dbTables[2], dbTables[3], dbTables[4], dbTables[5], dbTables[6], dbTables[7], dbTables[8], dbTables[9], dbTables[10]

# Adds the tables to the engine
md.create_all(engine)

# Maps our tables to the proper DAO classes
modelmapper.mapAll(dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table)

############################################################
# INSTANTIATE ASSERTION AND EVIDENCE OBJECTS
############################################################

# Declaring Variables
dtoL = []
daoL = [] # Assertion List
drugCtr = 1 # Key for the drug table
metaboliteCtr = 1 # Key for the metabolite table
chemicalCtr = 1 # Key for the chemical table
evidenceCtr = 1 # Key for the evidence table
assertionCtr = 1 # Key for the assertion table
assertionEvidenceCtr = 1 # Key for the assertion evidence mapping ids 
evidenceMappingCtr = 1 # Key for the evidence mapping ids
assumptionMappingCtr = 1 # Key for the assumption_mapping tab
assumptionListCtr = 1


# 1) make the modifications to work with ESlots and EMultiSlots -- e.g., create an ESlots table w. range_id, value (blob?) and for EMultiSlots a table w. range_id, type ('EMulti..' or 'EMultiCont..'), value_id (numeric) -- the latter a mapping to a list of values
# 2) With the modifications in place, try to do the ESlots -- hard code for now 
# 3) by "doing the ESlots," I mean, get the assertions in the 'evidence' list out to the DB with a mapping from the slot to the a list of assertions that fill that slot

# a dict to help get from Assertion instance names to their ids in the AssertionDAO table
asrtDict = {}

for k,v in new_ev.objects.iteritems():
    # Storing values of the current asserstion
    a = modelmapper.AssertDAO()
    a.id = assertionCtr
    a._name = v._name
    a.object = v.object
    a.slot = v.slot
    a.value = v.value
    a.ready_for_classification = v.ready_for_classification
    a.assert_by_default = v.assert_by_default
    a.evidence_rating = v.evidence_rating
    a.assert_class = v.__class__.__name__

    # Assertion dictionary, gives the ID value and keyed by the Assertion name
    asrtDict[a._name] = a.id

    # If there are values for evidence_for, it is mapped to the evidence table
    if len(v.evidence_for) != 0:
        a.evidence_for = assertionEvidenceCtr  
       
        # Loops through every assertion for evidence_for
        for evidenceForItem in v.evidence_for:
            emDAO = modelmapper.Evidence_mapDAO()
            emDAO.id = evidenceMappingCtr
            evidenceMappingCtr += 1
            emDAO.assert_ev_id = a.evidence_for
            emDAO.assert_id = assertionCtr

            # Storing the values of the current evidence item
            e = modelmapper.EvidenceDAO()                                    
            e.id = evidenceCtr
            e._name = evidenceForItem._name
            e.doc_pointer = evidenceForItem.doc_pointer
            e.quote = evidenceForItem.quote
            e.reviewer = evidenceForItem.reviewer.getEntry()
            e.timestamp = evidenceForItem.timestamp
            e.evidence_type = evidenceForItem.evidence_type.getEntry()
            e.evidence_class = evidenceForItem.__class__.__name__
        
            # Checks to see if there is a value for evidence in EvidenceContinousVal()
            if (type(evidenceForItem) in ([EvidenceContinousVal] + EvidenceContinousVal().__class__.__subclasses__())):
                # Stores the evidence value if it exist in EvidenceContinousVal()
                e.value = float(evidenceForItem.value)
            # Checks to see if there is a object_dose, precip_dose and number of subjects for evidence in PKStudy()
            if (type(evidenceForItem) in ([PKStudy] + PKStudy().__class__.__subclasses__())):
                # Stores the evidence object_dose, precip_dose and numb_subjects value if it exist in PKStudy()
                try:
                    e.object_dose = float(evidenceForItem.object_dose)
                except (ValueError, TypeError):
                    print 'WARNING: objec_dose produced ValueError, leaving as NULL: %s' % evidenceForItem.object_dose
                    pass
                try:
                    e.precip_dose = float(evidenceForItem.precip_dose)
                except (ValueError, TypeError):
                    print 'WARNING: precip_dose produced ValueError, leaving as NULL: %s' % evidenceForItem.precip_dose
                    pass
                try:
                    e.numb_subjects = int(evidenceForItem.numb_subj)
                except (ValueError, TypeError):
                    print 'WARNING: numb_subjects produced ValueError, leaving as NULL: %s' % evidenceForItem.numb_subj
                    pass

            # Checks to see if there is a enzyme_system value for evidence in In_vitro_inhibition_study()
            if (type(evidenceForItem) in ([In_vitro_inhibition_study] + In_vitro_inhibition_study().__class__.__subclasses__())):
                # Stores the evidence enyzme_system value  if it exist in In_vitro_inhibition_study()
                e.enzyme_system = evidenceForItem.enzyme_system.getEntry()
            # Checks to see if there is a dose value for evidence in Maximum_concentration_study()
            if (type(evidenceForItem) in ([Maximum_concentration_study] + Maximum_concentration_study().__class__.__subclasses__())):
                # Stores the evidence dose value if it exist in Maximum_concentration_study()
                e.dose = float(evidenceForItem.dose)

            # Assumptions for current evidence for item
            if len(evidenceForItem.assumptions.getEntries()) != 0:            
                for asmpt in evidenceForItem.assumptions.getEntries(): # asmpt is the string name of some Assumption instance
                    # Sets the proper DAO
                    u = modelmapper.Assumption_mapDAO()

                    # Stores the id, evidence id and the name of the current assumption
                    u.id = assumptionMappingCtr
                    u.ev_id = evidenceCtr
                    u.assump_assert_name = asmpt

                    # Increments the assumption mapping counter
                    assumptionMappingCtr += 1
                
                    # Stores the assumption list id, for both the evidence and assumption_map tables
                    e.assump_list_id = assumptionListCtr
                    u.assump_list_id = assumptionListCtr         
                
                    # Appends assumption to list
                    dtoL.append(u)
                # Increments the assumption list counter
                assumptionListCtr += 1

            # Increments the count for the evidence id
            evidenceCtr += 1

            # Appends the evidence to a list and the mapping object
            dtoL.append(e)
            dtoL.append(emDAO)

        # Increments the count for the assertion evidence counter
        assertionEvidenceCtr += 1
     
    # If there are values for evidence_against, it is mapped to the evidence table
    if len(v.evidence_against) != 0:
        a.evidence_against = assertionEvidenceCtr
        
        # Loops through every assertion for evidence_against
        for evidenceAgainstItem in v.evidence_against:
            emDAO = modelmapper.Evidence_mapDAO()
            emDAO.id = evidenceMappingCtr
            emDAO.assert_ev_id = a.evidence_against
            emDAO.assert_id = assertionCtr

            # Increments the Evidence Mapping Counter
            evidenceMappingCtr += 1

            # Store the values of the current evidence items
            e = modelmapper.EvidenceDAO()
            e.id = evidenceCtr
            e._name = evidenceAgainstItem._name
            e.doc_pointer = evidenceAgainstItem.doc_pointer
            e.quote = evidenceAgainstItem.quote
            e.reviewer = evidenceAgainstItem.reviewer.getEntry()
            e.timestamp = evidenceAgainstItem.timestamp
            e.evidence_type = evidenceAgainstItem.evidence_type.getEntry()
            e.evidence_class = evidenceAgainstItem.__class__.__name__

            # Checks to see if there is a value for evidence in EvidenceContinousVal()
            if (type(evidenceAgainstItem) in ([EvidenceContinousVal] + EvidenceContinousVal().__class__.__subclasses__())):
                # Stores the evidence value if it exist in EvidenceContinousVal()
                try:
                    e.value = float(evidenceAgainstItem.value)
                except (ValueError, TypeError):
                    print 'WARNING: value produced ValueError, leaving as NULL: %s' % evidenceAgainstItem.value
                    pass
           # Checks to see if there is a object_dose, precip_dose and number of subjects for evidence in PKStudy()
            if (type(evidenceAgainstItem) in ([PKStudy] + PKStudy().__class__.__subclasses__())):
                # Stores the evidence object_dose, precip_dose and numb_subjects value if it exist in PKStudy()
                try:
                    e.object_dose = float(evidenceAgainstItem.object_dose)
                except (ValueError, TypeError):
                    print 'WARNING: object dose produced ValueError, leaving as NULL: %s' % evidenceAgainstItem.object_dose
                    pass
                try:
                    e.precip_dose = float(evidenceAgainstItem.precip_dose)
                except (ValueError, TypeError):
                    print 'WARNING: precip dose produced ValueError, leaving as NULL: %s' % evidenceAgainstItem.precip_dose
                    pass
                try:
                    e.numb_subjects = int(evidenceAgainstItem.numb_subj)
                except (ValueError, TypeError):
                    print 'WARNING: number of subjects produced ValueError, leaving as NULL: %s' % evidenceAgainstItem.numb_subj
                    pass

            # Checks to see if there is a enzyme_system value for evidence in In_vitro_inhibition_study()
            if (type(evidenceAgainstItem) in ([In_vitro_inhibition_study] + In_vitro_inhibition_study().__class__.__subclasses__())):
                # Stores the evidence enyzme_system value  if it exist in In_vitro_inhibition_study()
                e.enzyme_system = evidenceAgainstItem.enzyme_system.getEntry()
           # Checks to see if there is a dose value for evidence in Maximum_concentration_study()
            if (type(evidenceAgainstItem) in ([Maximum_concentration_study] + Maximum_concentration_study().__class__.__subclasses__())):
                # Stores the evidence dose value if it exist in Maximum_concentration_study()
                e.dose = float(evidenceAgainstItem.dose)

            # Assumptions for current evidence against item
            if len(evidenceAgainstItem.assumptions.getEntries()) != 0:            
                for asmpt in evidenceAgainstItem.assumptions.getEntries(): # asmpt is the string name of some Assumption instance
                    # Sets the proper DAO
                    u = modelmapper.Assumption_mapDAO()

                    # Stores the id, evidence id and the name of the current assumption
                    u.id = assumptionMappingCtr
                    u.ev_id = evidenceCtr
                    u.assump_assert_name = asmpt

                    # Increments the assumption mapping counter
                    assumptionMappingCtr += 1
                    
                    # Stores the assumption list id, for both the evidence and assumption_map tables
                    e.assump_list_id = assumptionListCtr
                    u.assump_list_id = assumptionListCtr         
                    
                    # Appends assumption to list
                    dtoL.append(u)
                # Increments the assumption list counter
                assumptionListCtr += 1     
     
            # Increments the count for the evidence id
            evidenceCtr += 1

            # Appends the evidence to a list and the mapping object
            dtoL.append(e)
            dtoL.append(emDAO)

        # Increments the count for the assertion evidence counter
        assertionEvidenceCtr += 1
  
    # Checks to see if the value of the assertion is a continous value
    if (type(v) in ([ContValAssertion] + ContValAssertion().__class__.__subclasses__())):
        # Stores the continous and numeric value, if assertion is a continous value
        a.cont_val = v.cont_val
        a.numeric_val = v.numeric_val   

    # Increments the count for the assertion id
    assertionCtr += 1

    # Appends the assertion to a list
    dtoL.append(a)
           


############################################################
# INSTANTIATE DIKB DRUG OBJECTS
############################################################

## uncomment to run over only a subset of instances
#selectedKeys = ["clozapine", "midazolam", "ketoconazole", "simvastatin", "clarithromycin", "atorvastatin", "paroxetine"]

## uncomment to run over all instances of a particilar type defined above
selectedKeys = clsL

# Slot Counters 
eslotdao_ctr = 1
eslotevidence_ctr = 1
assert_id_ctr = 1
emultislot_ctr = 1
value_ctr = 1
value_id_ctr = 1

# Iterating through each asserstion
for k,v in new_dikb.objects.iteritems():
    if k not in selectedKeys:
        print "SKIPPING %s" % k
        continue

    d = None
    if type(v) == Drug:
        print "INFO: creating new Drug instance"
        d = modelmapper.dikbDAO()
        d.id = drugCtr
        d.prodrug = v.prodrug.getEntry() == "True"
        d.active_ingredient_name = v.active_ingredient_name.getEntry()
        d.active_ingredient = v.active_ingredient.getEntry() == "True"

    elif type(v) == Metabolite:
        print "INFO: creating new Metabolite instance"
        d = modelmapper.MetaboliteDAO()
        d.id = metaboliteCtr
        d.metabolite = v.metabolite.getEntry() == "True"

    elif type(v) == Chemical:
        print "INFO: creating new Chemical instance"
        d = modelmapper.ChemicalDAO()
        d.id = chemicalCtr
        d.chemical = v.chemical.getEntry() == "True"

    d._name = v._name
    
    # List of all the ESlots
    eSlotList = ["primary_total_clearance_mechanism", "primary_metabolic_clearance_enzyme", "primary_total_clearance_enzyme", "in_vitro_probe_substrate_of_enzyme", "in_viVo_probe_substrate_of_enzyme", "in_vitro_selective_inhibitor_of_enzyme", "in_viVo_selective_inhibitor_of_enzyme", "pceut_entity_of_concern"]

    # Iterates through each Slot
    for eSlotName in eSlotList:
        eSlot = v.__dict__[eSlotName]

        # Create the ESlotDAO instance 
        esDAO = modelmapper.ESlotDAO()
        esDAO.id = eslotdao_ctr
        esDAO.d_slot_id = eslotevidence_ctr

        d.__dict__[eSlotName] = esDAO.d_slot_id

        # Increment the ESlot id counter
        eslotdao_ctr += 1

        # The type of ESlot
        slotType = str(eSlot.__class__)
        slotType = slotType.replace("<class 'DIKB.ModelUtils.","").replace("'>", "")
        esDAO.type = slotType

        # Gets the value of the slot if there is one
        if eSlot.value != 'none_assigned':
            #if type(eSlot.value) == type(unicode("")):
            if type(eSlot.value) == type(""):
                esDAO.value_string = unicode(eSlot.value)
            if type(eSlot.value) == type(1):
                esDAO.value_numeric = eSlot.value

        # Evidence Slot Mapping, returns list of DAO's to 
        if len(eSlot.evidence) > 0:
            eSlotMap, inc = evidenceSlotMap(eSlot.evidence, assert_id_ctr, asrtDict, esDAO, drugCtr)

            # Increments the Evidence Slot Map Table ID counter
            assert_id_ctr += inc

            # Appends mapping to a list
            for elt in eSlotMap:
                dtoL.append(elt)
    
        # Increment the Eslot Evidence Counter
        eslotevidence_ctr += 1
        # Appends the Eslot to a list
        dtoL.append(esDAO)

    # List of all EMultiSlots
    eMultiSlotList = None    
    if type(v) == Metabolite or type(v) == Chemical:
        eMultiSlotList = ["maximum_concentration", "minimum_therapeutic_dose", "maximum_therapeutic_dose", "assumed_effective_dose", "substrate_of", "is_not_substrate_of", "inhibits", "does_not_inhibit", "has_metabolite", "does_not_permanently_deactivate_catalytic_function", "permanently_deactivates_catalytic_function", "inhibition_constant", "induces", "increases_auc", "sole_PK_effect_alter_metabolic_clearance"]

    elif type(v) == Drug:
        eMultiSlotList = ["maximum_concentration", "minimum_therapeutic_dose", "maximum_therapeutic_dose", "assumed_effective_dose", "substrate_of", "is_not_substrate_of", "inhibits", "does_not_inhibit", "has_metabolite", "does_not_permanently_deactivate_catalytic_function", "permanently_deactivates_catalytic_function", "inhibition_constant", "induces", "increases_auc", "sole_PK_effect_alter_metabolic_clearance", "bioavailability", "fraction_absorbed", "fraction_cleared_by"]

    # Iterates through each EMultiSlot from the EMultiSlotList
    for eMultiSlot in eMultiSlotList:

        # The type of EmultiSlot
        slotType = str(v.__dict__[eMultiSlot].__class__)
        slotType = slotType.replace("<class 'DIKB.ModelUtils.","").replace("'>", "")

        # Create the EMultiSlotDAO instance 
        emsDAO = modelmapper.EMultiSlotDAO()
        emsDAO.id = emultislot_ctr
        emsDAO.d_slot_id = eslotevidence_ctr
        emsDAO.type = slotType

        if len(v.__dict__[eMultiSlot].evidence) == 0:
            continue

        # values for EmultiContValSlots
        if type(v.__dict__[eMultiSlot]) in ([type(EMultiContValSlot())] + EMultiContValSlot().__class__.__subclasses__()):
            # iterate through each assertion in the evidence list and
            # check if the numeric_val and cont_val slots are equal to
            # None. If so, then pass. Otherwise, one or both of these
            # slots holds a combined value (e.g. based on average,
            # min, max, dependending on the assertion). The cont_val
            # and numeric_val data items are in the Assertion table of
            # the database. SO, we need to store the IDs to the
            # appropriate Assertion rows for this values slot

            # Gives the current eMultiSlot the correct d_slot_id in the drugs table
            d.__dict__[eMultiSlot] = emsDAO.d_slot_id

            # Loop that goes threw every assertion for the current evidence item
            for asrt in v.__dict__[eMultiSlot].evidence:
                # CONTINUES if both the numeric and constant value are NULL
                if asrt.numeric_val == None and asrt.cont_val == None:
                    continue

                ## use the valueDAO to store the assertion row
                ## IDs for each assertion that has a numeric_val or
                ## cont_val. Later, the user will have to know to
                ## query for assertion IDs to get the numeric_val or
                ## cont_val
                else:
                    # Checks to see if the assertion lies within the
                    # belief criteria by testing for the presence of
                    # the object (i.e., drug, metabolite, chemical) in
                    # the supporting evidence list for the slot
                    if asrt.value in v.__dict__[eMultiSlot].value:
                        # Creates the valueDAO instances
                        valueDAO = modelmapper.ValueDAO()
                        valueDAO.id = value_ctr
                        valueDAO.value_id = value_id_ctr
                        valueDAO.value_string = asrt.value

                        # Sets the assertion id for the value
                        valueDAO.value_numeric = asrtDict[asrt._name]

                        # Sets the correct matching value_id in the EMultiSlot table
                        emsDAO.value_id = value_id_ctr
                    
                        # Appends the values to a list
                        dtoL.append(emsDAO)
                        dtoL.append(valueDAO)
                    
                        # Increments the value counter
                        value_ctr += 1

            # Increment the value id
            value_id_ctr += 1


        # values for EmultiSlots
        else:
            # Gives the current eMultiSlot the correct d_slot_id in the drugs table
            d.__dict__[eMultiSlot] = emsDAO.d_slot_id

            # Loop that goes through every assertion for the current evidence item
            for asrt in v.__dict__[eMultiSlot].evidence:

                # Checks to see if the assertion lies within the
                # belief criteria by testing for the presence of
                # the object (i.e., drug, metabolite, chemical) in
                # the supporting evidence list for the slot
                if asrt.value in v.__dict__[eMultiSlot].value:
                    # Creates the valueDAO instances
                    valueDAO = modelmapper.ValueDAO()
                    valueDAO.id = value_ctr
                    valueDAO.value_id = value_id_ctr
                    valueDAO.value_string = asrt.value
                    
                    # Sets the correct matching value_id in the EMultiSlot table
                    emsDAO.value_id = value_id_ctr
                    
                    # Appends the values to a list
                    dtoL.append(emsDAO)
                    dtoL.append(valueDAO)
                    
                    # Increments the value counter
                    value_ctr += 1

            # Increment the value id
            value_id_ctr += 1

        # Appends the EMultiSlot to a list
        dtoL.append(emsDAO)

        # Increment the ESlot id counter
        emultislot_ctr += 1

        # Evidence Slot Mapping, returns list of DAO's to append
        eSlotMap, inc = evidenceSlotMap(v.__dict__[eMultiSlot].evidence, assert_id_ctr, asrtDict, emsDAO, drugCtr)

        # Increments the Evidence Slot Map Table ID counter
        assert_id_ctr += inc

        # Increment the Eslot Evidence Counter
        eslotevidence_ctr += 1

        # Appends mapping to a list
        for elt in eSlotMap:
            dtoL.append(elt)
    
    # Increment the appropriate Counter
    if type(v) == Metabolite:
        metaboliteCtr += 1
    elif type(v) == Chemical:
        chemicalCtr += 1
    elif type(v) == Drug:
        drugCtr += 1

    # Appends the Drug to a list
    dtoL.append(d)
    

''' -------------------------------------------End DIKB Entry--------------------------------------------------'''

''' See how the DIKB -> SQL mapping has worked out '''
def printResult(table):
    s = select([table])
    result = conn.execute(s)
    for row in result:
        print '%s' % row

# Open database session
Session = sessionmaker(bind=engine)
session = Session()

# Add objects and commit to database
for obj in dtoL:
    session.add(obj)

# Commits the current session
session.commit()

#Connect to database and do a select query
conn=engine.connect()

printResult(dikb_table)

print "INFO: done"
