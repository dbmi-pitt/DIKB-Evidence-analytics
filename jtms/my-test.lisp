;; -*- Mode: Lisp; -*-

;;;; Simple test of the JTRE for infering drug interactions

(in-package :COMMON-LISP-USER)

(defun ddi-jtre-continuous ()
  "a test of applying a value check as part of a rul"
  (in-jtre (create-jtre "Continuous DDI JTRE" :DEBUGGING t))
  (dolist (form '(
		  (defun test-relevance-of-inhibition-constant (c_max k_i )
		    (if (<= (float (/ (coerce c_max 'float) (coerce k_i 'float))) 1.0)
			'T
		      nil
		    ))
		  (rule ((:IN (inhibition-constant ?drug1 ?enzyme ?k_i) ) 
			 (:IN (maximum-concentration ?drug1 ?c_max) :TEST (test-relevance-of-inhibition-constant ?c_max ?k_i)))
			(rassert! (inhibits ?drug1 ?enzyme) 
				  ( nil 
				    (inhibition-constant ?drug1 ?enzyme ?k_i)
				    (maximum-concentration ?drug1 ?c_max)
				    (accept-in-vitro-based-enzyme-modulation-assertions)))
			)
                  (assume! '(inhibition-constant 'diltiazem 'cyp3a4 0.5) 'acceptable-level-of-evidence) 
                  (assume! '(maximum-concentration 'diltiazem 0.3) 'acceptable-level-of-evidence) 
		  (assume! '(accept-in-vitro-based-enzyme-modulation-assertions) 'user-config)
		  (run-rules)
		  (format t "~% No errors during attempted rule execution, should now see:~% (:IN (INHIBITS 'DILTIAZEM 'CYP3A4)).")
                  (show-data)))
    (print (eval form))))


(defun simplest-ddi-jtre ()
  "Doesn't get simpler than this"
  (in-jtre (create-jtre "Simplest DDI JTRE" :DEBUGGING t))
  (dolist (form '((rule ((:IN (substrate ?drug1 ?enzyme) ) 
			 (:IN (inhibitor ?drug2 ?enzyme) ))
                        (rassert! (inhibits ?drug2 ?drug1) ( nil (substrate ?drug1 ?enzyme) (inhibitor ?drug2 ?enzyme))))
                  (format t "~% inhibit rule defined okay.")
                  (assume! '(substrate 'simvastatin 'cyp3a4) 'acceptable-level-of-evidence) 
                  (format t "~% asserted substrate okay.")
                  (assume! '(inhibitor 'voriconazole 'cyp3a4) 'acceptable-level-of-evidence) 
                  (format t "~% asserted inhibitor okay.")
		  (run-rules)
		  (format t "~% No errors during attempted rule execution, should now see:~% (:IN (INHIBITS 'VORICONAZOLE 'SIMVASTATIN)).")
                  (show-data)))
    (print (eval form))))


(defun socrates-jtre ()
  "A simple example implementing p165 of 'Building Problem Solvers' - Forbus, DeKleer 1993
     'Socrates died because he was mortal and drank poison, and all mortals die when they
      drink poison. Socrates was mortal because he was a human and all humans all mortal. Socrates
      drank poison because he held dissident beliefs, the governments was conservative, and
      those holding dissident beliefs under such governments must drink poison'

   This example includes an example of retracting an assumption.
  "
  (in-jtre (create-jtre "Socrates JTRE" :DEBUGGING t))
  (dolist (form '((rule ((:IN (human  ?x) ))
                        (rassert! (mortal ?x) ( nil  (human  ?x) )))
                  (rule ((:IN (mortal  ?x) )
                         (:IN (drink-poison ?x)))
                        (rassert! (die ?x) ( nil (mortal  ?x) (drink-poison ?x))))
                  (rule ((:IN (hold-dissident-beliefs  ?x) )
                         (:IN (conservative-government ?y) )
                         (:IN (citizen ?x ?y) ))
                        (rassert! (drink-poison ?x) ( nil (hold-dissident-beliefs  ?x) (conservative-government ?y) (citizen ?x ?y))))
                  (assert! '(human 'socrates) nil)
                  (assume! '(hold-dissident-beliefs 'socrates) 'history-says-so)
                  (assert! '(conservative-government 'ancient-greece) nil)
                  (assert! '(citizen 'socrates 'ancient-greece) nil)
                  (run-rules)
                  (format t "~% The jtre instance: ~%~A." *jtre*)
                  (format t "~% The jtms associated with this jtre instance: ~%~A." (jtre-jtms *jtre*))
                  (format t "~% Its Nodes: ~%~A." (jtms-nodes (jtre-jtms *jtre*)))
                  (format t "~% Did Socrates die?: ~%~A."
                          (cond ((not (equal (length (FETCH '(DIE ?X))) 0)) t)
                                (t nil)))
                  (format t "~% Why?: ~%~A."
                          (why? '(die 'socrates)))
                  (format t "~% The Well-Founded support for consequence before retracting (hold-dissident-beliefs 'socrates) : ~%~A."
                          (wfs '(die 'socrates)))
                  (retract! '(hold-dissident-beliefs 'socrates) 'history-says-so)
                  (format t "~% Did Socrates die (is the assertion still ':IN'?): ~%~A."
                          (cond ((in? '(die 'socrates)) t)
                                (t nil)))
                  (format t "~% The Well-Founded support for consequence after retracting (hold-dissident-beliefs 'socrates): ~%~A."
                          (wfs '(die 'socrates)))
                  ))
    (print (eval form))))
                  
(defun test-retract-propogation ()
  "Assume the following dependancy network holds (* = asserted):
      C*     B*     A*  ;assumed nodes
       \    / \    /
        <j1>    <j2>    ;justifications
         |        |
        [E*]     [D*]   ;derived nodes
          \     /  |
           <j3>    |    
             |     |
            [F*]--<j4>

   This is a test of what happens when A is retracted, the
   result should be:
      C*     B*     A  ;assumed nodes
       \    / \    /
        <j1>    <j2>    ;justifications
         |        |
        [E*]     [D]   ;derived nodes
          \     /  |
           <j3>    |    
             |     |
            [F]--<j4>

   08042005: Looks good
 "
  (in-jtre (create-jtre "Propogate JTRE" :DEBUGGING t))
  (dolist (form '((rule ((:IN (A  ?x) )
                         (:IN (B  ?x)))
                        (rassert! (D ?x) ( nil  (A  ?x) (B ?x ))))
                  (rule ((:IN (B  ?x) )
                         (:IN (C  ?x)))
                        (rassert! (E ?x) ( nil  (B  ?x) (C ?x ))))
                  (rule ((:IN (E  ?x) )
                         (:IN (D  ?x)))
                        (rassert! (F ?x) ( nil  (E  ?x) (D ?x ))))
                  (rule ((:IN (F  ?x) ))
                        (rassert! (D ?x) ( nil  (F  ?x))))
                  (assume! '(A 'foo) nil)
                  (assume! '(B 'foo) nil)
                  (assume! '(C 'foo) nil)
                  (run-rules)
                  (show-data)
                  (format t "~% Why?: ~%~A."
                          (why? '(D 'foo)))
                  (retract! '(A 'foo) nil)
                  (format t "~% Why?: ~%~A."
                          (why? '(D 'foo)))
                  (show-data)
                  ))
    (print (eval form))))

(defun test-default-semantics ()
  "If default semantics hold, the following dependancy network should
   be the result of the actions taken (* = asserted, [_|_] = contradiction):
   A*     B     C*
     \   / \   /
      <j1>  <j2>
       |      |
     [_|_]  [_|_]

  08042005: Enters interactive contradiction resolution because the
            default condtradiction-handler is ask-user-handler in jtms.lisp
  "
  (in-jtre (create-jtre "Check default semantics JTRE" :DEBUGGING t))
  (dolist (form '((rule ((:IN (A  ?x) )
                         (:IN (B  ?x)))
                        (rassert! (D ?x) ( nil  (A  ?x) (B ?x ))))
                  (rule ((:IN (B  ?x) )
                         (:IN (C  ?x)))
                        (rassert! (E ?x) ( nil  (B  ?x) (C ?x ))))
                  (assume! '(A 'foo) nil)
                  (assume! '(B 'foo) nil)
                  (assume! '(C 'foo) nil)
                  (default-assumptions (jtre-jtms *jtre*))  ;;Treat all enabled assumptions into defaults
                  (run-rules)
                  (format t "~% Before labeling contras: ~%~A." (show-data))
                  (contradiction '(D 'foo))
                  (contradiction '(E 'foo))
                  (format t "~% After labeling contras: ~%~A." (show-data))
                  ))
    (print (eval form))))
                  
  
