# # ### an audit trail of evidence entries from command line

# # from DIKB_Utils import *
# # from DIKB import *
# # from DrugModel import *
# # from EvidenceModel import *


# # ev = EvidenceBase("evidence","123")
# # dikb = DIKB("dikb","123", ev)
# # dikb.unpickleKB("../var/DIKB/dikb.pickle")
# # ev.unpickleKB("../var/evidence-base/ev.pickle")
# # ev.renotifyObservers()


# # '''
# # a = ContValAssertion("erythromycin","increases_auc","midazolam")
# # e1 = PKStudy()
# # e1.create("10579141","midazolam: 15mg po; erythromycin 500 mg tidx7 d, po; change in AUC: 220", "rct1", "boycer", "01302006", 15.0, 500.0, 2.2)
# # a.insertEvidence("for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_midazolam"].ready_for_classification = True

# # dikb.pickleKB("../var/DIKB/dikb.pickle")
# # ev.pickleKB("../var/evidence-base/ev.pickle")

# # a = ContValAssertion("diltiazem","increases_auc","midazolam")
# # e1 = PKStudy()
# # e1.create("10579141","midazolam: 15mg po; diltiazem 60 mg tidx3 d, po; change in AUC: 380", "rct1", "boycer", "01302006", 15, 60.0, 3.8)
# # a.insertEvidence("for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_midazolam"].ready_for_classification = True

# # dikb.pickleKB("../var/DIKB/dikb.pickle")
# # ev.pickleKB("../var/evidence-base/ev.pickle")

# # '''
# # #
# # a = ContValAssertion("itraconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8181191", "# volunteers: 9; midazolam: 7.5mg po; itraconazole 200mg tidx4 d, po; change in AUC: 10-15", "rct1","boycer", "01312006" , 7.5, 200, 15) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_midazolam"].ready_for_classification = True
# # #
# # a = ContValAssertion("itraconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8527290", "#volunteers: 20; midazolam: 7.5mg po; itraconazole 100mg tidx d, po; change in AUC: 6-fold", "rct1","boycer", "01312006" , 7.5, 100, 6) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)

# # #
# # a = ContValAssertion("itraconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8623953", "#volunteers: 12; midazolam: 7.5mg po; itraconazole 200mg tidx 6d, po; change in AUC: 3.5-7 fold", "rct1","boycer", "01312006" ,7.5, 200, 7.0) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8181191", "#volunteers: 9; midazolam: 7.5mg po; ketoconazole 400mg tidx 4d, po; change in AUC: 10-15", "rct1","boycer", "01312006" , 7.5, 400, 15) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("9784084", "#volunteers: 10; alprazolam: .8mg po; itraconazole 200mg tidx 6d, po; change in AUC: 1.6", "rct1","boycer", "01312006", .8, 200, 1.6) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_alprazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("7995001", "#volunteers: 9; triazolam: .25mg po; itraconazole 200mg tidx 4d, po; change in AUC: 26", "rct1","boycer", "01312006", .25, 200, 26) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8841155", "#volunteers: 10; triazolam: .25mg po; itraconazole 200mg tidx 1d, po; change in AUC: 2.6", "rct1","boycer", "01312006", .25, 200, 2.6) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"simvastatin")
# # e1 = PKStudy()
# # e1.create("9542477", "#volunteers: 10; simvastatin: 40mg po; itraconazole 200mg tidx 4d, po; change in AUC: 10", "rct1","boycer", "01312006", 40, 200, 10) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_simvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"lovastatin")
# # e1 = PKStudy()
# # e1.create("8689812", "#volunteers: 12; lovastatin: 40mg po; itraconazole 200mg tidx 4d, po; change in AUC: 35", "rct1","boycer", "01312006", 40,200 , 35 ) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_lovastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"lovastatin")
# # e1 = PKStudy()
# # e1.create("9690949", "#volunteers: 10; lovastatin: 40mg po; itraconazole 100mg tidx 4d, po; change in AUC: 13.8", "rct1","boycer", "01312006",40 ,100 ,13.8) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_lovastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"fluvastatin")
# # e1 = PKStudy()
# # e1.create("9690949", "(as summarized in UW DIDB) #volunteers: 10; fluvastatin: 40mg po; itraconazole 100mg tidx 4d, po; change in AUC: 13.6", "rct1","boycer", "01312006", 40, 100, 13.6) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_fluvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"atorvastatin")
# # e1 = PKStudy()
# # e1.create("11061579", "#volunteers: 18; atorvastatin: 20mg po; itraconazole 200mg tidx 5d, po; change in AUC: 150%", "rct1","boycer", "01312006", 20, 200, 1.5) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_atorvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"pravastatin")
# # e1 = PKStudy()
# # e1.create("11061579", "#volunteers: 18; pravastatin: 40mg po; itraconazole 200mg tidx 5d, po; change in AUC: 51%", "rct1","boycer", "01312006", 40, 200, .5) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_pravastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"pravastatin")
# # e1 = PKStudy()
# # e1.create("9542477", "#volunteers: 10; pravastatin: 40mg po; itraconazole 200mg tidx 4d, po; change in AUC: 71.6%", "rct1","boycer", "01312006", 40, 200, .7) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_pravastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"rosuvastatin")
# # e1 = PKStudy()
# # e1.create("12709722", "#volunteers: 14; rosuvastatin: 80mg po; itraconazole 200mg tidx 5d, po; change in AUC: 26.4%", "rct1","boycer", "01312006", 80,200 , .26 ) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_rosuvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("itraconazole", "increases_auc" ,"rosuvastatin")
# # e1 = PKStudy()
# # e1.create("12709722", "#volunteers: 12; rosuvastatin: 10mg po; itraconazole 200mg tidx 5d, po; change in AUC: .37.3%", "rct1","boycer", "01312006", 10,200 , .37) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["itraconazole_increases_auc_rosuvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("8646822", "#volunteers: 12; alprazolam: 0.8mg po; erythromycin 400mg tidx d, po; change in AUC: 147.2% ", "rct1","boycer", "01312006", .8, 400, 1.47) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_alprazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("3771812", "#volunteers: 16; triazolam: 0.5mg po; erythromycin 333mg tidx 3d, po; change in AUC: 106% ", "rct1","boycer", "01312006", 0.5, 333, 1.06) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("9757151", "#volunteers: 12; triazolam: .125mg po; erythromycin 500mg tidx 2d, po; change in AUC: 280%", "rct1","boycer", "01312006", .125, 500, 2.8) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"simvastatin")
# # e1 = PKStudy()
# # e1.create("9728898", "(as summarized in UW DIDB) #volunteers: 12; simvastatin: 40mg po; erythromycin 500mg tidx 2d, po; change in AUC: 521.5%", "rct1","boycer", "01312006", 40, 500, 5.22) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_simvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"atorvastatin")
# # e1 = PKStudy()
# # e1.create("10234598", "(as summarized in UW DIDB) #volunteers: 11; atorvastatin: 10mg po; erythromycin 500mg tidx 11d, po; change in AUC: 32.5%", "rct1","boycer", "01312006", 10, 500, .33) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_atorvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("9757147", "(as summarized in UW DIDB) #volunteers: 7; alprazolam: 1mg po; ketoconazole 200mg tidx 4d, po; change in AUC: 298.3% ", "rct1","boycer", "01312006",1 ,200 , 2.98 ) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_alprazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("10634135", "(as summarized in UW DIDB) #volunteers: 4; alprazolam: 1mg po; ketoconazole 200mg tidx 2d, po; change in AUC: 76% ", "rct1","boycer", "01312006", 1, 200, .76) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_alprazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("9757147", "(as summarized in UW DIDB) #volunteers: 6; triazolam: .25mg po; ketoconazole 200mg tidx 4d, po; change in AUC:  1271.7%", "rct1","boycer", "01312006", .25 , 200 , 12.7 ) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8904618", "(as summarized in UW DIDB) #volunteers: 8; triazolam: .25mg po; fluconazole 100mg tidx 4d, po; change in AUC: 105.4%", "rct1","boycer", "01312006", .25,100 , 1.05) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8904618", "(as summarized in UW DIDB) #volunteers: 8; triazolam: .25mg po; fluconazole 200mg tidx 4d, po; change in AUC: 342.4%", "rct1","boycer", "01312006", .25, 200, 3.42) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8904618", "(as summarized in UW DIDB) #volunteers: 8; triazolam: .25mg po; fluconazole 50mg tidx 4d, po; change in AUC: 63%", "rct1","boycer", "01312006", .25, 50, .63) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8730978", "(as summarized in UW DIDB) #volunteers: 12; triazolam: .25mg po; fluconazole 100mg tidx 4d, po; change in AUC: 145.9%", "rct1","boycer", "01312006", .25, 100, 1.46) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_triazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"fluvastatin")
# # e1 = PKStudy()
# # e1.create("10952477", "(as summarized in UW DIDB) #volunteers: 12; fluvastatin: 40mg po; fluconazole 400 mg on day 1 and 200 mg on days 2-4 mg tidx 4d, po; change in AUC: 83.7% ", "rct1","boycer", "01312006", 40, 400, .84) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_fluvastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"pravastatin")
# # e1 = PKStudy()
# # e1.create("10952477", "(as summarized in UW DIDB) #volunteers: 12; pravastatin: 40mg po; fluconazole 400 mg on day 1 and 200 mg on days 2-4; change in AUC: 35.8%", "rct1","boycer", "01312006", 40, 200, .36) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_pravastatin"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("16172814", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 3mg po; fluconazole 100mg single dose, po; change in AUC: 116.4% ", "rct1","boycer", "01312006", 3 ,100 , 1.16 ) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("16172814", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 3mg po; fluconazole 200mg single dose, po; change in AUC: 231.9%", "rct1","boycer", "01312006", 3, 200, 2.32) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("16172814", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 3mg po; fluconazole 400mg single dose, po; change in AUC: 393% ", "rct1","boycer", "01312006", 3 ,400 , 3.93) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("fluconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8623953", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 7.5mg po; fluconazole 400 mg at D1 and then 200 mg (5 days); change in AUC: 259.8%", "rct1","boycer", "01312006",7.5 , 400, 2.6) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["fluconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("10579473", "(as summarized in UW DIDB) #volunteers: 9 ; midazolam: 6mg po; ketoconazole 200mg tidx 1.5d, po; change in AUC: 1261.6%", "rct1","boycer", "01312006", 6, 200, 12.62) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("ketoconazole", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("14551182", "(as summarized in UW DIDB) #volunteers: 10; midazolam: 10mg po; ketoconazole 200mg tidx 12d, po; change in AUC:  772+-596 ", "rct1","boycer", "01312006", 10, 200, 7.72) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["ketoconazole_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8720318", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 15mg po; erythromycin 500mg tidx 5d, po; change in AUC: 281.4%", "rct1","boycer", "01312006", 15, 500, 2.81) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("erythromycin", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8453848", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 15mg po; erythromycin 500mg tidx 7d, po; change in AUC: 341.7%", "rct1","boycer", "01312006", 15, 500, 3.42) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["erythromycin_increases_auc_midazolam"].ready_for_classification = True

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8880291", "(as summarized in UW DIDB) #volunteers: 12; midazolam: 15mg po; clarithromycin 250mg bid, po; change in AUC: 257.2%", "rct1","boycer", "01312006", 15, 250, 2.57) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_midazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"simvastatin")
# # e1 = PKStudy()
# # e1.create("15518608", "(as summarized in UW DIDB) #volunteers: 15; simvastatin: 40mg once daily on days 1-7 alone and with clarithromycin on days 10-17; clarithromycin 500mg BID on days 10-18; change in AUC: 895.5%", "rct1","boycer", "01312006", 40, 500, 8.96) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_simvastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"pravastatin")
# # e1 = PKStudy()
# # e1.create("15518608", "(as summarized in UW DIDB) #volunteers: 15; pravastatin: 40mg  once daily on days 1-7 alone and with clarithromycin on days 10-17; clarithromycin 500mg BID on days 10-18; change in AUC: 111.1%", "rct1","boycer", "01312006", 40, 500, 1.11) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_pravastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"atorvastatin")
# # e1 = PKStudy()
# # e1.create("15518608", "(as summarized in UW DIDB) #volunteers: 15; atorvastatin: 80mg  once daily on days 1-7 alone and with clarithromycin on days 10-17; clarithromycin 500mg BID on days 10-18; change in AUC: 345.1%", "rct1","boycer", "01312006", 80, 500, 3.45) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_atorvastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"atorvastatin")
# # e1 = PKStudy()
# # e1.create("11936570", "(as summarized in UW DIDB) #volunteers: 24; atorvastatin: 10mg po, once daily; clarithromycin 500mg tidx 3d, po, bid, from day 6 to day 8 of atorvastatin treatment; change in AUC: 81.9%", "rct1","boycer", "01312006", 10, 500, .82) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_atorvastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("clarithromycin", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("9757151", "(as summarized in UW DIDB) #volunteers: 12; triazolam: 0.125mg po single dose, 1h after the 3rd dose of clarithromycin or placebo; clarithromycin 500mg tidx 2d, po; change in AUC: 425.5%", "rct1","boycer", "01312006", 0.125, 500, 4.255) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["clarithromycin_increases_auc_triazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("nefazodone", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("14551182", "(as summarized in UW DIDB) #volunteers: 10; midazolam: 10mg single dose of midazolam oral solution (prepared as a 1:1 mixture of injectable midazolam and flavored, dye-free syrup), alone and 1 hour after the last dose of nefazodone; nefazodone 200 mg bid (100 mg bid for 5 days and 200 mg bid for 7 days); change in AUC: 444%", "rct1","boycer", "01312006", 10, 200, 4.44) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["nefazodone_increases_auc_midazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("nefazodone", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("8748428", "(as summarized in UW DIDB) #volunteers: 48; alprazolam: 1mg bid po 7days; nefazodone 200mg bidx 7d, po; change in AUC:98% ", "rct1","boycer", "01312006", 1, 200, .98) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["nefazodone_increases_auc_alprazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("nefazodone", "increases_auc" ,"alprazolam")
# # e1 = PKStudy()
# # e1.create("14709940", "(as summarized in UW DIDB) #volunteers: 16 (CYP2D6 EMs); alprazolam: 2mg po single dose before and on the last day of nefazodone therapy; nefazodone 400mg BID; 200 mg/day for 3 days then 400 mg/day for 5 days, po; change in AUC: 47.3%", "rct1","boycer", "01312006", 2, 400, .473) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["nefazodone_increases_auc_alprazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("nefazodone", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8830062", "(as summarized in UW DIDB) #volunteers: 12; triazolam: .25mg po; nefazodone 200mg bidx 7d, po; change in AUC: 289.9%", "rct1","boycer", "01312006", .25, 200, 2.899) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["nefazodone_increases_auc_triazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"midazolam")
# # e1 = PKStudy()
# # e1.create("8198928", "(as summarized in UW DIDB) #volunteers: 9; midazolam: 15mg po; diltiazem 60mg tidx 2d, po; change in AUC: 275%", "rct1","boycer", "01312006", 15, 60, 2.75) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_midazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("8612379", "(as summarized in UW DIDB) #volunteers: 10; triazolam: .25mg po; diltiazem 60mg tidx 2d, po; change in AUC: 238.1", "rct1","boycer", "01312006", .25, 60, 2.381) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_triazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"triazolam")
# # e1 = PKStudy()
# # e1.create("9146848", "(as summarized in UW DIDB) #volunteers: 7; triazolam: 0.25mg po; diltiazem 60mg   tid for 3 days and 1 hour before triazolam intake, po; change in AUC: 127.5%", "rct1","boycer", "01312006", .25, 60, 1.275) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_triazolam"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"simvastatin")
# # e1 = PKStudy()
# # e1.create("10741630", "(as summarized in UW DIDB) #volunteers: 10; simvastatin: 20mg po; diltiazem 120mg bid 2wks, po; change in AUC: 381.4% ", "rct1","boycer", "01312006", 20, 120, 3.814) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_simvastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"lovastatin")
# # e1 = PKStudy()
# # e1.create("9797793", "(as summarized in UW DIDB) #volunteers: 10; lovastatin: 20mg po; diltiazem 120mg bid x 2wks, po; change in AUC: 257.2%", "rct1","boycer", "01312006", 20, 120, 2.572) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_lovastatin"].ready_for_classification = False

# # #

# # a = ContValAssertion("diltiazem", "increases_auc" ,"pravastatin")
# # e1 = PKStudy()
# # e1.create("9797793", "(as summarized in UW DIDB) #volunteers: 10; pravastatin: 20mg po; diltiazem 120mg bid x 2wks, po; change in AUC: 2.7%", "rct1","boycer", "01312006", 20, 120, .027) 
# # a.insertEvidence( "for", e1)
# # ev.addAssertion(a)
# # ev.objects["diltiazem_increases_auc_pravastatin"].ready_for_classification = False

# # #

# # dikb.pickleKB("../var/DIKB/dikb.pickle")
# # ev.pickleKB("../var/evidence-base/ev.pickle")


# ########### fraction cleared by
# a = Assertion_m_discrete('alprazolam', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","alprazolam - f_mCYP: 0.80", 'est1', 'boycer', '02062006', 0.8)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# #

# a = Assertion_m_discrete('midazolam', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","midazolam - f_mCYP: 0.99", 'est3', 'boycer', '02062006', 0.99)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# a = Assertion_m_discrete('midazolam', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","midazolam - f_mCYP: 0.94", 'est1', 'boycer', '02062006', 0.99)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# ##

# a = Assertion_m_discrete('simvastatin', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","simvastatin - f_mCYP: 0.99", 'est2', 'boycer', '02062006', 0.99)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# #

# a = Assertion_m_discrete('triazolam', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","triazolam - f_mCYP: 0.98", 'est3', 'boycer', '02062006', 0.98)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# a = Assertion_m_discrete('triazolam', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","triazolam - f_mCYP: 0.92", 'est1', 'boycer', '02062006', 0.92)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# ##

# a = Assertion_m_discrete('lovastatin', 'fraction_cleared_by', 'cyp3a4')
# e1 = EvidenceContinousVal()
# e1.create("16236041","lovastatin - f_mCYP: 0.99", 'est2', 'boycer', '02062006', 0.99)
# a.insertEvidence( "for", e1)
# ev.addAssertion(a)

# #

# a1 =  Assertion_continuous_s_val('phenytoin','bioavailability','continuous_value')
# e1 = EvidenceContinousVal()
# e1.create("Goodman and Gillman 10th Ed", "90.0%", 'ast', 'boycer', '02142006', 90.0)
# a1.evidence_for.append(e1)
# ev.addAssertion(a1)
# ev.objects['phenytoin_bioavailability_continuous_value'].ready_for_classification = True

# #


# dikb.pickleKB("../var/DIKB/dikb.pickle")
# ev.pickleKB("../var/evidence-base/ev.pickle")


