from student_manager import add_student, list_students, update_student, delete_student
from database import create_table

def main():
    create_table()
    
    while True:
        print("\n--- Gestión de Estudiantes ---")
        print("1. Agregar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            name = input("Nombre: ")
            lastname = input("Apellido: ")
            age = int(input("Edad: "))
            grade = float(input("Nota: "))
            add_student(name, lastname, age, grade)
        
        elif choice == "2":
            students = list_students()
            for student in students:
                print(student)
        
        elif choice == "3":
            student_id = int(input("ID del estudiante a actualizar: "))
            name = input("Nuevo nombre: ")
            lastname = input("Nuevo apellido: ")
            age = int(input("Nueva edad: "))
            grade = float(input("Nueva nota: "))
            update_student(student_id, name, lastname, age, grade)
        
        elif choice == "4":
            student_id = int(input("ID del estudiante a eliminar: "))
            delete_student(student_id)
        
        elif choice == "5":
            break
        
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()