;; The Drug Interaction Knowledge Base (DIKB) is (C) Copyright 2005- by
;; Richard Boyce

;; Original Authors:
;;   Richard Boyce

;;; LICENCE:
;;; Use, reproduction, and preparation of derivative works are permitted.
;;; Any copy of this software or of any derivative work must include the
;;; above copyright notice and this paragraph.  Any distribution of this
;;; software or derivative works must comply with all applicable United
;;; States export control laws.  This software is made available as is, and
;;; Kenneth D. Forbus, Johan de Kleer and Xerox Corporation disclaim all
;;; warranties, express or implied, including without limitation the implied
;;; warranties of merchantability and fitness for a particular purpose, and
;;; notwithstanding any other provision contained herein, any liability for
;;; damages resulting from the software or its use is expressly disclaimed,
;;; whether arising in contract, tort (including negligence) or strict
;;; liability, even if Kenneth D. Forbus, Johan de Kleer or Xerox
;;; Corporation is advised of the possibility of such damages.

;;


;; -----------------------------------------------------------------
;; File:          dikb-inference-test.lisp


;; NOTE: Be sure and load "load.lisp" first.

(in-package :COMMON-LISP-USER)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; simple utilities
(defun filter (fn lst)
  (let ((acc nil))
    (dolist (x lst)
      (let ((val (funcall fn x)))
	(if val (push val acc))))
    (nreverse acc)))

(defun get-in-assertions (ptrn)
  (filter #'(lambda (x)
	    (if (in? (eval (quotize x))) x ))
	(fetch ptrn)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; RULE BASES
(defun test-dissertation-DIKB-rule-base-readable ()
  "The rule-base written about in my dissertation --  A simple set of rules about 
   pharmacokinetic drug-drug interactions 
 Script for first example:
      (load \"load\")
      (test-dissertation-DIKB-rule-base-readable)

     ;; TEST 1a: a simple test of inhibition assertions
     ;; no dependencies
     (TEST-DISSERTATION-DIKB-RULE-BASE-READABLE)
     (assert! '(1-inhibits-2 'troleandomycin 'cyp2c9) '('dikb-assertion (bc-satisfied 'inhibits-cyp3a4-troleandomycin)))
     (assume!
          '(bc-satisfied 'inhibits-cyp3a4-troleandomycin)
            'default-inference-assumption)

     (assume! 
        '(1-is-an-in-vitro-selective-inhibitor-of-2 'clopidogrel 'cyp2b6) 
          'default-inference-assumption)
     (run-rules)
     (in? '(1-INHIBITS-2 'TROLEANDOMYCIN 'CYP2C9))
     (in? '(1-INHIBITS-2 'CLOPIDOGREL 'CYP2B6))


      ;; TEST 1b: test of inhibits and substrate-of rules
      ;; no dependancies on other tests 
      (TEST-DISSERTATION-DIKB-RULE-BASE-READABLE)
      (assert! '(1-is-substrate-of-2 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (1-is-an-in-vitro-selective-inhibitor-of-2 'diltiazem 'cyp3a4)))
      (assert! '(1-is-substrate-of-2 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (1-is-an-in-vitro-selective-inhibitor-of-2 'ketoconazole 'cyp3a4)))
      (assume! 
         '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
           'default-inference-assumption)
      
      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'itraconazole 'cyp3a4) 
           'default-inference-assumption)
      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'diltiazem 'cyp3a4) 
           'default-inference-assumption)
      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
           'default-inference-assumption)
      (run-rules)
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))
       
      (retract! 
          '(1-is-an-in-vitro-selective-inhibitor-of-2 'diltiazem 'cyp3a4) 
           'default-inference-assumption)
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))
      (not (in? '(1-INHIBITS-2 'DILTIAZEM 'CYP3A4)))

      (retract! 
          '(1-is-an-in-vitro-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
           'default-inference-assumption)
      (not (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4)))

      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
           'default-inference-assumption)
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))

      (retract! 
         '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
           'default-inference-assumption)
      (not (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4)))

      (assert! 
         '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
           'default-inference-assumption)
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))


      ;; TEST 2: test of the metabolite and ancestor rules
      ;; depends on TEST 1b for data and valid functionality
      (assert! '(1-has-metabolite-2-via-3 'simvastatin 'beta-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)))
      (assert! '(1-has-metabolite-2-via-3 'beta-hydroxy-simvastatin '6-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)))
      (assume! 
          '(bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)
           'default-inference-assumption)
      (assume! 
          '(bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)
           'default-inference-assumption) 
      (run-rules)
      (in? '(1-IS-ANCESTOR-OF-2 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN))
      (in? '(1-IS-SUBSTRATE-OF-2 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'BETA-HYDROXY-SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'KETOCONAZOLE 'BETA-HYDROXY-SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))

      ;; what of the matching assertions are :IN?
      (filter #'(lambda (x)
	    (if (in? (eval (quotize x))) x ))
         (fetch '(1-is-ancestor-of-2 'simvastatin ?x)))

      ;; TEST 3: test of active ingredient rules
      ;; depends on TEST 2 data and valid functionality
      (assume! 
          '(1-is-an-active-ingredient 'simvastatin)
           'default-inference-assumption)
      (assume! 
          '(1-is-an-active-ingredient 'itraconazole)
           'default-inference-assumption)
      (run-rules)
      (in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-IS-AFFECTED-BY-3 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'ITRACONAZOLE))
      
      (why? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-IS-AFFECTED-BY-3 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN  'ITRACONAZOLE))
      
      (assume! 
          '(1-inhibits-2 'diltiazem 'cyp3a4)
           'default-inference-assumption)
      (assume! 
          '(1-inhibits-2 'diltiazem-active-metabolite 'cyp3a4)
           'default-inference-assumption)

      (assume! 
          '(1-controls-formation-of-2 'cyp3a4 'diltiazem-active-metabolite)
           'default-inference-assumption)
      (assume! 
          '(1-has-metabolite-2 'diltiazem 'diltiazem-active-metabolite)
           'default-inference-assumption)
      
      (assume! 
          '(1-is-an-active-ingredient 'diltiazem)
           'default-inference-assumption)
      (run-rules)  
      (in? '(1-IS-ANCESTOR-OF-2 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'DILTIAZEM 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'DILTIAZEM-ACTIVE-METABOLITE 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
      (in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-IS-AFFECTED-BY-3 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'DILTIAZEM-ACTIVE-METABOLITE))
      (in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-EFFECTS-AN-INTERACTION-WITH-3 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'SIMVASTATIN))
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'CYP3A4))
      (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'DILTIAZEM 'CYP3A4))
      ;; NOTE: circular inhibition is allowed...for now
      (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'DILTIAZEM-ACTIVE-METABOLITE 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'CYP3A4))

      ;; TEST 4: a complicated test of the effect of inhibiting various metabolites
      ;; depends on success of tests 1, 2, 3, and 4 for validity but has no data dependencies
      (TEST-DISSERTATION-DIKB-RULE-BASE-READABLE)

      (assert! '(1-inhibits-2 'troleandomycin 'cyp2c9) '('dikb-assertion (bc-satisfied 'inhibits-cyp3a4-troleandomycin)))
      (assume!
          '(bc-satisfied 'inhibits-cyp3a4-troleandomycin)
            'default-inference-assumption)

      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'clopidogrel 'cyp2b6) 
           'default-inference-assumption)

      (assume! 
         '(1-is-an-in-vitro-selective-inhibitor-of-2 'itraconazole 'cyp3a4) 
           'default-inference-assumption)
 
      (assume! 
          '(1-is-an-active-ingredient 'cyclophosimide)
              'default-inference-assumption)
      (run-rules)


      (assume! 
          '(primary-total-clearance-mechanism-of-1-is-2 'cyclophosimide 'METABOLIC-CLEARANCE)
               'default-inference-assumption)
      (assume! 
           '(primary-metabolic-clearance-enzyme-of-1-is-2 'cyclophosimide 'cyp2b6)
                    'default-inference-assumption)    

      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp2b6) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2b6)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2b6)
            'default-inference-assumption)
    
      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp2a6) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2a6)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2a6)
            'default-inference-assumption)

      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp2c8) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c8)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c8)
            'default-inference-assumption)
      
      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp2c9) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c9)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c9)
            'default-inference-assumption)

      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp2c19) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c19)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp2c19)
            'default-inference-assumption)

      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '4-hydroxy-cyclophosimide 'cyp3a4) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp3a4)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-4-hydroxy-cyclophosimide-cyp3a4)
            'default-inference-assumption)
       
      (assert! '(1-has-metabolite-2-via-3 'cyclophosimide '2-dechloroethyl-cyclophosimide 'cyp3a4) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-2-dechloroethyl-cyclophosimide-cyp3a4)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-2-dechloroethyl-cyclophosimide-cyp3a4)
            'default-inference-assumption)
 
     (assert! '(1-has-metabolite-2-via-3 'cyclophosimide 'chloroacetaldehyde-cyclophosimide 'cyp3a4) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-chloroacetaldehyde-cyclophosimide-cyp3a4)))
     (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-chloroacetaldehyde-cyclophosimide-cyp3a4)
            'default-inference-assumption)

      ;; always assume! uknowns so they can be retracted should the unknown become known
     (assume! '(1-has-metabolite-2-via-3 '4-hydroxy-cyclophosimide 'phosphoramide-mustard 'unknown) 
                    'default-inference-assumption)

     (assume! '(1-has-metabolite-2-via-3 '4-hydroxy-cyclophosimide 'acrolein 'unknown) 
                   'default-inference-assumption)
     (run-rules)
   
     ;; what of the matching assertions are :IN?
     (not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'ITRACONAZOLE 'ACROLEIN 'CYCLOPHOSIMIDE 'CYP3A4)))
     (not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'ITRACONAZOLE  'PHOSPHORAMIDE-MUSTARD 'CYCLOPHOSIMIDE 'CYP3A4)))
     (not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'ITRACONAZOLE '4-HYDROXY-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP3A4)))

     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP3A4))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP3A4))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'TROLEANDOMYCIN 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP2C9))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'TROLEANDOMYCIN 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP2C9))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'TROLEANDOMYCIN 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP2C9))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'CLOPIDOGREL 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP2B6))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP2B6))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP2B6))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2B6))
     (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2B6))
     (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'TROLEANDOMYCIN 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2C9))
     (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'TROLEANDOMYCIN '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2C9))
     (in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'PHOSPHORAMIDE-MUSTARD 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'ACROLEIN 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS '4-HYDROXY-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
     (in? '(1-INHIBITS-3-THE-PRIMARY-METABOLIC-ENZYME-OF-2 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'CYP2B6))

     ;; TEST 5 - identifying interesting metabolic inhibition facts 
     ;; depends on data and valid of results from TEST 4
     (assume! '(pceut-entity-of-concern 'ACROLEIN) 'dikb-default-assumption)
     (assume! '(pceut-entity-of-concern 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE) 'dikb-default-assumption)

     ;; possibly beneficial
     (get-in-assertions '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM ?x ?y 'ACROLEIN ?enz)) 
     (get-in-assertions '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM ?x ?y 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE ?enz))
     ;; NOTE: we might want to make (1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 ?x ?y) necessary and sufficient for 
     ;;       (1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM ?x ?y)
     (get-in-assertions '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 ?x ?y 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE ?enz))
      
     ;; possibly harmful
     (get-in-assertions '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 ?x 'ACROLEIN ?y ?enz))
     (get-in-assertions '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 ?x 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE ?y ?enz))
 
     ;; killing two or more birds with one stone
     (get-in-assertions '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 ?x 'CYCLOPHOSIMIDE ?y ?enz))

"
 
  (in-jtre (create-jtre "Boyce, R.D. UW PhD TEST-DIKB 'readable' JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(       
		  
		  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  ;; RULES FOR LINKING METABOLITES TO ACTIVE
		  ;; INGREDIENTS AND ANCESTOR COMPOUNDS
		  
		  ;; a rule linking the catalysis of the formation of a
		  ;; metabolite to parent compounds
		  (rule 
		   ((:IN (1-controls-formation-of-2 ?enz ?x))
		    (:IN (1-has-metabolite-2 ?y ?x)))
		   (rassert! 
		    (1-has-metabolite-2-via-3 ?y ?x ?enz)
		    (nil
		     (1-controls-formation-of-2 ?enz ?x)
		     (1-has-metabolite-2 ?y ?x)
		     )))

		  
		  ;; a rule linking ancestor compounds to a metabolite
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?y ?z)))
		   (rassert! 
		    (1-is-ancestor-of-2 ?x ?y)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?y ?z)
		     )))
		  
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?y ?z)))
		   (rassert! 
		    (1-is-substrate-of-2 ?x ?z)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?y ?z)
		     )))
		  
		  ;; a rule linking an ancestor compound to an metabolite
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?y ?e))
		    (:IN (1-is-ancestor-of-2 ?z ?x)))
		   (rassert! 
		    (1-is-ancestor-of-2 ?z ?y)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?y ?e)
		     (1-is-ancestor-of-2 ?z ?x)
		     )))
		  

                  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  ;; A SET OF RULES FOR MODELING THE EFFECT OF
		  ;; INHIBITION THROUGH A METABOLIC TREE; ALL OF THESE
		  ;; ASSUME THAT ALTERNATE CLEARANCE PATHWAYS ARE NOT
		  ;; SATURATED
		  
		  ;; inhibition of the formation of a metabolite
		  ;; upstream affects the formation of all metabolites
		  ;; dowstream
		  (rule 
		   ((:IN (1-inhibits-transformation-of-2-to-3-via-4 ?q ?x ?m1 ?enz))
		    (:IN (1-is-ancestor-of-2 ?m1 ?m2)))
		   (rassert!
		    (1-inhibits-transformation-of-2-to-3-via-4-upstream ?q ?x ?m2 ?enz)
		    (nil
		     (1-inhibits-transformation-of-2-to-3-via-4 ?q ?x ?m1 ?enz)
		     (1-is-ancestor-of-2 ?m1 ?m2)
		     )))

			  
		  ;; if the formation of two different metabolites
		  ;; from the same agent are catalyzed by *different*
		  ;; enzymes then, reducing the clearance of one
		  ;; enzyme will effect an increase in the formation
		  ;; of the other (assuming that there is available
		  ;; unaffected enzyme)
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?m1 ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?x ?m2 ?enz2) :TEST (and (not (equal ?m1 ?m2)) (not (equal ?enz1 ?enz2)))))
		   (assume! (eval (quotize (list 'effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1))) 
		    'default-inference-assumption))
		  
		  (rule 
		   ((:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m1 ?x ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2) :TEST (not (equal ?enz1 ?enz2))))
		   (assume! (eval (quotize (list 'effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1))) 
		    'default-inference-assumption))

		  
		  (rule 
		   ((:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?enz))
		    (:IN (1-inhibits-2 ?q ?enz)))
		   (rassert! 
		    (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m ?x ?enz)
		    (nil
                     (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?enz)
		     (1-inhibits-2 ?q ?enz)
		     )))

		  ;; The effect of an increased formation of a parent
		  ;; compound on some metabolite, X, due to reduced
		  ;; clearance of an alternate pathway is to increase
		  ;; formation of X when the enzymes involved in the
		  ;; formation of X and the alternate pathway are
		  ;; not the same 
		  (rule
		   ((:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2) :TEST (not (equal ?enz1 ?enz2)))
		    (:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1)))
		   (rassert! 
		    (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m2 ?x ?enz1)
		    (nil
		     (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz1)
		     (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2)
		     (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1)
		     )))

		  ;; Ambiguous and non-ambiguous effects are mutually
		  ;; exclusive. Since an unambiguous effect is the
		  ;; default assumption, it is retracted
		  (rule
		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m ?q ?x ?z))
		    (:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?z)))
		   (rretract! (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?z) 
		                   default-inference-assumption))

		  ;; It is a contradiction to have an ambiguous effect and a clearly 
		  ;; identified effect	  
		  (rule
		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m ?q ?x ?z))
		    (:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m ?x ?z)))
		   (contradiction (eval (quotize (list '1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m ?x ?z)))))
		  
		  ;; If the formation of two different metabolites
		  ;; from the same agent are catalyzed by *the same enzyme* 
		  ;; then the effect of inhibiting the enzyme
		  ;; on both metabolites is ambiguous. This is because
		  ;; there is both an increase in parent compound due
		  ;; to removal of one clearance pathway and a
		  ;; decrease in the ability of the enzyme formation
		  ;; of child compound
		  (rule		
		   ((:IN (1-has-metabolite-2-via-3 ?x ?m1 ?z))
		    (:IN (1-has-metabolite-2-via-3 ?x ?m2 ?z) :TEST (not (equal ?m1 ?m2)))
		    (:IN (1-inhibits-2 ?q ?z)))
		   (rassert! 
		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m2 ?q ?x ?z)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?m1 ?z)
		     (1-has-metabolite-2-via-3 ?x ?m2 ?z)
		     (1-inhibits-2 ?q ?z)
		     )))

		  
		  ;; If the effect of reducing the clearance of
		  ;; metabolite is uncertain for a given metabolite,
		  ;; it will be so for all metabolites downstream in
		  ;; the metabolic pathway
		  (rule 
		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m1 ?q ?x ?enz))
		    (:IN (1-is-ancestor-of-2 ?m1 ?m2)))
		   (rassert!
		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m2 ?q ?x ?enz)
		    (nil
		     (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m1 ?q ?x ?enz)
		     (1-is-ancestor-of-2 ?m1 ?m2)
		     )))
		  
		  		  
		  ;; The effect of an increased formation of a parent
		  ;; compound on a metabolite due to reduced clearance
		  ;; of an alternate pathway is unclear if the same
		  ;; enzyme is inhibited in both an alternate pathway
		  ;; and the formation of the metabolite
		  (rule
		   ((:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz)))
		   (rassert! 
		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m2 ?q ?x ?enz)
		    (nil
		     (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz)
		     (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz)
		     )))
		 
		  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
		  ;; A SET OF RULES TO FOR THE DISJUNCTIVE CASE WHERE AN 
		  ;; ACTIVE INGREDIENT IS ANCESTOR TO A COMPOUND THAT INTERACTS
		  ;; WITH ANOTHER ACTIVE INGREDIENT OR METABOLITE 
		  (rule 
		   ((:IN (1-is-an-active-ingredient ?x))
		    (:IN (1-is-ancestor-of-2  ?x ?y))
		    (:IN (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-1-is-ancestor-to-2-and-2-interacts-with-3 ?x ?y ?z)
		    (nil
		     (1-is-an-active-ingredient ?x)
		     (1-is-ancestor-of-2  ?x ?y)
		     (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz)
		     )))
		     
                  (rule 
		   ((:IN (1-is-an-active-ingredient ?x))
		    (:IN (1-is-ancestor-of-2  ?x ?y))
		    (:IN (1-inhibits-metabolic-clearance-of-2-via-3 ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-1-is-ancestor-to-2-and-2-effects-an-interaction-with-3 ?x ?y ?z)
		    (nil
		     (1-is-an-active-ingredient ?x)
		     (1-is-ancestor-of-2  ?x ?y)
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?y ?z ?enz)
		     )))
		  
		  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  ;; A SET OF RULES TO FOR THE DISJUNCTIVE CASE WHERE AN 
		  ;; ACTIVE INGREDIENT IS ANCESTOR TO A COMPOUND THAT IS THE 
		  ;; VICTIM OF AN INTERACTION WITH ANOTHER ACTIVE INGREDIENT 
		  ;; OR METABOLITE
		  (rule 
		   ((:IN (1-is-an-active-ingredient ?x))
		    (:IN (1-is-ancestor-of-2  ?x ?z))
		    (:IN (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-1-is-ancestor-to-2-and-2-is-affected-by-3 ?x ?z ?y)
		    (nil
		     (1-is-an-active-ingredient ?x)
		     (1-is-ancestor-of-2  ?x ?z)
		     (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz)
		     )))
		     
                  (rule 
		   ((:IN (1-is-an-active-ingredient ?x))
		    (:IN (1-is-ancestor-of-2  ?x ?z))
		    (:IN (1-inhibits-metabolic-clearance-of-2-via-3 ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-1-is-ancestor-to-2-and-2-is-affected-by-3 ?x ?z ?y)
		    (nil
		     (1-is-an-active-ingredient ?x)
		     (1-is-ancestor-of-2  ?x ?z)
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?y ?z ?enz)
		     )))

		  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  ;; RULES THAT MODEL METABOLIC INHIBITION
		  
		  ;; a rule for when a metabolic transformation is
		  ;; inhibited by inhibition of a *known*
		  ;; pathway. NOTE: This rule could explicitly ignore
		  ;; inhibition a metabolite's own production itself
		  ;; if a test were added to one of the antecedents:
		  ;; :TEST (not (equal ?q ?y))
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?y ?z))
		    (:IN (1-inhibits-2 ?q ?z)))
		   (rassert! 
		    (1-inhibits-transformation-of-2-to-3-via-4 ?q ?x ?y ?z)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?y ?z)
		     (1-inhibits-2 ?q ?z)
		     )))

		  
		  ;; a rule for when an active ingredient or metabolite, ?x, will 
		  ;; not inhibit the metabolic clearance  of another drug, ?z, 
		  ;; because ?x does not inhibit enzyme ?y's ability to catalyze
		  ;; drug ?z
		  (rule 
		   ((:IN (1-does-not-inhibit-2 ?x ?y))
		    (:IN (1-is-substrate-of-2 ?z ?y))) 	
		   (rassert! 
		    (1-does-not-inhibit-the-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		    (nil
		     (1-does-not-inhibit-2 ?x ?y)
		     (1-is-substrate-of-2 ?z ?y)
		     )))


		  ;; an necessary condition for being an 'in vitro 
		  ;; selective inhibitor' is that the agent is also
		  ;; an inhibitor
		  (rule 
		   ((:IN (1-is-an-in-vitro-selective-inhibitor-of-2 ?x ?y))) 	
		   (rassert! 
		    (1-inhibits-2 ?x ?y)
		    (nil
		     (1-is-an-in-vitro-selective-inhibitor-of-2 ?x ?y)
		     )))
		  
		  ;; Some, possibly negligible, inhibition of
		  ;; metabolic clearance of active ingredient or
		  ;; metabolite ?z by active ingredient or metabolite
		  ;; ?x due to ?x's inhibition of enzyme ?y's ability
		  ;; to catalyze ?z. NOTE: this test ignores cases
		  ;; where a drug inhibits itself
		  (rule 
		   ((:IN (1-inhibits-2 ?x ?y))
		    (:IN (1-is-substrate-of-2 ?z ?y) 
		           :TEST (not (equal ?x ?z)))) 	
		   (rassert! 
		    (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		    (nil
		     (1-inhibits-2 ?x ?y)
		     (1-is-substrate-of-2 ?z ?y)
		     )))


		  ;; A more significant inhibition of metabolic clearance
		  ;; that should lead to a greater *minimum* increase in AUC
		  ;; than the 1-inhibits-metabolic-clearance-of-2-via-3 assertion captures.
		  ;; This models the effect of inhibiting an enzyme that is responsible 
		  ;; for .25 of a drug's total clearance by requiring inhibition of an enzyme
		  ;; responsible for at least .50 of a drug's *metabolic* clearance when that 
		  ;; form of clearance is responsible for at least .50 of the drug's 
		  ;; *total* clearance 
		  (rule
		   ((:IN 
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		         :TEST (not (equal ?x ?z)))
		     (:IN 
		      (primary-total-clearance-mechanism-of-1-is-2 ?z
							 'METABOLIC-CLEARANCE))
		     (:IN 
		      (primary-metabolic-clearance-enzyme-of-1-is-2 ?z ?y)))
		   (rassert!
		    (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?x ?z ?y)
		    (nil
		     ;;justifications
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		     (primary-total-clearance-mechanism-of-1-is-2 ?z
							'METABOLIC-CLEARANCE)
		     (primary-metabolic-clearance-enzyme-of-1-is-2 ?z ?y)
		     ))) 


		  ;; This rule models inhibition of metabolic clearance that should lead to
		  ;; a greater *minimum* increase in AUC than the 
		  ;; 1-inhibits-3-the-primary-metabolic-enzyme-of-2 assertion captures.
		  ;; If one enzyme is responsible for at least .50  of the
		  ;; metabolic clearance of a drug and another drug fully inhibits that enzyme 
		  ;; then, one would expect at least at least a .50 decrease in clearance and, 
		  ;; subsequently, at least a 2-fold increase in AUC.
		  (rule
		   ((:IN 
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		     :TEST (not (equal ?x ?z)))
		     (:IN 
		      (primary-total-clearance-enzyme-of-1-is-2 ?z ?y)))
		   (rassert!
		    (1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y)
		    (nil
		     ;;justifications
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		     (primary-total-clearance-enzyme-of-1-is-2 ?z ?y)
		     )))


		  ;; This rule models inhibition of metabolic clearance that should lead to
		  ;; a greater *maximum* increase in AUC than the inhibit-primary-tot-clearance-enz
		  ;; assertion captures. It predicts a drastic increase in AUC for active
		  ;; ingredients that undergo a high degree first-pass metabolism
		  (rule
		   ((:IN 
		     (1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y))
		    (:IN
		     (first-pass-effect-on-1-is-2 ?z 'HIGH)))
		   (rassert!
		    (met-inhibit-drug-w-high-first-pass ?x ?z ?y)
		    (nil
		     ;;justifications
		     (1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y)
		     (first-pass-effect-on-1-is-2 ?z 'HIGH)
		     )))

		  ;; a rule defining some, possibly negligible, inhibition 
		  ;; of clearance for a pceut-entity-of-concern 
		  (rule
		   ((:IN 
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y))
		    (:IN
		     (1-is-pceut-entity-of-concern ?z)))
		   (rassert!
		    (first-level-metabolic-inhibition-of-pceut-entity-of-concern ?x ?z ?y)
		    (nil
		     ;;justifications
		     (1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		     (1-is-pceut-entity-of-concern ?z)
		     )))

		  ;; rules defining when the inhibition of a pceut-entity-of-concern 
		  ;; clearance should lead to a more significant increase in AUC 
		  ;; than that captured by  level-1-met-inhibit-pceut-entity-of-concern 
		  ;; assertions
		  (rule
		   ((:IN 
		     (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?x ?z ?y))
		    (:IN
		     (1-is-pceut-entity-of-concern ?z)))
		   (rassert!
		    (second-level-metabolic-inhibition-of-pceut-entity-of-concern ?x ?z ?y)
		    (nil
		     ;;justifications
		     (1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?x ?z ?y)
		     (1-is-pceut-entity-of-concern ?z)
		     )))

		  (rule
		   ((:IN 
		     (1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y))
		     (:IN (1-is-pceut-entity-of-concern ?z)))
		    (rassert!
		     (second-level-metabolic-inhibition-of-pceut-entity-of-concern ?x ?z ?y)
		     (nil
		      ;;justifications
		      (1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y)
		      (1-is-pceut-entity-of-concern ?z)
		      )))

		  
		  ;; a rule for that makes it a contradiction for an active ingrediant 
		  ;; or compund to both permanantly and not permanantly deactivate the catalytic
		  ;; function of an enzyme
		  (rule 
		   ((:IN (1-permanently-deactivates-catalytic-function-of-2 ?drug1 ?enzyme)) 
		    (:IN (1-does-not-permanently-deactivate-catalytic-function-of-2 ?drug1 ?enzyme))) 
		   (contradiction
		    (eval (quotize (list
				    '1-does-not-permanently-deactivate-catalytic-function-of-2 ?drug1 ?enzyme))))) 

		  ;; a rule for establishing that an active ingredient or metabolite
		  ;; *does* inhibit an enzyme based on in vitro evidence
		  (rule 
		   ((:IN (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i))  
		    (:IN (1-does-not-permanently-deactivate-catalytic-function-of-2 ?x ?y))
		    (:IN (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max) 
		     :TEST (> (float (/ ?c_max ?k_i )) .1)))
		   (rassert! (1-inhibits-2 ?x ?y) 
		    (nil 
		     ;;justifications
		     (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i)
		     (1-does-not-permanently-deactivate-catalytic-function-of-2 ?x ?y)
		     (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max)
		     (accept-in-vitro-based-enzyme-modulation-assertions)
		     )))

		  
		  ;; a rule for establishing that an active ingredient or metabolite
		  ;; *does not* inhibit an enzyme based on in vitro evidence
		  (rule 
		    ((:IN (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i)) 
		     (:IN (1-does-not-permanently-deactivates-catalytic-function-of-2 ?x ?y))
		     (:IN (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max) 
			  :TEST (<= (float (/ ?c_max ?k_i )) .1)))
		    (rassert! (1-does-not-inhibit-2 ?x ?y) 
		     (nil 
		      ;;justifications
		      (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i)
		      (1-does-not-permanently-deactivates-catalytic-function-of-2 ?x ?y)
		      (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max)
		      (accept-in-vitro-based-enzyme-modulation-assertions)
		      )))
		  ))
    (print (eval form))))


(defun test-dissertation-DIKB-rule-base-ancestor-of ()
  "The rule-base written about in my dissertation --  A simple set of rules about 
   pharmacokinetic drug-drug interactions 

     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))

  Script for first example:
      (load \"load\")
      (test-dissertation-DIKB-rule-base-ancestor-of)
      (assert! '(substrate-of 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (in-vitro-selective-inhibitor-of-enzyme 'diltiazem 'cyp3a4)))
      (assert! '(substrate-of 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (in-vitro-selective-inhibitor-of-enzyme 'ketoconazole 'cyp3a4)))
      (assert! '(inhibits 'itraconazole 'cyp3a4) '('dikb-assertion (bc-satisfied 'inhibits-itraconazole-cyp3a4)))
      (assume! 
         '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
           'default-inference-assumption)
      (assume! 
         '(bc-satisfied 'inhibits-itraconazole-cyp3a4) 
           'default-inference-assumption)
      (assume! 
         '(in-vitro-selective-inhibitor-of-enzyme 'diltiazem 'cyp3a4) 
           'default-inference-assumption)
      (assume! 
         '(in-vitro-selective-inhibitor-of-enzyme 'ketoconazole 'cyp3a4) 
           'default-inference-assumption)
      (run-rules)
      (show-data)
      (retract! 
          '(in-vitro-selective-inhibitor-of-enzyme 'diltiazem 'cyp3a4) 
           'default-inference-assumption)
      (show-data)
      (retract! 
          '(bc-satisfied 'substrate-of-cyp3a4-simvastatin)
           'default-inference-assumption)
      (show-data)

      (assume! 
          '(bc-satisfied 'substrate-of-cyp3a4-simvastatin)
           'default-inference-assumption)
      (assert! '(has-metabolite 'simvastatin 'beta-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)))
      (assert! '(has-metabolite 'beta-hydroxy-simvastatin '6-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)))
      (assume! 
          '(bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)
           'default-inference-assumption)
      (assume! 
          '(bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)
           'default-inference-assumption) 

      (assert! '(substrate-of 'beta-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-beta-hydroxy-simvastatin) (in-vitro-selective-inhibitor-of-enzyme 'ketoconazole 'cyp3a4))) 
      (assume! 
          '(bc-satisfied 'substrate-of-cyp3a4-beta-hydroxy-simvastatin)
           'default-inference-assumption) 
      (assert! '(substrate-of '6-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-6-hydroxy-simvastatin) (in-vitro-selective-inhibitor-of-enzyme 'ketoconazole 'cyp3a4)))
     (assume! 
          '(bc-satisfied 'substrate-of-cyp3a4-6-hydroxy-simvastatin)
           'default-inference-assumption) 
      (run-rules)
      (show-data)
      (fetch '(ancestor-of 'simvastatin ?x))

      (assume! 
          '(active-ingredient 'simvastatin)
           'default-inference-assumption)
      (assume! 
          '(active-ingredient 'itraconazole)
           'default-inference-assumption)
      (run-rules)
      (why? '(ACTIVE-INGREDIENT-ANCESTOR-TO-OBJECT 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN  'ITRACONAZOLE))

      (assume! 
          '(active-ingredient 'cyclophosimide)
           'default-inference-assumption)
      (assert! '(has-metabolite 'cyclophosimide 'a-cyclophosimide 'cyp2c9) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-a-cyclophosimide-cyp2c9)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-a-cyclophosimide-cyp2c9)
            'default-inference-assumption)
      (assert! '(substrate-of 'a-cyclophosimide 'cyp2c9) 
                   '('dikb-assertion (bc-satisfied 'substrate-of-cyp2c9-a-cyclophosimide))) 
      (assume!
          '(bc-satisfied 'substrate-of-cyp2c9-a-cyclophosimide)
            'default-inference-assumption)

      (assert! '(has-metabolite 'cyclophosimide 'b-cyclophosimide 'cyp2c19) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-cyclophosimide-b-cyclophosimide-cyp2c19)))
      (assume!
          '(bc-satisfied 'has-metabolite-cyclophosimide-b-cyclophosimide-cyp2c19)
            'default-inference-assumption)
      (assert! '(substrate-of 'b-cyclophosimide 'cyp2c19) 
                   '('dikb-assertion (bc-satisfied 'substrate-of-cyp2c19-b-cyclophosimide))) 
      (assume!
          '(bc-satisfied 'substrate-of-cyp2c19-b-cyclophosimide)
            'default-inference-assumption)
      

      (assert! '(has-metabolite 'a-cyclophosimide 'a-prime-cyclophosimide 'cyp3a4) 
                   '('dikb-assertion (bc-satisfied 'has-metabolite-a-cyclophosimide-a-prime-cyclophosimide-cyp3a4)))
      (assume!
          '(bc-satisfied 'has-metabolite-a-cyclophosimide-a-prime-cyclophosimide-cyp3a4)
            'default-inference-assumption)
      (assert! '(substrate-of 'a-prime-cyclophosimide 'cyp3a4) 
                   '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-a-prime-cyclophosimide))) 
      (assume!
          '(bc-satisfied 'substrate-of-cyp3a4-a-prime-cyclophosimide)
            'default-inference-assumption)
      (run-rules)
      (show-data)
   
      (assert! '(inhibits 'troleandomycin 'cyp2c9) '('dikb-assertion (bc-satisfied 'inhibits-cyp3a4-troleandomycin)))
      (run-rules)
      (show-data)

      (assume!
          '(bc-satisfied 'inhibits-cyp3a4-troleandomycin)
            'default-inference-assumption)
      (run-rules)
      
  "
  (in-jtre (create-jtre "Boyce, R.D. UW PhD TEST-DIKB 'ancestor-of' JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '( 
		  ;; a rule linking an parent compound to an metabolite
		  (rule 
		   ((:IN (has-metabolite ?x ?y ?z)))
		   (rassert! 
		    (ancestor-of ?x ?y)
		    (nil
		     (has-metabolite ?x ?y ?z)
		     )))
		  
		  ;; a rule linking an ancestor compound to an metabolite
		  (rule 
		   ((:IN (has-metabolite ?x ?y ?e))
		    (:IN (ancestor-of ?z ?x)))
		   (rassert! 
		    (ancestor-of ?z ?y)
		    (nil
		     (has-metabolite ?x ?y ?e)
		     (ancestor-of ?z ?x)
		     )))
		  
		  ;; a rule for when a metabolic transformation is inhibited
		  ;; by inhibition of a *known* pathway
		  (rule 
		   ((:IN (has-metabolite ?x ?y ?z))
		    (:IN (inhibits ?q ?z)))
		   (rassert! 
		    (inhibits-transformation ?q ?x ?y ?z)
		    (nil
		     (has-metabolite ?x ?y ?z)
		     (inhibits ?q ?z)
		     )))
		  
		  ;; a rule for when a metabolic transformation could
		  ;; be increased by inhibiting the clearance of a 
		  ;; ancestor active ingredient or metabolite
		  (rule 
		   ((:IN (ancestor-of ?x ?y))
		    (:IN (inhibit-metabolic-clearance ?q ?x ?enz)))
		   (rassert! 
		    (inhibits-clearance-of-ancestor ?q ?x ?y ?enz)
		    (nil
		     (ancestor-of ?x ?y)
		     (inhibit-metabolic-clearance ?q ?x ?enz)
		     )))
		  
		  ;; a set of rules to for the disjunctive case where an 
		  ;; active ingredient is ancestor to a compound that interacts
		  ;; with another active ingredient or metabolite 
		  (rule 
		   ((:IN (active-ingredient ?x))
		    (:IN (ancestor-of ?x ?y))
		    (:IN (inhibit-primary-enz-of-primary-clearance-mech ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-ancestor-to-precipitant ?x ?y ?z)
		    (nil
		     (active-ingredient ?x)
		     (ancestor-of ?x ?y)
		     (inhibit-primary-enz-of-primary-clearance-mech ?y ?z ?enz)
		     )))
		     
                  (rule 
		   ((:IN (active-ingredient ?x))
		    (:IN (ancestor-of ?x ?y))
		    (:IN (inhibit-metabolic-clearance ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-ancestor-to-precipitant ?x ?y ?z)
		    (nil
		     (active-ingredient ?x)
		     (ancestor-of ?x ?y)
		     (inhibit-metabolic-clearance ?y ?z ?enz)
		     )))
		  
		  ;; a set of rules to for the disjunctive case where an 
		  ;; active ingredient is ancestor to a compound that is the 
		  ;; victim of an interaction with another active ingredient 
		  ;; or metabolite
		  (rule 
		   ((:IN (active-ingredient ?x))
		    (:IN (ancestor-of ?x ?z))
		    (:IN (inhibit-primary-enz-of-primary-clearance-mech ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-ancestor-to-object ?x ?z ?y)
		    (nil
		     (active-ingredient ?x)
		     (ancestor-of ?x ?z)
		     (inhibit-primary-enz-of-primary-clearance-mech ?y ?z ?enz)
		     )))
		     
                  (rule 
		   ((:IN (active-ingredient ?x))
		    (:IN (ancestor-of ?x ?z))
		    (:IN (inhibit-metabolic-clearance ?y ?z ?enz))) 	
		   (rassert! 
		    (active-ingredient-ancestor-to-object ?x ?z ?y)
		    (nil
		     (active-ingredient ?x)
		     (ancestor-of ?x ?z)
		     (inhibit-metabolic-clearance ?y ?z ?enz)
		     )))

		  ;; a rule for when an active ingredient or metabolite, ?x, will 
		  ;; not inhibit the metabolic clearance  of another drug, ?z, 
		  ;; because ?x does not inhibit enzyme ?y's ability to catalyze
		  ;; drug ?z
		  (rule 
		   ((:IN (does-not-inhibit ?x ?y))
		    (:IN (substrate-of ?z ?y))) 	
		   (rassert! 
		    (does-not-inhibit-metabolic-clearance ?x ?z ?y)
		    (nil
		     (does-not-inhibit ?x ?y)
		     (substrate-of ?z ?y)
		     )))


		  ;; Some, possibly negligible, inhibition of metabolic clearance
		  ;; of active ingredient or metabolite ?z by active ingredient or 
		  ;; metabolite ?x due to ?x's inhibition of enzyme ?y's 
		  ;; ability to catalyze ?z.
		  (rule 
		   ((:IN (inhibits ?x ?y))
		    (:IN (substrate-of ?z ?y))) 	
		   (rassert! 
		    (inhibit-metabolic-clearance ?x ?z ?y)
		    (nil
		     (inhibits ?x ?y)
		     (substrate-of ?z ?y)
		     )))


		  ;; A more significant inhibition of metabolic clearance
		  ;; that should lead to a greater *minimum* increase in AUC
		  ;; than the inhibit-metabolic-clearance assertion captures.
		  ;; This models the effect of inhibiting an enzyme that is responsible 
		  ;; for .25 of a drug's total clearance by requiring inhibition of an enzyme
		  ;; responsible for at least .50 of a drug's *metabolic* clearance when that 
		  ;; form of clearance is responsible for at least .50 of the drug's 
		  ;; *total* clearance 
		  (rule
		   ((:IN 
		     (inhibit-metabolic-clearance ?x ?z ?y)
		     :TEST (not (equal ?x ?z))
		     (:IN 
		      (primary-total-clearance-mechanism ?z
							 'METABOLIC-CLEARANCE))
		     (:IN 
		      (primary-metabolic-clearance-enzyme ?z ?y))))
		   (rassert!
		    (inhibit-primary-enz-of-primary-clearance-mech ?x ?z ?y)
		    (nil
		     ;;justifications
		     (inhibit-metabolic-clearance ?x ?z ?y)
		     (primary-total-clearance-mechanism ?z
							'METABOLIC-CLEARANCE)
		     (primary-metabolic-clearance-enzyme ?z ?y)
		     ))) 


		  ;; This rule models inhibition of metabolic clearance that should lead to
		  ;; a greater *minimum* increase in AUC than the 
		  ;; inhibit-primary-enz-of-primary-clearance-mech assertion captures.
		  ;; If one enzyme is responsible for at least .50  of the
		  ;; metabolic clearance of a drug and another drug fully inhibits that enzyme 
		  ;; then, one would expect at least at least a .50 decrease in clearance and, 
		  ;; subsequently, at least a 2-fold increase in AUC.
		  (rule
		   ((:IN 
		     (inhibit-metabolic-clearance ?x ?z ?y)
		     :TEST (not (equal ?x ?z))
		     (:IN 
		      (primary-total-clearance-enzyme ?z ?y))))
		   (rassert!
		    (inhibit-primary-tot-clearance-enz ?x ?z ?y)
		    (nil
		     ;;justifications
		     (inhibit-metabolic-clearance ?x ?z ?y)
		     (primary-total-clearance-enzyme ?z ?y)
		     )))


		  ;; This rule models inhibition of metabolic clearance that should lead to
		  ;; a greater *maximum* increase in AUC than the inhibit-primary-tot-clearance-enz
		  ;; assertion captures. It predicts a drastic increase in AUC for active
		  ;; ingredients that undergo a high degree first-pass metabolism
		  (rule
		   ((:IN 
		     (inhibit-primary-tot-clearance-enz ?x ?z ?y))
		    (:IN
		     (first-pass-effect ?z 'HIGH)))
		   (rassert!
		    (met-inhibit-drug-w-high-first-pass ?x ?z ?y)
		    (nil
		     ;;justifications
		     (inhibit-primary-tot-clearance-enz ?x ?z ?y)
		     (first-pass-effect ?z 'HIGH)
		     )))

		  ;; a rule defining some, possibly negligible, inhibition 
		  ;; of clearance for a drug-of-concern 
		  (rule
		   ((:IN 
		     (inhibit-metabolic-clearance ?x ?z ?y))
		    (:IN
		     (drug-of-concern ?z)))
		   (rassert!
		    (level-1-met-inhibit-drug-of-concern ?x ?z ?y)
		    (nil
		     ;;justifications
		     (inhibit-metabolic-clearance ?x ?z ?y)
		     (drug-of-concern ?z)
		     )))

		  ;; rules defining when the inhibition of a drug-of-concern 
		  ;; clearance should lead to a more significant increase in AUC 
		  ;; than that captured by  level-1-met-inhibit-drug-of-concern 
		  ;; assertions
		  (rule
		   ((:IN 
		     (inhibit-primary-enz-of-primary-clearance-mech ?x ?z ?y))
		    (:IN
		     (drug-of-concern ?z)))
		   (rassert!
		    (level-2-met-inhibit-drug-of-concern ?x ?z ?y)
		    (nil
		     ;;justifications
		     (inhibit-primary-enz-of-primary-clearance-mech ?x ?z ?y)
		     (drug-of-concern ?z)
		     )))

		  (rule
		   ((:IN 
		     (inhibit-primary-tot-clearance-enz ?x ?z ?y))
		     (:IN (drug-of-concern ?z)))
		    (rassert!
		     (level-2-met-inhibit-drug-of-concern ?x ?z ?y)
		     (nil
		      ;;justifications
		      (inhibit-primary-tot-clearance-enz ?x ?z ?y)
		      (drug-of-concern ?z)
		      )))

		   ;; a rule for establishing that an active ingredient or metabolite
		   ;; *does* inhibit an enzyme based on in vitro evidence
		   (rule 
		    ((:IN (inhibition-constant ?x ?y ?k_i))  
		     (:IN (competitive-inhibitor ?x ?y))
		     (:IN (maximum-concentration ?x ?c_max) 
			  :TEST (> (float (/ ?c_max ?k_i )) .1)))
		    (rassert! (inhibits ?x ?y) 
		     (nil 
		      ;;justifications
		      (inhibition-constant ?x ?y ?k_i)
		      (competitive-inhibitor ?x ?y)
		      (maximum-concentration ?x ?c_max)
		      (accept-in-vitro-based-enzyme-modulation-assertions)
		      )))

		   ;; a rule for establishing that an active ingredient or metabolite
		   ;; *does not* inhibit an enzyme based on in vitro evidence
		   (rule 
		    ((:IN (inhibition-constant ?x ?y ?k_i)) 
		     (:IN (competitive-inhibitor ?x ?y))
		     (:IN (maximum-concentration ?x ?c_max) 
			  :TEST (<= (float (/ ?c_max ?k_i )) .1)))
		    (rassert! (does-not-inhibit ?x ?y) 
		     (nil 
		      ;;justifications
		      (inhibition-constant ?x ?y ?k_i)
		      (competitive-inhibitor ?x ?y)
		      (maximum-concentration ?x ?c_max)
		      (accept-in-vitro-based-enzyme-modulation-assertions)
		      )))
		  
		  ;; a rule for that makes it a contradiction for an active ingrediant 
		  ;; or metabolite to both inhibit and not inhibit the catalytic
		  ;; function of an enzyme
		  (rule 
		   ((:IN (1-inhibits-2 ?x ?y)) 
		    (:IN (1-does-not-inhibit-2 ?x ?y))) 
		   (contradiction
		    (eval (quotize (list
				    '1-does-not-inhibit-2 ?drug1 ?enzyme))))) 
		  
		  ))
    (print (eval form))))


(defun ieee-demo-rule-base ()
    "The rule-base written about in the IEEE TITB submission 10/18/2005.
    A simple set of rules about pharmacokinetic drug-drug interactions
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))

  Script for first example:
     * (load \"load\")
     * (ieee-demo-rule-base)
     * (assert! '(inhibits 'CMYN 'CYP3A4) 'dikb-assertion)
     * (assert! '(substrate-of 'CARB 'CYP3A4) 'dikb-assertion)
     * (assume!
         '(inhibitory-concentration 'CMYN 'CYP3A4)  
           'default-inference-assumption)
     * (run-rules)
     * (show-data)
     * (retract! 
        '(inhibitory-concentration 'CMYN 'CYP3A4)  
         'default-inference-assumption)
     * (show-data)
  "
  (in-jtre (create-jtre "IEEE-TITB 10182005 JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(                
                  (rule ((:IN (inhibits ?x ?y))
                         (:IN (substrate-of ?z ?y))) 	
                        (rassert! (inhibit-metabolic-clearance ?x ?z ?y)
                                  ;;justifications
                                  (nil
                                   (inhibits ?x ?y)
                                   (substrate-of ?z ?y)
                                   (inhibitory-concentration ?x ?y))))
                                    
                  (rule ((:IN (inhibit-metabolic-clearance ?x ?z ?y) :TEST (not (equal ?x ?z))))
                        (rassert! (increase-drug-exposure ?x ?z ?y)
                                  ;;justifications
                                  (nil
                                   (inhibit-metabolic-clearance ?x ?z ?y)
                                   (primary-clearance-mechanism ?z 'METABOLISM))))

                  (rule ((:IN (narrow-therapeutic-range ?z)))
                        (rassert!  (nti-or-sensitive-substrate ?z)
                                   ;;justifications
                                   (nil
                                    (narrow-therapeutic-range ?z))))
                  
                  (rule ((:IN (sensitive-substrate ?z ?y)))
                        (rassert!  (nti-or-sensitive-substrate ?z)
                                   ;;justifications
                                   (nil
                                    (sensitive-substrate ?z ?y))))
                                                                                        
                  (rule ((:IN (increase-drug-exposure ?x ?z ?y))
                         (:IN (primary-clearance-enzyme ?z ?y))
                         (:IN (nti-or-sensitive-substrate ?z)))
                        (rassert! (metabolic-inhibition-interaction ?x ?z ?y)
                                  ;;justifications
                                  (nil
                                   (increase-drug-exposure ?x ?z ?y)
                                   (primary-clearance-enzyme ?z ?y)
                                   (nti-or-sensitive-substrate ?z)
                                   )))

                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions generated by the DIKB:~%")
                  (load "./assertions.lisp")
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with NO enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                  (format t "~%~%prescribe: Assuming that currently accounts for more than half clearance ~A :~%" 'simvastatin)
                  (assume! '(inhibitory-concentration 'diltiazem 'cyp3a4)  'test-inference-assumption)
                  (assume! '(inhibitory-concentration 'FLUVASTATIN 'cyp2c9)  'test-inference-assumption)
                  (run-rules)      
                  ))
    (print (eval form))))


(defun test-rules-1 ()
   (in-jtre (create-jtre "TEST 1 JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(
		  (ieee-demo-rule-base)
		  (rule ((:IN (inhibits ?x ?y))
			 ) 	
			(assume! (eval (quotize (list 'competitive-inhibitor ?x ?y))) 'DIKB-default-assertion))
		  
		  (rule 
		   ((:IN (permanent-inhibitor ?drug1 ?enzyme)) 
		    (:IN (competitive-inhibitor ?drug1 ?enzyme))) 
		   (rretract! (competitive-inhibitor ?drug1 ?enzyme) DIKB-default-assertion) 
		   )
		  (run-rules)
		  (show-data)
		  (assume! '(permanent-inhibitor 'DILTIAZEM 'CYP3A4) 'test-inference-assumption)
		  (run-rules)
		  (show-data)
		  ))))


(defun patient-specific-rule-base ()
  "A simple set of rules about pharmacokinetic drug-drug interactions
   that models patient state.
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))
  "
  (setq t-jtre (create-jtre "Simple DDI JTRE" :DEBUGGING t))
  (in-jtre t-jtre)
  (dolist (form '(                
                  (rule ((:IN (inhibits ?precip ?enz))
                         (:IN (substrate-of ?object ?enz))) 	
                        (rassert! (inhibit-clearance ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibits ?precip ?enz)
                                   (substrate-of ?object ?enz)
                                   (sufficient-concentration-to-inhibit ?precip ?enz)
                                   (saturable-concentration ?precip ?enz))))
                                    
                  (rule (( :IN (inhibit-clearance ?precip ?object ?enz)))
                        (rassert! (increase-bioavailability ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibit-clearance ?precip ?object ?enz)
                                   (given-when-object-near-steady-state ?precip ?object)
                                   (currently-accounts-for-more-than-half-clearance ?enz ?object))))

                  (rule (( :IN (increase-bioavailability ?precip ?object ?enz)))
                        (rassert! (toxic-effect ?precip ?object)
                                  ;;justifications
                                  (nil
                                   (increase-bioavailability ?precip ?object ?enz)
                                   (currently-near-toxic-dose ?object))))
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions specific to patient simulation:~%")
                  (load "./patient-assertions.lisp")  ;;this assertion file does not include the default assumptions for each assertion
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with NO enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                        
                  ))
    (print (eval form)))
  t-jtre)


(defun test-negation ()
  (in-jtre (create-jtre "IEEE-" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(                
                  (rule ((:IN (narrow-therapeutic-range ?z)))
                        (rassert!  (nti-or-high-first-pass ?z)
                                   ;;justifications
                                   (nil
                                    (:IN (narrow-therapeutic-range ?z)))))
                  
                  (rule ((:IN (level-of-first-pass ?z 'MORE_THAN_HALF)))
                        (rassert!  (nti-or-high-first-pass ?z)
                                   ;;justifications
                                   (nil
                                    (:IN (level-of-first-pass ?z 'MORE_THAN_HALF)))))
                  
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions generated by the DIKB:~%")
                  (load "./assertions.lisp")
                  ))
    (print (eval form))))


(defun load-demo-rule-base ()
  "A simple set of rules about pharmacokinetic drug-drug interactions
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))
  "
  (in-jtre (create-jtre "Simple DDI JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(                
                  (rule ((:IN (inhibits ?precip ?enz))
                         (:IN (substrate-of ?object ?enz))) 	
                        (rassert! (inhibit-clearance ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibits ?precip ?enz)
                                   (substrate-of ?object ?enz)
                                   (sufficient-concentration-to-inhibit ?precip ?enz)
                                   (saturable-concentration ?precip ?enz))))
                                    
                  (rule (( :IN (inhibit-clearance ?precip ?object ?enz)))
                        (rassert! (increase-bioavailability ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibit-clearance ?precip ?object ?enz)
                                   (given-when-object-near-steady-state ?precip ?object)
                                   (currently-accounts-for-more-than-half-clearance ?enz ?object))))

                  (rule (( :IN (increase-bioavailability ?precip ?object ?enz)))
                        (rassert! (toxic-effect ?precip ?object)
                                  ;;justifications
                                  (nil
                                   (increase-bioavailability ?precip ?object ?enz)
                                   (currently-near-toxic-dose ?object))))
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions generated by the DIKB:~%")
                  (load "./assertions.lisp")
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with NO enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                  (format t "~%~%prescribe: Assuming that currently accounts for more than half clearance ~A :~%" 'simvastatin)
                  (assume! '(currently-accounts-for-more-than-half-clearance  'cyp3a4 'simvastatin)  'test-inference-assumption)
                        
                  ))
    (print (eval form))))

(defun patient-specific-rule-base ()
  "A simple set of rules about pharmacokinetic drug-drug interactions
   that models patient state.
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))
  "
  (setq t-jtre (create-jtre "Simple DDI JTRE" :DEBUGGING t))
  (in-jtre t-jtre)
  (dolist (form '(                
                  (rule ((:IN (inhibits ?precip ?enz))
                         (:IN (substrate-of ?object ?enz))) 	
                        (rassert! (inhibit-clearance ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibits ?precip ?enz)
                                   (substrate-of ?object ?enz)
                                   (sufficient-concentration-to-inhibit ?precip ?enz)
                                   (saturable-concentration ?precip ?enz))))
                                    
                  (rule (( :IN (inhibit-clearance ?precip ?object ?enz)))
                        (rassert! (increase-bioavailability ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibit-clearance ?precip ?object ?enz)
                                   (given-when-object-near-steady-state ?precip ?object)
                                   (currently-accounts-for-more-than-half-clearance ?enz ?object))))

                  (rule (( :IN (increase-bioavailability ?precip ?object ?enz)))
                        (rassert! (toxic-effect ?precip ?object)
                                  ;;justifications
                                  (nil
                                   (increase-bioavailability ?precip ?object ?enz)
                                   (currently-near-toxic-dose ?object))))
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions specific to patient simulation:~%")
                  (load "./patient-assertions.lisp")  ;;this assertion file does not include the default assumptions for each assertion
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with NO enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                        
                  ))
    (print (eval form)))
  t-jtre)


(defun test-ddi-rule-base ()
  "A simple set of rules about pharmacokinetic drug-drug interactions
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))
  "
  (in-jtre (create-jtre "Simple DDI JTRE" :DEBUGGING t))
  (defvar *jtre* in-jtre)
  (dolist (form '(                
                  (rule ((:IN (inhibits ?precip ?enz))
                         (:IN (substrate-of ?object ?enz))) 	
                        (rassert! (inhibit-clearance ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibits ?precip ?enz)
                                   (substrate-of ?object ?enz)
                                   (sufficient-concentration-to-inhibit ?precip ?enz)
                                   (saturable-concentration ?precip ?enz))))
                                    
                  (rule (( :IN (inhibit-clearance ?precip ?object ?enz)))
                        (rassert! (increase-bioavailability ?precip ?object ?enz)
                                  ;;justifications
                                  (nil
                                   (inhibit-clearance ?precip ?object ?enz)
                                   (given-when-object-near-steady-state ?precip ?object)
                                   (currently-accounts-for-more-than-half-clearance ?enz ?object))))

                  (rule (( :IN (increase-bioavailability ?precip ?object ?enz)))
                        (rassert! (toxic-effect ?precip ?object)
                                  ;;justifications
                                  (nil
                                   (increase-bioavailability ?precip ?object ?enz)
                                   (currently-near-toxic-dose ?object))))
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Loading enabled assumptions generated by the DIKB:~%")
                  (load "./assertions.lisp")
                   (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with currently enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                  
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Creating enabled assumptions:~%")
                  (assume! '(given-when-object-near-steady-state 'diltiazem 'simvastatin) 'test-inference-assumption)
                  (assume! '(currently-accounts-for-more-than-half-clearance  'cyp3a4 'simvastatin)  'test-inference-assumption)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Do we believe that diltiazem will cause a toxic ddi with simvastatin? ~%~A"
                          (cond ((in? '(TOXIC-EFFECT 'DILTIAZEM 'SIMVASTATIN)) t)
                                (t nil)))
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
                  
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Creating enabled assumptions:~%")
                  (assume! '(currently-near-toxic-dose   'simvastatin)  'test-inference-assumption)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with currently enabled assumptions:~%")
                  (run-rules)
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Do we believe that diltiazem will cause a toxic ddi with simvastatin? ~%~A"
                          (cond ((in? '(TOXIC-EFFECT 'DILTIAZEM 'SIMVASTATIN)) t)
                                (t nil)))
                  
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
                  (show-data)
          
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Why are the following assertions believed?: ~%~A ~%~%~A."
                          (why? '(INCREASE-BIOAVAILABILITY 'DILTIAZEM 'SIMVASTATIN 'CYP3A4))
                          (why? '(TOXIC-EFFECT 'DILTIAZEM 'SIMVASTATIN)))

                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Show the 'well founded support' for these assertions: ~%~A ~~%%~A."
                          (wfs '(INCREASE-BIOAVAILABILITY 'DILTIAZEM 'SIMVASTATIN 'CYP3A4))
                          (wfs '(TOXIC-EFFECT 'DILTIAZEM 'SIMVASTATIN)))

                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Retracting an enabled assumption from the DIKB:~%")
                  (retract! '(sufficient-concentration-to-inhibit 'diltiazem 'cyp3a4) 'dikb-enabled-assumption)

                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Do we now believe that diltiazem will cause a toxic ddi with simvastatin? ~%~A"
                          (cond ((in? '(TOXIC-EFFECT 'DILTIAZEM 'SIMVASTATIN)) t)
                                (t nil)))
                                    
                  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine, notice that there is a change in what was believed:~%")
                  (show-data)

                  ))
    (print (eval form))))



(defun first-ddi-rule-base ()
  "A simple set of rules about pharmacokinetic drug-drug interactions
     Assertions and  assumptions will come in from the DIKB in the form:
        (assume! '(drug-at-sufficient-concentration-to-inhibit 'precipitant 'enzyme))
      and
        (assert! '(inhibits 'precipitant 'enzyme))
  "
  (in-jtre (create-jtre "Simple DDI JTRE" :DEBUGGING t))
  (dolist (form '(
                  (rule ((:IN (inhibits ?precip ?enz))
                         (:IN (substrate-of ?object ?enz))) 	
                        (rassert! (:IN (inhibit-clearance ?precip ?object)) 
                                  ;;justifications
                                  (nil (inhibits ?precip ?enz)
                                       (substrate-of ?object ?enz)
                                       )))
                                    
                  (rule (( :IN (inhibit-clearance ?precip ?object)))
                        (rassert! (:IN (increase-auc ?precip ?object))
                                  ;;justifications
                                  (nil (inhibit-clearance ?precip ?object)
                                       )))

                  (rule (( :IN (increase-auc ?precip ?object )))
                        (rassert! (toxic-effect ?precip ?object)
                                  ;;justifications
                                  (nil (increase-auc ?precip ?object ?enz)
                                       )))
                  (load "./assertions.lisp")
                  (run-rules)
                  ))
    (print (eval form))))


(defun my-getenv (name &optional default)
  "Get environment variable"
  #+CMU
  (let ((x (assoc name ext:*environment-list*
                  :test #'string=)))
    (if x (cdr x) default))
  #-CMU
  (or
   #+Allegro (sys:getenv name)
   #+CLISP (ext:getenv name)
   #+ECL (si:getenv name)
   #+SBCL (sb-unix::posix-getenv name)
   #+LISPWORKS (lispworks:environment-variable name)
   default))

(defun explanation (fact f-name &optional (*JTRE* *JTRE*))
  ;; write well-founded support for a fact to html
  (with-open-file (str f-name
                     :direction :OUTPUT
                     :if-exists :OVERWRITE
                     :if-does-not-exist :CREATE)
                  (let ((*standard-output* str))
                    (cond ((out? fact) (format str "~% ~A is OUT." fact))
                          (t (format str "<p><tt><br>")
                             (do ((queue (list (get-tms-node fact))
                                         (nconc (cdr queue) new-antes))
                                  (so-far (list (get-tms-node fact)))
                                  (new-antes nil nil))
                                 ((null queue) (format str "<br>--------<br>") fact (format str "</tt></p>"))
                               (format str "<br><br>")
                               (why-node (car queue))
                             
                               (unless (or (out-node? (car queue))
                                           (tms-node-assumption? (car queue)))
                                 ;; Go down the support
                                 (dolist (ante (just-antecedents
                                                (tms-node-support (car queue))))
                                   (unless (member ante so-far)
                                     (push ante so-far)
                                     (push ante new-antes))))
                               (if (tms-node-assumption? (car queue))
                                   (cond ((equal (datum-assumption? (tms-node-datum (car queue))) 'TEST-INFERENCE-ASSUMPTION)
                                          (format str "<br>This assumption is enabled by default reasoning, you can retract this assumption by entering:<br> (retract! '~A 'TEST-INFERENCE-ASSUMPTION))" (node-string (car queue))))
                                         ;;(t
                                         ;; (let ((link (car (datum-assumption? (tms-node-datum (car queue))))))
                                         ;;  (format str "<br>This assumption was asserted by the evidence base. You can find out more about  this assertion and it's default assumptions :<br> <a target=\"new\" href=\"~A\">here</a>" link)))
                                         ))))))))


(defun prescribe (patient new-drg)
  (dolist (drug (cadr patient))
    ;;enable assumptions
    (format t "~%~%prescribe: Assuming that ~A given when ~A is near steady state:~%" new-drg drug)
    (assume! (eval (list 'QUOTE (cons 'given-when-object-near-steady-state (list (list 'QUOTE new-drg) (list 'QUOTE  drug))))) 'test-inference-assumption)
    (format t "~%~%prescribe: Assuming that ~A is currently near toxic dose :~%" drug)
    (assume! (eval (list 'QUOTE (cons 'currently-near-toxic-dose (list (list 'QUOTE drug))))) 'test-inference-assumption)
    
    (format t "~%~%SIMPLE-DDI-RULE-BASE: Result of running rules with CURRENTLY enabled assumptions:~%")
    (run-rules)
    
    (let ((toxic-l (fetch (eval (list `QUOTE (cons 'toxic-effect (list (list 'QUOTE new-drg) (list 'QUOTE drug)))))))
          (cnt 1))
      (if (not (null toxic-l))
          (dolist (inter toxic-l)
            (cond ((in? (eval (list `QUOTE (cons 'toxic-effect (list (list 'QUOTE new-drg) (list 'QUOTE drug))))))
                   (let ((f-name (concatenate 'string "ddi-" (format nil "~A.html" cnt))))
                     (format t "~%Interaction between ~A and ~A, please see ~A for details"
                             new-drg drug f-name)
                     (explanation inter f-name)
                     (= cnt (+ cnt 1))))
                  (t (format t "~%No interaction believed between ~A and ~A."
                             new-drg drug))))))
    ;; retract assumptions
 ;;   (format t "~%~%prescribe: Retracting assumption that ~A given when ~A is near steady state:~%" new-drg drug)
 ;;   (retract! (eval (list 'QUOTE (cons 'given-when-object-near-steady-state (list (list 'QUOTE new-drg) (list 'QUOTE  drug))))) 'test-inference-assumption)
 ;;   (format t "~%~%prescribe: Retracting assumption that ~A is currently near toxic dose :~%" drug)
 ;;   (retract! (eval (list 'QUOTE (cons 'currently-near-toxic-dose (list (list 'QUOTE drug))))) 'test-inference-assumption)
    ))
            


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Demonstration ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;(load-demo-rule-base)
;;(setq patient '(joe (simvastatin tylenol)))
;; (prescribe patient 'diltiazem)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Scratch ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


		  
; 		  ;; a rule for when a metabolic transformation could
; 		  ;; be increased by inhibiting the clearance of a 
; 		  ;; ancestor active ingredient or metabolite
; 		  (rule 
; 		   ((:IN (1-is-ancestor-of-2  ?x ?y))
; 		    (:IN (1-inhibits-metabolic-clearance-of-2-via-3 ?q ?x ?enz)))
; 		   (rassert! 
; 		    (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y ?enz)
; 		    (nil
; 		     (1-is-ancestor-of-2  ?x ?y)
; 		     (1-inhibits-metabolic-clearance-of-2-via-3 ?q ?x ?enz)
; 		     )))

; 		  ;; rules to classify an increase in a metabolite caused by a
; 		  ;; decrease in the clearance of an ancestor 
; 		  (rule 
; 		   ((:IN (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y1 ?enz))
; 		    (:IN (1-inhibits-transformation-of-2-to-3-via-4 ?q ?x ?y2 ?enz))
; 		    (:IN (1-is-ancestor-of-2 ?y2 ?y1)))
; 		   (rassert!
; 		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?y1 ?q ?x ?enz)
; 		    (nil
; 		     (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y1 ?enz)
; 		     (1-inhibits-transformation-of-2-to-3-via-4 ?q ?x ?y2 ?enz)
; 		     (1-is-ancestor-of-2 ?y2 ?y1)
; 		     )))

		  
; 		  ;; a method for tracking the effect of inhibition on
; 		  ;; a single point in a pathway vs multiple parts
; 		  ;; of a pathway by a single inhibitor
; 		  (rule 
; 		    ((:IN (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y ?enz)))
; 		    (assume! (eval (quotize (list '1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?y ?x ?enz))) 
; 		                'default-inference-assumption)
; 		   )
		  
; 		  (rule 
; 		    ((:OUT (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y ?enz)))
; 		    (rretract! (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?y ?x ?enz) default-inference-assumption)
; 		    )

; 		  (rule 
; 		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?y ?q ?x ?enz)))
;  		   (rretract! (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?y ?x ?enz) default-inference-assumption)
; 		   )



		  ;; an alternative method for tracking the effect of inhibition of multiple parts 
		  ;;of a pathway by a single inhibitor. This  seemed too complicated of a 
		  ;; representation that would be difficult to manage	  
; 		  (rule 
; 		    ((:IN (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y ?enz)))
; 		    (rassert!
; 		     (1-effects-an-increase-in-2 ?q ?y) 
; 		     (nil
; 		      (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y ?enz)
; 		      (1-does-not-affect-the-transformation-of-2-to-3 ?q ?x ?y)
; 		      )))

; 		   (rule 
; 		    ((:IN (1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 ?q ?x ?y1 ?enz)))
; 		    (assume! (eval (quotize (list '1-does-not-affect-the-transformation-of-2-to-3 ?q ?x ?y))) 
; 		                'default-inference-assumption)
; 		    )
;		  
; 		  (rule 
; 		    ((:IN (1-effects-an-ambiguous-increase-in-2 ?q ?y))
; 		     (:IN (1-effects-an-increase-in-2 ?q ?y)))
; 		   (rretract! (1-does-not-affect-the-transformation-of-2-to-3 ?q ?x ?y) default-inference-assumption)
; 		   )
	
		  
;       ;; TEST 4: a simple test of a method for tracking the effect of inhibition on
;       ;; a single point in a pathway vs multiple parts
;       ;; of a pathway by a single inhibitor.
;       ;; no dependencies
;       (TEST-DISSERTATION-DIKB-RULE-BASE-READABLE)
;       (assert! '(1-inhibits-4-reducing-the-clearance-of-2-an-ancestor-to-3 'd1 'd2 'm1 'enz1)  '('dikb-assertion))
;       (run-rules)
;       (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-via-4 'D1 'M1 'D2 'ENZ1))

;       (assume! '(effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous 'm1 'd1 'd2 'enz1) 'dikb-default-assertion)
;       (run-rules)
;       (not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-via-4 'D1 'M1 'D2 'ENZ1)))

