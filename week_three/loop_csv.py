#!/usr/bin/python

price = "82.67"

new_csv = open("test.csv", "r")
# first_line = new_csv.readline()

first_line = ""
first_loop = True
for line in new_csv:
    if (first_loop):
        first_line = line
        first_loop = False
    else:
        info = line.split(", ")
        #print(info)
        if (info[2] == price):
            print(info[0])
        else:
            print("None were found") 
#print(first_line)
