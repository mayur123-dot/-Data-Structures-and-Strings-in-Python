# -Data-Structures-and-Strings-in-Python
# Task 01
# Create a Dictionary of Student Marks
1) Create a Dictionary:
     The program starts by defining a dictionary named student_marks, where:
       Each key is a student's name (e.g., 'Alice'),
       Each value is the corresponding mark (e.g., 85).
       student_marks = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'Diana': 90
       }
2) Get User Input:
     It then prompts the user to enter a student's name using the input() function:
     name = input("Enter the student's name: ")
3) Check if Student Exists:
     The program checks if the entered name exists in the dictionary:
      If found, it prints the student's marks.
      If not found, it shows an appropriate error message.
       if name in student_marks:
          print(f"{name}'s marks: {student_marks[name]}")
       else:
          print("Student not found.")
# Task 02
# Demonstrate List Slicing 
1) Create a List of Numbers
    We use range(1, 11) to generate numbers from 1 to 10, then convert it into a list using list().
     The full list will be:
     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2) Extract the First Five Elements
    Using slicing numbers[:5], we extract the first five elements (from index 0 to 4).

   This results in a new list:
   first_five = [1, 2, 3, 4, 5]
3) Reverse the Extracted Elements
   We apply slicing with a step of -1: first_five[::-1]
    This gives us:
    reversed_five = [5, 4, 3, 2, 1]
4) Print the Results
   The program then prints both the extracted list and the reversed version.
