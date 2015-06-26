## UPIA_grant_KB_development_2009.py
#
# Author: Richard Boyce, PhD
#
# Postdoctoral Associate in Biomedical Informatics at the University of Pittsburgh
## 

## This file contains a record of changes made to the DIKB and its
## evidence-base while working on a grant funded by the University of
## Pittsburgh Institute on Aging in 2009

## The knowledge-base and evidence-base pickles prior to the start of
## the study can be found in
## ./backups/dikb-pickle-backup_2008-01-21040355.tar.gz

import sys
sys.path = sys.path + ['.']
from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.DIKB_Utils import *
from DIKB.TranslationRules import *
from DIKB.ExportAssertions import *


## CODE TO RELOAD THE EB; SUFFICIENT FOR ADDING INFORMATION TO THE
## EB. IF YOU NEED TO ADD OBJECTS TO THE KB OR ACCESS EVIDENCE FROM
## THE DIKB'S DRUG MODEL, THEN USE THE CODE THAT RENOTIFIES OBSERVERS
ev = EvidenceBase("evidence","UPIA")
ev.unpickleKB("var/evidence-base/ev.pickle")
       

## CODE TO RELOAD THE KB AND EB AND RESET ALL OBSERVERS; NOT NECESSARY
## IF ONLY ADDING INFORMATION TO THE EB (ALSO, IN MOST CASES YOU CAN
## LOAD THE dikb WITHOUT RENOTIFYING OBSERVERS; TO DO THAT UNPICKLE
## THE ev BEFORE THE dikb)
ev = EvidenceBase("evidence","UPIA")
dikb = DIKB("dikb","UPIA", ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.unpickleKB("var/evidence-base/ev.pickle")


## insert drugs from the antipsychotic list developed on 04/07/2009
# for i in ["aripiprazole", "chlorpromazine", "clozapine", "droperidol", "fluphenazine", "haloperidol", "molindone", "olanzapine", "paliperidone", "perphenazine", "pimozide", "quetiapine", "risperidone", "thioridazine", "thiothixene", "trifluoperazine", "ziprasidone"]:
#     if i in dikb.objects.keys():
#         print "%i seems to be present already!"
#         continue

#     d = Drug(i)
#     dikb.putObject(d)

## insert drugs from the non-MAOI/non-tricyclic antidepressant list
# for i in ["citalopram", "escitalopram", "fluoxetine", "fluvoxamine", "paroxetine", "sertraline", "venlafaxine", "desvenlafaxine", "duloxetine", "bupropion", "mirtazapine", "trazodone"]:
#     if i in dikb.objects.keys():
#         print "%i seems to be present already!"
#         continue

#     d = Drug(i)
#     dikb.putObject(d)

#dikb.pickleKB("var/DIKB/dikb.pickle")
#ev.pickleKB("var/evidence-base/ev.pickle")

## insert drugs from listed in FDA guidance 2006 as probe substrates
## or selective inhibitors 
# for i in ["desipramine","omeprazole","dextromethorphan","atomoxetine","phenacetin"]:
#     if i in dikb.objects.keys():
#         print "%i seems to be present already!"
#         continue

#     d = Drug(i)
#     dikb.putObject(d)

## insert a metabolite of aripiprazole
#d = Metabolite("dehydro-aripiprazole")
#dikb.putObject(d)

## make a correction to the number of participants in an evidence item
## used to support fluoxetine increases_auc desipramine
ev.objects['fluoxetine_increases_auc_desipramine'].evidence_for[0].numb_subj = 9
ev.objects['fluoxetine_increases_auc_desipramine'].evidence_for[0].quote = 'Route of administration: oral (inferred because IV formulations do not appear to be available for fluoxetine and desipramine)\r\n\r\nstudy duration: see below\r\n\r\npopulation: 9 healthy males; all extensive metabolizers of dextromethorphan (o-demethylation)\r\n\r\nages: mean(std dev): &quot;adults&quot; but no mention of age. It can be inferred that these were healthy male adults and not exclusively elderly or children\r\n\r\nDescription: \r\nhe pharmacokinetic interactions of sertraline and fluoxetine with the tricyclic antidepressant desipramine were studied in 18 healthy male volunteers phenotyped as extensive metabolizers of dextromethorphan. Concentrations in plasma were determined after 7 days of desipramine (50 mg/day) dosing alone, during the 21 days of desipramine and selective serotonin reuptake inhibitor (SSRI) coadministration (fluoxetine, 20 mg/day; sertraline, 50 mg/day), and for 21 days of continued desipramine administration after SSRI discontinuation. Desipramine Cmax was increased 4.0-fold versus 31% and AUC0-24 was increased 4.8-fold versus 23% for fluoxetine versus sertraline, respectively, relative to baseline after 3 weeks of coadministration. Desipramine trough concentrations approached baseline within 1 week of sertraline discontinuation but remained elevated for the 3-week follow-up period after fluoxetine discontinuation. Concentrations of SSRIs and their metabolites correlated significantly with desipramine concentration changes (for fluoxetine/norfluoxetine, r = 0.94 to 0.96; p &lt; 0.001; for sertraline/desmethylsertraline, r = 0.63; p &lt; 0.01). Thus, sertraline had less pharmacokinetic interaction with desipramine than did fluoxetine at their respective, minimum, usually effective doses.'

## make a correction to the number of participants in an evidence item
## used to support paroxetine increases_auc desipramine
ev.objects['paroxetine_increases_auc_desipramine'].evidence_for[0].value = 5.2
ev.objects['paroxetine_increases_auc_desipramine'].evidence_for[0].quote = 'Route of administration: oral (inferred because IV formulations do not appear to be available for paroxetine and desipramine)\r\n\r\nstudy duration: see below\r\n\r\npopulation: 17 volunteers (design called for 24 but several dropped out or were excluded due to non-compliance); all participants were extensive metabolizers of dextromethorphan (o-demethylation)\r\n\r\nages: mean(std dev): 30.4 (+/-5.2)\r\n\r\nAUC_i/AUC (24 hour): 3305 / 634 = 5.2\r\n\r\nNOTE: AUC increase mentioned is for the phase of the study using 20mg of paroxetine.\r\n\r\nDescription: \r\nThe pharmacokinetics of desipramine when coadministered with the selective serotonin reuptake inhibitors (SSRIs) paroxetine and sertraline were studied in 24 healthy male volunteers (CYP2D6 extensive metabolizers). Desipramine (50 mg/day) was administered for 23 days in each phase of the crossover study with a 7-day drug-free period between phases. In addition, subjects were randomly assigned to receive concomitant paroxetine (20 mg/day on days 8 through 17 followed by 30 mg/day on days 18 through 20) or sertraline (50 mg/day on days 8 through 17 and 100 mg/day on days 18 through 20). SSRI treatments were switched between phases. After 10 days of coadministration at the lower dose, mean desipramine maximum concentration in plasma (Cmax) relative to baseline increased from 37.8 to 173 ng/mL (+358%) with paroxetine versus from 36.1 to 51.9 ng/mL (+44%) with sertraline; the mean desipramine 24-hour area under the concentration-time curve (AUC[24]) increased from 634 to 3,305 ng x h/mL (+421%) with paroxetine versus from 611 to 838 ng x h/mL (+37%) with sertraline; and the mean desipramine trough value (C0) increased from 18.5 to 113 ng/mL (+511%) with paroxetine versus from 18.3 to 21.8 ng/mL (+19%) with sertraline (all increases, p &lt; 0.001). An approximately 10-fold increase in the Cmax and AUC(24) of paroxetine and an approximately 2-fold increase in these parameters for sertraline occurred simultaneously with the desipramine concentration changes. Thus, when coadministered with 50 mg/day desipramine, sertraline had significantly less pharmacokinetic interaction than paroxetine with desipramine at the recommended starting dosages of 50 mg/day and 20 mg/day, respectively.'

## remove the assertion duloxetine inhibits CYP2C19 because it was entered by mistake
ev.deleteAssertion(ev.objects['duloxetine_inhibits_cyp2c19'])

## replace the assumption for and evidence usage supporting paroxetine
## inhibits cyp2d6 with the correct one 
ev.objects['paroxetine_inhibits_cyp2d6'].evidence_for[0].assumptions.delAllEntries()
ev.objects['paroxetine_inhibits_cyp2d6'].evidence_for[0].assumptions.addEntry(['dextromethorphan_primary_total_clearance_enzyme_cyp2d6'])

## add debrisoquin to the DIKB
#d = Drug("debrisoquine")
#dikb.putObject(d)

## remove the default assertion status of the assertion 'debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6'
ev.objects['debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6'].assert_by_default = False

## add 4-hydroxydebrisoquine as a Metabolite
d = Metabolite("4-hydroxydebrisoquine")
dikb.putObject(d)

## add 7-hydroxyperphenazine as a Metabolite
d = Metabolite("7-hydroxyperphenazine")
dikb.putObject(d)


## insert several metabolites not formerly in the system
for i in ["threohydrobupropion", "erythrohydrobupropion", "hydroxybupropion", "M-chlorophenylpiperazine", "norfluoxetine", "N-desmethylsertraline", "demethylcitalopram", "didemethylcitalopram", "N-desalkylquetiapine", "N-desmethylvenlafaxin", "O-desmethylvenlafaxin", "S-demethylcitalopram", "S-didemethylcitalopram", "benzisothiazole-sulphoxide", "benzisothiazole-sulphone", "ziprasidone-sulphoxide", "S-methyl-dihydroziprasidone"]:
    if i in dikb.objects.keys():
        print "%i seems to be present already!"
        continue

    m = Metabolite(i)
    dikb.putObject(m)

## a batch evidence entry dealing with all CYP450s in the system
for elt in ["cyp1a1", "cyp1a2", "cyp1b1", "cyp2a6", "cyp2a13", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2d6", "cyp2e1", "cyp2j2", "cyp3a4", "cyp3a5", "cyp4a11", "cyp4f1"]:
    a = Assertion(elt, "controls_formation_of", "threohydrobupropion")
    e = Evidence(ev)
    e.create(doc_p = "buproprion-XR-actavis-south-atlantic-032008", q = "In vitro findings suggest that cytochrome P450IIB6 (CYP2B6) is the principal isoenzyme involved in the formation of hydroxybupropion, while cytochrome P450 isoenzymes are not involved in the formation of threohydrobupropion.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)


## a batch evidence entry dealing with several CYP450s and ziprasidone
for elt in ["cyp1a2", "cyp2c9", "cyp2c19", "cyp2d6", "cyp3a4"]:
    a = Assertion("ziprasidone", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "ziprasidone-roerig-082008", q = "An in vitro enzyme inhibition study utilizing human liver microsomes showed that ziprasidone had little inhibitory effect on CYP1A2, CYP2C9, CYP2C19, CYP2D6 and CYP3A4, and thus would not likely interfere with the metabolism of drugs primarily metabolized by these enzymes.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)

## a batch evidence entry dealing with several CYP450s and quetiapine
for elt in ["cyp1a2", "cyp2c9", "cyp2c19", "cyp2d6", "cyp3a4"]:
    a = Assertion("quetiapine", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "quetiapine-astra-zeneca-102007", q = "In vitro enzyme inhibition data suggest that quetiapine and 9 of its metabolites would have little inhibitory effect on in vivo metabolism mediated by cytochromes P450 1A2, 2C9, 2C19, 2D6 and 3A4.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)

## a batch evidence entry dealing with several CYP450s and N-desalkylquetiapine
for elt in ["cyp1a2", "cyp2c9", "cyp2c19", "cyp2d6", "cyp3a4"]:
    a = Assertion("N-desalkylquetiapine", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "quetiapine-astra-zeneca-102007", q = "In vitro enzyme inhibition data suggest that quetiapine and 9 of its metabolites would have little inhibitory effect on in vivo metabolism mediated by cytochromes P450 1A2, 2C9, 2C19, 2D6 and 3A4.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)

## a batch evidence entry dealing with several CYP450s and escitalopram
for elt in ["cyp2c19", "cyp2c9", "cyp2e1"]:
    a = Assertion("escitalopram", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "escitalopram-forest-laboratories-032009", q = "in vitro enzyme inhibition data did not reveal an inhibitory effect of escitalopram on CYP3A4, -1A2, -2C9, -2C19, and -2E1. Based on in vitro data, escitalopram would be expected to have little inhibitory effect on in vivo metabolism mediated by these cytochromes.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)


## a batch evidence entry dealing with several CYP450s and citalopram
for elt in ["cyp3a4", "cyp2c9", "cyp2e1"]:
    a = Assertion("citalopram", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "citalopram-teva-102008", q = "In vitro enzyme inhibition data did not reveal an inhibitory effect of citalopram on CYP3A4, -2C9, or -2E1, but did suggest that it is a weak inhibitor of CYP1A2, -2D6, and -2C19. Citalopram would be expected to have little inhibitory effect on in vivo metabolism mediated by these cytochromes. However, in vivo data to address this question are limited.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("against",e)
    ev.addAssertion(a)


## enter multiple metabolites for ziprasidone
for elt in ["benzisothiazole-sulphoxide", "benzisothiazole-sulphone", "ziprasidone-sulphoxide", "S-methyl-dihydroziprasidone"]:
    a = Assertion("ziprasidone", "has_metabolite", elt)
    e = Evidence(ev)
    e.create(doc_p = "ziprasidone-roerig-082008", q = "Metabolism and Elimination\n\nZiprasidone is extensively metabolized after oral administration with only a small amount excreted in the urine (<1%) or feces (<4%) as unchanged drug. Ziprasidone is primarily cleared via three metabolic routes to yield four major circulating metabolites, benzisothiazole (BITP) sulphoxide, BITP-sulphone, ziprasidone sulphoxide, and S-methyl-dihydroziprasidone.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

## enter multiple metabolites for escitalopram
for elt in ["S-demethylcitalopram", "S-didemethylcitalopram"]:
    a = Assertion("escitalopram", "has_metabolite", elt)
    e = Evidence(ev)
    e.create(doc_p = "escitalopram-forest-laboratories-032009", q = "Metabolism and Elimination\n\nFollowing oral administrations of escitalopram, the fraction of drug recovered in the urine as escitalopram and S-demethylcitalopram (S-DCT) is about 8% and 10%, respectively. The oral clearance of escitalopram is 600 mL/min, with approximately 7% of that due to renal clearance.\n\nEscitalopram is metabolized to S-DCT and S-didemethylcitalopram (S-DDCT). In humans, unchanged escitalopram is the predominant compound in plasma. At steady state, the concentration of the escitalopram metabolite S-DCT in plasma is approximately one-third that of escitalopram. The level of S-DDCT was not detectable in most subjects. In vitro studies show that escitalopram is at least 7 and 27 times more potent than S-DCT and S-DDCT, respectively, in the inhibition of serotonin reuptake, suggesting that the metabolites of escitalopram do not contribute significantly to the antidepressant actions of escitalopram. S-DCT and S-DDCT also have no or very low affinity for serotonergic (5-HT1-7) or other receptors including alpha- and beta-adrenergic, dopamine (D1-5), histamine (H1-3), muscarinic (M1-5), and benzodiazepine receptors. S-DCT and S-DDCT also do not bind to various ion channels including Na+, K+, Cl-, and Ca++ channels.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

## enter multiple metabolites for citalopram
for elt in ["demethylcitalopram", "didemethylcitalopram"]:
    a = Assertion("citalopram", "has_metabolite", elt)
    e = Evidence(ev)
    e.create(doc_p = "citalopram-teva-102008", q = "Citalopram is metabolized to demethylcitalopram (DCT), didemethylcitalopram (DDCT), citalopram-N-oxide, and a deaminated propionic acid derivative. In humans, unchanged citalopram is the predominant compound in plasma. At steady state, the concentrations of citalopram's metabolites, DCT and DDCT, in plasma are approximately one-half and one-tenth, respectively, that of the parent drug. In vitro studies show that citalopram is at least 8 times more potent than its metabolites in the inhibition of serotonin reuptake, suggesting that the metabolites evaluated do not likely contribute significantly to the antidepressant actions of citalopram.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

## enter multiple metabolites for buproprion
for elt in ["threohydrobupropion", "erythrohydrobupropion", "hydroxybupropion"]:
    a = Assertion("buproprion", "has_metabolite", elt)
    e = Evidence(ev)
    e.create(doc_p = "buproprion-XR-actavis-south-atlantic-032008", q = "Metabolism: Bupropion is extensively metabolized in humans. Three metabolites have been shown to be active: hydroxybupropion, which is formed via hydroxylation of the tert-butyl group of bupropion, and the amino-alcohol isomers threohydrobupropion and erythrohydrobupropion, which are formed via reduction of the carbonyl group. In vitro findings suggest that cytochrome P450IIB6 (CYP2B6) is the principal isoenzyme involved in the formation of hydroxybupropion, while cytochrome P450 isoenzymes are not involved in the formation of threohydrobupropion. Oxidation of the bupropion side chain results in the formation of a glycine conjugate of meta-chlorobenzoic acid, which is then excreted as the major urinary metabolite. The potency and toxicity of the metabolites relative to bupropion have not been fully characterized. However, it has been demonstrated in an antidepressant screening test in mice that hydroxybupropion is one half as potent as bupropion, while threohydrobupropion and erythrohydrobupropion are 5-fold less potent than bupropion. This may be of clinical importance because the plasma concentrations of the metabolites are as high or higher than those of bupropion.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "05142009")
    a.insertEvidence("for",e)
    ev.addAssertion(a)

## add cimetidine to the DIKB
d = Drug("cimetidine")
dikb.putObject(d)

## correct the doc pointer for some evidence items related to bupropion
ev.objects['buproprion_has_metabolite_erythrohydrobupropion'].evidence_for[0].doc_pointer = 'bupropion-XR-actavis-south-atlantic-032008'
ev.objects['buproprion_has_metabolite_hydroxybupropion'].evidence_for[0].doc_pointer = 'bupropion-XR-actavis-south-atlantic-032008'
ev.objects['buproprion_has_metabolite_threohydrobupropion'].evidence_for[0].doc_pointer = 'bupropion-XR-actavis-south-atlantic-032008'

for elt in ["cyp1a1", "cyp1a2", "cyp1b1", "cyp2a6", "cyp2a13", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2d6", "cyp2e1", "cyp2j2", "cyp3a4", "cyp3a5", "cyp4a11", "cyp4f1"]:
    ev.objects['%s_controls_formation_of_threohydrobupropion' % elt].evidence_against[0].doc_pointer = 'bupropion-XR-actavis-south-atlantic-032008'

for elt in ["cyp1a1", "cyp1a2", "cyp1b1", "cyp2a6", "cyp2a13", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2d6", "cyp2e1", "cyp2j2", "cyp3a4", "cyp3a5", "cyp4a11", "cyp4f1"]:
    print ev.objects['%s_controls_formation_of_threohydrobupropion' % elt].evidence_against[0].doc_pointer

## I forgot to enter the bioavailabity value for fluvoxamine
ev.objects['fluvoxamine_bioavailability_continuous_value'].evidence_for[0].value = "0.53"

## add theophylline to the knowledge-base
d = Drug("theophylline")
dikb.putObject(d)

## remove a redundant evidence item
ev.objects['quetiapine_substrate_of_cyp3a4'].evidence_for.pop()
ev.objects['quetiapine_primary_total_clearance_mechanism_Metabolic_Clearance'].evidence_for.pop()


## add the slots minimum_therapeutic_dose and
## minimum_therapeutic_dose_is_at_least to Drug instances
for k,v in dikb.objects.iteritems():
    if v.__class__ == Drug:
        v.minimum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)
        v.minimum_therapeutic_dose_is_at_least =  EMultiContValSlot(["continuous_value"],["continuous_value"], None)

## test how new slots are exported to the JTMS
for e,v in ev.objects.iteritems():
    v.ready_for_classification = False
ev.objects['diltiazem_minimum_therapeutic_dose_continuous_value'].ready_for_classification = True
ev.objects['diltiazem_minimum_therapeutic_dose_continuous_value'].assert_by_default = True
ev.objects['diltiazem_minimum_therapeutic_dose_is_at_least_continuous_value'].ready_for_classification = True
ev.objects['diltiazem_minimum_therapeutic_dose_is_at_least_continuous_value'].assert_by_default = True
exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

## correct the dose entries for two assertions
ev.objects['diltiazem_minimum_therapeutic_dose_continuous_value'].evidence_for[0].value = "0.120"
ev.objects['diltiazem_minimum_therapeutic_dose_is_at_least_continuous_value'].evidence_for[0].value = "0.120"

## testing a new format for exporting  maximum_concetration assertions to the JTMS
for e,v in ev.objects.iteritems():
    if not v.slot == 'maximum_concentration':
        v.ready_for_classification = False
    else:
        v.ready_for_classification = True

exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

## remove the 'diltiazem_minimum_therapeutic_dose_is_at_least_continuous_value' assertion because these assertion types are no longer entered by curators
ev.deleteAssertion(ev.objects['diltiazem_minimum_therapeutic_dose_is_at_least_continuous_value'])

## remove assertions containing mispelled versions of N-desmethylvenlafaxine and O-desmethylvenlafaxine
ev.deleteAssertion(ev.objects['cyp3a4_controls_formation_of_N-desmethylvenlafaxin'])
ev.deleteAssertion(ev.objects['cyp2d6_controls_formation_of_O-desmethylvenlafaxin'])
ev.deleteAssertion(ev.objects['ketoconazole_increases_auc_O-desmethylvenlafaxin'])
ev.deleteAssertion(ev.objects['venlafaxine_has_metabolite_O-desmethylvenlafaxin'])
ev.deleteAssertion(ev.objects['venlafaxine_has_metabolite_N-desmethylvenlafaxin'])

## add several new metabolites to the DIKB
for i in ["10-N-glucuronide", "9-hydroxyrisperidone", "reduced-haloperidol", "clozapine-N-oxide", "desmethylclozapine", "7-hydroxyclozapine", "quetiapine-sulfoxide", "7-hydroxy-quetiapine", "7-hydroxy-N-desalkyl-quetiapine", "4-(4-chlorophenyl)-4-hydroxypiperidine"]:
    if i in dikb.objects.keys():
        print "%s seems to be present already!" % i
        continue

    m = Metabolite(i)
    dikb.putObject(m)

## apply a single evidence item as rebuttal for multiple inhibits assertions for paliperidone
for elt in ["cyp1a2", "cyp2a6", "cyp2c8", "cyp2c9", "cyp2c10", "cyp2d6", "cyp2e1", "cyp3a4", "cyp3a5"]:
    a = Assertion("paliperidone", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "paliperidone-XR-janssen-122008", q = "Paliperidone is not expected to cause clinically important pharmacokinetic interactions with drugs that are metabolized by cytochrome P450 isozymes. In vitro studies in human liver microsomes showed that paliperidone does not substantially inhibit the metabolism of drugs metabolized by cytochrome P450 isozymes, including CYP1A2, CYP2A6, CYP2C8/9/10, CYP2D6, CYP2E1, CYP3A4, and CYP3A5. Therefore, paliperidone is not expected to inhibit clearance of drugs that are metabolized by these metabolic pathways in a clinically relevant manner. Paliperidone is also not expected to have enzyme inducing properties.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "06102009")
    err = a.insertEvidence("against",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)

## remove an assertion for cyp2c10 since this enzyme is not in our
## list of human drug-matabolizing P450s and it appears to be an
## anachronism from a time when 2c9 genotypes were not well
## established
ev.deleteAssertion(ev.objects["paliperidone_inhibits_cyp2c10"])

## apply a single evidence item as rebuttal for multiple substrate_of assertions for paliperidone
for elt in ["cyp1a2", "cyp2a6", "cyp2c9", "cyp2c19"]:
    a = Assertion("paliperidone", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "paliperidone-XR-janssen-122008", q = "Paliperidone is not a substrate of CYP1A2, CYP2A6, CYP2C9, and CYP2C19, so that an interaction with inhibitors or inducers of these isozymes is unlikely. While in vitro studies indicate that CYP2D6 and CYP3A4 may be minimally involved in paliperidone metabolism, in vivo studies do not show decreased elimination by these isozymes and they contribute to only a small fraction of total body clearance. In vitro studies have shown that paliperidone is a P-gp substrate.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "06102009")
    err = a.insertEvidence("against",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)


## move an evidence item from the evidence-for list of an assertion to
## the evidence-against list
e = ev.objects['cyp2d6_controls_formation_of_desmethylclozapine'].evidence_for[0]
del(ev.objects['cyp2d6_controls_formation_of_desmethylclozapine'].evidence_for[0])
ev.objects['cyp2d6_controls_formation_of_desmethylclozapine'].insertEvidence("against", e, ev)

## add evidence items from a study with rejected usage
## apply a single evidence item as rebuttal for multiple controls_formation_of assertions
a = Assertion("cyp2d6", "controls_formation_of", "4-(4-chlorophenyl)-4-hydroxypiperidine")
e = Evidence(ev)
e.create(doc_p = "9431831", q = "\r\nEnzyme system: human liver microsomes\r\n NADPH added: yes\r\n inhibitor used: quinidine\r\n reaction: haloperidol --> 4-(4-chlorophenyl)-4-hydroxypiperidine\r\n Quote: Ketoconazole was a potent inhibitor of CPHP (4-(4-chlorophenyl)-4-hydroxypiperidine) formation with IC50 values of 0,10, 0,23 and 0,14 micM in microsomes HL-1, HL-6 and HL-9 respectively, wheras sulphaphenazole, furafylline and quinidine showed little inhibition (IC50 > 100micM)", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom_Chem", timestamp = "06/11/2009")

# note: no evidence entry validity checking

#a.evidence_against.append(e)
#ev.addAssertion(a)


a = Assertion("cyp1a2", "controls_formation_of", "4-(4-chlorophenyl)-4-hydroxypiperidine")
e = Evidence(ev)
e.create(doc_p = "9431831", q = "\r\nEnzyme system: human liver microsomes\r\n NADPH added: yes\r\n inhibitor used: furafylline\r\n reaction: haloperidol --> 4-(4-chlorophenyl)-4-hydroxypiperidine\r\n Quote: Ketoconazole was a potent inhibitor of CPHP (4-(4-chlorophenyl)-4-hydroxypiperidine) formation with IC50 values of 0,10, 0,23 and 0,14 micM in microsomes HL-1, HL-6 and HL-9 respectively, wheras sulphaphenazole, furafylline and quinidine showed little inhibition (IC50 > 100micM)", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom_Chem", timestamp = "06/11/2009")

# note: no evidence entry validity checking

#a.evidence_against.append(e)
#ev.addAssertion(a)

a = Assertion("cyp2c9", "controls_formation_of", "4-(4-chlorophenyl)-4-hydroxypiperidine")
e = Evidence(ev)
e.create(doc_p = "9431831", q = "\r\nEnzyme system: human liver microsomes\r\n NADPH added: yes\r\n inhibitor used: sulphaphenazole\r\n reaction: haloperidol --> 4-(4-chlorophenyl)-4-hydroxypiperidine\r\n Quote: Ketoconazole was a potent inhibitor of CPHP (4-(4-chlorophenyl)-4-hydroxypiperidine) formation with IC50 values of 0,10, 0,23 and 0,14 micM in microsomes HL-1, HL-6 and HL-9 respectively, wheras sulphaphenazole, furafylline and quinidine showed little inhibition (IC50 > 100micM)", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom_Chem", timestamp = "06/11/2009")

# note: no evidence entry validity checking

#a.evidence_against.append(e)
#ev.addAssertion(a)


## START OF CITALOPRAM KNOWLEGE EDITING

# (DIKB NOTE) Citalopram is an interesting drug because it is racemic
# and and there are some significant differences between the R- and S-
# enantiomers of the drug. This means that we need to distinguish the
# enantiomers from the racemic drug in the knowledge-base. Going so far
# as to remove the racemic drug since it is no longer a pure "active
# ingredient" might be excessive because clinicians prescibe the racemic
# form and there are many shared PK properties between the
# enantiomers. So, the logical model for managing enantiomers in the
# DIKB will be as follows:

# a) Enter into the system the racemic active ingredient and each of
#   its metabolites. If there are PK differences between the
#   enantiomers of the metabolites, then enter both the racemic
#   metabolite and each enantiomer of the metabolite specifically. For
#   example, this rule would cause the following entries for
#   citalopram: citalopram (racemic), R-citalopram, escitalopram (the
#   NDF-RT name for S-citalopram), R-demethylcitalopram,
#   R-didemethylcitalopram, S-demethylcitalopram,
#   S-didemethylcitalopram.

# b) If evidence is not specific to an enantiomer, enter it as evidence
# for the racemic formulation.

# c) If evidence is specific to an enantiomer, enter it as evidence both
# for the specific enantiomer and the recemic compound. This will cause
# inference on the racemic compound to include known PK attributes of
# its enantiomer constituants while allowing specific inference on each
# enantiomer.
for e,v in ev.objects.iteritems():
    if v.object == "citalopram" or v.value == "citalopram":
        print e
    
    if v.object == "escitalopram" or v.value == "escitalopram":
        print e

## CURRENT RACEMIC CITALOPRAM ASSERTIONS
# citalopram_bioavailability_continuous_value (racemic only)
# citalopram_has_metabolite_demethylcitalopram (racemic only)
# citalopram_has_metabolite_didemethylcitalopram (racemic only)
# citalopram_inhibits_cyp2c9 (against) (racemic and enantiomer)
# citalopram_inhibits_cyp2e1 (against) (racemic and enantiomer)
# citalopram_inhibits_cyp3a4 (against) (racemic and enantiomer)
# citalopram_primary_total_clearance_mechanism_Metabolic_Clearance (racemic only)
# citalopram_substrate_of_cyp2c19 (for) (racemic and enantiomer)

## CURRENT S-CITALOPRAM ASSERTIONS
# escitalopram_bioavailability_continuous_value (enantiomer only)
# escitalopram_has_metabolite_S-demethylcitalopram (enantiomer only)
# escitalopram_has_metabolite_S-didemethylcitalopram (enantiomer only)
# escitalopram_inhibits_cyp2c19 (against)
# escitalopram_inhibits_cyp2c9 (against)
# escitalopram_inhibits_cyp2d6 (against)
# escitalopram_inhibits_cyp2e1 (against)
# escitalopram_inhibits_cyp3a4 (against)
# escitalopram_primary_total_clearance_mechanism_Metabolic_Clearance (enantiomer only)
# escitalopram_substrate_of_cyp2c19  (for) (racemic and enantiomer)

## All assertion's that need to be copied from the racemic object's
## attributes and evidence to the enantiomer's or vice versa are
## already taken care of. 

# add the R- enantiomers of citalopram and its metabolites to the DIKB
d = Drug("R-citalopram")
dikb.putObject(d)

d = Metabolite("R-demethylcitalopram")
dikb.putObject(d)

d = Metabolite("R-didemethylcitalopram")
dikb.putObject(d)

## these assertions apply to R-citalopram and have been entered using the web interface: 
# R-citalopram_inhibits_cyp2c9 (against) (racemic and enantiomer)
# R-citalopram_inhibits_cyp2e1 (against) (racemic and enantiomer)
# R-citalopram_inhibits_cyp3a4 (against) (racemic and enantiomer)
# R-citalopram_substrate_of_cyp2c19 (for) (racemic and enantiomer)

## these assertions are NOT to be entered because they would confuse
## the semantics of the has_metabolite assertion type
# citalopram_has_metabolite_R-demethylcitalopram
# citalopram_has_metabolite_S-demethylcitalopram
# citalopram_has_metabolite_R-didemethylcitalopram
# citalopram_has_metabolite_S-didemethylcitalopram

## END OF CITALOPRAM KNOWLEGE EDITING

## add tolbutamide to the knowledge-base
d = Drug("tolbutamide")
dikb.putObject(d)

## add mephenytoin and S-mephenytoin to the KB
d = Drug("mephenytoin")
dikb.putObject(d)

m = Metabolite("S-mephenytoin")
dikb.putObject(m)

## edit the quote line of a few different assertions
ev.objects['R-citalopram_inhibits_cyp1a2'].evidence_against[0].quote = '\r\nEnzyme system: human liver microsomes\r\n\r\nNADPH added: yes (a dehydrogenase generating system)\r\n\r\nprobe reaction: phenacetin O-deethylation\r\n\r\nQuote: \r\n\r\nIn all systems the positive control inhibitors produced the expected degree of inhibition of their respective index reactions (Table 1). CYP1A2. R- and S-CT and metabolites all were negligible inhibitors\r\nof phenacetin O-deethylation, the index reaction for CYP1A2. None of these compounds produced 50% inhibition. The mean IC50 for alpha-naphthoflavone was 0.2micM, and the mean IC50 for fluvoxamine was 0.3micM.\r\n\r\n\r\n'
ev.objects['escitalopram_inhibits_cyp1a2'].evidence_against[0].quote = '\r\nEnzyme system: human liver microsomes\r\n\r\nNADPH added: yes (a dehydrogenase generating system)\r\n\r\nprobe reaction: phenacetin O-deethylation\r\n\r\nQuote: \r\n\r\nIn all systems the positive control inhibitors produced the expected degree of inhibition of their respective index reactions (Table 1). CYP1A2. R- and S-CT and metabolites all were negligible inhibitors\r\nof phenacetin O-deethylation, the index reaction for CYP1A2. None of these compounds produced 50% inhibition. The mean IC50 for alpha-naphthoflavone was 0.2micM, and the mean IC50 for fluvoxamine was 0.3micM.\r\n\r\n\r\n'
ev.objects['citalopram_inhibits_cyp1a2'].evidence_against[0].quote = '\r\nEnzyme system: human liver microsomes\r\n\r\nNADPH added: yes (a dehydrogenase generating system)\r\n\r\nprobe reaction: phenacetin O-deethylation\r\n\r\nQuote: \r\n\r\nIn all systems the positive control inhibitors produced the expected degree of inhibition of their respective index reactions (Table 1). CYP1A2. R- and S-CT and metabolites all were negligible inhibitors\r\nof phenacetin O-deethylation, the index reaction for CYP1A2. None of these compounds produced 50% inhibition. The mean IC50 for alpha-naphthoflavone was 0.2micM, and the mean IC50 for fluvoxamine was 0.3micM.\r\n\r\n\r\n'

## correct a doubly-entered evidence item
ev.objects['S-demethylcitalopram_inhibits_cyp1a2'].evidence_against.pop() 

## correct quote entries for a couple of assertions
ev.objects['R-citalopram_maximum_concentration_continuous_value'].evidence_for[0].quote = 'Route of administration: oral\r\n\r\nstudy duration: rac-citalopram given @ 40mg qd X 21days\r\n\r\npopulation: 10 adults (6 female and 4 male) all extensive metabolizers according to 2d6 and 2c19 specific assays (sparteine and mephenytoin respectively)\r\n\r\nages: 23-32\r\n\r\n\r\nDescription: \r\nC_max for R-citalopram : 228.4nMol/L\r\n\r\n228.4nMol/L X 1M/10^9nMol X 324.39g/1M = 0.00007409g/L'
ev.objects['escitalopram_maximum_concentration_continuous_value'].evidence_for.pop()


## add assumptions to certain evidence entries that were lacking them
ev.objects['cyp2d6_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].assumptions.addEntry(['quinidine_in_vitro_selective_inhibitor_of_enzyme_cyp2d6'])
ev.objects['cyp1a2_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].assumptions.addEntry(['furafylline_in_vitro_selective_inhibitor_of_enzyme_cyp1a2'])
ev.objects['cyp2c9_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].assumptions.addEntry(['sulphaphenazole_in_vitro_selective_inhibitor_of_enzyme_cyp2c9'])

## fix a document reference
ev.objects['sertraline_increases_auc_clozapine'].evidence_against[0].doc_pointer = "11147928" 

## remove certain evidence from the system
ev.objects['cyp2d6_controls_formation_of_clozapine-N-oxide'].evidence_against.pop()
ev.objects['cyp2d6_controls_formation_of_desmethylclozapine'].evidence_against.pop()

## add sulfinpyrazone to the DIKB
d = Drug("sulfinpyrazone")
dikb.putObject(d)

## correct the evidence type assignment for several entries
ev.objects['venlafaxine_has_metabolite_N-desmethylvenlafaxine'].evidence_for[1].evidence_type.putEntry('EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome')
ev.objects['venlafaxine_has_metabolite_O-desmethylvenlafaxine'].evidence_for[1].evidence_type.putEntry('EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome')

ev.objects['cyp1a2_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].evidence_type.putEntry('EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem')
ev.objects['cyp2c9_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].evidence_type.putEntry('EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem')
ev.objects['cyp2d6_controls_formation_of_4-(4-chlorophenyl)-4-hydroxypiperidine'].evidence_against[0].evidence_type.putEntry('EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem')

## add an assertion with no evidence to the knowledge-base
a = Assertion("erythromycin", "in_viVo_selective_inhibitor_of_enzyme", "cyp3a4")
ev.addAssertion(a)

## add sparteine to the knowledge-base 
c = Chemical("sparteine")
dikb.putObject(c)

## add the slot in_viVo_probe_substrate_of_enzyme to the DIKB
for k,v in dikb.objects.iteritems():
    if type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__()):
        v.in_viVo_probe_substrate_of_enzyme  = ESlot(v.enzymes  + ["none_assigned"],"none_assigned")

## revise the assumption slot for a few different assertions
ev.objects['fluoxetine_inhibits_cyp2d6'].evidence_for[0].assumptions.value = ['dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6']
ev.objects['paroxetine_inhibits_cyp2d6'].evidence_for[0].assumptions.value = ['dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6']
ev.objects['sertraline_inhibits_cyp2d6'].evidence_for[1].assumptions.value = ['dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6']

ev.objects['fluoxetine_inhibits_cyp2d6'].evidence_for[2].assumptions.value = ['dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6']
ev.objects['paroxetine_inhibits_cyp2d6'].evidence_for[2].assumptions.value = ['dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6']

## add an assertion about sparteine with no evidence support
a = Assertion("sparteine", "in_viVo_probe_substrate_of_enzyme", "cyp2d6")
ev.addAssertion(a)

## add a spartiene assumption where needed
ev.objects['paroxetine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6'].evidence_for[1].assumptions.value = ['desipramine_primary_total_clearance_enzyme_cyp2d6', 'sparteine_in_viVo_probe_substrate_of_enzyme_cyp2d6']
ev.objects['paroxetine_inhibits_cyp2d6'].evidence_for[4].assumptions.value = ['desipramine_primary_total_clearance_enzyme_cyp2d6', 'sparteine_in_viVo_probe_substrate_of_enzyme_cyp2d6']

## revise citalopram and enantiomer evidence entries to fit the
## guidelines written in our inclusion criteria document
ev.objects['R-citalopram_inhibits_cyp2c9'].evidence_against.pop(0)
ev.objects['R-citalopram_inhibits_cyp2e1'].evidence_against.pop(0)
ev.objects['R-citalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['R-citalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['R-citalopram_maximum_concentration_continuous_value'].evidence_for.pop(0)
ev.objects['R-citalopram_primary_total_clearance_mechanism_Renal_Excretion'].evidence_against.pop(0)
ev.objects['R-citalopram_substrate_of_cyp2c19'].evidence_for.pop(0)
ev.objects['R-citalopram_substrate_of_cyp3a4'].evidence_against.pop(0)
ev.objects['escitalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['escitalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['escitalopram_substrate_of_cyp3a4'].evidence_against.pop(0)
ev.objects['citalopram_inhibits_cyp1a2'].evidence_against.pop(0)
ev.objects['citalopram_inhibits_cyp2c19'].evidence_against.pop(0)
ev.objects['citalopram_inhibits_cyp2c9'].evidence_against.pop(1)
ev.objects['citalopram_inhibits_cyp2d6'].evidence_against.pop(0)
ev.objects['citalopram_substrate_of_cyp2c19'].evidence_for.pop(1)
ev.objects['citalopram_substrate_of_cyp3a4'].evidence_for.pop(0)

ev.objects['demethylcitalopram_inhibits_cyp1a2'].evidence_against.pop(0)
ev.objects['demethylcitalopram_inhibits_cyp2d6'].evidence_against.pop(0)
ev.objects['demethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)

ev.objects['R-demethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['R-didemethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)

ev.objects['S-demethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)
ev.objects['S-didemethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)

ev.objects['demethylcitalopram_substrate_of_cyp2d6'].evidence_for.pop(0)

ev.objects['R-demethylcitalopram_substrate_of_cyp2c19'].evidence_against.pop(0)
ev.objects['R-demethylcitalopram_substrate_of_cyp3a4'].evidence_against.pop(0)

ev.objects['S-demethylcitalopram_substrate_of_cyp2c19'].evidence_against.pop(0)
ev.objects['S-demethylcitalopram_substrate_of_cyp3a4'].evidence_against.pop(0)

ev.objects['didemethylcitalopram_inhibits_cyp1a2'].evidence_against.pop(0)
ev.objects['didemethylcitalopram_inhibits_cyp2d6'].evidence_against.pop(0)
ev.objects['didemethylcitalopram_inhibits_cyp3a4'].evidence_against.pop(0)

## add a new chemical and a new metabolite
c = Chemical("7-ethoxyresorufin")
dikb.putObject(c)

m = Metabolite("thioridazine-5-sulfoxide")
dikb.putObject(m)

## add an assertion about 7-ethoxyresorufin
a = Assertion('7-ethoxyresorufin', 'in_vitro_probe_substrate_of_enzyme', 'cyp1a2')
a.assert_by_default = True
## apply a single evidence item as rebuttal for multiple in_vitro_probe_substrate_of_enzyme assertions
for elt in ["cyp1a2"]:
	e = Evidence(ev)
	e.create(doc_p = "fda2006a", q = "The FDA recommends 7-ethoxyresorufin to be an acceptable chemical CYP1A2 substrate (7-ethoxyresorufin O-deethylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "06/19/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## replace mis-spelled metabolites with correctly-spelled ones
dikb.objects.pop('O-desmethylvenlafaxin')
dikb.objects.pop('N-desmethylvenlafaxin')

m = Metabolite("N-desmethylvenlafaxine")
dikb.putObject(m)

m = Metabolite("O-desmethylvenlafaxine")
dikb.putObject(m)

## delete numerous incorrect venlafaxine evidence items so that they
## can be re-entered through the web interface
ev.objects['venlafaxine_maximum_concentration_continuous_value'].evidence_for.pop(0)
ev.objects['venlafaxine_maximum_concentration_continuous_value'].evidence_for.pop(0)
ev.objects['venlafaxine_maximum_concentration_continuous_value'].evidence_for.pop(0)
ev.objects['O-desmethylvenlafaxine_maximum_concentration_continuous_value'].evidence_for.pop(0)
ev.objects['O-desmethylvenlafaxine_maximum_concentration_continuous_value'].evidence_for.pop(0)

ev.objects['venlafaxine_maximum_concentration_continuous_value'].evidence_for[1].quote = '\r\n\r\nroute of administration: oral\r\n\r\nstudy duration: &quot;The study was a randomized three-period cross-over design using a pair of Latin squares.  Each sub-ject participated for three 5-day venlafaxine treatment periods separated by a 9-day drug-free interval.  Each treatment period consisted of 25, 75, or 150mg of venlafaxine given as a single dose on day 1, followed by the same dose given every 8 hours (q8h) on days 2 to 4, and ending with a single dose given on day 5, for a total of 2 doses. All doses were administered after food as multiple tablets of 25 mg venlafaxine base. The single doses on days 1 and 5 were administered 30 minutes after the subject had eaten a medium-fat breakfast and were followed by a 4-hour fast.&quot;\r\n\r\npopulation: 18, non-smoking, healthy men, NOTE: none were tested for known CYP450 phenotypes \r\n\r\nages: 20 - 34\r\n\r\nC_max (day 4) @ 225mg/day venlafaxine: 167ng/mL\r\n\r\n167ng/mL X 1g/10^9ng X 1000mL/1L = 0.000167g/L\r\n'

## some minor corrections
ev.objects['ziprasidone_substrate_of_cyp1a2'].evidence_for[0].quote = '\r\nEnzyme system: human liver microsomes\r\n\r\nNADPH added: yes\r\n\r\ninhibitor used: furafylline\r\n\r\nreaction: 1) ziprasidone --&gt; ziprasidone sulphoxide/sulphone\r\n2) ziprasidone --&gt; oxindole acetic acid\r\n\r\nQuote:\r\nInhibition of metabolite formation by each inhibitor is\r\nsummarized in Table 2. Ketoconazole (10micM) inhibited\r\nthe formation of ziprasidone sulphoxide (sulphoxide and\r\nsulphone) by 79% and oxindole acetic acid N-dealkylated\r\nproduct) completely. Sulphaphenazole an furafylline did\r\nnot inhibit the formation of ziprasidone sulphoxide. The formation of oxindole acetic acid was inhibited (~50%) by furafylline. The formation of ziprasidone metabolites was not inhibited by quinidine but rather increased. '

ev.objects['ziprasidone_substrate_of_cyp3a4'].evidence_for[1].quote = '\r\n\r\nEnzyme system: For CYP1A2 - recombinant CYP450 enzymes expressed in an human lymphoblastoid cell system. For CYP2C9, 2C19,2D6, and 3A4 - recombinant CYP450 enzymes expressed in insect cells\r\n\r\nNADPH added: yes\r\n\r\nreaction: 1) ziprasidone --&gt; ziprasidone sulphoxide \r\n          2) ziprasidone --&gt; ziprasidone sulphone \r\n\r\nQuote: \r\n&quot;The ability of specific CYP isoforms to metabolize\r\nziprasidone was determined using recombinant CYP1A2, CYP2C9, CYP2C19, CYP2D6 and CYP3A4. H.p.l.c.-radioactivity profiles of ziprasidone metabolites following incubation of [14C]-ziprasidone or [3H]-ziprasidone with CYP3A4 are shown in Figure 5(a) and (b), respectively. CYP3A4 catalysed the formation of the N-dealkylated metabolite (M5), as well as ziprasidone sulphone (M8) and ziprasidone sulphoxide (M10). These oxidative metabolites were not detected in incubations containing recombinant CYP1A2, CYP2C9, CYP2C19 or CYP2D6.&quot;\r\n\r\n'

ev.objects['cyp3a4_controls_formation_of_ziprasidone-sulphoxide'].evidence_for[0].quote = '\r\n\r\nEnzyme system: For CYP1A2 - recombinant CYP450 enzymes expressed in an human lymphoblastoid cell system. For CYP2C9, 2C19,2D6, and 3A4 - recombinant CYP450 enzymes expressed in insect cells\r\n\r\nNADPH added: yes\r\n\r\nreaction: 1) ziprasidone --&gt; ziprasidone sulphoxide \r\n          2) ziprasidone --&gt; ziprasidone sulphone \r\n\r\nQuote: \r\n&quot;The ability of specific CYP isoforms to metabolize\r\nziprasidone was determined using recombinant CYP1A2, CYP2C9, CYP2C19, CYP2D6 and CYP3A4. H.p.l.c.-radioactivity profiles of ziprasidone metabolites following incubation of [14C]-ziprasidone or [3H]-ziprasidone with CYP3A4 are shown in Figure 5(a) and (b), respectively. CYP3A4 catalysed the formation of the N-dealkylated metabolite (M5), as well as ziprasidone sulphone (M8) and ziprasidone sulphoxide (M10). These oxidative metabolites were not detected in incubations containing recombinant CYP1A2, CYP2C9, CYP2C19 or CYP2D6.&quot;\r\n\r\n'


## remove the default assumption status of an assertion
ev.objects['paroxetine_in_vitro_selective_inhibitor_of_enzyme_cyp2d6'].assert_by_default = False

## edit the quote assigned to an evidence item
ev.objects['venlafaxine_substrate_of_cyp3a4'].evidence_for[0].quote = '\r\nEnzyme system: human liver microsomes:\r\n\r\nNADPH added: yes\r\n\r\ninhibitor used: ketoconazole\r\n\r\nreaction: venlafaxine --&gt; N-desmethylvenlafaxine\r\n\r\nNOTE: the concentration of venlafaxine used in this experiment is very high relative to that expected in clinical use of the drug\r\n\r\nQuote: \r\n&quot;Formation of NDV had a mean Vmax of 2.14 nmol min mg protein, and a mean Km of 2504 M (Table 2). Incubations of 750micM VF with SFZ and QUI led to 18% and 23% reduction in NDV production respectively, while increasing concentrations of ANA led to an 11% increase in NDV formation over baseline. KET [ketoconazole] had a more profound effect on NDV formation, leading to a 65% mean reduction in production of this metabolite (Figure 5).&quot;'

ev.objects['bupropion_maximum_concentration_continuous_value'].evidence_for[1].quote = '\r\n\r\nroute of administration: oral\r\n\r\nstudy duration: &quot;On the morning of day I after an overnight fast, all of the volunteers ingested a single 150-mg bupropion sustained-release tablet with a glass of water.  Nineteen blood samples were collected from each volunteer, 1 immediately before and 18 during the 72 hours after administration (i.e., 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 24, 36, 48, 60, and 72 hours). On day 2, after the 24-hour postadministration assessment, all of the volunteers were released from the research unit, signifying the start of the outpatient period of the treatment phase.  During this period, volunteers returned to the research unit at scheduled times for blood draws.  Smokers were permitted to smoke cigarettes ad libitum during the study; in contrast, nonsmokers were required to refrain from smoking or using any tobacco products.&quot;\r\n\r\npopulation: 34 adults, 17 smokers (9 males/8 females) and 17 non-smokers (9 males/8 females)\r\n\r\ntested for known CYP450 polymorphisms? NO\r\n\r\nages: smokers - 26.7 SD:4.9; non-smokers - 25.7 SD:5.8\r\n\r\nNOTE: &quot;No clinically significant differences between smokers and nonsmokers or between male and female volunteers were observed for the pharmacokinetics of bupropion or its metabolites.&quot;\r\n\r\nC_max single-dose of 150mg EXTENDED RELEASE bupropion: 144ng/mL (the arithmetic average of C_max values for smokers and non-smokers)\r\n\r\n144ng/mL X 1g/10^9ng X 1000mL/1L = 0.000144g/L\r\n'

## fix an incorrectly entered dose value
ev.objects['ziprasidone_maximum_concentration_continuous_value'].evidence_for[4].dose = '0.040'

## edit a quote
ev.objects['hydroxybupropion_maximum_concentration_continuous_value'].evidence_for[1].quote = '\r\nroute of administration: oral (parent drug)\r\n\r\nstudy duration: Plasma profiles were obtained: 1) after a single 100 mg oral dose of [NON-XR] bupropion hydrochloride, 2) following administration of 100 mg 8-hourly for 14 days and 3) again after a single 100 mg dose 14 days later.\r\n\r\npopulation: 8 healthy, non-smoking, male subjects\r\n\r\ntested for known CYP450 polymorphisms? NO\r\n\r\nages: 22 - 42\r\n\r\nC_max of HYDROXYBUPROPION @ 300mg/day of NON-XR bupropion for 14 days: 4.2micM/L (OCCASION 2, Table 2, 306U)\r\n\r\n4.2micM/1L X 1M/10^6micM X 256.749g/1M = 0.001g/L\r\n'

## add bufuralol to the DIKB
c = Chemical("bufuralol")
dikb.putObject(c)

a = Assertion('bufuralol', 'in_vitro_probe_substrate_of_enzyme', 'cyp2d6')
a.assert_by_default = True
## apply a single evidence item as rebuttal for multiple in_vitro_probe_substrate_of_enzyme assertions
for elt in ["cyp2d6"]:
	e = Evidence(ev)
	e.create(doc_p = "fda2006a", q = "The FDA recommends bufuralol to be an acceptable chemical CYP2D6 substrate (bufuralol 1'-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "06/22/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)


## add all suspected inhibitors based on Horn's Top 100 and Flockhart's tables to the DIKB
si_l = ["amiodarone", "amprenavir", "aprepitant", "artemisinin", "atazanavir", "basiliximab", "bupropion", "capecitabine", "celecoxib", "chloramphenicol", "chloroquine", "chlorpheniramine", "chlorpromazine", "cimetidine", "cinacalcet", "ciprofloxacin", "citalopram", "clarithromycin", "clomipramine", "clopidogrel", "clotrimazole", "conivaptan", "cotrimoxazole", "cyclophosphamide", "cyclosporine", "danazol", "darunavir", "dasatinib", "delavirdine", "diltiazem", "diphenhydramine", "disulfiram", "doxifluridine", "doxorubicin", "duloxetine", "efavirenz", "erythromycin", "escitalopram", "ethanol", "ethynil-estradiol", "felbamate", "flecainide", "fluconazole", "fluorouracil", "fluoxetine", "fluvastatin", "fluvoxamine", "fosamprenavir", "gemfibrozil", "halofantrine", "haloperidol", "hydroxychloroquine", "imatinib", "indinavir", "indomethacin", "interferon", "interleukin-10", "isoniazid", "itraconazole", "ketoconazole", "lansoprazole", "lapatinib", "leflunomide", "methadone", "methoxsalen", "metronidazole", "mexiletine", "miconazole", "midodrine", "mifepristone", "moclobemide", "modafinil", "montelukast", "nefazodone", "nelfinavir", "nicardipine", "nilotinib", "norfloxacin", "omeprazole", "oxcarbazepine", "oxycarbazepine", "pantoprazole", "paroxetine", "perphenazine", "phenytoin", "pioglitazone", "posaconazole", "probenicid", "promethazine", "propafenone", "propoxyphene", "quinidine", "quinine", "quinupristin", "rabeprazole", "ranolazine", "risperidone", "ritonavir", "rosiglitazone", "saquinavir", "sertraline", "sitaxsentan", "sulfamethizole", "sulfamethoxazole", "sulfinpyrazone", "sulphaphenazole", "tacrine", "tamoxifen", "telithromycin", "teniposide", "terbinafine", "thiabendazole", "thioridazine", "thiotepa", "ticlopidine", "topiramate", "trimethoprim", "troleandomycin", "valproate", "verapamil", "voriconazole", "zafirlukast", "zileuton"]
for i in si_l:
    if i in dikb.objects.keys():
        print "%s seems to be present already!" % i
        continue
    
    d = Drug(i)
    dikb.putObject(d)

# DIKB: warning: Cannot accept artemisinin as identifier, possible values are:
# DIKB: warning: Cannot accept conivaptan as identifier, possible values are:
# DIKB: warning: Cannot accept cyclophosphamide as identifier, possible values are:
# DIKB: warning: Cannot accept darunavir as identifier, possible values are:
# DIKB: warning: Cannot accept doxifluridine as identifier, possible values are:
# DIKB: warning: Cannot accept ethynil-estradiol as identifier, possible values are:
# DIKB: warning: Cannot accept halofantrine as identifier, possible values are:
# DIKB: warning: Cannot accept interferon as identifier, possible values are:
# DIKB: warning: Cannot accept interleukin-10 as identifier, possible values are:
# DIKB: warning: Cannot accept moclobemide as identifier, possible values are:
# DIKB: warning: Cannot accept probenicid as identifier, possible values are:
# DIKB: warning: Cannot accept sitaxsentan as identifier, possible values are:

## get all drug objects in the DIKB
for e,v in dikb.objects.iteritems():
    if type(v) == Drug:
        print e

## fix a quote 
ev.objects['atazanavir_inhibits_cyp3a4'].evidence_for[0].quote = 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'


## apply a single evidence item as rebuttal for multiple inhibits assertions for topiramate
for elt in ["cyp1a2", "cyp2a6", "cyp2b6", "cyp2c9", "cyp2c19", "cyp2d6", "cyp2e1", "cyp3a4", "cyp3a5"]:
    a = Assertion("topiramate", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "topiramate-invagen-042009", q = "In vitro studies indicate that topiramate does not inhibit enzyme activity for CYP1A2, CYP2A6, CYP2B6, CYP2C9, CYP2C19, CYP2D6, CYP2E1 and CYP3A4/5 isozymes.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "09212009")
    err = a.insertEvidence("against",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)


## apply a single evidence item as rebuttal for multiple inhibits assertions for cinacalcet
for elt in ["cyp1a2", "cyp2c9", "cyp2c19",  "cyp3a4"]:
    a = Assertion("cinacalcet", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "cinacalcet-amgen-122008", q = "Drug Interactions\n...\nAn in vitro study indicates that cinacalcet is a strong inhibitor of CYP2D6, but not of CYP1A2, CYP2C9, CYP2C19, and CYP3A4.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "09212009")
    err = a.insertEvidence("against",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)


## apply a single evidence item as rebuttal for multiple inhibits assertions for celecoxib
for elt in ["cyp2c9", "cyp2c19",  "cyp3a4"]:
    a = Assertion("celecoxib", "inhibits", elt)
    e = Evidence(ev)
    e.create(doc_p = "celecoxib-pfizer-012009", q = "Drug interactions:\n\nIn vitro studies indicate that celecoxib is not an inhibitor of cytochrome P450 2C9, 2C19 or 3A4.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "09212009")
    err = a.insertEvidence("against",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)

## add coumarin to the knowledge-base 
c = Chemical("coumarin")
dikb.putObject(c)

## add an assertion about coumarin
a = Assertion("coumarin", "in_vitro_probe_substrate_of_enzyme", "cyp2a6")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "fda2006a", q = "The FDA recommends coumarin to be an acceptable chemical CYP2A6 substrate (coumarin 7-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "09/22/2009")
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
    ev.addAssertion(a)



## add p-nitrophenol to the knowledge-base 
c = Chemical("p-nitrophenol")
dikb.putObject(c)

a = Assertion("p-nitrophenol", "in_vitro_probe_substrate_of_enzyme", "cyp2e1")
a.assert_by_default = True
e = Evidence(ev)
e.create(doc_p = "fda2006a", q = "The FDA recommends p-nitrophenol to be an acceptable chemical CYP2E1 substrate (p-nitrophenol 3-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "09/22/2009")
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
    ev.addAssertion(a)


## add R- and S-warfarin to the knowledge-base 
c = Drug("R-warfarin")
dikb.putObject(c)

## add two assertions about R-warfarin with no evidence support
a = Assertion("R-warfarin", "in_vitro_probe_substrate_of_enzyme", "cyp1a2")
ev.addAssertion(a)

a = Assertion("R-warfarin", "in_vitro_probe_substrate_of_enzyme", "cyp3a4")
ev.addAssertion(a)

c = Drug("S-warfarin")
dikb.putObject(c)

## add chlorzoxazone to the knowledge base
c = Drug("chlorzoxazone")
dikb.putObject(c)

## move an evidence item for to be an evidence item against
e = ev.objects['topiramate_inhibits_cyp1a2'].evidence_for[0]
del(ev.objects['topiramate_inhibits_cyp1a2'].evidence_for[0])
ev.objects['topiramate_inhibits_cyp1a2'].insertEvidence("against", e, ev)

## add some missing information to an evidence item
ev.objects["sertraline_increases_auc_zolpidem"].evidence_against[0].numb_subj = "27"
ev.objects["sertraline_increases_auc_zolpidem"].evidence_against[0].object_dose = "0.010"
ev.objects["sertraline_increases_auc_zolpidem"].evidence_against[0].precip_dose = "0.050"

## add eszopiclone, zolpidem, and zaleplon to the DIKB
c = Drug("eszopiclone")
dikb.putObject(c)

c = Drug("zolpidem")
dikb.putObject(c)

c = Drug("zaleplon")
dikb.putObject(c)

## correct a document pointer 
ev.objects["eszopiclone_substrate_of_cyp3a4"].evidence_for[0].doc_pointer = 'eszoplicone-sepracor-052008'

## remove an evidence item
ev.objects["eszopiclone_substrate_of_cyp2e1"].evidence_for.pop()

## added two of eszoplicone's metabolites to the DIKB
c = Metabolite("S-zopiclone-N-oxide")
dikb.putObject(c)

c = Metabolite("S-N-desmethylzopiclone")
dikb.putObject(c)

## apply a single evidence item as support for multiple substrate_of assertions for cinacalcet
for elt in ["cyp3a4", "cyp2d6", "cyp1a2"]:
    a = Assertion("cinacalcet", "substrate_of", elt)
    e = Evidence(ev)
    e.create(doc_p = "cinacalcet-amgen-122008", q = "\nMetabolism and Excretion\n\nCinacalcet is metabolized by multiple enzymes, primarily CYP3A4, CYP2D6 and CYP1A2.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "009242009")
    err = a.insertEvidence("for",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)


## added two of atomoxetine's metabolites to the DIKB
c = Metabolite("4-hydroxyatomoxetine")
dikb.putObject(c)

c = Metabolite("N-desmethylatomoxetine")
dikb.putObject(c)

## move an evidence item for atomoxetine to support a different assertion
e = ev.objects["atomoxetine_primary_metabolic_clearance_enzyme_cyp2d6"].evidence_for.pop()
ev.objects["atomoxetine_primary_total_clearance_enzyme_cyp2d6"].insertEvidence("for",e)
ev.deleteAssertion(ev.objects["atomoxetine_primary_metabolic_clearance_enzyme_cyp2d6"])

## delete an assertion; this will be entered correctly using the web interface
ev.deleteAssertion(ev.objects["tolbutamide_primary_metabolic_clearance_enzyme_cyp2c9"])

## add a metabolite for leflunomide
c = Metabolite("teriflunomide")
dikb.putObject(c)

## tell the KB the leflunomide is a prodrug
dikb.objects["leflunomide"].prodrug.putEntry("True")

## add  metabolites for cinacalcet
c = Metabolite("hydrocinnamic-acid")
dikb.putObject(c)

c = Metabolite("hydroxy-hydrocinnamic-acid")
dikb.putObject(c)

## add a metabolite for modafinil
c = Metabolite("modafinil-sulfone")
dikb.putObject(c)

## add a metabolite for midodrine
c = Metabolite("desglymidodrine")
dikb.putObject(c)

## tell the KB that midodrine is a prodrug
dikb.objects["midodrine"].prodrug.putEntry("True")

## add a metabolite for midodrine
c = Metabolite("norpropoxyphene")
dikb.putObject(c)

## add  metabolites for tamoxifen
c = Metabolite("N-desmethyltamoxifen")
dikb.putObject(c)

c = Metabolite("4-hydroxytamoxifin")
dikb.putObject(c)

## add an assertion with no evidence support
a = Assertion('erythromycin', 'in_vitro_selective_inhibitor_of_enzyme', 'cyp3a4')
ev.addAssertion(a)

## apply a single evidence item as support for multiple substrate_of assertions for tamoxifen
for elt in ["cyp3a4", "cyp3a5", "cyp2c9", "cyp2d6"]:
    a = Assertion("tamoxifen", "substrate_of", elt)
    e = Evidence(ev)
    e.create(doc_p = "tamoxifen-teva-122008", q = "\nMetabolism\n\nTamoxifen is extensively metabolized after oral administration. N-desmethyl tamoxifen is the major metabolite found in patients’ plasma. The biological activity of N-desmethyl tamoxifen appears to be similar to that of tamoxifen. 4-Hydroxytamoxifen and a side chain primary alcohol derivative of tamoxifen have been identified as minor metabolites in plasma. Tamoxifen is a substrate of cytochrome P-450 3A, 2C9 and 2D6, and an inhibitor of P-glycoprotein.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "009242009")
    err = a.insertEvidence("for",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)

## add  metabolites for theophylline
c = Metabolite("1-methylxanthine")
dikb.putObject(c)

c = Metabolite("3-methylxanthine")
dikb.putObject(c)

c = Metabolite("1,3-dimethyluric-acid")
dikb.putObject(c)

c = Metabolite("1-methyluric-acid")
dikb.putObject(c)

c = Drug("caffeine")
dikb.putObject(c)

## apply a single evidence item as support for multiple has_metabolite assertions for theophylline
for elt in ["1-methylxanthine","3-methylxanthine","1,3-dimethyluric-acid","caffeine"]:
    a = Assertion("theophylline", "has_metabolite", elt)
    e = Evidence(ev)
    e.create(doc_p = "theophylline-3M-082006", q = "\nMetabolism Following oral dosing, theophylline does not undergo any measurable first-pass elimination. In adults and children beyond one year of age, approximately 90%of the dose is metabolized in the liver. Biotransformation takes place through demethylation to 1-methylxanthine and 3-methylxanthine and hydroxylation to 1,3-dimethyluric acid. 1-methylxanthine is further hydroxylated, by xanthine oxidase, to 1-methyluric acid. About 6%of a theophylline dose is N-methylated to caffeine. Theophylline demethylation to 3-methylxanthine is catalyzed by cytochrome P-450 1A2, while cytochromes P-450 2E1 and P-450 3A3 catalyze the hydroxylation to 1,3-dimethyluric acid. Demethylation to 1-methylxanthine appears to be catalyzed either by cytochrome P-450 1A2 or a closely related cytochrome. In neonates, the N-demethylation pathway is absent while the function of the hydroxylation pathway is markedly deficient. The activity of these pathways slowly increases to maximal levels by one year of age.\n\nCaffeine and 3-methylxanthine are the only theophylline metabolites with pharmacologic activity. 3-methylxanthine has approximately one tenth the pharmacologic activity of theophylline and serum concentrations in adults with normal renal function are <1 mcg/mL. In patients with end-stage renal disease, 3-methylxanthine may accumulate to concentrations that approximate the unmetabolized theophylline concentration. Caffeine concentrations are usually undetectable in adults regardless of renal function. In neonates, caffeine may accumulate to concentrations that approximate the unmetabolized theophylline concentration and thus, exert a pharmacologic effect.", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "009242009")
    err = a.insertEvidence("for",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)


## apply a single evidence item as support for multiple substrate_of assertions for voriconazole
for elt in ["cyp3a4", "cyp2c19", "cyp2c9"]:
    a = Assertion("voriconazole", "substrate_of", elt)
    e = Evidence(ev)
    e.create(doc_p = "voriconazole-roerig-052008", q = "\nMetabolism\n\nIn vitro studies showed that voriconazole is metabolized by the human hepatic cytochrome P450 enzymes, CYP2C19, CYP2C9 and CYP3A4 ", ev_type = "Non_traceable_Drug_Label_Statement", revwr = "boycer", timestamp = "009242009")
    err = a.insertEvidence("for",e, ev)
    if err[0] == 1:
        print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:s" % (a.object, a.slot, a.value, err[1])
    else:
        print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
        ev.addAssertion(a)

## apply a single evidence item as rebuttal for multiple inhibits assertions
for elt in ["cyp2c19","cyp2c9","cyp3a4"]:
	a = Assertion("voriconazole", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "voriconazole-roerig-052008", q = "Effects of Voriconazole on Other Drugs\n\nIn vitro studies with human hepatic microsomes show that voriconazole inhibits the metabolic activity of the cytochrome P450 enzymes CYP2C19, CYP2C9, and CYP3A4. In these studies, the inhibition potency of voriconazole for CYP3A4 metabolic activity was significantly less than that of two other azoles, ketoconazole and itraconazole. In vitro studies also show that the major metabolite of voriconazole, voriconazole N-oxide, inhibits the metabolic activity of CYP2C9 and CYP3A4 to a greater extent than that of CYP2C19. Therefore, there is potential for voriconazole and its major metabolite to increase the systemic exposure (plasma concentrations) of other drugs metabolized by these CYP450 enzymes.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "09/24/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence as rebuttal for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## add a  metabolite for voriconazole
c = Metabolite("voriconazole-N-oxide")
dikb.putObject(c)

## apply a single evidence item as support for multiple inhibits assertions
for elt in ["cyp2c19","cyp2c9","cyp3a4"]:
	a = Assertion("voriconazole-N-oxide", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "voriconazole-roerig-052008", q = "Effects of Voriconazole on Other Drugs\n\nIn vitro studies with human hepatic microsomes show that voriconazole inhibits the metabolic activity of the cytochrome P450 enzymes CYP2C19, CYP2C9, and CYP3A4. In these studies, the inhibition potency of voriconazole for CYP3A4 metabolic activity was significantly less than that of two other azoles, ketoconazole and itraconazole. In vitro studies also show that the major metabolite of voriconazole, voriconazole N-oxide, inhibits the metabolic activity of CYP2C9 and CYP3A4 to a greater extent than that of CYP2C19. Therefore, there is potential for voriconazole and its major metabolite to increase the systemic exposure (plasma concentrations) of other drugs metabolized by these CYP450 enzymes.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "09/24/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)


## apply a single evidence item as support for multiple inhibits assertions
for elt in ["cyp3a4","cyp2c9"]:
	a = Assertion("zafirlukast", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "zafirlukast-astrazeneca-012008", q = "Metabolism\n\nZafirlukast is extensively metabolized. The most common metabolic products are hydroxylated metabolites which are excreted in the feces. The metabolites of zafirlukast identified in plasma are at least 90 times less potent as LTD4 receptor antagonists than zafirlukast in a standard in vitro test of activity. In vitro studies using human liver microsomes showed that the hydroxylated metabolites of zafirlukast excreted in the feces are formed through the cytochrome P450 2C9 (CYP2C9) pathway. Additional in vitro studies utilizing human liver microsomes show that zafirlukast inhibits the cytochrome P450 CYP3A4 and CYP2C9 isoenzymes at concentrations close to the clinically achieved total plasma concentrations", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "09/24/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence as support for the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as support for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## add assumptions to certain evidence entries that were lacking them
ev.objects['cyp3a4_controls_formation_of_N-desmethyltamoxifen'].evidence_for[0].assumptions.addEntry(['erythromycin_in_vitro_selective_inhibitor_of_enzyme_cyp3a4'])

## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp3a4","cyp3a5","cyp2d6"]:
	a = Assertion("ranolazine", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "ranolazine-cv-therapeutics-042009", q = "7.2 Effects of Ranolazine on Other Drugs\n\nIn vitro studies indicate that ranolazine and its O-demethylated metabolite are weak inhibitors of CYP3A, moderate inhibitors of CYP2D6 and moderate P-gp inhibitors. ", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "09/25/2009")
	err = a.insertEvidence("for",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## add an assertion with no evidence support
a = Assertion('metoprolol', 'in_viVo_probe_substrate_of_enzyme', 'cyp2d6')
ev.addAssertion(a)

## add assumptions to certain evidence entries that were lacking them
ev.objects['perphenazine_substrate_of_cyp2d6'].evidence_for[3].assumptions.addEntry(['cyp2d6_polymorphic_enzyme_True'])

ev.objects['venlafaxine_primary_total_clearance_enzyme_cyp2d6'].evidence_for[0].assumptions.addEntry(['cyp2d6_polymorphic_enzyme_True'])

ev.objects['perphenazine_substrate_of_cyp2d6'].evidence_for[4].assumptions.addEntry(['cyp2d6_polymorphic_enzyme_True'])

ev.objects['sertraline_substrate_of_cyp2c19'].evidence_for[0].assumptions.addEntry(['cyp2c19_polymorphic_enzyme_True'])

## delete the minimum_therapeutic_dose_is_at_least assertion from the
## drug model DrugModel::Pceut_Entity
for e,v in dikb.objects.iteritems():
    if v.__dict__.has_key('minimum_therapeutic_dose_is_at_least'):
        del(v.__dict__['minimum_therapeutic_dose_is_at_least'])

## add the slots maximum_therapeutic_dose and assumed_effective_dose
## to Pceut_Entity instances and ensure that all Pceut_Entity classes have a
## minimum_therapeutic_dose attribute
for k,v in dikb.objects.iteritems():
    if type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__()):
        v.minimum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)
        v.maximum_therapeutic_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)
        v.assumed_effective_dose = EMultiContValSlot(["continuous_value"],["continuous_value"], None)


## inserting the min and max therapeutic dose ranges
## insert a minimum  therapeutic dose assertion 
a = Assertion("atorvastatin", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.010)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("atorvastatin", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.080)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

######

## insert a minimum  therapeutic dose assertion 
a = Assertion("celecoxib", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("celecoxib", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.800)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("fluvastatin", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.020)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("fluvastatin", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.800)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("lansoprazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.015)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("lansoprazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.180)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("leflunomide", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.010)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("leflunomide", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("metronidazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.750)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("metronidazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 4.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("midodrine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.030)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("midodrine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("nicardipine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.060)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("nicardipine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.120)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("pantoprazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.020)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("pantoprazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.240)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("promethazine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.0125)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("promethazine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.150)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("propoxyphene", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.065)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("propoxyphene", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.600)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("ranolazine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 1.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("ranolazine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 2.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("theophylline", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.840)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("theophylline", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 1.050)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("tolbutamide", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.250)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("tolbutamide", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 3.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("topiramate", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.025)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("topiramate", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.4)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("trimethoprim", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.2)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("trimethoprim", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("valproate", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.500)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("valproate", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 4.2)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("voriconazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("voriconazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.600)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = Assertion("zafirlukast", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = Assertion("zafirlukast", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

# assume the assertion 'desipramine primary_total_clearance_enzyme
# cyp2d6' true by default
ev.objects['desipramine_primary_total_clearance_enzyme_cyp2d6'].assert_by_default = True

# fix the statement written based on and FDA guidance entry for omeprazole
ev.objects['omeprazole_primary_total_clearance_enzyme_cyp2c19'].evidence_for[0].quote = '\r\nThe FDA recommends omeprazole as a recommended CYP2C19 substrate for in vivo studies in it most recent guidance document (See Table 2, p. 19)'

# assume the assertion 'debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6' true by default
ev.objects['debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6'].assert_by_default = True

## we incorrectly initialized all minimum_therapeutic_dose and
## maximum_therapeutic_dose assertions to be instances of the
## Assertion class instead of the ContValAssertion class. Fix this by
## deleting the previous assertions and re-initializing the assertions
## correctly.
for e in ev.objects.keys():
    if e.find("minimum_therapeutic_dose") != -1 or e.find("maximum_therapeutic_dose") != -1:
        print "deleting assertion %s" % e
        v =  ev.objects[e]        
        ev.deleteAssertion(v)

## re-inserting the min and max therapeutic dose ranges; this time
## making ContValAssertion instances instead of Assertion instances

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("atorvastatin", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.010)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("atorvastatin", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.080)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

######

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("celecoxib", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("celecoxib", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.800)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("fluvastatin", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.020)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("fluvastatin", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.800)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("lansoprazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.015)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("lansoprazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.180)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("leflunomide", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.010)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("leflunomide", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("metronidazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.750)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("metronidazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 4.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("midodrine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.030)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("midodrine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("nicardipine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.060)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("nicardipine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.120)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("pantoprazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.020)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("pantoprazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.240)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("promethazine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.0125)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("promethazine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.150)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("propoxyphene", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.065)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("propoxyphene", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.600)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("ranolazine", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 1.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("ranolazine", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 2.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("theophylline", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.840)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("theophylline", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 1.050)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("tolbutamide", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.250)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("tolbutamide", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 3.0)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("topiramate", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.025)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("topiramate", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.4)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("trimethoprim", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.2)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("trimethoprim", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("valproate", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.500)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("valproate", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 4.2)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("voriconazole", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.200)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("voriconazole", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.600)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a minimum  therapeutic dose assertion 
a = ContValAssertion("zafirlukast", "minimum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## insert a maximum therapeutic dose assertion 
a = ContValAssertion("zafirlukast", "maximum_therapeutic_dose", "continuous_value")
e = EvidenceContinousVal(ev)
e.create(doc_p = "Effective-dose-collection-spreadsheet-FINAL-08072009.xls", q = "GERIATRIC AND ADULT DOSE RANGE", revwr = "boycer", ev_type = "Non_Tracable_Statement", timestamp = "10/08/2009", val = 0.040)
err = a.insertEvidence("for",e, ev)
if err[0] == 1:
    print "ERROR: there was an error applying this evidence for  the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
else:
    print "SUCCESS: evidence successfully applied as support  for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
a.assert_by_default = True
ev.addAssertion(a)

## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["CYP1A2", "CYP2A6", "CYP2C9", "CYP2C19", "CYP2D6", "CYP2E1", "CYP3A4" ]:
	a = Assertion("eszopiclone", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "eszoplicone-sepracor-052008", q = "Metabolism\n\nFollowing oral administration, eszopiclone is extensively metabolized by oxidation and demethylation. The primary plasma metabolites are (S)-zopiclone-N-oxide and (S)-N-desmethyl zopiclone; the latter compound binds to GABA receptors with substantially lower potency than eszopiclone, and the former compound shows no significant binding to this receptor. In vitro studies have shown that CYP3A4 and CYP2E1 enzymes are involved in the metabolism of eszopiclone. Eszopiclone did not show any inhibitory potential on CYP450 1A2, 2A6, 2C9, 2C19, 2D6, 2E1, and 3A4 in cryopreserved human hepatocytes.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "11/09/2009")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)



# correcting a doc pointer
ev.objects["sertraline_increases_auc_desipramine"].evidence_for[1].doc_pointer = "9241008"

# add sildenafil to the DIKB
d = Drug("sildenafil")
dikb.putObject(d)

# add asenapine to the DIKB
d = Drug("asenapine")
dikb.putObject(d)

# add iloperidone to the DIKB
d = Drug("iloperidone")
dikb.putObject(d)

## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp2c19", "cyp2c9", "cyp2d6", "cyp2b6", "cyp2a6", "cyp1a2", "cyp2e1"]:
	a = Assertion("atazanavir", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "atazanavir-ERSquibb-112009", q = "Clinically significant interactions are not expected between atazanavir and substrates of CYP2C19, CYP2C9, CYP2D6, CYP2B6, CYP2A6, CYP1A2, or CYP2E1. Clinically significant interactions are not expected between atazanavir when administered with ritonavir and substrates of CYP2C8.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)


## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp2c9", "cyp2b6", "cyp1a2", "cyp2e1"]:
	a = Assertion("indinavir", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "indinavir-merck-112008", q = "Based on in vitro data in human liver microsomes, indinavir does not inhibit CYP1A2, CYP2C9, CYP2E1 and CYP2B6. However, indinavir may be a weak inhibitor of CYP2D6.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp2c19", "cyp2c9", "cyp2d6", "cyp2a6", "cyp1a2", "cyp3a4", "cyp2c8"]:
	a = Assertion("montelukast", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "montelukast-AS-092009", q = "Based on further in vitro results in human liver microsomes, therapeutic plasma concentrations of montelukast do not inhibit cytochromes P450 3A4, 2C9, 1A2, 2A6, 2C19, or 2D6 (see Drug Interactions). In vitro studies have shown that montelukast is a potent inhibitor of cytochrome P450 2C8; however, data from a clinical drug-drug interaction study involving montelukast and rosiglitazone (a probe substrate representative of drugs primarily metabolized by CYP2C8) demonstrated that montelukast does not inhibit CYP2C8 in vivo, and therefore is not anticipated to alter the metabolism of drugs metabolized by this enzyme (see Drug Interactions).", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp1a1", "cyp1a2", "cyp2a6", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2e1"]:
	a = Assertion("iloperidone", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "iloperidone-vanda-2009", q = "Iloperidone is not a substrate for CYP1A1, CYP1A2, CYP2A6, CYP2B6, CYP2C8, CYP2C9, CYP2C19, or CYP2E1 enzymes. This suggests that an interaction of iloperidone with inhibitors or inducers of these enzymes, or other factors, like smoking, is unlikely.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## Oops, delete all of those inhibits assertions and apply evidence against substrate-of assertions
for elt in ["cyp1a1", "cyp1a2", "cyp2a6", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2e1"]:
    s = "%s_%s_%s" % ("iloperidone", "inhibits", elt)
    ev.deleteAssertion(ev.objects[s])
# I saved the evidence-base here

for elt in ["cyp1a1", "cyp1a2", "cyp2a6", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2e1"]:
	a = Assertion("iloperidone", "substrate_of", elt)
	e = Evidence(ev)
	e.create(doc_p = "iloperidone-vanda-2009", q = "Iloperidone is not a substrate for CYP1A1, CYP1A2, CYP2A6, CYP2B6, CYP2C8, CYP2C9, CYP2C19, or CYP2E1 enzymes. This suggests that an interaction of iloperidone with inhibitors or inducers of these enzymes, or other factors, like smoking, is unlikely.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)


## apply a single evidence item as support or rebuttal for multiple inhibits assertions
for elt in ["cyp1a1", "cyp1a2", "cyp2a6", "cyp2b6", "cyp2c8", "cyp2c9", "cyp2c19", "cyp2d6", "cyp2e1", "cyp3a4", "cyp3a5"]:
	a = Assertion("rosiglitazone", "inhibits", elt)
	e = Evidence(ev)
	e.create(doc_p = "rosiglitazone-SmithKline-Beecham-042009", q = "In vitro drug metabolism studies suggest that rosiglitazone does not inhibit any of the major P450 enzymes at clinically relevant concentrations.", revwr = "boycer", ev_type = "Non_traceable_Drug_Label_Statement", timestamp = "01/11/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## change evidence for to evidence against
e = ev.objects['asenapine_substrate_of_cyp2d6'].evidence_for[0]
ev.objects['asenapine_substrate_of_cyp2d6'].evidence_against.append(e)
ev.objects['asenapine_substrate_of_cyp2d6'].evidence_for.pop()

## remove a older version of a redundant evidence item 
del(ev.objects["paroxetine_inhibits_cyp2d6"].evidence_for[1])
del(ev.objects["paroxetine_does_not_inhibit_cyp2d6"].evidence_against[1])

## remove three assertions for a drug that doesn't exist
ev.deleteAssertion(ev.objects['buproprion_has_metabolite_erythrohydrobupropion'])
ev.deleteAssertion(ev.objects['buproprion_has_metabolite_hydroxybupropion'])
ev.deleteAssertion(ev.objects['buproprion_has_metabolite_threohydrobupropion'])

## apply a single evidence item as support or rebuttal for multiple substrate_of assertions
for elt in ["cyp1a2","cyp2c9","cyp2c19","cyp2e1"]:
	a = Assertion("quetiapine", "substrate_of", elt)
	e = Evidence(ev)
	e.create(doc_p = "16390352", q = "Enzyme system: recombinant human enzymes in human lymphoblastoid\nNADPH added: not explicitly mentioned but assumed\n\ninhibitor used: no\n\nQuetiapine metabolites were not detected after 1-h incubations of quetiapine with microsomes from vector-control lymphoblastoid cell lines or those that expressed CYP1A2, CYP2C9, CYP2C19 or CYP2E1. In contrast, metabolite profles produced when quetiapine was incubated in human liver microsomes (Figure 2A) were similar to those produced by expressed CYP3A4 (Figure 2B). Quetiapine sulfoxide was the major metabolite formed during incubations with expressed CYP3A4.", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom", timestamp = "02/12/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%s\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)


## apply a single evidence item as support or rebuttal for multiple substrate_of assertions
for elt in ["cyp1a2","cyp2c8","cyp2c9","cyp2c19","cyp2d6"]:
	a = Assertion("nefazodone", "substrate_of", elt)
	e = Evidence(ev)
	e.create(doc_p = "11872324", q = "Enzyme system: recombinant human enzymes in human lymphoblastoid for CYP1A2 and CYP2D6; recombinant human enzymes in baculovirus-infected insect cells for CYP2C8, CYP2C9, and CYP2C19\nNADPH added:yes\n\ninhibitor used: no\n\nWhen NEF or OH-NEF was incubated with microsomes from cells transfected with human cDNA for one of CYP1A1, CYP1A2, CYP2A6, CYP2D6, CYP3A4, CYP2C8, CYP2C9 arg, CYP2C9 cys, or CYP2C19, metabolite formation was seen with the CYP3A4 incubations only (Table 4).", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom", timestamp = "02/12/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%s\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## apply a single evidence item as support or rebuttal for multiple substrate_of assertions
for elt in ["cyp2c19","cyp2b6","cyp2a6","cyp2e1"]:
	a = Assertion("mirtazapine", "substrate_of", elt)
	e = Evidence(ev)
	e.create(doc_p = "10997935", q = "Enzyme system: recombinant human enzymes in human lymphoblastoid cells\nNADPH added:yes\n\ninhibitor used: no\n\nTable 2 shows that CYP2C19, CYP2B6, CYP2A6, AND CYP3E1 each contributed less than 1% to the formation of metabolites by the three metabolic pathways examined. NOTE: Formation of MIR-N+-glucuronide, a metabolite found in significant concentrations in humans, was not examined however, this metabolite is likely the product of the either the dirct glucuronidation of mirtazapine or a metabolite produced by the three pathways examined. ", revwr = "boycer", ev_type = "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom", timestamp = "02/12/2010")
	err = a.insertEvidence("against",e, ev)
	if err[0] == 1:
		print "ERROR: there was an error applying this evidence for or against the assertion %s_%s_%s:\n%s\tMESSAGE:%s" % (a.object, a.slot, a.value, err[1])
	else:
		print "SUCCESS: evidence successfully applied as rebuttal for the assertion %s_%s_%s:\nWARNINGS:%s" % (a.object, a.slot, a.value, err[1])
		ev.addAssertion(a)

## add an assertion that is not supported by evidence
a = Assertion("fluvoxamine", "in_vitro_selective_inhibitor_of_enzyme", "cyp1a2")
ev.addAssertion(a)

## edit a quote to be more accurate
ev.objects["ziprasidone_substrate_of_cyp1a2"].evidence_for[0].quote = '\r\nEnzyme system: human liver microsomes\r\n\r\nNADPH added: yes\r\n\r\ninhibitor used: furafylline\r\n\r\nreaction: ziprasidone --&gt; oxindole acetic acid\r\n\r\nQuote:\r\nInhibition of metabolite formation by each inhibitor is\r\nsummarized in Table 2. Ketoconazole (10micM) inhibited\r\nthe formation of ziprasidone sulphoxide (sulphoxide and\r\nsulphone) by 79% and oxindole acetic acid N-dealkylated\r\nproduct) completely. Sulphaphenazole an furafylline did\r\nnot inhibit the formation of ziprasidone sulphoxide. The formation of oxindole acetic acid was inhibited (~50%) by furafylline. The formation of ziprasidone metabolites was not inhibited by quinidine but rather increased. '

## add some drugs found in AUC studies that we did not have before
si_l = ["prasugrel","desloratadine","alosetron","ibuprofen","lithium"]
for i in si_l:
    if i in dikb.objects.keys():
        print "%s seems to be present already!" % i
        continue
    
    d = Drug(i)
    dikb.putObject(d)


### SAVE CHANGES
#dikb.pickleKB("var/DIKB/dikb.pickle")
#ev.pickleKB("var/evidence-base/ev.pickle") 


################################################################################ 
######## REUSABLE SNIPPETS #####################################################

## UNCOMMENT AND RUN THIS WHEN THERE IS A CHANGE TO THE METABOLITE NAME FILE
# update the acceptable names for all metabolites
for k,v in dikb.objects.iteritems():

    try:
        del(v.metabolite_names)
    except AttributeError:
        pass
            
    try:
        f = open("data/chemicals_produced_by_metabolism")
    except IOError, err:
        warning(" ".join(["Could not open file containing metabolite names:",os.getcwd(),"data/chemicals_produced_by_metabolism", 
                          "Please make sure this file exists. Returning None"]), 1)
    else:
        t = f.read()
        # TODO : make sure to split off a newline if it exists
        f.close()
        
        if type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__()):
            v.metabolite_names = t.split("\n")
            v.has_metabolite.range = v.metabolite_names + ["none_assigned"]
            v.increases_auc.range = v.chemical_names + v.metabolite_names + v.drug_names +  ["none_assigned"]
            v.sole_PK_effect_alter_metabolic_clearance.range = v.chemical_names + v.metabolite_names + v.drug_names + ["none_assigned"]
        elif type(v) in ([Enzyme] + Enzyme("cyp3a4").__class__.__subclasses__()):
            v.metabolite_names = t.split("\n")
            v.controls_formation_of.range = v.metabolite_names + ["none_assigned"]

### END OF CODE TO UPDATE METABOLITE NAME LISTS

## UNCOMMENT AND RUN THIS WHEN THERE IS A CHANGE TO THE DRUG NAME FILE
# update the acceptable names for all DRUGS
for k,v in dikb.objects.iteritems():

    try:
        del(v.drug_names)
    except AttributeError:
        pass
            
    try:
        f = open("data/va-ndfrt-active-ingredients")
    except IOError, err:
        warning(" ".join(["Could not open file containing drug names:",os.getcwd(),"data/va-ndfrt-active-ingredients", 
                          "Please make sure this file exists. Returning None"]), 1)
    else:
        t = f.read()
        # TODO : make sure to split off a newline if it exists
        f.close()
        
        if type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__()):
            v.drug_names = t.split(",")
            v.increases_auc.range = v.chemical_names + v.metabolite_names + v.drug_names + ["none_assigned"]
            v.sole_PK_effect_alter_metabolic_clearance.range = v.chemical_names + v.metabolite_names + v.drug_names + ["none_assigned"]

### END OF CODE TO UPDATE DRUG NAME LISTS

## UNCOMMENT AND RUN THIS WHEN THERE IS A CHANGE TO THE CHEMICAL NAME FILE
# update the acceptable names for all CHEMICALS
for k,v in dikb.objects.iteritems():

    try:
        del(v.chemical_names)
    except AttributeError:
        pass
            
    try:
        f = open("data/non_therapeutic_or_metabolic_chemicals")
    except IOError, err:
        warning(" ".join(["Could not open file containing chemical names:",os.getcwd(),"data/non_therapeutic_or_metabolic_chemicals", 
                          "Please make sure this file exists. Returning None"]), 1)
    else:
        t = f.read()
        # TODO : make sure to split off a newline if it exists
        f.close()
        
        if type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__()):
            v.chemical_names = t.split("\n")
            v.increases_auc.range = v.chemical_names + v.metabolite_names + v.drug_names + ["none_assigned"]
            v.sole_PK_effect_alter_metabolic_clearance.range = v.chemical_names + v.metabolite_names + v.drug_names + ["none_assigned"]

### END OF CODE TO UPDATE CHEMICAL NAME LISTS


### Evidence base analytics

print "number of assertions in the system: %s" % len(ev.objects.keys()) 


ev_for_cnt = 0
ev_agnst_cnt = 0
for k,v in ev.objects.iteritems():                  
    for e in v.evidence_for:
        ev_for_cnt += 1
    for e in v.evidence_against:
        ev_agnst_cnt += 1
print "number of evidence items for and against -- for : %d, against : %d " % (ev_for_cnt, ev_agnst_cnt)


asrts = {
    "bioavailability":  None,
    "controls_formation_of": None,
    "first_pass_effect": None,
    "fraction_absorbed": None,
    "has_metabolite": None,
    "increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    "maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    "polymorphic_enzyme":None,
    "does_not_permanently_deactivate_catalytic_function":None,
    "permanently_deactivates_catalytic_function":None,
    "in_vitro_probe_substrate_of_enzyme":None,
    "in_vitro_selective_inhibitor_of_enzyme":None,
    "in_viVo_selective_inhibitor_of_enzyme":None,
    "in_viVo_probe_substrate_of_enzyme":None,
    "pceut_entity_of_concern":None,
    "sole_PK_effect_alter_metabolic_clearance":None,
    }
a_str = ""
asmpt_cnt = 0
ev_w_asmpts = 0
et_d = {}
a_to_asmpt = {}
for asrt_tp in asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    
    
    for k,v in ev.objects.iteritems():                  
        if k.find(asrt_tp) != -1:
            if k.find("is_not_substrate_of") != -1 or k.find("does_not_inhibit") != -1:
                #print "\tskipping %s because it is not a non-redundant or default evidence evidence item\n" % k
                continue

            if asrt_tp == "substrate_of" and k.find("in_vitro_probe_substrate_of_enzyme") != -1:
                continue

            print "\t%s" % k

            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                print "\t\t(for) %s" % e.evidence_type.value
                
                print "\t\tassumptions:" + str(e.assumptions.value)
                asmpt_cnt += len(e.assumptions.value)
                if len(e.assumptions.value) > 0:
                    a_str += "%s & %s & %s & %s \\\\ \n" % (e.doc_pointer, k, e.evidence_type.value, ", ".join(e.assumptions.value))
                    
                    ev_w_asmpts += 1
                    if not et_d.has_key(e.evidence_type.value):
                        et_d[e.evidence_type.value] = {}
                        
                    for a in e.assumptions.value:
                        et_d[e.evidence_type.value][a] = None
                        if not a_to_asmpt.has_key(a):
                            a_to_asmpt[a] = 1
                        else:
                            a_to_asmpt[a] += 1

            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1
                print "\t\t(against) %s" % e.evidence_type.value

                print "\t\tassumptions:" + str(e.assumptions.value)
                asmpt_cnt += len(e.assumptions.value)
                if len(e.assumptions.value) > 0:
                    a_str += "%s & %s & %s & %s \\\\ \n" % (e.doc_pointer, k, e.evidence_type.value, ",".join(e.assumptions.value))
                    
                    ev_w_asmpts += 1
                    if not et_d.has_key(e.evidence_type.value):
                        et_d[e.evidence_type.value] = {}
                        
                    for a in e.assumptions.value:
                        et_d[e.evidence_type.value][a] = None
                        if not a_to_asmpt.has_key(a):
                            a_to_asmpt[a] = 1
                        else:
                            a_to_asmpt[a] += 1

print "Evidence items with assumptions: %s" % ev_w_asmpts
print "Total evidence use assumptions used: %s" % asmpt_cnt
#print "all assumptions:\n%s" % a_str

#### TEST EXPORTING ASSERTIONS

# set all assertions as classifiable
for e,v in ev.objects.iteritems():
    v.ready_for_classification = True
exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

################################################################################
##  CLASSIFY THE RELEVANCE OF EACH NEW PMID BY USING DRUG AND SLOT
##  TERMS IN THE TITLE AND MESH HEADINGS
################################################################################
from Bio.EUtils  import HistoryClient
import re

# this PMID list represents all PMIDs from Carols DIDB queries in July 2009; see the notes in the upitt-ddi-research-notes emacs wiki for more information
pmid_l = ["10022747","10048600","10064566","10073324","10073330","10073330","10078840","10192755","10192756","10192828","10197892","10211916","10211917","10220126","10350035","10350045","10365639","10365640","10379638","10383917","10417041","10421611","10440457","10440472","10443872","10445377","10445380","10456487","10460810","10465860","10492058","10494454","10505485","10505590","10510155","10519444","10519458","10541779","10550852","10560276","10570018","10575324","10579150","10579472","10579479","10583026","10587282","10587283","10608481","10630840","10631623","10631960","10639689","10647097","10653204","10653206","10653222","10653223","10668847","10672631","10732663","10741632","10745059","10770452","10770480","10771452","10771453","10771454","10771455","10771457","10771458","10780263","10780971","10830154","10831018","10855463","10857058","10860134","10862503","10877005","10890261","10896409","10896409","10901285","10907965","10914294","10917404","10933885","10937612","10942191","10950473","10950475","10950476","10950477","10950845","10952475","10954064","10982203","10997935","10997936","10997938","10997944","11001249","11009047","11038157","11038165","11049910","11069441","11075316","11084219","11095583","11106150","11130217","11133003","11136295","11144696","11147928","11151749","11159797","11167668","11170509","11180037","11192140","11199933","11199955","11206048","11210405","11213850","11213852","11225566","11233461","11240973","11255075","11270912","11270913","11270914","11302931","11304901","11309547","11317475","11343579","11360029","11360030","11393588","11401013","11411823","11426073","11436960","11452243","11453896","11454728","11454731","11477317","11496034","11501681","11502727","11504269","11554425","11560868","11563412","11563413","11591904","11593075","11673748","11675850","11675851","11689122","11699614","11717183","11719727","11744603","11752104","11763009","11791889","11791895","11799345","11799350","11802103","11803239","11823755","11839370","11905593","11907488","11910256","11910261","11910263","11910267","11910269","11926715","11955666","11978161","11981236","11981356","11985287","12007677","12021638","12065442","12102620","12107617","12107857","12110370","12142636","12142637","12142644","12172335","12172343","12172351","12185555","12222750","12242602","12352271","12352274","12397887","12404553","12404680","12404680","12410055","12412820","12432977","12433805","12433817","12433827","12438554","12452751","12454563","12454566","12463729","12469329","12500067","12584149","12584149","12584155","12590402","12616671","12621382","12640212","12649767","12657913","12695344","12695349","12698310","12723462","12723464","12736515","12756206","12806570","12809966","12883230","12898080","12902213","12920164","12920410","12920426","12920491","12936703","12955290","12959283","12968986","12975335","1388041","1389950","1389951","1412604","1424422","1425809","14499311","14515060","14520118","14534519","14551182","14563790","14615476","14639062","14652237","14681337","14709940","14709949","14730412","14749554","14749694","14998432","15025747","15039292","15056484","15060511","15089819","15118480","15155554","15155557","15180173","15199083","15257068","15291653","15301577","15304427","15304522","15319333","15319335","15349025","15355124","15358990","15367832","15385843","1544284","1545398","1546384","15475412","15496220","15496221","15496223","15496639","15496643","15536467","15545309","15547048","15570188","15572275","15599502","15601807","15608135","15643105","15652242","15687478","1570226","15738749","15769884","15802384","15845683","15857446","15876900","15893449","15903129","15905806","15910012","15961986","15963095","16003291","1602320","16081671","16120067","16154484","16154484","16163531","16189751","16190800","16192107","16226034","16236038","16272405","16282832","16282844","16282848","16299161","16321618","16342006","16368922","16381668","16390352","16415122","16487224","16517279","16528137","16534635","16542203","16584121","16595756","16633141","16637792","16638740","16678550","16679385","16702902","16724927","16770757","16778712","16778714","16815319","16822276","16841513","16841959","16842393","16855466","16855470","16856883","16918719","16928789","16963489","16988941","17035599","17038872","17089108","17101742","17101742","17110831","17110835","17110836","17124578","17142561","17186001","17224709","17244765","17256449","17304149","17327954","17332142","17335546","17359941","1737080","17470523","17484519","17495417","17502774","17541885","17596106","17600081","17682072","17687273","1770158","1770159","17729385","17823234","17846135","17890444","1792934","1793525","18043911","18048485","18048485","18094219","18094221","18201587","18215333","18219560","18285471","18287571","18303146","18307373","18310890","18332082","18344053","18362161","1840138","18401578","18420781","18438654","18516595","1855347","18725510","18728628","18754843","18796323","18809730","18809731","18816299","18832427","1888636","18989234","19001559","19004846","19022943","19029327","19047469","1905641","19066872","19074527","19142106","19142178","19172438","19204080","19242403","1924640","19255936","2007317","2035723","2037714","2066458","2087328","2106534","2107764","2293416","2353956","2530759","2530800","2530801","2611560","2743709","2784633","2787124","3101102","3121163","3128416","3266222","3346197","3480904","3569026","3731135","3766793","3942266","3963258","3971003","400992","5008054","6149238","6685838","6770696","7124987","7396317","7473143","7482685","7485641","7544547","7586931","7604142","7632166","7640589","7650232","7655131","7690693","7742153","7751409","7751433","7782485","7806690","7852260","7878612","7891353","7946933","7954177","7955810","7961525","7962687","7974626","7977898","8005185","8043067","8081642","8096308","8138941","8159782","8160253","8195463","8204992","8214190","8225700","8249047","8267110","8286821","8295752","8317590","8333005","8333006","8359179","8376611","8448725","8466541","8477556","8486817","8513845","8531073","8536426","8601557","8615436","8617706","8617707","8617708","8632299","8632299","8632334","8633698","8635181","8667235","8675966","8685072","8690825","8703653","8721280","8730981","8732315","8737959","8738315","8739822","8764331","8784658","8807660","8823236","8830063","8834415","8838442","8845547","8852534","8861737","8866916","8866941","8880055","8885121","8885123","8889898","8904628","8930024","8930784","8941024","8944409","8946674","8978949","8984760","8986010","8986010","8986013","9004067","9004072","9017779","9020195","9023308","9024962","9024962","9027670","9029057","9029745","9029748","9034418","9068933","9068935","9140699","9143866","9169893","9183927","9205822","9208383","9209244","9218934","9241008","9241013","9248870","9264051","9272272","9278211","9284850","9286199","9298519","9315986","9326836","9333103","9333110","9342584","9352572","9375595","9375597","9378846","9384460","9384467","9394027","9408807","9431831","9433393","9442550","9447478","9469504","9472836","9493476","9505989","9546010","9549640","9565774","9574817","9580580","9584328","9585794","9602962","9605789","9616194","9626923","9627209","9641003","9660035","9660843","9681669","9681670","9681670","9690701","9690983","9729831","9734116","9757149","9803772","9834040","9835499","9855322","9860152","9862748","9863158","9864083","9868741","9895145","9923577","9923581","9934950","9951426","9988363"]

clnt = HistoryClient.HistoryClient()
abstr_l_d = {}

# gather all abstracts associated with each pmid
for id in pmid_l:
    rslt = clnt.search(id)
    if len(rslt) > 1:
        print "NOTE: More than one abstract returned for pmid:%s" % id

    for i in range(0,len(rslt)):
        rec = rslt[i].efetch(retmode = "text", rettype = "abstract").read()
        if not abstr_l_d.has_key(id):
            abstr_l_d[id] = []

        abstr_l_d[id].append(rec.upper())

#import pickle
# f = open("/tmp/dibk-abstract-search-07252009.pickle", 'w')
#f = open("/tmp/dibk-abstract-search-09162009.pickle", 'w')
#pickle.dump(abstr_l_d, f)
#f.close()

# validation set studies as of 07/25/2009
upia_drug_l = ["AMIODARONE", "ARIPIPRAZOLE", "ATOMOXETINE", "ATORVASTATIN", "BUPROPION", "CELECOXIB", "CIMETIDINE", "CINACALCET", "CIPROFLOXACIN", "CITALOPRAM", "CLARITHROMYCIN", "CLOPIDOGREL", "CLOZAPINE", "DANAZOL", "DESVENLAFAXINE", "DULOXETINE", "ESCITALOPRAM", "ESZOPICLONE", "FLUCONAZOLE", "FLUOXETINE", "FLUVASTATIN", "FLUVOXAMINE", "GEMFIBROZIL", "INDOMETHACIN", "ISONIAZID", "LANSOPRAZOLE", "LEFLUNOMIDE", "METRONIDAZOLE", "MEXILETINE", "MIDODRINE", "MIRTAZAPINE", "MONTELUKAST", "NICARDIPINE", "NORFLOXACIN", "OLANZAPINE", "OMEPRAZOLE", "PALIPERIDONE", "PANTOPRAZOLE", "PAROXETINE", "PIOGLITAZONE", "PROMETHAZINE", "PROPAFENONE", "PROPOXYPHENE", "QUETIAPINE", "QUINIDINE", "RABEPRAZOLE", "RANOLAZINE", "RISPERIDONE", "ROSIGLITAZONE", "SERTRALINE", "TAMOXIFEN", "TELITHROMYCIN", "TERBINAFINE", "THEOPHYLLINE", "TICLOPIDINE", "TOLBUTAMIDE", "TOPIRAMATE", "TRAZODONE", "TRIMETHOPRIM", "VALPROATE", "VENLAFAXINE", "VERAPAMIL", "VORICONAZOLE", "ZAFIRLUKAST", "ZALEPLON", "ZIPRASIDONE", "ZOLPIDEM"]

# purported probe substrates
l = filter(lambda x: x.find("probe_substrate_of_enzyme") != -1 , ev.objects.keys())
l.sort()
p_s_d = {}
for elt in l:
    a = ev.objects[elt]
    d = a.object.upper()
    if not p_s_d.has_key(d):
        p_s_d[d] = set()
    p_s_d[d].add(a.value.upper())

# purported selective inhibitors
l = filter(lambda x: x.find("selective_inhibitor_of_enzyme") != -1 , ev.objects.keys())
l.sort()
s_i_d = {}
for elt in l:
    a = ev.objects[elt]
    d = a.object.upper()
    if not s_i_d.has_key(d):
        s_i_d[d] = set()
    s_i_d[d].add(a.value.upper())

v_d = {}
pmid_cache = []
rex_AUC = re.compile("AUC|AREA UNDER")
rex_CT = re.compile("RANDOMIZED CONTROLLED TRIAL|CLINICAL TRIAL")
rex_CR = re.compile("CASE REPORTS|CASE STUDY|CASE STUDIES|CASE HISTORIES")
for k1 in upia_drug_l:
    for k2 in upia_drug_l:
        if k1 == k2: 
            continue 

        f_k = "%s - %s" % (k1, k2)
        r_k = "%s - %s" % (k2, k1)
        if k2 != k1 and not (v_d.has_key(f_k) or v_d.has_key(r_k)):
            v_d[f_k] = None
            v_d[r_k] = None

            rex_obj_1 = re.compile(k1.upper())
            rex_obj_2 = re.compile(k2.upper())

            m_l = []
            n_l = []
            k_l = []
            j_l = []
            p_s_l = []
            s_i_l = []
            for id, abstr_l in abstr_l_d.iteritems():
                for elt in abstr_l:
                    if rex_obj_1.search(elt) and rex_obj_2.search(elt):
                        print "\n-----------------------------------------------------\n"

                        pmid_cache.append(id)

                        for ky in p_s_d.keys():
                            rex_sbst = re.compile(ky)
                            if rex_sbst.search(elt):
                                p_s_l.append((id, ky, "".join(p_s_d[ky])))

                        for ky in s_i_d.keys():
                            rex_inh = re.compile(ky)
                            if rex_inh.search(elt):
                                s_i_l.append((id, ky, "".join(s_i_d[ky])))

                        if rex_AUC.search(elt):
                            m_l.append(id)
                        elif rex_CT.search(elt):
                            n_l.append(id)
                        elif rex_CR.search(elt):
                            k_l.append(id)
                        else:
                            j_l.append(id)
                        
            if len(m_l) > 0:
                print "Studies mentioning AUC and pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(m_l))

            if len(n_l) > 0:
                print "Clinical trials mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(n_l))

            if len(k_l) > 0:
                print "Case reports mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(k_l))

            if len(j_l) > 0:
                print "Other evidence items mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(j_l))

            if len(p_s_l) > 0:
                print "These studies involve a purported probe substrate possibly indicating that %s or %s inhibits one or more of these enzymes:\n%s\n" % (k1, k2, ",\t\n".join([",".join(x) for x in p_s_l]))

            if len(s_i_l) > 0:
                print "These studies involve a purported selective inhibitor possibly indicating that %s or %s is a substrate of one or more of these enzymes:\n%s\n" % (k1, k2, ",\t\n".join([",".join(x) for x in s_i_l]))


# for each object in the DIKB, determine which remaining abstracts contain the
# drug name and/or assertion type
kys = dikb.objects.keys()
kys.sort()
for k in kys:
    rex_obj = re.compile(k.upper())
    n_l = []
    k_l = []
    j_l = []
    p_s_l = []
    s_i_l = []
    for id, abstr_l in abstr_l_d.iteritems():
        if id in pmid_cache:
            #print "PMID:%s already classified" % id
            continue

        for elt in abstr_l:
            if rex_obj.search(elt):
                for ky in p_s_d.keys():
                    rex_sbst = re.compile(ky)
                    if rex_sbst.search(elt):
                        p_s_l.append((id, ky, "".join(p_s_d[ky])))

                for ky in s_i_d.keys():
                    rex_inh = re.compile(ky)
                    if rex_inh.search(elt):
                        s_i_l.append((id, ky, "".join(s_i_d[ky])))

                if rex_CT.search(elt):
                    n_l.append(id)
                elif rex_CR.search(elt):
                    k_l.append(id)
                else:
                    j_l.append(id)

    if len(n_l) + len(k_l) + len(j_l) + len(p_s_l) + len(s_i_l) > 0:
        print "\n-----------------------------------------------------\nOBJECT: %s" % k
           
    if len(n_l) > 0:
        print "Clinical trials mentioning %s:\n\t\t%s\n" % (k, ",".join(n_l))
        
    if len(k_l) > 0:
        print "Case reports mentioning  %s:\n\t\t%s\n" % (k, ",".join(k_l))

    if len(j_l) > 0:
        print "Other evidence items mentioning %s:\n\t\t%s\n" % (k, ",".join(j_l))

    if len(p_s_l) > 0:
        print "These studies involve a purported probe substrate possibly indicating that %s inhibits one or more of these enzymes:\n%s\n" % (k, ",\t\n".join([",".join(x) for x in p_s_l]))

    if len(s_i_l) > 0:
                print "These studies involve a purported selective inhibitor possibly indicating that %s is a substrate of one or more of these enzymes:\n%s\n" % (k, ",\t\n".join([",".join(x) for x in s_i_l]))
################################################################################
## END OF PMID CLASSIFICATION CODE
################################################################################


################################################################################
## CODE TO GENERATE PAIRS FOR THE VALIDATION SET 
################################################################################

# generate drug pairs that I will need to search clinical-trial and
# case-report literature for
ais_mets_l = ["AMIODARONE", "ARIPIPRAZOLE", "ATOMOXETINE", "ATORVASTATIN", "BUPROPION", "CELECOXIB", "CIMETIDINE", "CINACALCET", "CIPROFLOXACIN", "CITALOPRAM", "CLARITHROMYCIN", "CLOPIDOGREL", "CLOZAPINE", "DANAZOL", "DESVENLAFAXINE", "DULOXETINE", "ESCITALOPRAM", "ESZOPICLONE", "FLUCONAZOLE", "FLUOXETINE", "FLUVASTATIN", "FLUVOXAMINE", "GEMFIBROZIL", "INDOMETHACIN", "ISONIAZID", "LANSOPRAZOLE", "LEFLUNOMIDE", "METRONIDAZOLE", "MEXILETINE", "MIDODRINE", "MIRTAZAPINE", "MONTELUKAST", "NICARDIPINE", "NORFLOXACIN", "OLANZAPINE", "OMEPRAZOLE", "PALIPERIDONE", "PANTOPRAZOLE", "PAROXETINE", "PIOGLITAZONE", "PROMETHAZINE", "PROPAFENONE", "PROPOXYPHENE", "QUETIAPINE", "QUINIDINE", "RABEPRAZOLE", "RANOLAZINE", "RISPERIDONE", "ROSIGLITAZONE", "SERTRALINE", "TAMOXIFEN", "TELITHROMYCIN", "TERBINAFINE", "THEOPHYLLINE", "TICLOPIDINE", "TOLBUTAMIDE", "TOPIRAMATE", "TRAZODONE", "TRIMETHOPRIM", "VALPROATE", "VENLAFAXINE", "VERAPAMIL", "VORICONAZOLE", "ZAFIRLUKAST", "ZALEPLON", "ZIPRASIDONE", "ZOLPIDEM"]
ais_mets = {"AMIODARONE":None, "ARIPIPRAZOLE":None, "ATOMOXETINE":None, "ATORVASTATIN":None, "BUPROPION":None, "CELECOXIB":None, "CIMETIDINE":None, "CINACALCET":None, "CIPROFLOXACIN":None, "CITALOPRAM":None, "CLARITHROMYCIN":None, "CLOPIDOGREL":None, "CLOZAPINE":None, "DANAZOL":None, "DESVENLAFAXINE":None, "DULOXETINE":None, "ESCITALOPRAM":None, "ESZOPICLONE":None, "FLUCONAZOLE":None, "FLUOXETINE":None, "FLUVASTATIN":None, "FLUVOXAMINE":None, "GEMFIBROZIL":None, "INDOMETHACIN":None, "ISONIAZID":None, "LANSOPRAZOLE":None, "LEFLUNOMIDE":None, "METRONIDAZOLE":None, "MEXILETINE":None, "MIDODRINE":None, "MIRTAZAPINE":None, "MONTELUKAST":None, "NICARDIPINE":None, "NORFLOXACIN":None, "OLANZAPINE":None, "OMEPRAZOLE":None, "PALIPERIDONE":None, "PANTOPRAZOLE":None, "PAROXETINE":None, "PIOGLITAZONE":None, "PROMETHAZINE":None, "PROPAFENONE":None, "PROPOXYPHENE":None, "QUETIAPINE":None, "QUINIDINE":None, "RABEPRAZOLE":None, "RANOLAZINE":None, "RISPERIDONE":None, "ROSIGLITAZONE":None, "SERTRALINE":None, "TAMOXIFEN":None, "TELITHROMYCIN":None, "TERBINAFINE":None, "THEOPHYLLINE":None, "TICLOPIDINE":None, "TOLBUTAMIDE":None, "TOPIRAMATE":None, "TRAZODONE":None, "TRIMETHOPRIM":None, "VALPROATE":None, "VENLAFAXINE":None, "VERAPAMIL":None, "VORICONAZOLE":None, "ZAFIRLUKAST":None, "ZALEPLON":None, "ZIPRASIDONE":None, "ZOLPIDEM":None}
v_d = {}
for k1 in ais_mets_l:
    for k2 in ais_mets.keys():
        f_k = "%s - %s" % (k1, k2)
        r_k = "%s - %s" % (k2, k1)
        if k2 != k1 and not (v_d.has_key(f_k) or v_d.has_key(r_k)):
            v_d[f_k] = None
            v_d[r_k] = None
            print "%s, %s" % (k1, k2)

################################################################################
## END OF CODE TO GENERATE PAIRS FOR THE VALIDATION SET
################################################################################

################################################################################
# ANOTHER PASS AT VALIDATION SET STUDIES FOCUSING ON CLEARANCE STUDIES (09/16/2009)
################################################################################
upia_drug_l = ["AMIODARONE", "ARIPIPRAZOLE", "ATOMOXETINE", "ATORVASTATIN", "BUPROPION", "CELECOXIB", "CIMETIDINE", "CINACALCET", "CIPROFLOXACIN", "CITALOPRAM", "CLARITHROMYCIN", "CLOPIDOGREL", "CLOZAPINE", "DANAZOL", "DESVENLAFAXINE", "DULOXETINE", "ESCITALOPRAM", "ESZOPICLONE", "FLUCONAZOLE", "FLUOXETINE", "FLUVASTATIN", "FLUVOXAMINE", "GEMFIBROZIL", "INDOMETHACIN", "ISONIAZID", "LANSOPRAZOLE", "LEFLUNOMIDE", "METRONIDAZOLE", "MEXILETINE", "MIDODRINE", "MIRTAZAPINE", "MONTELUKAST", "NICARDIPINE", "NORFLOXACIN", "OLANZAPINE", "OMEPRAZOLE", "PALIPERIDONE", "PANTOPRAZOLE", "PAROXETINE", "PIOGLITAZONE", "PROMETHAZINE", "PROPAFENONE", "PROPOXYPHENE", "QUETIAPINE", "QUINIDINE", "RABEPRAZOLE", "RANOLAZINE", "RISPERIDONE", "ROSIGLITAZONE", "SERTRALINE", "TAMOXIFEN", "TELITHROMYCIN", "TERBINAFINE", "THEOPHYLLINE", "TICLOPIDINE", "TOLBUTAMIDE", "TOPIRAMATE", "TRAZODONE", "TRIMETHOPRIM", "VALPROATE", "VENLAFAXINE", "VERAPAMIL", "VORICONAZOLE", "ZAFIRLUKAST", "ZALEPLON", "ZIPRASIDONE", "ZOLPIDEM"]

# purported probe substrates
l = filter(lambda x: x.find("probe_substrate_of_enzyme") != -1 , ev.objects.keys())
l.sort()
p_s_d = {}
for elt in l:
    a = ev.objects[elt]
    d = a.object.upper()
    if not p_s_d.has_key(d):
        p_s_d[d] = set()
    p_s_d[d].add(a.value.upper())

# purported selective inhibitors
l = filter(lambda x: x.find("selective_inhibitor_of_enzyme") != -1 , ev.objects.keys())
l.sort()
s_i_d = {}
for elt in l:
    a = ev.objects[elt]
    d = a.object.upper()
    if not s_i_d.has_key(d):
        s_i_d[d] = set()
    s_i_d[d].add(a.value.upper())

v_d = {}
pmid_cache = []
rex_AUC = re.compile(" CL |CLEARANCE")
rex_CT = re.compile("RANDOMIZED CONTROLLED TRIAL|CLINICAL TRIAL")
rex_CR = re.compile("CASE REPORTS|CASE STUDY|CASE STUDIES|CASE HISTORIES")
skip_l = ["10073330", "10445377", "10579150", "10579479", "10771455", "10877005", "10950845", "11009047", "11240973", "11309547", "11452243", "11563412", "11907488", "11910256", "11985287", "12412820", "12621382", "12809966", "12920410", "14515060", "14551182", "14709940", "15025747", "15199083", "15496639", "15545309", "15961986", "15963095", "16003291", "16120067", "16487224", "16584121", "16778714", "16822276", "16856883", "17124578", "17224709", "17244765", "17687273", "18307373", "18809731", "18832427", "19001559", "19142106", "19242403", "8195463", "8830063", "8861737", "8941024", "9241008"]
for k1 in upia_drug_l:
    for k2 in upia_drug_l:
        if k1 == k2: 
            continue 

        f_k = "%s - %s" % (k1, k2)
        r_k = "%s - %s" % (k2, k1)
        if k2 != k1 and not (v_d.has_key(f_k) or v_d.has_key(r_k)):
            v_d[f_k] = None
            v_d[r_k] = None

            rex_obj_1 = re.compile(k1.upper())
            rex_obj_2 = re.compile(k2.upper())

            m_l = []
            n_l = []
            k_l = []
            j_l = []
            p_s_l = []
            s_i_l = []
            for id, abstr_l in abstr_l_d.iteritems():
                if id in skip_l:
                    print "Skipping %s since it has already been reviewed" % id
                    continue
                for elt in abstr_l:
                    if rex_obj_1.search(elt) and rex_obj_2.search(elt):
                        print "\n-----------------------------------------------------\n"

                        pmid_cache.append(id)

                        for ky in p_s_d.keys():
                            rex_sbst = re.compile(ky)
                            if rex_sbst.search(elt):
                                p_s_l.append((id, ky, "".join(p_s_d[ky])))

                        for ky in s_i_d.keys():
                            rex_inh = re.compile(ky)
                            if rex_inh.search(elt):
                                s_i_l.append((id, ky, "".join(s_i_d[ky])))

                        if rex_AUC.search(elt):
                            m_l.append(id)
                        elif rex_CT.search(elt):
                            n_l.append(id)
                        elif rex_CR.search(elt):
                            k_l.append(id)
                        else:
                            j_l.append(id)
                        
            if len(m_l) > 0:
                print "Studies mentioning CLEARANCE and pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(m_l))

            if len(n_l) > 0:
                print "Clinical trials mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(n_l))

            if len(k_l) > 0:
                print "Case reports mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(k_l))

            if len(j_l) > 0:
                print "Other evidence items mentioning pair %s - %s:\n\t\t%s\n" % (k1, k2, ",".join(j_l))

            if len(p_s_l) > 0:
                print "These studies involve a purported probe substrate possibly indicating that %s or %s inhibits one or more of these enzymes:\n%s\n" % (k1, k2, ",\t\n".join([",".join(x) for x in p_s_l]))

            if len(s_i_l) > 0:
                print "These studies involve a purported selective inhibitor possibly indicating that %s or %s is a substrate of one or more of these enzymes:\n%s\n" % (k1, k2, ",\t\n".join([",".join(x) for x in s_i_l]))


######### TALLYING EVIDENCE TYPES

non_default_asrts = {
    "bioavailability":  None,
    "controls_formation_of": None,
    "first_pass_effect": None,
    "fraction_absorbed": None,
    "has_metabolite": None,
    "increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    "maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    }

for asrt_tp in non_default_asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    for k,v in ev.objects.iteritems():                  
        if k.find(asrt_tp) != -1:
            if asrt_tp == 'substrate_of' and k.find("is_not") != -1:
                print "\tskipping %s because it is not the 'substrate_of' assertions\n" % k
                continue

            if asrt_tp == 'substrate_of' and k.find("in_vitro_probe") != -1:
                print "\tskipping %s because it is not the 'substrate_of' assertions\n" % k
                continue
            
            if v.assert_by_default == True:
                print "\tskipping %s because it is a default assumption\n" % k
                continue

            print "\t%s" % k
            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                print "\t\t(for) %s" % e.evidence_type.value
            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1
                print "\t\t(against) %s" % e.evidence_type.value
    tot = 0.0
    for k,v in et_for.iteritems():
        tot += v
        
    print "%d types found 'for' %s assertions (total items: %d):" % (len(et_for.keys()), asrt_tp, tot)
    for k,v in et_for.iteritems():
        print "\ttype: %s, %d/%d = %.2f" % (k, v, tot, float(v)/float(tot))

    tot = 0.0
    for k,v in et_against.iteritems():
        tot += v
    print "\n%d types found 'against' %s assertions (total items: %d):" % (len(et_against.keys()), asrt_tp, tot)
    for k,v in et_against.iteritems():
        print "\ttype: %s, %d/%d = %.2f" % (k, v, tot, float(v)/float(tot))


######### GET ALL DOC_POINTERS CURRENTLY IN THE DIKB ###############
doc_d = {}
for e,v in ev.objects.iteritems():
    for it in v.evidence_for:
        doc_d[it.doc_pointer] = None
    for it in v.evidence_against:
        doc_d[it.doc_pointer] = None


######### DETERMINING PREDICTIONS MADE USING THE MOST RIGOUROUS CRITERIA 09/25/2009  ###########
ev = EvidenceBase("evidence","UPIA")
dikb = DIKB("dikb","UPIA", ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.unpickleKB("var/evidence-base/ev.pickle")

for e,v in ev.objects.iteritems():
    v.ready_for_classification = True
# we are not ready to make in vitro to in vivo predictions and the
# correct min and max doses have not yet been entered so we shut the
# only therapeutic dose assertion off
ev.objects["diltiazem_minimum_therapeutic_dose_continuous_value"].ready_for_classification = False

reset_evidence_rating(ev, dikb)

# using levels-of-evidence-most-rigourous-09252009 as the belief criteria
exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")


######### DETERMINING PREDICTIONS MADE USING THE NON-VALIDATED CRITERIA 10/08/2009  ###########
ev = EvidenceBase("evidence","UPIA")
dikb = DIKB("dikb","UPIA", ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.unpickleKB("var/evidence-base/ev.pickle")

for e,v in ev.objects.iteritems():
    v.ready_for_classification = True

reset_evidence_rating(ev, dikb)

# using levels-of-evidence-unvalidated-10082009.txt as the belief criteria
exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

## how many drugs, metabolites, assertions, an evidence items?
drug_cnt = 0
met_cnt = 0
asrt_cnt = 0
ev_cnt = 0
for e,v in dikb.objects.iteritems():
    if type(v) == Drug:
        drug_cnt += 1
    elif type(v) == Metabolite:
        met_cnt += 1

asrt_cnt = len(ev.objects.values())
for e,v in ev.objects.iteritems():
    ev_cnt += len(v.evidence_for)
    ev_cnt += len(v.evidence_against)


## which items in the DIKB have evidence for and against that is both
## from product labeling? 
for e,v in ev.objects.iteritems():
    lbl_for = False
    fda_for = False
    ev_for = False
    lbl_against = False
    fda_against = False
    ev_against = False

    for it in v.evidence_for:
        ev_for = True
        if it.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            lbl_for = True
        if it.evidence_type.value == "Non_Tracable_Statement":
            fda_for = True

    for it in v.evidence_against:
        ev_against = True
        if it.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            lbl_against = True
        if it.evidence_type.value == "Non_Tracable_Statement":
            fda_against = True
    
    if (lbl_for and lbl_against):
        print "possible labeling inconsistency for assertion: %s" % e
        
    if (lbl_for and fda_against) or (fda_for and lbl_against):
        print "possible label/FDA inconsistency for assertion: %s" % e
    
    if (ev_for and lbl_against) or (lbl_for and ev_against):
        print "possible label/evidence inconsistency for assertion: %s" % e

# results on (12/09/2009):
# possible label/evidence inconsistency for assertion: ziprasidone_substrate_of_cyp1a2
# possible labeling inconsistency for assertion: escitalopram_inhibits_cyp2d6
# possible label/evidence inconsistency for assertion: escitalopram_inhibits_cyp2d6    
        
##############################
## MAKING SUBSTRATE_OF/IS_NOT_SUBSTRATE_OF INHIBITS/DOES_NOT_INHIBIT EVIDENCE CONCORDANT

# is evidence-for and evidence-against concordant for the substrate_of/is_not_substrate_of and inhibits/does_not_inhibit assertions?

# substrate_of FOR and is_not_substrate_of AGAINST
for k,v in dikb.objects.iteritems():
    if not (type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__())):
        print "\n\npassing on %s" % k
        continue 

    for asrt in v.substrate_of.evidence: # multiple assertions; one for each enzyme
        ev_for_ids = [x.doc_pointer for x in asrt.evidence_for]
        ev_for_ids.sort()

        found = False
        ev_against_ids = []
        casrt = None
        for casrt in v.is_not_substrate_of.evidence: # look for matching 'value'(enzyme)
            if found == False and casrt.value == asrt.value:
                found = True
                ev_against_ids = [x.doc_pointer for x in casrt.evidence_against]
            elif found == True and casrt.value == asrt.value:
                print "Something strange = more than one assertion for %s? (_id = %d)" % (casrt._name, casrt._id)

        if casrt == None:
            print "\n\n%s FOR: %s\nNO is_not_substrate_of assertions!" % (asrt._name, ", ".join(ev_for_ids))
            obj = k
            slot = "is_not_substrate_of"
            val = asrt.value
            print "Creating a new assertion: %s" % "_".join([obj, slot, val])
            nasrt = Assertion(obj, slot, val)
            for elt in asrt.evidence_for:
                print "adding evidence item with doc pointer '%s' to evidence_against." % elt.doc_pointer
                nev = Evidence(ev)
                nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
                nasrt.insertEvidence("against", nev)
            print "Assertion %s added to the evidence base" % nasrt._name
            ev.addAssertion(nasrt)

        if found:
            ev_against_ids.sort()
            print "\n\n%s FOR: %s\n%s AGAINST:%s" % (asrt._name, ", ".join(ev_for_ids), casrt._name, ", ".join(ev_against_ids))
            if not ev_for_ids == ev_against_ids:
                print "%s FOR and %s AGAINST are discordant" % (asrt._name, casrt._name)


# is_not_substrate_of FOR and substrate_of AGAINST
for k,v in dikb.objects.iteritems():
    if not (type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__())):
        print "\n\npassing on %s" % k
        continue 

    for asrt in v.is_not_substrate_of.evidence: # multiple assertions; one for each enzyme
        ev_for_ids = [x.doc_pointer for x in asrt.evidence_for]
        if len(ev_for_ids) == 0:
            print "\n\nNo evidence FOR for %s; going on to the next assertion." % asrt._name
            continue

        ev_for_ids.sort()

        found = False
        ev_against_ids = []
        casrt = None
        for casrt in v.substrate_of.evidence: # look for matching 'value'(enzyme)
            if found == False and casrt.value == asrt.value:
                found = True
                ev_against_ids = [x.doc_pointer for x in casrt.evidence_against]
            elif found == True and casrt.value == asrt.value:
                print "Something strange = more than one assertion for %s? (_id = %d)" % (casrt._name, casrt._id)

        if casrt == None:
            print "\n\n%s FOR: %s\nNO substrate_of assertions!" % (asrt._name, ", ".join(ev_for_ids))
            obj = k
            slot = "substrate_of"
            val = asrt.value
            print "Creating a new assertion: %s" % "_".join([obj, slot, val])
            nasrt = Assertion(obj, slot, val)
            for elt in asrt.evidence_for:
                print "adding evidence item with doc pointer '%s' to evidence_against." % elt.doc_pointer
                nev = Evidence(ev)
                nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
                nasrt.insertEvidence("against", nev)
            print "Assertion %s added to the evidence base" % nasrt._name
            ev.addAssertion(nasrt)

        if found:
            ev_against_ids.sort()
            print "\n\n%s FOR: %s\n%s AGAINST:%s" % (asrt._name, ", ".join(ev_for_ids), casrt._name, ", ".join(ev_against_ids))
            if not ev_for_ids == ev_against_ids:
                print "%s FOR and %s AGAINST are discordant" % (asrt._name, casrt._name)
                for elt in asrt.evidence_for:
                    if elt.doc_pointer not in ev_against_ids:
                        obj = k
                        slot = "substrate_of"
                        val = asrt.value
                        nasrt = Assertion(obj, slot, val)
                        print "adding evidence item with doc pointer '%s' to evidence_against." % elt.doc_pointer
                        nev = Evidence(ev)
                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
                        nasrt.insertEvidence("against", nev)
                        #ev.addAssertion(nasrt)
                        #print "Assertion %s added to the evidence base" % nasrt._name
                for elt in casrt.evidence_against:
                    if elt.doc_pointer not in ev_for_ids:
                        obj = k
                        slot = "is_not_substrate_of"
                        val = asrt.value
                        nasrt = Assertion(obj, slot, val)
                        print "adding evidence item with doc pointer '%s' to evidence_for." % elt.doc_pointer
                        nev = Evidence(ev)
                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
                        nasrt.insertEvidence("for", nev)
                        #ev.addAssertion(nasrt)
                        #print "Assertion %s added to the evidence base" % nasrt._name


## substrate_of AGAINST and is_not_substrate_of FOR AND is_not_substrate_of AGAINST and substrate_of FOR 
tpl_l = [("substrate_of", "evidence_against", "is_not_substrate_of", "evidence_for"), 
         ("is_not_substrate_of", "evidence_against", "substrate_of", "evidence_for")]
for tpl in tpl_l:
	for k,v in dikb.objects.iteritems():
	    if not (type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__())):
	        print "\n\npassing on %s" % k
	        continue 
	
	    for asrt in v.__dict__[tpl[0]].evidence: # multiple assertions; one for each enzyme
	        ev_a_ids = [x.doc_pointer for x in asrt.__dict__[tpl[1]]]
	        if len(ev_a_ids) == 0:
	            print "\n\nNo %s for %s; going on to the next assertion." % (tpl[1].upper(), asrt._name)
	            continue
	
	        ev_a_ids.sort()
	
	        found = False
	        ev_b_ids = []
	        casrt = None
	        for casrt in v.__dict__[tpl[2]].evidence: # look for matching 'value'(enzyme)
	            if found == False and casrt.value == asrt.value:
	                found = True
	                ev_b_ids = [x.doc_pointer for x in casrt.__dict__[tpl[3]]]
	            elif found == True and casrt.value == asrt.value:
	                print "Something strange = more than one assertion for %s? (_id = %d)" % (casrt._name, casrt._id)
	
	        if casrt == None:
	            print "\n\n%s %s: %s\nNO %s assertions!" % (asrt._name, tpl[1].upper(), ", ".join(ev_a_ids), tpl[2])
	            obj = k
	            slot = tpl[2]
	            val = asrt.value
	            print "Creating a new assertion: %s" % "_".join([obj, slot, val])
	            nasrt = Assertion(obj, slot, val)
	            for elt in asrt.__dict__[tpl[1]]:
	                print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, nasrt._name, tpl[3])
	                nev = Evidence(ev)
	                nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
	                nasrt.insertEvidence(tpl[3].split("_")[1], nev)
	            print "Assertion %s added to the evidence base" % nasrt._name
	            ev.addAssertion(nasrt)
	
	        if found:
	            ev_b_ids.sort()
	            print "\n\n%s %s: %s\n%s %s:%s" % (asrt._name, tpl[1].upper(), ", ".join(ev_a_ids), casrt._name, tpl[3].upper(), ", ".join(ev_b_ids))
	            if not ev_a_ids == ev_b_ids:
	                print "%s %s and %s %s are discordant" % (asrt._name, tpl[1].upper(), casrt._name, tpl[3].upper())
	                for elt in asrt.__dict__[tpl[1]]:
	                    if elt.doc_pointer not in ev_b_ids:
	                        obj = k
	                        slot = tpl[2]
	                        val = asrt.value
	                        nasrt = Assertion(obj, slot, val)
	                        print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, nasrt._name, tpl[3])
	                        nev = Evidence(ev)
	                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
	                        nasrt.insertEvidence(tpl[3].split("_")[1], nev)
	                        ev.addAssertion(nasrt)
	                        print "Assertion %s added to the evidence base" % nasrt._name
	                for elt in casrt.__dict__[tpl[3]]:
	                    if elt.doc_pointer not in ev_a_ids:
	                        obj = k
	                        slot = tpl[0]
	                        val = asrt.value
	                        nasrt = Assertion(obj, slot, val)
	                        print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, nasrt._name, tpl[1])
	                        nev = Evidence(ev)
	                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = "12172009")
	                        nasrt.insertEvidence(tpl[1].split("_")[1], nev)
	                        ev.addAssertion(nasrt)
	                        print "Assertion %s added to the evidence base" % nasrt._name
	

### THE ALGORITHM FOR ENSURING EVIDENCE FOR AND AGAINST IS CONCORDANT
## all substrate-of, is-not-substrate-of, inhibits and does_not_inhibit assertions
## NOTE: UNCOMMENT ALL LINES WITH 'ev.addAssertion(nasrt)' if you are ready to save

#!!!! NOTE: COMPLETE THE TODOS IN THE SECTION BEFORE ATTEMPTING TO RUN THIS CODE AGAIN!!!!!

timestamp = "02132010"
tpl_l = [("substrate_of", "evidence_against", "is_not_substrate_of", "evidence_for"), 
         ("substrate_of", "evidence_for", "is_not_substrate_of", "evidence_against"),
         ("is_not_substrate_of", "evidence_against", "substrate_of", "evidence_for"),
         ("is_not_substrate_of", "evidence_for", "substrate_of", "evidence_against"),
         ("inhibits", "evidence_against", "does_not_inhibit", "evidence_for"), 
         ("inhibits", "evidence_for", "does_not_inhibit", "evidence_against"),
         ("does_not_inhibit", "evidence_against", "inhibits", "evidence_for"),
         ("does_not_inhibit", "evidence_for", "inhibits", "evidence_against")]
for tpl in tpl_l:
	for k,v in dikb.objects.iteritems():
            print "Processing DIKB object '%s'" % k

	    if not (type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__())):
	        print "\n\npassing on %s" % k
	        continue 
	
            # iterate through all relevant assertions; there should be
            # only one for each enzyme
	    for asrt in v.__dict__[tpl[0]].evidence:
	        ev_a_ids = [x.doc_pointer for x in asrt.__dict__[tpl[1]]]
	        if len(ev_a_ids) == 0:
	            print "\n\nNo %s for %s; going on to the next assertion." % (tpl[1].upper(), asrt._name)
	            continue
                ev_a_ids.sort()
	
                ### handle case where there are opposing assertions
	        found = False
                ev_b_ids = []
	        casrt = None

                # look for matching 'value'(enzyme)
	        for casrt in v.__dict__[tpl[2]].evidence:
	            if found == False and casrt.value == asrt.value:
	                found = True
	                ev_b_ids = [x.doc_pointer for x in casrt.__dict__[tpl[3]]]
                        break

                # handle cases where there is are 1) no opposing
                # assertions or, 2) opposing assertions but non with a
                # matching value
	        if not found:
	            print "\n\n%s %s: %s\nNO %s assertions!" % (asrt._name, tpl[1].upper(), ", ".join(ev_a_ids), tpl[2])
	            obj = k
	            slot = tpl[2]
	            val = asrt.value
	            print "Creating a new assertion: %s" % "_".join([obj, slot, val])
	            nasrt = Assertion(obj, slot, val)
	            for elt in asrt.__dict__[tpl[1]]:
	                print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, nasrt._name, tpl[3])
	                nev = Evidence(ev)
	                nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = timestamp)

#!!!! TODO: COPY ALL ASSUMPTIONS !!!!!!!
	                nasrt.insertEvidence(tpl[3].split("_")[1], nev, ev)
	            print "Assertion %s added to the evidence base" % nasrt._name
	            ev.addAssertion(nasrt)


	        else:
	            ev_b_ids.sort()
	            print "\n\n%s %s: %s\n%s %s:%s" % (asrt._name, tpl[1].upper(), ", ".join(ev_a_ids), casrt._name, tpl[3].upper(), ", ".join(ev_b_ids))

	            if not ev_a_ids == ev_b_ids:
	                print "%s %s and %s %s are discordant" % (asrt._name, tpl[1].upper(), casrt._name, tpl[3].upper())
                        # make evidence for the two assertions concordant
	                for elt in asrt.__dict__[tpl[1]]:
	                    if elt.doc_pointer not in ev_b_ids:
	                        obj = k
	                        slot = tpl[2]
	                        val = asrt.value
	                        print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, asrt._name, tpl[3])
	                        nev = Evidence(ev)
	                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = timestamp)

#!!!! TODO: COPY ALL ASSUMPTIONS !!!!!!!
                                key = "%s_%s_%s" % (obj, slot, val)
                                ev.objects[key].insertEvidence(tpl[3].split("_")[1], nev, ev)


	                for elt in casrt.__dict__[tpl[3]]:
	                    if elt.doc_pointer not in ev_a_ids:
	                        obj = k
	                        slot = tpl[0]
	                        val = casrt.value
	                        print "adding evidence item with doc pointer '%s' to %s %s." % (elt.doc_pointer, casrt._name, tpl[1])
	                        nev = Evidence(ev)
	                        nev.create(doc_p = elt.doc_pointer, q = elt.quote, ev_type = elt.evidence_type.value, revwr = "boycer", timestamp = timestamp)

#!!!! TODO: COPY ALL ASSUMPTIONS !!!!!!!

                                key = "%s_%s_%s" % (obj, slot, val)
                                ev.objects[key].insertEvidence(tpl[1].split("_")[1], nev, ev)

	

######### DETERMINING PREDICTIONS MADE USING THE VARIOUS TIERS 12/17/2009  ###########
ev = EvidenceBase("evidence","UPIA")
dikb = DIKB("dikb","UPIA", ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.unpickleKB("var/evidence-base/ev.pickle")

for e,v in ev.objects.iteritems():
    v.ready_for_classification = True

reset_evidence_rating(ev, dikb)

exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

######
## LABELING ONLY - TURN OFF ALL DEFAULT ASSUMPTIONS TO REMOVE INHIBITS
## AND SUBSTRATE-OF ASSERTIONS FROM FDA GUIDANCE DOCUMENTS
ev = EvidenceBase("evidence","UPIA")
dikb = DIKB("dikb","UPIA", ev)
dikb.unpickleKB("var/DIKB/dikb.pickle")
ev.unpickleKB("var/evidence-base/ev.pickle")

defaults = []
for e,v in ev.objects.iteritems():
    if v.slot not in ["maximum_therapeutic_dose", "minimum_therapeutic_dose", ]  and v.assert_by_default == True and "Non_Tracable_Statement" in [x.evidence_type.value for x in v.evidence_for]:
        print "Removing assert_by_default status for %s" % e
        defaults.append(e)
        v.assert_by_default = False

for e,v in ev.objects.iteritems():
    v.ready_for_classification = True

reset_evidence_rating(ev, dikb)

exportAssertions(ev, dikb, "data/assertions.lisp")
assessBeliefCriteria(dikb, ev, "data/changing_assumptions.lisp")

## TURN BACK ON ALL DEFAULT ASSUMPTIONS 
for e,v in ev.objects.iteritems():
    if e in defaults:
        print "Re-setting assert_by_default status for %s" % e
        v.assert_by_default = True
## END OF LABELING ONLY

###### how many assertions in a list have product labeling evidence assigned?

l = ["7-ethoxyresorufin_in_vitro_probe_substrate_of_enzyme_cyp1a2",
     "S-mephenytoin_in_vitro_probe_substrate_of_enzyme_cyp2c19",
     "S-warfarin_in_vitro_probe_substrate_of_enzyme_cyp2c9",
     "S-warfarin_primary_total_clearance_enzyme_cyp2c9",
     "alpha-naphthoflavone_in_vitro_selective_inhibitor_of_enzyme_cyp1a2",
     "amiodarone_inhibits_cyp2c9",
     "amiodarone_inhibits_cyp2d6",
     "atazanavir_inhibits_cyp3a4",
     "atazanavir_inhibits_cyp3a5",
     "bufuralol_in_vitro_probe_substrate_of_enzyme_cyp2d6",
     "caffeine_primary_total_clearance_enzyme_cyp1a2",
     "chlorzoxazone_in_vitro_probe_substrate_of_enzyme_cyp2e1",
     "cimetidine_inhibits_cyp1a2",
     "cimetidine_inhibits_cyp3a4",
     "cimetidine_inhibits_cyp3a5",
     "ciprofloxacin_inhibits_cyp1a2",
     "clarithromycin_in_viVo_selective_inhibitor_of_enzyme_cyp3a4",
     "clarithromycin_inhibits_cyp3a4",
     "clarithromycin_inhibits_cyp3a5",
     "clopidogrel_inhibition_constant_cyp2b6",
     "coumarin_in_vitro_probe_substrate_of_enzyme_cyp2a6",
     "cyp2d6_controls_formation_of_4-hydroxydebrisoquine",
     "debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6",
     "desipramine_primary_total_clearance_enzyme_cyp2d6",
     "dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6",
     "dextromethorphan_in_vitro_probe_substrate_of_enzyme_cyp2d6",
     "dextromethorphan_primary_total_clearance_enzyme_cyp2d6",
     "erythromycin_in_vitro_probe_substrate_of_enzyme_cyp3a4",
     "fluconazole_inhibits_cyp2c9",
     "fluconazole_inhibits_cyp3a4",
     "fluconazole_inhibits_cyp3a5",
     "fluoxetine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6",
     "furafylline_in_vitro_selective_inhibitor_of_enzyme_cyp1a2",
     "gemfibrozil_inhibits_cyp2c8",
     "indinavir_inhibits_cyp3a4",
     "indinavir_inhibits_cyp3a5",
     "itraconazole_in_viVo_selective_inhibitor_of_enzyme_cyp3a4",
     "itraconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a4",
     "itraconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a5",
     "ketoconazole_in_viVo_selective_inhibitor_of_enzyme_cyp3a4",
     "ketoconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a4",
     "lansoprazole_primary_total_clearance_enzyme_cyp2c19",
     "mephenytoin_in_viVo_probe_substrate_of_enzyme_cyp2c19",
     "mexiletine_inhibits_cyp1a2",
     "midazolam_in_vitro_probe_substrate_of_enzyme_cyp3a4",
     "midazolam_primary_total_clearance_enzyme_cyp3a4",
     "montelukast_inhibition_constant_cyp2c8",
     "nefazodone_in_viVo_selective_inhibitor_of_enzyme_cyp3a4",
     "nefazodone_inhibits_cyp3a4",
     "nefazodone_inhibits_cyp3a5",
     "norfloxacin_inhibits_cyp1a2",
     "omeprazole_in_vitro_probe_substrate_of_enzyme_cyp2c19",
     "omeprazole_inhibits_cyp2c19",
     "omeprazole_primary_total_clearance_enzyme_cyp2c19",
     "p-nitrophenol_in_vitro_probe_substrate_of_enzyme_cyp2e1",
     "pantoprazole_primary_total_clearance_enzyme_cyp2c19",
     "paroxetine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6",
     "phenacetin_in_vitro_probe_substrate_of_enzyme_cyp1a2",
     "pioglitazone_inhibition_constant_cyp2c8",
     "propafenone_inhibits_cyp1a2",
     "quinidine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6",
     "quinidine_in_vitro_selective_inhibitor_of_enzyme_cyp2d6",
     "ritonavir_inhibits_cyp3a4",
     "ritonavir_inhibits_cyp3a5",
     "rosiglitazone_inhibition_constant_cyp2c8",
     "rosiglitazone_primary_total_clearance_enzyme_cyp2c8",
     "sildenafil_primary_total_clearance_enzyme_cyp3a4",
     "sulphaphenazole_in_vitro_selective_inhibitor_of_enzyme_cyp2c9",
     "telithromycin_inhibits_cyp3a4",
     "telithromycin_inhibits_cyp3a5",
     "terbinafine_inhibits_cyp2d6",
     "testosterone_in_vitro_probe_substrate_of_enzyme_cyp3a4",
     "theophylline_in_vitro_probe_substrate_of_enzyme_cyp1a2",
     "theophylline_primary_total_clearance_enzyme_cyp1a2",
     "ticlopidine_inhibition_constant_cyp2b6",
     "ticlopidine_inhibition_constant_cyp2c19",
     "tolbutamide_in_vitro_probe_substrate_of_enzyme_cyp2c9",
     "tolbutamide_primary_total_clearance_enzyme_cyp2c9",
     "triazolam_in_vitro_probe_substrate_of_enzyme_cyp3a4",
     "triazolam_primary_total_clearance_enzyme_cyp3a4",
     "trimethoprim_inhibits_cyp2c8",
     "troleandomycin_in_vitro_selective_inhibitor_of_enzyme_cyp3a4",
     "verapamil_inhibits_cyp1a2",
     "verapamil_inhibits_cyp3a4",
     "verapamil_inhibits_cyp3a5",
     "warfarin_primary_total_clearance_enzyme_cyp2c9"]

for asrt_str in l:
    asrt = ev.objects[asrt_str]
    for e in asrt.evidence_for:
        if e.evidence_type.value == 'Non_traceable_Drug_Label_Statement':
            print asrt_str
            break
    for e in asrt.evidence_against:
        if e.evidence_type.value == 'Non_traceable_Drug_Label_Statement':
            print asrt_str
            break

############################ ANALYSIS TO SUPPORT SPINA REVIEWS ####################### 
#  identify and classify all non-redundant assertions including
#  default assumptions
#####################################################################################

clinical_types = ["EV_CT_PK_Genotype", "EV_PK_DDI_RCT", "EV_CT_Pharmacokinetic", "EV_PK_DDI_Par_Grps", "EV_PK_DDI_NR"]
non_traceable_types = ["Non_traceable_Drug_Label_Statement", "Non_Tracable_Statement"]
#non_traceable_types = ["Non_traceable_Drug_Label_Statement"]
in_vitro_types = ["EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Recom", "EV_EX_Met_Enz_Inhibit_Cyp450_Hum_Microsome", "EV_EX_Met_Enz_ID", "EV_EX_Met_Enz_ID_Cyp450_Hum_Microsome_Chem", "EV_EX_Met_Enz_ID_Cyp450_Hum_Recom"]

asrts = {
    "bioavailability":  None,
    "controls_formation_of": None,
    "first_pass_effect": None,
    "fraction_absorbed": None,
    "has_metabolite": None,
    "increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    "maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    "polymorphic_enzyme":None,
    "does_not_permanently_deactivate_catalytic_function":None,
    "permanently_deactivates_catalytic_function":None,
    "in_vitro_probe_substrate_of_enzyme":None,
    "in_vitro_selective_inhibitor_of_enzyme":None,
    "in_viVo_selective_inhibitor_of_enzyme":None,
    "pceut_entity_of_concern":None,
    "sole_PK_effect_alter_metabolic_clearance":None,
    }


for asrt_tp in asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    (for_clin_cnt, for_non_trac_cnt, for_in_vitro_cnt) = (0,0,0)
    (against_clin_cnt, against_non_trac_cnt, against_in_vitro_cnt) = (0,0,0)
    a_cnt = 0
    default = 0
    
    for k,v in ev.objects.iteritems():                  
        if k.find(asrt_tp) != -1:
            if k.find("is_not_substrate_of") != -1 or k.find("does_not_inhibit") != -1:
                print "\tskipping %s because it is not a non-redundant or default evidence evidence item\n" % k
                continue

            if asrt_tp == "substrate_of" and k.find("in_vitro_probe_substrate_of_enzyme") != -1:
                continue
           
            if v.assert_by_default == True:
                default += 1

            a_cnt += 1
            print "\t%s" % k

            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                print "\t\t(for) %s" % e.evidence_type.value
                
                if e.evidence_type.value in clinical_types:
                    for_clin_cnt += 1
                elif e.evidence_type.value in non_traceable_types:
                    for_non_trac_cnt += 1
                elif e.evidence_type.value in in_vitro_types:
                    for_in_vitro_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               
         

            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1
                print "\t\t(against) %s" % e.evidence_type.value

                if e.evidence_type.value in clinical_types:
                    against_clin_cnt += 1
                elif e.evidence_type.value in non_traceable_types:
                    against_non_trac_cnt += 1
                elif e.evidence_type.value in in_vitro_types:
                    against_in_vitro_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               

    r_str = ""
                
    for_tot = 0.0
    for k,v in et_for.iteritems():
        for_tot += v
    print "%d types found 'for' %s assertions (total items: %d):" % (len(et_for.keys()), asrt_tp, for_tot)
    for k,v in et_for.iteritems():
        print "\ttype: %s, %d/%d = %.0f" % (k, v, for_tot, float(v)/float(for_tot))

    r_str +=  "%s & %s & %s & " % (asrt_tp, default, a_cnt)
    if for_tot == 0:
        r_str +=  "FOR: 0 & 0 & 0 & 0 &"
    else:
        r_str +=  "FOR: %s & %.0f & %.0f & %.0f \\\\" % (for_tot, float(for_clin_cnt)/float(for_tot) * 100, float(for_in_vitro_cnt)/float(for_tot) * 100, float(for_non_trac_cnt)/float(for_tot) * 100)

    against_tot = 0.0
    for k,v in et_against.iteritems():
        against_tot += v
    print "\n%d types found 'against' %s assertions (total items: %d):" % (len(et_against.keys()), asrt_tp, against_tot)
    for k,v in et_against.iteritems():
        print "\ttype: %s, %d/%d = %.0f" % (k, v, against_tot, float(v)/float(against_tot))

    r_str += "AGAINST: %s & " % against_tot
    if against_tot == 0:
        r_str +=  " 0 & 0 & 0 \\"
    else:
        r_str +=  " %.0f & %.0f & %.0f \\" % (float(against_clin_cnt)/float(against_tot) * 100, float(against_in_vitro_cnt)/float(against_tot) * 100, float(against_non_trac_cnt)/float(against_tot) * 100)

    print r_str
############################ END OF ANALYSIS TO SUPPORT SPINA REVIEWS ####################### 


############################ IDENTIFYING THE USE OF JUST ONE TYPE OF EVIDENCE ##############3

type = ["Non_traceable_Drug_Label_Statement"]

asrts = {
    #"bioavailability":  None,
    "controls_formation_of": None,
    #"first_pass_effect": None,
    #"fraction_absorbed": None,
    "has_metabolite": None,
    #"increases_auc": None,
    "inhibition_constant": None,
    "inhibits": None,
    #"maximum_concentration": None,
    "primary_metabolic_clearance_enzyme": None,
    "primary_total_clearance_enzyme": None,
    "primary_total_clearance_mechanism": None,
    "substrate_of": None,
    #"polymorphic_enzyme":None,
    #"does_not_permanently_deactivate_catalytic_function":None,
    #"permanently_deactivates_catalytic_function":None,
    #"in_vitro_probe_substrate_of_enzyme":None,
    #"in_vitro_selective_inhibitor_of_enzyme":None,
    #"in_viVo_selective_inhibitor_of_enzyme":None,
    #"pceut_entity_of_concern":None,
    #"sole_PK_effect_alter_metabolic_clearance":None,
    }


for asrt_tp in asrts.keys():
    print "\n\n%s: " % asrt_tp
    et_for = {}
    et_against = {}
    for_cnt = 0
    against_cnt = 0
    a_cnt = 0
    default = 0
    
    s_l = ev.objects.keys()
    s_l.sort()
    #for k,v in ev.objects.iteritems():                  
    for k in s_l:
        v = ev.objects[k]
        if k.find(asrt_tp) != -1:
            if k.find("is_not_substrate_of") != -1 or k.find("does_not_inhibit") != -1:
                #print "\tskipping %s because it is not a non-redundant or default evidence evidence item\n" % k
                continue

            if asrt_tp == "substrate_of" and k.find("in_vitro_probe_substrate_of_enzyme") != -1:
                continue
           
            if v.assert_by_default == True:
                default += 1

            a_cnt += 1
            print "\t%s" % k

            for e in v.evidence_for:
                if et_for.has_key(e.evidence_type.value):
                    et_for[e.evidence_type.value] += 1
                else:
                    et_for[e.evidence_type.value] = 1
                
                if e.evidence_type.value in type:
                    print "\t\t(for) %s" % e.evidence_type.value
                    for_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               
      

            for e in v.evidence_against:
                if et_against.has_key(e.evidence_type.value):
                    et_against[e.evidence_type.value] += 1
                else:
                    et_against[e.evidence_type.value] = 1

                if e.evidence_type.value in type:
                    print "\t\t(against) %s" % e.evidence_type.value
                    against_cnt += 1
                else:
                    "ERROR!, COULD NOT CLASSIFY EVIDENCE TYPE INTO ONE OF THREE CATEGORIES"               

    r_str = ""

    print r_str

############################ END OF IDENTIFYING THE USE OF JUST ONE TYPE OF EVIDENCE ##############




####### IDENTIFYING LEVELS OF EVIDENCE FOR MECHANISTIC ASSERTIONS 


inhibits_l = ["AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "ATAZANAVIR	CYP3A5", "ATAZANAVIR	CYP3A4", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2D6", "CIMETIDINE	CYP3A5", "CIMETIDINE	CYP1A2", "CIMETIDINE	CYP3A4", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A5", "CLARITHROMYCIN	CYP3A4", "DILTIAZEM	CYP3A4", "DULOXETINE	CYP2D6", "ERYTHROMYCIN	CYP3A4", "FLUCONAZOLE	CYP3A5", "FLUCONAZOLE	CYP2C9", "FLUCONAZOLE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP2C9", "FLUVOXAMINE	CYP1A2", "FLUVOXAMINE	CYP2C19", "GEMFIBROZIL	CYP2C8", "INDINAVIR	CYP3A5", "INDINAVIR	CYP3A4", "ITRACONAZOLE	CYP3A4", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "MODAFINIL	CYP2C19", "MODAFINIL-SULFONE	CYP2C19", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "NORFLOXACIN	CYP1A2", "OMEPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PROPAFENONE	CYP1A2", "QUINIDINE	CYP2D6", "RANOLAZINE	CYP2D6", "RANOLAZINE	CYP3A4", "RANOLAZINE	CYP3A5", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A5", "TELITHROMYCIN	CYP3A4", "TERBINAFINE	CYP2D6", "TERIFLUNOMIDE	CYP2C9", "TRIMETHOPRIM	CYP2C8", "VENLAFAXINE	CYP2D6", "VERAPAMIL	CYP3A4", "VERAPAMIL	CYP1A2", "VERAPAMIL	CYP3A5", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP2C19", "VORICONAZOLE-N-OXIDE	CYP2C9", "ZAFIRLUKAST	CYP2C9", "ZAFIRLUKAST	CYP3A4"]

t2_inhibits_l = ["AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "ATAZANAVIR	CYP3A4", "ATAZANAVIR	CYP3A5", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2D6", "CIMETIDINE	CYP1A2", "CIMETIDINE	CYP3A4", "CIMETIDINE	CYP3A5", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A4", "CLARITHROMYCIN	CYP3A5", "DILTIAZEM	CYP3A4", "DULOXETINE	CYP2D6", "ERYTHROMYCIN	CYP3A4", "FLUCONAZOLE	CYP2C9", "FLUCONAZOLE	CYP3A4", "FLUCONAZOLE	CYP3A5", "FLUOXETINE	CYP2D6", "GEMFIBROZIL	CYP2C8", "INDINAVIR	CYP3A4", "INDINAVIR	CYP3A5", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "NORFLOXACIN	CYP1A2", "OMEPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PROPAFENONE	CYP1A2", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A4", "TELITHROMYCIN	CYP3A5", "TERBINAFINE	CYP2D6", "TRIMETHOPRIM	CYP2C8", "VERAPAMIL	CYP1A2", "VERAPAMIL	CYP3A4", "VERAPAMIL	CYP3A5", "QUINIDINE	CYP2D6", "ITRACONAZOLE	CYP3A4"]

t3_inhibits_l = ["AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "ATAZANAVIR	CYP3A4", "ATAZANAVIR	CYP3A5", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2D6", "CIMETIDINE	CYP1A2", "CIMETIDINE	CYP3A4", "CIMETIDINE	CYP3A5", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A4", "CLARITHROMYCIN	CYP3A5", "DILTIAZEM	CYP3A4", "DULOXETINE	CYP2D6", "ERYTHROMYCIN	CYP3A4", "FLUCONAZOLE	CYP2C9", "FLUCONAZOLE	CYP3A4", "FLUCONAZOLE	CYP3A5", "FLUOXETINE	CYP2D6", "GEMFIBROZIL	CYP2C8", "INDINAVIR	CYP3A4", "INDINAVIR	CYP3A5", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "NORFLOXACIN	CYP1A2", "OMEPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PROPAFENONE	CYP1A2", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A4", "TELITHROMYCIN	CYP3A5", "TERBINAFINE	CYP2D6", "TRIMETHOPRIM	CYP2C8", "VERAPAMIL	CYP1A2", "VERAPAMIL	CYP3A4", "VERAPAMIL	CYP3A5", "QUINIDINE	CYP2D6", "ITRACONAZOLE	CYP3A4"]

t4_inhibits_l = ["AMIODARONE	CYP1A2", "AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "AMIODARONE	CYP3A4", "ATAZANAVIR	CYP3A4", "ATAZANAVIR	CYP3A5", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2D6", "CIMETIDINE	CYP1A2", "CIMETIDINE	CYP3A4", "CIMETIDINE	CYP3A5", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A4", "CLARITHROMYCIN	CYP3A5", "DILTIAZEM	CYP3A4", "DULOXETINE	CYP2D6", "ERYTHROMYCIN	CYP3A4", "FLUCONAZOLE	CYP2C9", "FLUCONAZOLE	CYP3A4", "FLUCONAZOLE	CYP3A5", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP1A2", "FLUVOXAMINE	CYP2C19", "FLUVOXAMINE	CYP2C9", "GEMFIBROZIL	CYP2C8", "ILOPERIDONE	CYP2D6", "INDINAVIR	CYP3A4", "INDINAVIR	CYP3A5", "ITRACONAZOLE	CYP3A4", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "MODAFINIL	CYP2C19", "MODAFINIL-SULFONE	CYP2C19", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "NORFLOXACIN	CYP1A2", "OMEPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PROPAFENONE	CYP1A2", "QUINIDINE	CYP2D6", "RANOLAZINE	CYP2D6", "RANOLAZINE	CYP3A4", "RANOLAZINE	CYP3A5", "RITONAVIR	CYP2D6", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A4", "TELITHROMYCIN	CYP3A5", "TERBINAFINE	CYP2D6", "TERIFLUNOMIDE	CYP2C9", "TRIMETHOPRIM	CYP2C8", "VENLAFAXINE	CYP2D6", "VERAPAMIL	CYP1A2", "VERAPAMIL	CYP3A4", "VERAPAMIL	CYP3A5", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP2C19", "VORICONAZOLE-N-OXIDE	CYP2C9", "VORICONAZOLE-N-OXIDE	CYP3A4", "ZAFIRLUKAST	CYP2C9", "ZAFIRLUKAST	CYP3A4"]

label_inhibits_l = ["AMIODARONE	CYP1A2", "AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "AMIODARONE	CYP3A4", "ATAZANAVIR	CYP3A4", "ATAZANAVIR	CYP3A5", "BUPROPION	CYP2D6", "CELECOXIB	CYP2D6", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A4", "CLARITHROMYCIN	CYP3A5", "DULOXETINE	CYP2D6", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP1A2", "FLUVOXAMINE	CYP2C19", "FLUVOXAMINE	CYP2C9", "ILOPERIDONE	CYP2D6", "INDINAVIR	CYP3A4", "INDINAVIR	CYP3A5", "ITRACONAZOLE	CYP3A4", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "MODAFINIL	CYP2C19", "MODAFINIL-SULFONE	CYP2C19", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "PAROXETINE	CYP2D6", "QUINIDINE	CYP2D6", "RANOLAZINE	CYP2D6", "RANOLAZINE	CYP3A4", "RANOLAZINE	CYP3A5", "RITONAVIR	CYP2D6", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A4", "TELITHROMYCIN	CYP3A5", "TERBINAFINE	CYP2D6", "TERIFLUNOMIDE	CYP2C9", "VENLAFAXINE	CYP2D6", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP2C19", "VORICONAZOLE-N-OXIDE	CYP2C9", "VORICONAZOLE-N-OXIDE	CYP3A4", "ZAFIRLUKAST	CYP2C9", "ZAFIRLUKAST	CYP3A4"]

fda_inhibits_in_viVo = ["AMIODARONE	CYP2C9","AMIODARONE	CYP2D6","ATAZANAVIR	CYP3A4","ATAZANAVIR	CYP3A5","CIMETIDINE	CYP1A2","CIMETIDINE	CYP3A4","CIMETIDINE	CYP3A5","CIPROFLOXACIN	CYP1A2","CLARITHROMYCIN	CYP3A4","CLARITHROMYCIN	CYP3A5","DULOXETINE	CYP2D6","FLUCONAZOLE	CYP2C9","FLUCONAZOLE	CYP3A4","FLUCONAZOLE	CYP3A5","FLUVOXAMINE	CYP1A2","FLUVOXAMINE	CYP2C19","GEMFIBROZIL	CYP2C8","INDINAVIR	CYP3A4","INDINAVIR	CYP3A5","MEXILETINE	CYP1A2","NEFAZODONE	CYP3A4","NEFAZODONE	CYP3A5","NORFLOXACIN	CYP1A2","OMEPRAZOLE	CYP2C19","PROPAFENONE	CYP1A2","RITONAVIR	CYP3A4","RITONAVIR	CYP3A5","SERTRALINE	CYP2D6","TELITHROMYCIN	CYP3A4","TELITHROMYCIN	CYP3A5","TERBINAFINE	CYP2D6","TRIMETHOPRIM	CYP2C8","VERAPAMIL	CYP1A2","VERAPAMIL	CYP3A4","VERAPAMIL	CYP3A5","CLARITHROMYCIN	CYP3A4","ITRACONAZOLE	CYP3A4","KETOCONAZOLE	CYP3A4","NEFAZODONE	CYP3A4","QUINIDINE	CYP2D6","PAROXETINE	CYP2D6","FLUOXETINE	CYP2D6"]

fda_inhibits_in_viTro = ["ALPHA-NAPHTHOFLAVONE	CYP1A2","FURAFYLLINE	CYP1A2","ITRACONAZOLE	CYP3A4","ITRACONAZOLE	CYP3A5","KETOCONAZOLE	CYP3A4","QUINIDINE	CYP2D6","SULPHAPHENAZOLE	CYP2C9"]

for asrt in inhibits_l:
    if asrt in t2_inhibits_l:
        print "Y"
    else:
        print "X"

for asrt in inhibits_l:
    if asrt in t3_inhibits_l:
        print "Y"
    else:
        print "X"


for asrt in inhibits_l:
    if asrt in t4_inhibits_l:
        print "Y"
    else:
        print "X"

for asrt in inhibits_l:
    if asrt in label_inhibits_l:
        print "Y"
    else:
        print "X"

for asrt in inhibits_l:
    if asrt in fda_inhibits_in_viVo:
        print "in viVo"
    else:
        print "X"

for asrt in inhibits_l:
    if asrt in fda_inhibits_in_viVo:
        print "Y"
    else:
        print "X"


for asrt in inhibits_l:
    if asrt in fda_inhibits_in_viTro:
        print "in viTro"
    else:
        print "X"

for asrt in inhibits_l:
    if asrt in fda_inhibits_in_viTro:
        print "Y"
    else:
        print "X"


substrate_l = ["ALPRAZOLAM	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATORVASTATIN	CYP3A4", "BETA-HYDROXY-LOVASTATIN	CYP3A4", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C9", "CINACALCET	CYP3A4", "CINACALCET	CYP1A2", "CINACALCET	CYP2D6", "CITALOPRAM	CYP2C19", "CLARITHROMYCIN	CYP3A4", "CLOZAPINE	CYP3A4", "CLOZAPINE	CYP1A2", "CLOZAPINE	CYP2D6", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DESACETYLDILTIAZEM	CYP2D6", "DESIPRAMINE	CYP2D6", "DEXTROMETHORPHAN	CYP2D6", "DULOXETINE	CYP1A2", "DULOXETINE	CYP2D6", "ESCITALOPRAM	CYP3A4", "ESCITALOPRAM	CYP2D6", "ESZOPICLONE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C9", "FLUVASTATIN	CYP3A4", "FLUVOXAMINE	CYP2D6", "HALOPERIDOL	CYP3A4", "LANSOPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP3A5", "LANSOPRAZOLE	CYP3A4", "LOVASTATIN	CYP3A4", "MIDAZOLAM	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP3A4", "MIRTAZAPINE	CYP3A5", "MODAFINIL	CYP3A4", "N-DEMETHYLDESACETYL-DILTIAZEM	CYP2D6", "N-DESALKYLQUETIAPINE	CYP3A4", "OLANZAPINE	CYP2D6", "OMEPRAZOLE	CYP2C19", "PANTOPRAZOLE	CYP3A4", "PANTOPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PERPHENAZINE	CYP3A4", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2D6", "R-CITALOPRAM	CYP2D6", "R-CITALOPRAM	CYP3A4", "R-DEMETHYLCITALOPRAM	CYP2D6", "RABEPRAZOLE	CYP3A4", "RABEPRAZOLE	CYP2C19", "RABEPRAZOLE	CYP3A5", "RANOLAZINE	CYP2D6", "REDUCED-HALOPERIDOL	CYP3A4", "RISPERIDONE	CYP2D6", "ROSIGLITAZONE	CYP2C8", "S-DEMETHYLCITALOPRAM	CYP2D6", "S-WARFARIN	CYP2C9", "SERTRALINE	CYP2C19", "SIMVASTATIN	CYP3A4", "TAMOXIFEN	CYP2D6", "TAMOXIFEN	CYP3A4", "TAMOXIFEN	CYP2C9", "TAMOXIFEN	CYP3A5", "THEOPHYLLINE	CYP1A2", "THIORIDAZINE	CYP2D6", "TOLBUTAMIDE	CYP2C9", "TRAZODONE	CYP3A4", "TRIAZOLAM	CYP3A4", "VENLAFAXINE	CYP3A4", "VENLAFAXINE	CYP2D6", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "WARFARIN	CYP2C9", "ZAFIRLUKAST	CYP2C9", "ZALEPLON	CYP3A4", "ZIPRASIDONE	CYP3A4", "ZOLPIDEM	CYP3A5", "ZOLPIDEM	CYP3A4"]

t2_substrate_l = ["N-DEMETHYLDESACETYL-DILTIAZEM	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "BETA-HYDROXY-LOVASTATIN	CYP3A4", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CLOZAPINE	CYP2D6", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DESACETYLDILTIAZEM	CYP2D6", "DULOXETINE	CYP2D6", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP2D6", "LOVASTATIN	CYP3A4", "PERPHENAZINE	CYP2D6", "RISPERIDONE	CYP2D6", "SERTRALINE	CYP2C19", "SIMVASTATIN	CYP3A4", "ZIPRASIDONE	CYP3A4", "VENLAFAXINE	CYP2D6", "TOLBUTAMIDE	CYP2C9", "THIORIDAZINE	CYP2D6", "THEOPHYLLINE	CYP1A2", "SILDENAFIL	CYP3A4", "ROSIGLITAZONE	CYP2C8", "PANTOPRAZOLE	CYP2C19", "OMEPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP2C19", "DEXTROMETHORPHAN	CYP2D6", "CAFFEINE	CYP1A2", "S-WARFARIN	CYP2C9", "WARFARIN	CYP2C9", "TRIAZOLAM	CYP3A4", "DESIPRAMINE	CYP2D6", "MIDAZOLAM	CYP3A4"]

t3_substrate_l = ["N-DEMETHYLDESACETYL-DILTIAZEM	CYP2D6", "R-CITALOPRAM	CYP2D6", "R-CITALOPRAM	CYP3A4", "R-DEMETHYLCITALOPRAM	CYP2D6", "S-DEMETHYLCITALOPRAM	CYP2D6", "ALPRAZOLAM	CYP3A4", "ARIPIPRAZOLE	CYP3A4", "ATORVASTATIN	CYP3A4", "BETA-HYDROXY-LOVASTATIN	CYP3A4", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CITALOPRAM	CYP3A4", "CLARITHROMYCIN	CYP3A4", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP3A4", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DESACETYLDILTIAZEM	CYP2D6", "DULOXETINE	CYP2D6", "ESCITALOPRAM	CYP2D6", "ESCITALOPRAM	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP2D6", "HALOPERIDOL	CYP3A4", "LOVASTATIN	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP3A4", "NEFAZODONE	CYP3A4", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP3A4", "REDUCED-HALOPERIDOL	CYP3A4", "RISPERIDONE	CYP2D6", "RISPERIDONE	CYP3A4", "SERTRALINE	CYP2C19", "SIMVASTATIN	CYP3A4", "VENLAFAXINE	CYP2D6", "VENLAFAXINE	CYP3A4", "ZIPRASIDONE	CYP1A2", "ZIPRASIDONE	CYP3A4", "TOLBUTAMIDE	CYP2C9", "THIORIDAZINE	CYP2D6", "THEOPHYLLINE	CYP1A2", "SILDENAFIL	CYP3A4", "ROSIGLITAZONE	CYP2C8", "PANTOPRAZOLE	CYP2C19", "OMEPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP2C19", "DEXTROMETHORPHAN	CYP2D6", "CAFFEINE	CYP1A2", "S-WARFARIN	CYP2C9", "WARFARIN	CYP2C9", "TRIAZOLAM	CYP3A4", "DESIPRAMINE	CYP2D6", "MIDAZOLAM	CYP3A4"]

t4_substrate_l = ["N-DEMETHYLDESACETYL-DILTIAZEM	CYP2D6", "N-DESALKYLQUETIAPINE	CYP3A4", "R-CITALOPRAM	CYP2D6", "R-CITALOPRAM	CYP3A4", "R-DEMETHYLCITALOPRAM	CYP2D6", "S-DEMETHYLCITALOPRAM	CYP2D6", "ALPRAZOLAM	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATORVASTATIN	CYP3A4", "BETA-HYDROXY-LOVASTATIN	CYP3A4", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C9", "CINACALCET	CYP1A2", "CINACALCET	CYP2D6", "CINACALCET	CYP3A4", "CITALOPRAM	CYP2C19", "CLARITHROMYCIN	CYP3A4", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP3A4", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DESACETYLDILTIAZEM	CYP2D6", "DULOXETINE	CYP1A2", "DULOXETINE	CYP2D6", "ESCITALOPRAM	CYP2D6", "ESCITALOPRAM	CYP3A4", "ESZOPICLONE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C9", "FLUVASTATIN	CYP3A4", "FLUVOXAMINE	CYP2D6", "HALOPERIDOL	CYP3A4", "ILOPERIDONE	CYP2D6", "ILOPERIDONE	CYP3A4", "LANSOPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP3A4", "LANSOPRAZOLE	CYP3A5", "LOVASTATIN	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP3A4", "MIRTAZAPINE	CYP3A5", "MODAFINIL	CYP3A4", "NEFAZODONE	CYP3A4", "OLANZAPINE	CYP2D6", "PANTOPRAZOLE	CYP2C19", "PANTOPRAZOLE	CYP3A4", "PAROXETINE	CYP2D6", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP3A4", "RABEPRAZOLE	CYP2C19", "RABEPRAZOLE	CYP3A4", "RABEPRAZOLE	CYP3A5", "RANOLAZINE	CYP2D6", "REDUCED-HALOPERIDOL	CYP3A4", "RISPERIDONE	CYP2D6", "RISPERIDONE	CYP3A4", "SERTRALINE	CYP2C19", "SIMVASTATIN	CYP3A4", "TAMOXIFEN	CYP2C9", "TAMOXIFEN	CYP2D6", "TAMOXIFEN	CYP3A4", "TAMOXIFEN	CYP3A5", "THIORIDAZINE	CYP2D6", "TRAZODONE	CYP3A4", "VENLAFAXINE	CYP2D6", "VENLAFAXINE	CYP3A4", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "ZAFIRLUKAST	CYP2C9", "ZALEPLON	CYP3A4", "ZIPRASIDONE	CYP3A4", "ZOLPIDEM	CYP3A4", "ZOLPIDEM	CYP3A5", "TOLBUTAMIDE	CYP2C9", "SILDENAFIL	CYP3A4", "ROSIGLITAZONE	CYP2C8", "RANOLAZINE	CYP3A4", "OMEPRAZOLE	CYP2C19", "CAFFEINE	CYP1A2", "ATOMOXETINE	CYP2D6", "S-WARFARIN	CYP2C9", "DEXTROMETHORPHAN	CYP2D6", "THEOPHYLLINE	CYP1A2", "WARFARIN	CYP2C9", "TRIAZOLAM	CYP3A4", "DESIPRAMINE	CYP2D6", "MIDAZOLAM	CYP3A4", "THEOPHYLLINE	CYP3A4", "THEOPHYLLINE	CYP2E1", "ROSUVASTATIN	CYP2C9", "ATOMOXETINE	CYP2C19", "BUPROPION	CYP2B6"]

label_substrate_of = ["N-DESALKYLQUETIAPINE	CYP3A4", "ALPRAZOLAM	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATOMOXETINE	CYP2C19", "ATOMOXETINE	CYP2D6", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2B6", "CAFFEINE	CYP1A2", "CELECOXIB	CYP2C9", "CINACALCET	CYP1A2", "CINACALCET	CYP2D6", "CINACALCET	CYP3A4", "CITALOPRAM	CYP2C19", "CLOZAPINE	CYP1A2", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP3A4", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DULOXETINE	CYP1A2", "DULOXETINE	CYP2D6", "ESCITALOPRAM	CYP2C19", "ESZOPICLONE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C9", "FLUVASTATIN	CYP3A4", "FLUVOXAMINE	CYP2D6", "ILOPERIDONE	CYP2D6", "ILOPERIDONE	CYP3A4", "LANSOPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP3A4", "LANSOPRAZOLE	CYP3A5", "LOVASTATIN	CYP3A4", "MIDAZOLAM	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP3A4", "MIRTAZAPINE	CYP3A5", "MODAFINIL	CYP3A4", "OLANZAPINE	CYP2D6", "PANTOPRAZOLE	CYP2C19", "PANTOPRAZOLE	CYP3A4", "PAROXETINE	CYP2D6", "QUETIAPINE	CYP3A4", "RABEPRAZOLE	CYP2C19", "RABEPRAZOLE	CYP3A4", "RABEPRAZOLE	CYP3A5", "RANOLAZINE	CYP2D6", "RANOLAZINE	CYP3A4", "RISPERIDONE	CYP2D6", "ROSUVASTATIN	CYP2C9", "S-WARFARIN	CYP2C9", "TAMOXIFEN	CYP2C9", "TAMOXIFEN	CYP2D6", "TAMOXIFEN	CYP3A4", "TAMOXIFEN	CYP3A5", "THEOPHYLLINE	CYP1A2", "THEOPHYLLINE	CYP2E1", "THEOPHYLLINE	CYP3A4", "THIORIDAZINE	CYP2D6", "TRAZODONE	CYP3A4", "VENLAFAXINE	CYP2D6", "VENLAFAXINE	CYP3A4", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "ZAFIRLUKAST	CYP2C9", "ZALEPLON	CYP3A4", "ZIPRASIDONE	CYP3A4", "ZOLPIDEM	CYP3A4", "ZOLPIDEM	CYP3A5"]

fda_substrate_of_in_viVo = ["CAFFEINE	CYP1A2", "DEXTROMETHORPHAN	CYP2D6", "MIDAZOLAM	CYP3A4", "SILDENAFIL	CYP3A4", "TRIAZOLAM	CYP3A4", "WARFARIN	CYP2C9", "DEXTROMETHORPHAN	CYP2D6", "THIORIDAZINE	CYP2D6"]

fda_substrate_of_in_viTro = ["7-ETHOXYRESORUFIN	CYP1A2", "S-MEPHENYTOIN	CYP2C19", "S-WARFARIN	CYP2C9", "BUFURALOL	CYP2D6", "CHLORZOXAZONE	CYP2E1", "COUMARIN	CYP2A6", "DEBRISOQUINE	CYP2D6", "DEXTROMETHORPHAN	CYP2D6", "ERYTHROMYCIN	CYP3A4", "MIDAZOLAM	CYP3A4", "OMEPRAZOLE	CYP2C19", "P-NITROPHENOL	CYP2E1", "PHENACETIN	CYP1A2", "TESTOSTERONE	CYP3A4", "TOLBUTAMIDE	CYP2C9", "TRIAZOLAM	CYP3A4"]

for asrt in substrate_l:
    if asrt in t2_substrate_l:
        print "Y"
    else:
        print "X"

for asrt in substrate_l:
    if asrt in t3_substrate_l:
        print "Y"
    else:
        print "X"


for asrt in substrate_l:
    if asrt in t4_substrate_of:
        print "Y"
    else:
        print "X"

for asrt in substrate_l:
    if asrt in label_substrate_of:
        print "Y"
    else:
        print "X"

for asrt in substrate_l:
    if asrt in fda_substrate_of_in_viVo:
        print "in viVo"
    else:
        print "X"

for asrt in substrate_l:
    if asrt in fda_substrate_of_in_viVo:
        print "Y"
    else:
        print "X"


for asrt in substrate_l:
    if asrt in fda_substrate_of_in_viTro:
        print "in viTro"
    else:
        print "X"

for asrt in substrate_l:
    if asrt in fda_substrate_of_in_viTro:
        print "Y"
    else:
        print "X"

not_substrate_l = ["ALPRAZOLAM	CYP1A2", "ARIPIPRAZOLE	CYP1A2", "CITALOPRAM	CYP3A4", "CLARITHROMYCIN	CYP1A2", "CLARITHROMYCIN	CYP2C9", "CLARITHROMYCIN	CYP2D6", "CLOZAPINE-N-OXIDE	CYP2D6", "DESVENLAFAXINE	CYP2D6", "ROSUVASTATIN	CYP3A4", "ZALEPLON	CYP2D6"]

t2_not_substrate_l = ["CLOZAPINE-N-OXIDE	CYP2D6", "DESVENLAFAXINE	CYP2D6"]

t3_not_substrate_l = ["ALPRAZOLAM	CYP1A2", "CLARITHROMYCIN	CYP1A2", "CLARITHROMYCIN	CYP2C9", "CLARITHROMYCIN	CYP2D6", "CLOZAPINE-N-OXIDE	CYP2D6", "DESVENLAFAXINE	CYP2D6", "NEFAZODONE	CYP2D6"]

t4_not_substrate_l = ["ALPRAZOLAM	CYP1A2", "ARIPIPRAZOLE	CYP1A1", "ARIPIPRAZOLE	CYP1A2", "ARIPIPRAZOLE	CYP2A6", "ARIPIPRAZOLE	CYP2B6", "ARIPIPRAZOLE	CYP2C19", "ARIPIPRAZOLE	CYP2C8", "ARIPIPRAZOLE	CYP2C9", "ARIPIPRAZOLE	CYP2E1", "ASENAPINE	CYP2D6", "CLARITHROMYCIN	CYP1A2", "CLARITHROMYCIN	CYP2C9", "CLARITHROMYCIN	CYP2D6", "CLOZAPINE-N-OXIDE	CYP2D6", "DESVENLAFAXINE	CYP2D6", "ILOPERIDONE	CYP1A1", "ILOPERIDONE	CYP1A2", "ILOPERIDONE	CYP2A6", "ILOPERIDONE	CYP2B6", "ILOPERIDONE	CYP2C19", "ILOPERIDONE	CYP2C8", "ILOPERIDONE	CYP2C9", "ILOPERIDONE	CYP2E1", "NEFAZODONE	CYP2D6", "ROSUVASTATIN	CYP3A4", "ZALEPLON	CYP2D6"]

label_not_substrate_of = ["ARIPIPRAZOLE	CYP1A1", "ARIPIPRAZOLE	CYP1A2", "ARIPIPRAZOLE	CYP2A6", "ARIPIPRAZOLE	CYP2B6", "ARIPIPRAZOLE	CYP2C19", "ARIPIPRAZOLE	CYP2C8", "ARIPIPRAZOLE	CYP2C9", "ARIPIPRAZOLE	CYP2E1", "ASENAPINE	CYP2D6", "CITALOPRAM	CYP3A4", "ILOPERIDONE	CYP1A1", "ILOPERIDONE	CYP1A2", "ILOPERIDONE	CYP2A6", "ILOPERIDONE	CYP2B6", "ILOPERIDONE	CYP2C19", "ILOPERIDONE	CYP2C8", "ILOPERIDONE	CYP2C9", "ILOPERIDONE	CYP2E1", "ROSUVASTATIN	CYP3A4", "ZALEPLON	CYP2D6", "ZIPRASIDONE	CYP1A2"]

for asrt in not_substrate_l:
    if asrt in t2_not_substrate_l:
        print "Y"
    else:
        print "X"

for asrt in not_substrate_l:
    if asrt in t3_not_substrate_l:
        print "Y"
    else:
        print "X"


for asrt in not_substrate_l:
    if asrt in t4_not_substrate_l:
        print "Y"
    else:
        print "X"

for asrt in not_substrate_l:
    if asrt in label_not_substrate_of:
        print "Y"
    else:
        print "X"


not_inhibits_l = ["N-DESALKYLQUETIAPINE	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ATOMOXETINE	CYP1A2", "ATORVASTATIN	CYP2C8", "BETA-HYDROXY-LOVASTATIN	CYP2C8", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C9", "CHLORPROMAZINE	CYP2C19", "CINACALCET	CYP2C19", "CITALOPRAM	CYP2C9", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP2C19", "DEHYDRO-ARIPIPRAZOLE	CYP1A2", "DEMETHYLCITALOPRAM	CYP3A4", "DULOXETINE	CYP2C19", "ESCITALOPRAM	CYP2C19", "ESZOPICLONE	CYP2E1", "FLUPHENAZINE	CYP2C19", "FLUPHENAZINE	CYP2D6", "FLUPHENAZINE	CYP1A2", "FLUVASTATIN	CYP2C8", "HALOPERIDOL	CYP2C19", "LANSOPRAZOLE	CYP2D6", "LOVASTATIN	CYP2C8", "OMEPRAZOLE	CYP2D6", "PALIPERIDONE	CYP3A4", "PANTOPRAZOLE	CYP2D6", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2C19", "PRAVASTATIN	CYP2C8", "QUETIAPINE	CYP3A4", "R-CITALOPRAM	CYP1A2", "R-DEMETHYLCITALOPRAM	CYP2C19", "R-DIDEMETHYLCITALOPRAM	CYP1A2", "RISPERIDONE	CYP2C19", "RISPERIDONE	CYP2D6", "ROSUVASTATIN	CYP2C8", "S-DEMETHYLCITALOPRAM	CYP2C9", "S-DIDEMETHYLCITALOPRAM	CYP2D6", "SIMVASTATIN	CYP3A4", "THIORIDAZINE	CYP2C19", "THIOTHIXENE	CYP2C19", "TOPIRAMATE	CYP2B6", "VENLAFAXINE	CYP2C9", "ZIPRASIDONE	CYP2D6"]

t2_not_inhibits_l = ["R-CITALOPRAM	CYP1A2", "R-CITALOPRAM	CYP2C19", "R-CITALOPRAM	CYP2C9", "R-CITALOPRAM	CYP2D6", "R-DEMETHYLCITALOPRAM	CYP1A2", "R-DEMETHYLCITALOPRAM	CYP2C19", "R-DEMETHYLCITALOPRAM	CYP2C9", "R-DIDEMETHYLCITALOPRAM	CYP1A2", "R-DIDEMETHYLCITALOPRAM	CYP2D6", "S-DEMETHYLCITALOPRAM	CYP1A2", "S-DEMETHYLCITALOPRAM	CYP2C19", "S-DEMETHYLCITALOPRAM	CYP2C9", "S-DIDEMETHYLCITALOPRAM	CYP1A2", "S-DIDEMETHYLCITALOPRAM	CYP2D6", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CHLORPROMAZINE	CYP2C19", "CITALOPRAM	CYP2C9", "CITALOPRAM	CYP3A4", "CLOZAPINE	CYP2C19", "DEMETHYLCITALOPRAM	CYP3A4", "ESCITALOPRAM	CYP1A2", "ESCITALOPRAM	CYP2C19", "ESCITALOPRAM	CYP2C9", "ESCITALOPRAM	CYP2D6", "FLUPHENAZINE	CYP2C19", "HALOPERIDOL	CYP2C19", "LANSOPRAZOLE	CYP2D6", "LANSOPRAZOLE	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2C19", "MIRTAZAPINE	CYP2C9", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP2E1", "OMEPRAZOLE	CYP2D6", "PANTOPRAZOLE	CYP2D6", "PERPHENAZINE	CYP2C19", "PRAVASTATIN	CYP2C8", "RISPERIDONE	CYP2C19", "ROSUVASTATIN	CYP2C8", "SIMVASTATIN	CYP3A4", "THIORIDAZINE	CYP2C19", "THIOTHIXENE	CYP2C19", "TOPIRAMATE	CYP1A2", "TOPIRAMATE	CYP2A6", "TOPIRAMATE	CYP2C9", "TOPIRAMATE	CYP2E1", "TOPIRAMATE	CYP3A4", "VENLAFAXINE	CYP1A2", "VENLAFAXINE	CYP2C9", "VENLAFAXINE	CYP3A4", "ZIPRASIDONE	CYP1A2", "ZIPRASIDONE	CYP2C19", "ZIPRASIDONE	CYP2C9", "ZIPRASIDONE	CYP2D6", "RISPERIDONE	CYP2D6", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP1A2", "OLANZAPINE	CYP3A4", "OLANZAPINE	CYP2C9", "OLANZAPINE	CYP2C19", "LOVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C8", "FLUPHENAZINE	CYP2D6", "FLUPHENAZINE	CYP1A2", "FLUOXETINE	CYP3A4", "CLOZAPINE	CYP3A4", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP2C9", "BETA-HYDROXY-LOVASTATIN	CYP2C8", "ATORVASTATIN	CYP2C8"]

t3_not_inhibits_l = ["R-CITALOPRAM	CYP1A2", "R-CITALOPRAM	CYP2C19", "R-CITALOPRAM	CYP2C9", "R-CITALOPRAM	CYP2D6", "R-DEMETHYLCITALOPRAM	CYP1A2", "R-DEMETHYLCITALOPRAM	CYP2C19", "R-DEMETHYLCITALOPRAM	CYP2C9", "R-DIDEMETHYLCITALOPRAM	CYP1A2", "R-DIDEMETHYLCITALOPRAM	CYP2D6", "S-DEMETHYLCITALOPRAM	CYP1A2", "S-DEMETHYLCITALOPRAM	CYP2C19", "S-DEMETHYLCITALOPRAM	CYP2C9", "S-DIDEMETHYLCITALOPRAM	CYP1A2", "S-DIDEMETHYLCITALOPRAM	CYP2D6", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CHLORPROMAZINE	CYP2C19", "CITALOPRAM	CYP2C9", "CITALOPRAM	CYP3A4", "CLOZAPINE	CYP2C19", "DEMETHYLCITALOPRAM	CYP3A4", "ESCITALOPRAM	CYP1A2", "ESCITALOPRAM	CYP2C19", "ESCITALOPRAM	CYP2C9", "ESCITALOPRAM	CYP2D6", "FLUPHENAZINE	CYP2C19", "HALOPERIDOL	CYP2C19", "LANSOPRAZOLE	CYP2D6", "LANSOPRAZOLE	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2C19", "MIRTAZAPINE	CYP2C9", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP2E1", "OMEPRAZOLE	CYP2D6", "PANTOPRAZOLE	CYP2D6", "PERPHENAZINE	CYP2C19", "PRAVASTATIN	CYP2C8", "RISPERIDONE	CYP2C19", "ROSUVASTATIN	CYP2C8", "SIMVASTATIN	CYP3A4", "THIORIDAZINE	CYP2C19", "THIOTHIXENE	CYP2C19", "TOPIRAMATE	CYP1A2", "TOPIRAMATE	CYP2A6", "TOPIRAMATE	CYP2C9", "TOPIRAMATE	CYP2E1", "TOPIRAMATE	CYP3A4", "VENLAFAXINE	CYP1A2", "VENLAFAXINE	CYP2C9", "VENLAFAXINE	CYP3A4", "ZIPRASIDONE	CYP1A2", "ZIPRASIDONE	CYP2C19", "ZIPRASIDONE	CYP2C9", "ZIPRASIDONE	CYP2D6", "RISPERIDONE	CYP2D6", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP1A2", "OLANZAPINE	CYP3A4", "OLANZAPINE	CYP2C9", "OLANZAPINE	CYP2C19", "LOVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C8", "FLUPHENAZINE	CYP2D6", "FLUPHENAZINE	CYP1A2", "FLUOXETINE	CYP3A4", "CLOZAPINE	CYP3A4", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP2C9", "BETA-HYDROXY-LOVASTATIN	CYP2C8", "ATORVASTATIN	CYP2C8"]

t4_not_inhibits_l = ["N-DESALKYLQUETIAPINE	CYP1A2", "N-DESALKYLQUETIAPINE	CYP2C19", "N-DESALKYLQUETIAPINE	CYP2C9", "N-DESALKYLQUETIAPINE	CYP2D6", "N-DESALKYLQUETIAPINE	CYP3A4", "R-CITALOPRAM	CYP1A2", "R-CITALOPRAM	CYP2C19", "R-CITALOPRAM	CYP2C9", "R-CITALOPRAM	CYP2D6", "R-DEMETHYLCITALOPRAM	CYP1A2", "R-DEMETHYLCITALOPRAM	CYP2C19", "R-DEMETHYLCITALOPRAM	CYP2C9", "R-DIDEMETHYLCITALOPRAM	CYP1A2", "R-DIDEMETHYLCITALOPRAM	CYP2D6", "S-DEMETHYLCITALOPRAM	CYP1A2", "S-DEMETHYLCITALOPRAM	CYP2C19", "S-DEMETHYLCITALOPRAM	CYP2C9", "S-DIDEMETHYLCITALOPRAM	CYP1A2", "S-DIDEMETHYLCITALOPRAM	CYP2D6", "ARIPIPRAZOLE	CYP1A2", "ARIPIPRAZOLE	CYP2C19", "ARIPIPRAZOLE	CYP2C9", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATAZANAVIR	CYP1A2", "ATAZANAVIR	CYP2A6", "ATAZANAVIR	CYP2B6", "ATAZANAVIR	CYP2C19", "ATAZANAVIR	CYP2C9", "ATAZANAVIR	CYP2D6", "ATAZANAVIR	CYP2E1", "ATOMOXETINE	CYP1A2", "ATOMOXETINE	CYP2C9", "ATOMOXETINE	CYP2D6", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C19", "CELECOXIB	CYP2C9", "CELECOXIB	CYP3A4", "CHLORPROMAZINE	CYP2C19", "CINACALCET	CYP1A2", "CINACALCET	CYP2C19", "CINACALCET	CYP2C9", "CINACALCET	CYP3A4", "CINACALCET	CYP3A5", "CITALOPRAM	CYP2C9", "CITALOPRAM	CYP2E1", "CITALOPRAM	CYP3A4", "CLOZAPINE	CYP2C19", "DEHYDRO-ARIPIPRAZOLE	CYP1A2", "DEMETHYLCITALOPRAM	CYP3A4", "DULOXETINE	CYP2C19", "DULOXETINE	CYP2C9", "DULOXETINE	CYP3A4", "DULOXETINE	CYP3A5", "ESCITALOPRAM	CYP1A2", "ESCITALOPRAM	CYP2C19", "ESCITALOPRAM	CYP2C9", "ESCITALOPRAM	CYP2E1", "ESZOPICLONE	CYP1A2", "ESZOPICLONE	CYP2A6", "ESZOPICLONE	CYP2C19", "ESZOPICLONE	CYP2C9", "ESZOPICLONE	CYP2D6", "ESZOPICLONE	CYP2E1", "ESZOPICLONE	CYP3A4", "FLUPHENAZINE	CYP2C19", "HALOPERIDOL	CYP2C19", "INDINAVIR	CYP1A2", "INDINAVIR	CYP2B6", "INDINAVIR	CYP2C9", "INDINAVIR	CYP2E1", "LANSOPRAZOLE	CYP2D6", "LANSOPRAZOLE	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2C19", "MIRTAZAPINE	CYP2C9", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP2E1", "MONTELUKAST	CYP1A2", "MONTELUKAST	CYP2A6", "MONTELUKAST	CYP2C19", "MONTELUKAST	CYP2C8", "MONTELUKAST	CYP2C9", "MONTELUKAST	CYP2D6", "MONTELUKAST	CYP3A4", "NEFAZODONE	CYP1A2", "OMEPRAZOLE	CYP2D6", "PALIPERIDONE	CYP1A2", "PALIPERIDONE	CYP2A6", "PALIPERIDONE	CYP2C19", "PALIPERIDONE	CYP2C8", "PALIPERIDONE	CYP2C9", "PALIPERIDONE	CYP2D6", "PALIPERIDONE	CYP2E1", "PALIPERIDONE	CYP3A4", "PALIPERIDONE	CYP3A5", "PANTOPRAZOLE	CYP2D6", "PERPHENAZINE	CYP2C19", "PRAVASTATIN	CYP2C8", "QUETIAPINE	CYP1A2", "QUETIAPINE	CYP2C19", "QUETIAPINE	CYP2C9", "QUETIAPINE	CYP2D6", "QUETIAPINE	CYP3A4", "RISPERIDONE	CYP2C19", "ROSIGLITAZONE	CYP1A1", "ROSIGLITAZONE	CYP1A2", "ROSIGLITAZONE	CYP2A6", "ROSIGLITAZONE	CYP2B6", "ROSIGLITAZONE	CYP2C19", "ROSIGLITAZONE	CYP2C8", "ROSIGLITAZONE	CYP2C9", "ROSIGLITAZONE	CYP2D6", "ROSIGLITAZONE	CYP2E1", "ROSIGLITAZONE	CYP3A4", "ROSIGLITAZONE	CYP3A5", "ROSUVASTATIN	CYP2C8", "SIMVASTATIN	CYP3A4", "THIORIDAZINE	CYP2C19", "THIOTHIXENE	CYP2C19", "TOPIRAMATE	CYP1A2", "TOPIRAMATE	CYP2A6", "TOPIRAMATE	CYP2B6", "TOPIRAMATE	CYP2C19", "TOPIRAMATE	CYP2C9", "TOPIRAMATE	CYP2D6", "TOPIRAMATE	CYP2E1", "TOPIRAMATE	CYP3A4", "TOPIRAMATE	CYP3A5", "VENLAFAXINE	CYP1A2", "VENLAFAXINE	CYP2C9", "VENLAFAXINE	CYP3A4", "ZIPRASIDONE	CYP1A2", "ZIPRASIDONE	CYP2C19", "ZIPRASIDONE	CYP2C9", "ZIPRASIDONE	CYP2D6", "ZIPRASIDONE	CYP3A4", "RISPERIDONE	CYP2D6", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP1A2", "OLANZAPINE	CYP3A4", "OLANZAPINE	CYP2C9", "OLANZAPINE	CYP2C19", "LOVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C8", "FLUPHENAZINE	CYP2D6", "FLUPHENAZINE	CYP1A2", "FLUOXETINE	CYP3A4", "CLOZAPINE	CYP3A4", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP2C9", "BETA-HYDROXY-LOVASTATIN	CYP2C8", "ATORVASTATIN	CYP2C8"]

label_not_inhibits_l = ["N-DESALKYLQUETIAPINE	CYP1A2", "N-DESALKYLQUETIAPINE	CYP2C19", "N-DESALKYLQUETIAPINE	CYP2C9", "N-DESALKYLQUETIAPINE	CYP2D6", "N-DESALKYLQUETIAPINE	CYP3A4", "ARIPIPRAZOLE	CYP1A2", "ARIPIPRAZOLE	CYP2C19", "ARIPIPRAZOLE	CYP2C9", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATAZANAVIR	CYP1A2", "ATAZANAVIR	CYP2A6", "ATAZANAVIR	CYP2B6", "ATAZANAVIR	CYP2C19", "ATAZANAVIR	CYP2C9", "ATAZANAVIR	CYP2D6", "ATAZANAVIR	CYP2E1", "ATOMOXETINE	CYP1A2", "ATOMOXETINE	CYP2C9", "ATOMOXETINE	CYP2D6", "CELECOXIB	CYP2C19", "CELECOXIB	CYP2C9", "CELECOXIB	CYP3A4", "CINACALCET	CYP1A2", "CINACALCET	CYP2C19", "CINACALCET	CYP2C9", "CINACALCET	CYP3A4", "CINACALCET	CYP3A5", "CITALOPRAM	CYP2C9", "CITALOPRAM	CYP2E1", "CITALOPRAM	CYP3A4", "DEHYDRO-ARIPIPRAZOLE	CYP1A2", "DULOXETINE	CYP2C19", "DULOXETINE	CYP2C9", "DULOXETINE	CYP3A4", "DULOXETINE	CYP3A5", "ESCITALOPRAM	CYP2C19", "ESCITALOPRAM	CYP2C9", "ESCITALOPRAM	CYP2E1", "ESZOPICLONE	CYP1A2", "ESZOPICLONE	CYP2A6", "ESZOPICLONE	CYP2C19", "ESZOPICLONE	CYP2C9", "ESZOPICLONE	CYP2D6", "ESZOPICLONE	CYP2E1", "ESZOPICLONE	CYP3A4", "INDINAVIR	CYP1A2", "INDINAVIR	CYP2B6", "INDINAVIR	CYP2C9", "INDINAVIR	CYP2E1", "MONTELUKAST	CYP1A2", "MONTELUKAST	CYP2A6", "MONTELUKAST	CYP2C19", "MONTELUKAST	CYP2C8", "MONTELUKAST	CYP2C9", "MONTELUKAST	CYP2D6", "MONTELUKAST	CYP3A4", "NEFAZODONE	CYP1A2", "PALIPERIDONE	CYP1A2", "PALIPERIDONE	CYP2A6", "PALIPERIDONE	CYP2C19", "PALIPERIDONE	CYP2C8", "PALIPERIDONE	CYP2C9", "PALIPERIDONE	CYP2D6", "PALIPERIDONE	CYP2E1", "PALIPERIDONE	CYP3A4", "PALIPERIDONE	CYP3A5", "QUETIAPINE	CYP1A2", "QUETIAPINE	CYP2C19", "QUETIAPINE	CYP2C9", "QUETIAPINE	CYP2D6", "QUETIAPINE	CYP3A4", "ROSIGLITAZONE	CYP1A1", "ROSIGLITAZONE	CYP1A2", "ROSIGLITAZONE	CYP2A6", "ROSIGLITAZONE	CYP2B6", "ROSIGLITAZONE	CYP2C19", "ROSIGLITAZONE	CYP2C8", "ROSIGLITAZONE	CYP2C9", "ROSIGLITAZONE	CYP2D6", "ROSIGLITAZONE	CYP2E1", "ROSIGLITAZONE	CYP3A4", "ROSIGLITAZONE	CYP3A5", "TOPIRAMATE	CYP1A2", "TOPIRAMATE	CYP2A6", "TOPIRAMATE	CYP2B6", "TOPIRAMATE	CYP2C19", "TOPIRAMATE	CYP2C9", "TOPIRAMATE	CYP2D6", "TOPIRAMATE	CYP2E1", "TOPIRAMATE	CYP3A4", "TOPIRAMATE	CYP3A5", "VENLAFAXINE	CYP1A2", "VENLAFAXINE	CYP2C9", "VENLAFAXINE	CYP3A4", "ZIPRASIDONE	CYP1A2", "ZIPRASIDONE	CYP2C19", "ZIPRASIDONE	CYP2C9", "ZIPRASIDONE	CYP2D6", "ZIPRASIDONE	CYP3A4"]

for asrt in not_inhibits_l:
    if asrt in t2_not_inhibits_l:
        print "Y"
    else:
        print "X"

for asrt in not_inhibits_l:
    if asrt in t3_not_inhibits_l:
        print "Y"
    else:
        print "X"


for asrt in not_inhibits_l:
    if asrt in t4_not_inhibits_l:
        print "Y"
    else:
        print "X"

for asrt in not_inhibits_l:
    if asrt in label_not_inhibits_l:
        print "Y"
    else:
        print "X"


######## Get all assertions that are supported by an FDA guidance statement
kys = ev.objects.keys()
kys.sort()

for e in kys:
    v = ev.objects[e]
    if v.slot in ["maximum_therapeutic_dose", "minimum_therapeutic_dose"]:
        continue 

    for evd in v.evidence_for:
        if evd.evidence_type.value == "Non_Tracable_Statement":
            #print "(for) %s : %s" % (e, evd.quote.replace("\n", " ")) # NOTE: this exposes some bug during string creation that causes the quote to be replaced with a newline for 'theophylline_primary_total_clearance_enzyme_cyp1a2'
            print "(for) %s : %s" % (e, evd.quote)

# (for) 7-ethoxyresorufin_in_vitro_probe_substrate_of_enzyme_cyp1a2 : The FDA recommends 7-ethoxyresorufin to be an acceptable chemical CYP1A2 substrate (7-ethoxyresorufin O-deethylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) S-mephenytoin_in_vitro_probe_substrate_of_enzyme_cyp2c19 : The FDA recommends S-mepheytoin to be an acceptable chemical CYP2C19 substrate (S-mephenytoin 4' hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) S-warfarin_in_vitro_probe_substrate_of_enzyme_cyp2c9 : The FDA recommends S-warfarin to be an acceptable chemical CYP2C9 substrate (S-warfarin 7-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) S-warfarin_primary_total_clearance_enzyme_cyp2c9 : 
# The FDA recommends warfarin as a preferred CYP2C9 substrate for in vivo studies in it most recent guidance document (See Table 2, p. 19) and expressly mentions that S-warfarin should be target of chemical analysis on 9, 1st paragraph.
# (for) alpha-naphthoflavone_in_vitro_selective_inhibitor_of_enzyme_cyp1a2 : he FDA recommends this as a acceptable chemical CYP1A2 inhibitor for in vitro experiments in it most recent guidance document. See Table 2, p. 28
# (for) alprazolam_primary_total_clearance_mechanism_Metabolic_Clearance : In this narrative review the authors state that &quot;only about 20% of the administered dose [is] excreted as unchanged alprazolam&quot; citing Reineke et al 1978. However, I cannot get access to the cited reference.
# (for) alprazolam_primary_total_clearance_mechanism_Metabolic_Clearance : Table 1 of this paper states that, on average, 21.4% of an oral dose of alprazolam is excreted in urine. The table does not seem to be the product of the study described in this evidence item. Prior to referring to the table, the authors cite a paper produced by the drug's manufacturer (Upjohn) but I am unable to acquire this article.
# (for) amiodarone_inhibits_cyp2c9 : The FDA recommends this as a CYPC9 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) amiodarone_inhibits_cyp2d6 : The FDA notes that this is a weak CYP2D6 inhibitor for in vivo studies in it most recent guidance document. See Table 6, p. 23
# (for) atazanavir_inhibits_cyp3a4 : The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) atazanavir_inhibits_cyp3a5 : The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) atomoxetine_primary_total_clearance_enzyme_cyp2d6 : The FDA recommends this as a preferred CYP2D6 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19 

# CURATOR NOTE (04/29/2009): atomoxetine might have some relevant clearance by CYP2C19 and CYP1A2; evidence is currently being sought 
# (for) bufuralol_in_vitro_probe_substrate_of_enzyme_cyp2d6 : The FDA recommends bufuralol to be an acceptable chemical CYP2D6 substrate (bufuralol 1'-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) caffeine_primary_total_clearance_enzyme_cyp1a2 : The FDA recommends caffeine as a preferred CYP1A2 substrate for in vivo studies in it most recent guidance document (See Table 2, p. 19) 
# (for) chlorzoxazone_in_vitro_probe_substrate_of_enzyme_cyp2e1 : The FDA recommends chlorzoxazone to be an acceptable chemical CYP2E1 substrate (chlorzoxazone 6-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) cimetidine_inhibits_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) cimetidine_inhibits_cyp3a4 : The FDA notes that this is a &quot;weak&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) cimetidine_inhibits_cyp3a5 : The FDA notes that this is a &quot;weak&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) ciprofloxacin_inhibits_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) clarithromycin_in_viVo_selective_inhibitor_of_enzyme_cyp3a4 :  The FDA lists this as a recommended in vivo inhibitor of CYP3A4 in it most recent guidance document. See Appendix A, Table 2, p. 19
# (for) clarithromycin_inhibits_cyp3a4 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) clarithromycin_inhibits_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) clopidogrel_inhibition_constant_cyp2b6 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.5micM. See Table 2, p. 28

# 0.5micM/L X 1M/10^6micM X 321.822g/M = 0.0001609g/L
# (for) coumarin_in_vitro_probe_substrate_of_enzyme_cyp2a6 : The FDA recommends coumarin to be an acceptable chemical CYP2A6 substrate (coumarin 7-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) cyp2d6_controls_formation_of_4-hydroxydebrisoquine : The FDA recommends debrisoquine to be an acceptable chemical CYP2D6 substrate (CYP2D6--&gt;(debrisoquine-&gt;4-OH-debrisoquine)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) debrisoquine_in_vitro_probe_substrate_of_enzyme_cyp2d6 : The FDA recommends this as an acceptable chemical CYP2D6 substrate (CYP2D6--&gt;(debrisoquin-&gt;4-hydroxydebrisoquin)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) desipramine_primary_total_clearance_enzyme_cyp2d6 :  The FDA recommends this as a preferred CYP2D6 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19

# CURATOR NOTE (04/29/2009): desipramine might have some relevant clearance by CYP2C19 and CYP1A2; evidence is currently being sought
# (for) dextromethorphan_in_viVo_probe_substrate_of_enzyme_cyp2d6 : The FDA guidance considers DMT-O-demethylation to be catalyzed selectively by CYP2D6 in vitro (see Table 3 of page 32) and recommends it as an substrate for in vivo DDI PK studies (see Table 2 page 19)
# (for) dextromethorphan_in_vitro_probe_substrate_of_enzyme_cyp2d6 : The FDA guidance considers DMT-O-demethylation to be catalyzed selectively by CYP2D6; see Table 3 of page 32
# (for) dextromethorphan_primary_total_clearance_enzyme_cyp2d6 :  The FDA recommends this as a preferred CYP2D6 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) duloxetine_inhibits_cyp2d6 : duloxetine is listed as a moderate inhibitor in Table 6 (p23) but does not show up in Table 2 (a table listing several selective in viVo inhibitors)
# (for) erythromycin_in_vitro_probe_substrate_of_enzyme_cyp3a4 : The FDA recommends this as a acceptable chemical CYP3A4 substrate (CYP3A4-->(erythromycin->N-Demethyl-erythromycin)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) fluconazole_inhibits_cyp2c9 : 'The FDA recommends this as a CYP2C9 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) fluconazole_inhibits_cyp3a4 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) fluconazole_inhibits_cyp3a5 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) fluoxetine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6 : fluoxetine is listed as a recommended inhibitor for AUC studies in Table 2 (p19)
# (for) fluvoxamine_inhibits_cyp1a2 : Fluvoxamine is listed as a recommended inhibitor of CYP1A2 for in vivo studies in Table 2 (p. 19). Typically, this would qualify it as a in vivo selective inhibitor however, Table 2 also shows fluvoxamine as a recommended inhibitor of 2C19.
# (for) fluvoxamine_inhibits_cyp2c19 : Fluvoxamine is listed as a recommended inhibitor of CYP2C19 for in vivo studies in Table 2 (p. 19). Typically, this would qualify it as a in vivo selective inhibitor however, Table 2 also shows fluvoxamine as a recommended inhibitor of CYP1A2.
# (for) furafylline_in_vitro_selective_inhibitor_of_enzyme_cyp1a2 : the FDA lists this as a accepted in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) gemfibrozil_inhibits_cyp2c8 : 'The FDA recommends this as a CYP2C8 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) indinavir_inhibits_cyp3a4 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) indinavir_inhibits_cyp3a5 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) itraconazole_in_viVo_selective_inhibitor_of_enzyme_cyp3a4 : The FDA lists this as a recommended in vivo inhibitor of CYP3A4 in it most recent guidance document. See Appendix A, Table 2, p. 19
# (for) itraconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a4 : the FDA lists this as a preferred in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) itraconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a5 : the FDA lists this as a preferred in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) ketoconazole_in_viVo_selective_inhibitor_of_enzyme_cyp3a4 :  The FDA lists this as a recommended in vivo inhibitor of CYP3A4 in it most recent guidance document. See Appendix A, Table 2, p. 19
# (for) ketoconazole_in_vitro_selective_inhibitor_of_enzyme_cyp3a4 : the FDA lists this as a preferred in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) lansoprazole_primary_total_clearance_enzyme_cyp2c19 : 
# The FDA recommends this as a CYPC19 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) mephenytoin_in_viVo_probe_substrate_of_enzyme_cyp2c19 : 
# The FDA guidance considers (S)-mephenytoin 4-hydroxylation to be catalyzed selectively by CYP2C19 in vitro (see Table 3 of page 32) and lists it as a 'sensitive' CYP2C19 substrate in vivo (see Table 4 page 21)
# (for) mexiletine_inhibits_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) midazolam_in_vitro_probe_substrate_of_enzyme_cyp3a4 : The FDA recommends this as a preferred chemical CYP3A4 substrate (CYP3A4-->(midazolam->1hydroxy-midazolam)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) midazolam_primary_total_clearance_enzyme_cyp3a4 : The FDA recommends this as a preferred CYP3A4 substrate for in vivo studies  in it most recent guidance document. See Table 2, p. 19
# (for) montelukast_inhibition_constant_cyp2c8 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.1micM. See Table 2, p. 28

# 1.1micM/L X 1M/10^6micM X 586.183g/M = 0.0006448g/L
# (for) nefazodone_in_viVo_selective_inhibitor_of_enzyme_cyp3a4 :  The FDA lists this as a recommended in vivo inhibitor of CYP3A4 in it most recent guidance document. See Appendix A, Table 2, p. 19
# (for) nefazodone_inhibits_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) nefazodone_inhibits_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) norfloxacin_inhibits_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) omeprazole_in_vitro_probe_substrate_of_enzyme_cyp2c19 : The FDA guidance considers omeprazole-5-hydroxylation to be catalyzed selectively by CYP2C19; see Table 3 of page 32
# (for) omeprazole_in_vitro_selective_inhibitor_of_enzyme_cyp2c19 : 
# The FDA lists this as a &quot;strong&quot; CYP2C19 inhibitor in its most recent guidance document. See Tables 2, p19 and 6, p. 23. 

# NOTE: there is no mention of omeprazole as a recommended or acceptable in vitro inhibitor in Table 2, p28
# (for) omeprazole_inhibits_cyp2c19 : 'The FDA recommends this as a CYPC19 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) omeprazole_primary_total_clearance_enzyme_cyp2c19 : 
# The FDA recommends omeprazole as a recommended CYP2C19 substrate for in vivo studies in it most recent guidance document (See Table 2, p. 19)
# (for) p-nitrophenol_in_vitro_probe_substrate_of_enzyme_cyp2e1 : The FDA recommends p-nitrophenol to be an acceptable chemical CYP2E1 substrate (p-nitrophenol 3-hydroxylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) pantoprazole_primary_total_clearance_enzyme_cyp2c19 : 
# The FDA recommends this as a CYPC19 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) paroxetine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6 : paroxetine is listed as a recommended inhibitor for AUC studies in Table 2 (p19)
# (for) phenacetin_in_vitro_probe_substrate_of_enzyme_cyp1a2 : The FDA guidance considers phenacetin-O-deethylation to be catalyzed selectively by CYP1A2; see Table 3 of page 32
# (for) pioglitazone_inhibition_constant_cyp2c8 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 1.7micM. See Table 2, p. 28

# 1.7micM/L X 1M/10^6micM X 356.439g/M = 0.0006059g/L
# (for) propafenone_inhibits_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) quinidine_in_viVo_selective_inhibitor_of_enzyme_cyp2d6 : The FDA lists this as a recommended in viVo inhibitor in it most recent guidance document. See Table 2, p. 19.
# (for) quinidine_in_vitro_selective_inhibitor_of_enzyme_cyp2d6 : the FDA lists this as a accepted in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) ritonavir_inhibits_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) ritonavir_inhibits_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) rosiglitazone_inhibition_constant_cyp2c8 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2C8 for in vitro experiments at a K_i of 5.6micM. See Table 2, p. 28

# 5.6micM/L X 1M/10^6micM X 357.427g/M = 0.002g/L
# (for) rosiglitazone_primary_total_clearance_enzyme_cyp2c8 : 
# The FDA lists this as a accepted in vivo probe substrate for CY2C8 PK clinical trials in this guidance document. See Table 2, p. 22
# (for) sertraline_inhibits_cyp2d6 : Sertraline is listed as a moderate inhibitor in Table 6 (p23) but does not show up in Table 2 (a table listing several selective in viVo inhibitors)
# (for) sildenafil_primary_total_clearance_enzyme_cyp3a4 : The FDA recommends sildenafil as a preferred CYP3A4/3A5 substrate for in vivo studies in it most recent guidance document (See Table 2, p. 19) 
# (for) sulfinpyrazone_in_vitro_selective_inhibitor_of_enzyme_cyp2c9 : 
# The FDA lists this as a weak inhibitor of cyp2c9 in Table 6 of its most recent guidance
# (for) sulphaphenazole_in_vitro_selective_inhibitor_of_enzyme_cyp2c9 : the FDA lists this as a preferred in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
# (for) telithromycin_inhibits_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) telithromycin_inhibits_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (for) terbinafine_inhibits_cyp2d6 : The FDA notes that this is a &quot;moderate&quot; CYP2D6 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) testosterone_in_vitro_probe_substrate_of_enzyme_cyp3a4 : The FDA recommends this as a preferred chemical 3a4 substrate (CYP3A4-->(testosterone -> 6beta-hydroxy-testosterone)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) theophylline_in_vitro_probe_substrate_of_enzyme_cyp1a2 : 
# The FDA recommends theophylline to be an acceptable chemical CYP1A2 substrate (theophylline N-demethylation) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) theophylline_primary_total_clearance_enzyme_cyp1a2 : The FDA recommends this as a preferred CYP1A2 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19

# (for) thioridazine_substrate_of_cyp2d6 : thioridizine is listed in table 4 (p21) as a CYP2D6 substrate with a narrow therapeutic range
# (for) ticlopidine_inhibition_constant_cyp2b6 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2B6 for in vitro experiments at a K_i of 0.2micM. See Table 2, p. 28

# 0.2.micM/L X 1M/10^6micM X 263.876g/M = 0.00005278g/L
# (for) ticlopidine_inhibition_constant_cyp2c19 : The FDA, in it most recent guidance document, recommends this as a chemical inhibitor of CYP2C19 for in vitro experiments at a K_i of 1.2micM. See Table 2, p. 28

# 1.2micM/L X 1M/10^6micM X 263.786g/M = 0.0003165g/L
# (for) tolbutamide_in_vitro_probe_substrate_of_enzyme_cyp2c9 : The FDA recommends tolbutamide to be an acceptable chemical CYP2C9 substrate (tolbutamide methyl-hydroxylation)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) tolbutamide_primary_total_clearance_enzyme_cyp2c9 : 
# The FDA recommends this as a CYPC9 substrate for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (for) triazolam_in_vitro_probe_substrate_of_enzyme_cyp3a4 : The FDA recommends this as an acceptable chemical CYP3A4 substrate (CYP3A4-->(triazolam->4-hydroxytriazolam)) for in vitro experiments in it most recent guidance document. See Table 3, p. 32
# (for) triazolam_primary_total_clearance_enzyme_cyp3a4 : The FDA lists this as a recommended in vivo substrate of CYP3A4 in it most recent guidance document. See Appendix A, Table 2, p. 19
# (for) trimethoprim_inhibits_cyp2c8 : The FDA notes that this is a &quot;weak&quot; CYP2C8 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) troleandomycin_in_vitro_selective_inhibitor_of_enzyme_cyp3a4 : the FDA lists this as a accepted in vitro inhibitor in it most recent guidance document. See Table 2, p. 28
	
# (for) verapamil_inhibits_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (for) verapamil_inhibits_cyp3a4 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) verapamil_inhibits_cyp3a5 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (for) warfarin_primary_total_clearance_enzyme_cyp2c9 : The FDA lists this as a recommended in vivo substrate of CYP2C9 in it most recent guidance document. See Appendix A, Table 2, p. 19

for e in kys:
    v = ev.objects[e]
    if v.slot in ["maximum_therapeutic_dose", "minimum_therapeutic_dose"]:
        continue 
    
    for evd in v.evidence_against:
        if evd.evidence_type.value == "Non_Tracable_Statement":
            print "(against) " + e + " : " + evd.quote

# (against) amiodarone_does_not_inhibit_cyp2c9 : The FDA recommends this as a CYPC9 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (against) amiodarone_does_not_inhibit_cyp2d6 : The FDA notes that this is a weak CYP2D6 inhibitor for in vivo studies in it most recent guidance document. See Table 6, p. 23
# (against) atazanavir_does_not_inhibit_cyp3a4 : The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (against) atazanavir_does_not_inhibit_cyp3a5 : The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19
# (against) cimetidine_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) cimetidine_does_not_inhibit_cyp3a4 : The FDA notes that this is a &quot;weak&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (against) cimetidine_does_not_inhibit_cyp3a5 : The FDA notes that this is a &quot;weak&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (against) ciprofloxacin_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) clarithromycin_does_not_inhibit_cyp3a4 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) clarithromycin_does_not_inhibit_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) duloxetine_does_not_inhibit_cyp2d6 : duloxetine is listed as a moderate inhibitor in Table 6 (p23) but does not show up in Table 2 (a table listing several selective in viVo inhibitors)
# (against) fluconazole_does_not_inhibit_cyp2c9 : 'The FDA recommends this as a CYP2C9 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) fluconazole_does_not_inhibit_cyp3a4 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (against) fluconazole_does_not_inhibit_cyp3a5 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (against) fluvoxamine_does_not_inhibit_cyp1a2 : Fluvoxamine is listed as a recommended inhibitor of CYP1A2 for in vivo studies in Table 2 (p. 19). Typically, this would qualify it as a in vivo selective inhibitor however, Table 2 also shows fluvoxamine as a recommended inhibitor of 2C19.
# (against) fluvoxamine_does_not_inhibit_cyp2c19 : Fluvoxamine is listed as a recommended inhibitor of CYP2C19 for in vivo studies in Table 2 (p. 19). Typically, this would qualify it as a in vivo selective inhibitor however, Table 2 also shows fluvoxamine as a recommended inhibitor of CYP1A2.
# (against) gemfibrozil_does_not_inhibit_cyp2c8 : 'The FDA recommends this as a CYP2C8 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) indinavir_does_not_inhibit_cyp3a4 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) indinavir_does_not_inhibit_cyp3a5 : 'The FDA recommends this as a CYP3A inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) mexiletine_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) nefazodone_does_not_inhibit_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) nefazodone_does_not_inhibit_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) norfloxacin_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) omeprazole_does_not_inhibit_cyp2c19 : 'The FDA recommends this as a CYPC19 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) propafenone_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;moderate&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) ritonavir_does_not_inhibit_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) ritonavir_does_not_inhibit_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) sertraline_does_not_inhibit_cyp2d6 : Sertraline is listed as a moderate inhibitor in Table 6 (p23) but does not show up in Table 2 (a table listing several selective in viVo inhibitors)
# (against) telithromycin_does_not_inhibit_cyp3a4 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) telithromycin_does_not_inhibit_cyp3a5 : 'The FDA recommends this as a CYP3A4/5 inhibitor for in vivo studies in it most recent guidance document. See Table 2, p. 19'
# (against) terbinafine_does_not_inhibit_cyp2d6 : The FDA notes that this is a &quot;moderate&quot; CYP2D6 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) thioridazine_is_not_substrate_of_cyp2d6 : thioridizine is listed in table 4 (p21) as a CYP2D6 substrate with a narrow therapeutic range
# (against) trimethoprim_does_not_inhibit_cyp2c8 : The FDA notes that this is a &quot;weak&quot; CYP2C8 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) verapamil_does_not_inhibit_cyp1a2 : The FDA notes that this is a &quot;weak&quot; CYP1A2 inhibitor in vivo in it most recent guidance document. See Table 6, p23
# (against) verapamil_does_not_inhibit_cyp3a4 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22
# (against) verapamil_does_not_inhibit_cyp3a5 : The FDA notes that this is a &quot;moderate&quot; CYP3A inhibitor in vivo in it most recent guidance document. See Table 5, p22



##################################################################
# mark drug interactions present in various sources 
##################################################################

dikb_ddi_l = ["CITALOPRAM	FLUVOXAMINE", "CITALOPRAM	MODAFINIL", "CITALOPRAM	VORICONAZOLE", "CITALOPRAM	MODAFINIL-SULFONE", "CITALOPRAM	VORICONAZOLE-N-OXIDE", "CITALOPRAM	OMEPRAZOLE", "DULOXETINE	FLUVOXAMINE", "DULOXETINE	BUPROPION", "DULOXETINE	MEXILETINE", "DULOXETINE	PAROXETINE", "DULOXETINE	TERBINAFINE", "DULOXETINE	NORFLOXACIN", "DULOXETINE	CIPROFLOXACIN", "DULOXETINE	CIMETIDINE", "DULOXETINE	PROPAFENONE", "DULOXETINE	VENLAFAXINE", "DULOXETINE	VERAPAMIL", "DULOXETINE	RANOLAZINE", "DULOXETINE	CINACALCET", "DULOXETINE	AMIODARONE", "DULOXETINE	QUINIDINE", "DULOXETINE	SERTRALINE", "DULOXETINE	FLUOXETINE", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	VENLAFAXINE", "ESCITALOPRAM	ATAZANAVIR", "ESCITALOPRAM	TERBINAFINE", "ESCITALOPRAM	INDINAVIR", "ESCITALOPRAM	VORICONAZOLE-N-OXIDE", "ESCITALOPRAM	NEFAZODONE", "ESCITALOPRAM	CIMETIDINE", "ESCITALOPRAM	QUINIDINE", "ESCITALOPRAM	PAROXETINE", "ESCITALOPRAM	ERYTHROMYCIN", "ESCITALOPRAM	FLUCONAZOLE", "ESCITALOPRAM	RITONAVIR", "ESCITALOPRAM	CLARITHROMYCIN", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	TELITHROMYCIN", "ESCITALOPRAM	BUPROPION", "ESCITALOPRAM	FLUOXETINE", "ESCITALOPRAM	ZAFIRLUKAST", "ESCITALOPRAM	KETOCONAZOLE", "ESCITALOPRAM	DULOXETINE", "ESCITALOPRAM	VORICONAZOLE", "ESCITALOPRAM	VERAPAMIL", "ESCITALOPRAM	DILTIAZEM", "ESCITALOPRAM	ATORVASTATIN", "ESCITALOPRAM	SERTRALINE", "ESCITALOPRAM	AMIODARONE", "ESCITALOPRAM	CINACALCET", "ESCITALOPRAM	ITRACONAZOLE", "FLUOXETINE	SERTRALINE", "FLUOXETINE	CINACALCET", "FLUOXETINE	DULOXETINE", "FLUOXETINE	AMIODARONE", "FLUOXETINE	RANOLAZINE", "FLUOXETINE	QUINIDINE", "FLUOXETINE	PAROXETINE", "FLUOXETINE	TERBINAFINE", "FLUOXETINE	VENLAFAXINE", "FLUOXETINE	BUPROPION", "FLUVOXAMINE	RANOLAZINE", "FLUVOXAMINE	DULOXETINE", "FLUVOXAMINE	PAROXETINE", "FLUVOXAMINE	SERTRALINE", "FLUVOXAMINE	BUPROPION", "FLUVOXAMINE	AMIODARONE", "FLUVOXAMINE	VENLAFAXINE", "FLUVOXAMINE	FLUOXETINE", "FLUVOXAMINE	CINACALCET", "FLUVOXAMINE	TERBINAFINE", "FLUVOXAMINE	QUINIDINE"]

micromedex_absent_l = ["CITALOPRAM	FLUVOXAMINE", "CITALOPRAM	MODAFINIL", "CITALOPRAM	VORICONAZOLE", "CITALOPRAM	MODAFINIL-SULFONE", "CITALOPRAM	VORICONAZOLE-N-OXIDE", "CITALOPRAM	OMEPRAZOLE", "DULOXETINE	BUPROPION", "DULOXETINE	MEXILETINE", "DULOXETINE	TERBINAFINE", "DULOXETINE	NORFLOXACIN", "DULOXETINE	CIMETIDINE", "DULOXETINE	PROPAFENONE", "DULOXETINE	VERAPAMIL", "DULOXETINE	RANOLAZINE", "DULOXETINE	CINACALCET", "DULOXETINE	AMIODARONE", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	VENLAFAXINE", "ESCITALOPRAM	ATAZANAVIR", "ESCITALOPRAM	TERBINAFINE", "ESCITALOPRAM	INDINAVIR", "ESCITALOPRAM	VORICONAZOLE-N-OXIDE", "ESCITALOPRAM	NEFAZODONE", "ESCITALOPRAM	QUINIDINE", "ESCITALOPRAM	PAROXETINE", "ESCITALOPRAM	ERYTHROMYCIN", "ESCITALOPRAM	FLUCONAZOLE", "ESCITALOPRAM	RITONAVIR", "ESCITALOPRAM	CLARITHROMYCIN", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	TELITHROMYCIN", "ESCITALOPRAM	BUPROPION", "ESCITALOPRAM	FLUOXETINE", "ESCITALOPRAM	ZAFIRLUKAST", "ESCITALOPRAM	VORICONAZOLE", "ESCITALOPRAM	VERAPAMIL", "ESCITALOPRAM	DILTIAZEM", "ESCITALOPRAM	ATORVASTATIN", "ESCITALOPRAM	SERTRALINE", "ESCITALOPRAM	AMIODARONE", "ESCITALOPRAM	CINACALCET", "ESCITALOPRAM	ITRACONAZOLE", "FLUOXETINE	SERTRALINE", "FLUOXETINE	CINACALCET", "FLUOXETINE	AMIODARONE", "FLUOXETINE	RANOLAZINE", "FLUOXETINE	TERBINAFINE", "FLUVOXAMINE	RANOLAZINE", "FLUVOXAMINE	PAROXETINE", "FLUVOXAMINE	SERTRALINE", "FLUVOXAMINE	AMIODARONE", "FLUVOXAMINE	VENLAFAXINE", "FLUVOXAMINE	FLUOXETINE", "FLUVOXAMINE	CINACALCET", "FLUVOXAMINE	TERBINAFINE", "FLUVOXAMINE	QUINIDINE", "PAROXETINE	SERTRALINE", "PAROXETINE	AMIODARONE", "PAROXETINE	CINACALCET", "PAROXETINE	VENLAFAXINE", "PAROXETINE	TERBINAFINE"]

epocrates_absent_l = ["CITALOPRAM	MODAFINIL", "CITALOPRAM	OMEPRAZOLE", "DULOXETINE	NORFLOXACIN", "DULOXETINE	VERAPAMIL", "DULOXETINE	RANOLAZINE", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	TERBINAFINE", "ESCITALOPRAM	QUINIDINE", "ESCITALOPRAM	FLUCONAZOLE", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	BUPROPION", "ESCITALOPRAM	ZAFIRLUKAST", "ESCITALOPRAM	VERAPAMIL", "ESCITALOPRAM	DILTIAZEM", "ESCITALOPRAM	ATORVASTATIN", "ESCITALOPRAM	AMIODARONE", "ESCITALOPRAM	CINACALCET", "FLUOXETINE	RANOLAZINE", "PAROXETINE	RANOLAZINE"] 


medscape_absent_l = ["CITALOPRAM	FLUVOXAMINE", "CITALOPRAM	MODAFINIL", "CITALOPRAM	VORICONAZOLE", "CITALOPRAM	OMEPRAZOLE", "DULOXETINE	MEXILETINE", "DULOXETINE	PAROXETINE", "DULOXETINE	TERBINAFINE", "DULOXETINE	CIMETIDINE", "DULOXETINE	PROPAFENONE", "DULOXETINE	VENLAFAXINE", "DULOXETINE	VERAPAMIL", "DULOXETINE	RANOLAZINE", "DULOXETINE	CINACALCET", "DULOXETINE	AMIODARONE", "DULOXETINE	QUINIDINE", "DULOXETINE	SERTRALINE", "DULOXETINE	FLUOXETINE", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	VENLAFAXINE", "ESCITALOPRAM	ATAZANAVIR", "ESCITALOPRAM	TERBINAFINE", "ESCITALOPRAM	INDINAVIR", "ESCITALOPRAM	NEFAZODONE", "ESCITALOPRAM	CIMETIDINE", "ESCITALOPRAM	QUINIDINE", "ESCITALOPRAM	PAROXETINE", "ESCITALOPRAM	ERYTHROMYCIN", "ESCITALOPRAM	FLUCONAZOLE", "ESCITALOPRAM	RITONAVIR", "ESCITALOPRAM	CLARITHROMYCIN", "ESCITALOPRAM	RANOLAZINE", "ESCITALOPRAM	TELITHROMYCIN", "ESCITALOPRAM	FLUOXETINE", "ESCITALOPRAM	ZAFIRLUKAST", "ESCITALOPRAM	KETOCONAZOLE", "ESCITALOPRAM	DULOXETINE", "ESCITALOPRAM	VORICONAZOLE", "ESCITALOPRAM	VERAPAMIL", "ESCITALOPRAM	DILTIAZEM", "ESCITALOPRAM	ATORVASTATIN", "ESCITALOPRAM	SERTRALINE", "ESCITALOPRAM	AMIODARONE", "ESCITALOPRAM	CINACALCET", "ESCITALOPRAM	ITRACONAZOLE", "FLUOXETINE	SERTRALINE", "FLUOXETINE	CINACALCET", "FLUOXETINE	DULOXETINE", "FLUOXETINE	AMIODARONE", "FLUOXETINE	RANOLAZINE", "FLUOXETINE	QUINIDINE", "FLUOXETINE	PAROXETINE", "FLUOXETINE	TERBINAFINE", "FLUOXETINE	VENLAFAXINE", "FLUVOXAMINE	RANOLAZINE", "FLUVOXAMINE	PAROXETINE", "FLUVOXAMINE	SERTRALINE", "FLUVOXAMINE	AMIODARONE", "FLUVOXAMINE	VENLAFAXINE", "FLUVOXAMINE	FLUOXETINE", "FLUVOXAMINE	CINACALCET", "FLUVOXAMINE	TERBINAFINE", "FLUVOXAMINE	QUINIDINE", "PAROXETINE	SERTRALINE", "PAROXETINE	FLUOXETINE", "PAROXETINE	AMIODARONE", "PAROXETINE	DULOXETINE", "PAROXETINE	CINACALCET", "PAROXETINE	RANOLAZINE", "PAROXETINE	QUINIDINE", "PAROXETINE	VENLAFAXINE"]

# micromedex
for ddi in dikb_ddi_l:
    if ddi in micromedex_absent_l:
        print 0
    else:
        print 1


# epocrates
for ddi in dikb_ddi_l:
    if ddi in epocrates_absent_l:
        print 0
    else:
        print 1


# medscape
for ddi in dikb_ddi_l:
    if ddi in medscape_absent_l:
        print 0
    else:
        print 1

##########################################################################################

inhibits_l = ["AMIODARONE	CYP2C9", "AMIODARONE	CYP2D6", "ATAZANAVIR	CYP3A5", "ATAZANAVIR	CYP3A4", "ATORVASTATIN	CYP3A4", "BUPROPION	CYP2D6", "CIMETIDINE	CYP3A5", "CIMETIDINE	CYP1A2", "CIMETIDINE	CYP3A4", "CINACALCET	CYP2D6", "CIPROFLOXACIN	CYP1A2", "CLARITHROMYCIN	CYP3A5", "CLARITHROMYCIN	CYP3A4", "DILTIAZEM	CYP3A4", "DULOXETINE	CYP2D6", "ERYTHROMYCIN	CYP3A4", "FLUCONAZOLE	CYP3A5", "FLUCONAZOLE	CYP2C9", "FLUCONAZOLE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVOXAMINE	CYP2C9", "FLUVOXAMINE	CYP1A2", "FLUVOXAMINE	CYP2C19", "GEMFIBROZIL	CYP2C8", "INDINAVIR	CYP3A5", "INDINAVIR	CYP3A4", "ITRACONAZOLE	CYP3A4", "KETOCONAZOLE	CYP3A4", "MEXILETINE	CYP1A2", "MODAFINIL	CYP2C19", "MODAFINIL-SULFONE	CYP2C19", "NEFAZODONE	CYP3A4", "NEFAZODONE	CYP3A5", "NORFLOXACIN	CYP1A2", "OMEPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PROPAFENONE	CYP1A2", "QUINIDINE	CYP2D6", "RANOLAZINE	CYP2D6", "RANOLAZINE	CYP3A4", "RANOLAZINE	CYP3A5", "RITONAVIR	CYP3A4", "RITONAVIR	CYP3A5", "SERTRALINE	CYP2D6", "TELITHROMYCIN	CYP3A5", "TELITHROMYCIN	CYP3A4", "TERBINAFINE	CYP2D6", "TERIFLUNOMIDE	CYP2C9", "TRIMETHOPRIM	CYP2C8", "VENLAFAXINE	CYP2D6", "VERAPAMIL	CYP3A4", "VERAPAMIL	CYP1A2", "VERAPAMIL	CYP3A5", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP3A4", "VORICONAZOLE-N-OXIDE	CYP2C19", "VORICONAZOLE-N-OXIDE	CYP2C9", "ZAFIRLUKAST	CYP2C9", "ZAFIRLUKAST	CYP3A4"]

substrate_l = ["ALPRAZOLAM	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ARIPIPRAZOLE	CYP3A4", "ATORVASTATIN	CYP3A4", "BETA-HYDROXY-LOVASTATIN	CYP3A4", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C9", "CINACALCET	CYP3A4", "CINACALCET	CYP1A2", "CINACALCET	CYP2D6", "CITALOPRAM	CYP2C19", "CLARITHROMYCIN	CYP3A4", "CLOZAPINE	CYP3A4", "CLOZAPINE	CYP1A2", "CLOZAPINE	CYP2D6", "DEHYDRO-ARIPIPRAZOLE	CYP3A4", "DESACETYLDILTIAZEM	CYP2D6", "DESIPRAMINE	CYP2D6", "DEXTROMETHORPHAN	CYP2D6", "DULOXETINE	CYP1A2", "DULOXETINE	CYP2D6", "ESCITALOPRAM	CYP3A4", "ESCITALOPRAM	CYP2D6", "ESZOPICLONE	CYP3A4", "FLUOXETINE	CYP2D6", "FLUVASTATIN	CYP2C8", "FLUVASTATIN	CYP2C9", "FLUVASTATIN	CYP3A4", "FLUVOXAMINE	CYP2D6", "HALOPERIDOL	CYP3A4", "LANSOPRAZOLE	CYP2C19", "LANSOPRAZOLE	CYP3A5", "LANSOPRAZOLE	CYP3A4", "LOVASTATIN	CYP3A4", "MIDAZOLAM	CYP3A4", "MIRTAZAPINE	CYP1A2", "MIRTAZAPINE	CYP2D6", "MIRTAZAPINE	CYP3A4", "MIRTAZAPINE	CYP3A5", "MODAFINIL	CYP3A4", "N-DEMETHYLDESACETYL-DILTIAZEM	CYP2D6", "N-DESALKYLQUETIAPINE	CYP3A4", "OLANZAPINE	CYP2D6", "OMEPRAZOLE	CYP2C19", "PANTOPRAZOLE	CYP3A4", "PANTOPRAZOLE	CYP2C19", "PAROXETINE	CYP2D6", "PERPHENAZINE	CYP3A4", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2D6", "R-CITALOPRAM	CYP2D6", "R-CITALOPRAM	CYP3A4", "R-DEMETHYLCITALOPRAM	CYP2D6", "RABEPRAZOLE	CYP3A4", "RABEPRAZOLE	CYP2C19", "RABEPRAZOLE	CYP3A5", "RANOLAZINE	CYP2D6", "REDUCED-HALOPERIDOL	CYP3A4", "RISPERIDONE	CYP2D6", "ROSIGLITAZONE	CYP2C8", "S-DEMETHYLCITALOPRAM	CYP2D6", "S-WARFARIN	CYP2C9", "SERTRALINE	CYP2C19", "SIMVASTATIN	CYP3A4", "TAMOXIFEN	CYP2D6", "TAMOXIFEN	CYP3A4", "TAMOXIFEN	CYP2C9", "TAMOXIFEN	CYP3A5", "THEOPHYLLINE	CYP1A2", "THIORIDAZINE	CYP2D6", "TOLBUTAMIDE	CYP2C9", "TRAZODONE	CYP3A4", "TRIAZOLAM	CYP3A4", "VENLAFAXINE	CYP3A4", "VENLAFAXINE	CYP2D6", "VORICONAZOLE	CYP2C19", "VORICONAZOLE	CYP2C9", "VORICONAZOLE	CYP3A4", "WARFARIN	CYP2C9", "ZAFIRLUKAST	CYP2C9", "ZALEPLON	CYP3A4", "ZIPRASIDONE	CYP3A4", "ZOLPIDEM	CYP3A5", "ZOLPIDEM	CYP3A4"]


# data extracted from SuperCYP
# (http://bioinformatics.charite.de/supercyp/index.php?site=home) on
# 04.23.2010
supercyp_l = [("1A2", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "SUBSTRATE", "HUMAN"),
("1A2", "000086408", "ACRIFLAVINIUMCHLORIDE", "SUBSTRATE", "HUMAN"),
("1A2", "054965218", "ALBENDAZOLE", "SUBSTRATE", "HUMAN"),
("1A2", "054965218", "ALBENDAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "054965218", "ALBENDAZOLE", "INDUCER", "HUMAN"),
("1A2", "005300038", "ALITRETINOIN", "INHIBITOR", "HUMAN"),
("1A2", "122852420", "ALOSETRON", "SUBSTRATE", "HUMAN"),
("1A2", "000125848", "AMINOGLUTHETIMIDE", "INDUCER", "HUMAN"),
("1A2", "000058151", "AMINOPHENAZONE", "SUBSTRATE", "HUMAN"),
("1A2", "000317340", "AMINOPHYLLINE", "SUBSTRATE", "HUMAN"),
("1A2", "001951253", "AMIODARONE", "INHIBITOR", "PARTIAL"),
("1A2", "001951253", "AMIODARONE", "SUBSTRATE", "HUMAN"),
("1A2", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("1A2", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("1A2", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("1A2", "068475423", "ANAGRELIDE", "SUBSTRATE", "HUMAN"),
("1A2", "120511731", "ANASTROZOLE", "INHIBITOR", "HUMAN"),
("1A2", "170729803", "APREPITANT", "SUBSTRATE", "HUMAN"),
("1A2", "063968649", "ARTEMISININ", "INHIBITOR", "HUMAN"),
("1A2", "000051558", "ATROPIN", "INHIBITOR", "HUMAN"),
("1A2", "000051558", "ATROPINE", "INHIBITOR", "HUMAN"),
("1A2", "058581898", "AZELASTINE", "SUBSTRATE", "HUMAN"),
("1A2", "051234287", "BENOXAPROFEN", "INDUCER", "RAT"),
("1A2", "000642728", "BENZYDAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000484208", "BERGAPTEN", "INHIBITOR", "HUMAN"),
("1A2", "007235407", "BETACAROTENE", "INDUCER", "HUMAN"),
("1A2", "063659187", "BETAXOLOL", "SUBSTRATE", "HUMAN"),
("1A2", "179324697", "BORTEZOMIB", "SUBSTRATE", "HUMAN"),
("1A2", "001812302", "BROMAZEPAM", "SUBSTRATE", "HUMAN"),
("1A2", "025614033", "BROMOCRIPTINE", "INHIBITOR", "HUMAN"),
("1A2", "038396393", "BUPIVACAINE", "SUBSTRATE", "HUMAN"),
("1A2", "052485797", "BUPRENORPHINE", "INHIBITOR", "HUMAN"),
("1A2", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("1A2", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("1A2", "000058082", "CAFFEINE", "INHIBITOR", "HUMAN"),
("1A2", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("1A2", "000298464", "CARBAMAZEPINE", "SUBSTRATE", "HUMAN"),
("1A2", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("1A2", "000298464", "CARBAMAZEPINE", "INHIBITOR", "HUMAN"),
("1A2", "000154938", "CARMUSTINE", "SUBSTRATE", "HUMAN"),
("1A2", "072956093", "CARVEDILOL", "SUBSTRATE", "HUMAN"),
("1A2", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("1A2", "000130950", "CHININ", "SUBSTRATE", "HUMAN"),
("1A2", "000130950", "CHININ", "INDUCER", "HUMAN"),
("1A2", "000058946", "CHLOROTHIAZIDE", "INDUCER", "RAT"),
("1A2", "000050533", "CHLORPROMAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000095250", "CHLORZOXAZONE", "SUBSTRATE", "HUMAN"),
("1A2", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("1A2", "000298577", "CINNARIZIN", "SUBSTRATE", "HUMAN"),
("1A2", "000298577", "CINNARIZINE", "SUBSTRATE", "HUMAN"),
("1A2", "085721331", "CIPROFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("1A2", "059729338", "CITALOPRAM", "INHIBITOR", "HUMAN"),
("1A2", "081103119", "CLARITHROMYCIN", "INHIBITOR", "HUMAN"),
("1A2", "037148279", "CLENBUTEROL", "SUBSTRATE", "HUMAN"),
("1A2", "025122412", "CLOBETASOL", "INHIBITOR", "HUMAN"),
("1A2", "000911455", "CLOMIFENE", "INHIBITOR", "HUMAN"),
("1A2", "000303491", "CLOMIPRAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("1A2", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("1A2", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("1A2", "003546030", "CYAMEMAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000303537", "CYCLOBENZAPRINE", "SUBSTRATE", "HUMAN"),
("1A2", "052315078", "CYPERMETHRIN", "SUBSTRATE", "HUMAN"),
("1A2", "004342034", "DACARBAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000050760", "DACTINOMYCIN", "INHIBITOR", "RABBIT"),
("1A2", "020830813", "DAUNORUBICIN", "SUBSTRATE", "HUMAN"),
("1A2", "000108010", "DEANOL", "SUBSTRATE", "HUMAN"),
("1A2", "052918635", "DECAMETHRIN", "SUBSTRATE", "RAT"),
("1A2", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("1A2", "000050475", "DESIPRAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "100643718", "DESLORATADINE", "INHIBITOR", "HUMAN"),
("1A2", "003239449", "DEXFENFLURAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "003239449", "DEXFENFLURAMINE", "INHIBITOR", "HUMAN"),
("1A2", "000439145", "DIAZEPAM", "INHIBITOR", "HUMAN"),
("1A2", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("1A2", "015307865", "DICLOFENAC", "INHIBITOR", ""),
("1A2", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("1A2", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("1A2", "000484231", "DIHYDRALAZINE", "SUBSTRATE", "RAT"),
("1A2", "000484231", "DIHYDRALAZINE", "INHIBITOR", "HUMAN"),
("1A2", "000363246", "DINOPROSTONE", "SUBSTRATE", "HUMAN"),
("1A2", "000097778", "DISULFIRAM", "SUBSTRATE", ""),
("1A2", "000097778", "DISULFIRAM", "INHIBITOR", ""),
("1A2", "057808669", "DOMPERIDONE", "SUBSTRATE", "HUMAN"),
("1A2", "000051616", "DOPAMINE", "INHIBITOR", "HUMAN"),
("1A2", "001668195", "DOXEPIN", "SUBSTRATE", "HUMAN"),
("1A2", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("1A2", "074011588", "ENOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("1A2", "000051434", "EPINEPHRIN", "INHIBITOR", "HUMAN"),
("1A2", "000051434", "EPINEPHRINE", "INHIBITOR", "HUMAN"),
("1A2", "000113155", "ERGOTAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000114078", "ERYTHROMYCIN", "INHIBITOR", "HUMAN"),
("1A2", "000050282", "ESTRADIOL", "SUBSTRATE", "HUMAN"),
("1A2", "000050271", "ESTRIOL", "INHIBITOR", ""),
("1A2", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("1A2", "000064175", "ETHANOL", "SUBSTRATE", "HUMAN"),
("1A2", "000057636", "ETHINYLESTRADIOL", "SUBSTRATE", "HUMAN"),
("1A2", "000057636", "ETHINYLESTRADIOL", "INHIBITOR", "HUMAN"),
("1A2", "033419420", "ETOPOSIDE", "SUBSTRATE", "HUMAN"),
("1A2", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("1A2", "043210679", "FENBENDAZOLE", "INDUCER", "RAT"),
("1A2", "054143554", "FLECAINIDE", "SUBSTRATE", ""),
("1A2", "086386734", "FLUCONAZOLE", "INHIBITOR", ""),
("1A2", "052468607", "FLUNARIZINE", "SUBSTRATE", "HUMAN"),
("1A2", "001622624", "FLUNITRAZEPAM", "SUBSTRATE", "HUMAN"),
("1A2", "000051218", "FLUOROURACIL", "SUBSTRATE", "HUMAN"),
("1A2", "054910893", "FLUOXETINE", "INHIBITOR", ""),
("1A2", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("1A2", "000069238", "FLUPHENAZINE", "INHIBITOR", "HUMAN"),
("1A2", "013311847", "FLUTAMIDE", "SUBSTRATE", "HUMAN"),
("1A2", "013311847", "FLUTAMIDE", "INHIBITOR", "HUMAN"),
("1A2", "093957541", "FLUVASTATIN", "INHIBITOR", "HUMAN"),
("1A2", "054739183", "FLUVOXAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("1A2", "158747025", "FROVATRIPTAN", "SUBSTRATE", "HUMAN"),
("1A2", "025812300", "GEMFIBROZIL", "INHIBITOR", "HUMAN"),
("1A2", "000126078", "GRISEOFULVIN", "SUBSTRATE", "HUMAN"),
("1A2", "000126078", "GRISEOFULVIN", "INDUCER", "5554"),
("1A2", "000489849", "GUAIAZULEN", "SUBSTRATE", "HUMAN"),
("1A2", "000489849", "GUAJAZULEN", "SUBSTRATE", "HUMAN"),
("1A2", "000052868", "HALOPERIDOL", "SUBSTRATE", ""),
("1A2", "000056291", "HEXOBARBITAL", "SUBSTRATE", "HUMAN"),
("1A2", "007647010", "HYDROCHLORICACID", "INHIBITOR", "HUMAN"),
("1A2", "152459955", "IMATINIB", "SUBSTRATE", ""),
("1A2", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000050497", "IMIPRAMINE", "INHIBITOR", "HUMAN"),
("1A2", "006829987", "IMIPRAMINEOXIDE", "SUBSTRATE", "HUMAN"),
("1A2", "099011026", "IMIQUIMOD", "SUBSTRATE", "HUMAN"),
("1A2", "011061680", "INSULIN(BEEF)", "INDUCER", "HUMAN"),
("1A2", "011061680", "INSULIN(HUMAN)", "INDUCER", "HUMAN"),
("1A2", "011061680", "INSULIN(PORK)", "INDUCER", "HUMAN"),
("1A2", "035212227", "IPRIFLAVONE", "INHIBITOR", "HUMAN"),
("1A2", "035212227", "IPRIFLAVONE", "SUBSTRATE", "HUMAN"),
("1A2", "138402116", "IRBESARTAN", "INHIBITOR", "HUMAN"),
("1A2", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("1A2", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "103577453", "LANSOPRAZOLE", "INDUCER", "HUMAN"),
("1A2", "027262471", "LEVOBUPIVACAINE", "SUBSTRATE", "HUMAN"),
("1A2", "100986854", "LEVOFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("1A2", "000137586", "LIDOCAIN", "INHIBITOR", "HUMAN"),
("1A2", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("1A2", "000137586", "LIDOCAINE", "INHIBITOR", "HUMAN"),
("1A2", "098079517", "LOMEFLOXACIN", "SUBSTRATE", "HUMAN"),
("1A2", "098079517", "LOMEFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("1A2", "114798264", "LOSARTAN", "INHIBITOR", "HUMAN"),
("1A2", "220991208", "LUMIRACOXIB", "SUBSTRATE", "HUMAN"),
("1A2", "000121755", "MALATHION", "SUBSTRATE", "HUMAN"),
("1A2", "010262698", "MAPROTILINE", "SUBSTRATE", "HUMAN"),
("1A2", "000569653", "MECLOZIN", "INHIBITOR", "HUMAN"),
("1A2", "000569653", "MECLOZINE", "INHIBITOR", "HUMAN"),
("1A2", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("1A2", "000073314", "MELATONIN", "SUBSTRATE", "HUMAN"),
("1A2", "000058275", "MENADIONE", "SUBSTRATE", "HUMAN"),
("1A2", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("1A2", "000298817", "METHOXSALEN", "INHIBITOR", "HUMAN"),
("1A2", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("1A2", "000555306", "METHYLDOPA(LEVOROTATORY)", "SUBSTRATE", "HUMAN"),
("1A2", "000555306", "METHYLDOPA(RACEMIC)", "SUBSTRATE", "HUMAN"),
("1A2", "031828714", "MEXILETINE", "INHIBITOR", "HUMAN"),
("1A2", "031828714", "MEXILETINE", "SUBSTRATE", "HUMAN"),
("1A2", "024219974", "MIANSERIN", "SUBSTRATE", "HUMAN"),
("1A2", "116644532", "MIBEFRADIL", "INHIBITOR", "HUMAN"),
("1A2", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "061337675", "MIRTAZAPINE", "SUBSTRATE", "HUMAN"),
("1A2", "000488415", "MITOBRONITOL", "INDUCER", "HUMAN"),
("1A2", "000050077", "MITOMYCIN", "INDUCER", "RAT"),
("1A2", "071320779", "MOCLOBEMIDE", "INHIBITOR", "HUMAN"),
("1A2", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("1A2", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("1A2", "031883053", "MORACIZINE", "INHIBITOR", "MOUSE"),
("1A2", "022204531", "NAPROXEN", "SUBSTRATE", "HUMAN"),
("1A2", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("1A2", "129618402", "NEVIRAPINE", "INHIBITOR", "HUMAN"),
("1A2", "000050657", "NICLOSAMIDE", "INHIBITOR", "HUMAN"),
("1A2", "000098920", "NICOTINAMIDE", "INDUCER", "MOUSE"),
("1A2", "000054115", "NICOTINE", "INDUCER", "HUMAN"),
("1A2", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("1A2", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("1A2", "075530686", "NILVADIPINE", "INHIBITOR", "HUMAN"),
("1A2", "063675729", "NISOLDIPINE", "INHIBITOR", "HUMAN"),
("1A2", "015078281", "NITROPRUSSIDE", "INHIBITOR", "HUMAN"),
("1A2", "000051412", "NOREPINEPHRINE", "INHIBITOR", "HUMAN"),
("1A2", "070458967", "NORFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "000072695", "NORTRIPTYLINE", "SUBSTRATE", "HUMAN"),
("1A2", "082419361", "OFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "132539061", "OLANZAPINE", "SUBSTRATE", "HUMAN"),
("1A2", "073590586", "OMEPRAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "073590586", "OMEPRAZOLE", "INDUCER", "HUMAN"),
("1A2", "073590586", "OMEPRAZOLE", "SUBSTRATE", "HUMAN"),
("1A2", "099614025", "ONDANSETRON", "INHIBITOR", "HUMAN"),
("1A2", "099614025", "ONDANSETRON", "SUBSTRATE", ""),
("1A2", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("1A2", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("1A2", "061825943", "OXALIPLATIN", "SUBSTRATE", "HUMAN"),
("1A2", "102625707", "PANTOPRAZOLE", "SUBSTRATE", "HUMAN"),
("1A2", "102625707", "PANTOPRAZOLE", "INDUCER", "HUMAN"),
("1A2", "000103902", "PARACETAMOL", "SUBSTRATE", ""),
("1A2", "000311455", "PARAOXON", "SUBSTRATE", "HUMAN"),
("1A2", "061869087", "PAROXETINE", "INHIBITOR", ""),
("1A2", "070458923", "PEFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "000140647", "PENTAMIDINEISETHIONATE", "SUBSTRATE", "HUMAN"),
("1A2", "006493056", "PENTOXIFYLLINE", "SUBSTRATE", "HUMAN"),
("1A2", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000084979", "PERAZINE", "INHIBITOR", "HUMAN"),
("1A2", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000058399", "PERPHENAZINE", "INHIBITOR", "HUMAN"),
("1A2", "000057421", "PETHIDINE", "INDUCER", "RAT"),
("1A2", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("1A2", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("1A2", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("1A2", "000122098", "PHENTERMINE", "INHIBITOR", "HUMAN"),
("1A2", "000059427", "PHENYLEPHRINE", "INDUCER", "HUMAN"),
("1A2", "014838154", "PHENYLPROPANOLAMINE", "INHIBITOR", "HUMAN"),
("1A2", "002062784", "PIMOZIDE", "SUBSTRATE", "HUMAN"),
("1A2", "001893330", "PIPAMPERONE", "INDUCER", "HUMAN"),
("1A2", "000053430", "PRASTERONE", "INHIBITOR", "RAT"),
("1A2", "055268741", "PRAZIQUANTEL", "SUBSTRATE", "HUMAN"),
("1A2", "000090346", "PRIMAQUINE", "INDUCER", "HUMAN"),
("1A2", "000090346", "PRIMAQUINE", "SUBSTRATE", "HUMAN"),
("1A2", "000090346", "PRIMAQUINE", "INHIBITOR", "HUMAN"),
("1A2", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("1A2", "000671169", "PROCARBAZINE", "SUBSTRATE", "RAT"),
("1A2", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("1A2", "000500925", "PROGUANIL", "SUBSTRATE", "HUMAN"),
("1A2", "000058402", "PROMAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "054063535", "PROPAFENONE", "SUBSTRATE", "HUMAN"),
("1A2", "054063535", "PROPAFENONE", "INHIBITOR", "HUMAN"),
("1A2", "002078548", "PROPOFOL", "INHIBITOR", "HUMAN"),
("1A2", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("1A2", "000525666", "PROPRANOLOL", "SUBSTRATE", "HUMAN"),
("1A2", "000525666", "PROPRANOLOL", "INHIBITOR", "HUMAN"),
("1A2", "000098964", "PYRAZINAMIDE", "SUBSTRATE", "HUMAN"),
("1A2", "000056542", "QUINIDINE", "INHIBITOR", "HUMAN"),
("1A2", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("1A2", "000130950", "QUININE", "SUBSTRATE", "HUMAN"),
("1A2", "000130950", "QUININE", "INDUCER", "HUMAN"),
("1A2", "117976893", "RABEPRAZOLE", "INDUCER", "HUMAN"),
("1A2", "066357355", "RANITIDINE", "SUBSTRATE", "HUMAN"),
("1A2", "066357355", "RANITIDINE", "INHIBITOR", "HUMAN"),
("1A2", "136236516", "RASAGILINE", "SUBSTRATE", "HUMAN"),
("1A2", "000068268", "RETINOL(VITA)", "SUBSTRATE", "HUMAN"),
("1A2", "072559069", "RIFABUTIN", "SUBSTRATE", "HUMAN"),
("1A2", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("1A2", "001744225", "RILUZOLE", "SUBSTRATE", "HUMAN"),
("1A2", "155213675", "RITONAVIR", "SUBSTRATE", "HUMAN"),
("1A2", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("1A2", "162011907", "ROFECOXIB", "SUBSTRATE", "HUMAN"),
("1A2", "162011907", "ROFECOXIB", "INHIBITOR", "HUMAN"),
("1A2", "091374219", "ROPINIROLE", "SUBSTRATE", "HUMAN"),
("1A2", "091374219", "ROPINIROLE", "INHIBITOR", "HUMAN"),
("1A2", "084057954", "ROPIVACAINE", "SUBSTRATE", "HUMAN"),
("1A2", "122320734", "ROSIGLITAZONE", "INHIBITOR", "HUMAN"),
("1A2", "080214831", "ROXITHROMYCIN", "INHIBITOR", "HUMAN"),
("1A2", "000065452", "SALICYLAMIDE", "INHIBITOR", "HUMAN"),
("1A2", "000076733", "SECOBARBITAL", "INDUCER", "MOUSE"),
("1A2", "014611519", "SELEGILINE", "SUBSTRATE", "HUMAN"),
("1A2", "014611519", "SELEGILINE", "INHIBITOR", "HUMAN"),
("1A2", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("1A2", "018883664", "STREPTOZOCIN", "INDUCER", ""),
("1A2", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "038194502", "SULINDAC", "INHIBITOR", "HUMAN"),
("1A2", "015676161", "SULPIRID", "INHIBITOR", "RAT"),
("1A2", "015676161", "SULPIRIDE", "INHIBITOR", "RAT"),
("1A2", "000321642", "TACRINE", "SUBSTRATE", "HUMAN"),
("1A2", "017902237", "TEGAFUR", "SUBSTRATE", "HUMAN"),
("1A2", "145158710", "TEGASEROD", "INHIBITOR", "HUMAN"),
("1A2", "191114484", "TELITHROMYCIN", "SUBSTRATE", "HUMAN"),
("1A2", "108319068", "TEMAFLOXACIN", "SUBSTRATE", "HUMAN"),
("1A2", "108319068", "TEMAFLOXACIN", "INHIBITOR", "HUMAN"),
("1A2", "201341051", "TENOFOVIRDISOPROXIL", "INHIBITOR", "HUMAN"),
("1A2", "091161716", "TERBINAFINE", "SUBSTRATE", "HUMAN"),
("1A2", "000058468", "TETRABENAZINE", "INDUCER", "RAT"),
("1A2", "000083670", "THEOBROMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("1A2", "000058559", "THEOPHYLLINE", "INHIBITOR", "HUMAN"),
("1A2", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "000050522", "THIORIDAZINE", "INHIBITOR", "HUMAN"),
("1A2", "000050522", "THIORIDAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "000148798", "TIABENDAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "000148798", "TIABENDAZOLE", "SUBSTRATE", "HUMAN"),
("1A2", "005630535", "TIBOLONE", "INHIBITOR", "HUMAN"),
("1A2", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("1A2", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("1A2", "003313266", "TIOTIXENE", "SUBSTRATE", "HUMAN"),
("1A2", "051322759", "TIZANIDINE", "SUBSTRATE", "HUMAN"),
("1A2", "041708729", "TOCAINIDE", "INHIBITOR", "HUMAN"),
("1A2", "000728881", "TOLPERISONE", "SUBSTRATE", "HUMAN"),
("1A2", "089778267", "TOREMIFENE", "SUBSTRATE", "HUMAN"),
("1A2", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("1A2", "000299752", "TREOSULFAN", "INHIBITOR", "HUMAN"),
("1A2", "000396010", "TRIAMTERENE", "INHIBITOR", "HUMAN"),
("1A2", "000396010", "TRIAMTERENE", "SUBSTRATE", "HUMAN"),
("1A2", "000079016", "TRICHLOROETHYLENE", "SUBSTRATE", "HUMAN"),
("1A2", "000117895", "TRIFLUOPERAZINE", "SUBSTRATE", "HUMAN"),
("1A2", "010405024", "TROSPIUM", "INHIBITOR", ""),
("1A2", "000073223", "TRYPTOPHAN", "INDUCER", "HEPALCLC7CELLS"),
("1A2", "000099661", "VALPROICACID", "INHIBITOR", "HUMAN"),
("1A2", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("1A2", "001617909", "VINCAMIN", "SUBSTRATE", "HUMAN"),
("1A2", "001617909", "VINCAMINE", "SUBSTRATE", "HUMAN"),
("1A2", "000081812", "WARFARIN", "SUBSTRATE", "HUMAN"),
("1A2", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("1A2", "146939277", "ZIPRASIDONE", "SUBSTRATE", "HUMAN"),
("1A2", "139264178", "ZOLMITRIPTAN", "SUBSTRATE", "HUMAN"),
("1A2", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("B6", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INHIBITOR", "HUMAN"),
("2B6", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2B6", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("2B6", "161814499", "AMPRENAVIR", "INHIBITOR", "HUMAN"),
("2B6", "000077021", "APROBARBITAL", "INDUCER", "RAT"),
("2B6", "063968649", "ARTEMISININ", "SUBSTRATE", "HUMAN"),
("2B6", "063968649", "ARTEMISININ", "INDUCER", "HUMAN"),
("2B6", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("2B6", "104713759", "BARNIDIPINE", "INHIBITOR", "HUMAN"),
("2B6", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2B6", "034911552", "BUPROPION", "INHIBITOR", "HUMAN"),
("2B6", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("2B6", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2B6", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("2B6", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("2B6", "000298577", "CINNARIZIN", "SUBSTRATE", "HUMAN"),
("2B6", "000298577", "CINNARIZINE", "SUBSTRATE", "HUMAN"),
("2B6", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("2B6", "059729338", "CITALOPRAM", "INHIBITOR", "HUMAN"),
("2B6", "022316478", "CLOBAZAM", "SUBSTRATE", "HUMAN"),
("2B6", "000637070", "CLOFIBRATE", "INDUCER", "HUMAN"),
("2B6", "000533459", "CLOMETHIAZOLE", "SUBSTRATE", "HUMAN"),
("2B6", "001622613", "CLONAZEPAM", "INDUCER", "RAT"),
("2B6", "001622613", "CLONAZEPAM", "INHIBITOR", "RAT"),
("2B6", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("2B6", "113665842", "CLOPIDOGREL", "INHIBITOR", "HUMAN"),
("2B6", "033671464", "CLOTIAZEPAM", "SUBSTRATE", "HUMAN"),
("2B6", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "023593751", "CLOTRIMAZOLE", "INDUCER", "HUMAN"),
("2B6", "000064868", "COLCHICINE", "INHIBITOR", "HUMAN"),
("2B6", "000067970", "COLECALCIFEROL", "INHIBITOR", "HUMAN"),
("2B6", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("2B6", "000050180", "CYCLOPHOSPHAMIDE", "INDUCER", "HUMAN"),
("2B6", "000050475", "DESIPRAMINE", "INHIBITOR", "HUMAN"),
("2B6", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2B6", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2B6", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2B6", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("2B6", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("2B6", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("2B6", "000097778", "DISULFIRAM", "SUBSTRATE", ""),
("2B6", "000097778", "DISULFIRAM", "INHIBITOR", ""),
("2B6", "057808669", "DOMPERIDONE", "SUBSTRATE", "HUMAN"),
("2B6", "023214928", "DOXORUBICIN", "INHIBITOR", ""),
("2B6", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("2B6", "154598524", "EFAVIRENZ", "INDUCER", "HUMAN"),
("2B6", "154598524", "EFAVIRENZ", "SUBSTRATE", "HUMAN"),
("2B6", "080012437", "EPINASTINE", "SUBSTRATE", "HUMAN"),
("2B6", "000114078", "ERYTHROMYCIN", "SUBSTRATE", ""),
("2B6", "033643468", "ESKETAMINE", "SUBSTRATE", "HUMAN"),
("2B6", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("2B6", "000064175", "ETHANOL", "INHIBITOR", "HUMAN"),
("2B6", "000057636", "ETHINYLESTRADIOL", "INHIBITOR", "HUMAN"),
("2B6", "000076584", "ETHYLMORPHINE", "SUBSTRATE", "HUMAN"),
("2B6", "001622624", "FLUNITRAZEPAM", "SUBSTRATE", "HUMAN"),
("2B6", "054910893", "FLUOXETINE", "INHIBITOR", ""),
("2B6", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("2B6", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("2B6", "093390819", "FOSPHENYTOIN", "INHIBITOR", ""),
("2B6", "000151677", "HALOTHANE", "SUBSTRATE", "HUMAN"),
("2B6", "003778732", "IFOSFAMIDE", "SUBSTRATE", ""),
("2B6", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2B6", "097682445", "IRINOTECAN", "SUBSTRATE", "HUMAN"),
("2B6", "026675467", "ISOFLURANE", "SUBSTRATE", "HUMAN"),
("2B6", "026675467", "ISOFLURANE", "INHIBITOR", "HUMAN"),
("2B6", "026675467", "ISOFLURANE", "INDUCER", "HUMAN"),
("2B6", "006740881", "KETAMINE", "SUBSTRATE", "HUMAN"),
("2B6", "000469794", "KETOBEMIDONE", "SUBSTRATE", "HUMAN"),
("2B6", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("2B6", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("2B6", "053179116", "LOPERAMIDE", "SUBSTRATE", ""),
("2B6", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("2B6", "000121755", "MALATHION", "SUBSTRATE", "HUMAN"),
("2B6", "019982082", "MEMANTINE", "INHIBITOR", "HUMAN"),
("2B6", "000068893", "METAMIZOLESODIUM", "INDUCER", "HUMAN"),
("2B6", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("2B6", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("2B6", "000115388", "METHYLPHENOBARBITAL", "SUBSTRATE", "HUMAN"),
("2B6", "000058184", "METHYLTESTOSTERONE", "SUBSTRATE", "HUMAN"),
("2B6", "031828714", "MEXILETINE", "SUBSTRATE", "HUMAN"),
("2B6", "024219974", "MIANSERIN", "SUBSTRATE", "HUMAN"),
("2B6", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "059467708", "MIDAZOLAM", "SUBSTRATE", "HUMAN"),
("2B6", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("2B6", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("2B6", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("2B6", "129618402", "NEVIRAPINE", "SUBSTRATE", "HUMAN"),
("2B6", "129618402", "NEVIRAPINE", "INDUCER", "HUMAN"),
("2B6", "055985325", "NICARDIPINE", "INDUCER", "HUMAN"),
("2B6", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2B6", "021829254", "NIFEDIPINE", "INDUCER", "HUMAN"),
("2B6", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("2B6", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("2B6", "061869087", "PAROXETINE", "INHIBITOR", "HUMAN"),
("2B6", "006621472", "PERHEXILINE", "SUBSTRATE", "HUMAN"),
("2B6", "052645531", "PERMETHRIN", "SUBSTRATE", "HUMAN"),
("2B6", "052645531", "PERMETHRIN", "INDUCER", "HUMAN"),
("2B6", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("2B6", "000057421", "PETHIDINE", "SUBSTRATE", "HUMAN"),
("2B6", "000060800", "PHENAZONE", "INHIBITOR", "HUMAN"),
("2B6", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2B6", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("2B6", "000057410", "PHENYTOIN", "INDUCER", ""),
("2B6", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("2B6", "000060877", "PROMETHAZIN", "SUBSTRATE", "HUMAN"),
("2B6", "000060877", "PROMETHAZINE", "SUBSTRATE", "HUMAN"),
("2B6", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2B6", "000056542", "QUINIDINE", "INHIBITOR", "HUMAN"),
("2B6", "000068268", "RETINOL(VITA)", "INHIBITOR", "HUMAN"),
("2B6", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("2B6", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("2B6", "155213675", "RITONAVIR", "SUBSTRATE", "HUMAN"),
("2B6", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2B6", "084057954", "ROPIVACAINE", "SUBSTRATE", "HUMAN"),
("2B6", "080214831", "ROXITHROMYCIN", "INHIBITOR", "HUMAN"),
("2B6", "014611519", "SELEGILINE", "SUBSTRATE", "HUMAN"),
("2B6", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("2B6", "079617962", "SERTRALINE", "INHIBITOR", "HUMAN"),
("2B6", "028523866", "SEVOFLURANE", "SUBSTRATE", "HUMAN"),
("2B6", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "000526089", "SULFAFENAZOL", "INHIBITOR", "HUMAN"),
("2B6", "000526089", "SULFAPHENAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "000057965", "SULFINPYRAZON", "INDUCER", "HUMAN"),
("2B6", "000057965", "SULFINPYRAZONE", "INDUCER", "HUMAN"),
("2B6", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("2B6", "010540291", "TAMOXIFEN", "INHIBITOR", "HUMAN"),
("2B6", "000846504", "TEMAZEPAM", "SUBSTRATE", "HUMAN"),
("2B6", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("2B6", "000057852", "TESTOSTERONE", "INDUCER", "HUMAN"),
("2B6", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("2B6", "000052244", "THIOTEPA", "INHIBITOR", "HUMAN"),
("2B6", "000137268", "THIRAM", "INDUCER", ""),
("2B6", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2B6", "027203925", "TRAMADOL", "SUBSTRATE", "HUMAN"),
("2B6", "000302794", "TRETINOIN", "SUBSTRATE", ""),
("2B6", "003380345", "TRICLOSAN", "INHIBITOR", ""),
("2B6", "022089221", "TROFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("2B6", "097322877", "TROGLITAZONE", "INDUCER", "HUMAN"),
("2B6", "093413695", "VENLAFAXINE", "INHIBITOR", "HUMAN"),
("2B6", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("2B6", "000052539", "VERAPAMIL", "INDUCER", "HUMAN"),
("2B6", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050782", "ACETYLSALICYLICACID", "SUBSTRATE", "HUMAN"),
("2C8", "000058151", "AMINOPHENAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "001951253", "AMIODARONE", "SUBSTRATE", "HUMAN"),
("2C8", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050486", "AMITRIPTYLINE", "INHIBITOR", "HUMAN"),
("2C8", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("2C8", "000086420", "AMODIAQUINE", "SUBSTRATE", "HUMAN"),
("2C8", "161814499", "AMPRENAVIR", "SUBSTRATE", "HUMAN"),
("2C8", "134523005", "ATORVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "041859670", "BEZAFIBRATE", "INHIBITOR", "HUMAN"),
("2C8", "179324697", "BORTEZOMIB", "INHIBITOR", "HUMAN"),
("2C8", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2C8", "052485797", "BUPRENORPHINE", "SUBSTRATE", "HUMAN"),
("2C8", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("2C8", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("2C8", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2C8", "000298464", "CARBAMAZEPINE", "SUBSTRATE", "HUMAN"),
("2C8", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("2C8", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050599", "CEFALORIDINE", "SUBSTRATE", "HUMAN"),
("2C8", "145599866", "CERIVASTATIN", "SUBSTRATE", "HUMAN"),
("2C8", "145599866", "CERIVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("2C8", "000056757", "CHLORAMPHENICOL", "INHIBITOR", "HUMAN"),
("2C8", "000054057", "CHLOROQUINE", "SUBSTRATE", "HUMAN"),
("2C8", "059865133", "CICLOSPORIN", "INHIBITOR", "HUMAN"),
("2C8", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("2C8", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("2C8", "113665842", "CLOPIDOGREL", "INHIBITOR", "HUMAN"),
("2C8", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050362", "COCAINE", "INHIBITOR", "HUMAN"),
("2C8", "000064868", "COLCHICINE", "INDUCER", "HUMAN"),
("2C8", "000064868", "COLCHICINE", "INHIBITOR", "HUMAN"),
("2C8", "000067970", "COLECALCIFEROL", "INHIBITOR", "HUMAN"),
("2C8", "003546030", "CYAMEMAZINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("2C8", "000050180", "CYCLOPHOSPHAMIDE", "INDUCER", "HUMAN"),
("2C8", "000080080", "DAPSONE", "SUBSTRATE", "HUMAN"),
("2C8", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("2C8", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2C8", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2C8", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2C8", "000469625", "DEXTROPROPOXYPHENE", "INHIBITOR", "HUMAN"),
("2C8", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("2C8", "015307865", "DICLOFENAC", "INHIBITOR", ""),
("2C8", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("2C8", "042399417", "DILTIAZEM", "INHIBITOR", ""),
("2C8", "042399417", "DILTIAZEM", "SUBSTRATE", "HUMAN"),
("2C8", "000097778", "DISULFIRAM", "INHIBITOR", ""),
("2C8", "115956122", "DOLASETRON", "SUBSTRATE", ""),
("2C8", "057808669", "DOMPERIDONE", "SUBSTRATE", "HUMAN"),
("2C8", "120279961", "DORZOLAMIDE", "SUBSTRATE", ""),
("2C8", "154598524", "EFAVIRENZ", "INHIBITOR", ""),
("2C8", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("2C8", "133040014", "EPROSARTAN", "INHIBITOR", ""),
("2C8", "000050282", "ESTRADIOL", "SUBSTRATE", "HUMAN"),
("2C8", "033419420", "ETOPOSIDE", "INHIBITOR", "HUMAN"),
("2C8", "072509763", "FELODIPINE", "INHIBITOR", "HUMAN"),
("2C8", "049562289", "FENOFIBRATE", "INHIBITOR", "HUMAN"),
("2C8", "086386734", "FLUCONAZOLE", "INHIBITOR", ""),
("2C8", "000051218", "FLUOROURACIL", "SUBSTRATE", "HUMAN"),
("2C8", "054910893", "FLUOXETINE", "SUBSTRATE", ""),
("2C8", "054910893", "FLUOXETINE", "INHIBITOR", ""),
("2C8", "000069238", "FLUPHENAZINE", "INHIBITOR", ""),
("2C8", "005104494", "FLURBIPROFEN", "SUBSTRATE", ""),
("2C8", "005104494", "FLURBIPROFEN", "INHIBITOR", ""),
("2C8", "093957541", "FLUVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "093957541", "FLUVASTATIN", "SUBSTRATE", "HUMAN"),
("2C8", "054739183", "FLUVOXAMINE", "INHIBITOR", ""),
("2C8", "043229807", "FORMOTEROL", "SUBSTRATE", ""),
("2C8", "226700794", "FOSAMPRENAVIR", "SUBSTRATE", ""),
("2C8", "093390819", "FOSPHENYTOIN", "SUBSTRATE", ""),
("2C8", "093390819", "FOSPHENYTOIN", "INHIBITOR", ""),
("2C8", "025812300", "GEMFIBROZIL", "INHIBITOR", "HUMAN"),
("2C8", "025812300", "GEMFIBROZIL", "INDUCER", "HUMAN"),
("2C8", "093479971", "GLIMEPIRIDE", "SUBSTRATE", ""),
("2C8", "029094619", "GLIPIZIDE", "SUBSTRATE", ""),
("2C8", "000126078", "GRISEOFULVIN", "INDUCER", ""),
("2C8", "069756532", "HALOFANTRINE", "SUBSTRATE", "HUMAN"),
("2C8", "000151677", "HALOTHANE", "SUBSTRATE", ""),
("2C8", "000050237", "HYDROCORTISONE", "INDUCER", "HUMAN"),
("2C8", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2C8", "015687271", "IBUPROFEN", "INHIBITOR", ""),
("2C8", "003778732", "IFOSFAMIDE", "INDUCER", "HUMAN"),
("2C8", "003778732", "IFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("2C8", "152459955", "IMATINIB", "SUBSTRATE", ""),
("2C8", "152459955", "IMATINIB", "INHIBITOR", ""),
("2C8", "150378179", "INDINAVIR", "INHIBITOR", ""),
("2C8", "000053861", "INDOMETACIN", "SUBSTRATE", ""),
("2C8", "000053861", "INDOMETACIN", "INHIBITOR", ""),
("2C8", "035212227", "IPRIFLAVONE", "INHIBITOR", "HUMAN"),
("2C8", "138402116", "IRBESARTAN", "SUBSTRATE", "HUMAN"),
("2C8", "138402116", "IRBESARTAN", "INHIBITOR", "HUMAN"),
("2C8", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("2C8", "006740881", "KETAMINE", "SUBSTRATE", "HUMAN"),
("2C8", "000469794", "KETOBEMIDONE", "SUBSTRATE", "HUMAN"),
("2C8", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "022071154", "KETOPROFEN", "INHIBITOR", "HUMAN"),
("2C8", "103577453", "LANSOPRAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "103577453", "LANSOPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C8", "075706126", "LEFLUNOMIDE", "SUBSTRATE", "HUMAN"),
("2C8", "075706126", "LEFLUNOMIDE", "INHIBITOR", "HUMAN"),
("2C8", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("2C8", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("2C8", "053179116", "LOPERAMIDE", "SUBSTRATE", ""),
("2C8", "079794755", "LORATADINE", "INHIBITOR", "HUMAN"),
("2C8", "114798264", "LOSARTAN", "SUBSTRATE", "HUMAN"),
("2C8", "114798264", "LOSARTAN", "INHIBITOR", "HUMAN"),
("2C8", "075330755", "LOVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "000520854", "MEDROXYPROGESTERONE", "INHIBITOR", "HUMAN"),
("2C8", "000061687", "MEFENAMICACID", "SUBSTRATE", "HUMAN"),
("2C8", "000061687", "MEFENAMICACID", "INHIBITOR", "HUMAN"),
("2C8", "071125387", "MELOXICAM", "SUBSTRATE", "HUMAN"),
("2C8", "071125387", "MELOXICAM", "INHIBITOR", "HUMAN"),
("2C8", "000050124", "MEPHENYTOIN", "SUBSTRATE", "HUMAN"),
("2C8", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("2C8", "000443481", "METRONIDAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "061337675", "MIRTAZAPINE", "SUBSTRATE", "HUMAN"),
("2C8", "105102225", "MOMETASONE", "INHIBITOR", "HUMAN"),
("2C8", "158966928", "MONTELUKAST", "INHIBITOR", "HUMAN"),
("2C8", "000057272", "MORPHINE", "SUBSTRATE", "HUMAN"),
("2C8", "000465656", "NALOXONE", "SUBSTRATE", "HUMAN"),
("2C8", "022204531", "NAPROXEN", "SUBSTRATE", "HUMAN"),
("2C8", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("2C8", "055985325", "NICARDIPINE", "SUBSTRATE", "HUMAN"),
("2C8", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2C8", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("2C8", "063612500", "NILUTAMIDE", "INHIBITOR", "HUMAN"),
("2C8", "075530686", "NILVADIPINE", "INHIBITOR", "HUMAN"),
("2C8", "073590586", "OMEPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C8", "005633205", "OXYBUTYNIN", "INHIBITOR", "HUMAN"),
("2C8", "033069624", "PACLITAXEL", "SUBSTRATE", "HUMAN"),
("2C8", "000103902", "PARACETAMOL", "SUBSTRATE", "HUMAN"),
("2C8", "000311455", "PARAOXON", "SUBSTRATE", "HUMAN"),
("2C8", "061869087", "PAROXETINE", "INHIBITOR", "HUMAN"),
("2C8", "000140647", "PENTAMIDINEISETHIONATE", "SUBSTRATE", "HUMAN"),
("2C8", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("2C8", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "000051718", "PHENELZINE", "INHIBITOR", "HUMAN"),
("2C8", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("2C8", "000050066", "PHENOBARBITAL", "SUBSTRATE", ""),
("2C8", "000435972", "PHENPROCOUMON", "SUBSTRATE", "HUMAN"),
("2C8", "000057410", "PHENYTOIN", "SUBSTRATE", "HUMAN"),
("2C8", "000057410", "PHENYTOIN", "INDUCER", "HUMAN"),
("2C8", "111025468", "PIOGLITAZONE", "INHIBITOR", "HUMAN"),
("2C8", "111025468", "PIOGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "036322904", "PIROXICAM", "SUBSTRATE", "HUMAN"),
("2C8", "036322904", "PIROXICAM", "INHIBITOR", "HUMAN"),
("2C8", "081093370", "PRAVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("2C8", "000057669", "PROBENECID", "INDUCER", "HUMAN"),
("2C8", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("2C8", "054063535", "PROPAFENONE", "INHIBITOR", "HUMAN"),
("2C8", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2C8", "000058140", "PYRIMETHAMINE", "INHIBITOR", "HUMAN"),
("2C8", "000056542", "QUINIDINE", "SUBSTRATE", "HUMAN"),
("2C8", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("2C8", "084449901", "RALOXIFENE", "INHIBITOR", "HUMAN"),
("2C8", "135062021", "REPAGLINIDE", "SUBSTRATE", "HUMAN"),
("2C8", "000068268", "RETINOL(VITA)", "SUBSTRATE", "HUMAN"),
("2C8", "000068268", "RETINOL(VITA)", "INHIBITOR", "HUMAN"),
("2C8", "013292461", "RIFAMPICIN", "SUBSTRATE", "HUMAN"),
("2C8", "013292461", "RIFAMPICIN", "INHIBITOR", "HUMAN"),
("2C8", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("2C8", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("2C8", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2C8", "162011907", "ROFECOXIB", "SUBSTRATE", "HUMAN"),
("2C8", "122320734", "ROSIGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "122320734", "ROSIGLITAZONE", "INHIBITOR", "HUMAN"),
("2C8", "000153184", "RUTOSIDE", "INHIBITOR", "HUMAN"),
("2C8", "089365504", "SALMETEROL", "INHIBITOR", "HUMAN"),
("2C8", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("2C8", "000076733", "SECOBARBITAL", "INDUCER", ""),
("2C8", "014611519", "SELEGILINE", "SUBSTRATE", "HUMAN"),
("2C8", "112665437", "SERATRODAST", "SUBSTRATE", "HUMAN"),
("2C8", "079902639", "SIMVASTATIN", "SUBSTRATE", ""),
("2C8", "079902639", "SIMVASTATIN", "INHIBITOR", "HUMAN"),
("2C8", "000052017", "SPIRONOLACTONE", "INHIBITOR", "HUMAN"),
("2C8", "000068359", "SULFADIAZINE", "SUBSTRATE", "HUMAN"),
("2C8", "000526089", "SULFAFENAZOL", "INHIBITOR", "HUMAN"),
("2C8", "000127695", "SULFAFURAZOLE", "SUBSTRATE", ""),
("2C8", "000127695", "SULFAFURAZOLE", "INHIBITOR", ""),
("2C8", "000723466", "SULFAMETHOXAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "000526089", "SULFAPHENAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "000057965", "SULFINPYRAZON", "SUBSTRATE", "HUMAN"),
("2C8", "000057965", "SULFINPYRAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "010540291", "TAMOXIFEN", "INHIBITOR", "HUMAN"),
("2C8", "118292403", "TAZAROTENE", "SUBSTRATE", "HUMAN"),
("2C8", "017902237", "TEGAFUR", "SUBSTRATE", "HUMAN"),
("2C8", "145158710", "TEGASEROD", "INHIBITOR", "HUMAN"),
("2C8", "000846504", "TEMAZEPAM", "SUBSTRATE", "HUMAN"),
("2C8", "091161716", "TERBINAFINE", "SUBSTRATE", "HUMAN"),
("2C8", "050679088", "TERFENADINE", "INHIBITOR", "HUMAN"),
("2C8", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("2C8", "000058468", "TETRABENAZINE", "INDUCER", "RAT"),
("2C8", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("2C8", "000050522", "THIORIDAZINE", "INHIBITOR", "HUMAN"),
("2C8", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2C8", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C8", "000064777", "TOLBUTAMIDE", "SUBSTRATE", "HUMAN"),
("2C8", "000064777", "TOLBUTAMIDE", "INHIBITOR", "HUMAN"),
("2C8", "056211406", "TORASEMIDE", "SUBSTRATE", "HUMAN"),
("2C8", "000302794", "TRETINOIN", "SUBSTRATE", ""),
("2C8", "000302794", "TRETINOIN", "INHIBITOR", ""),
("2C8", "028911015", "TRIAZOLAM", "INHIBITOR", "HUMAN"),
("2C8", "000127480", "TRIMETHADIONE", "SUBSTRATE", "HUMAN"),
("2C8", "000738705", "TRIMETHOPRIM", "INHIBITOR", "HUMAN"),
("2C8", "000738705", "TRIMETHOPRIM", "SUBSTRATE", "HUMAN"),
("2C8", "097322877", "TROGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C8", "097322877", "TROGLITAZONE", "INHIBITOR", "HUMAN"),
("2C8", "002751099", "TROLEANDOMYCIN", "INHIBITOR", "HUMAN"),
("2C8", "000099661", "VALPROICACID", "INHIBITOR", "HUMAN"),
("2C8", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("2C8", "000081812", "WARFARIN", "SUBSTRATE", "HUMAN"),
("2C8", "000081812", "WARFARIN", "INHIBITOR", "HUMAN"),
("2C8", "107753786", "ZAFIRLUKAST", "SUBSTRATE", "HUMAN"),
("2C8", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("2C8", "030516871", "ZIDOVUDINE", "SUBSTRATE", "HUMAN"),
("2C8", "043200802", "ZOPICLONE", "SUBSTRATE", "HUMAN"),
("2C8", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2C8", "015687271", "IBUPROFEN", "INHIBITOR", ""),
("2C8", "061379655", "RIFAPENTINE", "INDUCER", "HUMAN"),
("2C9", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INHIBITOR", "HUMAN"),
("2C9", "089796996", "ACECLOFENAC", "SUBSTRATE", "HUMAN"),
("2C9", "000152727", "ACENOCOUMAROL", "SUBSTRATE", "HUMAN"),
("2C9", "000152727", "ACENOCOUMAROL", "INHIBITOR", "HUMAN"),
("2C9", "000050782", "ACETYLSALICYLICACID", "SUBSTRATE", "HUMAN"),
("2C9", "122852420", "ALOSETRON", "SUBSTRATE", "HUMAN"),
("2C9", "000058151", "AMINOPHENAZONE", "INHIBITOR", "HUMAN"),
("2C9", "001951253", "AMIODARONE", "INHIBITOR", "HUMAN"),
("2C9", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2C9", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("2C9", "000086420", "AMODIAQUINE", "INHIBITOR", "HUMAN"),
("2C9", "161814499", "AMPRENAVIR", "SUBSTRATE", "HUMAN"),
("2C9", "120511731", "ANASTROZOLE", "INHIBITOR", "HUMAN"),
("2C9", "170729803", "APREPITANT", "INDUCER", "HUMAN"),
("2C9", "170729803", "APREPITANT", "INHIBITOR", "HUMAN"),
("2C9", "095233184", "ATOVAQUONE", "INHIBITOR", "HUMAN"),
("2C9", "013539598", "AZAPROPAZONE", "INHIBITOR", "HUMAN"),
("2C9", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("2C9", "104713759", "BARNIDIPINE", "INHIBITOR", "HUMAN"),
("2C9", "105979177", "BENIDIPINE", "INHIBITOR", "HUMAN"),
("2C9", "003562843", "BENZBROMARONE", "INHIBITOR", ""),
("2C9", "000121540", "BENZETHONIUM", "INHIBITOR", "HUMAN"),
("2C9", "153559490", "BEXAROTENE", "SUBSTRATE", "HUMAN"),
("2C9", "090357065", "BICALUTAMIDE", "INHIBITOR", ""),
("2C9", "179324697", "BORTEZOMIB", "SUBSTRATE", "HUMAN"),
("2C9", "179324697", "BORTEZOMIB", "INHIBITOR", "HUMAN"),
("2C9", "147536978", "BOSENTAN", "SUBSTRATE", "HUMAN"),
("2C9", "147536978", "BOSENTAN", "INDUCER", "HUMAN"),
("2C9", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("2C9", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("2C9", "139481597", "CANDESARTAN", "SUBSTRATE", "HUMAN"),
("2C9", "139481597", "CANDESARTAN", "INHIBITOR", "HUMAN"),
("2C9", "154361509", "CAPECITABINE", "INHIBITOR", "HUMAN"),
("2C9", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2C9", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("2C9", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "072956093", "CARVEDILOL", "SUBSTRATE", "HUMAN"),
("2C9", "169590425", "CELECOXIB", "SUBSTRATE", "HUMAN"),
("2C9", "184007952", "CELECOXIB", "SUBSTRATE", "HUMAN"),
("2C9", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("2C9", "000056757", "CHLORAMPHENICOL", "INHIBITOR", "HUMAN"),
("2C9", "000094202", "CHLORPROPAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "059865133", "CICLOSPORIN", "INHIBITOR", "HUMAN"),
("2C9", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("2C9", "000298577", "CINNARIZIN", "SUBSTRATE", "HUMAN"),
("2C9", "000298577", "CINNARIZINE", "SUBSTRATE", "HUMAN"),
("2C9", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("2C9", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("2C9", "113665842", "CLOPIDOGREL", "INHIBITOR", "HUMAN"),
("2C9", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("2C9", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("2C9", "000050362", "COCAINE", "INHIBITOR", "HUMAN"),
("2C9", "000064868", "COLCHICINE", "INDUCER", "HUMAN"),
("2C9", "000064868", "COLCHICINE", "INHIBITOR", "HUMAN"),
("2C9", "000067970", "COLECALCIFEROL", "INHIBITOR", "HUMAN"),
("2C9", "003546030", "CYAMEMAZINE", "SUBSTRATE", "HUMAN"),
("2C9", "000082928", "CYCLIZINE", "INHIBITOR", "HUMAN"),
("2C9", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "000050180", "CYCLOPHOSPHAMIDE", "INDUCER", "HUMAN"),
("2C9", "000080080", "DAPSONE", "SUBSTRATE", "HUMAN"),
("2C9", "000080080", "DAPSONE", "INDUCER", "HUMAN"),
("2C9", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("2C9", "100643718", "DESLORATADINE", "INHIBITOR", "HUMAN"),
("2C9", "054024225", "DESOGESTREL", "SUBSTRATE", "HUMAN"),
("2C9", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2C9", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2C9", "003239449", "DEXFENFLURAMINE", "INHIBITOR", "HUMAN"),
("2C9", "051146566", "DEXIBUPROFEN", "INHIBITOR", "HUMAN"),
("2C9", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2C9", "000469625", "DEXTROPROPOXYPHENE", "INHIBITOR", "HUMAN"),
("2C9", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("2C9", "000439145", "DIAZEPAM", "INHIBITOR", "HUMAN"),
("2C9", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("2C9", "015307865", "DICLOFENAC", "INHIBITOR", "HUMAN"),
("2C9", "000120978", "DICLOFENAMIDE", "INDUCER", "HUMAN"),
("2C9", "000066762", "DICOUMAROL", "SUBSTRATE", "HUMAN"),
("2C9", "000066762", "DICOUMAROL", "INHIBITOR", "HUMAN"),
("2C9", "042399417", "DILTIAZEM", "SUBSTRATE", "HUMAN"),
("2C9", "042399417", "DILTIAZEM", "INHIBITOR", "HUMAN"),
("2C9", "000097778", "DISULFIRAM", "INHIBITOR", "HUMAN"),
("2C9", "115956122", "DOLASETRON", "SUBSTRATE", "HUMAN"),
("2C9", "000051616", "DOPAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "120279961", "DORZOLAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "001668195", "DOXEPIN", "SUBSTRATE", "HUMAN"),
("2C9", "001972083", "DRONABINOL", "SUBSTRATE", "HUMAN"),
("2C9", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("2C9", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("2C9", "000051434", "EPINEPHRIN", "INHIBITOR", "HUMAN"),
("2C9", "000051434", "EPINEPHRINE", "INHIBITOR", "HUMAN"),
("2C9", "035121789", "EPOPROSTENOL", "SUBSTRATE", "HUMAN"),
("2C9", "133040014", "EPROSARTAN", "INHIBITOR", "HUMAN"),
("2C9", "033643468", "ESKETAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "000050282", "ESTRADIOL", "SUBSTRATE", "HUMAN"),
("2C9", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("2C9", "000064175", "ETHANOL", "INHIBITOR", "HUMAN"),
("2C9", "000057636", "ETHINYLESTRADIOL", "SUBSTRATE", "HUMAN"),
("2C9", "041340254", "ETODOLAC", "SUBSTRATE", "HUMAN"),
("2C9", "041340254", "ETODOLAC", "INHIBITOR", "HUMAN"),
("2C9", "033419420", "ETOPOSIDE", "INHIBITOR", ""),
("2C9", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("2C9", "072509763", "FELODIPINE", "INHIBITOR", "HUMAN"),
("2C9", "049562289", "FENOFIBRATE", "INHIBITOR", "HUMAN"),
("2C9", "054143554", "FLECAINIDE", "INHIBITOR", "HUMAN"),
("2C9", "086386734", "FLUCONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "052468607", "FLUNARIZINE", "SUBSTRATE", "HUMAN"),
("2C9", "001622624", "FLUNITRAZEPAM", "SUBSTRATE", "HUMAN"),
("2C9", "000051218", "FLUOROURACIL", "INHIBITOR", "HUMAN"),
("2C9", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("2C9", "054910893", "FLUOXETINE", "INHIBITOR", "HUMAN"),
("2C9", "000069238", "FLUPHENAZINE", "INHIBITOR", ""),
("2C9", "005104494", "FLURBIPROFEN", "SUBSTRATE", "HUMAN"),
("2C9", "005104494", "FLURBIPROFEN", "INHIBITOR", ""),
("2C9", "093957541", "FLUVASTATIN", "SUBSTRATE", "HUMAN"),
("2C9", "093957541", "FLUVASTATIN", "INHIBITOR", "HUMAN"),
("2C9", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("2C9", "043229807", "FORMOTEROL", "SUBSTRATE", ""),
("2C9", "226700794", "FOSAMPRENAVIR", "SUBSTRATE", ""),
("2C9", "093390819", "FOSPHENYTOIN", "SUBSTRATE", ""),
("2C9", "093390819", "FOSPHENYTOIN", "INHIBITOR", ""),
("2C9", "025812300", "GEMFIBROZIL", "INHIBITOR", "HUMAN"),
("2C9", "010238218", "GLIBENCLAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "010238218", "GLIBENCLAMIDE", "INHIBITOR", "HUMAN"),
("2C9", "093479971", "GLIMEPIRIDE", "SUBSTRATE", "HUMAN"),
("2C9", "029094619", "GLIPIZIDE", "SUBSTRATE", ""),
("2C9", "000126078", "GRISEOFULVIN", "INDUCER", ""),
("2C9", "069756532", "HALOFANTRINE", "SUBSTRATE", ""),
("2C9", "000052868", "HALOPERIDOL", "SUBSTRATE", "HUMAN"),
("2C9", "000151677", "HALOTHANE", "SUBSTRATE", "HUMAN"),
("2C9", "000056291", "HEXOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C9", "000051456", "HISTAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "000051456", "HISTAMINE", "INHIBITOR", "HUMAN"),
("2C9", "007647010", "HYDROCHLORICACID", "INHIBITOR", "HUMAN"),
("2C9", "000466999", "HYDROMORPHONE", "SUBSTRATE", "HUMAN"),
("2C9", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2C9", "015687271", "IBUPROFEN", "INHIBITOR", "HUMAN"),
("2C9", "058957929", "IDARUBICIN", "SUBSTRATE", "HUMAN"),
("2C9", "003778732", "IFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "003778732", "IFOSFAMIDE", "INDUCER", "HUMAN"),
("2C9", "152459955", "IMATINIB", "SUBSTRATE", ""),
("2C9", "152459955", "IMATINIB", "INHIBITOR", ""),
("2C9", "150378179", "INDINAVIR", "INHIBITOR", "HUMAN"),
("2C9", "000053861", "INDOMETACIN", "SUBSTRATE", "HUMAN"),
("2C9", "000053861", "INDOMETACIN", "INHIBITOR", ""),
("2C9", "035212227", "IPRIFLAVONE", "INHIBITOR", "HUMAN"),
("2C9", "138402116", "IRBESARTAN", "SUBSTRATE", "HUMAN"),
("2C9", "138402116", "IRBESARTAN", "INHIBITOR", "HUMAN"),
("2C9", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("2C9", "006740881", "KETAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "000469794", "KETOBEMIDONE", "SUBSTRATE", "HUMAN"),
("2C9", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "022071154", "KETOPROFEN", "INHIBITOR", "HUMAN"),
("2C9", "084057841", "LAMOTRIGINE", "SUBSTRATE", "HUMAN"),
("2C9", "103577453", "LANSOPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C9", "103577453", "LANSOPRAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "103577453", "LANSOPRAZOLE", "INDUCER", "HUMAN"),
("2C9", "075706126", "LEFLUNOMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "075706126", "LEFLUNOMIDE", "INHIBITOR", "HUMAN"),
("2C9", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("2C9", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("2C9", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("2C9", "079794755", "LORATADINE", "SUBSTRATE", "HUMAN"),
("2C9", "079794755", "LORATADINE", "INHIBITOR", "HUMAN"),
("2C9", "070374399", "LORNOXICAM", "SUBSTRATE", "HUMAN"),
("2C9", "070374399", "LORNOXICAM", "INHIBITOR", "HUMAN"),
("2C9", "114798264", "LOSARTAN", "SUBSTRATE", "HUMAN"),
("2C9", "114798264", "LOSARTAN", "INHIBITOR", "HUMAN"),
("2C9", "075330755", "LOVASTATIN", "INDUCER", "HUMAN"),
("2C9", "075330755", "LOVASTATIN", "INHIBITOR", "HUMAN"),
("2C9", "220991208", "LUMIRACOXIB", "SUBSTRATE", "HUMAN"),
("2C9", "089226506", "MANIDIPINE", "INHIBITOR", "HUMAN"),
("2C9", "000520854", "MEDROXYPROGESTERONE", "INHIBITOR", "HUMAN"),
("2C9", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("2C9", "000061687", "MEFENAMICACID", "SUBSTRATE", "HUMAN"),
("2C9", "000061687", "MEFENAMICACID", "INHIBITOR", "HUMAN"),
("2C9", "071125387", "MELOXICAM", "SUBSTRATE", "HUMAN"),
("2C9", "071125387", "MELOXICAM", "INHIBITOR", "HUMAN"),
("2C9", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("2C9", "000554574", "METHAZOLAMIDE", "INHIBITOR", "HUMAN"),
("2C9", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("2C9", "000443481", "METRONIDAZOLE", "SUBSTRATE", "HUMAN"),
("2C9", "000443481", "METRONIDAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "061337675", "MIRTAZAPINE", "SUBSTRATE", "HUMAN"),
("2C9", "108612459", "MIZOLASTINE", "INHIBITOR", ""),
("2C9", "071320779", "MOCLOBEMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "071320779", "MOCLOBEMIDE", "INHIBITOR", "HUMAN"),
("2C9", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("2C9", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("2C9", "022204531", "NAPROXEN", "SUBSTRATE", "HUMAN"),
("2C9", "105816044", "NATEGLINIDE", "SUBSTRATE", "HUMAN"),
("2C9", "159989647", "NELFINAVIR", "INDUCER", ""),
("2C9", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("2C9", "129618402", "NEVIRAPINE", "SUBSTRATE", "HUMAN"),
("2C9", "129618402", "NEVIRAPINE", "INHIBITOR", "HUMAN"),
("2C9", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("2C9", "055985325", "NICARDIPINE", "INDUCER", "HUMAN"),
("2C9", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2C9", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("2C9", "021829254", "NIFEDIPINE", "INDUCER", "HUMAN"),
("2C9", "063612500", "NILUTAMIDE", "INHIBITOR", "HUMAN"),
("2C9", "075530686", "NILVADIPINE", "INHIBITOR", "HUMAN"),
("2C9", "051803782", "NIMESULIDE", "SUBSTRATE", ""),
("2C9", "051803782", "NIMESULIDE", "INHIBITOR", ""),
("2C9", "132539061", "OLANZAPINE", "INHIBITOR", "HUMAN"),
("2C9", "073590586", "OMEPRAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "099614025", "ONDANSETRON", "SUBSTRATE", "HUMAN"),
("2C9", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("2C9", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("2C9", "021256188", "OXAPROZIN", "SUBSTRATE", "HUMAN"),
("2C9", "033069624", "PACLITAXEL", "SUBSTRATE", "HUMAN"),
("2C9", "009011976", "PANCREOZYMIN(CHOLECYSTOKININ)", "INHIBITOR", "HUMAN"),
("2C9", "102625707", "PANTOPRAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000103902", "PARACETAMOL", "SUBSTRATE", "HUMAN"),
("2C9", "198470847", "PARECOXIB", "INHIBITOR", "HUMAN"),
("2C9", "061869087", "PAROXETINE", "INHIBITOR", "HUMAN"),
("2C9", "000084979", "PERAZINE", "INHIBITOR", "HUMAN"),
("2C9", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("2C9", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("2C9", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("2C9", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("2C9", "000050066", "PHENOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C9", "000435972", "PHENPROCOUMON", "SUBSTRATE", "HUMAN"),
("2C9", "000122098", "PHENTERMINE", "INDUCER", "HUMAN"),
("2C9", "000122098", "PHENTERMINE", "INHIBITOR", "HUMAN"),
("2C9", "000050339", "PHENYLBUTAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "000050339", "PHENYLBUTAZONE", "INHIBITOR", "HUMAN"),
("2C9", "000057410", "PHENYTOIN", "INDUCER", "HUMAN"),
("2C9", "000057410", "PHENYTOIN", "SUBSTRATE", ""),
("2C9", "000057410", "PHENYTOIN", "INHIBITOR", "HUMAN"),
("2C9", "111025468", "PIOGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "111025468", "PIOGLITAZONE", "INHIBITOR", "HUMAN"),
("2C9", "036322904", "PIROXICAM", "SUBSTRATE", "HUMAN"),
("2C9", "036322904", "PIROXICAM", "INHIBITOR", "HUMAN"),
("2C9", "103177373", "PRANLUKAST", "INHIBITOR", "HUMAN"),
("2C9", "081093370", "PRAVASTATIN", "SUBSTRATE", "HUMAN"),
("2C9", "081093370", "PRAVASTATIN", "INHIBITOR", "HUMAN"),
("2C9", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("2C9", "000057669", "PROBENECID", "INHIBITOR", "HUMAN"),
("2C9", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("2C9", "000057830", "PROGESTERONE", "INHIBITOR", "HUMAN"),
("2C9", "000500925", "PROGUANIL", "SUBSTRATE", "HUMAN"),
("2C9", "000060877", "PROMETHAZIN", "INHIBITOR", "HUMAN"),
("2C9", "000060877", "PROMETHAZINE", "INHIBITOR", "HUMAN"),
("2C9", "054063535", "PROPAFENONE", "INHIBITOR", "HUMAN"),
("2C9", "000071238", "PROPANOL", "INHIBITOR", "HUMAN"),
("2C9", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2C9", "002078548", "PROPOFOL", "INHIBITOR", "HUMAN"),
("2C9", "000058140", "PYRIMETHAMINE", "INHIBITOR", "HUMAN"),
("2C9", "036735225", "QUAZEPAM", "SUBSTRATE", "HUMAN"),
("2C9", "000056542", "QUINIDINE", "INHIBITOR", "HUMAN"),
("2C9", "000056542", "QUINIDINE", "SUBSTRATE", "HUMAN"),
("2C9", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("2C9", "000068268", "RETINOL(VITA)", "INHIBITOR", "HUMAN"),
("2C9", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("2C9", "013292461", "RIFAMPICIN", "SUBSTRATE", "HUMAN"),
("2C9", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2C9", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("2C9", "162011907", "ROFECOXIB", "SUBSTRATE", "HUMAN"),
("2C9", "122320734", "ROSIGLITAZONE", "INHIBITOR", "HUMAN"),
("2C9", "122320734", "ROSIGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "287714414", "ROSUVASTATIN", "INHIBITOR", "HUMAN"),
("2C9", "287714414", "ROSUVASTATIN", "SUBSTRATE", "HUMAN"),
("2C9", "000153184", "RUTOSIDE", "INHIBITOR", "HUMAN"),
("2C9", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("2C9", "000076733", "SECOBARBITAL", "INDUCER", "HUMAN"),
("2C9", "014611519", "SELEGILINE", "SUBSTRATE", "HUMAN"),
("2C9", "014611519", "SELEGILINE", "INHIBITOR", "HUMAN"),
("2C9", "112665437", "SERATRODAST", "INDUCER", "HUMAN"),
("2C9", "112665437", "SERATRODAST", "SUBSTRATE", "HUMAN"),
("2C9", "112665437", "SERATRODAST", "INHIBITOR", "HUMAN"),
("2C9", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("2C9", "079617962", "SERTRALINE", "INHIBITOR", "HUMAN"),
("2C9", "139755832", "SILDENAFIL", "SUBSTRATE", "HUMAN"),
("2C9", "022888706", "SILYMARIN", "INHIBITOR", "HUMAN"),
("2C9", "079902639", "SIMVASTATIN", "INHIBITOR", "HUMAN"),
("2C9", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000068359", "SULFADIAZINE", "SUBSTRATE", "HUMAN"),
("2C9", "000068359", "SULFADIAZINE", "INHIBITOR", "HUMAN"),
("2C9", "000122112", "SULFADIMETHOXINE", "INHIBITOR", "HUMAN"),
("2C9", "000057681", "SULFADIMIDINE", "INHIBITOR", "DWARFGOAT"),
("2C9", "000526089", "SULFAFENAZOL", "INHIBITOR", "HUMAN"),
("2C9", "000127695", "SULFAFURAZOLE", "SUBSTRATE", ""),
("2C9", "000127695", "SULFAFURAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000144821", "SULFAMETHIZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000723466", "SULFAMETHOXAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000723466", "SULFAMETHOXAZOLE", "SUBSTRATE", "HUMAN"),
("2C9", "000729997", "SULFAMOXOLE", "INHIBITOR", "HUMAN"),
("2C9", "000063741", "SULFANILAMIDE", "INHIBITOR", "HUMAN"),
("2C9", "000526089", "SULFAPHENAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000144832", "SULFAPYRIDINE", "INHIBITOR", "HUMAN"),
("2C9", "000057965", "SULFINPYRAZON", "INHIBITOR", "HUMAN"),
("2C9", "000057965", "SULFINPYRAZON", "SUBSTRATE", "HUMAN"),
("2C9", "000057965", "SULFINPYRAZONE", "INHIBITOR", "HUMAN"),
("2C9", "000057965", "SULFINPYRAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "040828464", "SUPROFEN", "INHIBITOR", "HUMAN"),
("2C9", "040828464", "SUPROFEN", "SUBSTRATE", "HUMAN"),
("2C9", "010540291", "TAMOXIFEN", "INHIBITOR", "HUMAN"),
("2C9", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("2C9", "145158710", "TEGASEROD", "INHIBITOR", "HUMAN"),
("2C9", "144701484", "TELMISARTAN", "INHIBITOR", ""),
("2C9", "000846504", "TEMAZEPAM", "SUBSTRATE", "HUMAN"),
("2C9", "029767202", "TENIPOSIDE", "INHIBITOR", "HUMAN"),
("2C9", "059804374", "TENOXICAM", "SUBSTRATE", "HUMAN"),
("2C9", "091161716", "TERBINAFINE", "SUBSTRATE", "HUMAN"),
("2C9", "050679088", "TERFENADINE", "SUBSTRATE", "HUMAN"),
("2C9", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("2C9", "000058468", "TETRABENAZINE", "INDUCER", "RAT"),
("2C9", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("2C9", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000050522", "THIORIDAZINE", "INHIBITOR", "HUMAN"),
("2C9", "005630535", "TIBOLONE", "INHIBITOR", "HUMAN"),
("2C9", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2C9", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000064777", "TOLBUTAMIDE", "INHIBITOR", "HUMAN"),
("2C9", "000064777", "TOLBUTAMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "134308137", "TOLCAPONE", "INHIBITOR", "HUMAN"),
("2C9", "124937515", "TOLTERODINE", "SUBSTRATE", "HUMAN"),
("2C9", "056211406", "TORASEMIDE", "SUBSTRATE", "HUMAN"),
("2C9", "114899773", "TRABECTEDIN", "SUBSTRATE", "HUMAN"),
("2C9", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("2C9", "000302794", "TRETINOIN", "SUBSTRATE", ""),
("2C9", "000302794", "TRETINOIN", "INHIBITOR", ""),
("2C9", "028911015", "TRIAZOLAM", "INHIBITOR", "HUMAN"),
("2C9", "000127480", "TRIMETHADIONE", "SUBSTRATE", "HUMAN"),
("2C9", "000738705", "TRIMETHOPRIM", "SUBSTRATE", "HUMAN"),
("2C9", "000738705", "TRIMETHOPRIM", "INHIBITOR", "HUMAN"),
("2C9", "000739719", "TRIMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2C9", "097322877", "TROGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C9", "097322877", "TROGLITAZONE", "INHIBITOR", "HUMAN"),
("2C9", "089565684", "TROPISETRON", "SUBSTRATE", "HUMAN"),
("2C9", "010405024", "TROSPIUM", "INHIBITOR", ""),
("2C9", "181695727", "VALDECOXIB", "INHIBITOR", "HUMAN"),
("2C9", "181695727", "VALDECOXIB", "SUBSTRATE", "HUMAN"),
("2C9", "000099661", "VALPROICACID", "INHIBITOR", "HUMAN"),
("2C9", "000099661", "VALPROICACID", "SUBSTRATE", "HUMAN"),
("2C9", "137862534", "VALSARTAN", "SUBSTRATE", "HUMAN"),
("2C9", "137862534", "VALSARTAN", "INHIBITOR", "HUMAN"),
("2C9", "093413695", "VENLAFAXINE", "SUBSTRATE", "HUMAN"),
("2C9", "000052539", "VERAPAMIL", "INHIBITOR", "HUMAN"),
("2C9", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("2C9", "137234629", "VORICONAZOLE", "SUBSTRATE", "HUMAN"),
("2C9", "137234629", "VORICONAZOLE", "INHIBITOR", "HUMAN"),
("2C9", "000081812", "WARFARIN", "SUBSTRATE", "HUMAN"),
("2C9", "000081812", "WARFARIN", "INHIBITOR", "HUMAN"),
("2C9", "192939461", "XIMELAGATRAN", "SUBSTRATE", "HUMAN"),
("2C9", "107753786", "ZAFIRLUKAST", "SUBSTRATE", "HUMAN"),
("2C9", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("2C9", "007481892", "ZALCITABINE", "SUBSTRATE", "HUMAN"),
("2C9", "030516871", "ZIDOVUDINE", "SUBSTRATE", "HUMAN"),
("2C9", "043200802", "ZOPICLONE", "SUBSTRATE", "HUMAN"),
("2C9", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2C9", "015687271", "IBUPROFEN", "INHIBITOR", "HUMAN"),
("2C9", "061379655", "RIFAPENTINE", "INDUCER", "HUMAN"),
("2C19", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INHIBITOR", "HUMAN"),
("2C19", "000050782", "ACETYLSALICYLICACID", "INDUCER", "HUMAN"),
("2C19", "037115325", "ADINAZOLAM", "SUBSTRATE", "HUMAN"),
("2C19", "000125848", "AMINOGLUTHETIMIDE", "INDUCER", "HUMAN"),
("2C19", "000058151", "AMINOPHENAZONE", "INHIBITOR", "HUMAN"),
("2C19", "000058151", "AMINOPHENAZONE", "SUBSTRATE", "HUMAN"),
("2C19", "001951253", "AMIODARONE", "SUBSTRATE", "HUMAN"),
("2C19", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2C19", "000050486", "AMITRIPTYLINE", "INHIBITOR", "HUMAN"),
("2C19", "026787780", "AMOXICILLIN", "SUBSTRATE", "HUMAN"),
("2C19", "161814499", "AMPRENAVIR", "INHIBITOR", "HUMAN"),
("2C19", "170729803", "APREPITANT", "SUBSTRATE", "HUMAN"),
("2C19", "170729803", "APREPITANT", "INHIBITOR", "HUMAN"),
("2C19", "071939510", "ARTEMETHER", "SUBSTRATE", "HUMAN"),
("2C19", "063968649", "ARTEMISININ", "INDUCER", "HUMAN"),
("2C19", "083015263", "ATOMOXETINE", "SUBSTRATE", "HUMAN"),
("2C19", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("2C19", "058581898", "AZELASTINE", "SUBSTRATE", "HUMAN"),
("2C19", "104713759", "BARNIDIPINE", "INHIBITOR", "HUMAN"),
("2C19", "105979177", "BENIDIPINE", "INHIBITOR", "HUMAN"),
("2C19", "000086135", "BENZATROPINE", "SUBSTRATE", "HUMAN"),
("2C19", "000121540", "BENZETHONIUM", "SUBSTRATE", "HUMAN"),
("2C19", "000642728", "BENZYDAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "090357065", "BICALUTAMIDE", "INHIBITOR", ""),
("2C19", "060628968", "BIFONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "179324697", "BORTEZOMIB", "SUBSTRATE", "HUMAN"),
("2C19", "179324697", "BORTEZOMIB", "INHIBITOR", "HUMAN"),
("2C19", "001812302", "BROMAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "055837257", "BUFLOMEDIL", "SUBSTRATE", "HUMAN"),
("2C19", "038396393", "BUPIVACAINE", "SUBSTRATE", "HUMAN"),
("2C19", "052485797", "BUPRENORPHINE", "INHIBITOR", "HUMAN"),
("2C19", "000404864", "CAPSAICIN", "SUBSTRATE", ""),
("2C19", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2C19", "000298464", "CARBAMAZEPINE", "INHIBITOR", "HUMAN"),
("2C19", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("2C19", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "000078444", "CARISOPRODOL", "SUBSTRATE", "HUMAN"),
("2C19", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("2C19", "000130950", "CHININ", "SUBSTRATE", "HUMAN"),
("2C19", "000056757", "CHLORAMPHENICOL", "INHIBITOR", "HUMAN"),
("2C19", "000056757", "CHLORAMPHENICOL", "SUBSTRATE", ""),
("2C19", "001961779", "CHLORMADINONE", "INHIBITOR", ""),
("2C19", "000067663", "CHLOROFORM", "SUBSTRATE", "HUMAN"),
("2C19", "000094202", "CHLORPROPAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "059865133", "CICLOSPORIN", "INHIBITOR", "HUMAN"),
("2C19", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("2C19", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("2C19", "059729338", "CITALOPRAM", "SUBSTRATE", "HUMAN"),
("2C19", "059729338", "CITALOPRAM", "INHIBITOR", "HUMAN"),
("2C19", "081103119", "CLARITHROMYCIN", "SUBSTRATE", "HUMAN"),
("2C19", "081103119", "CLARITHROMYCIN", "INHIBITOR", "HUMAN"),
("2C19", "022316478", "CLOBAZAM", "SUBSTRATE", "HUMAN"),
("2C19", "000533459", "CLOMETHIAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "000303491", "CLOMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("2C19", "033671464", "CLOTIAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("2C19", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("2C19", "000067970", "COLECALCIFEROL", "INHIBITOR", "HUMAN"),
("2C19", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "000080080", "DAPSONE", "SUBSTRATE", "HUMAN"),
("2C19", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("2C19", "000050475", "DESIPRAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "000050475", "DESIPRAMINE", "INHIBITOR", "HUMAN"),
("2C19", "100643718", "DESLORATADINE", "INHIBITOR", "HUMAN"),
("2C19", "054024225", "DESOGESTREL", "SUBSTRATE", "HUMAN"),
("2C19", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2C19", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2C19", "003239449", "DEXFENFLURAMINE", "INHIBITOR", "HUMAN"),
("2C19", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2C19", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "000439145", "DIAZEPAM", "INHIBITOR", "HUMAN"),
("2C19", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("2C19", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "000067630", "DIIODOHYDROXYPROPANE", "INHIBITOR", "HUMAN"),
("2C19", "000067685", "DIMETHYLSULFOXIDE", "INHIBITOR", "HUMAN"),
("2C19", "000051616", "DOPAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "074191858", "DOXAZOSIN", "SUBSTRATE", "HUMAN"),
("2C19", "001668195", "DOXEPIN", "SUBSTRATE", "HUMAN"),
("2C19", "001972083", "DRONABINOL", "SUBSTRATE", "HUMAN"),
("2C19", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("2C19", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("2C19", "128196010", "ESCITALOPRAM", "SUBSTRATE", "HUMAN"),
("2C19", "161973100", "ESOMEPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "000050282", "ESTRADIOL", "SUBSTRATE", "HUMAN"),
("2C19", "000064175", "ETHANOL", "INHIBITOR", "HUMAN"),
("2C19", "000057636", "ETHINYLESTRADIOL", "SUBSTRATE", "HUMAN"),
("2C19", "000057636", "ETHINYLESTRADIOL", "INHIBITOR", "HUMAN"),
("2C19", "000086351", "ETHOTOIN", "INHIBITOR", "HUMAN"),
("2C19", "040054691", "ETIZOLAM", "SUBSTRATE", "HUMAN"),
("2C19", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("2C19", "076824356", "FAMOTIDINE", "SUBSTRATE", "HUMAN"),
("2C19", "025451154", "FELBAMATE", "INHIBITOR", "HUMAN"),
("2C19", "049562289", "FENOFIBRATE", "INHIBITOR", ""),
("2C19", "086386734", "FLUCONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "001622624", "FLUNITRAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "054910893", "FLUOXETINE", "INHIBITOR", "HUMAN"),
("2C19", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("2C19", "013311847", "FLUTAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("2C19", "043229807", "FORMOTEROL", "SUBSTRATE", ""),
("2C19", "226700794", "FOSAMPRENAVIR", "INHIBITOR", ""),
("2C19", "093390819", "FOSPHENYTOIN", "SUBSTRATE", ""),
("2C19", "093390819", "FOSPHENYTOIN", "INHIBITOR", ""),
("2C19", "184475352", "GEFITINIB", "INHIBITOR", ""),
("2C19", "025812300", "GEMFIBROZIL", "INHIBITOR", "HUMAN"),
("2C19", "010238218", "GLIBENCLAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "021187984", "GLICLAZIDE", "INHIBITOR", "HUMAN"),
("2C19", "029094619", "GLIPIZIDE", "SUBSTRATE", ""),
("2C19", "000052868", "HALOPERIDOL", "SUBSTRATE", "HUMAN"),
("2C19", "000056291", "HEXOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C19", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2C19", "003778732", "IFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "152459955", "IMATINIB", "SUBSTRATE", ""),
("2C19", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "000050497", "IMIPRAMINE", "INHIBITOR", "HUMAN"),
("2C19", "150378179", "INDINAVIR", "INHIBITOR", "HUMAN"),
("2C19", "000053861", "INDOMETACIN", "INHIBITOR", ""),
("2C19", "000053861", "INDOMETACIN", "SUBSTRATE", "HUMAN"),
("2C19", "035212227", "IPRIFLAVONE", "INHIBITOR", "HUMAN"),
("2C19", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("2C19", "000067630", "ISOPROPANOL", "INHIBITOR", "HUMAN"),
("2C19", "000469794", "KETOBEMIDONE", "SUBSTRATE", "HUMAN"),
("2C19", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "118288087", "LAFUTIDINE", "INHIBITOR", "HUMAN"),
("2C19", "084057841", "LAMOTRIGINE", "SUBSTRATE", "HUMAN"),
("2C19", "103577453", "LANSOPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "103577453", "LANSOPRAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("2C19", "079794755", "LORATADINE", "INDUCER", "HUMAN"),
("2C19", "079794755", "LORATADINE", "INHIBITOR", "HUMAN"),
("2C19", "114798264", "LOSARTAN", "INHIBITOR", "HUMAN"),
("2C19", "220991208", "LUMIRACOXIB", "SUBSTRATE", "HUMAN"),
("2C19", "002898126", "MEDAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("2C19", "000073314", "MELATONIN", "SUBSTRATE", "HUMAN"),
("2C19", "019982082", "MEMANTINE", "INHIBITOR", "HUMAN"),
("2C19", "000050124", "MEPHENYTOIN", "SUBSTRATE", "HUMAN"),
("2C19", "000050124", "MEPHENYTOIN", "INHIBITOR", "HUMAN"),
("2C19", "000057534", "MEPROBAMATE", "SUBSTRATE", "HUMAN"),
("2C19", "000077418", "MESUXIMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "000077418", "MESUXIMIDE", "INHIBITOR", "HUMAN"),
("2C19", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("2C19", "000554574", "METHAZOLAMIDE", "INHIBITOR", "HUMAN"),
("2C19", "000115388", "METHYLPHENOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C19", "000115388", "METHYLPHENOBARBITAL", "INHIBITOR", "HUMAN"),
("2C19", "037350586", "METOPROLOL", "SUBSTRATE", "HUMAN"),
("2C19", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "071320779", "MOCLOBEMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "071320779", "MOCLOBEMIDE", "INHIBITOR", "HUMAN"),
("2C19", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("2C19", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("2C19", "159989647", "NELFINAVIR", "SUBSTRATE", "HUMAN"),
("2C19", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("2C19", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("2C19", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2C19", "063612500", "NILUTAMIDE", "INHIBITOR", "HUMAN"),
("2C19", "063612500", "NILUTAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "075530686", "NILVADIPINE", "INHIBITOR", "HUMAN"),
("2C19", "001088115", "NORDAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "000068224", "NORETHISTERONE", "INDUCER", "HUMAN"),
("2C19", "000072695", "NORTRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2C19", "132539061", "OLANZAPINE", "INHIBITOR", "HUMAN"),
("2C19", "073590586", "OMEPRAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "073590586", "OMEPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("2C19", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("2C19", "028721075", "OXCARBAZEPINE", "INHIBITOR", "HUMAN"),
("2C19", "102625707", "PANTOPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "102625707", "PANTOPRAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "061869087", "PAROXETINE", "INHIBITOR", ""),
("2C19", "000076744", "PENTOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C19", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("2C19", "000084979", "PERAZINE", "INHIBITOR", "HUMAN"),
("2C19", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("2C19", "000057421", "PETHIDINE", "SUBSTRATE", "HUMAN"),
("2C19", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("2C19", "000060800", "PHENAZONE", "INHIBITOR", "HUMAN"),
("2C19", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2C19", "000051718", "PHENELZINE", "INHIBITOR", "HUMAN"),
("2C19", "000050066", "PHENOBARBITAL", "SUBSTRATE", "HUMAN"),
("2C19", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("2C19", "000086340", "PHENSUXIMIDE", "INHIBITOR", "HUMAN"),
("2C19", "000057410", "PHENYTOIN", "INDUCER", "HUMAN"),
("2C19", "000057410", "PHENYTOIN", "SUBSTRATE", "HUMAN"),
("2C19", "002062784", "PIMOZIDE", "INHIBITOR", "HUMAN"),
("2C19", "111025468", "PIOGLITAZONE", "INHIBITOR", "HUMAN"),
("2C19", "019186357", "PODOPHYLLOTOXIN", "SUBSTRATE", "HUMAN"),
("2C19", "055268741", "PRAZIQUANTEL", "SUBSTRATE", "HUMAN"),
("2C19", "000053032", "PREDNISONE", "INDUCER", "HUMAN"),
("2C19", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("2C19", "000125337", "PRIMIDONE", "SUBSTRATE", ""),
("2C19", "000057669", "PROBENECID", "INHIBITOR", "HUMAN"),
("2C19", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("2C19", "000057830", "PROGESTERONE", "INHIBITOR", "HUMAN"),
("2C19", "000500925", "PROGUANIL", "SUBSTRATE", "HUMAN"),
("2C19", "000058402", "PROMAZINE", "SUBSTRATE", "HUMAN"),
("2C19", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2C19", "000525666", "PROPRANOLOL", "SUBSTRATE", "HUMAN"),
("2C19", "036735225", "QUAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "111974697", "QUETIAPINE", "SUBSTRATE", "HUMAN"),
("2C19", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("2C19", "000130950", "QUININE", "SUBSTRATE", "HUMAN"),
("2C19", "117976893", "RABEPRAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "117976893", "RABEPRAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "066357355", "RANITIDINE", "SUBSTRATE", "HUMAN"),
("2C19", "000068268", "RETINOL(VITA)", "INHIBITOR", "HUMAN"),
("2C19", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("2C19", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("2C19", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2C19", "122320734", "ROSIGLITAZONE", "INHIBITOR", "HUMAN"),
("2C19", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("2C19", "014611519", "SELEGILINE", "SUBSTRATE", "HUMAN"),
("2C19", "112665437", "SERATRODAST", "SUBSTRATE", "HUMAN"),
("2C19", "112665437", "SERATRODAST", "INHIBITOR", "HUMAN"),
("2C19", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("2C19", "079617962", "SERTRALINE", "INHIBITOR", "HUMAN"),
("2C19", "139755832", "SILDENAFIL", "INHIBITOR", "HUMAN"),
("2C19", "139755832", "SILDENAFIL", "SUBSTRATE", "HUMAN"),
("2C19", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "000063741", "SULFANILAMIDE", "INHIBITOR", "HUMAN"),
("2C19", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("2C19", "144701484", "TELMISARTAN", "INHIBITOR", "HUMAN"),
("2C19", "000846504", "TEMAZEPAM", "SUBSTRATE", "HUMAN"),
("2C19", "029767202", "TENIPOSIDE", "SUBSTRATE", ""),
("2C19", "091161716", "TERBINAFINE", "SUBSTRATE", "HUMAN"),
("2C19", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("2C19", "000058468", "TETRABENAZINE", "INDUCER", "RAT"),
("2C19", "000050351", "THALIDOMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "000050522", "THIORIDAZINE", "SUBSTRATE", "HUMAN"),
("2C19", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2C19", "026839758", "TIMOLOL", "SUBSTRATE", "HUMAN"),
("2C19", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "000064777", "TOLBUTAMIDE", "SUBSTRATE", "HUMAN"),
("2C19", "000728881", "TOLPERISONE", "SUBSTRATE", ""),
("2C19", "124937515", "TOLTERODINE", "SUBSTRATE", "HUMAN"),
("2C19", "097240794", "TOPIRAMATE", "INHIBITOR", "HUMAN"),
("2C19", "056211406", "TORASEMIDE", "INHIBITOR", "HUMAN"),
("2C19", "114899773", "TRABECTEDIN", "SUBSTRATE", "HUMAN"),
("2C19", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("2C19", "000127480", "TRIMETHADIONE", "SUBSTRATE", "HUMAN"),
("2C19", "000739719", "TRIMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "097322877", "TROGLITAZONE", "SUBSTRATE", "HUMAN"),
("2C19", "097322877", "TROGLITAZONE", "INHIBITOR", "HUMAN"),
("2C19", "002751099", "TROLEANDOMYCIN", "INHIBITOR", "HUMAN"),
("2C19", "010405024", "TROSPIUM", "INHIBITOR", ""),
("2C19", "181695727", "VALDECOXIB", "INHIBITOR", "HUMAN"),
("2C19", "000099661", "VALPROICACID", "INHIBITOR", "HUMAN"),
("2C19", "000099661", "VALPROICACID", "SUBSTRATE", "HUMAN"),
("2C19", "093413695", "VENLAFAXINE", "SUBSTRATE", "HUMAN"),
("2C19", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("2C19", "137234629", "VORICONAZOLE", "SUBSTRATE", "HUMAN"),
("2C19", "137234629", "VORICONAZOLE", "INHIBITOR", "HUMAN"),
("2C19", "000081812", "WARFARIN", "SUBSTRATE", "HUMAN"),
("2C19", "000081812", "WARFARIN", "INHIBITOR", "HUMAN"),
("2C19", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("2C19", "030516871", "ZIDOVUDINE", "SUBSTRATE", "HUMAN"),
("2C19", "068291974", "ZONISAMIDE", "SUBSTRATE", ""),
("2C19", "068291974", "ZONISAMIDE", "INHIBITOR", "HUMAN"),
("2C19", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("2C19", "003416248", "GLUCOSAMINE", "SUBSTRATE", "HUMAN"),
("2C19", "015687271", "IBUPROFEN", "SUBSTRATE", "HUMAN"),
("2D6", "037517309", "ACEBUTOLOL", "INHIBITOR", "HUMAN"),
("2D6", "000051843", "ACETYLCHOLIN", "SUBSTRATE", "HUMAN"),
("2D6", "000051843", "ACETYLCHOLINE", "SUBSTRATE", "HUMAN"),
("2D6", "004360127", "AJMALINE", "SUBSTRATE", "HUMAN"),
("2D6", "004360127", "AJMALINE", "INHIBITOR", "HUMAN"),
("2D6", "154323576", "ALMOTRIPTAN", "SUBSTRATE", "HUMAN"),
("2D6", "013655522", "ALPRENOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "000300629", "AMFETAMINE", "INHIBITOR", "HUMAN"),
("2D6", "000300629", "AMFETAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000058151", "AMINOPHENAZONE", "SUBSTRATE", "HUMAN"),
("2D6", "001951253", "AMIODARONE", "SUBSTRATE", "HUMAN"),
("2D6", "001951253", "AMIODARONE", "INHIBITOR", "HUMAN"),
("2D6", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050486", "AMITRIPTYLINE", "INHIBITOR", "HUMAN"),
("2D6", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("2D6", "000086420", "AMODIAQUINE", "INHIBITOR", "HUMAN"),
("2D6", "161814499", "AMPRENAVIR", "SUBSTRATE", "HUMAN"),
("2D6", "051264143", "AMSACRINE", "SUBSTRATE", "HUMAN"),
("2D6", "037640714", "APRINDINE", "SUBSTRATE", "HUMAN"),
("2D6", "129722129", "ARIPIPRAZOLE", "SUBSTRATE", "HUMAN"),
("2D6", "129722129", "ARIPIPRAZOLE", "INDUCER", "HUMAN"),
("2D6", "129722129", "ARIPIPRAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "071939510", "ARTEMETHER", "SUBSTRATE", "HUMAN"),
("2D6", "068844779", "ASTEMIZOLE", "SUBSTRATE", "HUMAN"),
("2D6", "083015263", "ATOMOXETINE", "INHIBITOR", "HUMAN"),
("2D6", "083015263", "ATOMOXETINE", "SUBSTRATE", "HUMAN"),
("2D6", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("2D6", "058581898", "AZELASTINE", "SUBSTRATE", "HUMAN"),
("2D6", "104713759", "BARNIDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "039552017", "BEFUNOLOL", "SUBSTRATE", ""),
("2D6", "105979177", "BENIDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "000086135", "BENZATROPINE", "SUBSTRATE", "HUMAN"),
("2D6", "000121540", "BENZETHONIUM", "SUBSTRATE", "HUMAN"),
("2D6", "000642728", "BENZYDAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "064706543", "BEPRIDIL", "SUBSTRATE", "HUMAN"),
("2D6", "063659187", "BETAXOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "063659187", "BETAXOLOL", "INHIBITOR", "HUMAN"),
("2D6", "090357065", "BICALUTAMIDE", "INHIBITOR", ""),
("2D6", "000514658", "BIPERIDEN", "INHIBITOR", "HUMAN"),
("2D6", "066722449", "BISOPROLOL", "SUBSTRATE", "HUMAN"),
("2D6", "179324697", "BORTEZOMIB", "SUBSTRATE", "HUMAN"),
("2D6", "179324697", "BORTEZOMIB", "INHIBITOR", "HUMAN"),
("2D6", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000086226", "BROMPHENIRAMINE", "INHIBITOR", "HUMAN"),
("2D6", "057982782", "BUDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "055837257", "BUFLOMEDIL", "SUBSTRATE", "HUMAN"),
("2D6", "038396393", "BUPIVACAINE", "SUBSTRATE", "HUMAN"),
("2D6", "014556468", "BUPRANOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "052485797", "BUPRENORPHINE", "INHIBITOR", "HUMAN"),
("2D6", "052485797", "BUPRENORPHINE", "SUBSTRATE", "HUMAN"),
("2D6", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("2D6", "034911552", "BUPROPION", "INHIBITOR", "HUMAN"),
("2D6", "036505847", "BUSPIRONE", "SUBSTRATE", "HUMAN"),
("2D6", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("2D6", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2D6", "062571862", "CAPTOPRIL", "SUBSTRATE", "HUMAN"),
("2D6", "000486168", "CARBINOXAMINE", "INHIBITOR", "HUMAN"),
("2D6", "051781067", "CARTEOLOL", "INHIBITOR", "HUMAN"),
("2D6", "051781067", "CARTEOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "072956093", "CARVEDILOL", "SUBSTRATE", "HUMAN"),
("2D6", "015686712", "CEFALEXIN", "SUBSTRATE", "HUMAN"),
("2D6", "169590425", "CELECOXIB", "INHIBITOR", "HUMAN"),
("2D6", "184007952", "CELECOXIB", "INHIBITOR", "HUMAN"),
("2D6", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("2D6", "000058253", "CHLORDIAZEPOXIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000054057", "CHLOROQUINE", "SUBSTRATE", "HUMAN"),
("2D6", "000054057", "CHLOROQUINE", "INHIBITOR", "HUMAN"),
("2D6", "000088040", "CHLOROXYLENOL", "SUBSTRATE", "HUMAN"),
("2D6", "000132229", "CHLORPHENAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000132229", "CHLORPHENAMINE", "INHIBITOR", "HUMAN"),
("2D6", "000050533", "CHLORPROMAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050533", "CHLORPROMAZINE", "INHIBITOR", "HUMAN"),
("2D6", "000095250", "CHLORZOXAZONE", "SUBSTRATE", "HUMAN"),
("2D6", "053267019", "CIBENZOLINE", "SUBSTRATE", "HUMAN"),
("2D6", "059865133", "CICLOSPORIN", "INHIBITOR", "HUMAN"),
("2D6", "051481619", "CIMETIDINE", "INHIBITOR", "RAT"),
("2D6", "000298577", "CINNARIZIN", "SUBSTRATE", "HUMAN"),
("2D6", "000298577", "CINNARIZINE", "SUBSTRATE", "HUMAN"),
("2D6", "081098604", "CISAPRIDE", "INHIBITOR", "HUMAN"),
("2D6", "059729338", "CITALOPRAM", "SUBSTRATE", ""),
("2D6", "059729338", "CITALOPRAM", "INHIBITOR", ""),
("2D6", "015686518", "CLEMASTINE", "INHIBITOR", "HUMAN"),
("2D6", "000303491", "CLOMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000303491", "CLOMIPRAMINE", "INHIBITOR", "HUMAN"),
("2D6", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("2D6", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050362", "COCAINE", "INHIBITOR", "HUMAN"),
("2D6", "000076573", "CODEINE", "SUBSTRATE", ""),
("2D6", "000076573", "CODEINE", "INHIBITOR", "HUMAN"),
("2D6", "000067970", "COLECALCIFEROL", "INHIBITOR", "HUMAN"),
("2D6", "000303537", "CYCLOBENZAPRINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000108010", "DEANOL", "SUBSTRATE", "HUMAN"),
("2D6", "001131642", "DEBRISOQUINE", "SUBSTRATE", "HUMAN"),
("2D6", "136817599", "DELAVIRDINE", "SUBSTRATE", "HUMAN"),
("2D6", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("2D6", "000050475", "DESIPRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050475", "DESIPRAMINE", "INHIBITOR", "HUMAN"),
("2D6", "100643718", "DESLORATADINE", "INHIBITOR", "HUMAN"),
("2D6", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2D6", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2D6", "000051649", "DEXAMFETAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000051649", "DEXAMFETAMINE", "INHIBITOR", "HUMAN"),
("2D6", "003239449", "DEXFENFLURAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "003239449", "DEXFENFLURAMINE", "INHIBITOR", "HUMAN"),
("2D6", "000125713", "DEXTROMETHORPHAN", "INHIBITOR", "HUMAN"),
("2D6", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2D6", "000469625", "DEXTROPROPOXYPHENE", "INHIBITOR", "HUMAN"),
("2D6", "015307865", "DICLOFENAC", "SUBSTRATE", ""),
("2D6", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000125280", "DIHYDROCODEIN", "SUBSTRATE", "HUMAN"),
("2D6", "000125280", "DIHYDROCODEINE", "SUBSTRATE", "HUMAN"),
("2D6", "042399417", "DILTIAZEM", "SUBSTRATE", "HUMAN"),
("2D6", "042399417", "DILTIAZEM", "INHIBITOR", "HUMAN"),
("2D6", "000067685", "DIMETHYLSULFOXIDE", "INHIBITOR", "HUMAN"),
("2D6", "000058731", "DIPHENHYDRAMIN", "SUBSTRATE", "HUMAN"),
("2D6", "000058731", "DIPHENHYDRAMIN", "INHIBITOR", "HUMAN"),
("2D6", "000058731", "DIPHENHYDRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000058731", "DIPHENHYDRAMINE", "INHIBITOR", "HUMAN"),
("2D6", "031065891", "DIPHENHYDRAMINEMETHYLBROMIDE", "INHIBITOR", "HUMAN"),
("2D6", "000097778", "DISULFIRAM", "SUBSTRATE", ""),
("2D6", "000097778", "DISULFIRAM", "INHIBITOR", ""),
("2D6", "115956122", "DOLASETRON", "SUBSTRATE", "HUMAN"),
("2D6", "115956122", "DOLASETRON", "INHIBITOR", ""),
("2D6", "057808669", "DOMPERIDONE", "SUBSTRATE", "HUMAN"),
("2D6", "120014064", "DONEPEZIL", "SUBSTRATE", "HUMAN"),
("2D6", "000051616", "DOPAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "074191858", "DOXAZOSIN", "SUBSTRATE", "HUMAN"),
("2D6", "001668195", "DOXEPIN", "SUBSTRATE", "HUMAN"),
("2D6", "001668195", "DOXEPIN", "INHIBITOR", "HUMAN"),
("2D6", "023214928", "DOXORUBICIN", "SUBSTRATE", ""),
("2D6", "023214928", "DOXORUBICIN", "INHIBITOR", "HUMAN"),
("2D6", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("2D6", "143322581", "ELETRIPTAN", "SUBSTRATE", "HUMAN"),
("2D6", "000483181", "EMETINE", "SUBSTRATE", "HUMAN"),
("2D6", "000483181", "EMETINE", "INHIBITOR", "HUMAN"),
("2D6", "066778367", "ENCAINIDE", "SUBSTRATE", "HUMAN"),
("2D6", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("2D6", "080012437", "EPINASTINE", "INHIBITOR", "HUMAN"),
("2D6", "080012437", "EPINASTINE", "SUBSTRATE", "HUMAN"),
("2D6", "128196010", "ESCITALOPRAM", "SUBSTRATE", "HUMAN"),
("2D6", "128196010", "ESCITALOPRAM", "INHIBITOR", "HUMAN"),
("2D6", "000058731", "ETANAUTINE", "SUBSTRATE", "HUMAN"),
("2D6", "000058731", "ETANAUTINE", "INHIBITOR", "HUMAN"),
("2D6", "000076584", "ETHYLMORPHINE", "SUBSTRATE", "HUMAN"),
("2D6", "000457874", "ETILAMFETAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("2D6", "072509763", "FELODIPINE", "INHIBITOR", "HUMAN"),
("2D6", "000458242", "FENFLURAMINE", "INHIBITOR", "HUMAN"),
("2D6", "083799240", "FEXOFENADINE", "INHIBITOR", "HUMAN"),
("2D6", "054143554", "FLECAINIDE", "INHIBITOR", "HUMAN"),
("2D6", "054143554", "FLECAINIDE", "SUBSTRATE", "HUMAN"),
("2D6", "052468607", "FLUNARIZINE", "SUBSTRATE", "HUMAN"),
("2D6", "054910893", "FLUOXETINE", "INHIBITOR", "HUMAN"),
("2D6", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("2D6", "000069238", "FLUPHENAZINE", "INHIBITOR", "HUMAN"),
("2D6", "000069238", "FLUPHENAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "093957541", "FLUVASTATIN", "INHIBITOR", "HUMAN"),
("2D6", "093957541", "FLUVASTATIN", "SUBSTRATE", "HUMAN"),
("2D6", "054739183", "FLUVOXAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("2D6", "043229807", "FORMOTEROL", "SUBSTRATE", ""),
("2D6", "000357700", "GALANTAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "184475352", "GEFITINIB", "INHIBITOR", "HUMAN"),
("2D6", "184475352", "GEFITINIB", "SUBSTRATE", "HUMAN"),
("2D6", "083928761", "GEPIRONE", "SUBSTRATE", "HUMAN"),
("2D6", "109889090", "GRANISETRON", "INDUCER", "HUMAN"),
("2D6", "109889090", "GRANISETRON", "INHIBITOR", "HUMAN"),
("2D6", "109889090", "GRANISETRON", "SUBSTRATE", "HUMAN"),
("2D6", "002165197", "GUANOXAN", "SUBSTRATE", "HUMAN"),
("2D6", "069756532", "HALOFANTRINE", "INHIBITOR", "HUMAN"),
("2D6", "069756532", "HALOFANTRINE", "SUBSTRATE", "HUMAN"),
("2D6", "000052868", "HALOPERIDOL", "INHIBITOR", "HUMAN"),
("2D6", "000052868", "HALOPERIDOL", "SUBSTRATE", "HUMAN"),
("2D6", "000052868", "HALOPERIDOL", "INDUCER", "HUMAN"),
("2D6", "000151677", "HALOTHANE", "SUBSTRATE", "HUMAN"),
("2D6", "000051456", "HISTAMINE", "INHIBITOR", "HUMAN"),
("2D6", "007647010", "HYDROCHLORICACID", "INHIBITOR", "HUMAN"),
("2D6", "000125291", "HYDROCODONE", "SUBSTRATE", "HUMAN"),
("2D6", "007722841", "HYDROGENPEROXIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000466999", "HYDROMORPHONE", "SUBSTRATE", "HUMAN"),
("2D6", "000127071", "HYDROXYCARBAMIDE", "INHIBITOR", "HUMAN"),
("2D6", "000118423", "HYDROXYCHLOROQUINE", "INHIBITOR", "HUMAN"),
("2D6", "000068882", "HYDROXYZIN", "INHIBITOR", "HUMAN"),
("2D6", "000068882", "HYDROXYZINE", "INHIBITOR", "HUMAN"),
("2D6", "058957929", "IDARUBICIN", "INHIBITOR", "HUMAN"),
("2D6", "058957929", "IDARUBICIN", "SUBSTRATE", "HUMAN"),
("2D6", "152459955", "IMATINIB", "SUBSTRATE", ""),
("2D6", "152459955", "IMATINIB", "INHIBITOR", ""),
("2D6", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050497", "IMIPRAMINE", "INHIBITOR", "RAT"),
("2D6", "150378179", "INDINAVIR", "SUBSTRATE", ""),
("2D6", "150378179", "INDINAVIR", "INHIBITOR", "HUMAN"),
("2D6", "026844122", "INDORAMIN", "SUBSTRATE", "HUMAN"),
("2D6", "138402116", "IRBESARTAN", "INHIBITOR", "HUMAN"),
("2D6", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("2D6", "084625616", "ITRACONAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "036894696", "LABETALOL", "INHIBITOR", "HUMAN"),
("2D6", "036894696", "LABETALOL", "SUBSTRATE", "HUMAN"),
("2D6", "103577453", "LANSOPRAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "100427267", "LERCANIDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "000059927", "LEVODOPA", "SUBSTRATE", "HUMAN"),
("2D6", "000060991", "LEVOMEPROMAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000060991", "LEVOMEPROMAZINE", "INHIBITOR", "HUMAN"),
("2D6", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("2D6", "000137586", "LIDOCAIN", "INHIBITOR", "HUMAN"),
("2D6", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("2D6", "000137586", "LIDOCAINE", "INHIBITOR", "HUMAN"),
("2D6", "018016803", "LISURID", "SUBSTRATE", "HUMAN"),
("2D6", "018016803", "LISURIDE", "SUBSTRATE", "HUMAN"),
("2D6", "023047258", "LOFEPRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "013010474", "LOMUSTINE", "INHIBITOR", "HUMAN"),
("2D6", "013010474", "LOMUSTINE", "SUBSTRATE", "HUMAN"),
("2D6", "053179116", "LOPERAMIDE", "SUBSTRATE", ""),
("2D6", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("2D6", "079794755", "LORATADINE", "SUBSTRATE", "HUMAN"),
("2D6", "079794755", "LORATADINE", "INDUCER", "HUMAN"),
("2D6", "079794755", "LORATADINE", "INHIBITOR", "HUMAN"),
("2D6", "075330755", "LOVASTATIN", "INHIBITOR", "HUMAN"),
("2D6", "089226506", "MANIDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "010262698", "MAPROTILINE", "SUBSTRATE", "HUMAN"),
("2D6", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("2D6", "053230107", "MEFLOQUINE", "INHIBITOR", "HUMAN"),
("2D6", "003575802", "MELPERONE", "INHIBITOR", "HUMAN"),
("2D6", "019982082", "MEMANTINE", "INHIBITOR", "HUMAN"),
("2D6", "000091849", "MEPYRAMINE", "INHIBITOR", "HUMAN"),
("2D6", "029216282", "MEQUITAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "005588330", "MESORIDAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000537462", "METAMFETAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000537462", "METAMFETAMINE", "INHIBITOR", "HUMAN"),
("2D6", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("2D6", "000076993", "METHADONE", "INHIBITOR", "HUMAN"),
("2D6", "000554574", "METHAZOLAMIDE", "INHIBITOR", "HUMAN"),
("2D6", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("2D6", "000093301", "METHOXYPHENAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000555306", "METHYLDOPA(LEVOROTATORY)", "SUBSTRATE", "HUMAN"),
("2D6", "000555306", "METHYLDOPA(RACEMIC)", "SUBSTRATE", "HUMAN"),
("2D6", "000113451", "METHYLPHENIDATE", "SUBSTRATE", "HUMAN"),
("2D6", "000113451", "METHYLPHENIDATE", "INHIBITOR", "HUMAN"),
("2D6", "000125644", "METHYPRYLON", "SUBSTRATE", "HUMAN"),
("2D6", "000364625", "METOCLOPRAMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000364625", "METOCLOPRAMIDE", "INHIBITOR", "HUMAN"),
("2D6", "037350586", "METOPROLOL", "SUBSTRATE", "HUMAN"),
("2D6", "037350586", "METOPROLOL", "INHIBITOR", "HUMAN"),
("2D6", "031828714", "MEXILETINE", "SUBSTRATE", "HUMAN"),
("2D6", "024219974", "MIANSERIN", "INHIBITOR", "HUMAN"),
("2D6", "024219974", "MIANSERIN", "SUBSTRATE", "HUMAN"),
("2D6", "116644532", "MIBEFRADIL", "INHIBITOR", "HUMAN"),
("2D6", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "042794763", "MIDODRINE", "INHIBITOR", "HUMAN"),
("2D6", "084371653", "MIFEPRISTONE", "INHIBITOR", "HUMAN"),
("2D6", "025905775", "MINAPRINE", "SUBSTRATE", "HUMAN"),
("2D6", "061337675", "MIRTAZAPINE", "SUBSTRATE", "HUMAN"),
("2D6", "061337675", "MIRTAZAPINE", "INHIBITOR", "HUMAN"),
("2D6", "061337675", "MIRTAZAPINE", "INDUCER", "HUMAN"),
("2D6", "108612459", "MIZOLASTINE", "INHIBITOR", ""),
("2D6", "071320779", "MOCLOBEMIDE", "INHIBITOR", "HUMAN"),
("2D6", "071320779", "MOCLOBEMIDE", "INDUCER", "HUMAN"),
("2D6", "071320779", "MOCLOBEMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000057272", "MORPHINE", "SUBSTRATE", "HUMAN"),
("2D6", "105816044", "NATEGLINIDE", "SUBSTRATE", "HUMAN"),
("2D6", "099200096", "NEBIVOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "083366669", "NEFAZODONE", "INHIBITOR", "HUMAN"),
("2D6", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("2D6", "129618402", "NEVIRAPINE", "SUBSTRATE", "HUMAN"),
("2D6", "129618402", "NEVIRAPINE", "INHIBITOR", "HUMAN"),
("2D6", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "055985325", "NICARDIPINE", "SUBSTRATE", "HUMAN"),
("2D6", "027848846", "NICERGOLIN", "SUBSTRATE", "HUMAN"),
("2D6", "027848846", "NICERGOLINE", "SUBSTRATE", "HUMAN"),
("2D6", "000098920", "NICOTINAMIDE", "INHIBITOR", "HUMAN"),
("2D6", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2D6", "000059676", "NICOTINICACID", "INHIBITOR", "HUMAN"),
("2D6", "021829254", "NIFEDIPINE", "SUBSTRATE", "HUMAN"),
("2D6", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("2D6", "000059870", "NITROFURAL", "SUBSTRATE", "HUMAN"),
("2D6", "000072695", "NORTRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2D6", "000072695", "NORTRIPTYLINE", "INHIBITOR", "HUMAN"),
("2D6", "000104143", "OCTOPAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "132539061", "OLANZAPINE", "SUBSTRATE", "HUMAN"),
("2D6", "132539061", "OLANZAPINE", "INHIBITOR", "HUMAN"),
("2D6", "073590586", "OMEPRAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "099614025", "ONDANSETRON", "INHIBITOR", "HUMAN"),
("2D6", "099614025", "ONDANSETRON", "SUBSTRATE", "HUMAN"),
("2D6", "000315720", "OPIPRAMOL", "SUBSTRATE", "HUMAN"),
("2D6", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("2D6", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("2D6", "021738421", "OXAMNIQUINE", "INHIBITOR", "HUMAN"),
("2D6", "060576138", "OXATOMIDE", "INHIBITOR", "HUMAN"),
("2D6", "060576138", "OXATOMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "006452717", "OXPRENOLOL", "INHIBITOR", "HUMAN"),
("2D6", "005633205", "OXYBUTYNIN", "INHIBITOR", "HUMAN"),
("2D6", "000076426", "OXYCODONE", "SUBSTRATE", "HUMAN"),
("2D6", "000103902", "PARACETAMOL", "SUBSTRATE", "HUMAN"),
("2D6", "198470847", "PARECOXIB", "INHIBITOR", "HUMAN"),
("2D6", "061869087", "PAROXETINE", "SUBSTRATE", "HUMAN"),
("2D6", "061869087", "PAROXETINE", "INHIBITOR", "HUMAN"),
("2D6", "000140647", "PENTAMIDINEISETHIONATE", "SUBSTRATE", "HUMAN"),
("2D6", "000077236", "PENTOXYVERINE", "SUBSTRATE", "HUMAN"),
("2D6", "000077236", "PENTOXYVERINE", "INHIBITOR", "HUMAN"),
("2D6", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000084979", "PERAZINE", "INHIBITOR", "HUMAN"),
("2D6", "066104221", "PERGOLIDE", "INHIBITOR", "HUMAN"),
("2D6", "006621472", "PERHEXILINE", "SUBSTRATE", "HUMAN"),
("2D6", "006621472", "PERHEXILINE", "INHIBITOR", "HUMAN"),
("2D6", "000058399", "PERPHENAZINE", "INHIBITOR", "HUMAN"),
("2D6", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("2D6", "000060800", "PHENAZONE", "INHIBITOR", "HUMAN"),
("2D6", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2D6", "000114863", "PHENFORMIN", "SUBSTRATE", "HUMAN"),
("2D6", "000122098", "PHENTERMINE", "INHIBITOR", "HUMAN"),
("2D6", "002062784", "PIMOZIDE", "INHIBITOR", "HUMAN"),
("2D6", "013523869", "PINDOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "013523869", "PINDOLOL", "INDUCER", "HUMAN"),
("2D6", "013523869", "PINDOLOL", "INHIBITOR", "HUMAN"),
("2D6", "111025468", "PIOGLITAZONE", "INHIBITOR", "HUMAN"),
("2D6", "000110850", "PIPERAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "035080116", "PRAJMALINE", "SUBSTRATE", "HUMAN"),
("2D6", "081093370", "PRAVASTATIN", "INHIBITOR", "HUMAN"),
("2D6", "055268741", "PRAZIQUANTEL", "INHIBITOR", "HUMAN"),
("2D6", "000090346", "PRIMAQUINE", "INHIBITOR", "HUMAN"),
("2D6", "000051069", "PROCAINAMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000058388", "PROCHLORPERAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("2D6", "000500925", "PROGUANIL", "INHIBITOR", "HUMAN"),
("2D6", "000060877", "PROMETHAZIN", "INHIBITOR", "HUMAN"),
("2D6", "000060877", "PROMETHAZIN", "SUBSTRATE", "HUMAN"),
("2D6", "000060877", "PROMETHAZINE", "INHIBITOR", "HUMAN"),
("2D6", "000060877", "PROMETHAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "054063535", "PROPAFENONE", "INHIBITOR", "POTENT"),
("2D6", "054063535", "PROPAFENONE", "SUBSTRATE", "HUMAN"),
("2D6", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2D6", "002078548", "PROPOFOL", "INHIBITOR", "HUMAN"),
("2D6", "000525666", "PROPRANOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "000525666", "PROPRANOLOL", "INHIBITOR", "HUMAN"),
("2D6", "000438608", "PROTRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2D6", "000090824", "PSEUDOEPHEDRINE", "SUBSTRATE", "HUMAN"),
("2D6", "015686836", "PYRANTEL", "SUBSTRATE", "HUMAN"),
("2D6", "000058140", "PYRIMETHAMINE", "INHIBITOR", "HUMAN"),
("2D6", "111974697", "QUETIAPINE", "SUBSTRATE", "HUMAN"),
("2D6", "111974697", "QUETIAPINE", "INHIBITOR", "HUMAN"),
("2D6", "000056542", "QUINIDINE", "INHIBITOR", "HUMAN"),
("2D6", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("2D6", "066357355", "RANITIDINE", "INHIBITOR", "HUMAN"),
("2D6", "066357355", "RANITIDINE", "SUBSTRATE", "HUMAN"),
("2D6", "098769814", "REBOXETINE", "INHIBITOR", "HUMAN"),
("2D6", "098769814", "REBOXETINE", "INDUCER", "HUMAN"),
("2D6", "080125140", "REMOXIPRIDE", "SUBSTRATE", "HUMAN"),
("2D6", "106266062", "RISPERIDONE", "SUBSTRATE", "HUMAN"),
("2D6", "106266062", "RISPERIDONE", "INHIBITOR", "HUMAN"),
("2D6", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2D6", "155213675", "RITONAVIR", "SUBSTRATE", "HUMAN"),
("2D6", "123441032", "RIVASTIGMINE", "INHIBITOR", "HUMAN"),
("2D6", "091374219", "ROPINIROLE", "INHIBITOR", "HUMAN"),
("2D6", "084057954", "ROPIVACAINE", "SUBSTRATE", "HUMAN"),
("2D6", "122320734", "ROSIGLITAZONE", "INHIBITOR", "HUMAN"),
("2D6", "078273800", "ROXATIDINE", "SUBSTRATE", "HUMAN"),
("2D6", "000153184", "RUTOSIDE", "INHIBITOR", "HUMAN"),
("2D6", "127779208", "SAQUINAVIR", "SUBSTRATE", "HUMAN"),
("2D6", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("2D6", "014611519", "SELEGILINE", "SUBSTRATE", ""),
("2D6", "014611519", "SELEGILINE", "INHIBITOR", "HUMAN"),
("2D6", "106516249", "SERTINDOLE", "SUBSTRATE", "HUMAN"),
("2D6", "079617962", "SERTRALINE", "INHIBITOR", "HUMAN"),
("2D6", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("2D6", "139755832", "SILDENAFIL", "INHIBITOR", "HUMAN"),
("2D6", "139755832", "SILDENAFIL", "SUBSTRATE", "HUMAN"),
("2D6", "079902639", "SIMVASTATIN", "SUBSTRATE", "HUMAN"),
("2D6", "079902639", "SIMVASTATIN", "INHIBITOR", "HUMAN"),
("2D6", "051110011", "SOMATOSTATIN", "INHIBITOR", "HUMAN"),
("2D6", "000090391", "SPARTEINE", "SUBSTRATE", "HUMAN"),
("2D6", "000090391", "SPARTEINE", "INHIBITOR", "HUMAN"),
("2D6", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "000526089", "SULFAFENAZOL", "INHIBITOR", "HUMAN"),
("2D6", "000063741", "SULFANILAMIDE", "INHIBITOR", "HUMAN"),
("2D6", "000526089", "SULFAPHENAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "010540291", "TAMOXIFEN", "INHIBITOR", "HUMAN"),
("2D6", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("2D6", "106133204", "TAMSULOSIN", "SUBSTRATE", "HUMAN"),
("2D6", "145158710", "TEGASEROD", "SUBSTRATE", "HUMAN"),
("2D6", "145158710", "TEGASEROD", "INHIBITOR", "HUMAN"),
("2D6", "191114484", "TELITHROMYCIN", "INHIBITOR", "HUMAN"),
("2D6", "091161716", "TERBINAFINE", "INHIBITOR", "HUMAN"),
("2D6", "050679088", "TERFENADINE", "SUBSTRATE", "HUMAN"),
("2D6", "050679088", "TERFENADINE", "INHIBITOR", "HUMAN"),
("2D6", "000466900", "THEBACON", "SUBSTRATE", "HUMAN"),
("2D6", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("2D6", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("2D6", "000050522", "THIORIDAZINE", "SUBSTRATE", "HUMAN"),
("2D6", "000050522", "THIORIDAZINE", "INHIBITOR", "HUMAN"),
("2D6", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2D6", "026839758", "TIMOLOL", "SUBSTRATE", "HUMAN"),
("2D6", "026839758", "TIMOLOL", "INHIBITOR", ""),
("2D6", "003313266", "TIOTIXENE", "INHIBITOR", "HUMAN"),
("2D6", "136310935", "TIOTROPIUMBROMIDE", "SUBSTRATE", "HUMAN"),
("2D6", "000728881", "TOLPERISONE", "SUBSTRATE", ""),
("2D6", "124937515", "TOLTERODINE", "SUBSTRATE", "HUMAN"),
("2D6", "114899773", "TRABECTEDIN", "SUBSTRATE", "HUMAN"),
("2D6", "027203925", "TRAMADOL", "SUBSTRATE", "HUMAN"),
("2D6", "027203925", "TRAMADOL", "INHIBITOR", "HUMAN"),
("2D6", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("2D6", "019794935", "TRAZODONE", "SUBSTRATE", "HUMAN"),
("2D6", "000749133", "TRIFLUPERIDOL", "SUBSTRATE", "HUMAN"),
("2D6", "000739719", "TRIMIPRAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "000091816", "TRIPELENNAMINE", "INHIBITOR", "HUMAN"),
("2D6", "000486124", "TRIPROLIDINE", "INHIBITOR", "HUMAN"),
("2D6", "089565684", "TROPISETRON", "SUBSTRATE", "HUMAN"),
("2D6", "089565684", "TROPISETRON", "INHIBITOR", "HUMAN"),
("2D6", "010405024", "TROSPIUM", "INHIBITOR", ""),
("2D6", "X030", "TROSPIUM", "INHIBITOR", "HUMAN"),
("2D6", "093413695", "VENLAFAXINE", "SUBSTRATE", "HUMAN"),
("2D6", "093413695", "VENLAFAXINE", "INHIBITOR", "HUMAN"),
("2D6", "000052539", "VERAPAMIL", "INHIBITOR", "HUMAN"),
("2D6", "000865214", "VINBLASTINE", "SUBSTRATE", "HUMAN"),
("2D6", "000865214", "VINBLASTINE", "INHIBITOR", "HUMAN"),
("2D6", "001617909", "VINCAMIN", "SUBSTRATE", "HUMAN"),
("2D6", "001617909", "VINCAMINE", "SUBSTRATE", "HUMAN"),
("2D6", "071486221", "VINORELBINE", "SUBSTRATE", "HUMAN"),
("2D6", "071486221", "VINORELBINE", "INHIBITOR", "HUMAN"),
("2D6", "000146485", "YOHIMBIN", "SUBSTRATE", "HUMAN"),
("2D6", "000146485", "YOHIMBIN", "INHIBITOR", "HUMAN"),
("2D6", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("2D6", "007481892", "ZALCITABINE", "SUBSTRATE", "HUMAN"),
("2D6", "146939277", "ZIPRASIDONE", "INHIBITOR", "HUMAN"),
("2D6", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("2D6", "053772831", "ZUCLOPENTHIXOL", "SUBSTRATE", "HUMAN"),
("2D6", "061379655", "RIFAPENTINE", "INDUCER", "HUMAN"),
("2E1", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "SUBSTRATE", "HUMAN"),
("2E1", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INDUCER", "HUMAN"),
("2E1", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INHIBITOR", "HUMAN"),
("2E1", "056180940", "ACARBOSE", "INDUCER", "RAT"),
("2E1", "056180940", "ACARBOSE", "INHIBITOR", "RAT"),
("2E1", "029908030", "ADEMETIONIN", "SUBSTRATE", "HUMAN"),
("2E1", "029908030", "ADEMETIONIN", "INHIBITOR", "HUMAN"),
("2E1", "029908030", "ADEMETIONINE", "SUBSTRATE", "HUMAN"),
("2E1", "029908030", "ADEMETIONINE", "INHIBITOR", "HUMAN"),
("2E1", "000315300", "ALLOPURINOL", "INHIBITOR", "RAT"),
("2E1", "122852420", "ALOSETRON", "INHIBITOR", "HUMAN"),
("2E1", "000317340", "AMINOPHYLLINE", "SUBSTRATE", "HUMAN"),
("2E1", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("2E1", "000050486", "AMITRIPTYLINE", "INHIBITOR", "HUMAN"),
("2E1", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("2E1", "000094097", "BENZOCAINE", "INHIBITOR", "SPARUSAURATA(FISH)"),
("2E1", "000642728", "BENZYDAMINE", "SUBSTRATE", "HUMAN"),
("2E1", "060628968", "BIFONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "001812302", "BROMAZEPAM", "INHIBITOR", "HUMAN"),
("2E1", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("2E1", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("2E1", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("2E1", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("2E1", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("2E1", "072956093", "CARVEDILOL", "SUBSTRATE", "HUMAN"),
("2E1", "000067663", "CHLOROFORM", "SUBSTRATE", "HUMAN"),
("2E1", "000088040", "CHLOROXYLENOL", "SUBSTRATE", "HUMAN"),
("2E1", "000050533", "CHLORPROMAZINE", "INHIBITOR", "HUMAN"),
("2E1", "000095250", "CHLORZOXAZONE", "SUBSTRATE", "HUMAN"),
("2E1", "000095250", "CHLORZOXAZONE", "INHIBITOR", "HUMAN"),
("2E1", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("2E1", "015663271", "CISPLATIN", "SUBSTRATE", "MOUSE"),
("2E1", "059729338", "CITALOPRAM", "SUBSTRATE", "HUMAN"),
("2E1", "000637070", "CLOFIBRATE", "INDUCER", "HUMAN"),
("2E1", "000533459", "CLOMETHIAZOLE", "INHIBITOR", "MOUSE"),
("2E1", "000911455", "CLOMIFENE", "INHIBITOR", "HUMAN"),
("2E1", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("2E1", "000064868", "COLCHICINE", "INDUCER", "HUMAN"),
("2E1", "004342034", "DACARBAZINE", "SUBSTRATE", "HUMAN"),
("2E1", "000080080", "DAPSONE", "SUBSTRATE", "HUMAN"),
("2E1", "000050475", "DESIPRAMINE", "INHIBITOR", "HUMAN"),
("2E1", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("2E1", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("2E1", "003239449", "DEXFENFLURAMINE", "INHIBITOR", "HUMAN"),
("2E1", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("2E1", "015307865", "DICLOFENAC", "INHIBITOR", "HUMAN"),
("2E1", "000060297", "DIETHYLETHER", "INDUCER", "RAT"),
("2E1", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("2E1", "000067630", "DIIODOHYDROXYPROPANE", "INDUCER", "RAT"),
("2E1", "000067630", "DIIODOHYDROXYPROPANE", "INHIBITOR", "HUMAN"),
("2E1", "000097778", "DISULFIRAM", "SUBSTRATE", ""),
("2E1", "000097778", "DISULFIRAM", "INHIBITOR", "HUMAN"),
("2E1", "120279961", "DORZOLAMIDE", "SUBSTRATE", "RAT"),
("2E1", "027220479", "ECONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "013838169", "ENFLURANE", "SUBSTRATE", "HUMAN"),
("2E1", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("2E1", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("2E1", "000064175", "ETHANOL", "SUBSTRATE", "HUMAN"),
("2E1", "000064175", "ETHANOL", "INDUCER", "HUMAN"),
("2E1", "000064175", "ETHANOL", "INHIBITOR", "HUMAN"),
("2E1", "000077678", "ETHOSUXIMIDE", "SUBSTRATE", "HUMAN"),
("2E1", "033419420", "ETOPOSIDE", "SUBSTRATE", "HUMAN"),
("2E1", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("2E1", "025451154", "FELBAMATE", "SUBSTRATE", "HUMAN"),
("2E1", "000530789", "FLUFENAMICACID", "INDUCER", "MOUSE"),
("2E1", "000530789", "FLUFENAMINS�URE", "INDUCER", "MOUSE"),
("2E1", "042835256", "FLUMEQUINE", "INHIBITOR", "MOUSE"),
("2E1", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("2E1", "000069238", "FLUPHENAZINE", "INHIBITOR", "HUMAN"),
("2E1", "017617231", "FLURAZEPAM", "INHIBITOR", "HUMAN"),
("2E1", "054739183", "FLUVOXAMINE", "SUBSTRATE", "HUMAN"),
("2E1", "000059303", "FOLICACID", "SUBSTRATE", "HUMAN"),
("2E1", "007554656", "FOMEPIZOLE", "INHIBITOR", "HUMAN"),
("2E1", "000056815", "GLYCEROL", "INDUCER", "HUMAN"),
("2E1", "000151677", "HALOTHANE", "SUBSTRATE", "HUMAN"),
("2E1", "000050497", "IMIPRAMINE", "INHIBITOR", "HUMAN"),
("2E1", "011061680", "INSULIN(BEEF)", "INHIBITOR", "RAT"),
("2E1", "011061680", "INSULIN(HUMAN)", "INHIBITOR", "RAT"),
("2E1", "011061680", "INSULIN(PORK)", "INHIBITOR", "RAT"),
("2E1", "035212227", "IPRIFLAVONE", "INDUCER", "RAT"),
("2E1", "026675467", "ISOFLURANE", "SUBSTRATE", "HUMAN"),
("2E1", "000054853", "ISONIAZID", "INDUCER", "HUMAN"),
("2E1", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("2E1", "000054853", "ISONIAZID", "SUBSTRATE", "HUMAN"),
("2E1", "000067630", "ISOPROPANOL", "INDUCER", "RAT"),
("2E1", "000067630", "ISOPROPANOL", "INHIBITOR", "HUMAN"),
("2E1", "000087332", "ISOSORBIDEDINITRATE", "INHIBITOR", "HUMAN"),
("2E1", "084625616", "ITRACONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "000541151", "LEVOCARNITINE", "SUBSTRATE", "RAT"),
("2E1", "000060991", "LEVOMEPROMAZINE", "INHIBITOR", "HUMAN"),
("2E1", "002898126", "MEDAZEPAM", "INHIBITOR", "HUMAN"),
("2E1", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("2E1", "000058275", "MENADIONE", "SUBSTRATE", "HUMAN"),
("2E1", "000057534", "MEPROBAMATE", "SUBSTRATE", "HUMAN"),
("2E1", "000554574", "METHAZOLAMIDE", "INHIBITOR", "HUMAN"),
("2E1", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("2E1", "000054364", "METYRAPONE", "INHIBITOR", "HUMAN"),
("2E1", "031828714", "MEXILETINE", "SUBSTRATE", "HUMAN"),
("2E1", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "065271809", "MITOXANTRONE", "SUBSTRATE", "HUMAN"),
("2E1", "108612459", "MIZOLASTINE", "INHIBITOR", ""),
("2E1", "002272119", "MONOETHANOLAMINEOLEATE", "SUBSTRATE", "HUMAN"),
("2E1", "007647145", "NATRIUMCHLORID", "INDUCER", "HUMAN"),
("2E1", "055985325", "NICARDIPINE", "SUBSTRATE", "HUMAN"),
("2E1", "000098920", "NICOTINAMIDE", "INHIBITOR", "HUMAN"),
("2E1", "000054115", "NICOTINE", "INDUCER", "RAT"),
("2E1", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("2E1", "000054115", "NICOTINE", "INHIBITOR", "HUMAN"),
("2E1", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("2E1", "075530686", "NILVADIPINE", "SUBSTRATE", "HUMAN"),
("2E1", "000072695", "NORTRIPTYLINE", "INHIBITOR", "HUMAN"),
("2E1", "099614025", "ONDANSETRON", "SUBSTRATE", "HUMAN"),
("2E1", "061825943", "OXALIPLATIN", "SUBSTRATE", "HUMAN"),
("2E1", "009011976", "PANCREOZYMIN(CHOLECYSTOKININ)", "INHIBITOR", "HUMAN"),
("2E1", "000103902", "PARACETAMOL", "SUBSTRATE", "HUMAN"),
("2E1", "000311455", "PARAOXON", "SUBSTRATE", "HUMAN"),
("2E1", "000555577", "PARGYLINE", "INHIBITOR", "MOUSE"),
("2E1", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("2E1", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("2E1", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("2E1", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("2E1", "000050066", "PHENOBARBITAL", "SUBSTRATE", "HUMAN"),
("2E1", "000108952", "PHENOL", "SUBSTRATE", "MOUSE"),
("2E1", "000092137", "PILOCARPIN", "SUBSTRATE", "HUMAN"),
("2E1", "000092137", "PILOCARPINE", "SUBSTRATE", "HUMAN"),
("2E1", "002062784", "PIMOZIDE", "INHIBITOR", "HUMAN"),
("2E1", "000500925", "PROGUANIL", "SUBSTRATE", "HUMAN"),
("2E1", "002078548", "PROPOFOL", "INHIBITOR", "HUMAN"),
("2E1", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("2E1", "000056542", "QUINIDINE", "SUBSTRATE", "HUMAN"),
("2E1", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("2E1", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("2E1", "014611519", "SELEGILINE", "INHIBITOR", "HUMAN"),
("2E1", "028523866", "SEVOFLURANE", "SUBSTRATE", "HUMAN"),
("2E1", "139755832", "SILDENAFIL", "INHIBITOR", "HUMAN"),
("2E1", "007647145", "SODIUMCHLORIDE", "INDUCER", "HUMAN"),
("2E1", "000054217", "SODIUMSALICYLATE", "INDUCER", ""),
("2E1", "018883664", "STREPTOZOCIN", "INDUCER", "RAT"),
("2E1", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "000068359", "SULFADIAZINE", "SUBSTRATE", "HUMAN"),
("2E1", "000063741", "SULFANILAMIDE", "INHIBITOR", "HUMAN"),
("2E1", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("2E1", "017902237", "TEGAFUR", "SUBSTRATE", "HUMAN"),
("2E1", "145158710", "TEGASEROD", "INHIBITOR", "HUMAN"),
("2E1", "000083670", "THEOBROMINE", "SUBSTRATE", "HUMAN"),
("2E1", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("2E1", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "000076755", "THIOPENTAL", "INHIBITOR", "HUMAN"),
("2E1", "000050522", "THIORIDAZINE", "INHIBITOR", "HUMAN"),
("2E1", "014383507", "THIOSULFATE", "INHIBITOR", "HUMAN"),
("2E1", "000137268", "THIRAM", "SUBSTRATE", "RAT"),
("2E1", "005630535", "TIBOLONE", "INHIBITOR", "HUMAN"),
("2E1", "055142853", "TICLOPIDINE", "INHIBITOR", "HUMAN"),
("2E1", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("2E1", "001406662", "TOCOPHEROL(VITE)", "INHIBITOR", "RAT"),
("2E1", "114899773", "TRABECTEDIN", "SUBSTRATE", "HUMAN"),
("2E1", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("2E1", "000302794", "TRETINOIN", "INDUCER", ""),
("2E1", "000079016", "TRICHLOROETHYLENE", "SUBSTRATE", "MOUSE"),
("2E1", "000079016", "TRICHLOROETHYLENE", "INHIBITOR", "HUMAN"),
("2E1", "000127480", "TRIMETHADIONE", "SUBSTRATE", "HUMAN"),
("2E1", "010405024", "TROSPIUM", "INHIBITOR", ""),
("2E1", "000128132", "URSODEOXYCHOLICACID", "INDUCER", "HUMAN"),
("2E1", "000128132", "URSODEOXYCHOLICACID", "INHIBITOR", "HUMAN"),
("2E1", "001617909", "VINCAMIN", "SUBSTRATE", "HUMAN"),
("2E1", "001617909", "VINCAMINE", "SUBSTRATE", "HUMAN"),
("2E1", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("2E1", "043200802", "ZOPICLONE", "SUBSTRATE", "HUMAN"),
("2E1", "003416248", "GLUCOSAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INDUCER", "HUMAN"),
("3A4", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "SUBSTRATE", "HUMAN"),
("3A4", "000064175", "2-(4-CHLORPHENOXY)-ETHANOL", "INHIBITOR", "HUMAN"),
("3A4", "000059665", "ACETAZOLAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "029908030", "ADEMETIONIN", "INHIBITOR", "HUMAN"),
("3A4", "029908030", "ADEMETIONINE", "INHIBITOR", "HUMAN"),
("3A4", "037115325", "ADINAZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "054965218", "ALBENDAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "071195589", "ALFENTANIL", "SUBSTRATE", "HUMAN"),
("3A4", "081403807", "ALFUZOSIN", "SUBSTRATE", ""),
("3A4", "000432600", "ALLYLESTRENOL", "SUBSTRATE", "HUMAN"),
("3A4", "154323576", "ALMOTRIPTAN", "SUBSTRATE", "HUMAN"),
("3A4", "122852420", "ALOSETRON", "SUBSTRATE", "HUMAN"),
("3A4", "028981977", "ALPRAZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "018683915", "AMBROXOL", "INHIBITOR", "HUMAN"),
("3A4", "018683915", "AMBROXOL", "SUBSTRATE", "HUMAN"),
("3A4", "000125848", "AMINOGLUTHETIMIDE", "INDUCER", "HUMAN"),
("3A4", "000058151", "AMINOPHENAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "000317340", "AMINOPHYLLINE", "SUBSTRATE", "HUMAN"),
("3A4", "001951253", "AMIODARONE", "INHIBITOR", "PARTIAL"),
("3A4", "001951253", "AMIODARONE", "SUBSTRATE", "HUMAN"),
("3A4", "000050486", "AMITRIPTYLINE", "SUBSTRATE", "HUMAN"),
("3A4", "088150429", "AMLODIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "088150429", "AMLODIPINE", "INHIBITOR", "HUMAN"),
("3A4", "161814499", "AMPRENAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "161814499", "AMPRENAVIR", "INHIBITOR", "HUMAN"),
("3A4", "120511731", "ANASTROZOLE", "INHIBITOR", "HUMAN"),
("3A4", "170729803", "APREPITANT", "SUBSTRATE", "HUMAN"),
("3A4", "170729803", "APREPITANT", "INHIBITOR", "HUMAN"),
("3A4", "074863846", "ARGATROBAN", "SUBSTRATE", "HUMAN"),
("3A4", "129722129", "ARIPIPRAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "001327533", "ARSENICTRIOXIDE", "INHIBITOR", "HUMAN"),
("3A4", "071939510", "ARTEMETHER", "SUBSTRATE", "HUMAN"),
("3A4", "063968649", "ARTEMISININ", "INDUCER", "HUMAN"),
("3A4", "063968649", "ARTEMISININ", "SUBSTRATE", "HUMAN"),
("3A4", "068844779", "ASTEMIZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "068844779", "ASTEMIZOLE", "INHIBITOR", "HUMAN"),
("3A4", "029122687", "ATENOLOL", "SUBSTRATE", ""),
("3A4", "083015263", "ATOMOXETINE", "INHIBITOR", "HUMAN"),
("3A4", "134523005", "ATORVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "134523005", "ATORVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "003964816", "AZATADINE", "INDUCER", "HUMAN"),
("3A4", "058581898", "AZELASTINE", "SUBSTRATE", "HUMAN"),
("3A4", "058581898", "AZELASTINE", "INHIBITOR", "HUMAN"),
("3A4", "083905015", "AZITHROMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "083905015", "AZITHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "078110380", "AZTREONAM", "SUBSTRATE", "MONKEY"),
("3A4", "104713759", "BARNIDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "104713759", "BARNIDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "105979177", "BENIDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "000121540", "BENZETHONIUM", "INHIBITOR", "HUMAN"),
("3A4", "000094097", "BENZOCAINE", "INHIBITOR", "SPARUSAURATA(FISH)"),
("3A4", "000642728", "BENZYDAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000484208", "BERGAPTEN", "INHIBITOR", "HUMAN"),
("3A4", "000378449", "BETAMETHASON", "INHIBITOR", "HUMAN"),
("3A4", "000378449", "BETAMETHASONE", "INHIBITOR", "HUMAN"),
("3A4", "153559490", "BEXAROTENE", "INDUCER", "HUMAN"),
("3A4", "153559490", "BEXAROTENE", "SUBSTRATE", "HUMAN"),
("3A4", "041859670", "BEZAFIBRATE", "SUBSTRATE", "HUMAN"),
("3A4", "090357065", "BICALUTAMIDE", "SUBSTRATE", ""),
("3A4", "090357065", "BICALUTAMIDE", "INHIBITOR", ""),
("3A4", "060628968", "BIFONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "066722449", "BISOPROLOL", "SUBSTRATE", "HUMAN"),
("3A4", "179324697", "BORTEZOMIB", "SUBSTRATE", "HUMAN"),
("3A4", "179324697", "BORTEZOMIB", "INHIBITOR", "HUMAN"),
("3A4", "147536978", "BOSENTAN", "SUBSTRATE", "HUMAN"),
("3A4", "147536978", "BOSENTAN", "INDUCER", "HUMAN"),
("3A4", "138890627", "BRINZOLAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "001812302", "BROMAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "025614033", "BROMOCRIPTINE", "SUBSTRATE", "HUMAN"),
("3A4", "025614033", "BROMOCRIPTINE", "INHIBITOR", "HUMAN"),
("3A4", "010457906", "BROMPERIDOL", "SUBSTRATE", "HUMAN"),
("3A4", "000086226", "BROMPHENIRAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "057801817", "BROTIZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "051333223", "BUDESONID", "SUBSTRATE", "HUMAN"),
("3A4", "051333223", "BUDESONIDE", "SUBSTRATE", "HUMAN"),
("3A4", "038396393", "BUPIVACAINE", "SUBSTRATE", "HUMAN"),
("3A4", "052485797", "BUPRENORPHINE", "INHIBITOR", "HUMAN"),
("3A4", "052485797", "BUPRENORPHINE", "SUBSTRATE", "HUMAN"),
("3A4", "034911552", "BUPROPION", "SUBSTRATE", "HUMAN"),
("3A4", "036505847", "BUSPIRONE", "SUBSTRATE", "HUMAN"),
("3A4", "000055981", "BUSULFAN", "SUBSTRATE", "HUMAN"),
("3A4", "000058082", "CAFFEINE", "INHIBITOR", "HUMAN"),
("3A4", "000058082", "CAFFEINE", "SUBSTRATE", "HUMAN"),
("3A4", "032222063", "CALCITRIOL", "INDUCER", "HUMAN"),
("3A4", "000404864", "CAPSAICIN", "SUBSTRATE", "HUMAN"),
("3A4", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("3A4", "000298464", "CARBAMAZEPINE", "SUBSTRATE", "HUMAN"),
("3A4", "000486168", "CARBINOXAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "072956093", "CARVEDILOL", "SUBSTRATE", "HUMAN"),
("3A4", "162808620", "CASPOFUNGIN", "INHIBITOR", "HUMAN"),
("3A4", "015686712", "CEFALEXIN", "SUBSTRATE", "HUMAN"),
("3A4", "169590425", "CELECOXIB", "SUBSTRATE", "HUMAN"),
("3A4", "184007952", "CELECOXIB", "SUBSTRATE", "HUMAN"),
("3A4", "145599866", "CERIVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "145599866", "CERIVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "083881510", "CETIRIZINE", "SUBSTRATE", ""),
("3A4", "000130950", "CHININ", "SUBSTRATE", "HUMAN"),
("3A4", "000130950", "CHININ", "INHIBITOR", "HUMAN"),
("3A4", "000130950", "CHININ", "INDUCER", "HUMAN"),
("3A4", "000056757", "CHLORAMPHENICOL", "INHIBITOR", "HUMAN"),
("3A4", "000058253", "CHLORDIAZEPOXIDE", "SUBSTRATE", "HUMAN"),
("3A4", "001961779", "CHLORMADINONE", "INHIBITOR", ""),
("3A4", "000054057", "CHLOROQUINE", "SUBSTRATE", "HUMAN"),
("3A4", "000132229", "CHLORPHENAMINE", "SUBSTRATE", ""),
("3A4", "000050533", "CHLORPROMAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000113597", "CHLORPROTHIXENE", "SUBSTRATE", ""),
("3A4", "000095250", "CHLORZOXAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "000095250", "CHLORZOXAZONE", "INHIBITOR", "HUMAN"),
("3A4", "053267019", "CIBENZOLINE", "SUBSTRATE", "HUMAN"),
("3A4", "141845821", "CICLESONIDE", "SUBSTRATE", "HUMAN"),
("3A4", "059865133", "CICLOSPORIN", "SUBSTRATE", "HUMAN"),
("3A4", "059865133", "CICLOSPORIN", "INHIBITOR", "HUMAN"),
("3A4", "132203704", "CILNIDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("3A4", "052214843", "CIPROFIBRATE", "SUBSTRATE", "HUMAN"),
("3A4", "085721331", "CIPROFLOXACIN", "INHIBITOR", "HUMAN"),
("3A4", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("3A4", "081098604", "CISAPRIDE", "INHIBITOR", "HUMAN"),
("3A4", "059729338", "CITALOPRAM", "SUBSTRATE", "HUMAN"),
("3A4", "081103119", "CLARITHROMYCIN", "INDUCER", "HUMAN"),
("3A4", "081103119", "CLARITHROMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "081103119", "CLARITHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "015686518", "CLEMASTINE", "INHIBITOR", "HUMAN"),
("3A4", "018323449", "CLINDAMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "018323449", "CLINDAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "022316478", "CLOBAZAM", "SUBSTRATE", "HUMAN"),
("3A4", "002030639", "CLOFAZIMINE", "SUBSTRATE", "HUMAN"),
("3A4", "002030639", "CLOFAZIMINE", "INHIBITOR", "HUMAN"),
("3A4", "000050293", "CLOFENOTANE", "INDUCER", ""),
("3A4", "000637070", "CLOFIBRATE", "SUBSTRATE", "HUMAN"),
("3A4", "000637070", "CLOFIBRATE", "INDUCER", "HUMAN"),
("3A4", "000533459", "CLOMETHIAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "000911455", "CLOMIFENE", "INHIBITOR", "HUMAN"),
("3A4", "000303491", "CLOMIPRAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "001622613", "CLONAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("3A4", "033671464", "CLOTIAZEPAM", "INHIBITOR", "HUMAN"),
("3A4", "033671464", "CLOTIAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "023593751", "CLOTRIMAZOLE", "INDUCER", "HUMAN"),
("3A4", "023593751", "CLOTRIMAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "005786210", "CLOZAPINE", "INDUCER", "HUMAN"),
("3A4", "005786210", "CLOZAPINE", "SUBSTRATE", "HUMAN"),
("3A4", "005786210", "CLOZAPINE", "INHIBITOR", "HUMAN"),
("3A4", "000050362", "COCAINE", "SUBSTRATE", "HUMAN"),
("3A4", "000050362", "COCAINE", "INHIBITOR", "HUMAN"),
("3A4", "000076573", "CODEINE", "SUBSTRATE", "HUMAN"),
("3A4", "000064868", "COLCHICINE", "SUBSTRATE", "HUMAN"),
("3A4", "000064868", "COLCHICINE", "INDUCER", "HUMAN"),
("3A4", "000064868", "COLCHICINE", "INHIBITOR", "HUMAN"),
("3A4", "003546030", "CYAMEMAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000052313", "CYCLOBARBITAL", "INDUCER", ""),
("3A4", "000303537", "CYCLOBENZAPRINE", "SUBSTRATE", "HUMAN"),
("3A4", "000050180", "CYCLOPHOSPHAMIDE", "INDUCER", "HUMAN"),
("3A4", "000050180", "CYCLOPHOSPHAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000050180", "CYCLOPHOSPHAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "000147944", "CYTARABINE", "SUBSTRATE", "HUMAN"),
("3A4", "017230885", "DANAZOL", "INHIBITOR", "HUMAN"),
("3A4", "007261974", "DANTROLENE", "SUBSTRATE", "HUMAN"),
("3A4", "000080080", "DAPSONE", "SUBSTRATE", "HUMAN"),
("3A4", "020830813", "DAUNORUBICIN", "SUBSTRATE", "HUMAN"),
("3A4", "020830813", "DAUNORUBICIN", "INHIBITOR", "HUMAN"),
("3A4", "136817599", "DELAVIRDINE", "SUBSTRATE", "HUMAN"),
("3A4", "136817599", "DELAVIRDINE", "INHIBITOR", "HUMAN"),
("3A4", "000050475", "DESIPRAMINE", "INHIBITOR", "HUMAN"),
("3A4", "054024225", "DESOGESTREL", "SUBSTRATE", "HUMAN"),
("3A4", "000050022", "DEXAMETHASON", "SUBSTRATE", "HUMAN"),
("3A4", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("3A4", "000050022", "DEXAMETHASON", "INHIBITOR", "HUMAN"),
("3A4", "000050022", "DEXAMETHASONE", "SUBSTRATE", "HUMAN"),
("3A4", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("3A4", "000050022", "DEXAMETHASONE", "INHIBITOR", "HUMAN"),
("3A4", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("3A4", "000469625", "DEXTROPROPOXYPHENE", "SUBSTRATE", "HUMAN"),
("3A4", "000469625", "DEXTROPROPOXYPHENE", "INHIBITOR", "HUMAN"),
("3A4", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "000439145", "DIAZEPAM", "INHIBITOR", "HUMAN"),
("3A4", "015307865", "DICLOFENAC", "INHIBITOR", ""),
("3A4", "015307865", "DICLOFENAC", "SUBSTRATE", "HUMAN"),
("3A4", "003116765", "DICLOXACILLIN", "INDUCER", ""),
("3A4", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000071636", "DIGITOXIN", "SUBSTRATE", "HUMAN"),
("3A4", "020830755", "DIGOXIN", "SUBSTRATE", "HUMAN"),
("3A4", "000484231", "DIHYDRALAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000484231", "DIHYDRALAZINE", "INHIBITOR", "HUMAN"),
("3A4", "000125280", "DIHYDROCODEIN", "SUBSTRATE", "HUMAN"),
("3A4", "000125280", "DIHYDROCODEINE", "SUBSTRATE", "HUMAN"),
("3A4", "000511126", "DIHYDROERGOTAMINE", "INHIBITOR", "HUMAN"),
("3A4", "000511126", "DIHYDROERGOTAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000128461", "DIHYDROSTREPTOMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "000067630", "DIIODOHYDROXYPROPANE", "INHIBITOR", "HUMAN"),
("3A4", "042399417", "DILTIAZEM", "SUBSTRATE", "HUMAN"),
("3A4", "042399417", "DILTIAZEM", "INHIBITOR", "HUMAN"),
("3A4", "000067685", "DIMETHYLSULFOXIDE", "INHIBITOR", "HUMAN"),
("3A4", "007456248", "DIMETOTIAZINE", "INHIBITOR", "HUMAN"),
("3A4", "000520343", "DIOSMECTITE", "INHIBITOR", "HUMAN"),
("3A4", "031065891", "DIPHENHYDRAMINEMETHYLBROMIDE", "SUBSTRATE", ""),
("3A4", "062013041", "DIRITHROMYCIN", "SUBSTRATE", ""),
("3A4", "003737095", "DISOPYRAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000097778", "DISULFIRAM", "SUBSTRATE", "HUMAN"),
("3A4", "000097778", "DISULFIRAM", "INHIBITOR", ""),
("3A4", "114977285", "DOCETAXEL", "SUBSTRATE", "HUMAN"),
("3A4", "114977285", "DOCETAXEL", "INHIBITOR", "HUMAN"),
("3A4", "115256116", "DOFETILIDE", "SUBSTRATE", "HUMAN"),
("3A4", "115956122", "DOLASETRON", "SUBSTRATE", ""),
("3A4", "057808669", "DOMPERIDONE", "SUBSTRATE", "HUMAN"),
("3A4", "120014064", "DONEPEZIL", "SUBSTRATE", "HUMAN"),
("3A4", "120279961", "DORZOLAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "074191858", "DOXAZOSIN", "SUBSTRATE", ""),
("3A4", "001668195", "DOXEPIN", "SUBSTRATE", ""),
("3A4", "023214928", "DOXORUBICIN", "INHIBITOR", "HUMAN"),
("3A4", "023214928", "DOXORUBICIN", "SUBSTRATE", "HUMAN"),
("3A4", "000564250", "DOXYCYCLINE", "SUBSTRATE", ""),
("3A4", "000564250", "DOXYCYCLINE", "INHIBITOR", "HUMAN"),
("3A4", "164656239", "DUTASTERIDE", "SUBSTRATE", "HUMAN"),
("3A4", "090729434", "EBASTINE", "SUBSTRATE", "HUMAN"),
("3A4", "027220479", "ECONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "154598524", "EFAVIRENZ", "INDUCER", "HUMAN"),
("3A4", "154598524", "EFAVIRENZ", "INHIBITOR", "HUMAN"),
("3A4", "154598524", "EFAVIRENZ", "SUBSTRATE", "HUMAN"),
("3A4", "143322581", "ELETRIPTAN", "SUBSTRATE", "HUMAN"),
("3A4", "143322581", "ELETRIPTAN", "INDUCER", "HUMAN"),
("3A4", "000483181", "EMETINE", "SUBSTRATE", "HUMAN"),
("3A4", "000483181", "EMETINE", "INHIBITOR", "HUMAN"),
("3A4", "075847733", "ENALAPRIL", "SUBSTRATE", "HUMAN"),
("3A4", "116314671", "ENTACAPONE", "INHIBITOR", ""),
("3A4", "080012437", "EPINASTINE", "SUBSTRATE", "HUMAN"),
("3A4", "000051434", "EPINEPHRIN", "INHIBITOR", "HUMAN"),
("3A4", "000051434", "EPINEPHRINE", "INHIBITOR", "HUMAN"),
("3A4", "107724209", "EPLERENONE", "SUBSTRATE", "HUMAN"),
("3A4", "000060797", "ERGOMETRINE", "INHIBITOR", "HUMAN"),
("3A4", "000113155", "ERGOTAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000113155", "ERGOTAMINE", "INHIBITOR", "HUMAN"),
("3A4", "000114078", "ERYTHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "000114078", "ERYTHROMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "128196010", "ESCITALOPRAM", "SUBSTRATE", "HUMAN"),
("3A4", "033643468", "ESKETAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "161973100", "ESOMEPRAZOLE", "SUBSTRATE", ""),
("3A4", "029975164", "ESTAZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "000050282", "ESTRADIOL", "SUBSTRATE", "HUMAN"),
("3A4", "002998574", "ESTRAMUSTINE", "SUBSTRATE", "HUMAN"),
("3A4", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("3A4", "000064175", "ETHANOL", "INDUCER", "HUMAN"),
("3A4", "000064175", "ETHANOL", "SUBSTRATE", "HUMAN"),
("3A4", "000064175", "ETHANOL", "INHIBITOR", "HUMAN"),
("3A4", "000057636", "ETHINYLESTRADIOL", "INDUCER", "HUMAN"),
("3A4", "000057636", "ETHINYLESTRADIOL", "INHIBITOR", "HUMAN"),
("3A4", "000057636", "ETHINYLESTRADIOL", "SUBSTRATE", "HUMAN"),
("3A4", "000077678", "ETHOSUXIMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000076584", "ETHYLMORPHINE", "SUBSTRATE", "HUMAN"),
("3A4", "040054691", "ETIZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "054048101", "ETONOGESTREL", "SUBSTRATE", "HUMAN"),
("3A4", "052942311", "ETOPERIDONE", "SUBSTRATE", "HUMAN"),
("3A4", "033419420", "ETOPOSIDE", "INDUCER", "HUMAN"),
("3A4", "033419420", "ETOPOSIDE", "INHIBITOR", "HUMAN"),
("3A4", "033419420", "ETOPOSIDE", "SUBSTRATE", "HUMAN"),
("3A4", "202409334", "ETORICOXIB", "INHIBITOR", "HUMAN"),
("3A4", "202409334", "ETORICOXIB", "SUBSTRATE", "HUMAN"),
("3A4", "159351696", "EVEROLIMUS", "SUBSTRATE", "HUMAN"),
("3A4", "107868304", "EXEMESTANE", "SUBSTRATE", "HUMAN"),
("3A4", "104227874", "FAMCICLOVIR", "SUBSTRATE", "HUMAN"),
("3A4", "025451154", "FELBAMATE", "INDUCER", "HUMAN"),
("3A4", "025451154", "FELBAMATE", "SUBSTRATE", "HUMAN"),
("3A4", "072509763", "FELODIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "072509763", "FELODIPINE", "INHIBITOR", "HUMAN"),
("3A4", "049562289", "FENOFIBRATE", "SUBSTRATE", "HUMAN"),
("3A4", "000437387", "FENTANYL", "SUBSTRATE", "HUMAN"),
("3A4", "000437387", "FENTANYL", "INHIBITOR", "HUMAN"),
("3A4", "083799240", "FEXOFENADINE", "SUBSTRATE", ""),
("3A4", "098319267", "FINASTERIDE", "SUBSTRATE", "HUMAN"),
("3A4", "076568020", "FLOSEQUINAN", "SUBSTRATE", "HUMAN"),
("3A4", "005250395", "FLUCLOXACILLIN", "INDUCER", "HUMAN"),
("3A4", "086386734", "FLUCONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "001622624", "FLUNITRAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "054910893", "FLUOXETINE", "SUBSTRATE", "HUMAN"),
("3A4", "054910893", "FLUOXETINE", "INHIBITOR", "HUMAN"),
("3A4", "017617231", "FLURAZEPAM", "SUBSTRATE", ""),
("3A4", "082664208", "FLURITHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "013311847", "FLUTAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "080474142", "FLUTICASONE", "SUBSTRATE", ""),
("3A4", "093957541", "FLUVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "093957541", "FLUVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("3A4", "226700794", "FOSAMPRENAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "226700794", "FOSAMPRENAVIR", "INHIBITOR", ""),
("3A4", "093390819", "FOSPHENYTOIN", "SUBSTRATE", ""),
("3A4", "093390819", "FOSPHENYTOIN", "INHIBITOR", ""),
("3A4", "129453618", "FULVESTRANT", "SUBSTRATE", "HUMAN"),
("3A4", "000357700", "GALANTAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "016662478", "GALLOPAMIL", "SUBSTRATE", "HUMAN"),
("3A4", "184475352", "GEFITINIB", "SUBSTRATE", "HUMAN"),
("3A4", "025812300", "GEMFIBROZIL", "INHIBITOR", "HUMAN"),
("3A4", "025812300", "GEMFIBROZIL", "SUBSTRATE", "HUMAN"),
("3A4", "025812300", "GEMFIBROZIL", "INDUCER", "HUMAN"),
("3A4", "083928761", "GEPIRONE", "SUBSTRATE", "HUMAN"),
("3A4", "010238218", "GLIBENCLAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "010238218", "GLIBENCLAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "029094619", "GLIPIZIDE", "SUBSTRATE", "HUMAN"),
("3A4", "109889090", "GRANISETRON", "SUBSTRATE", "HUMAN"),
("3A4", "000126078", "GRISEOFULVIN", "INDUCER", ""),
("3A4", "000055652", "GUANETHIDINE", "INDUCER", "HUMAN"),
("3A4", "069756532", "HALOFANTRINE", "SUBSTRATE", "HUMAN"),
("3A4", "000052868", "HALOPERIDOL", "SUBSTRATE", "HUMAN"),
("3A4", "000052868", "HALOPERIDOL", "INHIBITOR", ""),
("3A4", "000151677", "HALOTHANE", "SUBSTRATE", "HUMAN"),
("3A4", "000056291", "HEXOBARBITAL", "SUBSTRATE", "HUMAN"),
("3A4", "000051456", "HISTAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000051456", "HISTAMINE", "INHIBITOR", "HUMAN"),
("3A4", "000086544", "HYDRALAZINE", "INHIBITOR", "HUMAN"),
("3A4", "000050237", "HYDROCORTISONE", "INDUCER", ""),
("3A4", "000050237", "HYDROCORTISONE", "SUBSTRATE", "HUMAN"),
("3A4", "000050237", "HYDROCORTISONE", "INHIBITOR", "HUMAN"),
("3A4", "074050207", "HYDROCORTISONEACEPONATE", "SUBSTRATE", "HUMAN"),
("3A4", "000466999", "HYDROMORPHONE", "SUBSTRATE", "HUMAN"),
("3A4", "000123319", "HYDROQUINONE", "SUBSTRATE", "HUMAN"),
("3A4", "000090335", "HYMECROMONE", "SUBSTRATE", "HUMAN"),
("3A4", "003778732", "IFOSFAMIDE", "INDUCER", "HUMAN"),
("3A4", "003778732", "IFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "003778732", "IFOSFAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "152459955", "IMATINIB", "SUBSTRATE", "HUMAN"),
("3A4", "152459955", "IMATINIB", "INHIBITOR", "HUMAN"),
("3A4", "000050497", "IMIPRAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "006829987", "IMIPRAMINEOXIDE", "SUBSTRATE", "HUMAN"),
("3A4", "099011026", "IMIQUIMOD", "SUBSTRATE", "HUMAN"),
("3A4", "150378179", "INDINAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "150378179", "INDINAVIR", "INHIBITOR", "HUMAN"),
("3A4", "035212227", "IPRIFLAVONE", "SUBSTRATE", "HUMAN"),
("3A4", "035212227", "IPRIFLAVONE", "INHIBITOR", "HUMAN"),
("3A4", "138402116", "IRBESARTAN", "INHIBITOR", "HUMAN"),
("3A4", "097682445", "IRINOTECAN", "SUBSTRATE", "HUMAN"),
("3A4", "097682445", "IRINOTECAN", "INHIBITOR", "HUMAN"),
("3A4", "000054853", "ISONIAZID", "INHIBITOR", "HUMAN"),
("3A4", "000067630", "ISOPROPANOL", "INHIBITOR", "HUMAN"),
("3A4", "000087332", "ISOSORBIDEDINITRATE", "SUBSTRATE", "HUMAN"),
("3A4", "016051777", "ISOSORBIDEMONONITRATE", "SUBSTRATE", "HUMAN"),
("3A4", "004759482", "ISOTRETINOIN", "SUBSTRATE", ""),
("3A4", "075695931", "ISRADIPINE", "INHIBITOR", "HUMAN"),
("3A4", "075695931", "ISRADIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "084625616", "ITRACONAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "084625616", "ITRACONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "070288867", "IVERMECTIN", "SUBSTRATE", "HUMAN"),
("3A4", "016846245", "JOSAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "006740881", "KETAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000469794", "KETOBEMIDONE", "SUBSTRATE", "HUMAN"),
("3A4", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "065277421", "KETOCONAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "103890784", "LACIDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "103577453", "LANSOPRAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "103577453", "LANSOPRAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "103577453", "LANSOPRAZOLE", "INDUCER", "HUMAN"),
("3A4", "100427267", "LERCANIDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "100427267", "LERCANIDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "112809515", "LETROZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "001477403", "LEVACETYLMETHADOL", "SUBSTRATE", "HUMAN"),
("3A4", "027262471", "LEVOBUPIVACAINE", "SUBSTRATE", "HUMAN"),
("3A4", "100986854", "LEVOFLOXACIN", "INHIBITOR", "HUMAN"),
("3A4", "000797637", "LEVONORGESTREL", "SUBSTRATE", "HUMAN"),
("3A4", "000055038", "LEVOTHYROXINESODIUM", "SUBSTRATE", "HUMAN"),
("3A4", "000137586", "LIDOCAIN", "INHIBITOR", "HUMAN"),
("3A4", "000137586", "LIDOCAIN", "SUBSTRATE", "HUMAN"),
("3A4", "000137586", "LIDOCAINE", "INHIBITOR", "HUMAN"),
("3A4", "000137586", "LIDOCAINE", "SUBSTRATE", "HUMAN"),
("3A4", "018016803", "LISURID", "SUBSTRATE", "HUMAN"),
("3A4", "018016803", "LISURIDE", "SUBSTRATE", "HUMAN"),
("3A4", "013010474", "LOMUSTINE", "INHIBITOR", "HUMAN"),
("3A4", "053179116", "LOPERAMIDE", "SUBSTRATE", ""),
("3A4", "192725170", "LOPINAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "192725170", "LOPINAVIR", "INHIBITOR", "HUMAN"),
("3A4", "079794755", "LORATADINE", "SUBSTRATE", "HUMAN"),
("3A4", "079794755", "LORATADINE", "INDUCER", "HUMAN"),
("3A4", "079794755", "LORATADINE", "INHIBITOR", "HUMAN"),
("3A4", "114798264", "LOSARTAN", "SUBSTRATE", "HUMAN"),
("3A4", "114798264", "LOSARTAN", "INHIBITOR", "HUMAN"),
("3A4", "075330755", "LOVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "075330755", "LOVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "089226506", "MANIDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "031431397", "MEBENDAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "002898126", "MEDAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "032359345", "MEDIFOXAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000977797", "MEDROGESTONE", "SUBSTRATE", "RAT"),
("3A4", "000520854", "MEDROXYPROGESTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "000520854", "MEDROXYPROGESTERONE", "INDUCER", "HUMAN"),
("3A4", "002668668", "MEDRYSONE", "INHIBITOR", ""),
("3A4", "053230107", "MEFLOQUINE", "SUBSTRATE", "HUMAN"),
("3A4", "053230107", "MEFLOQUINE", "INHIBITOR", "HUMAN"),
("3A4", "071125387", "MELOXICAM", "SUBSTRATE", "HUMAN"),
("3A4", "000083896", "MEPACRINE", "SUBSTRATE", "HUMAN"),
("3A4", "029216282", "MEQUITAZINE", "INHIBITOR", "HUMAN"),
("3A4", "000068893", "METAMIZOLESODIUM", "INDUCER", "HUMAN"),
("3A4", "000072639", "METANDIENONE", "SUBSTRATE", "HUMAN"),
("3A4", "000076993", "METHADONE", "SUBSTRATE", "HUMAN"),
("3A4", "000076993", "METHADONE", "INDUCER", "HUMAN"),
("3A4", "000076993", "METHADONE", "INHIBITOR", "HUMAN"),
("3A4", "000072446", "METHAQUALONE", "SUBSTRATE", "HUMAN"),
("3A4", "000554574", "METHAZOLAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "000298817", "METHOXSALEN", "SUBSTRATE", "HUMAN"),
("3A4", "000076380", "METHOXYFLURANE", "SUBSTRATE", "HUMAN"),
("3A4", "000113428", "METHYLERGOMETRINE", "SUBSTRATE", ""),
("3A4", "000083432", "METHYLPREDNISOLONE", "SUBSTRATE", "HUMAN"),
("3A4", "000083432", "METHYLPREDNISOLONE", "INHIBITOR", "HUMAN"),
("3A4", "086401958", "METHYLPREDNISOLONEACEPONATE", "INDUCER", "HUMAN"),
("3A4", "000058184", "METHYLTESTOSTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "000443481", "METRONIDAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "000443481", "METRONIDAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "000054364", "METYRAPONE", "INDUCER", "HUMAN"),
("3A4", "000054364", "METYRAPONE", "INHIBITOR", "HUMAN"),
("3A4", "031828714", "MEXILETINE", "SUBSTRATE", "HUMAN"),
("3A4", "024219974", "MIANSERIN", "SUBSTRATE", "HUMAN"),
("3A4", "116644532", "MIBEFRADIL", "INHIBITOR", "HUMAN"),
("3A4", "116644532", "MIBEFRADIL", "SUBSTRATE", "HUMAN"),
("3A4", "022916478", "MICONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "022916478", "MICONAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "059467708", "MIDAZOLAM", "INHIBITOR", "HUMAN"),
("3A4", "059467708", "MIDAZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "035457808", "MIDECAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "084371653", "MIFEPRISTONE", "SUBSTRATE", "HUMAN"),
("3A4", "084371653", "MIFEPRISTONE", "INHIBITOR", "HUMAN"),
("3A4", "084371653", "MIFEPRISTONE", "INDUCER", "HUMAN"),
("3A4", "055881077", "MIOCAMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "055881077", "MIOCAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "061337675", "MIRTAZAPINE", "SUBSTRATE", "HUMAN"),
("3A4", "061337675", "MIRTAZAPINE", "INHIBITOR", "HUMAN"),
("3A4", "065271809", "MITOXANTRONE", "INHIBITOR", "HUMAN"),
("3A4", "108612459", "MIZOLASTINE", "INHIBITOR", ""),
("3A4", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("3A4", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("3A4", "068693118", "MODAFINIL", "SUBSTRATE", "HUMAN"),
("3A4", "000057272", "MORPHINE", "SUBSTRATE", "HUMAN"),
("3A4", "000465656", "NALOXONE", "SUBSTRATE", "HUMAN"),
("3A4", "105816044", "NATEGLINIDE", "SUBSTRATE", "HUMAN"),
("3A4", "083366669", "NEFAZODONE", "INHIBITOR", "HUMAN"),
("3A4", "083366669", "NEFAZODONE", "SUBSTRATE", "HUMAN"),
("3A4", "159989647", "NELFINAVIR", "SUBSTRATE", ""),
("3A4", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("3A4", "129618402", "NEVIRAPINE", "INDUCER", "HUMAN"),
("3A4", "129618402", "NEVIRAPINE", "INHIBITOR", "HUMAN"),
("3A4", "129618402", "NEVIRAPINE", "SUBSTRATE", "HUMAN"),
("3A4", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "055985325", "NICARDIPINE", "INDUCER", "HUMAN"),
("3A4", "055985325", "NICARDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "000098920", "NICOTINAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "000054115", "NICOTINE", "SUBSTRATE", "HUMAN"),
("3A4", "021829254", "NIFEDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "021829254", "NIFEDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "021829254", "NIFEDIPINE", "INDUCER", "HUMAN"),
("3A4", "075530686", "NILVADIPINE", "INHIBITOR", "HUMAN"),
("3A4", "066085594", "NIMODIPIN", "SUBSTRATE", "HUMAN"),
("3A4", "066085594", "NIMODIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "063675729", "NISOLDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "063675729", "NISOLDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "000146225", "NITRAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "039562704", "NITRENDIPINE", "INHIBITOR", "HUMAN"),
("3A4", "039562704", "NITRENDIPINE", "SUBSTRATE", "HUMAN"),
("3A4", "001088115", "NORDAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "000068224", "NORETHISTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "070458967", "NORFLOXACIN", "INHIBITOR", "HUMAN"),
("3A4", "000072695", "NORTRIPTYLINE", "SUBSTRATE", "HUMAN,RAT"),
("3A4", "000104143", "OCTOPAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000104143", "OCTOPAMINE", "INHIBITOR", "HUMAN"),
("3A4", "132539061", "OLANZAPINE", "INHIBITOR", "HUMAN"),
("3A4", "003922905", "OLEANDOMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "113806056", "OLOPATADINE", "SUBSTRATE", "HUMAN"),
("3A4", "073590586", "OMEPRAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "073590586", "OMEPRAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "073590586", "OMEPRAZOLE", "INDUCER", "HUMAN"),
("3A4", "099614025", "ONDANSETRON", "SUBSTRATE", "HUMAN"),
("3A4", "000083987", "ORPHENADRINE(CHLORIDE)", "INHIBITOR", "HUMAN"),
("3A4", "000083987", "ORPHENADRINE(CHLORIDE)", "SUBSTRATE", "HUMAN"),
("3A4", "000083987", "ORPHENADRINE(CITRATE)", "INHIBITOR", "HUMAN"),
("3A4", "000083987", "ORPHENADRINE(CITRATE)", "SUBSTRATE", "HUMAN"),
("3A4", "060576138", "OXATOMIDE", "INHIBITOR", "HUMAN"),
("3A4", "060576138", "OXATOMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000604751", "OXAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "028721075", "OXCARBAZEPINE", "INDUCER", "HUMAN"),
("3A4", "003689507", "OXOMEMAZINE", "INDUCER", "HUMAN"),
("3A4", "005633205", "OXYBUTYNIN", "INHIBITOR", "HUMAN"),
("3A4", "005633205", "OXYBUTYNIN", "SUBSTRATE", "HUMAN"),
("3A4", "033069624", "PACLITAXEL", "SUBSTRATE", "HUMAN"),
("3A4", "033069624", "PACLITAXEL", "INHIBITOR", "HUMAN"),
("3A4", "033069624", "PACLITAXEL", "INDUCER", "HUMAN"),
("3A4", "102625707", "PANTOPRAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "102625707", "PANTOPRAZOLE", "INDUCER", "HUMAN"),
("3A4", "000103902", "PARACETAMOL", "INDUCER", "HUMAN"),
("3A4", "000103902", "PARACETAMOL", "SUBSTRATE", "HUMAN"),
("3A4", "000103902", "PARACETAMOL", "INHIBITOR", "HUMAN"),
("3A4", "000311455", "PARAOXON", "SUBSTRATE", "HUMAN"),
("3A4", "198470847", "PARECOXIB", "SUBSTRATE", "HUMAN"),
("3A4", "061869087", "PAROXETINE", "INHIBITOR", ""),
("3A4", "000140647", "PENTAMIDINEISETHIONATE", "SUBSTRATE", "HUMAN"),
("3A4", "000077236", "PENTOXYVERINE", "SUBSTRATE", "HUMAN"),
("3A4", "000084979", "PERAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000084979", "PERAZINE", "INHIBITOR", "HUMAN"),
("3A4", "066104221", "PERGOLIDE", "INHIBITOR", "HUMAN"),
("3A4", "066104221", "PERGOLIDE", "SUBSTRATE", "HUMAN"),
("3A4", "006621472", "PERHEXILINE", "SUBSTRATE", "HUMAN"),
("3A4", "052645531", "PERMETHRIN", "SUBSTRATE", "HUMAN"),
("3A4", "000058399", "PERPHENAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057421", "PETHIDINE", "SUBSTRATE", "HUMAN"),
("3A4", "000062442", "PHENACETIN", "SUBSTRATE", "HUMAN"),
("3A4", "000060800", "PHENAZONE", "INHIBITOR", "HUMAN"),
("3A4", "000060800", "PHENAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "000051718", "PHENELZINE", "INHIBITOR", "HUMAN"),
("3A4", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("3A4", "000059961", "PHENOXYBENZAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000435972", "PHENPROCOUMON", "SUBSTRATE", "HUMAN"),
("3A4", "000050339", "PHENYLBUTAZONE", "INDUCER", "HUMAN"),
("3A4", "000057410", "PHENYTOIN", "INDUCER", ""),
("3A4", "000057410", "PHENYTOIN", "SUBSTRATE", "HUMAN"),
("3A4", "000057476", "PHYSOSTIGMINE", "INHIBITOR", "RAT"),
("3A4", "000092137", "PILOCARPIN", "SUBSTRATE", "HUMAN"),
("3A4", "000092137", "PILOCARPIN", "INHIBITOR", "HUMAN"),
("3A4", "000092137", "PILOCARPINE", "SUBSTRATE", "HUMAN"),
("3A4", "000092137", "PILOCARPINE", "INHIBITOR", "HUMAN"),
("3A4", "002062784", "PIMOZIDE", "INHIBITOR", "HUMAN"),
("3A4", "002062784", "PIMOZIDE", "SUBSTRATE", "HUMAN"),
("3A4", "085371648", "PINACIDIL", "SUBSTRATE", "HUMAN"),
("3A4", "111025468", "PIOGLITAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "111025468", "PIOGLITAZONE", "INDUCER", "HUMAN"),
("3A4", "019186357", "PODOPHYLLOTOXIN", "SUBSTRATE", "HUMAN"),
("3A4", "000053430", "PRASTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "081093370", "PRAVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "081093370", "PRAVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "002955386", "PRAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "055268741", "PRAZIQUANTEL", "SUBSTRATE", "HUMAN"),
("3A4", "000050248", "PREDNISOLON", "SUBSTRATE", "HUMAN"),
("3A4", "000050248", "PREDNISOLON", "INHIBITOR", "HUMAN"),
("3A4", "000050248", "PREDNISOLONE", "SUBSTRATE", "HUMAN"),
("3A4", "000050248", "PREDNISOLONE", "INHIBITOR", "HUMAN"),
("3A4", "000053032", "PREDNISONE", "SUBSTRATE", "HUMAN"),
("3A4", "000053032", "PREDNISONE", "INDUCER", "HUMAN"),
("3A4", "000053032", "PREDNISONE", "INHIBITOR", "HUMAN"),
("3A4", "000090346", "PRIMAQUINE", "SUBSTRATE", "HUMAN"),
("3A4", "000090346", "PRIMAQUINE", "INHIBITOR", "HUMAN"),
("3A4", "000125337", "PRIMIDONE", "INDUCER", "HUMAN"),
("3A4", "011006761", "PRISTINAMYCIN", "INDUCER", "HUMAN"),
("3A4", "011006761", "PRISTINAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "000057669", "PROBENECID", "INDUCER", "HUMAN"),
("3A4", "000058388", "PROCHLORPERAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057830", "PROGESTERONE", "INHIBITOR", "HUMAN"),
("3A4", "000057830", "PROGESTERONE", "INDUCER", "HUMAN"),
("3A4", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "000500925", "PROGUANIL", "SUBSTRATE", "HUMAN"),
("3A4", "000058402", "PROMAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "054063535", "PROPAFENONE", "SUBSTRATE", "HUMAN"),
("3A4", "060569199", "PROPIVERINE", "INHIBITOR", "HUMAN"),
("3A4", "002078548", "PROPOFOL", "INHIBITOR", "HUMAN"),
("3A4", "002078548", "PROPOFOL", "SUBSTRATE", "HUMAN"),
("3A4", "000525666", "PROPRANOLOL", "SUBSTRATE", "HUMAN"),
("3A4", "000098964", "PYRAZINAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000155975", "PYRIDOSTIGMINE", "INDUCER", "HUMAN"),
("3A4", "036735225", "QUAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "111974697", "QUETIAPINE", "SUBSTRATE", "HUMAN"),
("3A4", "000056542", "QUINIDINE", "INHIBITOR", "HUMAN"),
("3A4", "000056542", "QUINIDINE", "INDUCER", "HUMAN"),
("3A4", "000056542", "QUINIDINE", "SUBSTRATE", "HUMAN"),
("3A4", "000130950", "QUININE", "SUBSTRATE", "HUMAN"),
("3A4", "000130950", "QUININE", "INHIBITOR", "HUMAN"),
("3A4", "000130950", "QUININE", "INDUCER", "HUMAN"),
("3A4", "126602899", "QUINUPRISTIN/DALFOPRISTIN", "INHIBITOR", "HUMAN"),
("3A4", "117976893", "RABEPRAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "117976893", "RABEPRAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "084449901", "RALOXIFENE", "INHIBITOR", "HUMAN"),
("3A4", "084449901", "RALOXIFENE", "SUBSTRATE", "HUMAN"),
("3A4", "066357355", "RANITIDINE", "INHIBITOR", "HUMAN"),
("3A4", "098769814", "REBOXETINE", "SUBSTRATE", "HUMAN"),
("3A4", "135062021", "REPAGLINIDE", "INHIBITOR", "HUMAN"),
("3A4", "135062021", "REPAGLINIDE", "SUBSTRATE", "HUMAN"),
("3A4", "000068268", "RETINOL(VITA)", "SUBSTRATE", "HUMAN"),
("3A4", "072559069", "RIFABUTIN", "INDUCER", "HUMAN"),
("3A4", "072559069", "RIFABUTIN", "SUBSTRATE", "HUMAN"),
("3A4", "013292461", "RIFAMPICIN", "SUBSTRATE", "HUMAN"),
("3A4", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("3A4", "080621814", "RIFAXIMIN", "INDUCER", "HUMAN"),
("3A4", "106266062", "RISPERIDONE", "SUBSTRATE", "HUMAN"),
("3A4", "106266062", "RISPERIDONE", "INHIBITOR", "HUMAN"),
("3A4", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("3A4", "155213675", "RITONAVIR", "INDUCER", "HUMAN"),
("3A4", "155213675", "RITONAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "123441032", "RIVASTIGMINE", "INHIBITOR", "HUMAN"),
("3A4", "162011907", "ROFECOXIB", "INDUCER", "HUMAN"),
("3A4", "074014510", "ROKITAMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "074014510", "ROKITAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "091374219", "ROPINIROLE", "SUBSTRATE", "HUMAN"),
("3A4", "084057954", "ROPIVACAINE", "SUBSTRATE", "HUMAN"),
("3A4", "084088426", "ROQUINIMEX", "SUBSTRATE", "HUMAN"),
("3A4", "287714414", "ROSUVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "287714414", "ROSUVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "080214831", "ROXITHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "080214831", "ROXITHROMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "156611766", "RUPATADINE", "SUBSTRATE", "HUMAN"),
("3A4", "000153184", "RUTOSIDE", "INHIBITOR", "HUMAN"),
("3A4", "018559949", "SALBUTAMOL", "INHIBITOR", "HUMAN"),
("3A4", "089365504", "SALMETEROL", "SUBSTRATE", "HUMAN"),
("3A4", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("3A4", "127779208", "SAQUINAVIR", "SUBSTRATE", "HUMAN"),
("3A4", "014611519", "SELEGILINE", "SUBSTRATE", ""),
("3A4", "112665437", "SERATRODAST", "INDUCER", "HUMAN"),
("3A4", "112665437", "SERATRODAST", "SUBSTRATE", "HUMAN"),
("3A4", "106516249", "SERTINDOLE", "SUBSTRATE", "HUMAN"),
("3A4", "079617962", "SERTRALINE", "SUBSTRATE", "HUMAN"),
("3A4", "079617962", "SERTRALINE", "INHIBITOR", "HUMAN"),
("3A4", "028523866", "SEVOFLURANE", "SUBSTRATE", "HUMAN"),
("3A4", "106650560", "SIBUTRAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "139755832", "SILDENAFIL", "SUBSTRATE", "HUMAN"),
("3A4", "139755832", "SILDENAFIL", "INHIBITOR", "HUMAN"),
("3A4", "022888706", "SILYMARIN", "INHIBITOR", "HUMAN"),
("3A4", "022888706", "SILYMARIN", "INDUCER", "HUMAN"),
("3A4", "079902639", "SIMVASTATIN", "SUBSTRATE", "HUMAN"),
("3A4", "079902639", "SIMVASTATIN", "INHIBITOR", "HUMAN"),
("3A4", "053123889", "SIROLIMUS", "INHIBITOR", "HUMAN"),
("3A4", "053123889", "SIROLIMUS", "SUBSTRATE", "HUMAN"),
("3A4", "000064028", "SODIUMEDETATE", "SUBSTRATE", "HUMAN"),
("3A4", "000059961", "SOLIFENACIN", "SUBSTRATE", "HUMAN"),
("3A4", "051110011", "SOMATOSTATIN", "INHIBITOR", "HUMAN"),
("3A4", "008025818", "SPIRAMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "000052017", "SPIRONOLACTONE", "INDUCER", "RAT"),
("3A4", "056030547", "SUFENTANIL", "SUBSTRATE", "HUMAN"),
("3A4", "061318909", "SULCONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "000068359", "SULFADIAZINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057681", "SULFADIMIDINE", "INDUCER", "HUMAN"),
("3A4", "000723466", "SULFAMETHOXAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "000723466", "SULFAMETHOXAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "000063741", "SULFANILAMIDE", "INHIBITOR", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZON", "INDUCER", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZON", "INHIBITOR", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZON", "SUBSTRATE", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZONE", "INDUCER", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZONE", "INHIBITOR", "HUMAN"),
("3A4", "000057965", "SULFINPYRAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "109581933", "TACROLIMUS", "SUBSTRATE", "HUMAN"),
("3A4", "109581933", "TACROLIMUS", "INHIBITOR", "HUMAN"),
("3A4", "171596295", "TADALAFIL", "SUBSTRATE", "HUMAN"),
("3A4", "038649739", "TALINOLOL", "SUBSTRATE", ""),
("3A4", "010540291", "TAMOXIFEN", "INHIBITOR", "HUMAN"),
("3A4", "010540291", "TAMOXIFEN", "INDUCER", "HUMAN"),
("3A4", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("3A4", "106133204", "TAMSULOSIN", "SUBSTRATE", "HUMAN"),
("3A4", "145733364", "TASOSARTAN", "SUBSTRATE", "HUMAN"),
("3A4", "191114484", "TELITHROMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "191114484", "TELITHROMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "000846504", "TEMAZEPAM", "SUBSTRATE", "HUMAN"),
("3A4", "085622931", "TEMOZOLOMIDE", "INDUCER", "HUMAN"),
("3A4", "029767202", "TENIPOSIDE", "SUBSTRATE", "HUMAN"),
("3A4", "029767202", "TENIPOSIDE", "INHIBITOR", "HUMAN"),
("3A4", "091161716", "TERBINAFINE", "SUBSTRATE", "HUMAN"),
("3A4", "091161716", "TERBINAFINE", "INDUCER", "HUMAN"),
("3A4", "050679088", "TERFENADINE", "INHIBITOR", "HUMAN"),
("3A4", "050679088", "TERFENADINE", "INDUCER", "HUMAN"),
("3A4", "050679088", "TERFENADINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("3A4", "000057852", "TESTOSTERONE", "INHIBITOR", "HUMAN"),
("3A4", "000057852", "TESTOSTERONE", "INDUCER", "HUMAN"),
("3A4", "000060548", "TETRACYCLIN", "INHIBITOR", ""),
("3A4", "000060548", "TETRACYCLIN", "SUBSTRATE", "HUMAN"),
("3A4", "000060548", "TETRACYCLINE", "INHIBITOR", ""),
("3A4", "000060548", "TETRACYCLINE", "SUBSTRATE", "HUMAN"),
("3A4", "000058559", "THEOPHYLLINE", "SUBSTRATE", "HUMAN"),
("3A4", "000060560", "THIAMAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "000076755", "THIOPENTAL", "INHIBITOR", "HUMAN"),
("3A4", "000052244", "THIOTEPA", "SUBSTRATE", "HUMAN"),
("3A4", "115103543", "TIAGABINE", "SUBSTRATE", "HUMAN"),
("3A4", "005630535", "TIBOLONE", "INHIBITOR", "HUMAN"),
("3A4", "055142853", "TICLOPIDINE", "SUBSTRATE", "HUMAN"),
("3A4", "019387918", "TINIDAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "065899732", "TIOCONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "136310935", "TIOTROPIUMBROMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "110101661", "TIRILAZAD", "SUBSTRATE", "HUMAN"),
("3A4", "001406662", "TOCOPHEROL(VITE)", "SUBSTRATE", ""),
("3A4", "001406662", "TOCOPHEROL(VITE)", "INDUCER", ""),
("3A4", "022345477", "TOFISOPAM", "INHIBITOR", "HUMAN"),
("3A4", "124937515", "TOLTERODINE", "SUBSTRATE", "HUMAN"),
("3A4", "097240794", "TOPIRAMATE", "INDUCER", "HUMAN"),
("3A4", "123948878", "TOPOTECAN", "INHIBITOR", "HUMAN"),
("3A4", "123948878", "TOPOTECAN", "INDUCER", "HUMAN"),
("3A4", "089778267", "TOREMIFENE", "SUBSTRATE", "HUMAN"),
("3A4", "114899773", "TRABECTEDIN", "SUBSTRATE", "HUMAN"),
("3A4", "027203925", "TRAMADOL", "INHIBITOR", "HUMAN"),
("3A4", "027203925", "TRAMADOL", "SUBSTRATE", "HUMAN"),
("3A4", "000155099", "TRANYLCYPROMINE", "INHIBITOR", "HUMAN"),
("3A4", "019794935", "TRAZODONE", "SUBSTRATE", "HUMAN"),
("3A4", "000299752", "TREOSULFAN", "INHIBITOR", "HUMAN"),
("3A4", "028911015", "TRIAZOLAM", "SUBSTRATE", "HUMAN"),
("3A4", "000079016", "TRICHLOROETHYLENE", "SUBSTRATE", "HUMAN"),
("3A4", "000127480", "TRIMETHADIONE", "SUBSTRATE", "HUMAN"),
("3A4", "000738705", "TRIMETHOPRIM", "SUBSTRATE", "HUMAN"),
("3A4", "000739719", "TRIMIPRAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "022089221", "TROFOSFAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "097322877", "TROGLITAZONE", "SUBSTRATE", "HUMAN"),
("3A4", "097322877", "TROGLITAZONE", "INHIBITOR", "HUMAN"),
("3A4", "097322877", "TROGLITAZONE", "INDUCER", "HUMAN"),
("3A4", "002751099", "TROLEANDOMYCIN", "SUBSTRATE", "HUMAN"),
("3A4", "002751099", "TROLEANDOMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "089565684", "TROPISETRON", "SUBSTRATE", "HUMAN"),
("3A4", "010405024", "TROSPIUM", "INHIBITOR", ""),
("3A4", "181695727", "VALDECOXIB", "SUBSTRATE", "HUMAN"),
("3A4", "000099661", "VALPROICACID", "INHIBITOR", "HUMAN"),
("3A4", "224785904", "VARDENAFIL", "SUBSTRATE", "HUMAN"),
("3A4", "093413695", "VENLAFAXINE", "SUBSTRATE", "HUMAN"),
("3A4", "093413695", "VENLAFAXINE", "INHIBITOR", "HUMAN"),
("3A4", "000052539", "VERAPAMIL", "SUBSTRATE", "HUMAN"),
("3A4", "000052539", "VERAPAMIL", "INHIBITOR", "HUMAN"),
("3A4", "000865214", "VINBLASTINE", "SUBSTRATE", "HUMAN"),
("3A4", "000865214", "VINBLASTINE", "INHIBITOR", "HUMAN"),
("3A4", "001617909", "VINCAMIN", "SUBSTRATE", "HUMAN"),
("3A4", "001617909", "VINCAMINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057227", "VINCRISTINE", "SUBSTRATE", "HUMAN"),
("3A4", "000057227", "VINCRISTINE", "INHIBITOR", "HUMAN"),
("3A4", "053643484", "VINDESINE", "SUBSTRATE", "HUMAN"),
("3A4", "071486221", "VINORELBINE", "SUBSTRATE", ""),
("3A4", "071486221", "VINORELBINE", "INHIBITOR", "HUMAN"),
("3A4", "011006761", "VIRGINIAMYCIN", "INDUCER", "HUMAN"),
("3A4", "011006761", "VIRGINIAMYCIN", "INHIBITOR", "HUMAN"),
("3A4", "137234629", "VORICONAZOLE", "SUBSTRATE", "HUMAN"),
("3A4", "137234629", "VORICONAZOLE", "INHIBITOR", "HUMAN"),
("3A4", "000081812", "WARFARIN", "SUBSTRATE", "HUMAN"),
("3A4", "000146485", "YOHIMBIN", "SUBSTRATE", "HUMAN"),
("3A4", "107753786", "ZAFIRLUKAST", "INHIBITOR", "HUMAN"),
("3A4", "007481892", "ZALCITABINE", "SUBSTRATE", "HUMAN"),
("3A4", "151319345", "ZALEPLON", "SUBSTRATE", "HUMAN"),
("3A4", "030516871", "ZIDOVUDINE", "SUBSTRATE", "HUMAN"),
("3A4", "146939277", "ZIPRASIDONE", "INHIBITOR", "HUMAN"),
("3A4", "146939277", "ZIPRASIDONE", "SUBSTRATE", "HUMAN"),
("3A4", "033369312", "ZOMEPIRAC", "SUBSTRATE", "HUMAN"),
("3A4", "068291974", "ZONISAMIDE", "SUBSTRATE", "HUMAN"),
("3A4", "043200802", "ZOPICLONE", "SUBSTRATE", "HUMAN"),
("3A4", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("3A4", "061379655", "RIFAPENTINE", "INDUCER", "HUMAN"),
("3A5", "071195589", "ALFENTANIL", "SUBSTRATE", "HUMAN"),
("3A5", "028981977", "ALPRAZOLAM", "SUBSTRATE", "HUMAN"),
("3A5", "001951253", "AMIODARONE", "INHIBITOR", "HUMAN"),
("3A5", "088150429", "AMLODIPINE", "SUBSTRATE", ""),
("3A5", "161814499", "AMPRENAVIR", "SUBSTRATE", "HUMAN"),
("3A5", "170729803", "APREPITANT", "SUBSTRATE", ""),
("3A5", "074863846", "ARGATROBAN", "SUBSTRATE", "HUMAN"),
("3A5", "129722129", "ARIPIPRAZOLE", "SUBSTRATE", ""),
("3A5", "068844779", "ASTEMIZOLE", "SUBSTRATE", ""),
("3A5", "134523005", "ATORVASTATIN", "SUBSTRATE", "HUMAN"),
("3A5", "078110380", "AZTREONAM", "SUBSTRATE", "MONKEY"),
("3A5", "004419390", "BECLOMETASONE", "INDUCER", "HUMAN"),
("3A5", "036505847", "BUSPIRONE", "SUBSTRATE", ""),
("3A5", "000058082", "CAFFEINE", "SUBSTRATE", ""),
("3A5", "000298464", "CARBAMAZEPINE", "INDUCER", "HUMAN"),
("3A5", "145599866", "CERIVASTATIN", "SUBSTRATE", ""),
("3A5", "000130950", "CHININ", "SUBSTRATE", ""),
("3A5", "000054057", "CHLOROQUINE", "SUBSTRATE", "HUMAN"),
("3A5", "000132229", "CHLORPHENAMINE", "SUBSTRATE", ""),
("3A5", "059865133", "CICLOSPORIN", "SUBSTRATE", ""),
("3A5", "059865133", "CICLOSPORIN", "INDUCER", "HUMAN"),
("3A5", "051481619", "CIMETIDINE", "INHIBITOR", "HUMAN"),
("3A5", "081098604", "CISAPRIDE", "SUBSTRATE", "HUMAN"),
("3A5", "081103119", "CLARITHROMYCIN", "SUBSTRATE", ""),
("3A5", "113665842", "CLOPIDOGREL", "SUBSTRATE", "HUMAN"),
("3A5", "000050362", "COCAINE", "SUBSTRATE", ""),
("3A5", "000076573", "CODEINE", "SUBSTRATE", ""),
("3A5", "000052313", "CYCLOBARBITAL", "INDUCER", ""),
("3A5", "000080080", "DAPSONE", "SUBSTRATE", ""),
("3A5", "000050022", "DEXAMETHASON", "SUBSTRATE", ""),
("3A5", "000050022", "DEXAMETHASON", "INDUCER", "HUMAN"),
("3A5", "000050022", "DEXAMETHASONE", "SUBSTRATE", ""),
("3A5", "000050022", "DEXAMETHASONE", "INDUCER", "HUMAN"),
("3A5", "000125713", "DEXTROMETHORPHAN", "SUBSTRATE", "HUMAN"),
("3A5", "000439145", "DIAZEPAM", "SUBSTRATE", "HUMAN"),
("3A5", "000134623", "DIETHYLTOLUAMIDE", "SUBSTRATE", "HUMAN"),
("3A5", "042399417", "DILTIAZEM", "SUBSTRATE", ""),
("3A5", "042399417", "DILTIAZEM", "INHIBITOR", "HUMAN"),
("3A5", "000097778", "DISULFIRAM", "SUBSTRATE", "HUMAN"),
("3A5", "114977285", "DOCETAXEL", "SUBSTRATE", ""),
("3A5", "057808669", "DOMPERIDONE", "SUBSTRATE", ""),
("3A5", "164656239", "DUTASTERIDE", "SUBSTRATE", "HUMAN"),
("3A5", "107724209", "EPLERENONE", "SUBSTRATE", ""),
("3A5", "000050282", "ESTRADIOL", "SUBSTRATE", ""),
("3A5", "000053167", "ESTRONE", "SUBSTRATE", "HUMAN"),
("3A5", "000057636", "ETHINYLESTRADIOL", "SUBSTRATE", "HUMAN"),
("3A5", "000077678", "ETHOSUXIMIDE", "SUBSTRATE", "HUMAN"),
("3A5", "033419420", "ETOPOSIDE", "INDUCER", "HUMAN"),
("3A5", "033419420", "ETOPOSIDE", "SUBSTRATE", "HUMAN"),
("3A5", "072509763", "FELODIPINE", "SUBSTRATE", ""),
("3A5", "000437387", "FENTANYL", "SUBSTRATE", "HUMAN"),
("3A5", "098319267", "FINASTERIDE", "SUBSTRATE", ""),
("3A5", "013311847", "FLUTAMIDE", "SUBSTRATE", "HUMAN"),
("3A5", "054739183", "FLUVOXAMINE", "INHIBITOR", "HUMAN"),
("3A5", "109889090", "GRANISETRON", "SUBSTRATE", "HUMAN"),
("3A5", "069756532", "HALOFANTRINE", "SUBSTRATE", "HUMAN"),
("3A5", "000052868", "HALOPERIDOL", "SUBSTRATE", "HUMAN"),
("3A5", "000050237", "HYDROCORTISONE", "SUBSTRATE", ""),
("3A5", "152459955", "IMATINIB", "INHIBITOR", "HUMAN"),
("3A5", "152459955", "IMATINIB", "SUBSTRATE", "HUMAN"),
("3A5", "150378179", "INDINAVIR", "SUBSTRATE", "HUMAN"),
("3A5", "150378179", "INDINAVIR", "INHIBITOR", "HUMAN"),
("3A5", "097682445", "IRINOTECAN", "SUBSTRATE", "HUMAN"),
("3A5", "065277421", "KETOCONAZOLE", "INHIBITOR", "HUMAN"),
("3A5", "100427267", "LERCANIDIPINE", "SUBSTRATE", ""),
("3A5", "001477403", "LEVACETYLMETHADOL", "SUBSTRATE", ""),
("3A5", "000137586", "LIDOCAIN", "SUBSTRATE", ""),
("3A5", "000137586", "LIDOCAINE", "SUBSTRATE", ""),
("3A5", "114798264", "LOSARTAN", "SUBSTRATE", "HUMAN"),
("3A5", "075330755", "LOVASTATIN", "SUBSTRATE", ""),
("3A5", "000083896", "MEPACRINE", "SUBSTRATE", "HUMAN"),
("3A5", "000076993", "METHADONE", "SUBSTRATE", ""),
("3A5", "116644532", "MIBEFRADIL", "INHIBITOR", "HUMAN"),
("3A5", "059467708", "MIDAZOLAM", "SUBSTRATE", "HUMAN"),
("3A5", "084371653", "MIFEPRISTONE", "SUBSTRATE", "HUMAN"),
("3A5", "084371653", "MIFEPRISTONE", "INHIBITOR", "HUMAN"),
("3A5", "068693118", "MODAFINIL", "INHIBITOR", "HUMAN"),
("3A5", "068693118", "MODAFINIL", "INDUCER", "HUMAN"),
("3A5", "105816044", "NATEGLINIDE", "SUBSTRATE", ""),
("3A5", "083366669", "NEFAZODONE", "INHIBITOR", "HUMAN"),
("3A5", "159989647", "NELFINAVIR", "SUBSTRATE", ""),
("3A5", "159989647", "NELFINAVIR", "INHIBITOR", "HUMAN"),
("3A5", "055985325", "NICARDIPINE", "INHIBITOR", "HUMAN"),
("3A5", "021829254", "NIFEDIPINE", "SUBSTRATE", "HUMAN"),
("3A5", "066085594", "NIMODIPIN", "SUBSTRATE", "HUMAN"),
("3A5", "066085594", "NIMODIPINE", "SUBSTRATE", "HUMAN"),
("3A5", "063675729", "NISOLDIPINE", "SUBSTRATE", ""),
("3A5", "039562704", "NITRENDIPINE", "SUBSTRATE", ""),
("3A5", "000068224", "NORETHISTERONE", "SUBSTRATE", "HUMAN"),
("3A5", "070458967", "NORFLOXACIN", "INHIBITOR", "HUMAN"),
("3A5", "000104143", "OCTOPAMINE", "SUBSTRATE", "HUMAN"),
("3A5", "099614025", "ONDANSETRON", "SUBSTRATE", ""),
("3A5", "000604751", "OXAZEPAM", "SUBSTRATE", "HUMAN"),
("3A5", "028721075", "OXCARBAZEPINE", "INDUCER", "HUMAN"),
("3A5", "005633205", "OXYBUTYNIN", "SUBSTRATE", "HUMAN"),
("3A5", "000076426", "OXYCODONE", "SUBSTRATE", "HUMAN"),
("3A5", "033069624", "PACLITAXEL", "SUBSTRATE", ""),
("3A5", "000311455", "PARAOXON", "SUBSTRATE", "HUMAN"),
("3A5", "000051718", "PHENELZINE", "INHIBITOR", "HUMAN"),
("3A5", "000050066", "PHENOBARBITAL", "INDUCER", "HUMAN"),
("3A5", "000057410", "PHENYTOIN", "INDUCER", "HUMAN"),
("3A5", "000057476", "PHYSOSTIGMINE", "INHIBITOR", "RAT"),
("3A5", "002062784", "PIMOZIDE", "SUBSTRATE", ""),
("3A5", "081093370", "PRAVASTATIN", "SUBSTRATE", "HUMAN"),
("3A5", "055268741", "PRAZIQUANTEL", "SUBSTRATE", "HUMAN"),
("3A5", "000057830", "PROGESTERONE", "SUBSTRATE", "HUMAN"),
("3A5", "000525666", "PROPRANOLOL", "SUBSTRATE", "HUMAN"),
("3A5", "111974697", "QUETIAPINE", "SUBSTRATE", ""),
("3A5", "000130950", "QUININE", "SUBSTRATE", ""),
("3A5", "066357355", "RANITIDINE", "INHIBITOR", "HUMAN"),
("3A5", "000050555", "RESERPIN", "INDUCER", "HUMAN"),
("3A5", "000050555", "RESERPINE", "INDUCER", "HUMAN"),
("3A5", "013292461", "RIFAMPICIN", "INDUCER", "HUMAN"),
("3A5", "106266062", "RISPERIDONE", "SUBSTRATE", "HUMAN"),
("3A5", "155213675", "RITONAVIR", "SUBSTRATE", ""),
("3A5", "155213675", "RITONAVIR", "INHIBITOR", "HUMAN"),
("3A5", "287714414", "ROSUVASTATIN", "INHIBITOR", "HUMAN"),
("3A5", "089365504", "SALMETEROL", "SUBSTRATE", ""),
("3A5", "127779208", "SAQUINAVIR", "SUBSTRATE", ""),
("3A5", "127779208", "SAQUINAVIR", "INHIBITOR", "HUMAN"),
("3A5", "139755832", "SILDENAFIL", "SUBSTRATE", ""),
("3A5", "079902639", "SIMVASTATIN", "SUBSTRATE", "HUMAN"),
("3A5", "053123889", "SIROLIMUS", "SUBSTRATE", ""),
("3A5", "000052017", "SPIRONOLACTONE", "INDUCER", "RAT"),
("3A5", "000599791", "SULFASALAZIN", "SUBSTRATE", "HUMAN"),
("3A5", "000599791", "SULFASALAZINE", "SUBSTRATE", "HUMAN"),
("3A5", "109581933", "TACROLIMUS", "SUBSTRATE", "HUMAN"),
("3A5", "010540291", "TAMOXIFEN", "SUBSTRATE", "HUMAN"),
("3A5", "017902237", "TEGAFUR", "SUBSTRATE", "HUMAN"),
("3A5", "191114484", "TELITHROMYCIN", "SUBSTRATE", ""),
("3A5", "029767202", "TENIPOSIDE", "SUBSTRATE", "HUMAN"),
("3A5", "000057852", "TESTOSTERONE", "SUBSTRATE", "HUMAN"),
("3A5", "001406662", "TOCOPHEROL(VITE)", "INDUCER", ""),
("3A5", "019794935", "TRAZODONE", "SUBSTRATE", ""),
("3A5", "028911015", "TRIAZOLAM", "SUBSTRATE", "HUMAN"),
("3A5", "097322877", "TROGLITAZONE", "INHIBITOR", "HUMAN"),
("3A5", "097322877", "TROGLITAZONE", "INDUCER", "HUMAN"),
("3A5", "224785904", "VARDENAFIL", "SUBSTRATE", "HUMAN"),
("3A5", "000052539", "VERAPAMIL", "SUBSTRATE", ""),
("3A5", "000052539", "VERAPAMIL", "INHIBITOR", "HUMAN"),
("3A5", "000057227", "VINCRISTINE", "SUBSTRATE", "HUMAN"),
("3A5", "007481892", "ZALCITABINE", "SUBSTRATE", "HUMAN"),
("3A5", "151319345", "ZALEPLON", "SUBSTRATE", ""),
("3A5", "146939277", "ZIPRASIDONE", "SUBSTRATE", ""),
("3A5", "082626480", "ZOLPIDEM", "SUBSTRATE", ""),
("3A5", "068291974", "ZONISAMIDE", "SUBSTRATE", ""),
("3A5", "026615214", "ZOTEPINE", "SUBSTRATE", "HUMAN"),
("3A5", "061379655", "RIFAPENTINE", "INDUCER", "HUMAN")]

sypercyp_substr_l = ["%s	CYP%s" % (y[2], y[0]) for y in  filter(lambda x: x[3] == "SUBSTRATE" and x[4] == "HUMAN", supercyp_l)]

sypercyp_inhibits_l = ["%s	CYP%s" % (y[2], y[0]) for y in  filter(lambda x: x[3] == "INHIBITOR" and x[4] == "HUMAN", supercyp_l)]

for asrt in substrate_l:
    if asrt in sypercyp_substr_l:
        print "Y"
    else:
        print "X"


for asrt in inhibits_l:
    if asrt in sypercyp_inhibits_l:
        print "Y"
    else:
        print "X"

### the following lines were for the search for the is-not-substrate-of assertions 
# >>> filter(lambda x: x[0] == "1A2" and x[2] == "ALPRAZOLAM" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "1A2" and x[2] == "ARIPIPRAZOLE" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "3A4" and x[2] == "CITALOPRAM" and x[3] == "SUBSTRATE", supercyp_l)
# [('3A4', '059729338', 'CITALOPRAM', 'SUBSTRATE', 'HUMAN')]
# >>> filter(lambda x: x[0] == "1A2" and x[2] == "CLARITHROMYCIN" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "2C9" and x[2] == "CLARITHROMYCIN" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "2D6" and x[2] == "CLARITHROMYCIN" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "2D6" and x[2] == "DESVENLAFAXINE" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> filter(lambda x: x[0] == "3A4" and x[2] == "ROSUVASTATIN" and x[3] == "SUBSTRATE", supercyp_l)
# [('3A4', '287714414', 'ROSUVASTATIN', 'SUBSTRATE', 'HUMAN')]
# >>> filter(lambda x: x[0] == "2D6" and x[2] == "ZALEPLON" and x[3] == "SUBSTRATE", supercyp_l)
# []
# >>> 

### the following lines were for the search for the does-not-inhibit assertions 
does_not_inhibit_l = ["N-DESALKYLQUETIAPINE	CYP3A4", "ARIPIPRAZOLE	CYP2D6", "ATOMOXETINE	CYP1A2", "ATORVASTATIN	CYP2C8", "BETA-HYDROXY-LOVASTATIN	CYP2C8", "BETA-HYDROXY-SIMVASTATIN	CYP3A4", "CELECOXIB	CYP2C9", "CHLORPROMAZINE	CYP2C19", "CINACALCET	CYP2C19", "CITALOPRAM	CYP2C9", "CLOZAPINE	CYP2D6", "CLOZAPINE	CYP2C19", "DEHYDRO-ARIPIPRAZOLE	CYP1A2", "DEMETHYLCITALOPRAM	CYP3A4", "DULOXETINE	CYP2C19", "ESCITALOPRAM	CYP2C19", "ESZOPICLONE	CYP2E1", "FLUPHENAZINE	CYP2C19", "FLUPHENAZINE	CYP2D6", "FLUPHENAZINE	CYP1A2", "FLUVASTATIN	CYP2C8", "HALOPERIDOL	CYP2C19", "LANSOPRAZOLE	CYP2D6", "LOVASTATIN	CYP2C8", "OMEPRAZOLE	CYP2D6", "PALIPERIDONE	CYP3A4", "PANTOPRAZOLE	CYP2D6", "PERPHENAZINE	CYP2D6", "PERPHENAZINE	CYP1A2", "PERPHENAZINE	CYP2C19", "PRAVASTATIN	CYP2C8", "QUETIAPINE	CYP3A4", "R-CITALOPRAM	CYP1A2", "R-DEMETHYLCITALOPRAM	CYP2C19", "R-DIDEMETHYLCITALOPRAM	CYP1A2", "RISPERIDONE	CYP2C19", "RISPERIDONE	CYP2D6", "ROSUVASTATIN	CYP2C8", "S-DEMETHYLCITALOPRAM	CYP2C9", "S-DIDEMETHYLCITALOPRAM	CYP2D6", "SIMVASTATIN	CYP3A4", "THIORIDAZINE	CYP2C19", "THIOTHIXENE	CYP2C19", "TOPIRAMATE	CYP2B6", "VENLAFAXINE	CYP2C9", "ZIPRASIDONE	CYP2D6"]

sypercyp_inhibits_l = ["%s	CYP%s" % (y[2], y[0]) for y in  filter(lambda x: x[3] == "INHIBITOR" and x[4] == "HUMAN", supercyp_l)]

for asrt in does_not_inhibit_l:
    if asrt in sypercyp_inhibits_l:
        print "N"
    else:
        print "X"


################################################################################ 
### ensure that assumptions are concordant -- this is to fix a bug
### that was introduced into the evidence-base the last time I synced
### evidence-for and against (02132010)
timestamp = "05242010"
tpl_l = [("substrate_of", "evidence_against", "is_not_substrate_of", "evidence_for"), 
         ("substrate_of", "evidence_for", "is_not_substrate_of", "evidence_against"),
         ("is_not_substrate_of", "evidence_against", "substrate_of", "evidence_for"),
         ("is_not_substrate_of", "evidence_for", "substrate_of", "evidence_against"),
         ("inhibits", "evidence_against", "does_not_inhibit", "evidence_for"), 
         ("inhibits", "evidence_for", "does_not_inhibit", "evidence_against"),
         ("does_not_inhibit", "evidence_against", "inhibits", "evidence_for"),
         ("does_not_inhibit", "evidence_for", "inhibits", "evidence_against")]
for tpl in tpl_l:
	for k,v in dikb.objects.iteritems():
            print "Processing DIKB object '%s'" % k

	    if not (type(v) in ([Pceut_Entity] + Pceut_Entity().__class__.__subclasses__())):
	        print "\n\npassing on %s" % k
	        continue 
	
            # iterate through all relevant assertions; there should be
            # only one for each enzyme
	    for asrt in v.__dict__[tpl[0]].evidence:
	        ev_a_ids = [x.doc_pointer for x in asrt.__dict__[tpl[1]]]
                ev_a_quotes = [x.quote for x in asrt.__dict__[tpl[1]]]

	        if len(ev_a_ids) == 0:
	            print "\n\nNo %s for %s; going on to the next assertion." % (tpl[1].upper(), asrt._name)
	            continue
	
	        casrt = None
                # look for matching 'value'(enzyme)
	        for casrt in v.__dict__[tpl[2]].evidence:
	            if casrt.value == asrt.value:

                        # iterate through evidence items in this
                        # assertion comparing each assumption list for
                        # with the corresponding evidence item in the
                        # assertion's complement
                        x_idx = -1
	                for x in casrt.__dict__[tpl[3]]:                            
                            x_idx += 1

                            if ev_a_ids.count(x.doc_pointer) > 1 and ev_a_quotes.count(x.quote) > 1:
                                print "WARNING:  MULTIPLE EVIDENCE ITEMS HAVE THE SAME DOC POINTER AND QUOTES - TOO AMBIGUOUS"
                                print ":\n\tassertion: %s\n\tcomplement: %s\n\tassertion complement evidence doc pointer: %s\n\tquote: %s" % (asrt._name, casrt._name,  x.doc_pointer, x.quote)
                                break

                            cntr = 0
                            while cntr < len(ev_a_ids) and not (ev_a_ids[cntr] == x.doc_pointer and ev_a_quotes[cntr] == x.quote):
                                print "incrementing counter from %s to %s (%s / %s)" % (cntr, cntr + 1, asrt._name, casrt._name)
                                cntr += 1
                            
                            if cntr == len(ev_a_ids):
                                print "WARNING:  MULTIPLE EVIDENCE ITEMS HAVE THE SAME DOC POINTER BUT COULD NOT MATCH QUOTES - TOO AMBIGUOUS"
                                print ":\n\tassertion: %s\n\tcomplement: %s\n\tassertion complement evidence doc pointer: %s\n\tquote: %s\n\tcounter: %s" % (asrt._name, casrt._name,  x.doc_pointer, x.quote, cntr)
                                break        
                                
                            if asrt.__dict__[tpl[1]][cntr].assumptions.value != x.assumptions.value:
                                print "\n\n\nASSUMPTION LIST MISMATCH FOUND:\n\tassertion: %s\n\tcomplement: %s\n\tassertion evidence doc pointer: %s\n\tassertion complement evidence doc pointer: %s\n\tassertion evidence quote: %s\n\tcomplement assertion evidence quote: %s\n\tassertion assumptions: %s\n\tassertion complement assumptions: %s" % (asrt._name, casrt._name, asrt.__dict__[tpl[1]][cntr].doc_pointer, x.doc_pointer, asrt.__dict__[tpl[1]][cntr].quote, x.quote, asrt.__dict__[tpl[1]][cntr].assumptions.value, x.assumptions.value)
                                print "Applying solution of assigning the following list to both assumption lists: %s" % [k for k in set(asrt.__dict__[tpl[1]][cntr].assumptions.value + x.assumptions.value)]
                                n_asmpts = [k for k in set(asrt.__dict__[tpl[1]][cntr].assumptions.value + x.assumptions.value)]
                                ev.objects[asrt._name].__dict__[tpl[1]][cntr].assumptions.value = n_asmpts
                                ev.objects[casrt._name].__dict__[tpl[3]][x_idx].assumptions.value = n_asmpts





############ LABELING AUC VS PRIMARY LITERATURE AUC ANALYSIS  ################################################

# How many AUC studies are in the DIKB that are based on data from the
# product label?
for e,v in ev.objects.iteritems():
    if v.slot == "increases_auc":
        for evid in v.evidence_for:
            if evid.evidence_type.value == "Non_traceable_Drug_Label_Statement":
                #print "evidence FOR %s: %s \n\t%s" % (v._name, evid.doc_pointer, evid.quote)
                print "FOR	%s	%s	%s	%s" % (v.value.upper(), v.object.upper(), "", evid.doc_pointer)

        for evid in v.evidence_against:
            if evid.evidence_type.value == "Non_traceable_Drug_Label_Statement":
                #print "evidence AGAINST %s: %s \n\t%s" % (v._name, evid.doc_pointer, evid.quote)
                print "AGAINST	%s	%s	%s	%s" % (v.value.upper(), v.object.upper(), "", evid.doc_pointer)

# results on 06022010
# AGAINST	ERYTHROMYCIN	RISPERIDONE		risperidone-janssen-032007
# AGAINST	FLUVASTATIN	ERYTHROMYCIN		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=3237
# AGAINST	FLUVASTATIN	ITRACONAZOLE		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=3237
# AGAINST	NEFAZODONE	TRIAZOLAM		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=2640
# AGAINST	RISPERIDONE	ERYTHROMYCIN		risperidone-janssen-032007
# FOR	ALPRAZOLAM	NEFAZODONE		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=2640
# FOR	ERYTHROHYDROBUPROPION	CIMETIDINE		bupropion-XR-actavis-south-atlantic-032008
# FOR	HALOPERIDOL	VENLAFAXINE		venlafaxine-wyeth-122008
# FOR	MIDAZOLAM	FLUCONAZOLE		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=2346
# FOR	O-DESMETHYLVENLAFAXINE	KETOCONAZOLE		venlafaxine-wyeth-122008
# FOR	RISPERIDONE	PAROXETINE		paroxetine-apotex-082007
# FOR	THIORIDAZINE	FLUVOXAMINE		thioridazine-mylan-012007
# FOR	THREOHYDROBUPROPION	CIMETIDINE		bupropion-XR-actavis-south-atlantic-032008
# FOR	TRIAZOLAM	NEFAZODONE		http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?id=2640
# FOR	VENLAFAXINE	KETOCONAZOLE		venlafaxine-wyeth-122008

# RESULTS ON 06/07/2010
ev_type_l = ["Non_traceable_Drug_Label_Statement"]
for e,v in ev.objects.iteritems():
    for evid in v.evidence_for:
        if evid.evidence_type.value in ev_type_l and evid.assumptions.value != []:
            if v.slot in ["substrate_of", "primary_total_clearance_enzyme", "primary_metabolic_clearance_enzyme"]:
                print "FOR	%s	%s	%s	%s" % (v.object.upper(), evid.assumptions.value[0].split("_")[0].upper(), v.value.upper(), evid.doc_pointer)
            if v.slot in ["is_not_substrate_of"]:
                print "AGAINST	%s	%s	%s	%s" % (v.object.upper(), evid.assumptions.value[0].split("_")[0].upper(), v.value.upper(), evid.doc_pointer)
            elif v.slot in ["inhibits"]:
                print "FOR	%s	%s	%s	%s" % (evid.assumptions.value[0].split("_")[0].upper(), v.object.upper(), v.value.upper(), evid.doc_pointer)
            elif v.slot in ["does-not-inhibit"]:
                print "AGAINST	%s	%s	%s	%s" % (evid.assumptions.value[0].split("_")[0].upper(), v.object.upper(), v.value.upper(), evid.doc_pointer)

# AGAINST	ASENAPINE	PAROXETINE	CYP2D6	asenapine-organon-082009
# AGAINST	CITALOPRAM	KETOCONAZOLE	CYP3A4	citalopram-teva-102008
# AGAINST	ZALEPLON	PAROXETINE	CYP2D6	zaleplon-teva-062008
# FOR	CAFFEINE	MEXILETINE	CYP1A2	mexiletine-watson-042008
# FOR	CINACALCET	KETOCONAZOLE	CYP3A4	cinacalcet-amgen-122008
# FOR	DESIPRAMINE	BUPROPION	CYP2D6	bupropion-XR-actavis-south-atlantic-032008
# FOR	DESIPRAMINE	CINACALCET	CYP2D6	cinacalcet-amgen-122008
# FOR	DESIPRAMINE	DULOXETINE	CYP2D6	duloxetine-eli-lilly-022009
# FOR	DESIPRAMINE	ESCITALOPRAM	CYP2D6	escitalopram-forest-laboratories-032009
# FOR	DESIPRAMINE	RITONAVIR	CYP2D6	ritonavir-abbot-092008
# FOR	DEXTROMETHORPHAN	ILOPERIDONE	CYP2D6	iloperidone-vanda-2009
# FOR	DULOXETINE	PAROXETINE	CYP2D6	duloxetine-eli-lilly-022009
# FOR	ESZOPICLONE	KETOCONAZOLE	CYP3A4	eszoplicone-sepracor-052008
# FOR	ILOPERIDONE	FLUOXETINE	CYP2D6	iloperidone-vanda-2009
# FOR	ILOPERIDONE	KETOCONAZOLE	CYP3A4	iloperidone-vanda-2009
# FOR	ILOPERIDONE	PAROXETINE	CYP2D6	iloperidone-vanda-2009
# FOR	MIDAZOLAM	TELITHROMYCIN	CYP3A4	telithromycin-Sanofi-Aventis-052009
# FOR	OLANZAPINE	FLUOXETINE	CYP2D6	olanzapine-eli-lilly-042009
# FOR	RABEPRAZOLE	CLARITHROMYCIN	CYP3A4	rabeprazole-eisai-022009
# FOR	RANOLAZINE	KETOCONAZOLE	CYP3A4	ranolazine-cv-therapeutics-042009
# FOR	RANOLAZINE	PAROXETINE	CYP2D6	ranolazine-cv-therapeutics-042009
# FOR	S-WARFARIN	ZAFIRLUKAST	CYP2C9	zafirlukast-astrazeneca-012008
# FOR	SILDENAFIL	INDINAVIR	CYP3A4	indinavir-merck-112008
# FOR	SILDENAFIL	RITONAVIR	CYP3A4	ritonavir-abbot-092008
# FOR	THEOPHYLLINE	FLUVOXAMINE	CYP1A2	fluvoxamine-mylan-092007
# FOR	THEOPHYLLINE	MEXILETINE	CYP1A2	mexiletine-watson-042008
# FOR	TRIAZOLAM	NEFAZODONE	CYP3A4	nefazodone-ranbaxy-122008
# FOR	WARFARIN	FLUVOXAMINE	CYP2C9	fluvoxamine-mylan-092007
# FOR	ZOLPIDEM	ITRACONAZOLE	CYP3A4	zolpidem-meda-072009
# FOR	ZOLPIDEM	KETOCONAZOLE	CYP3A4	zolpidem-meda-072009


# How many PK studies in the DIKB could be used to support or refute
# an increases AUC assertion?
ev_type_l = ["EV_CT_Pharmacokinetic", "EV_PK_DDI_NR", "EV_PK_DDI_Par_Grps", "EV_PK_DDI_RCT"]
for e,v in ev.objects.iteritems():
    for evid in v.evidence_for:
        if evid.evidence_type.value in ev_type_l :
            if v.slot in ["substrate_of", "primary_total_clearance_enzyme", "primary_metabolic_clearance_enzyme"]:
                print "FOR	%s	%s	%s	%s" % (v.object.upper(), evid.assumptions.value[0].split("_")[0].upper(), v.value.upper(), evid.doc_pointer)
            if v.slot in ["is_not_substrate_of"]:
                print "AGAINST	%s	%s	%s	%s" % (v.object.upper(), evid.assumptions.value[0].split("_")[0].upper(), v.value.upper(), evid.doc_pointer)
            elif v.slot in ["inhibits"]:
                print "FOR	%s	%s	%s	%s" % (evid.assumptions.value[0].split("_")[0].upper(), v.object.upper(), v.value.upper(), evid.doc_pointer)
            elif v.slot in ["does-not-inhibit"]:
                print "AGAINST	%s	%s	%s	%s" % (evid.assumptions.value[0].split("_")[0].upper(), v.object.upper(), v.value.upper(), evid.doc_pointer)

## RESULTS ON 06.07.2010
# AGAINST	CLOZAPINE-N-OXIDE	PAROXETINE	CYP2D6	11147928
# FOR	ARIPIPRAZOLE	ITRACONAZOLE	CYP3A4	15770075
# FOR	ATORVASTATIN	ITRACONAZOLE	CYP3A4	9695720
# FOR	BETA-HYDROXY-LOVASTATIN	ITRACONAZOLE	CYP3A4	8689812
# FOR	BETA-HYDROXY-LOVASTATIN	ITRACONAZOLE	CYP3A4	8689812
# FOR	BETA-HYDROXY-SIMVASTATIN	CLARITHROMYCIN	CYP3A4	15518608
# FOR	BETA-HYDROXY-SIMVASTATIN	ITRACONAZOLE	CYP3A4	9542477
# FOR	BETA-HYDROXY-SIMVASTATIN	ITRACONAZOLE	CYP3A4	9542477
# FOR	CLOZAPINE	PAROXETINE	CYP2D6	11147928
# FOR	DEHYDRO-ARIPIPRAZOLE	ITRACONAZOLE	CYP3A4	15770075
# FOR	DESIPRAMINE	CINACALCET	CYP2D6	16680561
# FOR	DESIPRAMINE	DULOXETINE	CYP2D6	12621382
# FOR	DEXTROMETHORPHAN	BUPROPION	CYP2D6	15876900
# FOR	DEXTROMETHORPHAN	CINACALCET	CYP2D6	17652181
# FOR	DEXTROMETHORPHAN	FLUOXETINE	CYP2D6	11910262
# FOR	DEXTROMETHORPHAN	PAROXETINE	CYP2D6	11910262
# FOR	DEXTROMETHORPHAN	SERTRALINE	CYP2D6	11910262
# FOR	DULOXETINE	PAROXETINE	CYP2D6	12621382
# FOR	LOVASTATIN	ITRACONAZOLE	CYP3A4	8689812
# FOR	LOVASTATIN	ITRACONAZOLE	CYP3A4	8689812
# FOR	METOPROLOL	CELECOXIB	CYP2D6	12891223
# FOR	MIDAZOLAM	ATORVASTATIN	CYP3A4	12911366
# FOR	MIDAZOLAM	CLARITHROMYCIN	CYP3A4	8880291
# FOR	MIDAZOLAM	ERYTHROMYCIN	CYP3A4	8720318
# FOR	MIDAZOLAM	FLUCONAZOLE	CYP3A4	16172184
# FOR	MIDAZOLAM	KETOCONAZOLE	CYP3A4	14551182
# FOR	MIDAZOLAM	KETOCONAZOLE	CYP3A4	15114429
# FOR	PERPHENAZINE	PAROXETINE	CYP2D6	9333110
# FOR	QUETIAPINE	ERYTHROMYCIN	CYP3A4	15834460
# FOR	QUETIAPINE	KETOCONAZOLE	CYP3A4	16390352
# FOR	SIMVASTATIN	CLARITHROMYCIN	CYP3A4	15518608
# FOR	SIMVASTATIN	ITRACONAZOLE	CYP3A4	9542477
# FOR	SIMVASTATIN	ITRACONAZOLE	CYP3A4	9542477
# FOR	THEOPHYLLINE	FLUVOXAMINE	CYP1A2	11719727
# FOR	TRIAZOLAM	DILTIAZEM	CYP3A4	9146848
# FOR	TRIAZOLAM	ERYTHROMYCIN	CYP3A4	9757151
# FOR	TRIAZOLAM	FLUCONAZOLE	CYP3A4	8904618
# FOR	WARFARIN	FLUCONAZOLE	CYP2C9	8801057
# FOR	ZIPRASIDONE	KETOCONAZOLE	CYP3A4	10771458


### AUC studies manually compiled from DIKB and evidence sheets
### reviewed but not yet entered into the system

# FOR	BUPROPION	VALPROATE		PMID 8830063 : T. A. Ketter, J. B. Jenkins, D. H. Schroeder, P. J. Pazzaglia, L. B. Marangell, M. S. George, A. M. Callahan, M. L. Hinton, J. Chao, and R. M. Post. Carbamazepine but not valproate induces bupropion metabolism. J Clin Psychopharmacol, 15(5):327-333, 1995.
# FOR	BUPROPION	CLOPIDOGREL		PMID 15961986 : M. Turpeinen, A. Tolonen, J. Uusitalo, J. Jalonen, O. Pelkonen, and K. Laine. Effect of clopidogrel and ticlopidine on cytochrome P450 2B6 activity as measured by bupropion hydroxylation. Clin Pharmacol Ther, 77(6):553-559, 2005. 
# FOR	BUPROPION	TICLOPIDINE		PMID 15961986 : M. Turpeinen, A. Tolonen, J. Uusitalo, J. Jalonen, O. Pelkonen, and K. Laine. Effect of clopidogrel and ticlopidine on cytochrome P450 2B6 activity as measured by bupropion hydroxylation. Clin Pharmacol Ther, 77(6):553-559, 2005.
# FOR	CLOZAPINE	FLUVOXAMINE	CYP1A2	pmid 10445377:  W. H. Chang, B. Augustin, H. Y. Lane, T. ZumBrunnen, H. C. Liu, Y. Kazmi, and M. W. Jann. In-vitro and in-vivo evaluation of the drug-drug interaction between fluvoxamine and clozapine. Psychopharmacology (Berl), 145(1):91-98, 1999.
# FOR	DULOXETINE	FLUVOXAMINE	CYP1A2	pmid 18307373: E. D. Lobo, R. F. Bergstrom, S. Reddy, T. Quinlan, J. Chappell, Q. Hong, B. Ring, and M. P. Knadler. In vitro and in vivo evaluations of cytochrome P450 1A2 interactions with duloxetine. Clin Pharmacokinet, 47(3):191-202, 2008.
# FOR	ESCITALOPRAM	CIMETIDINE	CYP3A4	PMID 16120067: D. Malling, M. N. Poulsen, and B. Sogaard. The effect of cimetidine or omeprazole on the pharmacokinetics of escitalopram in healthy subjects. Br J Clin Pharmacol, 60(3):287-290, 2005. 
# FOR	ESCITALOPRAM	OMEPRAZOLE		PMID 16120067: D. Malling, M. N. Poulsen, and B. Sogaard. The effect of cimetidine or omeprazole on the pharmacokinetics of escitalopram in healthy subjects. Br J Clin Pharmacol, 60(3):287-290, 2005. 
# FOR	MIRTAZAPINE	CIMETIDINE	CYP3A5	PMID 11009047 : J. Sitsen, F. Maris, and C. Timmer. Drug-drug interaction studies with mirtazapine and carbamazepine in healthy male subjects. Eur J Drug Metab Pharmacokinet, 26(1-2):109-121, 2001.
# FOR	MIRTAZAPINE	PAROXETINE	CYP2D6	pmid 12404553: F. J. Ruwe, R. A. Smulders, H. J. Kleijn, H. L. Hartmans, and J. M. Sitsen. Mirtazapine and paroxetine: a drug-drug interaction study in healthy subjects. Hum Psychopharmacol, 16(6):449-459, 2001. 
# FOR	OLANZAPINE	FLUOXETINE	CYP2D6	PMID 12102620 : D. Gossen, J. M. de Suray, F. Vandenhende, C. Onkelinx, and D. Gangji. Influence of fluoxetine on olanzapine pharmacokinetics. AAPS PharmSci, 4(2):E11, 2002.
# FOR	OLANZAPINE	FLUVOXAMINE		PMID 15199083: C. Y. Wang, Z. J. Zhang, W. B. Li, Y. M. Zhai, Z. J. Cai, Y. Z. Weng, R. H. Zhu, J. P. Zhao, and H. H. Zhou. The differential effects of steady-state fluvoxamine on the pharmacokinetics of olanzapine and clozapine in healthy volunteers. J Clin Pharmacol, 44(7):785-792, 2004.
# FOR	PAROXETINE	TERBINAFINE	CYP2D6	PMID 17124578 : N. Yasui-Furukori, M. Saito, Y. Inoue, T. Niioka, Y. Sato, S. Tsuchimine, and S. Kaneko. Terbinafine increases the plasma concentration of paroxetine after a single oral administration of paroxetine in healthy subjects. Eur J Clin Pharmacol, 63(1):51-56, 2007.
# FOR	QUETIAPINE	ERYTHROMYCIN		PMID 15599502 : K. Y. Li, X. Li, Z. N. Cheng, B. K. Zhang, W. X. Peng, and H. D. Li. Effect of erythromycin on metabolism of quetiapine in Chinese suffering from schizophrenia. Eur J Clin Pharmacol, 60(11):791-795, 2005.
# FOR	RISPERIDONE	VENLAFAXINE		PMID 10073330 :  J. Amchin, W. Zarycranski, K. P. Taylor, D. Albano, and P. M. Klockowski. Effect of venlafaxine on the pharmacokinetics of risperidone. J Clin Pharmacol, 39(3):297-309, 1999.
# FOR	TRAZODONE	CLARITHROMYCIN	CYP3A4	PMID 19242403 : D. Farkas, L. P. Volak, J. S. Harmatz, L. L. von Moltke, M. H. Court, and D. J. Greenblatt. Short-term clarithromycin administration impairs clearance and enhances pharmacodynamic effects of trazodone but not of zolpidem. Clin Pharmacol Ther, 85(6):644-650, 2009.
# FOR	VENLAFAXINE	CIMETIDINE	CYP3A4	PMID 9602962 : S. M. Troy, R. Rudolph, M. Mayersohn, and S. T. Chiang. The influence of cimetidine on the disposition kinetics of the antidepressant venlafaxine. J Clin Pharmacol, 38(5):467-474, 1998.
# FOR	VENLAFAXINE	TERBINAFINE	CYP2D6	PMID 17687273 : V. V. Hynninen, K. T. Olkkola, L. Bertilsson, K. Kurkinen, P. J. Neuvonen, and K. Laine. Effect of terbinafine and voriconazole on the pharmacokinetics of the antidepressant venlafaxine. Clin Pharmacol Ther, 83(2):342-348, 2008.
# AGAINST	ARIPIPRAZOLE	VALPROATE		PMID 15601809 :  L. Citrome, R. Josiassen, N. Bark, D. E. Salazar, and S. Mallikaarjun. Pharmacokinetics of aripiprazole and concomitant lithium and valproate. J Clin Pharmacol, 45(1):89-93, 2005.
# AGAINST	BUPROPION	VALPROATE		PMID 8830063 : T. A. Ketter, J. B. Jenkins, D. H. Schroeder, P. J. Pazzaglia, L. B. Marangell, M. S. George, A. M. Callahan, M. L. Hinton, J. Chao, and R. M. Post. Carbamazepine but not valproate induces bupropion metabolism. J Clin Psychopharmacol, 15(5):327-333, 1995.
# AGAINST	PALIPERIDONE	VENLAFAXINE		PMID 10073330 : J. Amchin, W. Zarycranski, K. P. Taylor, D. Albano, and P. M. Klockowski. Effect of venlafaxine on the pharmacokinetics of risperidone. J Clin Pharmacol, 39(3):297-309, 1999.
# AGAINST	QUETIAPINE 	CIMETIDINE		PMID 11910267 : S. M. Strakowski, P. E. Jr Keck, Y. W. Wong, P. T. Thyrum, and C. Yeh. The effect of multiple doses of cimetidine on the steady-state pharmacokinetics of quetiapine in men with selected psychotic disorders. J Clin Psychopharmacol, 22(2):201-205, 2002.
# AGAINST	RISPERIDONE	VERAPAMIL		PMID 16003291 : T. Nakagami, N. Yasui-Furukori, M. Saito, T. Tateishi, and S. Kaneo. Effect of verapamil on pharmacokinetics and pharmacodynamics of risperidone: in vivo evidence of involvement of P-glycoprotein in risperidone disposition. Clin Pharmacol Ther, 78(1):43-51, 2005.
# AGAINST	ZIPRASIDONE	CIMETIDINE		PMID 10771455 : K. D. Wilner, R. A. Hansen, C. J. Folger, and P. Geoffroy. The pharmacokinetics of ziprasidone in healthy volunteers treated with cimetidine or antacid. Br J Clin Pharmacol, 49 Suppl 1:57S-60S, 2000.

################################################################################

# get all PMIDs for every article entered into the DIKB
doc_pointer_d = {}
for e,v in ev.objects.iteritems():
    for evd in v.evidence_for:
        doc_pointer_d[evd.doc_pointer] = None
    for evd in v.evidence_against:
        doc_pointer_d[evd.doc_pointer] = None

print "%s" % doc_pointer_d.keys()

len(doc_pointer_d.keys())


################################################################################

# get the length of the maximum size quote field
quotes = []
for e,v in ev.objects.iteritems():
    for evd in v.evidence_for:
        quotes.append(evd.quote)
    for evd in v.evidence_against:
        quotes.append(evd.quote)

mx = -1
for q in quotes:
    if len(q) > mx:
        mx = len(q)

################################################################################

# get all claims about citalopram in the DIKB that are from package inserts
dlFull = []
for e,v in ev.objects.iteritems():
    if v.object != "citalopram":
        continue

    for evd in v.evidence_for:
        if evd.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("for")
            dl.append(evd.doc_pointer)
            dl.append(evd.quote)
            dlFull.append(dl)
    for evd in v.evidence_against:
        if evd.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("against")
            dl.append(evd.doc_pointer)
            dl.append(evd.quote)
            dlFull.append(dl)

for l in dlFull:
    print "\t".join(l)

##########################################################################################
# get all claims about venlafaxine in the DIKB that are from package inserts
dlFull = []
for e,v in ev.objects.iteritems():
    if v.object != "venlafaxine":
        continue

    for evd in v.evidence_for:
        if evd.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("for")
            dl.append(evd.doc_pointer)
            dl.append(evd.quote)
            dlFull.append(dl)
    for evd in v.evidence_against:
        if evd.evidence_type.value == "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("against")
            dl.append(evd.doc_pointer)
            dl.append(evd.quote)
            dlFull.append(dl)

for l in dlFull:
    print "\t".join(l)

##########################################################################################

# get all claims about citalopram in the DIKB that are NOT from package inserts
dlFull = []
for e,v in ev.objects.iteritems():
    if v.object != "citalopram":
        continue

    for evd in v.evidence_for:
        if evd.evidence_type.value != "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("for")
            dl.append(evd.doc_pointer)
            dl.append("\"%s\"" % evd.quote)
            dlFull.append(dl)
    for evd in v.evidence_against:
        if evd.evidence_type.value != "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("against")
            dl.append(evd.doc_pointer)
            dl.append("\"%s\"" % evd.quote)
            dlFull.append(dl)

for l in dlFull:
    print "|".join(l)


##########################################################################################

dlFull = []
for e,v in ev.objects.iteritems():
    if v.object != "venlafaxine":
        continue

    for evd in v.evidence_for:
        if evd.evidence_type.value != "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("for")
            dl.append(evd.doc_pointer)
            dl.append("\"%s\"" % evd.quote)
            dlFull.append(dl)
    for evd in v.evidence_against:
        if evd.evidence_type.value != "Non_traceable_Drug_Label_Statement":
            dl = [v.object, v.slot, v.value]
            dl.append("against")
            dl.append(evd.doc_pointer)
            dl.append("\"%s\"" % evd.quote)
            dlFull.append(dl)

for l in dlFull:
    print "|".join(l)
