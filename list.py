#!/usr/bin/env python3
#This is a list it is indexed 
names = ["Alex", "Nick", "Shell", "Sebs"]

#This is a for loop it will run through the list and print out each value
for name in names:
    print(name)

yourName = input("what is your name : ")

names.append(yourName)

for name in names:
    print(name)

#This is how you access a single value in a list via the index
print(names[1])



