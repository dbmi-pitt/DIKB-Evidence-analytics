#!/usr/bin/env python

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
## File:          createHTML.py

### script which generates web pages for the drug interaction modeling
import sys
sys.path = sys.path + ['.']
import string, re, os, time, glob

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from HTMLcolors import *
from HTMLgen import *
from DrugKB_webpages import *
from DIKB.ModelUtils  import *

from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *


version = "1.2"

timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
ident = "".join(["confirmSave.rpy cgi:", timestamp])

htmldir = './html-output'
datadir = './data'

doctitle = 'Drug Interaction Knowledge Base %s' % str(version)

LICENSE = '<BR><BR><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Drug Interaction Knowledge Base (DIKB)</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.dbmi.pitt.edu/person/richard-boyce-phd" property="cc:attributionName" rel="cc:attributionURL">Richard D. Boyce</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.'


def make_link(pointer):
    """return a pubmed url query to the pointer if it is a pmid"""
    reg = re.compile("[a-zA-Z]+")
    link_head ='''<a target="new" href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids='''
    link_tail = '''&query_hl=1"'''
    end_tag = '''>'''
    close_tag = '''</a>'''
    
    if reg.match(pointer):
        return pointer
    else:
        return "".join([link_head,pointer,link_tail,end_tag,pointer,close_tag])


### define functions for the various html pages
def createFrontPage():
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Front Page of the Drug Interaction Knowledge Base'
    try:
        f = open(os.path.join(datadir,"front-page"))
    except IOError, err:
        error("".join(["Could not find data file: ", os.path.join(datadir, "front-page")]))

    t = f.read()
    f.close()
    doc.append(t)
    doc.append(LICENSE)
    doc.write(os.path.join(htmldir,"front-page.html"))

def createAssertionPage(doc_path, subtitle, aft=None, fore=None, top=None, home=None ):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = subtitle
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    doc.append_file(doc_path)

    doc.append("<b>You can go to DIKB assertion index here:</b>  ")
    doc.append(Href(url="/dikb-evidence/index.html",text="DIKB assertion index"))
    doc.append("<br><b>You can go to DIKB the home page here:</b>  ")
    doc.append(Href(url="/dikb-evidence/front-page.html",text="DIKB Front Page"))
    doc.append(P())
    doc.append(LICENSE)
    doc.write(htmldir + "/" + subtitle + ".html")


def createEvidencePages():
    ev = load_ev_from_db(ident)

    l = []
    for ent, assertion in ev.objects.iteritems():
        (head, tail) = ent,assertion
        l.append((head, tail))
    l.sort()
    
    for ent, assertion in l:
        doc = SimpleDocument(os.path.join(datadir,'HTMLgen.rc'))
        doc.append("<b>You can go to DIKB assertion index here:</b>  ")
        doc.append(Href(url="/dikb-evidence/index.html",text="DIKB assertion index"))
        doc.append("<br><b>You can go to DIKB the home page here:</b>  ")
        doc.append(Href(url="/dikb-evidence/front-page.html",text="DIKB Front Page"))
        doc.append(P())

        obj_slot_val = [assertion.object,assertion.slot,assertion.value]
        doc.append('''<a name="''', "_".join(obj_slot_val),'''"></a>''')
        doc.append("<b>Assertion:", " ".join(obj_slot_val), "</b>",BR())
           
        #table of evidence
        t = assertionTableView(assertion)
        doc.append(t,BR())

        ## dump contents of assertion

        #doc.append("".join(["Contents of assertion:"]),BR(),assertion.__html__(),BR())

        doc.write("/tmp/html_gen")
        createAssertionPage("/tmp/html_gen", ent)

    ## create the index page
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = "Index of Assertions and Evidence"

    for ent, assertion in l:
        doc.append("".join(['''<br><a href=''', ent, ".html>", ent, "</a>"]))

    doc.append(P())                      
    doc.append("<b>You can go to the DIKB front page here:</b>  ")
    doc.append(Href(url="/dikb-evidence/front-page.html",text="DIKB Front Page"))
    doc.append(P())
    doc.append(LICENSE)

    doc.write(htmldir + "/" + "index.html")        

def summarizeEvidence():
    ev = load_ev_from_db(ident)

    l = []
    for ent, assertion in ev.objects.iteritems():
        (head, tail) = ent,assertion
        l.append((head, tail))
    l.sort()

    doc = SimpleDocument(os.path.join(datadir,'HTMLgen.rc'))    
    doc.append("<b>You can go to DIKB assertion index here:</b>  ")
    doc.append(Href(url="/dikb-evidence/index.html",text="DIKB assertion index"))
    doc.append("<br><b>You can go to DIKB the home page here:</b>  ")
    doc.append(Href(url="/dikb-evidence/front-page.html",text="DIKB Front Page"))
    doc.append(P())

    obj = ""
    for ent, assertion in l:
        if assertion.object != obj:
            obj = assertion.object 
            doc.append("<HR><b>OBJECT:&nbsp;&nbsp;&nbsp;%s</b><br><br>" % obj.upper())
            
        slot_val = [assertion.slot,assertion.value]
        doc.append('''<a name="''', "_".join(slot_val),'''"></a>''')
        doc.append("<b>Assertion:", " ".join(slot_val), "</b>",BR())
           
        #table of evidence
        t = assertionShortTableView(assertion)
        doc.append(t,BR())

    doc.append(LICENSE)
    doc.write(htmldir + "/" + "evidenceSummary.html")
 

## create the documents
createEvidencePages()
#createFrontPage()
summarizeEvidence()           

