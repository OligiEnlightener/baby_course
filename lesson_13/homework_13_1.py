from lesson_13.student_comparable import Student_comparable

vasyl = Student_comparable("male", 22, "Vasyl","Vasylenko", "228")
vasyl2 = Student_comparable("male", 22, "Vasyl","Vasylenko", "228")
fedor = Student_comparable("male", 22, "Fedor","Vasylenko", "228")

assert vasyl2 == vasyl, vasyl2 == vasyl
assert fedor == vasyl, fedor == vasyl