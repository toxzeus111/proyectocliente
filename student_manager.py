from database import create_connection

def add_student(name, lastname, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, lastname, age, grade) VALUES (?, ?, ?, ?)",
                   (name, lastname, age, grade))
    conn.commit()
    conn.close()

def list_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def update_student(student_id, name, lastname, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE students SET name = ?, lastname = ?, age = ?, grade = ? 
                      WHERE id = ?''', (name, lastname, age, grade, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()