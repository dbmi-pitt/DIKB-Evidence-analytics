## DrugModel.py
##
## The classes and method used to represent drugs

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
## File:          DrugModel.py

import os,sys, string

from Observer import *
from ModelUtils import * 
from Defines import *



class DIKB_instance(Frame, Observer):
    def __init__(self):
        Observer.__init__(self, None, None, None)
        Observer.__init__(self)

    
    def __html__(self):
        s = ""

        for ent, val in self.__dict__.iteritems():
            if ent not in ["_name","ingredients"]:
                s = s + "<p>"
                s = "".join([s,'''<br><b>''',ent,":</b>", val.__html__(),'''<br>'''])
                s = s + '''</p>'''
                  
        return s

    
    def update(self, observable, event, assertion):
        warning("".join(["DIKB_instance: ", self._name, " I have been notified of a change to evidence base with event = ",
                         str(event)]), 3)
        warning("".join(["Data: ",assertion.__str__()]), 3)
        
        if assertion.object != self._name:
            warning("I am not  " + assertion.object + "!", 3)
            return None
        
        elif not self.__dict__.has_key(assertion.slot):
            warning("I do not have slot: " + assertion.slot, 3)
            return None
        
        if event == ADD_ASSERTION:
            warning("".join(["attempting to add assertion for ", "_".join([assertion.object, assertion.slot, assertion.value])]), 2)
            if (type(self.__dict__[assertion.slot]) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__()))  or  (type(self.__dict__[assertion.slot]) in ([type(ESlot())] +  ESlot().__class__.__subclasses__())):
                self.__dict__[assertion.slot].evidence.append(assertion)
            else:
                warning("".join([assertion.slot, " is not an evidence slot! Cannot add evidence for this slot."]), 1) 
            return None
        
        elif event == REPLACE_ASSERTION:
            warning("Replacement of assertion for" +  assertion.slot + "noted", 3)

        elif event == MODIFY_ASSERTION:
            warning("Modification of assertion for" +  assertion.slot + "noted", 3)

        elif event == DELETE_ASSERTION:
            warning("".join(["attempting to delete assertion for ", "_".join([assertion.object, assertion.slot, assertion.value])]), 2)
            if (type(self.__dict__[assertion.slot]) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__())) or (type(self.__dict__[assertion.slot]) in [type(ESlot())] +  ESlot().__class__.__subclasses__()):
                f = False
                for ev in self.__dict__[assertion.slot].evidence:
                    """we cannot assume the object references are the same so must go by the value of the assertion"""
                    if ev.value == assertion.value:
                        warning("".join(["deleting assertion for ", "_".join([assertion.object, assertion.slot, assertion.value])]), 2)
                        self.__dict__[assertion.slot].evidence.remove(ev)
                        f = True
                        
                if not f:
                    warning("".join(["DIKB_instance: ", self._name, " update - Could not find assertion to delete. Looking for ",
                                     assertion.value]), 1)
            else:
                warning("".join([assertion.slot, " is not an evidence slot! Cannot add evidence for this slot."]), 1)
                
        elif event == RENOTIFY:
            warning("".join(["attempting to replace assertion for ", "_".join([assertion.object, assertion.slot, assertion.value])]), 2)
            if (type(self.__dict__[assertion.slot]) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__())) or (type(self.__dict__[assertion.slot]) in [type(ESlot())] +  ESlot().__class__.__subclasses__()):
                self.__dict__[assertion.slot].evidence.append(assertion)
            else:
                warning("".join([assertion.slot, " is not an evidence slot! Cannot add evidence for this slot."]), 1) 
            return None
        else:
            warning("".join(["DIKB_instance: ", self._name, " update - Could not find event ", str(event), "!. "]), 1)


class Enzyme(DIKB_instance):
    def __init__(self, enz_name):
        DIKB_instance.__init__(self)

        """ the name of this Enzyme from the DIKB ontology"""
        try:
            f = open("data/enzymes")
        except IOError, err:
            warning(" ".join(["Could not open file containing enzyme names:",os.getcwd(),"data/enzymes", "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        enz_names = filter(lambda x: x != "", t.split("\n"))

        # a list of valid metabolite names
        try:
            f = open("data/chemicals_produced_by_metabolism")
        except IOError, err:
            warning(" ".join(["Could not open file containing metabolite names:",os.getcwd(),"data/chemicals_produced_by_metabolism", 
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        self.metabolite_names = filter(lambda x: x != "", t.split("\n"))
        f.close()

        
        self.enzyme_name = Slot(enz_names, enz_name)
        self._name = enz_name

        """True if this enzyme is polymorphic has multiple
        drug-catalysis phenotypes due to genetic polymorphisms"""
        self.polymorphic_enzyme = ESlot(["True","False","none_assigned"],"none_assigned")

        """biochemical physical entity formations that this enzyme catalyzes """
        self.controls_formation_of = EMultiSlot(self.metabolite_names  + ["none_assigned"],["none_assigned"])

        

    def makeInstance(self):
        d = Enzyme(self._name)
        ##print "Making instance of Enzyme: " + d._name
        return d

        

class Pharmaceutical_Preparation(DIKB_instance):
    def __init__(self, prep_name, ndc_code, va_ndfrt_code):
        DIKB_instance.__init__(self)

        """ the name of this pharmaceutical preparation in the DIKB"""
        try:
            f = open("data/va-ndfrt-pharmaceutical-preparations")
        except IOError, err:
            warning(" ".join(["Could not open file containing pharmaceutical preparation names:",os.getcwd(),"data/va-ndfrt-pharmaceutical-preparations", "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        ##TODO : make sure to split off a newline if it exists
        names = t.split(",")
        self.prep_name = Slot(names, prep_name)
        self._name = prep_name
        self.ndc_code = ndc_code
        self.va_ndfrt_code = va_ndfrt_code
        
        """active ingredient names from the VA-NDFRT terminology """
        try:
            f = open("data/va-ndfrt-active-ingredients")
        except IOError, err:
            warning(" ".join(["Could not open file containing active ingredient names:",os.getcwd(),"data/va-ndfrt-active-ingredients",
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        ##TODO : make sure to split off a newline if it exists
        names = t.split(",")
        self.ingredients =  MultiSlot(names,["none_assigned"])

        """the form of the preparation oral, transdermal, or iv"""
        self.form = Slot(["oral", "transdermal","iv"],"oral")

        """is the preparation a normal or extended release formulation?"""
        self.preparation = Slot(["normal_release", "extended_release","none_assigned"],"none_assigned")

        """the dose of the preparation"""
        self.dose = ContValSlot(None, "none_assigned")

    def makeInstance(self):
        d = Pharmaceutical_Preparation(self._name)
        ##print "Making instance of Pharmaceutical_Preparation: " + d._name
        return d



class Pceut_Entity(DIKB_instance):
    """an abstract class for pharmaceutical entities like active
    ingredients and metabolites. This class in not meant to be
    directly instanctiated; rather, it provides slots that are common
    to child classes"""
    def __init__(self):
        DIKB_instance.__init__(self)

        ## get enzyme names
        try:
            f = open("data/enzymes")
        except IOError, err:
            warning(" ".join(["Could not open file containing enzyme names:",os.getcwd(),"data/enzymes", "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        f.close()
        self.enzymes = filter(lambda x: x != "", t.split("\n"))

        ## get names of all active ingredients and metabolites
        try:
            f = open("data/chemicals_produced_by_metabolism")
        except IOError, err:
            warning(" ".join(["Could not open file containing metabolite names:",os.getcwd(),"data/chemicals_produced_by_metabolism", 
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        self.metabolite_names = filter(lambda x: x != "", t.split("\n"))
        f.close()

        try:
            f = open("data/va-ndfrt-active-ingredients")
        except IOError, err:
            warning(" ".join(["Could not open file containing active ingredent names:",os.getcwd(),"data/va-ndfrt-active-ingredients", 
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        f.close()
        self.drug_names = t.split(",")

        try:
            f = open("data/non_therapeutic_or_metabolic_chemicals")
        except IOError, err:
            warning(" ".join(["Could not open file containing non_therapeutic_or_metabolic_chemicals:",
                              os.getcwd(),"data/non_therapeutic_or_metabolic_chemicals", 
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        t = f.read()
        f.close()
        self.chemical_names = filter(lambda x: x != "", t.split("\n"))
        
        names = self.metabolite_names + self.drug_names + self.chemical_names


        """ the maximum concentration ($C_{max}$) in grams/l that the drug is known to reach at a particular dose given in grams """ 
        self.maximum_concentration =  EMultiContValSlot(["continuous_value"],["continuous_value"], None)
        
        """The minimum therapeutic dose based on evidence"""
        self.minimum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)

        """The maximum therapeutic dose based on evidence"""
        self.maximum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)

        """The assumed effective dose"""
        self.assumed_effective_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)

        """Enzymes that this drug is a substrate of"""
        self.substrate_of = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """Enzymes that this drug is not a substrate of"""
        self.is_not_substrate_of = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])
    
        """Enzymes that this drug inhibits by competitive, MI-complex, or non-competitive inhibition"""
        self.inhibits = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """An incomplete list of self.enzymes that this drug does not inhibit by any known mechanism"""
        self.does_not_inhibit = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])
     
        """a biochemical entity that this pharaceutical entity is transformed to via catalysis """
        self.has_metabolite = EMultiSlot(self.metabolite_names  + ["none_assigned"],["none_assigned"])

        """Enzymes that this drug competitively inhibits"""
        self.does_not_permanently_deactivate_catalytic_function = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """enzymes for which this drug inhibits in such a way that the enzyme is no longer available for calysis (see~\ref{sec:mi-inh}"""
        self.permanently_deactivates_catalytic_function = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """each list member hold the concentration, in grams/L at which the drug instance inhibits .5 of the enzyme's activity"""
        self.inhibition_constant = EMultiContValSlot(self.enzymes + ["none_assigned"],["none_assigned"], None)
        # was - self.inhibition_constant =  EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """Enzymes that this drug is induces"""
        self.induces = EMultiSlot(self.enzymes  + ["none_assigned"],["none_assigned"])

        """the mechanism responsible for more than .5 of the drug instance's clearance"""
        self.primary_total_clearance_mechanism = ESlot(["none_assigned" , "Renal_Excretion", "Metabolic_Clearance" , "Exhalation_Excretion","Biliary_Excretion"],"none_assigned")

        """The enzyme responsible for at least .5 of the drug instance's clearance by metabolism alone"""
        self.primary_metabolic_clearance_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """the enzyme responsible for more than .5 of the drug instance's total clearance by any clearance mechanism """
        self.primary_total_clearance_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """a list of self.enzymes for which this drug is considered a valid in vitro probe substrate; see \ref{sec:ivps}"""
        self.in_vitro_probe_substrate_of_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """a list of self.enzymes for which this drug is considered a valid in viVo probe substrate; see \ref{sec:ivvps}"""
        self.in_viVo_probe_substrate_of_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """a list of self.enzymes for which this drug is considered a selective inhibitor in viTro, see \ref{sec:ivsi}"""
        self.in_vitro_selective_inhibitor_of_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """a list of self.enzymes for which this drug is considered a selective inhibitor in viVo, see \ref{sec:ivvsi}"""
        self.in_viVo_selective_inhibitor_of_enzyme = ESlot(self.enzymes  + ["none_assigned"],"none_assigned")

        """the drugs that this drug is known to cause an increase in AUC in during pharmacokinetic trials"""
        self.increases_auc = EMultiContValSlot(names + ["none_assigned"],["none_assigned"],{"low":[0.0,1.0],"medium-low":[1.0,1.0],"medium":[1.0,2.0],"medium-high":[2.0,2.0],"high":[2.0,100000.0]})

        """considered a drug of concern?"""
        self.pceut_entity_of_concern = ESlot(["True","False","none_assigned"],"none_assigned")

        """asserts that the drug's sole pharmacokinetic effect on another drug, \texttt{X}, is alteration
           of \texttt{X}'s  metabolic clearance """ 
        self.sole_PK_effect_alter_metabolic_clearance =  EMultiSlot(names + ["none_assigned"],["none_assigned"])
   

        # implement the __setstate__ method if the schema changes
        def __setstate__(self, state):
            
            if 'minimum_therapeutic_dose_is_at_least' in state:
                del(state['minimum_therapeutic_dose_is_at_least'])

            # UNCOMMENT THIS WHEN THERE IS A CHANGE TO THE METABOLITE NAME FILE
            # get names of all active ingredients and metabolites
            #if 'metabolite_names' in state:
            #    del(state['metabolite_names'])
                
            #try:
            #    f = open("data/chemicals_produced_by_metabolism")
            #except IOError, err:
            #    warning(" ".join(["Could not open file containing metabolite names:",os.getcwd(),"data/chemicals_produced_by_metabolism", 
            #                      "Please make sure this file exists. Returning None"]), 1)
            #    return None
            #t = f.read()
            # TODO : make sure to split off a newline if it exists
            #self.metabolite_names = t.split("\n")
            #f.close()
           
            #state['has_metabolite'].range = self.metabolite_names + ["none_assigned"]
            #state['increases_auc'].range = self.metabolite_names + state['drug_names'] + ["none_assigned"]
            #state['sole_PK_effect_alter_metabolic_clearance'].range = self.metabolite_names + state['drug_names'] + ["none_assigned"]
            
                
            self.__dict__.update(state)
            

class Chemical(Pceut_Entity):
    def __init__(self, chemical_name):
        Pceut_Entity.__init__(self)

        """chemical names come from various places; they are found,
        linked to external database references in the DIKB ontology,
        and placed in a file for use in the DIKB"""
       
        if chemical_name != "" and chemical_name != None:
            if self.chemical_names.__contains__(chemical_name):
                self.chemical_name = Slot(self.chemical_names, chemical_name)
                self._name = chemical_name
            else:
                warning("".join(["Cannot accept ", str(chemical_name),
                                 " as identifier, possible values are:\n",
                                 ",".join(self.chemical_names)]), 1)
                return None
        else:
            warning("".join(["Cannot accept ", str(chemical_name),
                             " as identifier, Please initialize this  instance with the",
                             "generic name like \'m1 = Chemical(\"chemical name\")\'"]), 1)
            return None

        self.chemical = Slot(["True","False","none_assigned"],"True")


    def makeInstance(self):
        d = Chemical(self._name)
        ##print "Making instance of Chemical: " + d._name
        return d

    ## implement the __setstate__ method if the schema changes
    #def __setstate__(self, state):
       
        #         if 'drug_of_concern' in state:
        #             del(state['drug_of_concern'])

    
        #if 'metabolite' not in state:
           # self.metabolite = Slot(["True","False","none_assigned"],"True")
            

        #self.__dict__.update(state)


class Metabolite(Pceut_Entity):
    def __init__(self, metabolite_name):
        Pceut_Entity.__init__(self)

        """metabolite names come from various places; they are found,
        linked to external database references in the DIKB ontology,
        and placed in a file for use in the DIKB"""
       
        if metabolite_name != "" and metabolite_name != None:
            if self.metabolite_names.__contains__(metabolite_name):
                self.metabolite_name = Slot(self.metabolite_names, metabolite_name)
                self._name = metabolite_name
            else:
                warning("".join(["Cannot accept ", str(metabolite_name),
                                 " as identifier, possible values are:\n",
                                 ",".join(self.metabolite_names)]), 1)
                return None
        else:
            warning("".join(["Cannot accept ", str(metabolite_name),
                             " as identifier, Please initialize this  instance with the",
                             "generic name like \'m1 = Metabolite(\"metabolite name\")\'"]), 1)
            return None

        self.metabolite = Slot(["True","False","none_assigned"],"True")


    ## implement the __setstate__ method if the schema changes
    #def __setstate__(self, state):
       
        #         if 'drug_of_concern' in state:
        #             del(state['drug_of_concern'])

    
        #if 'metabolite' not in state:
           # self.metabolite = Slot(["True","False","none_assigned"],"True")
            

        #self.__dict__.update(state)
        

    def makeInstance(self):
        d = Metabolite(self._name)
        ##print "Making instance of Metabolite: " + d._name
        return d


        
class Drug(Pceut_Entity): 
    def __init__(self, active_ingredient_name):
        Pceut_Entity.__init__(self)
        
        """active ingredient names from the VA-NDFRT terminology """
        
        if active_ingredient_name != "" and active_ingredient_name != None:
            if self.drug_names.__contains__(active_ingredient_name):
                self.active_ingredient_name = Slot(self.drug_names, active_ingredient_name)
                self._name = active_ingredient_name
            else:
                warning("".join(["Cannot accept ", str(active_ingredient_name),
                                 " as identifier, possible values are:\n",
                                 ",".join(self.drug_names)]), 1)
                return None
        else:
            warning("".join(["Cannot accept ", str(active_ingredient_name),
                             " as identifier, Please initialize this drug instance with the",
                             "generic name like \'drug = Drug(\"generic name\")\'"]), 1)
            return None

        self.active_ingredient = Slot(["True","False","none_assigned"],"True")
        self.prodrug = Slot(["True","False","none_assigned"],"none_assigned")
        
        """a qualitative statement of the degree to which a drug is cleared from the body before entering systemic circulation"""
        self.first_pass_effect = EContValSlot(["continuous_value"],"continuous_value", {"low":[0.0,.50],"medium-low":[.50,.50], "medium":[.501,.80],"medium-high":[.80,.80], "high":[.801,1]})

        """the proportion of an active ingredient's dose that reaches systemic circulation"""
        self.bioavailability = EMultiContValSlot(["continuous_value"],["continuous_value"], {"low":[0.0,.20],"medium-low":[.20,.20], "medium":[.201,.50],"medium-high":[.50,.50], "high":[.501,1]})

        """the percentage of drug that is absorbed in the gastro-intestinal tract """
        self.fraction_absorbed = EMultiContValSlot(["continuous_value"],["continuous_value"], {"low":[0.0,.50],"medium-low":[.50,.50], "medium":[.50,.50],"medium-high":[.50,.50], "high":[.501,1]})

        """the fraction of the active ingredient's dose that is cleared by various enzymes"""
        self.fraction_cleared_by = EMultiContValSlot(self.enzymes + ["none_assigned"],["none_assigned"],{"low":[0.0,0.5],"medium-low":[0.5,0.5],"medium":[0.5,0.75],"medium-high":[0.75,0.75],"high":[0.75,1.0]})


    ## implement the __setstate__ method if the schema changes
    #def __setstate__(self, state):
       
        #         if 'drug_of_concern' in state:
        #             del(state['drug_of_concern'])

    
        #if 'active_ingredient' not in state:
            #self.active_ingredient = Slot(["True","False","none_assigned"],"True")
        #if 'minimum_therapeutic_dose' not in state:
        #    self.minimum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)
        #if 'minimum_therapeutic_dose_is_at_least' not in state:
        #    self.minimum_therapeutic_dose_is_at_least =  EMultiContValSlot(["continuous_value"],["continuous_value"], None)

        #self.__dict__.update(state)
        
         
       
        
    def makeInstance(self):
        d = Drug(self._name)
        ##print "Making instance of Drug: " + d._name
        return d

