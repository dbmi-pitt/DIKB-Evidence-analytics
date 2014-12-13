
#basic entry attempt for inhibition
for elt in ["cyp2d6", "cyp3a4"]:
    a = Assertion("rosko", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "samuel rosko's brain", q = "samuel rosko believes that this is a likely result", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom", revwr = "boycer", timestamp = "11132014")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

#entry attempt for metabolite
a = Assertion("samuel", "has_metabolite", "rosko")
e = Evidence(ev)
e.create(doc_p = "rosko family tree", q = "Samuel has the middle name Charles and the last name of Rosko.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "11132014")
a.insertEvidence("for",e)
ev.addAssertion(a)

a = Assertion("samuel", "has_metabolite", "rosko")
e = Evidence(ev)
e.create(doc_p = "krebs family tree", q = "Samuel's mother's last name is Krebs rather than Rosko.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "11142014")
a.insertEvidence("against",e)
ev.addAssertion(a)

#add assumption for inhibition entry from metabolite entry
ev.objects['rosko_inhibits_cyp2d6'].evidence_for[0].assumptions.addEntry(['samuel_has_metabolite_rosko'])

#deleting an assertion
ev.deleteAssertion(ev.objects['rosko_inhibits_cyp2d6'])

#deleting an evidence item
ev.objects['samuel_has_metabolite_charles'].evidence_for.pop()

#identify fda2006, fda2006a, and fda206 evidence items and for what assertions
doc_fda2006 = {}
doc_fda2006a = {}
doc_fda206a = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006':
            doc_fda2006[it] = 'supports: ' + e
        elif it.doc_pointer == 'fda2006a':
            doc_fda2006a[it] = 'supports: ' + e
        elif it.doc_pointer == 'fda206a':
            doc_fda206a[it] = 'supports: ' + e
    for it in v.evidence_against:
        if it.doc_pointer == 'fda2006':
            doc_fda2006[it] = 'supports: ' + e
        elif it.doc_pointer == 'fda2006a':
            doc_fda2006a[it] = 'supports: ' + e
        elif it.doc_pointer == 'fda206a':
            doc_fda206a[it] = 'supports: ' + e

#create one group for all instead of 3, since it was just typos anyways
doc_fda = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            doc_fda[it] = 'supports: ' + e
    for it in v.evidence_against:
         if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            doc_fda[it] = 'supports: ' + e

#remove all the evidence based on fda2006 information
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            v.evidence_for.remove(it)
    for it in v.evidence_against:
         if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            v.evidence_against.remove(it)

#create list of evidence that has fda2006 data as a supported assumption my guess for this is to create a list of all evidence claims that are supported by fda2006, then compare that to the assumptions for every item, and make a second list of those which have the fda2006 claims in their assumptions... should just be a for loop within a for loop
e_list = []
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            if e_list.count(e) == 0:
                e_list.append(e)
    for it in v.evidence_against:
         if it.doc_pointer == 'fda2006' or it.doc_pointer == 'fda2006a' or it.doc_pointer == 'fda206a':
            if e_list.count(e) == 0:
                e_list.append(e)
dep_list = []
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        if len(it.assumptions.getEntries()) > 0:
            for assum in it.assumptions.getEntries():
                if e_list.count(assum) > 0 and dep_list.count(assum) == 0:
                    dep_list.append(assum)
    for it in v.evidence_against:
         if len(it.assumptions.getEntries()) > 0:
            for assum in it.assumptions.getEntries():
                if e_list.count(assum) > 0 and dep_list.count(assum) == 0:
                    dep_list.append(assum)

#sample evidence entry from 2012 data
a = Assertion("enoxacin", "inhibits", "cyp1a2")
e = Evidence(ev)
e.create(doc_p = "fda2012", q = "The FDA guidelines suggest that this is a strong in vivo inhibitor of CYP3A4. For more information, see Table 3, p. 41 and Table 5 on the FDA website.", ev_type = "Non_Tracable_Statement", revwr = "roskos", timestamp = "11252014")
a.insertEvidence("for",e)
ev.addAssertion(a)

#sample for a change from 2006 to 2012, 
#     ev.objects['clarithromycin_inhibits_cyp3a4'].evidence_for[1].doc_pointer 
#returns fda2006a, so to change it to 2012, we would simply use the following code:
ev.objects['clarithromycin_inhibits_cyp3a4'].evidence_for[1].doc_pointer = 'fda2012'
#and to correct the quote, we would use the following code:
ev.objects['clarithromycin_inhibits_cyp3a4'].evidence_for[1].quote = '"The FDA guidelines suggest that this is a strong in vivo inhibitor of CYP3A4. For more information, see Table 3, p. 41 and Table 5 on the FDA website."'



