import os,sys, string, cgi
from time import time, strftime, localtime

import sys
sys.path = sys.path + ['.']

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from DIKB.ModelUtils import *
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *

ident = "".join(["Current SQL DIKB evidence : ", timestamp])
sqlEv = load_ev_from_db(ident)

# the number of supporting and refuting evidence items
ev_for_cnt = 0
ev_agnst_cnt = 0
for k,v in sqlEv.objects.iteritems():                  
    for e in v.evidence_for:
        ev_for_cnt += 1
    for e in v.evidence_against:
        ev_agnst_cnt += 1


## identify all doc_pointers in the system
docs = {}
for k,v in sqlEv.objects.iteritems():
    for e in v.evidence_for:
        if not docs.has_key(e.doc_pointer):
            docs[e.doc_pointer] = 1
        else:
            docs[e.doc_pointer] += 1
    for e in v.evidence_against:
        if not docs.has_key(e.doc_pointer):
            docs[e.doc_pointer] = 1
        else:
            docs[e.doc_pointer] += 1


# how is evidence being applied?
ev_for_docs = {}
ev_against_docs = {}
for k,v in sqlEv.objects.iteritems():
    for e in v.evidence_for:
        if not ev_for_docs.has_key(e.doc_pointer):
            ev_for_docs[e.doc_pointer] = 1
        else:
            ev_for_docs[e.doc_pointer] += 1
    for e in v.evidence_against:
        if not ev_against_docs.has_key(e.doc_pointer):
            ev_against_docs[e.doc_pointer] = 1
        else:
            ev_against_docs[e.doc_pointer] += 1

ev_for_against = filter(lambda x: x in ev_for_docs.keys() and x in ev_against_docs.keys(), docs.keys())
ev_for_only = filter(lambda x: x not in ev_against_docs.keys(), ev_for_docs.keys())
ev_against_only = filter(lambda x: x not in ev_for_docs.keys(), ev_against_docs.keys())
