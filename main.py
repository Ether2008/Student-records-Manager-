import os

FILE_NAME = "students_data.txt"

# --- UTILS ---
def display_menu():
    print("\n--- Student Record Management ---")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Delete a Student")
    print("4. View Class Average")
    print("5. Exit")

def get_valid_score():
    while True:
        score_input = input("Enter student score (0-100): ")
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        else:
            print("Error: Please enter a valid number.")

# --- FILE HANDLING ---
def save_data(students_dict):
    file = open(FILE_NAME, "w")
    for roll_no, details in students_dict.items():
        file.write(f"{roll_no},{details['name']},{details['score']}\n")
    file.close()

def load_data():
    students_dict = {}
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                roll_no = parts[0]
                name = parts[1]
                score = int(parts[2])
                students_dict[roll_no] = {"name": name, "score": score}
        file.close()
    return students_dict

# --- STUDENT OPERATIONS (CRUD) ---
def add_student(students_dict):
    roll_no = input("Enter Roll Number: ")
    if roll_no in students_dict:
        print("Student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ")
    score = get_valid_score()
    
    students_dict[roll_no] = {"name": name, "score": score}
    print(f"Student {name} added successfully!")

def view_students(students_dict):
    if not students_dict:
        print("No student records found.")
        return
        
    print("\n--- Student List ---")
    for roll_no, details in students_dict.items():
        print(f"Roll No: {roll_no} | Name: {details['name']} | Score: {details['score']}")

def delete_student(students_dict):
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in students_dict:
        deleted_student = students_dict.pop(roll_no)
        print(f"Student {deleted_student['name']} deleted.")
    else:
        print("Student not found.")

# --- ANALYTICS ---
def show_class_average(students_dict):
    if not students_dict:
        print("No data available to calculate average.")
        return
        
    total_score = 0
    count = 0
    
    for details in students_dict.values():
        total_score += details["score"]
        count += 1
        
    average = total_score / count
    print(f"\nThe average score of the class is: {average:.2f}")

# --- MAIN EXECUTION ---
def main():
    # Load existing data on startup
    students = load_data()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student(students)
            save_data(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            delete_student(students)
            save_data(students)
        elif choice == '4':
            show_class_average(students)
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()