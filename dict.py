#!/usr/bin/env python3


#This is a dictionary its a a list of key value pairs

ageDict = {"Alex" : "100", "Nick" : "101"}

#you can access the value from the key 
print(ageDict["Alex"])
print(ageDict["Nick"])


#These are lists, there are indexed
names = ["Alex", "Nick", "Shell", "Sebs"]
age = ["100", "101", "102", "103"]
favColor = ["red", "blue", "green", "yellow"]

names2 = ["sdfsdad", "dfsf", "dfsdf", "gfgf", "jdskjdsj"]
age2 = ["dfd", "sd", "1323302", "dssd", "jksdjdks"]
favColor2 = ["gffgd", "blrerweue", "grdfdfseen", "yellerereow", "hdhjshdjsj"]

#this is a list of lists
profile =[names, age, favColor]
profile2 =[names2, age2, favColor2]

#this is a funtion to use the index of the lists to print out the names ages and favcolor
def printProfiles(listOflists):
    count = 0 
    targetCount = len(listOflists[0])
    while count < targetCount :
        subCount = 0
        while subCount <= 2:
            print(listOflists[subCount][count])
            subCount = subCount + 1
        count = count + 1

#this is where you actually call the function and pass it the list to print out
printProfiles(profile)

print("********************************************************************************")

printProfiles(profile2)