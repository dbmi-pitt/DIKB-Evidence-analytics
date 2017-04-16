# parse-inference-results-to-tsv.py
# purpose: re-format the inference results for further analysis
# made by dr. richard boyce, revised and updated by samuel rosko
# last update: 4/18/2016
import re

val_kys = {}
with open('/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/scr25-combination-list.txt','r') as inf:
    val_kys = eval(inf.read())

## scr25 configuration
pth_prfx = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/experiment_2"

f = open(pth_prfx + "/paths-to-experiment-folders", 'r')
dirs = f.read().split("\n")
f.close()

log_f = open("/media/scr25/DATA/drive-logs/parse-inferences.log", 'w')
cntr = 1

for pth in dirs:
    f = open(pth + "/inference-results")
    
    buf_l = f.read().split("\n")
    asrts = []
    for ast in buf_l:
        if ast.find("NO-PKI") != -1 or ast.find("PKI-1") != -1 or ast.find("PKI-2") != -1 or ast.find("PKI-3") != -1:
            asrts.append(ast)
    asrts_st = "\n".join(asrts)
    f.close()

    no_int_re = re.compile("<TR><TD>NO-PKI</TD><TD>(.*) DOES NOT INHIBIT THE METABOLIC CLEARANCE OF (.*) VIA")
    no_int_l = no_int_re.findall(asrts_st)

    pki_1_re =  re.compile("<TR><TD>PKI-1</TD><TD>(.*) INHIBITS METABOLIC CLEARANCE OF (.*) VIA")
    pki_1_l = pki_1_re.findall(asrts_st)

    pki_2_re =  re.compile("<TR><TD>PKI-2</TD><TD>(.*) INHIBITS .* THE PRIMARY METABOLIC ENZYME of (.*)</TD><TD>")
    pki_2_l = pki_2_re.findall(asrts_st)

    pki_3_re =  re.compile("<TR><TD>PKI-3</TD><TD>(.*) INHIBITS .* THE PRIMARY TOTAL CLEARANCE ENZ OF (.*)</TD><TD>")
    pki_3_l = pki_3_re.findall(asrts_st)

    f = open(pth + "/experiment-results-tab.tsv", "w")
    f.write("PAIR\tDDI_DIKB\tNON_DDI_DIKB\n")

    cmbnd = map(lambda x: (x, "NO-PKI"), no_int_l) + map(lambda x: (x, "PKI-1"), pki_1_l) + map(lambda x: (x, "PKI-2"), pki_2_l) + map(lambda x: (x, "PKI-3"), pki_3_l)
    for (ast, lbl) in cmbnd:
        # first, translate the free text represention of each active
        # ingredient or metabolite to the its representation in the
        # validation set
        (d1,d2) = (ast[0].lower().replace(" ", "-").replace("prime","prime-").replace("prime","'").replace("--","-"),
                   ast[1].lower().replace(" ", "-").replace("prime","prime-").replace("prime","'").replace("--","-"))
        ll_rep = ["6beta-hydroxytestosterone", "n-demethyl_erythromycin", "n-demethyldesacetyl-diltiazem", "n-demethyldiltiazem", "n-desmethylrosuvastatin"]
        corr_rep = ["6beta-Hydroxytestosterone", "N-Demethyl_erythromycin", "N-demethyldesacetyl-diltiazem", "N-demethyldiltiazem", "N-desmethylrosuvastatin"]
        for cnt in range(0, len(ll_rep)):
            if d1 == ll_rep[cnt]:
                d1 = corr_rep[cnt]
            if d2 == ll_rep[cnt]:
                d2 = corr_rep[cnt]

        # now see if the pair is in the validation set 
        t1 = "%s - %s" % (d1, d2)
        t2 = "%s - %s" % (d2, d1)
        if val_kys.has_key(t1):
            if lbl == "NO-PKI":
                s = "%s\t\t%s\n" % (t1, lbl)
            else:
                s = "%s\t%s\t\n" % (t1, lbl)
            #print s
            f.write(s)
        
        elif val_kys.has_key(t2):
            if lbl == "NO-PKI":
                s = "%s\t\t%s\n" % (t2, lbl)
            else:
                s = "%s\t%s\t\n" % (t2, lbl)
            #print s
            f.write(s)
        else:
            log_f.write("WARNING: could not find pair '%s' or '%s' in validation set key list!" % (t1, t2))

    f.close()

    log_f.write("\n%d: parsed inference-results in %s to %s" % (cntr, pth + "/inference-results", pth + "/experiment-results-tab.tsv"))
    cntr +=1
    
log_f.close()
