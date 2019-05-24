(defn read-input [day]
  (with-open [rdr (clojure.java.io/reader (str "../input/input." day))]
    (doall (line-seq rdr))))

(defn day01a []
  (reduce + (map #(Integer/parseInt %) (read-input "01"))))

(defn day01b []
  (map #(Integer/parseInt %) (read-input "01")))


(prn (day01a))
(prn (day01b))
