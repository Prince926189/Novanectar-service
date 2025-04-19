students = {}
 
def accept_student():
     student_id = input("Enter Student ID: ")
     name = input ("Enter Student Name: ")
     age = input("Enter Student Age: ")
     students[student_id] = {"Name": name, "Age": age}
     print("Student added successfully!")
 
def display_students():
     for student_id, info in students.items():
         print(f"ID: {student_id}, Name: {info['Name']}, Age: {info['Age']}")
 
def search_student():
     student_id = input("Enter student ID to search: ")
     name = input ("Enter student name: ") 
     if student_id in students:
         print(f"Found: ID: {student_id}, Name: {students[student_id]['Name']}, Age: {students[student_id]['Age']}")
     else:
         print("Student not found.")
 
def delete_student():
     student_id = input("Enter student ID to delete: ")
     if student_id in students:
         del students[student_id] 
         print("Student deleted successfully.")
     else:
         print("Student not found.")
 
def update_student():
     student_id = input("Enter student ID to update: ")
     if student_id in students:
         name = input("Enter new student name: ")
         age = input("Enter new student age: ")
         students[student_id] = {"Name": name, "Age": age}
         print("Student updated successfully.")
     else:
         print("Student not found.")
 
def main_menu():
     while True:
         print("\nStudent Management System")
         print("1. Accept Student")
         print("2. Display All Students")
         print("3. Search Student")
         print("4. Delete Student")
         print("5. Update Student")
         print("6. Exit")
 
         choice = input("Enter your choice: ")
 
         if choice == '1':
             accept_student()
         elif choice == '2':
             display_students()
         elif choice == '3':
             search_student()
         elif choice == '4':
             delete_student()
         elif choice == '5':
             update_student()
         elif choice == '6':
             print("Exiting the system.")
             break
         else:
             print("Invalid choice, please choose again.")
if __name__ == "__main__":
     main_menu()