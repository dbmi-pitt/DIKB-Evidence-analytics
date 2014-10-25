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
## File:          addAssumptions.rpy

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


#ev = EvidenceBase("evidence",ident)
#ev.unpickleKB("var/evidence-base/ev.pickle")


def create_form(obj, slot, value, assumpt_keys, assumpt_picks, cont, args, aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Add assumptions that must be believed for this evidence to be applied to this assertion (for or against)'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    if cont:
        assumpt_picks = filter(lambda x: x != "", assumpt_picks)
        if assumpt_picks == []:
            doc.append("You entered <b>no assumptions</b> as necessary for this evidence item to be credible<br>")
        else:
            doc.append("You entered the following assumptions as necessary for this evidence item to be credible:<br>")
            doc.append("<br>".join(["".join(['<tt>', a, '</tt>']) for a in assumpt_picks]))
            doc.append("<br><br>")
            
        doc.append("Push submit to continue and enter evidence data or use your browser's 'Back' button to change assumptions ")
        form = Form('addEvidence.rpy')
        form.submit = Input(type='submit', name="add-assumptions", value='Continue')
        for k,v in args.iteritems():
            if k == 'assumption_picks':
                form.append(Input(type='hidden', name=k, value=",".join(assumpt_picks)))
            else:
                form.append(Input(type='hidden', name=k, value=v[0]))

        doc.append(form)
        doc.append(P())
        return doc.__str__()


    url = 'addAssumptions.rpy'
    form = addAssumptionsForm(url, obj, slot, value, assumpt_keys, assumpt_picks)
    for k,v in args.iteritems():
        if k == 'assert-by-default':
            form.append(Input(type='hidden', name=k, value=v[0]))
  
    doc.append(form)
    doc.append(P())
    
    return doc.__str__()



class Resource(resource.Resource):
    """class that processes the form, from the twisted lib"""
    def __init__(self): 
        self.summary = ""
        self.error = "no results for this query: "
     
    def render(self, request):
        args = ['slot','object', 'value', 'new_assumption', 'assumption_picks', "add-assumptions"]

        for arg in args:
            if not request.args.has_key(arg):
                page = " variable: " + arg + " not recieved, Please use your browser's 'Back' button to enter this item."
                return page
            
        slot = request.args['slot'][0]
        obj = request.args['object'][0]
        value = request.args['value'][0]
        n_assumpt = request.args['new_assumption'][0]
        assumpt_picks = request.args['assumption_picks'][0].split(",")

        """gg - Get all assertions that do not have "continuous value" in value field"""
        assumpt_keys = session.query(AssertionTable._name).filter(AssertionTable.value!="continuous_value").all()
#        assumpt_keys = ev.getQualitativeAssertionKeys()

        err = "".join(["Data passed in: ", n_assumpt, request.args['assumption_picks'][0]])
        t_log.msg(err)

        if n_assumpt in ["", None] or request.args['add-assumptions'][0] == 'No assumptions needed':
            page = create_form(obj, slot, value, assumpt_keys, assumpt_picks, True, request.args)
        else:
            if n_assumpt not in ["ignore"] + assumpt_picks:
                assumpt_picks.append(n_assumpt)
            page = create_form(obj, slot, value, assumpt_keys, assumpt_picks, False, request.args)
            
        return page

session = load_session()
resource = Resource()

