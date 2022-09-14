"""
filename: heart_rate.py
author: Tanner Levi
"""
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("Please enter your age: "))

heartRateMax = 220 - age
heartRate65 = heartRateMax * .65
heartRate85 = heartRateMax * .85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {heartRate65} and {heartRate85} beats per minute.")