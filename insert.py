from authentication import *
print("SUCCESSFUL LOGIN PLEASE ENTER YOUR DATA.......\n")
file = open("students.txt", "a")

i = 0
while i < 3:

    stndid = input("ENTER YOUR STUDENTS ID:-")
    stndname = input("ENTER YOUR STUDENT NAME:-")
    stndage = input("ENTER YOUR STUDENT AGE:-")
    stndlocation = input("ENTER YOUR STUDENT LOCATION:-")

    alldata = stndid + " : " + stndname + " : " + stndage + " : " + stndlocation
    file.write(alldata + "\n")
    print("LETS GO NEXT.....\n")
    i = i + 1

file.close()
print("THREE DATA STORE SUCCESSFULLY....")