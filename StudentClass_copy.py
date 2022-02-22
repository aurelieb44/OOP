
from datetime import date

class Student:

    def __init__(self, StudentID, Name, DOB, Classification):
        self.__studentID = StudentID
        self.__name = Name
        self.__dob = DOB
        self.__classification = Classification
        self.__age = 0
        self.__regis_date = 0

    def set_studentID(self, StudentID):
        self.__studentID = StudentID
    
    def calculate_age(self): #method to calculate student age
        today = date.today()
        self.__age = today.year - int(self.__dob.split('/')[2])

    def set_regis_date(self): #method to determine registration date
        if self.__classification == 'Sr':
            self.__regis_date = 'Registration date: 11/1 thru 11/3'
        elif self.__classification == 'Jr':
            self.__regis_date = 'Registration date: 11/4 thru 11/6'
        elif self.__classification == 'S':
            self.__regis_date = 'Registration date: 11/7 thru 11/9'
        else:
            self.__regis_date = 'Registration date: 11/10 thru 11/12'

    def get_studentID(self):
        return self.__studentID

    def get_age(self):
        return self.__age

    def get_regis_date(self):
        return self.__regis_date

