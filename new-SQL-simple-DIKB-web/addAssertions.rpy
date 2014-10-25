## -*-Mode:python-*-

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
## File:          addAssertions.rpy

import os,sys, string, pdb
from time import time, strftime, localtime

from twisted.web import resource

from mysql_tool import *

### for generating nice html pages
from HTMLcolors import *
from HTMLgen import *


from DrugKB_webpages import *
from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *

###---------------------------VERSION INFO----------------------
version = getVersion("") ## remember that the root of the filesystem
                         ## the project base directory

timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
ident = "".join(["addAssertions.rpy cgi:", timestamp])
        
#ev = EvidenceBase("evidence",ident)
#ev.unpickleKB("var/evidence-base/ev.pickle")

dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
#dikb.unpickleKB("../var/DIKB/dikb.pickle")


## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)

    

def create_form(aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Select an object and slot from Drug Interaction Knowledge Base'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    #objects = dikb.objects.keys()
    #objects.sort()

    doc.append("<b>Objects and assertions for ACTIVE INGREDIENTS:</b><br>")
    
    """gg - Get all names from Drugs table in db, add all to sorted list"""
    ooi = sorted(session.query(DrugTable._name).all())
    
    """
    # get the sub-set of active ingredients that are currently being modeled in the DIKB
    try:
        f = open("data/va-ndfrt-active-ingredients")
    except IOError, err:
        warning(" ".join(["Could not open file containing active ingredent names:",os.getcwd(),"data/va-ndfrt-active-ingredients", 
                              "Please make sure this file exists. Returning None"]), 1)
        return None
    t = f.read()
    ##TODO : make sure to split off a newline if it exists
    aingrds = t.split(",")
    d = {}
    for elt in aingrds:
        d[elt] = None
    ooi = filter(lambda x: d.has_key(x), objects)
    """

    # get the current set of slots for active ingredient objects
    d = Drug('simvastatin')
    slots = []
    for key, obj in d.__dict__.iteritems(): ##get evidence slots
        if type(obj) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__() + [type(ESlot())] +  ESlot().__class__.__subclasses__()):
            slots.append(key)
        
    slots.sort()
    """gg - Added object_type as hidden field on form, so we don't have to look it up by name 
    in editAssertions.rpy"""
    form = addAssertionsForm( ooi, slots, 'drug' )
    doc.append(form)
    doc.append(P())

    doc.append("<b>Objects and assertions for METABOLITES:</b><br>")
    '''
    # get the sub-set of metabolites that are currently being modeled in the DIKB
    try:
        f = open("data/chemicals_produced_by_metabolism")
    except IOError, err:
        warning(" ".join(["Could not open file containing metabolite names:",os.getcwd(),"data/chemicals_produced_by_metabolism", 
                          "Please make sure this file exists. Returning None"]), 1)
        return None
    t = f.read()
    ##TODO : make sure to split off a newline if it exists
    metabolites = t.split("\n")
    d = {}
    for elt in metabolites:
        d[elt] = None
    ooi = filter(lambda x: d.has_key(x), objects)
    '''

    """gg - Get all names from Metabolite table in db, add all to sorted list"""
    ooi = sorted(session.query(MetaboliteTable._name).all())
    
    # get the current set of slots for active ingredient objects
    d = Metabolite('6beta-Hydroxytestosterone')
    slots = []
    for key, obj in d.__dict__.iteritems(): ##get evidence slots
        if type(obj) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__() + [type(ESlot())] +  ESlot().__class__.__subclasses__()):
            slots.append(key)
        
    slots.sort()
    form = addAssertionsForm(ooi, slots, 'metabolite')
    doc.append(form)
    doc.append(P())

    doc.append("<b>Objects and assertions for ENZYMES:</b><br>")
    # get the sub-set of metabolites that are currently being modeled in the DIKB
    """gg - Put this code in a function in mysql_tool.py"""
    '''
    try:
        f = open("data/enzymes")
    except IOError, err:
        warning(" ".join(["Could not open file containing enzyme names:",os.getcwd(),"data/enzymes", 
                          "Please make sure this file exists. Returning None"]), 1)
        return None
    t = f.read()
    ##TODO : make sure to split off a newline if it exists
    enzymes = t.split("\n")
    '''
    '''
    d = {}
    for elt in enzymes:
        d[elt] = None
    ooi = filter(lambda x: d.has_key(x), objects)
    '''
    """gg - The dikb isn't being loaded anymore, I'm assuming all enzymes in data/enzymes were in the DIKB"""
    ooi = get_enzymes()

    # get the current set of slots for active ingredient objects
    d = Enzyme('cyp3a4')
    slots = []
    for key, obj in d.__dict__.iteritems(): ##get evidence slots
        if type(obj) in ([type(EMultiSlot())] + EMultiSlot().__class__.__subclasses__() + [type(ESlot())] +  ESlot().__class__.__subclasses__()):
            slots.append(key)
        
    slots.sort()
    form = addAssertionsForm(ooi, slots, 'enzyme')
    doc.append(form)
    doc.append(P())

    
    return doc.__str__()



class Resource(resource.Resource):
    """class that processes the form, from the twisted lib"""
    def __init__(self): 
        self.summary = ""
        self.error = "no results for this query: "
     
    def render(self, request):
        if len(request.args) == 0:
            '''no form submision yet'''
            page = create_form()
        else:
            page = "not implemeted yet"

        return page

"""gg - get a sqlalchemy session object from mysql_tool.py"""
session = load_session()
resource = Resource()
