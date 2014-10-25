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
## File:          addEvidence.rpy


import os,sys, string
from time import time, strftime, localtime

from twisted.web import resource
from twisted.python import log as t_log

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
ident = "".join(["addEvidence.rpy cgi:", timestamp])
        

## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)

"""gg - These aren't used in this script"""
#ev = EvidenceBase("evidence",ident)
#ev.unpickleKB("var/evidence-base/ev.pickle")

    
def create_form(obj, slot, value, assumpt_picks, args, aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Assign evidence to an assertion in the Drug Interaction Knowledge Base'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    url = 'confirmSave.rpy'

    if args.has_key('assert-by-default'):
        form = addEvidenceForm(url, obj, slot, value, assumpt_picks, True)
    else:
        form = addEvidenceForm(url, obj, slot, value, assumpt_picks, False)
    
    doc.append(form)
    doc.append(P())
    
    return doc.__str__()



class Resource(resource.Resource):
    """class that processes the form, from the twisted lib"""
    def __init__(self): 
        self.summary = ""
        self.error = "no results for this query: "
     
    def render(self, request):
        args = ['slot','object', 'value', 'assumption_picks']

        for arg in args:
            if not request.args.has_key(arg):
                page = " variable: " + arg + " not recieved, Please use your browser's 'Back' button to enter this item."
                return page
            
        slot = request.args['slot'][0]
        obj = request.args['object'][0]
        value = request.args['value'][0]
        assumpt_picks = request.args['assumption_picks'][0].split(",")
    
        page = create_form(obj, slot, value, assumpt_picks, request.args)
            
        return page

resource = Resource()
