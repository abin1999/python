# Write a Python program to read each row from a given csv file and print a list of strings.

f = open("P3.csv","r")
list = list(f.readlines())
print(list)
