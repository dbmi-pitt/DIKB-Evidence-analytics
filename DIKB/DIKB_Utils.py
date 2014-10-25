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
## File:          DIKB_Utils.py

###Functions for editing assertions in the KBs
from DIKB import *
from DrugModel import *
from EvidenceModel import *

            
# #### a function for adding bioavailability - TODO: create general evidence adding/editing functions
# def addBioavail(drg,et,pntr, quote, val, revwr, ev_base, ev_pickle_path, dikb):
#     """ add evidence for the bioavailability of a drug.
#     in: drg -  a string specifying an drug in the 'dikb' knowledge-base
#     in: et -  a string specifying the 'evidence_type' of the evidence
#     in: pntr -  a string specifying the name or pubmed id of the evidence
#     in: quote - a relevant quote from the document 
#     in: val - a float value for the bioavailability of the drug
#     in: revwr - a string stating the reviewer of this evidence
#     in: ev_base - an EvidenceBase drgect to store this evidence in
#     in: ev_pickle_path - a string path to the pickle file for the evidence base
#     in: dikb - a DIKB drgect

#     out: 1 if error, 0 otherwise"""

#     if not dikb.drgects.has_key(drg):
#         print(" ".join(["addBioavail - Error: drgect name ", drg, "does not exist in dikb; spelling correct?. EXITING! Values - ",
#                         "drug: ", drg, "evidence pointer: ", pntr, "evidence type: ", et]))
#         return 1

#     a1 = Assertion(drg,'bioavailability','continuous_value')
#     e1 = EvidenceContinousVal()
#     e1.doc_pointer = pntr
#     e1.quote = quote
#     e1.evidence_type.putEntry(et)
#     e1.value = val
#     e1.reviewer.putEntry(revwr)
#     a1.evidence_for.append(e1)

#     lst_len = len(dikb.drgects[drg].bioavailability.evidence)
    
#     ev_base.addAssertion(a1)

#     if len(dikb.drgects[drg].bioavailability.evidence) == lst_len:
#         print(" ".join(["addBioavail - Error: evidence for bioavailability did not get assigned. Values - ",
#                         "drug: ", drg, "evidence pointer: ", pntr, "evidence type: ", et]))

#     try:
#         ev.pickleKB(ev_pickle_path)
#         print(" ".join(["addBioavail - Message: evidence for bioavailability  added and stored in pickle. Values - ",
#                         "drug: ", drg, "evidence pointer: ", pntr, "evidence type: ", et]))
#     except IOError, err:
#         print(" ".join(["addBioavail - Error: evidence for bioavailability added but NOT STORED in pickle. Values - ",
#                         "drug: ", drg, "evidence pointer: ", pntr, "evidence type: ", et]))
#     return 0
