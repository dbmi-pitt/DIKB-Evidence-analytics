'''
Created on Mar 30, 2011

@author: gardnerga

Create the tables on which to map DIKB classes
'''

from sqlalchemy import Table, Column, Integer, Boolean, String, ForeignKey, Float, BLOB

''' Create SQL Tables for mapping to DIKB classes. Takes a sqlalchemy
    MetaData object as an argument.  '''
def make_tables(md):
    dikb_table = Table('Drugs', md,
                       Column('id', Integer, primary_key=True),                       
                       Column('_name', String(100)),
                       Column('prodrug', Boolean()),
                       Column('primary_total_clearance_mechanism', Integer, nullable=True),
                       Column('primary_metabolic_clearance_enzyme', Integer, nullable=True),
                       Column('primary_total_clearance_enzyme', Integer, nullable=True),
                       Column('in_vitro_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_vitro_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('pceut_entity_of_concern', Integer, nullable=True),
                       Column('active_ingredient_name', String(100), nullable=True),
                       Column('active_ingredient', Boolean(), nullable=True),
                       Column('maximum_concentration', Integer, nullable=True),
                       Column('minimum_therapeutic_dose', Integer, nullable=True),
                       Column('maximum_therapeutic_dose', Integer, nullable=True),
                       Column('assumed_effective_dose',  Integer, nullable=True),
                       Column('substrate_of', Integer, nullable=True),
                       Column('is_not_substrate_of', Integer, nullable=True),
                       Column('inhibits', Integer, nullable=True),
                       Column('does_not_inhibit', Integer, nullable=True),
                       Column('has_metabolite', Integer, nullable=True),
                       Column('permanently_deactivates_catalytic_function', Integer, nullable=True),
                       Column('does_not_permanently_deactivate_catalytic_function', Integer, nullable=True),
                       Column('inhibition_constant', Integer, nullable=True),
                       Column('induces', Integer, nullable=True),
                       Column('increases_auc', Integer, nullable=True),
                       Column('sole_PK_effect_alter_metabolic_clearance', Integer, nullable=True),
                       Column('bioavailability', Integer, nullable=True),
                       Column('fraction_absorbed', Integer, nullable=True),
                       Column('fraction_cleared_by', Integer)
                       )    

    ev_table = Table('Evidence', md,
                     Column('id', Integer, primary_key=True),
                     Column('_name', String(100)),
                     Column('doc_pointer', String(100)),
                     Column('quote', String(4000)),
                     Column('reviewer', String(100)),
                     Column('timestamp', String(100)),
                     Column('evidence_type', String(100)),
                     Column('evidence_class', String(100)),
                     Column('value', Float, nullable=True),
                     Column('object_dose', Float, nullable=True),
                     Column('precip_dose', Float, nullable=True),
                     Column('numb_subjects', Integer, nullable=True),
                     Column('enzyme_system', String(100)),
                     Column('dose', Float, nullable=True),
                     Column('assump_list_id', Integer, nullable=True)
                     )

    assert_table = Table('Assertions', md,
                         Column('id', Integer, primary_key=True),
                         Column('_name', String(100)),
                         Column('object', String(100)),
                         Column('slot', String(100)),
                         Column('value', String(100)),
                         Column('ready_for_classification', String(100)),
                         Column('assert_by_default', String(100)),
                         Column('evidence_rating', String(100)),
                         Column('cont_val', String(100), nullable=True),
                         Column('numeric_val', String(100), nullable=True),
                         Column('assert_class', String(100)),
                         Column('evidence_for', Integer, nullable=True),
                         Column('evidence_against', Integer, nullable=True)
                         )

    evidence_map_table = Table('Evidence_map', md,
                               Column('id', Integer, primary_key=True),
                               Column('assert_ev_id', Integer),
                               Column('assert_id', Integer)
                               )

    assumption_map_table = Table('Assumption_map', md,
                                 Column('id', Integer, primary_key=True),
                                 Column('assump_list_id', Integer),
                                 Column('ev_id', Integer),
                                 Column('assump_assert_name', String(100))
                                 )

    eslot_table = Table('ESlot',  md,
                        Column('id', Integer, primary_key=True),
                        Column('range_id', Integer),
                        Column('type', String(100)),
                        Column('d_slot_id', Integer),
                        Column('value_string', String(100), nullable=True),
                        Column('value_numeric', Float, nullable=True),
                        Column('value_boolean', Boolean(), nullable=True)
                        )

    emultislot_table = Table('EMultiSlot', md,
                             Column('id', Integer, primary_key=True),
                             Column('range_id', Integer),
                             Column('type', String(100)),
                             Column('value_id', Integer),
                             Column('d_slot_id', Integer)
                             )

    evidence_slot_map_table = Table('Evidence_slot_map', md,
                                    Column('id', Integer, primary_key=True),
                                    Column('assert_id', Integer),
                                    Column('d_slot_id', Integer),
                                    )
    value_table = Table('Value', md,
                        Column('id', Integer, primary_key=True),
                        Column('value_id', Integer),
                        Column('value_string', String(100)),
                        Column('value_numeric', Integer),
                        Column('value_boolean', Boolean())
                        )

    metabolite_table = Table('Metabolite', md,
                       Column('id', Integer, primary_key=True),                       
                       Column('_name', String(100)),
                       Column('metabolite', Boolean()),
                       Column('primary_total_clearance_mechanism', Integer, nullable=True),
                       Column('primary_metabolic_clearance_enzyme', Integer, nullable=True),
                       Column('primary_total_clearance_enzyme', Integer, nullable=True),
                       Column('in_vitro_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_vitro_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('pceut_entity_of_concern', Integer, nullable=True),
                       Column('maximum_concentration', Integer, nullable=True),
                       Column('minimum_therapeutic_dose', Integer, nullable=True),
                       Column('maximum_therapeutic_dose', Integer, nullable=True),
                       Column('assumed_effective_dose',  Integer, nullable=True),
                       Column('substrate_of', Integer, nullable=True),
                       Column('is_not_substrate_of', Integer, nullable=True),
                       Column('inhibits', Integer, nullable=True),
                       Column('does_not_inhibit', Integer, nullable=True),
                       Column('has_metabolite', Integer, nullable=True),
                       Column('permanently_deactivates_catalytic_function', Integer, nullable=True),
                       Column('does_not_permanently_deactivate_catalytic_function', Integer, nullable=True),
                       Column('inhibition_constant', Integer, nullable=True),
                       Column('induces', Integer, nullable=True),
                       Column('increases_auc', Integer, nullable=True),
                       Column('sole_PK_effect_alter_metabolic_clearance', Integer, nullable=True),
                       )                              

    chemical_table = Table('Chemical', md,
                       Column('id', Integer, primary_key=True),                       
                       Column('_name', String(100)),
                       Column('chemical', Boolean()),
                       Column('primary_total_clearance_mechanism', Integer, nullable=True),
                       Column('primary_metabolic_clearance_enzyme', Integer, nullable=True),
                       Column('primary_total_clearance_enzyme', Integer, nullable=True),
                       Column('in_vitro_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_probe_substrate_of_enzyme', Integer, nullable=True),
                       Column('in_vitro_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('in_viVo_selective_inhibitor_of_enzyme', Integer, nullable=True),
                       Column('pceut_entity_of_concern', Integer, nullable=True),
                       Column('maximum_concentration', Integer, nullable=True),
                       Column('minimum_therapeutic_dose', Integer, nullable=True),
                       Column('maximum_therapeutic_dose', Integer, nullable=True),
                       Column('assumed_effective_dose',  Integer, nullable=True),
                       Column('substrate_of', Integer, nullable=True),
                       Column('is_not_substrate_of', Integer, nullable=True),
                       Column('inhibits', Integer, nullable=True),
                       Column('does_not_inhibit', Integer, nullable=True),
                       Column('has_metabolite', Integer, nullable=True),
                       Column('permanently_deactivates_catalytic_function', Integer, nullable=True),
                       Column('does_not_permanently_deactivate_catalytic_function', Integer, nullable=True),
                       Column('inhibition_constant', Integer, nullable=True),
                       Column('induces', Integer, nullable=True),
                       Column('increases_auc', Integer, nullable=True),
                       Column('sole_PK_effect_alter_metabolic_clearance', Integer, nullable=True),
                       )                               

    return [dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table]
