# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:53:51 2026

@author: shama
"""

startValue = int(input("Enter the start value: "))
stopValue = int(input("Enter the stop value: "))
incrementValue = int(input("Enter the increment value: "))

currentValue = startValue


while currentValue <= stopValue:
    print(currentValue)
    currentValue += incrementValue