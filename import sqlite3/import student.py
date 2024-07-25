import sqlite3
conn=sqlite3.connect("school.db")
c=conn.cursor()
c.execute('''CREATE  TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   class TEXT NOT NULL
                   )''')
def add_student(namee,student_class):
    c.execute("INSERT INTO students (name, class) VALUES (?,?)", (name, student_class))
    conn.commit()
    print("Student addd successfullyy.")
def get_students_by_class(student_class):
    c.execute("SELECT*FROM students WHERE class=?",(student_class,))
    students=c.fetchall()
    if students:
        for student in students:
            print(f"ID:{student[0]}, Name: {student[1]}, class: {student[2]}")
    else:
        print("NO students found  for the given class.")
def delete_student (student_id):
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")
def update_student_class(student_id, new_class):
    c.execute("UPDATE students SET class=? WHERE id=?", (new_class, student_id))
    conn.commit()
        name=input("Enter student class:")
        student_class = input("Enter student class: ")
        add_student(name, student_class)
    elif choice == "2":
        student_class = input("Enter class to retrieve students: ")
        get_students_by_class(student_class)
    elif choice == "3":
        student_id = input("Enter student ID to delete:")
        delete_student(student_id)
    elif choice == "4":
        student_id = input("Enter student ID to update class:")
        new_class = input("Enter new class: ")
        update_student_class(student_id, new_class)
    elif choice == "5":
        break
conn.close()    
