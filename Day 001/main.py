# Exercise 1 - Print
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Exercise 2 - Fix Code
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# Exercise 3 - Variable
glass1 = "milk"
glass2 = "juice"
# Langkah 1: Simpan isi glass1 ke dalam variabel sementara
temp = glass1
# Langkah 2: Set glass1 dengan isi glass2
glass1 = glass2
# Langkah 3: Set glass2 dengan isi dari variabel sementara
glass2 = temp

# Day 001 Project - Band Name Generator
print("Welcome to the band generator")
city = input("What the name of the city you grew up in?\n")
name = input("What is your name?\n")
print("Your band name could be " + city + " " + name)