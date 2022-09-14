"""
filename: tire_volume
author: Tanner Levi
date: 9/12/2022
"""

"""
Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.
"""

from cmath import pi


w = float(input("Enther the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000

print()
print(f"The approximate volume is {v:.2f} liters")
print()