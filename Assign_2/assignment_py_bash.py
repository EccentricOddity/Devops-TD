

# 1 Grade Checker
def grade_checker():
    score = int(input("Enter your score: "));
    grade = ""
    if score >= 90:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "F"
    print("Your grade is: " + grade)

# 2 Student grades
def student_grades():
    _student_grades = {}
    while True:
        _command = input("Enter 'add' to add a student, 'update' to update a student's score, or 'print' to print all students' grades, or 'exit' to exit: ").lower()
        if _command == "exit":
            print("Exiting the program.")
            break

        if _command == "add":
            _student_name = input("Enter student's name: ")
            _student_score = int(input("Enter student's score: "))
            _student_grades[_student_name] = _student_score
        

        elif _command == "update":
            _student_name = input("Enter student's name: ")
            if _student_name in _student_grades:
                _student_score = int(input("Enter student's new score: "))
                _student_grades[_student_name] = _student_score
            else:
                print("Student not found.")
        
    
        elif _command == "print":
            for name, score in _student_grades.items():
                print(f"{name}: {score}")
        
        else:
            print("Invalid command.")

#3. Write to a File
def create_file():
    file = open("output.txt", "w")
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.close()


#4 Read from a File
def read_file():
    try:
        file = open("output.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found. Please create the file first.")

__super_command = input("Enter 'grade' to check a grade, 'student' to manage student grades, 'write' to create a file, or 'read' to read from a file: and 'exit' to exit: ").lower()
while True:
    if __super_command == "exit":
        print("Exiting the program.")
        break
    if __super_command == "grade":
        grade_checker()
        break
    elif __super_command == "student":
        student_grades()
        break
    elif __super_command == "write":
        create_file()
        print("File created successfully.")
        break
    elif __super_command == "read":
        read_file()
        break
    else:
        print("Invalid command. Please try again.")
        __super_command = input("Enter 'grade' to check a grade, 'student' to manage student grades, 'write' to create a file, or 'read' to read from a file: ").lower()

