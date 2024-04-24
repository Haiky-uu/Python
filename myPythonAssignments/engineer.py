# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:13:31 2020

@author: MANDAR
"""


import person as p

class Engg(p.Person):
    def __init__(self, fname,lname,age,gender,speciality,salary):
        super().__init__(fname,lname,age,gender)
        self.speciality = speciality
        self.salary = salary
    #@override
    def print_person(self):
        print("OVERRIDE METHOD IN ENGG CLASS@@@@##$$$$$")
        print(self.first_name, self.last_name, self.salary)
        
    def print_tax(self):
       print("Salary Based Tax Calculation")