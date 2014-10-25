
## The Drug Interaction Knowledge Base (DIKB) is (C) Copyright 2005- by
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
## File:          TranslationRules.py


def txt_cln(s):
    """prepare a string for processing in the JTMS"""
    t = s.replace("'","prime-")
    return t.replace("--","-")

def assume_in_vitro_based_enzyme_modification_assertions(ac):
    """ write a JTMS assumption specifying that in vitro-based evidence is acceptable

    @param ac:bool True if action is to assert!, False if action is to
                 retract!, None to get the representation of the assumption
    @returns: a string representation of the appropriate JTMS
    assumption
    """
    rep = "(accept-in-vitro-based-enzyme-modulation-assertions)"
    
    if ac == True:
        return "(assume! '%s 'dikb-inference-assumption)" % rep
    elif ac == False:
        return "(retract! '%s 'dikb-inference-assumption)" % rep
    else:
        return rep

def assume_bc_satisfied(a, ac):
    """ write a JTMS assumption specifying that belief criteria for an assertion has been satisfied

    @param a:an instance of Assertion or a sub-class
    @param ac:bool True if action is to assert!, False if action is to
                 retract!
    @returns: a string  representation of the appropriate JTMS assumption
    """
    if ac:
        return "(assume!\n\t'(bc-satisfied '%s) 'dikb-inference-assumption)" % a._id
    else:
        return "(retract!\n\t'(bc-satisfied '%s) 'dikb-inference-assumption)" % a._id
  
## assertion mappings

# a mapping for categorical assertions
categorical_assertion_map = {'active_ingredient' : '1-is-an-active-ingredient',
                             'metabolite' : '1-is-a-metabolite',
                             'prodrug' : '1-is-a-prodrug'
                             }

# a mapping for single valued assertions
single_val_assertion_map = { 'polymorphic_enzyme' : '1-is-a-polymorphic-enzyme',
                             'pceut_entity_of_concern' : '1-is-an-pceut-entity-of-concern',
                             }

# a mapping of basic assertion 'slots' to their jtms represetation strings
basic_assertion_map = {'has_metabolite': '1-has-metabolite-2',
                       'substrate_of': '1-is-substrate-of-2',
                       'is_not_substrate_of': '1-is-not-a-substrate-of-2',
                       'inhibits': '1-inhibits-2 ',
                       'does_not_inhibit': '1-does-not-inhibit-2',
                       'primary_total_clearance_mechanism': 'primary-total-clearance-mechanism-of-1-is-2',
                       'primary_metabolic_clearance_enzyme' : 'primary-metabolic-clearance-enzyme-of-1-is-2',
                       'primary_total_clearance_enzyme' : 'primary-total-clearance-enzyme-of-1-is-2',
                       'sole_PK_effect_alter_metabolic_clearance' : 'sole-pk-effect-of-1-on-2-alter-metabolic-clearance',
                       'in_vitro_probe_substrate_of_enzyme' : '1-is-an-in-vitro-probe-substrate-of-2',
                       'in_viVo_probe_substrate_of_enzyme' : '1-is-an-in-viVo-probe-substrate-of-2',
                       'in_vitro_selective_inhibitor_of_enzyme' : '1-is-an-in-vitro-selective-inhibitor-of-2',
                       'in_viVo_selective_inhibitor_of_enzyme' : '1-is-an-in-viVo-selective-inhibitor-of-2',
                       'permanently_deactivates_catalytic_function' : '1-permanently-deactivates-catalytic-function-of-2',
                       'does_not_permanently_deactivate_catalytic_function' : '1-does-not-permanently-deactivate-catalytic-function-of-2',
                       'controls_formation_of' : '1-controls-formation-of-2'
                       }

# a mapping of discretized assertion 'slots' to their jtms representation strings
discretized_assertion_map = {'first_pass_effect' : 'first-pass-effect-of-1-is-2',
                             'bioavailability' : 'bioavailability-of-1-is-2',
                             'fraction_absorbed' : 'oral-dose-fraction-absorbed-of-1-is-2'
                             }

# a mapping of real-valued assertion 'slot's to their jtms representation strings
numeric_assertion_map = {'inhibition_constant' : 'inhibition-constant-of-1-for-2-is-3',
                         'minimum_therapeutic_dose' : 'minimum-therapeutic-dose-of-1-is-2',
                         'maximum_therapeutic_dose' : 'maximum-therapeutic-dose-of-1-is-2',
                         'assumed_effective_dose' : 'assumed-effective-dose-of-1-is-2'
                         }
# a mapping of real-valued assertion 'slot's to their jtms representation strings for assertions that 1) export the maximum value among evidence items that meet belief criteria and 2) require the dose used in the experiment/study during inference
max_valued_dose_dependent_assertion_map = { 'maximum_concentration' : 'maximum-in-vivo-concentration-of-1-is-2-at-dose-3'}

# a mapping of which of a numeric  assertion's variables to use when building a JTMS representation. 3 says
# to use '1','2','3' => a.obj, a.val, a.numeric_val as in the example above for 'inhibition-constant';
# 2 says to use '1','2' => a.obj, a.numeric_val as is done for  'bioavailability-of-1-is-2'
n_it_map = {'inhibition_constant' : 3,
            'maximum_concentration' : 2,
            'minimum_therapeutic_dose' : 2,
            'maximum_therapeutic_dose' : 2,
            'assumed_effective_dose' : 2
            }

def categorical_assertion_to_jtms(s, obj, ac):
    """ convert this DIKB assertion to a JTMS assertion

    @param s:string - representation of the assertion type
           e.g. '1-is-an-active-ingredient' where '1' is the string name of a DIKB_instance object
    @param obj:string - the string name of a DIKB_instance object
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion
    """
    obj_cln = txt_cln(obj)
    rep = "(%s '%s)" % (s, obj_cln)
    if ac:
        return  "(assert! '%s \n\t'(dikb-categorical-assertion))" % (rep)

    return rep
    
def single_val_assertion_to_jtms(ev, s, a, ac):
    """ convert this DIKB assertion t

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param s:string - representation of the assertion type
           e.g. '1-is-a-polymorphic-enzyme' where '1' is the object of the
           Assertion instance 
    @param a:an instance of Assertion or a sub-class
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion
    @returns: the jtms representation of this assertion as a string
    """
    obj = txt_cln(a.object)
    rep = "(%s '%s)" % (s, obj)

    if not ac:
            return rep

    s_exp = "(assert! '%s \n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)" % (rep, a._id)
    a_str = get_assumption_reps(ev, a)
    if a_str == None:
        pass
        #print "ERROR: TranslationRules::single_val_assertion_to_jtms - could not get a representation for the assumptions belonging to assertion '%s''s evidence items!" % a._name
        return None
    s_exp += a_str + "\n"
    s_exp += "\t))"
    
    return  s_exp


                          

def basic_assertion_to_jtms(ev, s, a, ac):
    """ convert this DIKB assertion to a JTMS assertion

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param s:string - representation of the assertion type
           e.g. '1-inhibits-2' where '1' is the object and '2' is the value of the
           Assertion instance 
    @param a:an instance of Assertion or a sub-class
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion
    @returns: the jtms representation of this assertion as a string
    """
    obj = txt_cln(a.object)
    val = txt_cln(a.value)
    rep = "(%s '%s '%s)" % (s, obj, val)

    if not ac:
        return rep

    s_exp =  "(assert! '%s \n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)" % (rep, a._id)
    a_str = get_assumption_reps(ev, a)
    if a_str == None:
        #print "ERROR: TranslationRules::basic_assertion_to_jtms - could not get a representation for the assumptions belonging to assertion '%s''s evidence items!" % a._name
        return None
    s_exp += a_str + "\n"
    s_exp += "\t))"
    
    return  s_exp




def discretized_assertion_to_jtms(ev, s, a, ac):
    """ convert this discrete valued DIKB assertion to a JTMS assertion

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param s:string - representation of the assertion type
           e.g. 'first-pass-effect-of-1-is-2' where '1' is the object and '2' is the cont_value of the
           ContValAssertion instance 
    @param a:an instance of ContValAssertion or a sub-class
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion
    @returns: the jtms representation of this assertion as a string
    """
    obj = txt_cln(a.object)
    if not a.cont_val:
        #print "It appears that no value has been assigned to the cont_val slot of assertion '%s'; returning None" % a._name
        return None
    val = txt_cln(a.cont_val)
    rep = "(%s '%s '%s)" % (s, obj, val)

    if not ac:
        return rep

    s_exp = "(assert! '%s \n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)" % (rep, a._id)
    a_str = get_assumption_reps(ev, a)
    if a_str == None:
        #print "ERROR: TranslationRules::discretized_assertion_to_jtms - could not get a representation for the assumptions belonging to assertion '%s''s evidence items!" % a._name
        return None
    s_exp += a_str + "\n"
    s_exp += "\t))"
    
    return  s_exp

def cont_val_assertion_to_jtms(ev, s, a, ac):
    """ convert this continous valued DIKB assertion to a JTMS assertion

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param s:string - representation of the assertion type
           e.g. 'inhibition-constant-of-1-for-2-is-3' where '1' is the object and '2' is the value and '3'
           is  of the numeric_val of a  ContValAssertion instance 
    @param a:an instance of ContValAssertion or a sub-class
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion

    @returns: the jtms representation of this assertion as a string
    """
    obj = txt_cln(a.object)
    val = txt_cln(a.value)
    if not a.numeric_val:
        #print "TranslationRules::cont_val_assertion_to_jtms - It appears that no value has been assigned to the numeric_val slot of assertion '%s'; returning None" % a._name
        return None
    n_val = "%.3E" % a.numeric_val

    if not n_it_map.has_key(a.slot):
        #print "TranslationRules::cont_val_assertion_to_jtms - could not find key '%s' in  n_it_map" % a.slot
        return None

    if n_it_map[a.slot] == 2:
        rep = "(%s '%s '%s)" % (s, obj, n_val)
    elif n_it_map[a.slot] == 3:
        rep = "(%s '%s '%s '%s)" % (s, obj, val, n_val)

    if not ac:
        return rep

    s_exp =  "(assert! '%s \n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)" % (rep, a._id)
    a_str = get_assumption_reps(ev, a)
    if a_str == None:
        #print "ERROR: TranslationRules::cont_val_assertion_to_jtms - could not get a representation for the assumptions belonging to assertion '%s''s evidence items!" % a._name
        return None
    s_exp += a_str + "\n"
    s_exp += "\t))"
    
    return  s_exp


def max_valued_dose_dependent_assertion_to_jtms(ev, s, a, ac):
    """ convert this continous valued DIKB assertion to a JTMS assertion that includes the dose used in the study/experiment 

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param s:string - representation of the assertion type
           e.g. 'maximum-in-vivo-concentration-of-1-is-2-at-dose-3' where '1' is the object and '2' is the value and '3' is the dose used in the evidence item that was chosen to provide the numeric value in the assertion
    @param a:an instance of ContValAssertion or a sub-class
    @param ac:bool True if action is to assert!, False or None to get the representation of the assertion

    @returns: the jtms representation of this assertion as a string
    """
    obj = txt_cln(a.object)
    val = txt_cln(a.value)
    if not a.numeric_val:
        #print "TranslationRules::cont_val_assertion_to_jtms - It appears that no value has been assigned to the numeric_val slot of assertion '%s'; returning None" % a._name
        return None
    n_val = "%.3E" % a.numeric_val

    try:
        ev_idx = a.ev_bc_cache[0] # the index of the evidence item used to
                                  # generate the numeric value for this
                                  # assertion
    except IndexError:
        #print "TranslationRules::cont_val_assertion_to_jtms - the ev_bc_cache list does not contain anything -- has the evidence for this assertion been assessed?
        return None

    try:
        ev_item = a.evidence_for[ev_idx]
    except IndexError:
        #print "TranslationRules::cont_val_assertion_to_jtms - the evidence_for list does not contain anything  at index ev_bc_cache!
        return None
    
    try:
        dose = "%.3E" % float(ev_item.dose)
    except AttributeError:
        #print "TranslationRules::cont_val_assertion_to_jtms - no dose attribute in the evidence item pionted to by ev_bc_cache
        return None
    
    if not n_it_map.has_key(a.slot):
        #print "TranslationRules::cont_val_assertion_to_jtms - could not find key '%s' in  n_it_map" % a.slot
        return None

    if n_it_map[a.slot] == 2:
        rep = "(%s '%s '%s '%s)" % (s, obj, n_val, dose)
    elif n_it_map[a.slot] == 3:
        rep = "(%s '%s '%s '%s '%s)" % (s, obj, val, n_val, dose)

    if not ac:
        return rep

    s_exp =  "(assert! '%s \n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)\n\t\t(assumed-effective-dose-of-1-is-2 '%s '%s)" % (rep, a._id, obj, dose)
    a_str = get_assumption_reps(ev, a)
    if a_str == None:
        #print "ERROR: TranslationRules::cont_val_assertion_to_jtms - could not get a representation for the assumptions belonging to assertion '%s''s evidence items!" % a._name
        return None
    s_exp += a_str + "\n"
    s_exp += "\t))"
    s_exp += "\n(assume! `(assumed-effective-dose-of-1-is-2 '%s '%s) `dikb-inference-assumption)\n" % (obj, dose)
    
    return  s_exp

def increases_auc_to_jtms(a):
     """ convert this DIKB assertion to a JTMS assertion

     @param a:an instance of Assertion or a sub-class
     @returns: the jtms representation of this assertion as a string
     """
     pl = [txt_cln(elt) for elt in a.prop_lst]
     asrt = "(assert! '(1-increases-auc-of-2-by-3-at-object-dose-4-precip-dose-5 '%s '%s)\n\t'(dikb-assertion\n\t\t(bc-satisfied '%s)))" % (pl[1], pl[2], pl[5], pl[3], pl[4], a._id)
     return asrt

## interface to assertion mappings
def get_asrt_to_jtms(ev, obj, slot, val):
    """
    Return a JTMS representation given an object, slot, and value and a dictionary of Assertion instances

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param obj:string - the name of a DIKB instance 
    @param slot:string - the string name of a slot for obj
    @param val:string - the string name of a value for obj
  
    @returns: a JTMS representation of the given an object, slot, and value
    """
    if slot in categorical_assertion_map.keys():
        return categorical_assertion_to_jtms(categorical_assertion_map[slot],obj,True)

    k = '_'.join([obj,slot,val])
    if not ev.objects.has_key(k):
        #print "TranslationRules::get_asrt_to_jtms - There is no assertion matching the object, slot, value (%s, %s, %s) in the evidence-base" % (obj, slot, val)
        return None
    asrt = ev.objects[k]
        
    if slot in single_val_assertion_map.keys():
        return single_val_assertion_to_jtms(ev, single_val_assertion_map[slot],asrt,True)

    if slot in basic_assertion_map.keys():
        return basic_assertion_to_jtms(ev, basic_assertion_map[slot],asrt, True)

    if slot in discretized_assertion_map.keys():
        return discretized_assertion_to_jtms(ev, discretized_assertion_map[slot],asrt,True)
    
    if slot in numeric_assertion_map.keys():
        return cont_val_assertion_to_jtms(ev, numeric_assertion_map[slot],asrt,True)

    if slot in max_valued_dose_dependent_assertion_map.keys():
        return max_valued_dose_dependent_assertion_to_jtms(ev, max_valued_dose_dependent_assertion_map[slot], asrt, True)

    #print "TranslationRules::get_asrt_to_jtms - Sorry, I could not find the key '%s' in any assertion mapping" % slot
    return None

def get_rep(ev, k):
    """
    Return a JTMS representation given a Assertion instance by its key

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param k:string - the key of the assertion in the evidence-base 
  
    @returns: a JTMS representation of the given an object, slot, and value
    """
    if not ev.objects.has_key(k):
        #print "TranslationRules::get_rep - There is no assertion matching key '%s' in the evidence-base" % k
        return None
    asrt = ev.objects[k]
        
    if asrt.slot in single_val_assertion_map.keys():
        return single_val_assertion_to_jtms(ev, single_val_assertion_map[asrt.slot],asrt,False)

    if asrt.slot in basic_assertion_map.keys():
        return basic_assertion_to_jtms(ev, basic_assertion_map[asrt.slot],asrt,False)

    if asrt.slot in discretized_assertion_map.keys():
        return discretized_assertion_to_jtms(ev, discretized_assertion_map[asrt.slot],asrt,False)
    
    if asrt.slot in numeric_assertion_map.keys():
        return cont_val_assertion_to_jtms(ev, numeric_assertion_map[asrt.slot],asrt, False)

    if asrt.slot in max_valued_dose_dependent_assertion_map.keys():
        return max_valued_dose_dependent_assertion_to_jtms(ev, max_valued_dose_dependent_assertion_map[asrt.slot], asrt, False)

    #print "TranslationRules::get_rep - Sorry, I could not find the key '%s' in any assertion mapping" % slot
    return None

def get_assumption_reps(ev, a):
    """
    return a string containing the representation of all assumptions
    belonging to an assertions 'evidence-for' item's that were used to
    establish that the assertion meets belief criteria and determine
    any continuous or discrete value for the assertion

    @param ev:an instance of EvidenceBase containing Assertions instances
    @param a:an instance of Assertion or a sub-class
    @returns: string containing the representation of all assumptions
              belonging to an assertions 'evidence-for' item's
    """
    s_exp = ""

    if a.ev_bc_cache == None:
        #print "ERROR: TranslationRules::get_assumption_reps - cannot export assumptions because ev_bc_cache is not initialized for this assertion '%s'!" % a._name
        return None
    elif a.ev_bc_cache == []:
        #print "Warning: TranslationRules::get_assumption_reps - cannot export assumptions because ev_bc_cache is an empty list for assertion '%s'!" % a._name
        return ""
    else:
        pass
        #print "TranslationRules::get_assumption_reps - exporting assumptions for the following evidence items in the evidence for list: %s" % str(a.ev_bc_cache)

    ev_l = []
    for idx in a.ev_bc_cache:
        ev_l.append(a.evidence_for[idx])
    
    for elt in ev_l:
        for asmp in elt.assumptions.getEntries():
            mp = get_rep(ev, asmp)
            if not mp:
                #print "ERROR: TranslationRules::get_assumption_reps - could not get representation for  assumption '%s'!" % asmp
                return None
            s_exp += mp + "\n"

    return s_exp
