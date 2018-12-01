(defun read-input (filename)
  (with-open-file (stream filename)
                  (loop for line = (read-line stream nil)
                        while line
                        collect line)))

(defun read-ints (filename)
  (mapcar #'parse-integer (read-input filename)))

(defun day01a ()
  (let ((changes (read-ints "input.01")))
    (reduce #'+ changes)))

(setf *print-circle* t)
(defun circular! (items)
  (setf (cdr (last items)) items))

(defun day01b ()
  (let ((changes (circular! (read-ints "input.01")))
        (table (make-hash-table))
        (frequency 0))
    (loop for change in changes
          if (gethash frequency table)
          return frequency
          else do (setf (gethash frequency table) t)
          do (setf frequency (+ frequency change)))))


(day01a)
(day01b)
