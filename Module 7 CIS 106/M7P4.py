# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:07:38 2026

@author: shama
"""

totalGrossPay = 0.0
employeeCount = 0


userChoice = input("Do you want to run this program? (Yes/No): ")


while userChoice.lower() == "yes":

    lastName = input("Enter employee's last name: ")
    hoursWorked = float(input("Enter hours worked: "))
    payRate = float(input("Enter rate of pay: "))
    
    
    if hoursWorked > 40:
        regularPay = 40 * payRate
        overtimeHours = hoursWorked - 40
        overtimePay = overtimeHours * (payRate * 1.5)
        grossPay = regularPay + overtimePay
    else:
        grossPay = hoursWorked * payRate
        
    totalGrossPay += grossPay
    employeeCount += 1
    
    print(f"Employee: {lastName} | Gross Pay: ${grossPay:.2f}")
    
    userChoice = input("Do you want to enter another employee? (Yes/No): ")
    
if employeeCount > 0:
    averagePay = totalGrossPay / employeeCount
    print("\n--- Payroll Summary ---")
    print(f"Total Gross Pay Paid: ${totalGrossPay:.2f}")
    print(f"Total Employees Processed: {employeeCount}")
    print(f"Average Employee Pay: ${averagePay:.2f}")
else:
    print("\nNo employee data was entered.")