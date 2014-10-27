'''
Created on September 12th, 2011

@authors: Richard Boyce and Hassen Khan from a test file created by Greg Gardner (gardnerga)

Load drug objects into the DIKB.  Store some info
about them in a relational database using sqlAlchemy.
'''

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

import sys
sys.path = sys.path + ['.']

import tables as sql_tables
import modelmapper

import os
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *

import pdb

# Change log level if desired
os.environ["DIKB_LOG_LEVEL"] = "0"

def evidence_matching(ev_mapDAO, session, allowed_assumptions):
    """
    For each evidence item, the function finds all the assumptions, adds the values to the DIKB and returns the evidence

        @param ev_mapDAO: (class) The evidence_map class for evidence items for the current assertion
                
        @return: (class) -- the current evidence item
     """
    # Loop that gives every evidence id that matches the ev_id from evidence_mapDAO
    for evDAO in session.query(modelmapper.EvidenceDAO).filter(modelmapper.EvidenceDAO.id == ev_mapDAO.id):
        e = None
       
        # The evidence values are stored from the EvidenceDAO
        if (evDAO.evidence_class == "Evidence"):
            e = Evidence(ev = allowed_assumptions) 
            e.create(evDAO.doc_pointer, evDAO.quote, evDAO.evidence_type, evDAO.reviewer, evDAO.timestamp)
        if (evDAO.evidence_class in ["EvidenceContinousVal","EvidenceContinuousVal"]):
            e = EvidenceContinousVal(ev = allowed_assumptions)
            e.create(evDAO.doc_pointer, evDAO.quote, evDAO.evidence_type, evDAO.reviewer, evDAO.timestamp, evDAO.value)
        if (evDAO.evidence_class == "PKStudy"):
            e = PKStudy(ev = allowed_assumptions)
            e.create(evDAO.doc_pointer, evDAO.quote, evDAO.evidence_type, evDAO.reviewer, evDAO.timestamp, evDAO.object_dose, evDAO.precip_dose, evDAO.value, evDAO.numb_subjects)
        if (evDAO.evidence_class == "In_vitro_inhibition_study"):
            e = In_vitro_inhibition_study(ev = allowed_assumptions)
            e.create(evDAO.doc_pointer, evDAO.quote, evDAO.evidence_type, evDAO.reviewer, evDAO.timestamp, evDAO.value, evDAO.enzyme_system)
        if (evDAO.evidence_class == "Maximum_concentration_study"):
            e = Maximum_concentration_study(ev = allowed_assumptions)
            e.create(evDAO.doc_pointer, evDAO.quote, evDAO.evidence_type, evDAO.reviewer, evDAO.timestamp, evDAO.dose, evDAO.numb_subjects, evDAO.value)

        if e == None:
            print "ERROR: unable to find the Evidence row referred to by evidence id %s" % ev_mapDAO.id
        
        # The current name and id of the evidence
        e.id = evDAO.id
        e._name = evDAO._name
        
        # A list that stores all possible assumptions for the current evidence
        assump_list = []

        # assembles the list of Assertions that are assumptions
        # for this evidence item and adds their name to the
        # assumptions list
        for amDAO in session.query(modelmapper.Assumption_mapDAO).filter(modelmapper.Assumption_mapDAO.ev_id == evDAO.id):
            assump_list.append(amDAO.assump_assert_name)

        """gg: There seems to be an invalid assumption in dikbEvidence.Assumption_map, just remove it from assump_list for now"""
        if "cyp3a5_polymorphic_enzyme_True" in assump_list:
            assump_list.remove("cyp3a5_polymorphic_enzyme_True")
        e.assumptions.addEntry(assump_list)

    return e

def load_ev_from_db(ident):
    # Creating the engine for our database
    engine = create_engine('mysql://root:5bboys@localhost/dikbEvidence') 

    # Mapping Style
    # Retrieving the MetaData
    md = MetaData()

    # Adds the tables to the engine
    md.create_all(engine)

    # Creates the tables using MetaData and Tables.py
    tables = sql_tables.make_tables(md)

    # Save the Evidence, Assertion and Evidence Mapping tables
    dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table = tables[0], tables[1], tables[2], tables[3], tables[4], tables[5], tables[6], tables[7], tables[8], tables[9], tables[10]

    # Maps our tables to the proper DAO classes
    modelmapper.mapAll(dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table)

    # Open database session
    Session = sessionmaker(bind=engine)
    session = Session()

    ## an EvidenceBase to hold the re-constituted Assertion and Evidence instances
    new_ev = EvidenceBase("evidence",ident)

    # The list of allowed assumptions, will be used as the range for the "assumptions" slot of Evidence instances
    allowed_assumptions = Assumptions()
    for instance in session.query(modelmapper.AssertDAO).order_by(modelmapper.AssertDAO.id):
        allowed_assumptions.add(instance._name)

    # Loop that goes through every assertion item
    for asDAO in session.query(modelmapper.AssertDAO):
        print "assertion: %s" % asDAO._name
        print 'assertion id: %s' % asDAO.id

        # Initialization
        a = None
    
        # The proper assertion class is used
        if (asDAO.assert_class == "Assertion"):
            a = Assertion(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "Assertion_maximum_concentration"):
            a = Assertion_maximum_concentration(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "Assertion_inhibition_constant"):
            a = Assertion_inhibition_constant(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "Assertion_IncreaseAUC"):
            a = Assertion_IncreaseAUC(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "Assertion_m_discrete"):
            a = Assertion_m_discrete(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "Assertion_continuous_s_val"):
            a = Assertion_continuous_s_val(asDAO.object, asDAO.slot, asDAO.value)
        elif (asDAO.assert_class == "ContValAssertion"):
            a = ContValAssertion(asDAO.object, asDAO.slot, asDAO.value)

        # Store the ID, Name, Ready For Classification and Assert By Default for the current assertion
        a._id = asDAO.id
        a._name = asDAO._name
        a.ready_for_classification = asDAO.ready_for_classification
        a.assert_by_default = asDAO.assert_by_default

        # Checks to see if the assertion is a Continous Assertion
        if (asDAO.assert_class in ["ContValAssertion", "Assertion_continuous_s_val", "Assertion_IncreaseAUC", "Assertion_inhibition_constant", "Assertion_maximum_concentration"]):

            # Stores the continous and numeric value, if assertion is a continous value
            a.cont_val = asDAO.cont_val
            a.numeric_val = asDAO.numeric_val   

        # Loop that gets every assert_ev_id that matches the evidence_for value
        for ev_mapDAO in session.query(modelmapper.Evidence_mapDAO).filter(modelmapper.Evidence_mapDAO.assert_ev_id == asDAO.evidence_for):

            # Matches the current evidence to the evidence mapping table
            e = evidence_matching(ev_mapDAO, session, allowed_assumptions)

            # all values for the Evidence item initialized...
            #print u'Evidence For %s' % e

            # The evidence values are inserted for the current assertion
            a.insertEvidence("for", e)

        # Loop that gets every assert_ev_id that matches the evidence_against value
        for ev_mapDAO in session.query(modelmapper.Evidence_mapDAO).filter(modelmapper.Evidence_mapDAO.assert_ev_id == asDAO.evidence_against):
        
            # Matches the current evidence to the evidence mapping table
            e = evidence_matching(ev_mapDAO, session, allowed_assumptions)

            # all values for the Evidence item initialized...
            #print u'Evidence against %s' % e

            # The evidence values are inserted for the current assertion
            a.insertEvidence("against", e)
 
        # The assertion is added with the new evidence                      
        new_ev.addAssertion(a)
    return new_ev
    # pickle the evidence-base for testing
    # new_ev.pickleKB('reconstitued-upia-FULL.pickle')

class Assumptions:
    def __init__(self):
        self.objects = {}

    def add(self, assumption):
        self.objects[assumption] = ""

if __name__ == "__main__":
    load_ev_from_db("test")
