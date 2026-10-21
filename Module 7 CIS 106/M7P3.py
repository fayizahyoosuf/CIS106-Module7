# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:59:11 2026

@author: shama
"""

studentCount = 0


userChoice = input("Do you want to run this program? (Yes/No): ")


while userChoice.lower() == "yes":

    lastName = input("Enter student's last name: ")
    examScore1 = float(input("Enter exam score 1: "))
    examScore2 = float(input("Enter exam score 2: "))
    
    
    averageScore = (examScore1 + examScore2) / 2
    studentCount += 1
    
    print(f"Student: {lastName} | Average Score: {averageScore:.2f}")
    
    
    userChoice = input("Do you want to enter another student? (Yes/No): ")

print(f"\nTotal number of students processed: {studentCount}")