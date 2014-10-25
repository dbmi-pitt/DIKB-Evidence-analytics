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
## File:          confirmSave.rpy


import os,sys, string, cgi
from time import time, strftime, localtime

from twisted.python import log as t_log
from twisted.web import resource

from mysql_tool import *
from DIKB_Load import load_ev_from_db

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

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
ident = "".join(["confirmSave.rpy cgi:", timestamp])

#dikb = DIKB("dikb",ident, EvidenceBase("null", ident))
#dikb.unpickleKB("var/DIKB/dikb.pickle")

"""gg - Load an EvidenceBase from the database using DIKB-Load.py.  Hopefully faster
        than unpickling"""
#ev = load_ev_from_db(ident)
#ev = EvidenceBase("evidence",ident)
#ev.unpickleKB("var/evidence-base/ev.pickle")

## paths
htmldir = 'html'   ## where html where go
datadir = 'data'   ## where data and config files reside
bibpath = "bib"


###------------------------HTML section-----------------------
##set up html
doctitle = 'Drug Interaction Knowledge Base %s' % str(version)


def create_page(page_t="collect", args = [], vals = [], warnings=None, aft=None, fore=None, top=None, home=None):
    doc = SeriesDocument(os.path.join(datadir,'HTMLgen.rc'))
    doc.title = doctitle
    doc.subtitle = 'Confirm and save new evidence to the Drug Interaction Knowledge Base'
    doc.goprev,doc.gonext,doc.gotop,doc.gohome = aft,fore,top,home

    if page_t == 'Cancel':
        doc.append("Save canceled, you can go back with you browser's back button or return to the home page here:",BR(),BR())
        doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))
        return doc.__str__()
    elif page_t == 'Save':
        doc.append("<b>Evidence entered succesfully!</b>",BR())
        if warnings:
            doc.append("<br><b>Please note the following warnings occured when saving evidence:</b>",BR(),warnings.replace("\n","<BR>").replace("\t","&nbsp;&nbsp;&nbsp;"),BR(),BR())
        doc.append("You can go to DIKB the home page here:",BR())
        doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))

        doc.append(BR(),BR(),"You can also enter this evidence item for an assertion involving a different object:",BR())
        form = Form('confirmSave.rpy')
        i = 0

        #objects = dikb.objects.keys()
        #objects.sort()      
        """gg - Looks like you're just loading the names of all the objects in the dikb...they span several tables now, so 
           we need to get them all.  Enzymes loaded from text file."""
        objects = session.query(DrugTable._name).all() + session.query(MetaboliteTable._name).all() + session.query(ChemicalTable._name).all() + get_enzymes()
        objects.sort()
        form.append("".join(["<b>",args[i],": </b>"]))  # input for the new object 
        form.append(Select(objects, name='object', size=1, multiple=0))
        for item in vals:
            if args[i] == 'checkout':
                continue

            if args[i] == "object":            
                pass

            else:
                doc.append("".join(["<b>",args[i],": </b>",item]),BR())
                form.append(Input(type='hidden', name=args[i], value=item))
            i = i+1
                   
        form.submit = Input(type='submit', value='Add a value for this assertion')
        doc.append(form)
            
        return doc.__str__()

    elif page_t == 'Error':
        doc.append(warnings, "<br>You can go to DIKB the home page here:",BR(),BR())
        doc.append(Href(url="/html/front-page.html",text="DIKB Front Page"))
        return doc.__str__()

    doc.append("Please confirm that you want to save the following  evidence:",P())

    form = Form('confirmSave.rpy')
    i = 0
    for item in vals:
        doc.append("".join(["<b>",args[i],": </b>",item]),BR())
        form.append(Input(type='hidden', name=args[i], value=item))
        i = i+1

    ## a helpful check on previous use of a particular evidence item
    """gg - This was a roundabout way of checking for the string "pointer" in args -- hopefully it always is."""
    #if len(filter(lambda x: x == "pointer", args)) > 0:
    if "pointer" in args:
        pntr = vals[args.index('pointer')]
        #ev.buildEvidenceAssrtDicts()

        doc.append("<p><i>Please confirm by reading through the following lists that 1) this will not be a duplicate use of this evidence and 2) that the entry of this evidence will not cause it to be linked to both an inhibits/substrate_of assertion AND an increase_auc assertion</i></p>")
        """gg - I think you're just getting all the assertions associated with a particular pointer"""
        """gg - So, do a query across Evidence, Evidence_map, and Assertions to get all assertions with a particular
        associated pointer. Currently, the map refers to evidence_for and against fields, so already separated on that criteria."""
        """gg - ***NOTE: Evidence_map is not a true many-to-many table, but this may still currently work most or all of the time."""

        ev_for = session.query(AssertionTable._name).filter(AssertionTable.evidence_for == EvidenceMapTable.assert_ev_id) \
            .filter(EvidenceMapTable.id == EvidenceTable.id).filter(EvidenceTable.doc_pointer == pntr).all()
        ev_for = list(set(ev_for))
        ev_against = session.query(AssertionTable._name).filter(AssertionTable.evidence_against == EvidenceMapTable.assert_ev_id) \
            .filter(EvidenceMapTable.id == EvidenceTable.id).filter(EvidenceTable.doc_pointer == pntr).all()
        ev_against = list(set(ev_against))

        #doc.append("pntr: " + pntr, BR())
        #doc.append("ev_for: " + str(ev_for), BR())
        #doc.append("ev_against: " + str(ev_against), BR())
        if ev_for:
            st = '''evidence item '%s' is linked to the following assertions as 'evidence_for':''' % pntr
            doc.append(st, BR())
            doc.append("<br>".join([x[0] for x in ev_for]), BR())
        if ev_against:
            st = '''<br><br>evidence item '%s' is linked to the following assertions as 'evidence_against':''' % pntr
            doc.append(st, BR())
            doc.append("<br>".join([x[0] for x in ev_against]), BR())
        """
        if len(ev.ev_for_d.keys()) > 0 and ev.ev_for_d.has_key(pntr):
            st = '''evidence item '%s' is linked to the following assertions as 'evidence_for':''' % pntr
            doc.append(st, BR())
            doc.append("<br>".join(ev.ev_for_d[pntr]))
            
        if len(ev.ev_against_d.keys()) > 0 and ev.ev_against_d.has_key(pntr):
            st = '''<br><br>evidence item '%s' is linked to the following assertions as 'evidence_against':''' % pntr
            doc.append(st, BR())
            doc.append("<br>".join(ev.ev_against_d[pntr]))
        """
    form.append(P(),Input(type='submit', name="checkout", value='Cancel'))
    form.submit = Input(type='submit', name="checkout", value='Save')

    doc.append(form)
    doc.append(P())

    return doc.__str__()



class Resource(resource.Resource):
    """class that processes the form, from the twisted lib"""
    def __init__(self): 
        self.summary = ""
        self.error = "no results for this query: "
     
    def render(self, request):

        page = ""
        slot = None
        if request.args.has_key('slot'):
            slot = request.args['slot'][0]
        else:
            page = " variable: slot not recieved, Please use your browser's 'Back' button to enter this item."
            return page

        ## values common to all
        args = ['object','slot', 'value',  'assumption_picks', 'reviewer']

        if request.args.has_key('assert_by_default'):
            args += ['assert_by_default']
            
        if (request.args.has_key('evidence-entry') and request.args['evidence-entry'][0] == 'Add Evidence') or request.args.has_key('has_evidence'):
            # handle new evidence entry
            args += ['position', 'pointer', 'quote', 'type', 'has_evidence']
     
            if slot in ['bioavailability', 'first_pass_effect', 'fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration', 'minimum_therapeutic_dose', 'minimum_therapeutic_dose_is_at_least']:
                args.append('cont_value')

            if slot == 'inhibition_constant':
                args.append('enzyme_system')
            elif slot == 'increases_auc':
                args += ['object_dose','precip_dose','numb_subj']
            elif slot == 'maximum_concentration':
                args += ['dose', 'numb_subjects']
            
                
        ## test for each variable in the request
        for arg in args:
            if not arg == 'has_evidence' and not request.args.has_key(arg):
                page = " variable: " + arg + " not recieved, Please use your browser's 'Back' button to enter this item."
                return page

        ## values common to all
        vals = [request.args['object'][0],
                request.args['slot'][0],
                request.args['value'][0],
                request.args['assumption_picks'][0],
                request.args['reviewer'][0]]

        if request.args.has_key('assert_by_default'):
            vals += ["True"]

        ## for when there is no evidence to enter
        if (request.args.has_key('evidence-entry') and request.args['evidence-entry'][0] == 'Do Not Add Evidence at This Time') or request.args.has_key('no_evidence'):
            args += ["no_evidence"] # this is a special argument that is not passed in to confirm save the first time
            vals += ["True"]
        else:
            vals += [request.args['position'][0],
                     cgi.escape(request.args['pointer'][0], True),
                     cgi.escape(request.args['quote'][0], True),
                     request.args['type'][0],
                     "True"]
        
            if slot in ['bioavailability', 'first_pass_effect','fraction_absorbed', 'inhibition_constant', 'increases_auc', 'maximum_concentration', 'minimum_therapeutic_dose', 'minimum_therapeutic_dose_is_at_least']:
                vals.append(request.args['cont_value'][0])
            if slot == 'inhibition_constant':
                vals.append(request.args['enzyme_system'][0])
            elif slot == 'increases_auc':
                vals += [ request.args['object_dose'][0], request.args['precip_dose'][0], request.args['numb_subj'][0]]
            elif slot == 'maximum_concentration':
                vals += [ request.args['dose'][0],  request.args['numb_subjects'][0]]
            
      
        if request.args.has_key('checkout'):
            val = request.args['checkout'][0]
            if val == 'Cancel':
                page = create_page('Cancel')
                return page
            if val == ('Save'):
                """Time to add evidence"""
                ev = load_ev_from_db(ident)
                ev_present = not request.args.has_key("no_evidence")
                assumpts_present = not vals[args.index('assumption_picks')].split(",") == ['']

                """gg: Go ahead and get the assertion from the assertion table if present"""
                _name = "_".join([vals[args.index('object')], slot, vals[args.index('value')]])
                try:
                    atable = session.query(AssertionTable).filter(AssertionTable._name == _name).one()
                except NoResultFound or MultipleResultsFound:
                    atable = None
                
                a = None
                e = None
                if slot in ['substrate_of',
                            'is_not_substrate_of',
                            'inhibits',
                            'does_not_inhibit',
                            'induces',
                            'primary_total_clearance_mechanism',
                            'primary_metabolic_clearance_enzyme',
                            'primary_total_clearance_enzyme',
                            'in_vitro_probe_substrate_of_enzyme',
                            'in_viVo_probe_substrate_of_enzyme',
                            'in_vitro_selective_inhibitor_of_enzyme',
                            'pceut_entity_of_concern',
                            'does_not_permanently_deactivate_catalytic_function',
                            'permanently_deactivates_catalytic_function',
                            'sole_PK_effect_alter_metabolic_clearance',
                            'has_metabolite',
                            'controls_formation_of',
                            'polymorphic_enzyme',
                            'in_viVo_selective_inhibitor_of_enzyme']:

                    a = Assertion(vals[args.index('object')], slot, vals[args.index('value')])
                    
                    """gg: Build an AssertionTable object if needed"""
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "Assertion")

                    if ev_present:
                        """gg - Wherever a call to the dikb Evidence class is made, also create an EvidenceTable instance and 
                                add the appropriate data"""
                        e = Evidence(ev)
                        etable = EvidenceTable()
                        """gg - This looks to be a common way to add data to evidence instances in the dikb, so I added a create method in
                                EvidenceTable to emulate the process"""
                        e.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp)
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp, evidence_class="Evidence")

                        if assumpts_present:
                            """gg - For now, just add the assumptions to the EvidenceTable object, but they will be saved
                                    to an AssumptionMapTable object when the session is flushed"""
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))
                    
                elif slot in ['first_pass_effect', 'bioavailability', 'fraction_absorbed']:
                    ## NOTE (RDB): this code could be refactored to
                    ## eliminate all of the sub-class instantiations
                    ## and associated logic because the Evidence table
                    ## has all of the columns necessary to model the
                    ## values of each class.
                    a = Assertion_m_discrete(vals[args.index('object')], slot, vals[args.index('value')])
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "Assertion_m_discrete")
                    
                    if ev_present:
                        e = EvidenceContinousVal(ev)
                        etable = EvidenceTable()
                        e.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp, vals[args.index('cont_value')])
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp, evidence_class="EvidenceContinuousVal", value=vals[args.index('cont_value')])
                        ## NOTE (RDB): - cont_value will be stored in
                        ## the value column of the table -- this
                        ## cont_value is different than the cont_value
                        ## present in the ContValueAssertion class and
                        ## those that inherit from it

                        # t_log.msg('confirmSave:: value of "cont_val": ' + vals[args.index('cont_value')])
                        if assumpts_present:
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))

                elif slot in ['inhibition_constant']:
                    a = Assertion_inhibition_constant(vals[args.index('object')], slot, vals[args.index('value')])
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "Assertion_inhibition_constant")

                    if ev_present:
                        e = In_vitro_inhibition_study(ev)
                        etable = EvidenceTable()
                        e.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp, vals[args.index('cont_value')], vals[args.index('enzyme_system')])
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')],
                                 vals[args.index('reviewer')], timestamp, evidence_class="In_vitro_inhibition_study", value=vals[args.index('cont_value')], 
                                 enzyme_system=vals[args.index('enzyme_system')])
                        if assumpts_present:
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))
                                 
                elif slot in ['maximum_concentration']:
                    a = Assertion_maximum_concentration(vals[args.index('object')], slot, vals[args.index('value')])
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "Assertion_maximum_concentration")

                    if ev_present:
                        e = Maximum_concentration_study(ev)
                        etable = EvidenceTable()
                        e.create(vals[args.index('pointer')], vals[args.index('quote')],
                                 vals[args.index('type')], vals[args.index('reviewer')],
                                 timestamp, vals[args.index('dose')],
                                 vals[args.index('numb_subjects')], vals[args.index('cont_value')])
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')],
                                 vals[args.index('type')], vals[args.index('reviewer')],
                                 timestamp, dose=vals[args.index('dose')],
                                 numb_subjects=vals[args.index('numb_subjects')], evidence_class="Maximum_concentration_study", 
                                      value=vals[args.index('cont_value')])

                        if assumpts_present:
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))

                elif slot in ['increases_auc']:
                    a = ContValAssertion(vals[args.index('object')], slot, vals[args.index('value')])
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "ContValAssertion")

                    if ev_present:
                        e = PKStudy(ev)
                        etable = EvidenceTable()
                        e.create(vals[args.index('pointer')], vals[args.index('quote')],
                                 vals[args.index('type')], vals[args.index('reviewer')],
                                 timestamp, vals[args.index('object_dose')],
                                 vals[args.index('precip_dose')], vals[args.index('cont_value')],
                                 numb_subj = vals[args.index('numb_subj')])
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')],
                                 vals[args.index('type')], vals[args.index('reviewer')],
                                 timestamp, evidence_class="PKStudy", object_dose=vals[args.index('object_dose')],
                                 precip_dose=vals[args.index('precip_dose')], value=vals[args.index('cont_value')],
                                 numb_subj = vals[args.index('numb_subj')])
                        
                        if assumpts_present:
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))

                elif slot in ['minimum_therapeutic_dose', 'minimum_therapeutic_dose_is_at_least']:
                    a = ContValAssertion(vals[args.index('object')], slot, vals[args.index('value')])
                    if not atable:
                        atable = AssertionTable()
                        atable.create(vals[args.index('object')], slot, vals[args.index('value')], "ContValAssertion")

                    if ev_present:
                        e = EvidenceContinousVal(ev)
                        etable = EvidenceTable()
                        e.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')], vals[args.index('reviewer')], timestamp)
                        etable.create(vals[args.index('pointer')], vals[args.index('quote')], vals[args.index('type')], vals[args.index('reviewer')], 
                                      timestamp, evidence_class="EvidenceContinuousVal", value=vals[args.index('cont_value')])
                        
                        if assumpts_present:
                            e.assumptions.addEntry(vals[args.index('assumption_picks')].split(","))
                            etable.add_assumptions(vals[args.index('assumption_picks')].split(","))
                    

                warnings = ""
                if a and e:
                    try:
                        rslts = [None, None]
                        if vals[args.index('position')] == "for":
                            rslt = a.insertEvidence("for",e, ev)
                        elif vals[args.index('position')] == "against":
                            rslt = a.insertEvidence("against",e, ev)

                        if rslt[0]:
                            page = create_page('Error', warnings="<b>Evidence was not entered into the system due to a failure of an evidence integrity check:</b><br>%s") % rslt[1]
                            return page
                        elif rslt[1]:
                            warnings += rslt[1]
                    except ValueError:
                        page = create_page('Error', warnings="<b>There was a PROGRAM ERROR (ValueError):</b><br> Could not find value vals[args.index('position')]<br>Please notify boycer@u.washington.edu.")
                        return page
                else:
                    pass

                if request.args.has_key('assert_by_default'):
                    # a_str = "_".join([vals[args.index('object')], slot, vals[args.index('value')]])
                    # if ev.objects.has_key(a_str):
                    #     # we have to set this attribute manually if there is already an assertion instance
                    #     # in the evidence base
                    #     ev.objects[a_str].assert_by_default = True
                    # else:
                    #     a.assert_by_default = True
                    """gg: Set the AssertionTable objects assert_by_default attribute to true"""
                    atable.assert_by_default = "1"

                ## NOTE (RDB): the old addAssertion method checked to see of the assertion is new and added it, otherwise, it modified the assertion (if I remember by simply adding the evidence instance to the evidence_for or evidence_against list). 
                """gg: DIKB objects are used to run the checks above using an EvidenceBase loaded from the database.  Now, we need to flush
                the sqlalchemy session, making sure to save the evidence items, assumptions, mapping, and either save the new assertion or 
                modify an existing one."""

                
                """gg: Retrieve or create an id to map from Assertions to Evidence (Assertions.evidence_for or Assertions.evidence_against).
                Also need an id to map from Evidence to Assumption_map (Evidence.assump_list_id).
                Set up the mapping tables, add each to session and commit.  If you're asserting by default
                without evidence, just save the assertion."""
                
                if ev_present:
                    if vals[args.index('position')] == 'for':
                        if atable.evidence_for:
                            evMapId = atable.evidence_for
                        else:
                            maxEvFor = session.query(func.max(AssertionTable.evidence_for)).one()[0]
                            maxEvAgainst = session.query(func.max(AssertionTable.evidence_against)).one()[0]
                            evMapId = maxEvFor+1 if maxEvFor > maxEvAgainst else maxEvAgainst+1
                            atable.evidence_for = evMapId
                    elif vals[args.index('position')] == 'against':
                        if atable.evidence_against:
                            evMapId = atable.evidence_against
                        else:
                            maxEvFor = session.query(func.max(AssertionTable.evidence_for)).one()[0]
                            maxEvAgainst = session.query(func.max(AssertionTable.evidence_against)).one()[0]
                            evMapId = maxEvFor+1 if maxEvFor > maxEvAgainst else maxEvAgainst+1
                            atable.evidence_against = evMapId
                    if assumpts_present:
                        etable.assump_list_id = session.query(func.max(EvidenceTable.assump_list_id)).one()[0]+1 

                    if not atable.id:
                        atable.id = session.query(func.max(AssertionTable.id)).one()[0]+1
                    etable.id = session.query(func.max(EvidenceTable.id)).one()[0]+1
                    etable._name = e._name

                    evmapTable = EvidenceMapTable()
                    evmapTable.id = session.query(func.max(EvidenceMapTable.id)).one()[0]+1
                    evmapTable.assert_ev_id = evMapId
                    evmapTable.assert_id = atable.id

                    for assumption in etable.assumptions:
                        assumpmapTable = AssumptionMapTable()
                        assumpmapTable.id = session.query(func.max(AssumptionMapTable.id)).one()[0]+1
                        assumpmapTable.assump_list_id = etable.assump_list_id
                        assumpmapTable.ev_id = etable.id
                        assumpmapTable.assump_assert_name = assumption
                        session.add(assumpmapTable)

                    if atable not in session.dirty:
                        session.add(atable)
                    session.add_all([etable, evmapTable])

                    session.commit()
                else:
                    if not atable.id:
                        atable.id = session.query(func.max(AssertionTable.id)).one()[0]+1
                    if atable not in session.dirty:
                        session.add(atable)
                    session.commit()


            #ev.addAssertion(a)                
            #ev.pickleKB("var/evidence-base/ev.pickle")  ### NEW EVIDENCE GETS WRITTEN HERE 

            page = create_page('Save', args, vals, warnings=warnings)
            return page
        
        else:
            page = create_page('collect', args, vals)

        return page

session = load_session()
resource = Resource()
