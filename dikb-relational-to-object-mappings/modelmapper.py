
'''
Created on Sep 1st, 2011

@author: Hassen

Map classes from DIKB.EvidenceModel to a SQL table
'''
from sqlalchemy.orm import mapper, class_mapper
from sqlalchemy.orm.exc import UnmappedClassError


''' Takes list of classes from DIKB.EvidenceModel and maps them to a table '''
def map(classes, table):
    for c in classes:
        try:
            class_mapper(c)
        except UnmappedClassError:
            mapper(c, table)

def mapAll(dikb_table, ev_table, assert_table, evidence_map_table, assumption_map_table, eslot_table, emultislot_table, evidence_slot_map_table, value_table, metabolite_table, chemical_table):
    map([dikbDAO], dikb_table)
    map([EvidenceDAO], ev_table)
    map([AssertDAO], assert_table)
    map([Evidence_mapDAO], evidence_map_table)
    map([Assumption_mapDAO], assumption_map_table)
    map([ESlotDAO], eslot_table)
    map([EMultiSlotDAO], emultislot_table)
    map([Evidence_Slot_mapDAO], evidence_slot_map_table)
    map([ValueDAO], value_table)
    map([MetaboliteDAO], metabolite_table)
    map([ChemicalDAO], chemical_table)

############################################################
# DAO classes to help w/ mapping
############################################################
class dikbDAO(object):
    def __init__(self):
        self._name = ""
        self.id = None
        self.prodrug = None
        self.primary_total_clearance_mechanism = None
        self.primary_metabolic_clearance_enzyme = None
        self.primary_total_clearance_enzyme = None
        self.in_vitro_probe_substrate_of_enzyme = None
        self.in_viVo_probe_substrate_of_enzyme = None
        self.in_vitro_selective_inhibitor_of_enzyme = None
        self.in_viVo_selective_inhibitor_of_enzyme = None
        self.pceut_entity_of_concern = None
        self.active_ingredient_name = ""
        self.active_ingredient = None
        self.maximum_concentration = None
        self.minimum_therapeutic_dose = None
        self.maximum_therapeutic_dose = None
        self.assumed_effective_dose = None
        self.substrate_of = None
        self.is_not_substrate_of = None
        self.inhibits = None
        self.does_not_inhibit = None
        self.has_metabolite = None
        self.permanently_deactivates_catalytic_function = None
        self.inhibition_constant = None
        self.induces = None
        self.increases_auc = None
        self.sole_PK_effect_alter_metabolic_clearance = None
        self.bioavailability = None
        self.fraction_absorbed = None
        self.fraction_cleared_by = None
 
class MetaboliteDAO(object):
    def __init__(self):
        self._name = ""
        self.id = None
        self.metabolite = None
        self.primary_total_clearance_mechanism = None
        self.primary_metabolic_clearance_enzyme = None
        self.primary_total_clearance_enzyme = None
        self.in_vitro_probe_substrate_of_enzyme = None
        self.in_viVo_probe_substrate_of_enzyme = None
        self.in_vitro_selective_inhibitor_of_enzyme = None
        self.in_viVo_selective_inhibitor_of_enzyme = None
        self.pceut_entity_of_concern = None
        self.maximum_concentration = None
        self.minimum_therapeutic_dose = None
        self.maximum_therapeutic_dose = None
        self.assumed_effective_dose = None
        self.substrate_of = None
        self.is_not_substrate_of = None
        self.inhibits = None
        self.does_not_inhibit = None
        self.has_metabolite = None
        self.permanently_deactivates_catalytic_function = None
        self.does_not_permanently_deactivate_catalytic_function = None
        self.inhibition_constant = None
        self.induces = None
        self.increases_auc = None
        self.sole_PK_effect_alter_metabolic_clearance = None

class ChemicalDAO(object):
    def __init__(self):
        self._name = ""
        self.id = None
        self.chemical = None
        self.primary_total_clearance_mechanism = None
        self.primary_metabolic_clearance_enzyme = None
        self.primary_total_clearance_enzyme = None
        self.in_vitro_probe_substrate_of_enzyme = None
        self.in_viVo_probe_substrate_of_enzyme = None
        self.in_vitro_selective_inhibitor_of_enzyme = None
        self.in_viVo_selective_inhibitor_of_enzyme = None
        self.pceut_entity_of_concern = None
        self.maximum_concentration = None
        self.minimum_therapeutic_dose = None
        self.maximum_therapeutic_dose = None
        self.assumed_effective_dose = None
        self.substrate_of = None
        self.is_not_substrate_of = None
        self.inhibits = None
        self.does_not_inhibit = None
        self.has_metabolite = None
        self.permanently_deactivates_catalytic_function = None
        self.does_not_permanently_deactivate_catalytic_function = None
        self.inhibition_constant = None
        self.induces = None
        self.increases_auc = None
        self.sole_PK_effect_alter_metabolic_clearance = None

class EvidenceDAO(object):
    def __init__(self):
        self._name = ""
        self.id = None
        self.doc_pointer = ""
        self.quote = ""
        self.reviewer = ""
        self.timestamp  = ""
        self.evidence_type = ""
        self.evidence_class = ""
        self.value = None
        self.object_dose = None
        self.precip_dose = None
        self.numb_subjects = None
        self.enzyme_system = ""
        self.dose = None
        self.assump_list_id = None

class AssertDAO(object):
    def __init__(self):
        self.id = None
        self._name = ""
        self.object = ""
        self.slot = ""
        self.value = ""
        self.ready_for_classification = ""
        self.assert_by_default = ""
        self.evidence_rating = ""
        self.cont_val = None
        self.numeric_val = None
        self.assert_class = ""
        self.evidence_for = None
        self.evidence_against = None

class Evidence_mapDAO(object):
    def __init__(self):
        self.id = None
        self.assert_ev_id = None
        self.assert_id = None

class Assumption_mapDAO(object):
    def __init__(self):
        self.id = None
        self.assump_list_id = None
        self.ev_id = None
        self.assump_assert_name = ""

class ESlotDAO(object):
    def __init__(self):
        self.id = None
        self.range_id = None
        self.type = None
        self.d_slot_id = None
        self.value_string = ""
        self.value_numeric = None
        self.value_boolean = None

class EMultiSlotDAO(object):
    def __init__(self):
        self.id = None
        self.range_id = None
        self.type = ""
        self.value_id = None
        self.d_slot_id = None

class Evidence_Slot_mapDAO(object):
    def __init__(self):
        self.id = None
        self.assert_id = None
        self.d_slot_id = None

class ValueDAO(object):
    def __init__(self):
        self.id = None
        self.value_id = None
        self.value_string = ""
        self.value_numeric = None
        self.value_boolean = None
