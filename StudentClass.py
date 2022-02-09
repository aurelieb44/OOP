
from datetime import date

class Student:

    def __init__(self, StudentID, Name, DOB, Classification):
        self.__studentID = StudentID
        self.__name = Name
        self.__dob = DOB
        self.__classification = Classification
        self.__age = 0
        self.__regis_date = 0

    def set_age(self,DOB): #method to calculate student age
        today = date.today()
        self.__age = today.year - self.__dob

    def set_regis_date(self,Classification): #method to determine registration date
        if Classification == 'Sr':
            self.__regis_date = 'Registration date: 11/1 thru 11/3'
        elif Classification == 'Jr':
            self.__regis_date = 'Registration date: 11/4 thru 11/6'
        elif Classification == 'S':
            self.__regis_date = 'Registration date: 11/7 thru 11/9'
        else:
            self.__regis_date = 'Registration date: 11/10 thru 11/12'

    def get_age(self):
        return self.__age

    def get_regis_date(self):
        return self.__regis_date

