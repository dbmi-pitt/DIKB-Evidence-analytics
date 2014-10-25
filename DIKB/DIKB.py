## DIKB.py
##
## Classes and methods to support the evidence and knowledge bases of the DIKB
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
## File:          DIKB.py

import os,sys, string, random, commands
#import cPickle
import pickle

from Portalocker import lock, unlock, LOCK_EX, LOCK_SH, LOCK_NB

from Observer import *

from ModelUtils import * 
from EvidenceModel import ContValAssertion

from Defines import *

"""The Drug Interaction Knowledge Base (DIKB) stores the objects used
   for reasoning about metabolic drug interactions. The EvidenceBase
   stores assertions and their associated evidence.  These both should
   be a singletons but this is not yet implemented.

   Conceptually, all evidence slots (e.g. ESLot and EMultiSlot)
   belonging to objects will be asociated with zero or more
   Assertions. For example, the substrate slot of a drug object can
   posses an assertion for each of the enzymes that it is a substrate
   of. All Assertions are stored in an EvidenceBase object rather than
   the instance of the object(s) they are associated with. This design
   was chosen to decouple evidence about object properties, such as
   drug-enzyme inhibition or protien polymorphism, and protiens from
   instantiation of the objects themselves. An object 'Frame' can add
   or ignore any assertions in any the EvidenceBase associated with
   its type. For example, if a user did not want to include assertions
   about first-pass metabolism, it could ignore them by removing that
   slot from the drug object's Frame prototype. However, for some
   purposes, first-pass is very important so any assertions about drug
   first-pass should remain in the evidence base.

   Each Assertion can have evidence for and against
   it. \"categorical\" slots, such as a drug's generic name, are not
   associated any Assertion types. The EvidenceBase manages
   Assertions in it's 'object' dictionary.  Changes are made through
   the add_, modify_, delete, and replace, methods. The evidence base
   fills the role of an observable in the Observer pattern (Gamma
   1992). It notifies its observers each time an Assertion is added,
   deleted, replaced, or modified.

   There is pattern of usage that should be followed to re-associate
   assertions with the objects they are related to:
   ev = EvidenceBase('<some name>','<some identifier>')
   dikb = DIKB('<some name>','<some identifier>', ev) #NOTE the EvidenceBase is passed here

   # Reinitialize the DBs
   dikb.unpickleKB('../var/DIKB/dikb.pickle')
   ev.unpickleKB('../var/evidence-base/ev.pickle')
   ev.renotifyObservers() 


   <make changes to the evidence base and/or DIKB
   
   # Save changes
   dikb.pickleKB('../var/DIKB/dikb.pickle')
   ev.pickleKB('../var/evidence-base/ev.pickle')
             
   It is expected that an inference engine will assess and asign a
   'evidence_rating' for slots that are non 'categorical'. Also, the
   'magnitude_estimator' slot of an Assertion should be assigned to a
   slot-specific method for estimating a clinically relevant magnitude of effect
   of effect to be assigned to the assertions's 'magnitude' slot.
"""


class KB(Frame):
    """A generic knowledge-base that adds and returns objects and is
    capable of serializing the objects it contains"""
    def __init__(self, name = "KB", owner_id = ""):
        self._name = name
        """A unique identifier for the object that is managing this KB"""
        self._owner_id = owner_id
        """objects are {string:cass instance} pairs"""
        self.objects = {}

    
    def putObject(self, obj):
        if not obj.__dict__.has_key("_name"):
            warning("Cannot insert this object into the DIKB, it must be a child of the class Frame!", 1)
            return None
        
        if self.objects.has_key(obj._name):
            warning("Cannot insert this object into the DIKB, an object with the same _name slot exists!", 1)
            return None
        else:
            self.objects[obj._name] = obj

    def getObject(self, obj_name):
        if not type(obj_name) == type('str'):
            warning("Please pass the string name of the object you are requesting.", 1)
            return None
        
        if self.objects.has_key(obj_name):
            return self.objects[obj_name]
        else:
            warning("Could not find object ", obj_name, "are you sure that this is the _name attribute of the object?", 1)
            return None

    def pickleKB(self, path_to_file):
        log("".join(["Web instance id: ", self._owner_id, " writing KB to file: ", path_to_file]))
        ## test for and backup what is already there
        exist = True
        try:
            v = open(path_to_file, 'r')
        except IOError, err:
            warning (" ".join(["can't open :",path_to_file]), 1)
            exist = False

        if exist == True:
            v.close()
            r = random.randrange(1000,2000,1)
            cmd = "".join(['mv ', path_to_file, ' ', path_to_file, '_backup_', str(r)])
            er = commands.getstatusoutput(cmd)


        outF = open(path_to_file, 'w')

        log("".join(["Web instance id: ", self._owner_id," locking: ", path_to_file]))
        lock(outF, LOCK_EX)
        
        ## update to cPickle when Python 2.6 comes out, see http://mail.python.org/pipermail/python-list/2009-January/694992.html
        #p = cPickle.Pickler(outF)
        #p.dump(self.objects)
        p = pickle.Pickler(outF)
        p.dump(self.objects)
        
        outF.close()
        log("".join(["Web instance id: ", self._owner_id, " Done: ", path_to_file]))


    def unpickleKB(self, path_to_file):
        log("".join(["Web instance id: ", self._owner_id, " locking  KB file to open: ", path_to_file]))
        try:
            outF = open(path_to_file, 'r')
        except IOError, err:
            warning (" ".join(["Web instance id: ", self._owner_id, "can't open :",path_to_file]), 1)
            log (" ".join(["Web instance id: ", self._owner_id, "can't open :", path_to_file]))
            return None

        lock(outF, LOCK_EX)
        #self.objects = cPickle.load(outF)
        p = pickle.Unpickler(outF)
        self.objects = p.load()
        outF.close()
        log("".join(["Web instance id: ", self._owner_id, "Done loading: ", path_to_file]))
        return True


        
    def deepCopy(self, old_kb, new_kb):
        for ent, val in old_kb.objects.iteritems():
            """make a new class of the val type but with the current class prototype"""
            new_obj = val.copy(val)
            ##print new_obj.__str__()
            new_kb.putObject(new_obj)

        print new_kb.objects
            
        return new_kb
    
        
class DIKB(KB):
    """A DIKB must be associated with an EvidenceBase instance. It registers its objects as obervers of
    its associated evidence base"""
    def __init__(self, name = "DIKB", owner_id = "", evidence_base = None):
        KB.__init__(self, name, owner_id)

        self.evidence_base = None
        
        if evidence_base == None:
            warning("".join(["Third paramater not pointing to an EvidenceBase. Please set self.ev_base equal to a valid EvidenceBase instance"]),1 )
            return None
        elif type(evidence_base) != EvidenceBase:
            warning("".join("Third paramater must be a valid EvidenceBase type. Please set self.ev_base equal to a valid evidence base"), 1)
            return None
        else:
            self.ev_base = evidence_base

    def unpickleKB(self, path_to_file):
        """load in KB from file and subscribe each object as observer to this KBs evidence base"""
        if KB.unpickleKB(self,path_to_file) != None:
            self.registerObservers()
            
    def registerObservers(self):
        for ent, val in self.objects.iteritems():
                self.objects[ent].subscribeToObservable(self.ev_base)

    def putObject(self, obj):
        """subscribe object to evidence base, then enter into database"""
        obj.subscribeToObservable(self.ev_base)
        KB.putObject(self,obj)

    

class EvidenceBase(KB, Observable):
    """A collection of  assertions and associated evidence.
    Assertions are stored in self.objects as {string:list} pairs indexed
    by the concatenated name and slot of the objects that
    they are associated with. Each entry is the name of the object and the associated
    assertions. For example: {'simvastatin_prodrug':[assertion1,assertion2]}
    """
    max_id = 0

    def __init__(self, name = "EB", owner_id = ""):
        Observable.__init__(self)
        
        KB.__init__(self, name, owner_id)

    def pickleKB(self, path_to_file):
        f = open('./data/evidence-base-max-id', 'w')
        f.write(str(self.max_id) + '\n')
        f.close()

        KB.pickleKB(self, path_to_file)

    def unpickleKB(self, path_to_file):
        f = open('./data/evidence-base-max-id', 'r')
        if not f:
            print "Unable to open the file containing the current max id for assertions '%s'" % './data/evidence-base-max-id'
            sys.exit(1)
        v  =  int(f.readline().split()[0])
        self.max_id = int(v)
        f.close()

        if KB.unpickleKB(self,path_to_file) != None:
            self.renotifyObservers()
      


    def getQualitativeAssertionKeys(self):
        """ return a list of the non-continuous valued assertions in the evidence base """
        keys = []
        for k,v in self.objects.iteritems():
            if not type(v) in ([type(ContValAssertion())] + ContValAssertion().__class__.__subclasses__()):
                keys.append(k)

        return keys
                
    def addAssertion(self, a):
        """add an assertion class instance to the set of assertions and notify observers"""
        key = a.object + '_' + a.slot + '_' + a.value
        if self.objects.has_key(key):
            self.modifyAssertion(a)
        else:
            self.max_id += 1
            a._id = "assertion_" + str(self.max_id)
                    
            self.objects[key] = a

        """Notify observers of the new assertion"""
        self.notifyObservers(ADD_ASSERTION, a)
        return True

    def modifyAssertion(self, a):
        key = a.object + '_' + a.slot + '_' + a.value
        if self.objects.has_key(key):
            self.objects[key].evidence_for = self.objects[key].evidence_for + a.evidence_for
            self.objects[key].evidence_against = self.objects[key].evidence_against + a.evidence_against

            self.notifyObservers(MODIFY_ASSERTION, a)
            
            return True
        else:
            warning("".join(["modifyAssertion: Could not find key in evidence base: ",
                             key]), 1)
        return False

    def replaceAssertion(self, old_a, new_a):
        key = old_a.object + '_' + old_a.slot + '_' + old_a.value
        if self.objects.has_key(key):
            self.objects[key] = new_a

            """Notify observers of the modified assertion"""
            self.notifyObservers(REPLACE_ASSERTION, new_a)
            return True
        else:
            warning("".join(["replaceAssertion: Could not find assertion you are trying to replace in evidence base",
                             old_a._name]), 1)
        return False

    def deleteAssertion(self, a):
        key = a.object + '_' + a.slot + '_' + a.value
        if self.objects.has_key(key):
            del(self.objects[key])
                    
            """Notify observers of the deleted assertion"""
            self.notifyObservers(DELETE_ASSERTION, a)
            return True
                        
        warning("".join(["deleteAssertion: Could not find key in evidence base: ",
                         key]), 1)
        return False

             
    def renotifyObservers(self):
        """WARNING: this is a destructive call!. Call the call-back of
        registered observers with the Assertion instances in this
        EvidenceBase.  This forces initialization of these objects and
        replacement and re-initialization if there are assertions
        matching this one in the observers list
        """
        for id, assertion in self.objects.iteritems():
            """I violate the accepted use of the observer pattern here
               to force a replacement of old assertion values; the
               desired side effect is that any matching assertion be
               updated to the new versions.
            """
            self.notifyObservers(DELETE_ASSERTION, assertion)
            self.notifyObservers(RENOTIFY, assertion)

    
    def buildEvidenceAssrtDicts(self):
        """ build two dictionaries containing the assertions each evidence item is linked to

        This method builds the self.ev_for_d and self.ev_against_d
        dictionaries; self.ev_for_d links each evidence item's
        doc_pointer to the set of assertion is is linked to as
        'evidence_for', self.ev_against_d links each evidence item's
        doc_pointer to the set of assertion is is linked to as
        'evidence_against
        """
        self.ev_for_d = {}
        self.ev_against_d = {}
        for k, obj in self.objects.iteritems():
            for ev_o in obj.evidence_for:
                if not self.ev_for_d.has_key(ev_o.doc_pointer):
                    self.ev_for_d[ev_o.doc_pointer] = []
                self.ev_for_d[ev_o.doc_pointer].append(k)

            for ev_o in obj.evidence_against:
                if not self.ev_against_d.has_key(ev_o.doc_pointer):
                    self.ev_against_d[ev_o.doc_pointer] = []

                self.ev_against_d[ev_o.doc_pointer].append(k)

