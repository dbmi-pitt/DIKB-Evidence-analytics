;; a walk through of simulating changes to belief of mechanistic assertions
;; and their effect on a theory of metabolic drug-drug interaction


;; Example 1, a simple change of belief
(load "load")  ;; load the program
(load-demo-rule-base) ;; load the rules for reasoning and assumptions from evidence-base
                      ;; assertions are made using a soft belief criteria
(show-data)
(load "assertions")   ;; change to a more rigourous belief criteria and the some beliefs are retracted
(show-data)
(load "assertions")   ;; vice versa 
(show-data)


;;;;;;;;;          END DEMO 1                ;;;;;;;;;

;; Example 2, a change in belief of  default assumptions
(load "load")
(load-demo-rule-base)
(setq patient '(joe (simvastatin codiene))) 
(prescribe patient 'diltiazem)   ;; prescribe makes some assumptions about the drugs
                                 ;; and tests for any interactions

;; remove one of the interactions
(retract! '(CURRENTLY-NEAR-TOXIC-DOSE 'SIMVASTATIN) 'TEST-INFERENCE-ASSUMPTION) 

;;;;;;;;;          END DEMO 2                ;;;;;;;;;



;; Example 3, a  patient-specific pharmacological model
;; create a blank state for Joanne
(load "load")
(setq joanne-PK-state (patient-specific-rule-base))
(show-data joanne-PK-state)

(progn 
  (setq joanne '(joanne (SIMVASTATIN)))
  (assume! '(currently-accounts-for-more-than-half-clearance  'cyp3a4 'simvastatin) 'test joanne-PK-state)
  (run-rules joanne-PK-state)
  (show-data joanne-PK-state))

(progn
  (setq joanne '(joanne (SIMVASTATIN DILTIAZEM)))
  (assume! '(given-when-object-near-steady-state 'diltiazem 'simvastatin) 'test)
  (assume! '(sufficient-concentration-to-inhibit 'diltiazem 'cyp3a4) 'test)
  (assume! '(saturable-concentration 'diltiazem 'cyp3a4) 'test)
  (run-rules joanne-PK-state)
  (show-data joanne-PK-state))

(progn
  (show-data joanne-PK-state)
  (assume! '(currently-near-toxic-dose 'simvastatin) 'test)
  (show-data joanne-PK-state))
