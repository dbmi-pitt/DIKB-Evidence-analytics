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
;; File:      test-dissertation-dikb.lisp

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

(defun replace-all (string part replacement &key (test #'char=))
  "Returns a new string in which all the occurences of the part 
   is replaced with replacement. 
   - published online at http://cl-cookbook.sourceforge.net/strings.html
   
   @param string:string - the string in which replacements will be placed
   @param part:string - the target for replacement
   @param replacement:string - the replacement string
   @returns: string with replacement"
  (with-output-to-string (out)
    (loop with part-length = (length part)
	for old-pos = 0 then (+ pos part-length)
	for pos = (search part string
			  :start2 old-pos
			  :test test)
	do (write-string string out
			 :start old-pos
			 :end (or pos (length string)))
	when pos do (write-string replacement out)
	while pos))) 
 
(defun trnslt-asrt (asrt)
  "Translate the lisp form of an assertion into a plain english string"
  (let ((cls (string (car asrt)))
	(vrs (cdr asrt))
	(i 0))
    (if (string-equal cls "BC-SATISFIED")
	(setf cls (concatenate 'string  (string (car asrt)) " " (string (car (cdr (nth 1 asrt))))))
      (progn
	(dolist (el vrs)
	  (setf i (+ i 1))
	  (let ((st  (car (cdr el))))
	    (if (not (null st))
		(setf cls (replace-all cls (string (digit-char i)) (format nil "~A" st))))))))
    (setf cls (replace-all cls "-" " "))
    cls))
	     

(defun wfs-html (ptrn cls)
  "Gather a plain english representation of the support for an assertion into a html formatted string"
  (setf out "")
  (let ((asrt_l (get-in-assertions ptrn)))
    (dolist (a asrt_l)
      (let ((support (tms-node-support (get-tms-node a))))
	(if (eq support :ENABLED-ASSUMPTION)
	    (setf out (concatenate 'string out (format nil "~%<TR><TD>~A</TD></TR>" (node-string (get-tms-node a)))))
	  (progn
	    (let ((j-a-l (just-antecedents support))
		  (eng-a (trnslt-asrt a)))
	      (setf out (concatenate 'string out (format nil "~%<TR><TD>~A</TD><TD>~A</TD><TD>" cls eng-a)))
	      (dolist (j j-a-l)
		(setf out (concatenate 'string out (format nil "~A, " (trnslt-asrt (view-node j))))))
	      (setf out (concatenate 'string out (format nil "</TD></TR><BR>")))
	      ))))))
  out)

(defun data-to-html (&optional (*JTRE* *JTRE*)
			       (stream *standard-output*))
  "output all :IN assertions to a file for processing into an HTML page"
  (setf path (make-pathname :name "inference-results" ))
  (setf str (open path :direction :output 
		  :if-exists :supersede))
  (map-dbclass
   #'(lambda (dbclass)
       (setf out "")
       (dolist (datum (dbclass-facts dbclass))
	 (if (in-node? (datum-tms-node datum))
	     (let ((lfrm (datum-lisp-form datum)))
	       (cond ((member lfrm PKI-1 :test #'equal)
		      (setf out (concatenate 'string out (wfs-html lfrm "PKI-1"))))
		     ((member lfrm PKI-2 :test #'equal)
		      (setf out (concatenate 'string out (wfs-html lfrm "PKI-2"))))
		     ((member lfrm PKI-3 :test #'equal)
		      (setf out (concatenate 'string out (wfs-html lfrm "PKI-3"))))
		     ((member lfrm NO-PKI :test #'equal)
		      (setf out (concatenate 'string out (wfs-html lfrm "NO-PKI"))))
		     (t
		      (setf out (concatenate 'string out (wfs-html lfrm "Z"))))
		     )
	       )))
       (format str "~A" out)
       ))
  (close str)
  )


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; RULE BASE

(defun test-dissertation-DIKB-rule-base-simple-met ()
  "The rule-base written about in my dissertation --  A simple set of rules about 
   pharmacokinetic drug-drug interactions 
 
     (load \"load\")
     (simple-dikb-rule-engine)
 "
 
  (in-jtre (create-jtre "Boyce, R.D. UW PhD TEST-DIKB 'simple-met' JTRE" :DEBUGGING t))
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

			  
		  ;; if the formation of two different metabolites, M1
		  ;; and M2, from the same agent, X, is catalyzed by
		  ;; *different* enzymes then, the effect on M2 of
		  ;; modulating the clearance of X by inhibiting or
		  ;; inducing the catalytic function of one of the
		  ;; enzymes will be an non-ambiguous increase or
		  ;; decrease
		  (rule 
		   ((:IN (1-has-metabolite-2-via-3 ?x ?m1 ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?x ?m2 ?enz2) 
		     :TEST (and (not (equal ?m1 ?m2)) 
				(not (equal ?enz1 ?enz2)) 
				(not (equal ?enz1 'UNKNOWN)))))
		   (assume! (eval (quotize (list 'effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1))) 
		    'default-inference-assumption))
		  
		  ;; If the effect on some metabolite, M1, of
		  ;; modulating the clearance of its parent compound,
		  ;; X, by inhibiting or inducing the catalytic
		  ;; function of some enzyme, E, is an unambiguous
		  ;; increase or decrease and if M1 has a metabolite,
		  ;; M2, and the transformation of M1 to M2 is
		  ;; controlled by a different enzyme than E then,
		  ;; then an increase or decrease in X will effect an
		  ;; non-ambiguouse increase M2
		  (rule 
		   ((:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m1 ?x ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2) 
		     :TEST (and (not (equal ?enz1 ?enz2)) 
				(not (equal ?enz1 'UNKNOWN)))))
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
		  ;; compound, X, on some metabolite, M1, due to
		  ;; reduced clearance by an alternate pathway is to
		  ;; increase formation of M2 when the enzymes
		  ;; involved in the formation of M1 and M2 are both
		  ;; different then the enzyme whose inhibition caused
		  ;; an increase in X
		  (rule
		   ((:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz1))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2) 
		     :TEST (and (not (equal ?enz1 ?enz2))
				(not (equal ?enz1 'UNKNOWN))))
		    (:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1)))
		   (rassert! 
		    (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m2 ?x ?enz1)
		    (nil
		     (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz1)
		     (1-has-metabolite-2-via-3 ?m1 ?m2 ?enz2)
		     (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m2 ?x ?enz1)
		     )))

		  ;; Ambiguous and non-ambiguous effects are mutually
		  ;; exclusive. Since an non-ambiguous effect is the
		  ;; default assumption, it is retracted
		  (rule
		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m ?q ?x ?z))
		    (:IN (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?z)))
		   (rretract! (effect-on-1-of-modulating-the-clearance-of-2-via-3-is-non-ambiguous ?m ?x ?z) 
		                   default-inference-assumption))

		  
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

		  ;; If it is not known if the formation of two
		  ;; different metabolites from the same agent are
		  ;; catalyzed by *the same enzyme* then the effect of
		  ;; inhibiting the enzyme on both metabolites is
		  ;; ambiguous. This is because there might be both an
		  ;; increase in parent compound due to removal of one
		  ;; clearance pathway and a decrease in the ability
		  ;; of the enzyme formation of child compound
		  (rule		
		   ((:IN (1-has-metabolite-2-via-3 ?x ?m1 ?z))
		    (:IN (1-has-metabolite-2-via-3 ?x ?m2 'UNKNOWN) :TEST (not (equal ?m1 ?m2)))
		    (:IN (1-inhibits-2 ?q ?z)))
		   (rassert! 
		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m2 ?q ?x ?z)
		    (nil
		     (1-has-metabolite-2-via-3 ?x ?m1 ?z)
		     (1-has-metabolite-2-via-3 ?x ?m2 'UNKNOWN)
		     (1-inhibits-2 ?q ?z)
		     )))
				  
		  ;; The effect of an increased formation of a parent
		  ;; compound on a metabolite due to reduced clearance
		  ;; of an alternate pathway is unclear if the same
		  ;; enzyme is inhibited in both the alternate pathway
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

		  ;; The effect of an increased formation of a parent
		  ;; compound on a metabolite due to reduced clearance
		  ;; of an alternate pathway is unclear if is not
		  ;; known whether or not the same enzyme is inhibited
		  ;; in both the alternate pathway and the formation
		  ;; of the metabolite
		  (rule
		   ((:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz))
		    (:IN (1-has-metabolite-2-via-3 ?m1 ?m2 'UNKNOWN)))
		   (rassert! 
		    (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m2 ?q ?x ?enz)
		    (nil
		     (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz)
		     (1-has-metabolite-2-via-3 ?m1 ?m2 'UNKNOWN)
		     )))
		  
		  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  ;; A SET OF RULES TO FOR THE DISJUNCTIVE CASE WHERE
		  ;; AN ACTIVE INGREDIENT IS ANCESTOR TO A COMPOUND
		  ;; THAT INTERACTS WITH ANOTHER ACTIVE INGREDIENT OR
		  ;; METABOLITE
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
		  
		  	  
		  ;; an necessary condition for being an 'in vivo
		  ;; selective inhibitor' is that the agent renders
		  ;; measurable enzyme inhibition in humans
		  (rule 
		   ((:IN (1-is-an-in-vivo-selective-inhibitor-of-2 ?x ?y))) 	
		   (rassert! 
		    (1-inhibits-2 ?x ?y)
		    (nil
		     (1-is-an-in-vivo-selective-inhibitor-of-2 ?x ?y)
		     )))
		  
		  ;; a necessary condition of some active ingredient
		  ;; or compound having a primary total clearance
		  ;; enzyme is that it is a substrate of that enzyme
		  (rule 
		   ((:IN (primary-total-clearance-enzyme-of-1-is-2 ?x ?y))) 	
		   (rassert! 
		    (1-is-substrate-of-2 ?x ?y)
		    (nil
		     (primary-total-clearance-enzyme-of-1-is-2 ?x ?y)
		     )))
		  
		  ;; a necessary condition of some active ingredient
		  ;; or compound having a primary total clearance
		  ;; enzyme is that it is primarily cleared by metabolism
		  (rule 
		   ((:IN (primary-total-clearance-enzyme-of-1-is-2 ?x ?y))) 	
		   (rassert! 
		     (primary-total-clearance-mechanism-of-1-is-2 ?x 'METABOLIC-CLEARANCE)
		    (nil
		     (primary-total-clearance-enzyme-of-1-is-2 ?x ?y)
		     )))

		  
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

		  ;; a rule for when an active ingredient or metabolite, ?x, will 
		  ;; not inhibit the metabolic clearance  of another drug, ?z, 
		  ;; because ?z is not a substrate of enzyme ?y
		  (rule 
		   ((:IN (1-inhibits-2 ?x ?y))
		    (:IN (1-is-not-a-substrate-of-2 ?z ?y))) 	
		   (rassert! 
		    (1-does-not-inhibit-the-metabolic-clearance-of-2-via-3 ?x ?z ?y)
		    (nil
		     (1-inhibits-2 ?x ?y)
		     (1-is-not-a-substrate-of-2 ?z ?y)
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
		    (1-inhibits-3-the-primary-total-clearance-enz-of-2-and-2-has-high-first-pass ?x ?z ?y)
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
		  ;; than that captured by first-level-metabolic-inhibition-of-pceut-entity-of-concern 
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

		  ;; a rule for establishing that an active ingredient or metabolite
		  ;; *does* inhibit an enzyme based on in vitro evidence
		  (rule 
		   ((:IN (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i))  
		    (:IN (1-does-not-permanently-deactivate-catalytic-function-of-2 ?x ?y))
		    (:IN (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max) 
		     :TEST (> (float (/ (eval ?c_max) (eval ?k_i))) .1)))
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
		     (:IN (1-does-not-permanently-deactivate-catalytic-function-of-2 ?x ?y))
		     (:IN (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max) 
			  :TEST (<= (float (/ (eval ?c_max) (eval ?k_i) )) .1)))
		    (rassert! (1-does-not-inhibit-2 ?x ?y) 
		     (nil 
		      ;;justifications
		      (inhibition-constant-of-1-for-2-is-3 ?x ?y ?k_i)
		      (1-does-not-permanently-deactivate-catalytic-function-of-2 ?x ?y)
		      (maximum-in-vivo-concentration-of-1-is-2 ?x ?c_max)
		      (accept-in-vitro-based-enzyme-modulation-assertions)
		      )))
		  
		  ;; HOUSEKEEPING RULES -- BE SURE AND PUT THESE AFTER
		  ;; ALL OTHER RULES!! THE ORDER OF RULE EXECUTION IS
		  ;; IMPORTANT IN ESTABLISHING WHETHER SOME EFFECTS
		  ;; ARE AMBIGUOUS. PLACING THESE RULES ELSEWHERE CAN
		  ;; TRIGGER FALSE CONTRADICTIONS.

		  ;; It is a contradiction to have an ambiguous effect and a clearly 
		  ;; identified effect	  
		  (rule
		   ((:IN (effect-on-1-of-2-reducing-the-clearance-of-3-via-4-is-ambiguous ?m ?q ?x ?z))
		    (:IN (1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m ?x ?z)))
		   (contradiction (eval (quotize (list '1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m ?x ?z)))))

		  
		  ;; a rule for that makes it a contradiction for an active ingredient 
		  ;; or compound to inhibit and *not* inhibit an enzyme
		  (rule 
		   ((:IN (1-inhibits-2 ?drug ?enzyme)) 
		    (:IN (1-does-not-inhibit-2 ?drug ?enzyme))) 
		   (contradiction
		    (eval (quotize (list
				    '1-does-not-inhibit-2 ?drug ?enzyme))))) 

		  ;; a rule for that makes it a contradiction for an active ingredient 
		  ;; or compound to be  and *not* be a substrate of an enzyme
		  (rule 
		   ((:IN (1-is-substrate-of-2 ?drug ?enzyme)) 
		    (:IN (1-is-not-substrate-of-2 ?drug ?enzyme))) 
		   (contradiction
		    (eval (quotize (list
				    '1-is-not-substrate-of-2 ?drug ?enzyme))))) 

		  ;; a rule for that makes it a contradiction for an active ingrediant 
		  ;; or compund to both permanantly and not permanantly deactivate the catalytic
		  ;; function of an enzyme
		  (rule 
		   ((:IN (1-permanently-deactivates-catalytic-function-of-2 ?drug1 ?enzyme)) 
		    (:IN (1-does-not-permanently-deactivate-catalytic-function-of-2 ?drug1 ?enzyme))) 
		   (contradiction
		    (eval (quotize (list
				    '1-does-not-permanently-deactivate-catalytic-function-of-2 ?drug1 ?enzyme))))) 


		  
		  ))
    (print (eval form))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; load assertions and run-rules 
(defun simple-dikb-rule-engine ()
  (format t "~%~%SIMPLE-DDI-RULE-ENGINE: Loading the DIKB rule-base:~%")
  (test-dissertation-DIKB-rule-base-simple-met)
  
  (format t "~%~%SIMPLE-DDI-RULE-ENGINE: Loading assertions generated by the DIKB:~%")
  (load "./assertions.lisp")
  (run-rules)
  (format t "~%~%SIMPLE-DDI-RULE-BASE: Assertions currently in the rule engine:~%")
  (show-data)

  (format t "~%~%SIMPLE-DDI-RULE-ENGINE: Loading assumptions generated by the DIKB:~%")
  (load "./changing_assumptions.lisp")
  (run-rules)
  (show-data)
  
  (setf PKI-1 (concatenate 'list (get-in-assertions '(1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)) (get-in-assertions '(1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz))))
  (setf PKI-2 (concatenate 'list (get-in-assertions '(1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz))))
  (setf PKI-3 (concatenate 'list (get-in-assertions '(1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y)) (get-in-assertions '(1-inhibits-3-the-primary-total-clearance-enz-of-2-and-2-has-high-first-pass ?x ?z ?y))))
  (setf NO-PKI (concatenate 'list (get-in-assertions '(1-does-not-inhibit-the-metabolic-clearance-of-2-via-3 ?x ?z ?y))))
  (data-to-html)
  )

(defun update-inference ()
  
  (load "./changing_assumptions.lisp")
  (run-rules)
  (show-data)
  
  (setf PKI-1 (concatenate 'list (get-in-assertions '(1-inhibits-metabolic-clearance-of-2-via-3 ?x ?z ?y)) (get-in-assertions '(1-effects-an-increase-in-2-by-reducing-clearance-of-3-via-4 ?q ?m1 ?x ?enz))))
  (setf PKI-2 (concatenate 'list (get-in-assertions '(1-inhibits-3-the-primary-metabolic-enzyme-of-2 ?y ?z ?enz))))
  (setf PKI-3 (concatenate 'list (get-in-assertions '(1-inhibits-3-the-primary-total-clearance-enz-of-2 ?x ?z ?y)) (get-in-assertions '(1-inhibits-3-the-primary-total-clearance-enz-of-2-and-2-has-high-first-pass ?x ?z ?y))))
  (setf NO-PKI (concatenate 'list (get-in-assertions '(1-does-not-inhibit-the-metabolic-clearance-of-2-via-3 ?x ?z ?y))))
  (data-to-html)
  )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; System for running integrity checks on the rule-base

(defclass test-case () 
  ( 
   ;; unique string identifier (can't we do this with CLOS introspection?)
   (tid  :accessor access-tid
	:initarg :tid
	:initform nil)
   ;; description of this test
   (doc  :accessor access-doc
	 :initarg :doc
	 :initform "an new instance of test-case")
   ;; a symbol that is true if test-case instance passes all test
   (flg  :accessor access-flg
	 :initarg :flg)	 
   ;; an list of test-case instances that need to be run before this instance's tests are ran
   (deps  :accessor access-deps
	  :initarg :deps
	  :initform nil) 
   ;; a form of rules
   (state-change  :accessor access-state-change
	   :initarg :state-change)
    ;; a list of qouted test that each returns T on success
   (tests  :accessor access-tests
	   :initarg :tests)
   ))

(defmethod init-state-change ((tc test-case) reset)
    (if reset 
	(TEST-DISSERTATION-DIKB-RULE-BASE-SIMPLE-MET))
    
    (if (run-deps tc)
        (progn 
	  (dolist (form (access-state-change tc))
	    (print (eval form)))
	  T)
      nil
      ))
    

(defmethod run-deps ((tc test-case))
  (setf (access-flg tc) T)
  (dolist (dep (access-deps tc))
    (init-state-change dep nil)
    (if (not (run-tests dep))
	(progn
	  (format t "~%TEST cannot run because tests for dependency ~A did not run succesfully!" (quote dep))
	  (setf (access-flg tc) nil)
	  (error "FAILED INVARIANT CONDITION")
	  )
      ))
  (if (eq (access-flg tc) nil)
      nil
    T)
  )

(defmethod run-tests ((tc test-case))
  (setf (access-flg tc) T)
  (dolist (tst (access-tests tc))
    (format t "~%TEST ~A - RUNNING TEST: ~A " (access-tid tc) tst)
	(let ((v (eval tst)))
	  (if (not v)
	      (progn
		(format t "~%TEST ~A: TEST ~A FAILED!" (access-tid tc) tst)
		(setf (access-flg tc) nil)
		(error "FAILED INVARIANT CONDITION")
		)
	    T)))
  (if (eq (access-flg tc) nil)
      nil
    T)
  )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; TESTS 
;; These tests are useful for ensuring that changes made to the DIKB
;; rules do not inadvertently corrupt the knowledge base.
;;
;; To run them - 
;;   1) load the system:
;;           $ (load "load")
;;   2) decide on the test you want to run and initialize it; for example, to run test t4a:
;;           $ (init-state-change t4a T)
;;  NOTE: if the interpreter enters debug mode reply with  (tms-answer 2) at the prompt
;;   3) run the test you chose:
;;           $ (run-tests t4a)

;; basic tests on inhibition, substrate-of, and evidence
(setf t1a (make-instance 'test-case
	    :tid "t1a"
	    :doc "a simple test of inhibition assertions"
	    :flg 'test-1a-ok
	    :deps nil
	    :state-change '(
			    (assert! '(1-inhibits-2 'troleandomycin 'cyp2c9) '('dikb-assertion (bc-satisfied 'inhibits-cyp3a4-troleandomycin)))
			    (assume!
			     '(bc-satisfied 'inhibits-cyp3a4-troleandomycin)
			     'default-inference-assumption)
			    
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'clopidogrel 'cyp2b6) 
			     'default-inference-assumption)
			    (run-rules)
			    )
	    :tests  (list '(in? '(1-INHIBITS-2 'TROLEANDOMYCIN 'CYP2C9))
			  '(in? '(1-INHIBITS-2 'CLOPIDOGREL 'CYP2B6)))
	    ))


(setf t1b (make-instance 'test-case
	    :tid "t1b"
	    :doc "test of inhibits and substrate-of rules"
	    :flg 'test-1b-ok
	    :deps nil
	    :state-change '(
			    (assert! '(1-is-substrate-of-2 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (1-is-an-in-vivo-selective-inhibitor-of-2 'diltiazem 'cyp3a4)))
			    (assert! '(1-is-substrate-of-2 'simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'substrate-of-cyp3a4-simvastatin) (1-is-an-in-vivo-selective-inhibitor-of-2 'ketoconazole 'cyp3a4)))
			    (assume! 
			     '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
			     'default-inference-assumption)
			    
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'itraconazole 'cyp3a4) 
			     'default-inference-assumption)
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'diltiazem 'cyp3a4) 
			     'default-inference-assumption)
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
			     'default-inference-assumption)
			    (run-rules)
			    )
	    :tests  (list '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4)))
	   ))

(setf t1c (make-instance 'test-case
	    :tid "t1c"
	    :doc "test of retracting a default assumption"
	    :flg 'test-1c-ok
	    :deps (list t1b)
	    :state-change '(
			    (retract! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'diltiazem 'cyp3a4) 
			     'default-inference-assumption)	  
			    )
	    :tests  (list '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))
			  '(not (in? '(1-INHIBITS-2 'DILTIAZEM 'CYP3A4))))
	    ))

(setf t1d (make-instance 'test-case
	    :tid "t1d"
	    :doc "test of retracting a default assumption"
	    :flg 'test-1d-ok
	    :deps (list t1c)
	    :state-change '(
			    (retract! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
			     'default-inference-assumption)	  
			    )
	    :tests  (list '(not (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))))
	    ))

(setf t1e (make-instance 'test-case
	    :tid "t1e"
	    :doc "test of re-assuming a default assumption"
	    :flg 'test-1e-ok
	    :deps (list t1d)
	    :state-change '(
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'ketoconazole 'cyp3a4) 
			     'default-inference-assumption)	  
			    )
	    :tests  (list '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))
			  )
	    ))

(setf t1f (make-instance 'test-case
	    :tid "t1f"
	    :doc "test of retracting assertions because evidence fails to meet belief criteria"
	    :flg 'test-1f-ok
	    :deps (list t1e)
	    :state-change '(
			    (retract! 
			     '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
			     'default-inference-assumption)
			    )
	    :tests  (list '(not (in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4)))
			  )
	    ))

(setf t1g (make-instance 'test-case
	    :tid "t1g"
	    :doc "test of retracting assertions because evidence fails to meet belief criteria"
	    :flg 'test-1g-ok
	    :deps (list t1f)
	    :state-change '(
			    (assert! 
			     '(bc-satisfied 'substrate-of-cyp3a4-simvastatin) 
			     'default-inference-assumption)
			    )
	    :tests  (list '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'SIMVASTATIN 'CYP3A4))
			  )
	    ))

;; tests of the metabolite and ancestor rules
(setf t2a (make-instance 'test-case
	    :tid "t2a"
	    :doc "test of the metabolite and ancestor rules"
	    :flg 'test-2a-ok
	    :deps (list t1b)
	    :state-change '(
			    (assert! '(1-has-metabolite-2-via-3 'simvastatin 'beta-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)))
			    (assert! '(1-has-metabolite-2-via-3 'beta-hydroxy-simvastatin '6-hydroxy-simvastatin 'cyp3a4) '('dikb-assertion (bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)))
			    (assume! 
			     '(bc-satisfied 'has-metabolite-simvastatin-beta-hydroxy-simvastatin-cyp3a4)
			     'default-inference-assumption)
			    (assume! 
			     '(bc-satisfied 'has-metabolite-beta-hydroxy-simvastatin-6-hydroxy-simvastatin-cyp3a4)
			     'default-inference-assumption) 
			    (run-rules)
			    )
	    :tests  (list 
		     '(in? '(1-IS-ANCESTOR-OF-2 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN))
		     '(in? '(1-IS-SUBSTRATE-OF-2 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
		     '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'BETA-HYDROXY-SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'KETOCONAZOLE 'BETA-HYDROXY-SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
		     )
	    ))

;; tests of active ingredient rules
(setf t3a (make-instance 'test-case
	    :tid "t3a"
	    :doc "test of active ingredient rules"
	    :flg 'test-3a-ok
	    :deps (list t2a)
	    :state-change '(
			    (assume! 
			     '(1-is-an-active-ingredient 'simvastatin)
			     'default-inference-assumption)
			    (assume! 
			     '(1-is-an-active-ingredient 'itraconazole)
			     'default-inference-assumption)
			    (run-rules)
			    )
	    :tests  (list 
		     '(in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-IS-AFFECTED-BY-3 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'ITRACONAZOLE))
                     )
	    ))

(setf t3b (make-instance 'test-case
	  :tid "t3b"
	  :doc "test of active ingredient rules"
	  :flg 'test-3b-ok
	  :deps (list t3a)
	  :state-change '(
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
			  )
	  :tests  (list 
		   '(in? '(1-IS-ANCESTOR-OF-2 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE))
		   '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'DILTIAZEM 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
		   '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'DILTIAZEM-ACTIVE-METABOLITE 'SIMVASTATIN '6-HYDROXY-SIMVASTATIN 'CYP3A4))
		   '(in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-IS-AFFECTED-BY-3 'SIMVASTATIN 'BETA-HYDROXY-SIMVASTATIN 'DILTIAZEM-ACTIVE-METABOLITE))
		   '(in? '(ACTIVE-INGREDIENT-1-IS-ANCESTOR-TO-2-AND-2-EFFECTS-AN-INTERACTION-WITH-3 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'SIMVASTATIN))
		   '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'CYP3A4))
		   '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'DILTIAZEM 'CYP3A4))
		   ;; NOTE: circular inhibition is allowed...for now
		   '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'DILTIAZEM-ACTIVE-METABOLITE 'DILTIAZEM 'DILTIAZEM-ACTIVE-METABOLITE 'CYP3A4))

		   )
	  ))
;; a complicated test of the effect of inhibiting various metabolites
(setf t4a (make-instance 'test-case
	    :tid "t4a"
	    :doc "a complicated test of the effect of inhibiting various metabolites"
	    :flg 'test-t4a-ok
	    :deps nil
	    :state-change '(
			    (assert! '(1-inhibits-2 'sulfinpyrazone 'cyp2c9) '('dikb-assertion (bc-satisfied 'inhibits-cyp2c9-sulfinpyrazone)))
			    (assume!
			     '(bc-satisfied 'inhibits-cyp2c9-sulfinpyrazone)
			     'default-inference-assumption)

			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'clopidogrel 'cyp2b6) 
			     'default-inference-assumption)

			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'itraconazole 'cyp3a4) 
			     'default-inference-assumption)
			    
			    (assume! 
			     '(1-is-an-in-vivo-selective-inhibitor-of-2 'bogus-drug-1 'cyp2a6) 
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

			    (assert! '(1-has-metabolite-2-via-3 'chloroacetaldehyde-cyclophosimide 'bogus-metabolite-2 'cyp2a6) 
			     '('dikb-assertion (bc-satisfied 'has-metabolite-chloroacetaldehyde-cyclophosimide-bogus-metabolite-2-cyp2a6)))
			    (assume!
			     '(bc-satisfied 'has-metabolite-chloroacetaldehyde-cyclophosimide-bogus-metabolite-2-cyp2a6)
			     'default-inference-assumption)
			    
			    ;; always assume! uknowns so they can be retracted should the unknown become known
			    (assume! '(1-has-metabolite-2-via-3 '2-dechloroethyl-cyclophosimide 'bogus-metabolite-1 'unknown) 
			     'default-inference-assumption)
			    
			    (assume! '(1-has-metabolite-2-via-3 'bogus-metabolite-2 'bogus-metabolite-3 'cyp2a6) 
			     'default-inference-assumption)
			    			    
			    (assume! '(1-has-metabolite-2-via-3 '4-hydroxy-cyclophosimide 'phosphoramide-mustard 'unknown) 
			     'default-inference-assumption)

			    (assume! '(1-has-metabolite-2-via-3 '4-hydroxy-cyclophosimide 'acrolein 'unknown) 
			     'default-inference-assumption)
			    (run-rules)

			    )
	    :tests  (list 
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS '4-HYDROXY-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'ACROLEIN 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'ITRACONAZOLE 'ACROLEIN 'CYCLOPHOSIMIDE 'CYP3A4)))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'PHOSPHORAMIDE-MUSTARD 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(not (in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'ITRACONAZOLE  'PHOSPHORAMIDE-MUSTARD 'CYCLOPHOSIMIDE 'CYP3A4)))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-1 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-2 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-3 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'CYP3A4))
		     '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-INHIBITS-3-THE-PRIMARY-METABOLIC-ENZYME-OF-2 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-1 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-INHIBITS-METABOLIC-CLEARANCE-OF-2-VIA-3 'SULFINPYRAZONE 'CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'SULFINPYRAZONE 'CHLOROACETALDEHYDE-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'SULFINPYRAZONE '2-DECHLOROETHYL-CYCLOPHOSIMIDE 'CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL 'BOGUS-METABOLITE-2 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'CLOPIDOGREL 'BOGUS-METABOLITE-3 'CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-1 'SULFINPYRAZONE 'CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'SULFINPYRAZONE 'BOGUS-METABOLITE-2 'CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-EFFECTS-AN-INCREASE-IN-2-BY-REDUCING-CLEARANCE-OF-3-VIA-4 'SULFINPYRAZONE 'BOGUS-METABOLITE-3 'CYCLOPHOSIMIDE 'CYP2C9))
		     		     
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'ITRACONAZOLE 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP3A4))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'SULFINPYRAZONE 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP2C9))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'SULFINPYRAZONE 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP2C9))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'SULFINPYRAZONE 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP2C9))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4 'CLOPIDOGREL 'CYCLOPHOSIMIDE '4-HYDROXY-CYCLOPHOSIMIDE 'CYP2B6))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'PHOSPHORAMIDE-MUSTARD 'CYP2B6))
		     '(in? '(1-INHIBITS-TRANSFORMATION-OF-2-TO-3-VIA-4-UPSTREAM 'CLOPIDOGREL 'CYCLOPHOSIMIDE 'ACROLEIN 'CYP2B6))
		     '(in? '(EFFECT-ON-1-OF-2-REDUCING-THE-CLEARANCE-OF-3-VIA-4-IS-AMBIGUOUS 'BOGUS-METABOLITE-3 'BOGUS-DRUG-1 'CYCLOPHOSIMIDE 'CYP2A6))
		     )
	    ))



;  (setf t (make-instance 'test-case
;         :tid ""
; 	   :doc ""
; 	   :flg '
; 	   :deps nil
; 	   :state-change '(
		   
; 		    )
; 	   :tests  (list 
;                      )
; 	   ))



