(defun factorial (n)
 (loop for result =1 then (* result i)
	for i from 2 to n
	finally (return result))
