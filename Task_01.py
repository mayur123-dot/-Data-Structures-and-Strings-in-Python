student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95 
}
name=input("Enter the name of the student: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student {name} not found.")    