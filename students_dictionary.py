

students = []


def add_student(student_id, student_name, student_grade):
    
    for student in students:
        if student['ID'] == student_id:
            print(f"Student ID {student_id} already exists.")
            return
    
    
    new_student = {
        'ID': student_id,
        'Name': student_name,
        'Grade': student_grade
    }
    students.append(new_student)
    print(f" {student_name} added successfully.")


add_student(101, 'Akash', 'A')
add_student(102, 'Madhab', 'B')
add_student(101, 'Abhinash', 'A')  
add_student(104, 'Abhimanyu', 'A+')


print(students)
