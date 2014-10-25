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
## File:          editAssertions.rpy

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
ident = "".join(["editAssertions.rpy cgi:", timestamp])

#ev = EvidenceBase("evidence",ident)
#ev.unpickleKB("var/evidence-base/ev.pickle")

#dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
#dikb.unpickleKB("var/DIKB/dikb.pickle")


## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)


    
def create_form(obj, slot, value_lst, aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Add the value for an assertion in the Drug Interaction Knowledge Base'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    form = selectObjectSlotForm('addAssumptions.rpy', obj, slot, value_lst)
    
    
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
            page = "This form should only be accesed from within the DIKB site, please return to the home page"
        else:
            if not request.args.has_key('object') or not request.args.has_key('slot'):
                page = "object and slot variables not recieved. Please use your browser's 'Back' button to enter this item."
                return page
            slot = request.args['slot'][0]
            obj = request.args['object'][0]
            obj_type = request.args['type'][0]

            """find out the valid entries for this slot"""
            values = None

            """gg - Instead of trying to figure out the object type from its name, let's just pass in the type from the form.
            I'm assuming here that pceuty_entity and pharmaceutical_preparation weren't really implemented on the site yet.  However
            if these can come from one of the current menus (drugs, metabolites, enzymes) we can find another way to do this."""
            
#            if type(dikb.objects[obj]) == Drug:
            if obj_type == 'drug':
                if Drug('simvastatin').__dict__.has_key(slot):
                    values = Drug('simvastatin').__dict__[slot].range
#            elif type(dikb.objects[obj]) == Metabolite:
            elif obj_type == 'metabolite':
                if Metabolite('1-Hydroxymidazolam').__dict__.has_key(slot):
                    values = Metabolite('1-Hydroxymidazolam').__dict__[slot].range
#            elif type(dikb.objects[obj]) == Enzyme:
            elif obj_type == 'enzyme':
                if Enzyme('cyp3a4').__dict__.has_key(slot):
                    values = Enzyme('cyp3a4').__dict__[slot].range
#            elif type(dikb.objects[obj]) == Pceut_Entity:
            elif obj_type == 'pceut_entity':
                if Pceut_Entity().__dict__.has_key(slot):
                    values = Pceut_Entity().__dict__[slot].range
#            elif type(dikb.objects[obj]) ==  Pharmaceutical_Preparation:
            elif obj_type == 'pharmaceutical_preparation':
                if  Pharmaceutical_Preparation("ACETAMINOPHEN 160MG TAB,CHEW", "000045046724", "N0000116401").__dict__.has_key(slot):
                    values =  Pharmaceutical_Preparation("ACETAMINOPHEN 160MG TAB,CHEW", "000045046724", "N0000116401").__dict__[slot].range

            if not values:
                page = "Could not find the range for slot '%s'; please check that this slot exists and is correctly initialized using the python interface to the DIKB"
                return page
                 
            values.sort()
            page = create_form(obj, slot, values)

        return page

resource = Resource()

