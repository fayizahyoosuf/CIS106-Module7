# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:18:38 2026

@author: shama
"""

totalDiscounts = 0.0


userChoice = input("Do you want to run this program? (Yes/No): ")

while userChoice.lower() == "yes":

    itemQuantity = int(input("Enter item quantity: "))
    itemPrice = float(input("Enter item price: "))
    
    
    extendedPrice = itemQuantity * itemPrice
    
    
    if extendedPrice > 10000.00:
        discountRate = 0.25
    else:
        discountRate = 0.10
        
    
    discountAmount = extendedPrice * discountRate
    finalTotal = extendedPrice - discountAmount
    
    
    totalDiscounts += discountAmount
    
    
    print(f"\nOrder Breakdown:")
    print(f"  Extended Price: ${extendedPrice:.2f}")
    print(f"  Discount Amount: ${discountAmount:.2f}")
    print(f"  Order Total: ${finalTotal:.2f}")
    
    
    userChoice = input("Do you want to enter another order? (Yes/No): ")


print("\n--- Summary Reports ---")
print(f"Sum of all applied discounts: ${totalDiscounts:.2f}")