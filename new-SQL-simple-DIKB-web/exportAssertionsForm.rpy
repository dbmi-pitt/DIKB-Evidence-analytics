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
## File:          exportAssertionsForm.rpy


import os,sys, string, re
import commands
from time import time, strftime, localtime

from twisted.web import resource

### for generating nice html pages
from HTMLcolors import *
from HTMLgen import *


from DrugKB_webpages import *
from ModelUtils import *
from DIKB import *
from DrugModel import *
from EvidenceModel import *
from ExportAssertions import *

###---------------------------VERSION INFO----------------------
version = getVersion("") ## remember that the root of the filesystem
                         ## the project base directory

timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
ident = "".join(["viewData.rpy cgi:", timestamp])
        
ev = EvidenceBase("evidence",ident)
ev.unpickleKB("var/evidence-base/ev.pickle")

dikb = DIKB("dikb",ident, ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.renotifyObservers()


## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)
    
def create_page( aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Choose Belief Criteria and Export Assertions'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    form = Form("exportAssertionsForm.rpy")
    form.append(Input(type='hidden', name='swap_belief_rules', value = True))
    form.append("Select belief criteria: An assertion is believable only if evidence for pharmacokinetic drug properties is...")
    lab0 = "from an FDA guidance letter OR at least one randomized controlled trial"
    lab1 = "from an FDA guidance letter OR a drug label OR at least one randomized controlled trial"
    lab2 = "from an FDA guidance letter OR the drug label OR at least  one randomized controlled trial OR (one or more in vitro trials in human tissue AND one or more non-randomized human trials)"
    lab3 = "an FDA guidance letter OR the drug label OR consists of at least  one randomized controlled trial OR consists of one or more in vitro trials in human tissue OR one or more non-randomized human trials"
    radio_b0 = Input(type='radio',  name='state', value='switch_0',  rlabel=lab0)
    radio_b1 = Input(type='radio',  name='state', value='switch_1',  rlabel=lab1)
    radio_b2 = Input(type='radio',  name='state', value='switch_2',  rlabel=lab2)
    radio_b3 = Input(type='radio',  name='state', value='switch_3', rlabel=lab3)
    form.append(BR(),radio_b0, BR(),BR(),radio_b1,BR(),BR(),radio_b2,BR(),BR(),radio_b3,BR(),BR())

    form.append(Input(type='submit', name="export", value='Assess and Export Assertions'))
    form.append(Input(type='submit', name="export", value='Re-assess Assertions'))

    form.submit = Input(type='submit', name="export", value='Reset all assertions')




    doc.append(form)

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
            if request.args.has_key('swap_belief_rules'): 
                script_name = request.args['state'][0] ## swaps the rules for accepted belief 
                err = commands.getstatusoutput("".join(['cd data/ && ./', script_name]))
                error(err[1],0)

                if  request.args['export'][0] == 'Reset all assertions':
                    reset_evidence_rating(ev,dikb)
                    ev.pickleKB("var/evidence-base/ev.pickle")

                    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
                    doc.title = doctitle
                    doc.subtitle = 'Reset Evidence Base'
                    doc.append("All assertion rankings reset, all assertions in the evidence base are unclassified.",BR())
                    doc.append("<b>You can go to DIKB the home page here:</b>  ")
                    doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))
                    doc.append(P())

                    return doc.__str__()
                    
                else:
                    if request.args['export'][0] == 'Assess and Export Assertions':
                    ## export all assertions
                        reset_evidence_rating(ev,dikb)
                        exportAssertions(dikb, ev, "data/assertions.lisp", "False")
                        ev.pickleKB("var/evidence-base/ev.pickle")
                        
                    elif request.args['export'][0] == 'Re-assess Assertions':
                    ## export only the assertions whose belief status has changed
                        exportAssertions(dikb, ev, "data/assertions.lisp", "True")
                        ev.pickleKB("var/evidence-base/ev.pickle")

                    ##load assertions and print to page
                    try:
                        f = open("data/assertions.lisp")
                    except IOError, err:
                        error(" ".join(["Could not open assertions file containing drug generic names:",os.getcwd(),"data/assertions.lisp",
                                        "Please make sure this file exists. Returning None"]), 0)
                        return None
                
                    txt = f.read()
                    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
                    doc.title = doctitle
                    doc.subtitle = 'Assertions from Evidence Base'

                    doc.append("<pre>",txt,"</pre>")

                    doc.append("<b>You can go to DIKB the home page here:</b>  ")
                    doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))
                    doc.append(P())

                    return doc.__str__()
                
        page = create_page()
        return page

resource = Resource()
