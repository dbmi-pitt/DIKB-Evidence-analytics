;; -*- Mode: Lisp; -*- 

;;;; JTRE definitions  
;;;; Last edited 1/29/93, by KDF

;;; Copyright (c) 1989 -- 1992 Kenneth D. Forbus, Northwestern University,
;;; Johan de Kleer and Xerox Corporation.
;;; All rights reserved.


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

(in-package :COMMON-LISP-USER) 

(defstruct (jtre (:PRINT-FUNCTION jtre-printer))
  title                   ; Pretty name
  jtms                    ; Pointer to its JTMS
  (dbclass-table nil)       ; Table of dbclasses
  (datum-counter 0)       ; Unique ID for asserts
  (rule-counter 0)        ; Unique ID for rules
  (debugging nil)         ; If non-NIL, show basic operations
  (queue nil)             ; Rule queue
  (rules-run 0))          ; Statistic

(defun jtre-printer (j st ignore)
  (format st "<JTRE: ~A>" (jtre-title j)))

(defvar *JTRE* nil)

(defmacro With-Jtre (jtre &rest forms)
  `(let ((*JTRE* ,jtre)) ,@ forms))

(defun In-Jtre (jtre) (setq *JTRE* jtre))

(defmacro debugging-jtre (msg &rest args)
  `(when (jtre-debugging *JTRE*) (format t ,msg  ,@args)))

(defun create-jtre (title &key debugging)
 (let ((j (make-jtre
	   :TITLE title 
	   :JTMS (create-jtms (list :JTMS-OF title) 
			      :NODE-STRING 'view-node)
	   :DBCLASS-TABLE (make-hash-table :TEST #'eq)
	   :DEBUGGING debugging)))
   (change-jtms (jtre-jtms j)
		:ENQUEUE-PROCEDURE
		#'(lambda (rule) (enqueue rule j)))
   j))

(defun change-jtre (jtre &key (debugging :NADA))
  (unless (eq debugging :NADA)
	  (setf (jtre-debugging jtre) debugging)))

;;;; Running JTRE

(defun uassert! (fact &optional (just 'user))
  (assert! fact just) ;; Do internal operation
  (run-rules *JTRE*))        ;; Run the rules

(defun uassume! (fact reason) ;; Similar to UASSERT!
  (assume! fact reason *JTRE*)
  (run-rules *JTRE*))

(defun run-forms (forms &optional (*JTRE* *JTRE*))
  (dolist (form forms) (eval form) (run-rules *JTRE*)))

(defun run (&optional (*JTRE* *JTRE*)) ;; Toplevel driver function
    (format T "~%>>")
    (do ((form (read) (read)))
        ((member form '(quit stop exit abort)) nil)
        (format t "~%~A" (eval form))
        (run-rules)
        (format t "~%>>")))

(defun show (&optional (*JTRE* *JTRE*) (stream *standard-output*))
  (show-data *JTRE* stream) (show-rules *JTRE* stream))

