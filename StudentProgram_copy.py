import StudentClass_copy as sc

my_student = sc.Student('789', 'Yo','9/9/2005','Sr')


my_student.calculate_age()
my_student.set_regis_date()

print('Student ID: ', my_student.get_studentID())
print('Student Age: ', my_student.get_age())
print('Student Registration Date: ', my_student.get_regis_date())
