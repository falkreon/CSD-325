# CSD325: Advanced Python
# Module 8.2 Assignment: JSON Practice
# Isaac Ellingson
# 11/20/2025

import json

STUDENTS_FILE = 'student.json'

def list_students(students):
    for student in students:
        print("  " +
            (student['L_Name'] + ", " + student['F_Name']).ljust(18) +
            " : ID = " + str(student['Student_ID']).ljust(6) +
            ", Email = " + student["Email"]
            )


# Open and list out the file
with open(STUDENTS_FILE) as f:
    students = json.load(f)

print("This is the original student list:")
list_students(students)

# Modify the data
students.append({
    'L_Name' : 'Ellingson',
    'F_Name' : 'Isaac',
    'Student_ID': 70764,
    'Email': 'falkreon@example.com'
    })

# Display the modified data
print()
print("This is the updated student list:")
list_students(students)

# Dump the data back out to the file
with open(STUDENTS_FILE, 'w') as f:
    json.dump(students, f, indent=4)

print("The json file was updated.")
