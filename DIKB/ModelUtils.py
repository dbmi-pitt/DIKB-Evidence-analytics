## ModelUtils.py
##
## Classes and methods for modeling objects - a simple frame system

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
## File:          ModelUtils.py

import os,sys, string

## for time stamp
from time import time, strftime, localtime

## for file lock facilities
from Portalocker import lock, unlock, LOCK_EX, LOCK_SH, LOCK_NB

## reviewers able to add evidence to this knowledge base 
## TODO: fix database de-serialization process so that reviewers are
## properly handled. For now, we have to enter in conjunctions of
## reviewers to avoid Slot entry errors
reviewers = ['boycer','c3c','jhorn','ikalet',"boycer,annals2012","boycer,annals2012,ajgp2012","boycer,aj\
gp2012",'roskos']

def getVersion(path):
    """
    get version information
    in: a string identifying the path to the version file
        necessary because the webservers root path is different
        from Gnu Make's
    """
    
    f = os.path.join(path,"VERSION")
    try:
        v = open(f)
    except IOError, err:
        error (" ".join(["can't open :",f]))

    l = str.split(v.readline(),"\n")
    v.close
    return l[0]



##error handling
class InvalidIdentifier(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NonEvidence(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class RejectedEvidence(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CircularEvidence(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def error (text, exit = 1):
    sys.stderr.write (" ".join(["DIKB: error:", text, "\n",]))
    sys.stderr.flush()
    if exit:
        sys.exit (1)
    return

def warning (text, level = 1, exit = 0):
    """Use 3 for information, 2 for warning, 1 for error"""
    log_level = string._int(os.getenv("DIKB_LOG_LEVEL"))
    if (log_level >= level):
        sys.stderr.write (" ".join(["DIKB: warning:", text, "\n",]))
        sys.stderr.flush()
        if exit:
            sys.exit (1)
    return

## logging
def log (text):
    log = open('log.txt', "a+")
    lock(log, LOCK_EX)
    timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
    log.write (" ".join(["DIKB log:", timestamp, " - ", text, "\n",]))
    log.close()
    
 

class Frame(object):
    """A class with some attributes of frames.
    pure virtual: makeInstance()
    """
    def __init__(self):
        self._name = ""
        
    def __str__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'\n',ent,":",'\t',val.__str__(),'\n'])

        return s

    def __html__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'''<b>''',ent,":",'''</b>''',val.__str__(),'''<br>'''])

        return s

    def copy(self, obj):
        """ Recursively copy the contents of this objects slots into the corresponding slots of the new object.
           This method can only be called on objects that contain either lists, strings, numbers,
           or Frame derived classes. It is intended to allow changes to the core representation of objects
           in EvidenceBase and DIKB objects without losing data. Date from older representation can be copied
           into the new representations.

           TODO: A better pattern may be the Factory pattern, but I do not have time to
           look into it right now. Come back to this later.
           TODO: fix this to work with new types; right now it retains the
                 type of the original slot. So if you change of a slot type rather than add
                 or delete a slot, the old slot type is retained; or worse, sometimes it goest to
                 base type of the slot instead of the orignial type. I think the problem has to do with the
                 line:
                        new_obj.__dict__[name] = slot_obj.copy(slot_obj)
           
           @param: an instance of the object this instance will be copied into - new_obj
           out: a deep copy of this object in the new_objects class prototype
        """
        def copy_object(old):
            if not dir(old).__contains__('__dict__'):
                new = old
            else:
                new = old.copy(old)

            return new

        new_obj = obj.makeInstance()
       
        for name, slot_obj in obj.__dict__.iteritems():
            if new_obj.__dict__.has_key(name) and name != '_name':
                
                """strings, numbers, and lists don't have __dict__"""
                if not dir(slot_obj).__contains__('__dict__'):
                    if type(slot_obj) == type([]):
                        new_obj.__dict__[name] = []
                        for item in slot_obj:
                            n = copy_object(item)
                            new_obj.__dict__[name].append(n)
                    else:
                        new_obj.__dict__[name] = slot_obj
                else:
                    ## This should really test for Frame objects
                    new_obj.__dict__[name] = slot_obj.copy(slot_obj)
        
        return new_obj

    def makeInstance(self):
        """ allows dynamic creation of child class instances with the current class
            definition"""
        return Frame()


class Slot(Frame):
    """an class that behaves like a frame-based slot type with constraints
    """
    def __init__(self, allowed_vals = None, default = ""):
        """
        in: allowed_vals - a list of string types, the default values for this slot
        in: default - a string specifying the default value of this slot"""
        Frame.__init__(self)
        self.range =  allowed_vals
        self.value = ""

        self.putEntry(default)

   
    def putEntry(self, entry):
        if self.range == None:
            """No Constraint"""
            self.value = entry
        elif self.range.__contains__(entry):
                self.value = entry
        else:
            warning(" ".join(["allowed values for this slot are: ", ",".join(self.range),
                              "entry: ", str(entry),
                              " not added. Please add a value from the list of allowed values.",
                              "Did you forget to initialize the slot?"]), 1)
            err = entry + " is an invalid identifier for this slot" 

            raise InvalidIdentifier, err

    def delEntry(self, entry):
        self.value = None

    def getEntry(self):
        return self.value
    
    def getRange(self):
        return self.range

    def makeInstance(self):
        return Slot(self.range)


class ContValSlot(Slot):
    """ a slot that possesses a mapping from continous values to discrete value categories.
    """
    def __init__(self, allowed_vals = None, default = "", m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}):
        """
        @param allowed_vals - a list of string types, the default values for this slot
        @param default - a string specifying the default value of this slot
        @param m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats. Categories can be one of"""
        
        ## A mapping of continous value ranges to discrete categories in
        ## the pattern category:[min,max] where min is the lower-bound
        ## of the range, max is the upper bound. Both min and max should be
        ## floats
        self.mapping = m

        Slot.__init__(self, allowed_vals, default)



class MultiSlot(Frame):
    """an class that behaves like a frame-based multi-slot type with constraints
    """
    def __init__(self, allowed_vals = None, default = []):
        """ in: allowed_vals - a list of string types, the default values for this slot
        in: default - a list of strings specifying the default values of this slot"""
        Frame.__init__(self)
        self.range =  allowed_vals
        self.value = []
        self.putEntry(default)
            
    
    def addEntry(self, entry):
        if self.range == None:
            """No Constraint"""
            self.value = entry
        else:
            for item in entry:
                if self.range.__contains__(item):
                    self.value.append(item)
                else:
                    warning(" ".join(["allowed values for this slot are: ", ",".join(self.range),
                                      "entry item : ", item,
                                      " not added. Please be sure values are from the list of allowed values.",
                                      "Did you forget to initialize the slot?"]), 1)
                    err = item + " is an invalid identifier for this slot"
                    raise InvalidIdentifier, err

    def delAllEntries(self):
        self.value = []


    def putEntry(self, entry):
        self.delAllEntries()
        return self.addEntry(entry)
    
    def getEntries(self):
        return self.value
    
    def getRange(self):
        return self.range

    def makeInstance(self):
        return MultiSlot(self.range)

class EvidenceType:
    """Evidence types have a list of Assertions that support or
       refute its owner's value."""
    def __init__(self):
        self.evidence = []
        self.saturation_class = Slot("none_assigned","none_assigned")
        """The assumptions that are implicit when this evidence type is asserted.
        Assumptions are translated into 'enabled assumptions' when the Evidencetype instance
        evaluates to True. The pattern of the generated enabled assumptions is:

        (assume! '(self.assumption[0] 'object 'value) 'dikb-enabled-assumption)
        (assume! '(self.assumption[1] 'object 'value) 'dikb-enabled-assumption)
        ...

        NOTE: this is currently a hack and can lead to ugly mistakes
        if the assumption does not make sense with the object and
        value. For example, this makes sense:

        object: simvastatin
        slot: substrate_of
        value: cyp3a4
        self.assumptions = ['sufficient_concentration_to_inhibit','saturable_concentration']
        enabled assumptions: (assume! '(sufficient-concentration-to-inhibit 'simvastatin 'cyp2c8) 'dikb-enabled-assumption)
                             (assume! '(saturable-concentration 'simvastatin 'cyp2c8) 'dikb-enabled-assumption)

        While this makes no sense:

        object: simvastatin
        slot: level_of_first_pass
        value: more_than_half
        self.assumptions: ['bogus_test_assumption_2','bogus_test_assumption_1']
        enabled assumptions: (assume! '(bogus-test-assumption-1 'simvastatin 'more_than_half) 'dikb-enabled-assumption)
                             (assume! '(bogus-test-assumption-2 'simvastatin 'more_than_half) 'dikb-enabled-assumption)

        TODO: change assumptions to allow new objects, slots, and values.

        """
        self.assumptions = []
        
    def __str__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'\n',ent,":",'\t',val.__str__(),'\n'])
            if ent == "evidence":
                for ev in val:
                    s = "".join([s,'\t\t', ev.__str__(),'\n'])

        return s

    def __html__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'''<br>''',ent,":", val.__str__(),'''<br>'''])
            if ent == "evidence":
                s = s + '''<p>'''
                for ev in val:
                    s = "".join([s, ev.__str__(),'''<br>'''])
                s = s + '''</p>'''

        


class ESlot(Slot, EvidenceType):
    """an ESlot is an evidence slot supporting only one assertion (the
    one stored in the 'value' slot of the Slot type from which it inherits)"""
    def __init__(self, allowed_vals = None, default = ""):
        """
        in: allowed_vals - a list of string types, the default values for this slot
        in: default - a string specifying the default value of this slot"""

        Slot.__init__(self, allowed_vals, default)
        EvidenceType.__init__(self)

    def makeInstance(self):
        return ESlot(self.range)

    def assessEvidence(self,ranking_categories, believable_ev_for, believable_ev_against):
        """If the assertion claims to be ready, evaluate the evidence
           for this slot place it in this objects value variable
           
           in: ranking_categories - a dictionary of categories to which evidence types are
             assigned.  the value of each dictionary entry being a Set
             of ev types - ranking_categories
           in: believable_ev_for -  a list of ranking_categories: if the the set of
             evidence_types in the evidence_for list for this assertion is a superset of any of
             the believable combinations than this assertion is believable.
           in: believable_ev_against -  a list of ranking_categories: if the the set of
             evidence_types in the evidence_against list for this assertion is a superset of any of
             the believable combinations than this assertion is believable.
           out: changing_assumptions - a list values whose evidence meets the current belief
             criteria. For example, if the evidence list contains three assertions, with values
             A, B, and C and one the evidence for A and C meets the current belief criteria than
             changing_assumtions will return the values A and C
           side-effect: each assigned value is placed in the this objects
             values list. NOTE: this is for each assertion that has an assignable
             value.
         """
        changing_assumption = "" ## these are enabled assumptions that are changing state
        if len(self.evidence) > 0:
            if self.evidence[0].ready_for_classification:
                result =  self.evidence[0].assessEvidence(ranking_categories, believable_ev_for, believable_ev_against)
                if  result == 'assume!':
                    changing_assumption = self.evidence[0].value
                    self.value = self.evidence[0].value
                    warning(" ".join(["ESlot::assessEvidence: Assigned value of ",
                                      self.value, " for ", self.evidence[0].object,
                                      self.evidence[0].slot, self.evidence[0].value,
                                    "because evidence evaluated to:", result]), 2)

                elif  result == 'retract!':
                    changing_assumption = self.evidence[0].value
                    ## database maintenance
                    self.value = "none_assigned"
                    warning(" ".join(["ESlot::assessEvidence: Assigned value of ",
                                      self.value, " for ", self.evidence[0].object,
                                      self.evidence[0].slot, self.evidence[0].value,
                                    "because evidence evaluated to:", result]), 2)

                    
                elif result == 'pass':  ## no change in enabled assumption state
                    warning(" ".join(["ESlot::assessEvidence: Passing on ",
                                      self.value, " for ", self.evidence[0].object,
                                      self.evidence[0].slot, self.evidence[0].value,
                                    "because evidence evaluated to:", result]), 2)

                    
        return changing_assumption


class EContValSlot(ESlot):
    """ a slot that possesses a mapping from continous values to discrete value categories.
    """
    def __init__(self, allowed_vals = None, default = "", m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}):
        """
        in: allowed_vals - a list of string types, the default values for this slot
        in: default - a string specifying the default value of this slot
        in: m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats. Categories can be one of"""
        
        ## A mapping of continous value ranges to discrete categories in
        ## the pattern category:[min,max] where min is the lower-bound
        ## of the range, max is the upper bound. Both min and max should be
        ## floats
        self.mapping = m

        ESlot.__init__(self, allowed_vals, default)



class EMultiSlot(MultiSlot, EvidenceType):
    """an EMultiSlot is an evidence slot supporting multiple
    assertions (stored in the list type 'value' slot of the MultiSlot
    type from which it inherits)

    in: allowed_vals - a list of string types, the default values for this slot
    in: default - a list of strings specifying the default values of this slot"""
    def __init__(self, allowed_vals = None, default = []):
        MultiSlot.__init__(self, allowed_vals, default)
        EvidenceType.__init__(self)

    def makeInstance(self):
        return EMultiSlot(self.range)

    def assessEvidence(self, ranking_categories, believable_ev_for, believable_ev_against):
        """Evaluate the evidence for each assertion that claims to be
           ready in this slots evidence list. Place assigned values in
           the this objects values list.

           in: ranking_categories - a dictionary of categories to which evidence types are
             assigned.  the value of each dictionary entry being a Set
             of ev types - ranking_categories
           in: believable_ev_for -  a list of ranking_categories: if the the set of
             evidence_types in the evidence_for list for this assertion is a superset of any of
             the believable combinations than this assertion is believable.
           in: believable_ev_against -  a list of ranking_categories: if the the set of
             evidence_types in the evidence_against list for this assertion is a superset of any of
             the believable combinations than this assertion is believable.
           out: changing_assumptions - a list values whose evidence meets the current belief
             criteria. For example, if the evidence list contains three assertions, with values
             A, B, and C and one the evidence for A and C meets the current belief criteria than
             changing_assumtions will return the values A and C
           side-effect: each assigned value is placed in the this objects
             values list. NOTE: this is for each assertion that has an assignable
             value.
         """
        self.assumptions = []
        changing_assumptions = [] ## these are enabled assumptions that are changing state
        for assertion in self.evidence:
            if assertion.ready_for_classification:
                result = assertion.assessEvidence(ranking_categories, believable_ev_for, believable_ev_against)
                ## if assertion is now believed or not believed,
                ## place it on the list of assertions
                if  result == 'assume!':
                    """Append this assertion's  value (its name) to this slot's value list"""
                    if self.value.__contains__('none_assigned'):
                        self.value.remove('none_assigned')
                    if not self.value.__contains__(assertion.value):
                        self.value.append(assertion.value)
                        
                    warning(" ".join(["EMultiSlot::assessEvidence: Assigned value of ",
                                      assertion.value, " for ", assertion.object, assertion.slot, assertion.value,
                                      "because evidence evaluated to:", result]), 2)

                    changing_assumptions.append(assertion.value)
                   
                elif  result == 'retract!':
                    ## database maintenance
                    if self.value.__contains__(assertion.value):
                        self.value.remove(assertion.value)
                        warning(" ".join(["EMultiSlot::assessEvidence: removed",
                                          assertion.object, assertion.slot, assertion.value,
                                          "from assertions because its evidence evaluated to:", result]), 2)

                    changing_assumptions.append(assertion.value)
                    
                elif result == 'pass':  ## no change in enabled assumption state
                    warning(" ".join(["EMultiSlot::assessEvidence: passing on",
                                      assertion.object, assertion.slot, assertion.value,
                                      "to assertions because its evidence evaluated to:", result]), 2)
                 
        return changing_assumptions
        

class EMultiContValSlot(EMultiSlot):
    """ a multi-valued slot lot that can possess a mapping from continous values to discrete value categories
    """
    def __init__(self, allowed_vals = None, default = "", m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}):
        """
        in: allowed_vals - a list of string types, the default values for this slot
        in: default - a string specifying the default value of this slot
        in: m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats. Categories can be one of"""
        
        ## A mapping of continous value ranges to discrete categories in
        ## the pattern category:[min,max] where min is the lower-bound
        ## of the range, max is the upper bound. Both min and max should be
        ## floats
        self.mapping = m

        EMultiSlot.__init__(self, allowed_vals, default)

    
