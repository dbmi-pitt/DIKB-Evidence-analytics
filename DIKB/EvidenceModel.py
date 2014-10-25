## EvidenceModel.py
##
## Classes and methods used to represent assertions and evidence, see DIBK.py for a description
##
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
## File:          EvidenceModel.py

import os,sys, string, random, re

## for time stamp
from time import time, strftime, localtime

## for set functionality, used to combine evidence types
from sets import Set

## for Frame system definitions
from ModelUtils import *

## get a list of rejected evidence items
try:
    f = open("data/rejected-evidence")
except IOError, err:
    warning(" ".join(["Could not open file containing rejected-evidence:",os.getcwd(),"data/rejected-evidence", 
                              "Please make sure this file exists. Exiting"]), 1)
    exit(1)
    
RJCTD_EV = {}
ln = f.readline()
while ln: 
    t = ln.split("|")
    if len(t) > 1:
        if not RJCTD_EV.has_key(t[0]):
            RJCTD_EV[t[0]] = []

        RJCTD_EV[t[0]].append((t[1],t[2]))

    ln = f.readline()
    
def assessBelief(ev_types, ranking_categories, believable):
    """Check whether any of the evidence types belonging within a list of evidence types are in the set of types that meet the current
    belief criteria.

    @param ev_types - a list of strings where each item specifies an evidence type
    @param ranking_categories -a dictionary of categories to which evidence types are assigned.
        the value of each dictionary entry being a Set of ev types - ranking_categories
    @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
        for this assertion is a superset of any of the believable combinations
        than this assertion is believable.
    @returns: (<boolean>,<list of ints>) - The bool is true if the evidence meets the current belief criteria, false otherwise.
                                           The list of ints holds the indices of ev_types that met belief criteria 
    """
    member_of = [] # list holding all ranking categories that the evidence types belong to
    e_r_mp = [] # same as member of but keeps ranking categories
                # grouped so as to enable mapping the evidence items
                # to their respective ranking categories
    for ev in ev_types:
        e_r_mp.append([])
        ev_s = Set([ev])
        for rank, ev_t in ranking_categories.iteritems():
            """intesection test, is this an ev type in the set of ev types belonging to
            category rank? """
            if len(ev_s & ev_t) > 0: 
                member_of.append(rank)
                e_r_mp[-1].append(rank)

    """create a sorted string of all ranking categories this assertion's evidence belongs to"""
    member_of.sort()
    member_ptrn = " ".join(member_of)

    bc_met = [] # holds the indices to the first set of evidence that meet belief criteria
    belief = False
    """Rules are really regular expressions; we see if the belief
    criteria are met by performing a reg expression search on each
    rule until the belief pattern is found or there are no more rules

    It is critical that that multiple ranking categories can be joined
    by conjunction or disjunction.  The code does this by:

      * creating a list of all ranking categories any evidence item maps to

      * alphabetizing the set of ranking categories 

      * doing a reg exp search applying each rule for belief criteria
        to the sorted list of ranking categories

      * iterating throuch the list of evidence types to find the first
        set of evidence items that match all of the ranking categories
        in the match object

    The user must write conjunctive ranking categories in alphabetical
    order; disjunctive ranking categories are written as seperate
    regular expressions within the list of regular expressions that
    define a level of evidence 
    """
    for rule in believable:
        reg = re.compile(rule)
        m = reg.search(member_ptrn)
        if m:
            belief = True

            # identify the indices of evidence items used to meet meet belief criteria
            grps_l = filter(lambda x: x != "", m.groups())
            r_l = []
            for r_s in grps_l:
                r_l += (r_s.split(' '))

            warning("r_l: %s" % str(r_l), 2)
            grps = Set(r_l)       
            for i in range(0,len(ev_types)):
                r_cs = Set(e_r_mp[i]) # the ranking categories this evidence type maps to
                warning("r_cs: %s" % str(e_r_mp[i]),2)
                """intersection test"""
                if len(r_cs & grps) > 0: 
                    bc_met.append(i)
                    grps = grps - r_cs # we do this so that other evidence types that map to
                                       # the same ranking categories as were just used are not
                                       # also identified as used to satisfy belief criteria
            break
        
    warning(' '.join(["EvidenceModel::assessBelief: Testing belief, values are -\n",
                      "ev_types: ", str(ev_types), "\n",
                      "member_of: ", str(member_of), "\n",
                      "member_ptrn: ", str(member_ptrn), "\n",
                      "ranking_categories: ", str(ranking_categories), "\n",
                      "believable: ", str(believable), "\n",
                      "belief (returning): ",str(belief), "\n",
                      "indices of evidence items that meet belief criteria: ", str(bc_met), "\n",
                      "e_r_mp: ", str(e_r_mp)]), 2)


    return (belief, bc_met)
            

def rejectedEvidenceCheck(ev):
    """test if an evidence item has ever been rejected"""
    if ev.doc_pointer in RJCTD_EV.keys():
        return True

    return False

def circularEvidenceCheck(e1, a1, ev_base):
    """test if addition of evidence item to the evidence-base would create a circular line of evidence support
       A consequence of incorporating assumptions into an evidence-based knowledge-representation
       is that it becomes possible to identify circular lines of evidence support. For example,
       imagine some evidence item, E1, is being used as support for
       the assertion  (diltiazem inhibits CYP3A4) and that this use of E1 depends on the validity of
       (simvastatin primary-clearance-enzyme CYP3A4). Imagine also that the same evidence item, E1, is being
       used to support (simvastatin primary-clearance-enzyme CYP3A4) and that this use of E1 depends on the
       validity of (diltiazem inhibits CYP3A4). This creates a circular line of evidence support: 
            1. the use of E1 to support (diltiazem inhibits CYP3A4) depends on
            the validity of (simvastatin primary-clearance-enzyme CYP3A4)

            2. the validity of (simvastatin primary-clearance-enzyme CYP3A4) depends in part or whole on E1

            3. the use of E1 to support (simvastatin primary-clearance-enzyme CYP3A4) depends on the
            validity of (diltiazem inhibits CYP3A4)

            4. E1 is supporting (diltiazem inhibits CYP3A4)

       A formal definition of a circular line of evidence support is as follows:

              Let E1 be an item of evidence that is being considered
              as evidence for or against some assertion A1. Assume
              that the use of E1 as evidence for or against A1 is
              contingent on the validity of one or more other
              assertions in the set A1_L = [as_1, as_2, ..., as_n].
              If, E1 is currently being used as evidence for or
              against some assertion, as_i, in A1_l and the use of E1
              to support or refute as_i depends on the assumption A1
              then, the addition of E1 to support A1 would create a
              circular line of evidence support.

              1. the use of E1 to support or refute A1 depends on
              the validity of as_i

              2. the validity of as_i depends in part or whole on E1

              3. the use of E1 to support or refute as_i depends on the
              validity of A1

              4. If E1 supports or refutes A1 the evidence support
                 will be circular

       @param e1:Evidence instance - the item of evidence for which
              this circularity check is being ran

       @param a1:string - the string name of the assertion that this
              evidence item ('e1') is being used to support or refute

       @param ev_base:EvidenceBase instance

       @returns: (None, <string>) - if there is an exception; the
                 error that triggered the execption is written to stderr and is
                 placed in string

                 (True, <string>) - if the addition of 'e1' will cause a circular
                 line of evidence support to exist in the ev_base; string describes the
                 circularity

                 (False, None) - if the addition of 'e1' will *not* cause a circular
                 line of evidence support to exist in the ev_base
              
    """
    asrts = ev_base.objects.keys()
    try:
        a1_l = e1.assumptions
    except AttributeError, err:
        str_e = "Evidence instance has no slot 'assumptions' so cannot perform circularity check. Returning None"
        warning(str_e, 1)
        return (None, str_e)

    # the use of e1 to support or refute a1 depends on the validity of as_i
    for a in a1_l.value:
        try:
            as_i = ev_base.objects[a]
        except AttributeError, err:
            str_e = "Evidence item %s listed '%s' as an assumption but there is no such assertion in the evidence-base. No circularity check can be performed. Returning None" % (ev.doc_pointer, asmpt)
            warning(str_e , 1)
            return (None, str_e)

        # does the validity of as_i depends in part or whole on e1?
        for e in as_i.evidence_for:
            if e1.doc_pointer == e.doc_pointer:
                # yes, the validity of as_i depends in part or
                # whole on e1...Does the use of e1 to support as_i
                # depends on the validity of a1?
                try:
                    e_a_l = e.assumptions
                except AttributeError, err:
                    str_e = "Evidence instance %s has no slot 'assumptions' so cannot perform circularity check. Returning None"  % (e._name)
                    warning(str_e, 1)
                    return (None, str_e)
                
                for e_asmpt in e.assumptions.value:
                    if e_asmpt == a1:
                        # yes, the use of e1 to support as_i
                        # depends on the validity of a1, this is
                        # circular
                        s = "The addition of this evidence would cause a circular line of evidence as follows:\n \
1. the use of %s to support or refute %s depends on\n \
the validity of %s\n \
\n \
2. the validity of %s depends in part or whole on %s\n \
\n \
3. the use of %s to support or refute %s depends on the\n \
validity of %s\n \
\n \
4. If %s is used to  support or refute %s, the evidence support\n \
will be circular " % (e1.doc_pointer, a1, as_i._name, as_i._name, e1.doc_pointer, e1.doc_pointer, as_i._name, a1, e1.doc_pointer, a1)
                        return (True, s)

        # does the validity of as_i depends in part or whole on e1?    
        for e in as_i.evidence_against:
            if e1.doc_pointer == e.doc_pointer:
                # yes, the validity of as_i depends in part or
                # whole on e1...Does the use of e1 to refute as_i
                # depends on the validity of a1?
                try:
                    e_a_l = e.assumptions
                except AttributeError, err:
                    str_e = "Evidence instance %s has no slot 'assumptions' so cannot perform circularity check. Returning None"  % (e._name)
                    warning(str_e, 1)
                    return (None, str_e)
                for e_asmpt in e.assumptions.value:
                    if e_asmpt == a1:
                        # yes, the use of e1 to refure as_i
                        # depends on the validity of a1, this is
                        # circular
                        s = "The addition of this evidence would cause a circular line of evidence as follows:\n \
1. the use of %s to support or refute %s depends on\n \
the validity of %s\n \
\n \
2. the validity of %s depends in part or whole on %s\n \
\n \
3. the use of %s to support or refute %s depends on the\n \
validity of %s\n \
\n \
4. If %s is used to  support or refute %s, the evidence support\n \
will be circular " % (e1.doc_pointer, a1, as_i._name, as_i._name, e1.doc_pointer, e1.doc_pointer, as_i._name, a1, e1.doc_pointer, a1)
                        return (True, s)
                    
    return (False, None)

    
class Evidence(Frame):
    """
    A single unit of evidence for an assertion

    @param ev: an instance of EvidenceBase    
    """
    """a unique name"""
    
    def __init__(self, ev = None):
        """make a unique identifier for this object - the doc_pointer concatenated with the _name field should be unique"""
        r = random.randrange(1000,2000,1)
        self._name = "".join(['evidence_',str(r)])
        
        """a url, pubmed id, or pointer to an identifier in the DIKB bibliographic database  """
        self.doc_pointer = ""
        """The quotation that led the person to feel this assertion was valid"""
        self.quote = ""
        "Person who entered this evidence"
        self.reviewer = Slot(reviewers, 'boycer')

        self.timestamp  = ""

        """define the acceptable types for this slot from types listed in a file on disk"""
        try:
            f = open("data/evidence-types")
        except IOError, err:
            warning(" ".join(["Could not open file containing evidence types at:",getcwd(),"data/evidence-types",
                              "Please make sure this file exists. Returning None"]), 1)
            return None
        types = f.read()
        reg = re.compile("^[_A-Za-z0-9]+",re.MULTILINE)
        all = reg.findall(types)
        all.append('none_assigned')
        evidence_types = all
        self.evidence_type = Slot(evidence_types,"none_assigned")

        """the set of assumptions that this evidence item depends on; a list of keys to assumptions in the evidence base"""
        if ev:
            self.assumptions = MultiSlot(ev.objects.keys(), [])


    def create(self, doc_p = "" , q = "", ev_type = "", revwr = "", timestamp = ""):
        self.doc_pointer = doc_p
        self.quote = q
        self.evidence_type.putEntry(ev_type)
        self.reviewer.putEntry(revwr)
        self.timestamp = timestamp

    def makeInstance(self):
        return Evidence()

class EvidenceContinousVal(Evidence):
    """Evidence class with a continuous value"""

    def __init__(self, ev = None):
        Evidence.__init__(self, ev)
        #a float value 
        self.value = None
   
    def create(self, doc_p = "" , q = "", ev_type = "", revwr = "", timestamp = "", val = None):
        Evidence.create(self, doc_p, q, ev_type, revwr, timestamp)
        self.value = val



class PKStudy(EvidenceContinousVal):
    """an evidence type for randomized controlled pharmacokinetic studies"""

    """dose in grams  of object and precipitant"""
    object_dose = 0.0
    precip_dose = 0.0
    """ the number of study participants"""
    numb_subj = 0
    
    def __init__(self, ev = None):
        EvidenceContinousVal.__init__(self, ev)

            
    def create(self, doc_p = "" , q = "", ev_type = "", revwr = "",
               timestamp = "", object_dose = None, precip_dose = None, val = None, numb_subj = None):
        """Initialize the variables of this class:

        @param doc_p - a string value pointer to the document; usually the name of a file in the evidence folder or a PubMed id
        @param q - a string specifying the results of the study in the format:
                     <description> <object>: <object drug dose in mg> po; <precipitant drug dose in mg> <'single dose' or tidx# days given>, po; change in AUC: <percent change>
                     For example: '(summary from UW DIDB)  midazolam: 15mg po; diltiazem 60 mg tidx3 d, po; change in AUC: 380'
        @param ev_type - a string representing the evidence type
        @param revwr -  the reviewer id
        @param timestamp - a string represent the timestamp of data entry
        @param object_dose - a float, the dose in g of the object drug
        @param precip dose - a float, the dose in g of the precipitant drug
        @param val - a float, the  AUC change in decimal form. For example, a 342% change = 3.42"""
        
        EvidenceContinousVal.create(self, doc_p, q, ev_type, revwr, timestamp, val)
        self.object_dose = object_dose
        self.precip_dose = precip_dose
        self.numb_subj = numb_subj

class In_vitro_inhibition_study(EvidenceContinousVal):
    """an evidence type for in vitro inhibition studies

    """
        
    def __init__(self, ev = None):
        EvidenceContinousVal.__init__(self, ev)
        self.enzyme_system = ESlot(["none_assigned" , "Human_Liver_Microsomes", "Human_Recombinant_Enzymes"],"none_assigned")

        
#     def __setstate__(self, state):
#        if 'ev_bc_cache' not in state:
#             self.ev_bc_cache = None
#        self.__dict__.update(state)
        
    def create(self, doc_p = "" , q = "", ev_type = "", revwr = "",
               timestamp = "", val = None, enzyme_system = "none_assigned"):
        """Initialize the variables of this class:

        @param doc_p - a string value pointer to the document; usually the name of a file in the evidence folder or a PubMed id
        @param q - a string specifying the results of the study 
        @param ev_type - a string representing the evidence type
        @param revwr -  the reviewer id
        @param timestamp - a string represent the timestamp of data entry
        @param val - a float, the inhibition constant, k_i (Mol/L), derived from the study
        @param enzyme_system - a string, one of 'none_assigned' ,
                               'Human_Liver_Microsomes',
                               'Human_Recombinant_Enzymes'
        """
        
        EvidenceContinousVal.create(self, doc_p, q, ev_type, revwr, timestamp, val)
        self.enzyme_system.putEntry(enzyme_system)
        

class Maximum_concentration_study(EvidenceContinousVal):
    """an evidence type for in studies that establish a drug's C_max

    """
    
    """dose in grams  of object and precipitant"""
    dose = 0.0
    """the number of participants in the study"""
    numb_subjects = 0
        
    def __init__(self, ev = None):
        EvidenceContinousVal.__init__(self, ev)

        
        
    def create(self, doc_p = "" , q = "", ev_type = "", revwr = "",
               timestamp = "", dose = None, numb_subjects = None, val = None):
        """Initialize the variables of this class:

        @param: doc_p - a string value pointer to the document; usually the name of a file in the evidence folder or a PubMed id
        @param: q - a string specifying the results of the study 
        @param: ev_type - a string representing the evidence type
        @param: revwr -  the reviewer id
        @param: timestamp - a string represent the timestamp of data entry
        @param: dose - a float, the dose of the drug in the study given in grams
        @param: numb_subjects - the number of subjects participating in the study 
        @param: val - a float, the C_max as derived from the study in Mol/L
        """
        
        EvidenceContinousVal.create(self, doc_p, q, ev_type, revwr, timestamp, val)
        self.dose = dose
        self.numb_subjects = numb_subjects


class Assertion(Frame):
    """a proported fact about an object and slot"""
    def __init__(self, obj_name = "", slot = "", val = "", ev = None):
                
        """The string identifier of the object"""
        self.object = obj_name

        """the slot name"""
        self.slot = slot
        
        """the value of the slot, make sure it is one that is allowed!"""
        self.value = val
        
        """make a unique identifier for this object"""
        self._id = "assertion_NEW"
        
        self._name = "".join([self.object,'_',self.slot,'_', self.value])

        """A slot specific method for estimating a clinically relevant magnitude of effect"""
        self.magnitude_estimator = None
        self.magnitude = None
        
        """evidence for, use Evidence Class"""
        self.evidence_for = []
        """evidence against, use Evidence Class"""
        self.evidence_against = []
        """Is this assertion ready for  classification?"""
        self.ready_for_classification = False
        """should this assertion be asserted by default? The assertion
        will be retracted if evidence-against meets belief criteria"""
        self.assert_by_default = False
        
        """calculate evidence rating"""
        self.evidence_rating = "none_assigned"

        """cache references to evidence items that were used to meet belief criteria"""
        self.ev_bc_cache = None

#     def __setstate__(self, state):
#        if 'ev_bc_cache' not in state:
#             self.ev_bc_cache = None
#        self.__dict__.update(state)
        
    def __str__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'\n',ent,":",'\t',val.__str__(),'\n'])
            if ent == "evidence_for" or ent == "evidence_against":
                for ev in val:
                    s = "".join([s,'\t\t', ev.__str__(),'\n'])

        return s

    def __html__(self):
        s = ""
        for ent, val in self.__dict__.iteritems():
            s = "".join([s,'''<br>''',ent,":", val.__str__(),'''<br>'''])
            if ent == "evidence_for" or ent == "evidence_against":
                s = s + '''<p>'''
                for ev in val:
                    s = "".join([s, ev.__html__(),'''<br>'''])
                s = s + '''</p>'''
                  
        return s

    def insertEvidence(self, for_against, evd, ev_base=None):
        """insert evidence into this assertion type

        @param for_against - a string, either 'for' or 'against' specifying whether
                          the evidence is for or against the assertion
        @param evd - either an Evidence instance or an instance of one of its subclasses

        @returns: (0, <string>) - on success; <string> will contain any warnings
                  (1, <string>) - on failure; string will contain details on the error that occured
        """
        warnings = ""

        if not ev_base:
            warnings += "EvidenceModel::insertEvidence - not checking for circular lines of evidence or rejected evidence because you did not specify an  EvidenceBase instance. "
        else:
            rslt = circularEvidenceCheck(evd, self._name, ev_base)
            if rslt[0] == None:
                err = "EvidenceModel::insertEvidence - call to EvidenceModel::circularEvidenceCheck triggered an exception; error:\n%s" % (rslt[1])
                return (1, err)
            elif rslt[0] == True:
                err = "EvidenceModel::insertEvidence - call to EvidenceModel::circularEvidenceCheck triggered the following error: \n%s" % (rslt[1])
                return (1, err)
                     
            if rejectedEvidenceCheck(evd):
                # see if this assertion is in the set of assertions
                # that this evidence cannot be used to support
                flg = False
                str_e = ""

                # create a list of all assertions in the system; it is
                # possible that there does not yet exist an assertion
                # of the type this instance belongs to so, we need to
                # add it to the list
                assrts = ev_base.objects.keys()
                if self._name not in assrts:
                    assrts.append(self._name)
                
                # there can be multiple assertions that an evidence item cannot be applied to 
                r = RJCTD_EV[evd.doc_pointer] 
                for elt in r:
                    # get all assertions with a string match to string
                    # for which this evidence is rejected.  This
                    # method will pull in all assertions that have a
                    # match with the string up to the '*' character if
                    # it exists
                    s_l = filter(lambda x: x.find(elt[0].split("*")[0]) == 0, assrts) # match must start at the beginning of the string name
                    if  self._name in s_l:
                        flg = True

                    if s_l == []:
                        s_l = [elt[0]]

                    str_e += "The evidence items pointed to by %s has been rejected for assertion(s) '%s'; explanation:\n\t%s" % (evd.doc_pointer, ",".join(s_l), elt[1])

                if flg:
                    err = "EvidenceModel::insertEvidence - call to EvidenceModel::rejectedEvidenceCheck triggered the following error:\n %s " % str_e
                    return (1, err)
                else:
                    warnings += "WARNING: \n%s" % str_e
        
        if for_against == "for":
            self.evidence_for.append(evd)
        elif for_against == "against":
            self.evidence_against.append(evd)

        return (0, warnings)

    def assessEvidence(self, ranking_categories, believable_ev_for, believable_ev_against):
        """ A method that derives an evidence assessment from the
        evidence values. This method tells its caller whether the
        evidence in this assertion's evidence_for list satisfies the
        the current belief criteria to a higher degree than the
        evidence in its evidence_against slot.

        @param ranking_categories - a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable_ev_for - a list of ranking_categories: if the the set of evidence_types in the
            evidence_for list for this assertion is a superset of any of the believable combinations
            than this assertion is believable.
        @param believable_ev_against - a list of ranking_categories: if the the set of evidence_types in the
            evidence_against list for this assertion is a superset of any of the believable combinations
            than this assertion is NOT believable.
        @returns: 'True', 'False', or 'can't decide' depending on whether
            the evidence meets the belief criteria or is undecidable
        side-effect: this assertions evidence_rating slot is given a value, one of 'assume!',
                     'retract!', or 'can't decide' depending on how its evidence evaluates
        """
        warning(' '.join(["Assertion::assessEvidence: Assessing evidence for",
                          self.object, self.slot, self.value,
                          "\nValues passed were:\nranking_categories:%s\nbelievable_ev_for:%s\nbelievable_ev_against:%s" % (str(ranking_categories), str(believable_ev_for), str(believable_ev_against))]), 2)

        # reset the cache of evidence used to establish belief criteria
        self.ev_bc_cache = None
    
        "create the set of evidence types for and against this assertion"
        ev_for = []
        for ev in self.evidence_for:
            ev_for.append(ev.evidence_type.value)
            
        (belief_for, bc_for_met) = assessBelief(ev_for, ranking_categories, believable_ev_for)
        
        ev_against = []
        for ev in self.evidence_against:
            ev_against.append(ev.evidence_type.value)

        (belief_against, bc_against_met) = assessBelief(ev_against, ranking_categories, believable_ev_against)
        warning( "Assertion::assessEvidence: belief_for: " + str(belief_for) + "\nbelief_against: " + str(belief_against) + "\n", 2)

        if self.assert_by_default:
            warning("Assertion::assessEvidence: This assertion is to be believed by default - setting belief_for to True and belief _against to False")
            belief_for = True
            belief_against = False
            self.ev_bc_cache = []
        
        if belief_for and (not belief_against):
            ## change state of assertion
            if self.evidence_rating == "none_assigned" or self.evidence_rating == "can't decide":
                self.evidence_rating = "assume!"
                warning( "returning assume!", 2)
                self.ev_bc_cache = bc_for_met
                return "assume!"
            
            elif self.evidence_rating == "assume!":
                return "pass"

            elif self.evidence_rating == "retract!":
                self.evidence_rating = "assume!"
                warning( "returning assume!", 2)
                self.ev_bc_cache = bc_for_met
                return 'assume!'
        
        elif (not belief_for) and belief_against :
            ## change state of assertion
            if self.evidence_rating == "none_assigned":
                self.evidence_rating = "retract!"
                return "pass"

            elif self.evidence_rating == "can't decide":
                self.evidence_rating = "retract!"
                return "pass"

            elif self.evidence_rating == "assume!":
                self.evidence_rating = "retract!"
                warning( "returning retract!", 2)
                self.ev_bc_cache = None
                return "retract!"

            elif self.evidence_rating == "retract!":
               return "pass"
           
        elif ((not belief_for) and (not belief_against)) or (belief_for and belief_against) :
            warning(' '.join(["Assertion::assessEvidence: Assigning 'can't decide for: ",
                              self.object, self.slot, self.value,
                              "\nValues passed were:\nranking_categories:%s\nbelievable_ev_for:%s\nbelievable_ev_against:%s" % (str(ranking_categories), str(believable_ev_for), str(believable_ev_against))]), 2)

            if (self.evidence_rating == "none_assigned") or (self.evidence_rating == "can't decide"):
                self.evidence_rating = "can't decide"
                return "pass"
            elif self.evidence_rating == "assume!":
                self.evidence_rating = "retract!"
                warning( "returning retract!", 2)
                self.ev_bc_cache = None
                return 'retract!'
            elif self.evidence_rating == "retract!":
                self.evidence_rating = "can't decide"
                return "pass"


    def makeInstance(self):
        return Assertion(self.object, self.slot, self.value)

    def assertionLst(self):
        """returns a list of strings containing a single assertion"""
        st = "".join([" '(", self.slot, " '", self.object, " '", self.value, ")"])

        return [st]

class ContValAssertion(Assertion):
    """An Assertion class that can combine the continuous values
    associated in its evidence_for slots a single, possibly discrete, value.

    This class provides a simple method for combining evidence-based
    values into their average and then discretizing them based on a
    discretization mapping. Sub-classes can over-ride any of this
    calsses methods for their own purposes
    """
    def __init__(self, obj_name = "", slot = "", val = ""):
        Assertion.__init__(self, obj_name, slot, val)
        
        ## a discrete value assigned by self.combineEvidence used only
        ## for assertions that need a discrete value as output
        self.cont_val = None
        ## the numeric value resulting from combining evidence
        self.numeric_val = None
        ## the mapping dictionary most recently used
        self.l_map = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}

    def assertionLst(self):
        """returns a list containing a single assertion if cont_val is not None, None otherwise"""
        if self.cont_val != None:
            st = "".join([" '(", self.slot, " '", self.object, " '", self.value, " '", self.cont_val, ")"])
            return [st]
        else:
            return []


    def getBelievable(self, for_against, ranking_categories, believable):
        """returns a list of evidence objects that meet the belief criteria

        @param for_against - a string that specifies which evidence list to assess
        @param ranking_categories -a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
            for this assertion is a superset of any of the believable combinations
            than this assertion is believable.
        @returns: a list of (object, int) tuples containing objects that meet the belief criteria and their indices
                  in the specified evidence list
        """
        l = []
        
        if for_against == "for":
            i = 0
            for ev in self.evidence_for:
                belief_for = assessBelief([ev.evidence_type.value], ranking_categories, believable)
                if belief_for:
                    l.append((ev, i))
                i += 1
                    
        elif for_against == "against":
            i = 0
            for ev in self.evidence_against:
                belief_against = assessBelief([ev.evidence_type.value], ranking_categories, believable)
                if belief_against:
                    l.append((ev, i))
                i += 1

        return l

    def combineEvidence(self, m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}, ranking_categories = None, believable = None):
        """finds the maximum continuous values in its evidence_for slots that meets the current belief criteria and maps it to a discrete category using a mapping of continuous value ranges to categories
        
        @param m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats. 
        @param ranking_categories -a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
            for this assertion is a superset of any of the believable combinations
            than this assertion is believable.    
        @returns: a discrete category for the maximum acceptable continuous value in the evidence_for list """
        self.l_map = m
        
        ## get the simple average
        max_v = -100000000000.0
        if ranking_categories == None or believable == None:
            error("ContValAssertion::combineEvidence - Please pass a dictionary of categories\n to which evidence types are assigned. the value of each dictionary\n entry being a Set of ev types and a list of believable combinations of\n ranking_categories for the first and second arguments of this function.")

        b = self.getBelievable("for", ranking_categories, believable)
        if len(b) > 0:
            for (ev, idx) in b:
                if ev.__dict__.has_key('value'):
                    if float(ev.value) > max_v:
                        max_v = float(ev.value)
                        self.ev_bc_cache = [idx] # store the index to evidence item used
                                                 # to determine the max
                else:
                    error(" ".join(["ContValAssertion::combineEvidence - slot:",
                                    self.value, " evidence ", ev._name,
                                    " does not have a 'value' slot!"]))
            self.numeric_val = max_v
            warning(" ".join(["ContValAssertion::combineEvidence - slot:",
                              self.value, " evidence ", ev._name,
                              "average of evidence:", str(self.numeric_val)]), 3)
            
            if not self.l_map:
                warning(" ".join(["ContValAssertion::combineEvidence - slot:",
                                  self.value, " evidence ", ev._name,
                                  "No mapping from continuous to discrete values, returning the simple average of evidence:", str(self.numeric_val)]), 3) 
                return self.numeric_val
            
            for cat,rng in self.l_map.iteritems():
                try:
                    if self.numeric_val >= rng[0] and self.numeric_val <= rng[1]:
                        self.cont_val = cat
                        warning(" ".join(["ContValAssertion::combineEvidence - slot:",
                                          self.value, " evidence ", ev._name,
                                          "discretized category:", cat]), 3)
                        return cat
                except IOError, err:
                    error(" ".join(["ContValAssertion::combineEvidence - mapping does not appear to be valid,\
                    cannot check ranges - EXITING\n",
                                      "current mapping: ", self.l_map]))

            ## error if no category assigned
            error("ContValAssertion::combineEvidence - average of evidence did\
            not fall between any ranges in mapping, could not assign value\
            - please fix mappings for slot:" + self.value + " evidence: " + ev._name)
                    
                            
        warning("ContValAssertion::combineEvidence - evidence_for list has no believable evidence items of no\
        items of type EvidenceContinousVal, Assertion: " + self._name, 0)


class Assertion_maximum_concentration(ContValAssertion):
    """a subclass of Evidence::ContValAssertion for an assertion about a drug's maximum concentration (C_max) at a specific dose.  This assertion does not use a discretization mapping and will export the largest magnitude C_max value that meets belief criteria during evidence assessment. The index of evidence item used to determine C_max will be the sole entry in the list self.ev_bc_cache"""

    
    def __init__(self, obj_name = "", slot = "", val = ""):
        ContValAssertion.__init__(self, obj_name, slot, val)

        self.l_map = None


    def assertionLst(self):
        """returns a list containing a single assertion if cont_val is not None, None otherwise"""
        if self.cont_val != None:
            st = "".join([" '(", self.slot, " '", self.object, " '", self.value, " '", str(self.numeric_val), ")"])
            return [st]
        else:
            return []


class Assertion_inhibition_constant(ContValAssertion):
    """a subclass of Evidence::ContValAssertion for the assertion that an inhibition constant is clinically relevant for a given drug and enzyme.

    If evidence meet belief criteria and all assumptions are believed this assertion writes out:
   (inhibition_constant_is_clinically_relevant ?obj ?enzyme ?inhibition-constant)"""

    def __init__(self, obj_name = "", slot = "", val = ""):
        ContValAssertion.__init__(self, obj_name, slot, val)
        self.prop_lst = []

    def assertionLst(self):
            """returns a list containing a one or more assertions representing each clinically relevant inhibition constant at a specific maximal inhibitor concentrations """
            st = []
            if len(self.prop_lst) > 0:
                for prop in self.prop_lst:                
                    st.append(prop)

            return st


    def combineEvidence(self, m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}, ranking_categories = None, believable = None):
        """finds the minimum continuous values in its evidence_for slots that meets the current belief criteria and maps it to a discrete category using a mapping of continuous value ranges to categories
        
        @param m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats. 
        @param ranking_categories -a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
            for this assertion is a superset of any of the believable combinations
            than this assertion is believable.    
        @returns: a discrete category for the minimum acceptable continuous value in the evidence_for list """
        self.l_map = m
        
        ## get the simple average
        min_v = 100000000000.0
        if ranking_categories == None or believable == None:
            error("Assertion_inhibition_constant::combineEvidence - Please pass a dictionary of categories\n to which evidence types are assigned. the value of each dictionary\n entry being a Set of ev types and a list of believable combinations of\n ranking_categories for the first and second arguments of this function.")
            
        b = self.getBelievable("for", ranking_categories, believable)
        if len(b) > 0:
            for (ev, idx) in b:
                if ev.__dict__.has_key('value'):
                    if float(ev.value) < min_v:
                        min_v = float(ev.value)
                        self.ev_bc_cache = [idx] # store the index to evidence item used
                                                 # to determine the min
                else:
                    error(" ".join(["Assertion_inhibition_constant::combineEvidence - slot:",
                                    self.value, " evidence ", ev._name,
                                    " does not have a 'value' slot!"]))
            self.numeric_val = min_v
            warning(" ".join(["Assertion_inhibition_constant::combineEvidence - slot:",
                              self.value, " evidence ", ev._name,
                              "average of evidence:", str(self.numeric_val)]), 3)
            
            if not self.l_map:
                warning(" ".join(["Assertion_inhibition_constant::combineEvidence - slot:",
                                  self.value, " evidence ", ev._name,
                                  "No mapping from continuous to discrete values, returning the simple average of evidence:", str(self.numeric_val)]), 3) 
                return self.numeric_val
            
            for cat,rng in self.l_map.iteritems():
                try:
                    if self.numeric_val >= rng[0] and self.numeric_val <= rng[1]:
                        self.cont_val = cat
                        warning(" ".join(["Assertion_inhibition_constant::combineEvidence - slot:",
                                          self.value, " evidence ", ev._name,
                                          "discretized category:", cat]), 3)
                        return cat
                except IOError, err:
                    error(" ".join(["Assertion_inhibition_constant::combineEvidence - mapping does not appear to be valid,\
                    cannot check ranges - EXITING\n",
                                      "current mapping: ", self.l_map]))

            ## error if no category assigned
            error("Assertion_inhibition_constant::combineEvidence - average of evidence did\
            not fall between any ranges in mapping, could not assign value\
            - please fix mappings for slot:" + self.value + " evidence: " + ev._name)
                    
                            
        warning("Assertion_inhibition_constant::combineEvidence - evidence_for list is empty\
        or is not of type EvidenceContinousVal, slot: " + self.value + " evidence: " + ev._name, 0)


class Assertion_IncreaseAUC(ContValAssertion):
    """a subclass of Evidence::ContValAssertion for increase_auc assertions that combines its evidence entries by merging values that map to the same discrete categories and writes out the increase_auc assertion as follows:
   (increase-auc ?precip ?obj ?precip-dose ?object-dose ?change-in-auc)"""

    def __init__(self, obj_name = "", slot = "", val = ""):
        ContValAssertion.__init__(self, obj_name, slot, val)
        
        self.prop_lst = []

    def assertionLst(self):
            """returns a list containing a single assertion if cont_val is not None, None otherwise"""
            st = []
            if len(self.prop_lst) > 0:
                for prop in self.prop_lst:                
                    st.append(prop)

            return st
        
    def combineEvidence(self, m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}, ranking_categories = None, believable = None):
        """combines the continuous values in its evidence_for that meets the current belief criteria slots into discrete
        categories using a mapping of continuous value ranges to categories.

        Checks for evidence entries that have the same
        object and precipitant dose and, if the 'value' slot for all
        these entries map to the same discrete category, an assertion
        with that category is added to self.prop_lst. If they do not
        all map to same discrete category then no assertion is made
        and an error is generated.
        
        @param m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats.
        @param ranking_categories -a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
            for this assertion is a superset of any of the believable combinations
            than this assertion is believable.    
        @returns: a discrete category that the combined values of its evidence_for entries map to """
        pass
    ## TODO: 12/11/2007 - fix this function; be sure to use self.ev_bc_cache to store indices to evidence items used to create the JTMS assertion
#         self.l_map = m

#         self.prop_lst = []

#         """a dictionary that maps evidence with the same object and
#         precipitant dose to the same list"""
#         d = {}

#         if ranking_categories == None or believable == None:
#             error(type(self) + "- Please pass a dictionary of categories\n to which evidence types are assigned. the value of each dictionary\n entry being a Set of ev types and a list of believable combinations of\n ranking_categories for the first and second arguments of this function.")
            
#         b = self.getBelievable("for", ranking_categories, believable)
#         if len(b) > 0:
#             for ev in b:
#                 if type(ev) == type(PKStudy()):
#                     key = str(ev.object_dose) + str(ev.precip_dose)
#                     if d.has_key(key):
#                         d[key].append(ev)
#                     else:
#                         d[key] = [ev]
#                 else:
#                     error(" ".join(["Assertion_IncreaseAUC::combineEvidence - evidence:",
#                                     self._name, " evidence ", ev._name,
#                                     " is not an instance of  'PKstudy' !"]))
#             for st,lst in d.iteritems():
#                 """check that value is in the same category and if so,
#                 add an assertion with the discrete value to
#                 self.prop_lst"""

#                 t = ""
#                 cnt = 0
#                 for obj in lst:
#                     for cat,rng in self.l_map.iteritems():
#                         try:
#                             if float(obj.value) >= rng[0] and float(obj.value) <= rng[1]:
#                                 if cnt > 0:
#                                     if cat != t: # cat must map to the same category or there is an error
#                                         error(" ".join(["Assertion_IncreaseAUC::combineEvidence - assertion:",
#                                                         self._name, " evidence ", obj._name,
#                                                         " ERROR - all values do not map to the same discretized categories...",
#                                                         cat, " does not map to ", t,
#                                                         "\nplease check the evidence for this assertion! EXITING"]))
                                        
#                                 t  = cat # continue with this category
#                                 cnt += 1
#                                 warning(" ".join(["Assertion_IncreaseAUC::combineEvidence - assertion:",
#                                                   self._name, " evidence ", obj._name,
#                                                   " continuing to find discretized category: ", cat]), 3)
#                                 break

#                         except IOError, err:
#                             error(" ".join(["Assertion_IncreaseAUC::combineEvidence - mapping does not appear to be valid,\
#                             cannot check ranges - EXITING\n",
#                                             "current mapping: ", self.l_map]))
#                 """all values map to the same discrete category, so make the appropriate assertion"""
#                 a = "".join([" '(", self.slot, " '", self.object, " '", self.value,
#                              " '", str(obj.object_dose), " '", str(obj.precip_dose), " '", t, ")"])
#                 self.prop_lst.append(a)
#                 warning(" ".join(["Assertion_IncreaseAUC::combineEvidence - slot:",
#                                   self.value, " evidence ", " Adding proposition: ",
#                                   a, " to self.prop_lst"]), 2)
        
#         return self.prop_lst



class Assertion_m_discrete(ContValAssertion):
    """a subclass of Evidence::ContValAssertion for assertions that combine their evidence entries by merging entries with the same discrete categories """

    def __init__(self, obj_name = "", slot = "", val = ""):
        ContValAssertion.__init__(self, obj_name, slot, val)
        
        
    def combineEvidence(self, m = {"low":[],"medium-low":[],"medium":[],"medium-high":[],"high":[]}, ranking_categories = None, believable = None):
        """combines the continuous values in its evidence_for slots that meets the current belief criteria into discrete
        categories using a mapping of continuous value ranges to categories.

        If they do not all map to same discrete category
        then no assertion is made and an error is generated.
        
        @param m - a dictionary containing a mapping of continous value ranges to discrete categories in
            the pattern category:[min,max] where min is the lower-bound
            of the range, max is the upper bound. Both min and max should be
            floats.
        @param ranking_categories -a dictionary of categories to which evidence types are assigned.
            the value of each dictionary entry being a Set of ev types - ranking_categories
        @param believable - a list of believable combinations of ranking_categories: if the the set of evidence_types
            for this assertion is a superset of any of the believable combinations
            than this assertion is believable.                
        @returns: a discrete category that the combined values of its evidence_for entries map to """

        self.l_map = m

        if ranking_categories == None or believable == None:
            error(type(self) + "- Please pass a dictionary of categories\n to which evidence types are assigned. the value of each dictionary\n entry being a Set of ev types and a list of believable combinations of\n ranking_categories for the first and second arguments of this function.")

        self.ev_bc_cache = [] # store indices to all of the evidence items that establish the discrete value for this slot
        b = self.getBelievable("for", ranking_categories, believable)
        if len(b) == 0:
            error(" ".join(["Assertion_m_discrete::combineEvidence - No evidence that meets belief criteria!!! assertion:",
                            self._name]))
        else:
            t = None
            cnt = 0
            for (obj, idx) in b:
                """check that value is in the same category and if not, generate an error"""
                self.ev_bc_cache.append(idx) 
                if not obj.__dict__.has_key('value'):
                    error(" ".join(["Assertion_m_discrete::combineEvidence - assertion:",
                                    self._name, " evidence ", obj._name,
                                    " does not have a 'value' slot!"]))
                    
                for cat,rng in self.l_map.iteritems():
                    try:
                        if float(obj.value) >= rng[0] and float(obj.value) <= rng[1]:
                            if cnt > 0:
                                if cat != t: # cat must map to the same category or there is an error
                                        error(" ".join(["Assertion_m_discrete::combineEvidence - assertion:",
                                                        self._name, " evidence ", obj._name,
                                                        " ERROR - all values do not map to the same discretized categories...",
                                                        cat, " does not map to ", t,
                                                        " ...please check the evidence for this assertion! EXITING"]))
                                        
                            t  = cat # continue with this category
                            cnt += 1
                            warning(" ".join(["Assertion_m_discrete::combineEvidence - assertion:",
                                              self._name, " evidence ", obj._name,
                                              " continuing to find discretized category: ", cat]), 3)
                            break

                    except IOError, err:
                        error(" ".join(["Assertion_m_discrete::combineEvidence - mapping does not appear to be valid,\
                        cannot check ranges - EXITING\n", "current mapping: ", self.l_map]))
                        
            if t == None:
                error("Assertion_m_discrete::combineEvidence - could not assign a discrete category to %s using this mapping,\n%s\n\
                cannot check ranges - EXITING\n" % (self._name, str(self.l_map)))
                
            """all values map to the same discrete category, so make the appropriate assertion"""
            self.cont_val = t
            warning(" ".join(["Assertion_m_discrete::combineEvidence - slot:",
                              self.value, " evidence ", obj._name,
                              "discretized category:", cat]), 3)

        return self.cont_val


class Assertion_continuous_s_val(Assertion_m_discrete):
    """ An assertion that combines evidence like Assertion_m_discrete objects but that only has one parameter

    Replaces its 'value' slot with the discrete category in 'self.cont_val' derived  by self.combine_evidence. For example, rather than export:
        (self.slot self.object self.value self.cont_val)
    it exports:
        (self.slot self.object self.cont_val)
        
    More specifically, the bioavailability of a drug only has one
    parameter, its discretized vale, so this slot handles that type of
    assertions. On the other hand, increase_auc has both a value and
    an enzyme parameter so this type is not appropriate.""" 

    def __init__(self, obj_name = "", slot = "", val = ""):
        Assertion_m_discrete.__init__(self, obj_name, slot, val)

    def assertionLst(self):
        """returns a list containing a single assertion if cont_val is not None, None otherwise"""
        if self.cont_val != None:
            st = "".join([" '(", self.slot, " '", self.object, " '", self.cont_val, ")"])
            return [st]
        else:
            return []

### scratch
