from authentication import *
print("SUCCESSFUL LOGIN YOU CAN VIEW YOUR DATA.......\n")
file = open("students.txt","r")

id = []
name = []
age = []
location = []

for f in file:
        velue = f.strip().split(" : ")
        id.append(velue[0])
        name.append(str(velue[1]))
        age.append(int(velue[2]))
        location.append(velue[3])

from prettytable import PrettyTable
columns = ['Student id', 'Student Name', 'Student Age', 'Student Location']
mytable = PrettyTable()

mytable.add_column(columns[0], id)
mytable.add_column(columns[1], name)
mytable.add_column(columns[2], age)
mytable.add_column(columns[3], location)

print(mytable , "\n")

print("NO.OF STUDENTS: ",len(name))
print("LOWEST AGE OF STUDENT: ",min(age))
print("HIGHEST AGE OF STUDENT: ",max(age))

