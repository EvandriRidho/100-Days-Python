# Exercise 1 - BMI Calculator
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / ( height ** 2)

print(bmi)


# Day 002 Project - Calculator Tip
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
tipBill = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

totalResults = (totalBill + (totalBill * (tipBill / 100))) / people
print(f"Each person should pay: ${totalResults}")

print(6 + 4 / 2 - (1 * 2))