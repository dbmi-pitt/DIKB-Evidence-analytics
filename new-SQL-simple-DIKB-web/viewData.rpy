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
## File:          viewData.rpy


import os,sys, string, re
from time import time, strftime, localtime

from twisted.web import resource

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
ident = "".join(["viewData.rpy cgi:", timestamp])
        
ev = EvidenceBase("evidence",ident)
ev.unpickleKB("var/evidence-base/ev.pickle")

## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s ' % str(version)

    
def create_page( aft=None, fore=None, top=None, home=None ):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'View data in  the Drug Interaction Knowledge Base'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home
    
    # doc.append(P(),"<h2><b>Assertions in the Evidence Base</b></h2>",BR())
    l = []
    for ent, assertion in ev.objects.iteritems():
        (head, tail) = ent,assertion
        l.append((head, tail))
    l.sort()
    
    for ent, assertion in l:
        obj_slot_val = [assertion.object,assertion.slot,assertion.value]
        doc.append('''<a name="''', "_".join(obj_slot_val),'''"></a>''')
        doc.append("<b>Assertion:", " ".join(obj_slot_val), "</b>",BR())
        doc.append("current evidence_rating: ", assertion.evidence_rating, BR())
        doc.append("Assert by default?: ", str(assertion.assert_by_default), BR())
        state = ev.objects["_".join(obj_slot_val)].ready_for_classification
        doc.append(readyToClassifyForm("_".join(obj_slot_val), state))
           
        #table of evidence
        t = assertionTableView(assertion)
        doc.append(t,HR(),BR())

    doc.append("<b>You can go to DIKB the home page here:</b>  ")
    doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))
    doc.append(P())

    return doc.__str__()



class Resource(resource.Resource):
    """class that processes the form, from the twisted lib"""
    def __init__(self): 
        self.summary = ""
        self.error = "no results for this query: "
     
    def render(self, request):

        if len(request.args) != 0:
            if request.args.has_key('obj_slot_val'):
                obj_slot_val = request.args['obj_slot_val'][0]
                state = request.args['state'][0]
                old_state = ev.objects[obj_slot_val].ready_for_classification
                if state != old_state:
                    s = True
                    if state == "False":
                        s = False
                    ev.objects[obj_slot_val].ready_for_classification = s
                    warning("".join(["Changing ready_for_classification slot of evidence object ",
                                      obj_slot_val, " to ", state]), 3)
                    ev.pickleKB("var/evidence-base/ev.pickle")
                    
        page = create_page()
        return page

resource = Resource()
