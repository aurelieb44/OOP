import StudentClass as sc

StudentID = input('Enter Student ID: ')
DOB = (input('Enter Date of Birth: '))
DOB = int(DOB.split('/')[2])

Name = input('Enter Name: ')
Classification = input("Enter Classification - i.e. 'Sr','Jr','S' or 'F'): ")

my_student = sc.Student(StudentID, Name, DOB, Classification)

my_student.set_age(DOB)
my_student.set_regis_date(Classification)

print('Student Age: ', my_student.get_age())
print('Student Registration Date: ', my_student.get_regis_date())



