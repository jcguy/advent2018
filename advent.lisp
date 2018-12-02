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

(defun char-counts (id)
  (let ((chars (remove-duplicates id)))
    (loop for char across chars
          collect (count char id))))

(defun day02a ()
  (let ((ids (read-input "input.02")))
    (* (list-length (remove-if-not #'(lambda (id) (find 2 (char-counts id))) ids))
       (list-length (remove-if-not #'(lambda (id) (find 3 (char-counts id))) ids)))))

(defun cartesian-product (first-list second-list)
  (loop for x in first-list
        nconc (loop for y in second-list
                 collect (list x y))))

(defun exactly-one-different (strings)
  (let ((string1 (car strings))
        (string2 (cadr strings)))
    (= 1 (count t (loop for a across string1
                        for b across string2
                        collect (not (char= a b)))))))

(defun day02b ()
  (let* ((ids (read-input "input.02"))
         (matches (remove-if-not #'exactly-one-different (cartesian-product ids ids)))
         (match (nth 0 matches))
         (first-string (nth 0 match))
         (second-string (nth 1 match)))
    (coerce (loop for char1 across first-string
             for char2 across second-string
             if (char= char1 char2)
             collect char1)
            'string)))


(day02a)
(day02b)
