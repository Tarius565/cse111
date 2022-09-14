"""
filename: tire_volume
author: Tanner Levi
date: 9/14/2022
"""

"""
Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.
"""

from cmath import pi
from datetime import datetime
from datetime import date

dateTime = date.today()

width = float(input("Enther the width of the tire in mm (ex 205): "))
aspectRatio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (pi * width ** 2 * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000000

print()
print(f"The approximate volume is {v:.2f} liters")
print()

ans = input("Would you like to buy these tires?(Y/N) ").upper()

if ans == "Y":
    phone = input("Please enter your phone number: ")
    with open("Prove_Assignments/L02 Tire Volume/volumes.txt", "at") as volumes:
        print(f"{dateTime}, {width}, {aspectRatio}, {diameter}, {v:.2f}, {phone}", file=volumes)
else:
    with open("Prove_Assignments/L02 Tire Volume/volumes.txt", "at") as volumes:
        print(f"{dateTime}, {width}, {aspectRatio}, {diameter}, {v:.2f}", file=volumes)