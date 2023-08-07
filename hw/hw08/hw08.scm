(define (my-filter pred s) 
    (if (null? s) nil
        (if (pred (car s)) 
        (cons (car s) (my-filter pred (cdr s)))
        (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 
    (cond 
          ((null? lst1) lst2 )
          ((null? lst2) lst1 )
          (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
          ))

(define (accumulate joiner start n term)
  (if (= n 1) (term 1)
      (let (
               (startvalue (term n)))
           (if (or (eq? joiner *) (eq? joiner /))
               (joiner start startvalue (accumulate joiner 1 (- n 1) term))
               (joiner start startvalue (accumulate joiner 0 (- n 1) term))
               
      ))
           )
           )
           

(define (no-repeats lst) 
    (if (null? lst) nil
        (cons (car lst) (no-repeats (my-filter (lambda (n) (not (= n (car lst)))) (cdr lst)))) 
        )
    )
    
                 
