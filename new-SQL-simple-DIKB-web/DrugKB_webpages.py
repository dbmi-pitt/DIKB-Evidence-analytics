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
## File:          DrugKB_webpages.py

## functions for generating re-used html snippets 

import string, re, os, time, glob
from HTMLcolors import *
from HTMLgen import *

from DIKB.ModelUtils import *
from DIKB.EvidenceModel import *



### define functions for the various html pages
def addAssertionsForm(object_lst, slot_lst, object_type):
    form = Form('editAssertions.rpy')
    form.append("Please select the object that you want to make an assertion about:")
    form.append(BR())
    if len(object_lst) == 0:
        object_lst = ["No Objects to choose from!"]
    objects = Select(object_lst, name='object', size=1, multiple=0)
    form.append(objects)
    form.append(P()) 
    form.append("Please select the slot you have information on:")
    form.append(BR())
    slots = Select(slot_lst, name='slot', size=1, multiple=0)
    form.append(slots)
    form.append(P())
    """gg - Added a hidden field for object type so we don't have to try to figure it out by name in editAssertions.rpy"""
    hidden = Input(type='hidden', name='type', value=object_type)
    form.append(hidden)
    form.submit = Input(type='submit', value='Add a value for this assertion')

    return form
           

def selectObjectSlotForm(submit_url, obj, slot, value_lst):
    form = Form(submit_url)
    form.append(Input(type='hidden', name='object', value=obj))
    form.append(Input(type='hidden', name='slot', value=slot))
    form.append(Input(type='hidden', name='assumption_picks', value=""))
    form.append(Input(type='hidden', name='new_assumption', value="ignore"))
    
    form.append(" ".join(["Edit an assertion for <b>object: ", obj,"</b>",
                          " and <b>slot:", slot, "</b>"]))
    form.append(BR())
    form.append("Please select a value for the slot that this evidence suggests:")
    form.append(BR())
    form.append(P())
    values = Select(value_lst, name='value', size=1, multiple=0)
    form.append(values)
    form.append(P())

    form.append(Input(type='checkbox',  name='assert-by-default', llabel='Assert by default with no evidence support? '))
    
    form.submit = Input(type='submit', name="add-assumptions", value='Add assumptions')
    form.append(P(), Input(type='submit', name="add-assumptions", value='No assumptions needed'))

    return form

def addAssumptionsForm(submit_url, obj, slot, value, assumption_keys, assumption_picks):
    form = Form(submit_url)
    form.append(Input(type='hidden', name='object', value=obj))
    form.append(Input(type='hidden', name='slot', value=slot))
    form.append(Input(type='hidden', name='value', value=value))
    form.append(Input(type='hidden', name='assumption_picks', value=",".join(assumption_picks)))

    """ get assumptions that this use of evidence depends on """
    form.append('''<a name="add_assumptions"></a>''')
    assumption_picks = filter(lambda x: x != "", assumption_picks)
    form.append(" ".join(["If necessary, add an assumption that this use of evidence depends on; currently - <br><tt>",
                          "<br>".join(assumption_picks),"</tt><br>"]))

    assumption_keys.sort()
    assumption_keys.insert(0,"")
    form.append(Select(assumption_keys, name='new_assumption', size=1, multiple=0))
    form.append(Input(type='submit', name="add-assumptions", value='Add this assumption'))
    form.append("<br>")
    form.submit = Input(type='submit', name="add-assumptions", value='Done')

    return form

def addEvidenceForm(submit_url, obj, slot, value, assumption_picks, default):
        
    form = Form(submit_url)
    form.append(Input(type='hidden', name='object', value=obj))
    form.append(Input(type='hidden', name='slot', value=slot))
    form.append(Input(type='hidden', name='value', value=value))
    form.append(Input(type='hidden', name='assumption_picks', value=",".join(assumption_picks)))

    if default:
        form.append(" ".join(["<h3>Assertion '<b>", obj,"_", slot, "_", value, '</b> will be enabled by default however you can still enter evidence in case the validity of the assertion will later be evaluated by evidence.</h3>']))
        form.append(Input(type='hidden', name='assert_by_default', value="True"))
        form.append(Input(type='submit', name="evidence-entry", value='Do Not Add Evidence at This Time'), P())
        
    else:
        form.append(" ".join(["Add evidence for <b>object:", obj,"</b>",
                              ", <b>slot:", slot, "</b>, with <b>value:", value, '</b>']))
    form.append(BR())
    
    r = reviewers
    r.sort()
    form.append(Select(r, name='reviewer', size=1, multiple=0),P())
                
    form.append("".join(["Is this evidence for or against slot value <b>", value,
                         "</b>?"]),P())
    radio_for = Input(type='radio',  name='position', value='for', checked=True, llabel='Evidence for')
    radio_against = Input(type='radio',  name='position', value='against',  llabel='Evidence against')
    form.append(radio_for,BR(),radio_against,P())

    if slot == 'bioavailability':
        form.append("The proportion (%/100) of an active ingredient's dose that reaches systemic circulation: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())
    elif slot == 'first_pass_effect':
        form.append("The proportion (%/100) of an active ingredient's absorbed dose that is cleared by first-pass metabolism: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())
    elif slot == 'fraction_absorbed':
        form.append("The proportion (%/100) of an active ingredient's dose that is absorbed in the gastro-intestinal tract: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())
    elif slot == 'increases_auc':
        form.append("The number of study participants: ")
        form.append(Input(type='text',  name='numb_subj', size=10), P())
        form.append("The object drug's's dose in grams: ")
        form.append(Input(type='text',  name='object_dose', size=10), P())
        form.append("The precipitant drug's's dose in grams: ")
        form.append(Input(type='text',  name='precip_dose', size=10), P())
        form.append("AUC_i/AUC (AUC_i: the AUC of the object drug in the presence of inhibitor): ")
        form.append(Input(type='text',  name='cont_value', size=10), P())
    elif slot == 'inhibition_constant':
        form.append("The inhibition constant, k_i, in grams/L: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())

        e_it = In_vitro_inhibition_study()
        e_s = e_it.enzyme_system.range
        form.append("The enzyme system used in this study: ")
        form.append(Select(e_s, name='enzyme_system', size=1, multiple=0),P())
    
    elif slot == 'maximum_concentration':
        form.append("The number of subjects in the study (if available): ")
        form.append(Input(type='text',  name='numb_subjects', size=10), P())
        form.append("The dose of the drug from which the C_max was derived in grams: ")
        form.append(Input(type='text',  name='dose', size=10), P())
        form.append("The maximum concentration, C_max, in grams/L: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())

    elif slot == 'minimum_therapeutic_dose':
        form.append("The usual (or commonly accepted) minimum therapeutic dose in <I>grams</I> per day: ")
        form.append(Input(type='text',  name='cont_value', size=10), P())

    elif slot == 'minimum_therapeutic_dose_is_at_least':
        form.append("A dose (in <I>grams</I> per day) assumed to be larger than the usual (or commonly accepted) minimum therapeutic dose (the system will confirm the validity of this assertion during inference): ")
        form.append(Input(type='text',  name='cont_value', size=10), P())
    
    form.append("Please input a pointer to this evidence, For example a PubMed ID, a url, or the article identifier from the Drug KB bibliography:")
    form.append(P())
    form.append(Input(type='text',  name='pointer', size=55), P())

    form.append("Please paste or type in relevant information about the evidence including data required by inclusion criteria:",BR())
    form.append(Textarea(name='quote', rows=20, cols=55), P())

    """evidence type specific input"""
    

    """get evidence types"""
    try:
        f = open("data/evidence-types", 'r')
    except IOError, err:
        warning(" ".join(["Could not open file containing evidence types at:",getcwd(),"data/evidence-types",
                          "Please make sure this file exists. Returning None"]) , 1)
        return None

    types = f.read()
    f.close()

    reg = re.compile("^[_A-Za-z0-9]+",re.MULTILINE)
    all_types = reg.findall(types)
    all_types.sort()
                
    lst = types.split('\n')
    lst.sort()
    
    form.append("<br><b>Please select one evidence type from the set of evidence types listed below:</b>",BR())
    cnt = 0
    for item in lst:
        radio = Input(type='radio',  name='type', value=all_types[cnt], rlabel=item)
        form.append(radio, BR(), BR())
        cnt = cnt + 1

    form.submit = Input(type='submit', name="evidence-entry", value='Add Evidence')
    
    return form


def readyToClassifyForm(object_slot_value, state):
    form = Form("".join(['viewData.rpy#',object_slot_value]))
    form.append(Input(type='hidden', name='obj_slot_val', value = object_slot_value))
    form.append("Ready for classification: ")
    radio_True = Input(type='radio',  name='state', value='True', checked = state, llabel='True')
    radio_False = Input(type='radio',  name='state', value='False', checked=(not state), llabel='False')
    form.append(BR(),radio_True,BR(),radio_False,BR())
    form.submit = Input(type='submit', value='Change Classification Status')

    return form


def assertionTableView(assertion):
    """Create a table view of an assertion

       @param assertion:EvidenceBase::Assertion instance

       returns: an HTMLgen Table instance
    """
    title = 'Evidence'
    t = Table(title)
    t_content = []
    
    if len(assertion.evidence_for) == 0:
        tmp = ['No evidence for!']
        t_content.append(tmp)
            
    else:
        for i in assertion.evidence_for:
            e = []
            e = [Bold('Evidence For (item %s)').__str__() % assertion.evidence_for.index(i),
                 Bold('Evidence Type: ').__str__() + i.evidence_type.value,
                 Bold('Pointer: ').__str__() + make_link(i.doc_pointer),
                 Bold('Reviewer: ').__str__() + i.reviewer.value]
            t_content.append(e)

            e = ['', Bold('Quote: ').__str__() + i.quote]
            t_content.append(e)

            e = ['', Bold('Assumptions: ').__str__() + "<br>".join(i.assumptions.getEntries())]
            t_content.append(e)
                
            if assertion.slot in ['bioavailability', 'first_pass_effect', 'fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration']:
                e = ['', Bold(assertion.slot + ": ").__str__() + str(i.value)]
                t_content.append(e)
                
            if assertion.slot == 'inhibition_constant':
                e = ['', Bold('enzyme_system: ').__str__() + str(i.enzyme_system.getEntry())]
                t_content.append(e)
                    
            elif assertion.slot == 'increases_auc':
                e = ['', Bold('object_dose: ').__str__() + str(i.object_dose), Bold('precip_dose: ').__str__() + str(i.precip_dose)]
                t_content.append(e)
                e = ['', Bold('numb_subj: ').__str__() + str(i.numb_subj)]
                t_content.append(e)
                    
            elif assertion.slot == 'maximum_concentration':
                e = ['', Bold('dose: ').__str__() + str(i.dose), Bold('numb_subjects: ').__str__() + str(i.numb_subjects)]
                t_content.append(e)
                            
    if len(assertion.evidence_against) == 0:
        if assertion.slot in ['bioavailability', 'first_pass_effect', 'fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration']:
            msg = [Bold('Evidence Against N/A').__str__()]
        else:
            msg = [Bold('No evidence against!').__str__()]
            t_content.append(msg)
    else:
        for i in assertion.evidence_against:
            e = []
            e = [Bold('Evidence Against (item %s)').__str__() % assertion.evidence_against.index(i),
                 Bold('Evidence Type: ').__str__() + i.evidence_type.value,
                 Bold('Pointer: ').__str__() + make_link(i.doc_pointer),
                 Bold('Reviewer: ').__str__() + i.reviewer.value]
            t_content.append(e)

            e = ['', Bold('Quote: ').__str__() + i.quote]
            t_content.append(e)

            e = ['', Bold('Assumptions: ').__str__() + "<br>".join(i.assumptions.getEntries())]
            t_content.append(e)
                   
    t.body = t_content

    return t

def assertionShortTableView(assertion):
    """Create a simplified table view of an assertion

       @param assertion:EvidenceBase::Assertion instance

       returns: an HTMLgen Table instance
    """
    title = 'Evidence'
    t = Table(title)
    t_content = []
    
    if len(assertion.evidence_for) == 0:
        tmp = ['No evidence for!']
        t_content.append(tmp)
            
    else:
        for i in assertion.evidence_for:
            e = []
            e = [Bold('Evidence For (item %s)').__str__() % assertion.evidence_for.index(i),
                 Bold('Evidence Type: ').__str__() + i.evidence_type.value]
            t_content.append(e)
                            
    if len(assertion.evidence_against) == 0:
        if assertion.slot in ['bioavailability', 'first_pass_effect', 'fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration']:
            msg = [Bold('Evidence Against N/A').__str__()]
        else:
            msg = [Bold('No evidence against!').__str__()]
            t_content.append(msg)
    else:
        for i in assertion.evidence_against:
            e = []
            e = [Bold('Evidence Against (item %s)').__str__() % assertion.evidence_against.index(i),
                 Bold('Evidence Type: ').__str__() + i.evidence_type.value]
            t_content.append(e)

    t.body = t_content

    return t


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
