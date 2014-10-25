(defun increase-auc-assertion (object precip)
  (interactive 
   (list
    (setq object (read-string "object-drug: "))
    (setq precip (read-string "precipitant-drug: "))))

  (setq s (concat "a = ContValAssertion(\"" precip "\", \"increases_auc\" ,\"" object "\")\n"
		  "e1 = PKStudy()\n"
		  "e1.create(\"\", \"(as summarized in UW DIDB) #volunteers: ; " object ": mg po; " precip " mg tidx d, po; change in AUC: \", \"rct1\",\"boycer\", \"01312006\", , , ) \n"
		  "a.insertEvidence( \"for\", e1)\n"
		  "ev.addAssertion(a)\n"
		  "ev.objects[\"" precip "_increases_auc_" object "\"].ready_for_classification = False"))
 
  (princ s (current-buffer)))


	
