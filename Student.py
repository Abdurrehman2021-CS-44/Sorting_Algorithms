# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:02:16 2022

@author: USER
"""

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def display_student(self):
        print ("Name: " + self.name)
        print ("Major: " + self.major)
        print ("GPA: " + str(self.gpa))