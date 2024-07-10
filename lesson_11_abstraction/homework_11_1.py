from lesson_11_abstraction.homework_11_1.group import Group
from lesson_11_abstraction.homework_11_1.student import Student

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza', 'Faylor', 'AN145')
st4 = Student('Female', 25, 'Liza', 'Caylor', 'AN145')
st5 = Student('Female', 25, 'Liza', 'Baylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), f'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!