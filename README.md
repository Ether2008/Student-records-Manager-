# Student Record Management System

Welcome to my Python basics project. I built this lightweight, command-line application as my final submission for the VITyarthi flipped course evaluation.

Instead of relying on heavy frameworks, this project showcases core Python fundamentals. It is a simple, crash-resistant tool designed for educators and administrators to manage student scores, calculate class averages, and securely store data locally from the terminal.

## Features

The functionality is broken down into three main modules:

1. **User Management :**

   * Add new students with their roll numbers, names, and scores.

   * View a formatted list of all registered students.

   * Delete records when a student leaves the class.

2. **Reporting & Analytics:**

   * Calculate the current class average based on saved scores.

3. **Persistent Storage:**

   * Automatically save all records to a local text file (`students_data.txt`) and load them upon the next startup to prevent data loss.

## How to Run It Locally

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/student-record-manager.git
   
   ```

2. **Navigate to the project folder:**

   ```
   cd student-record-manager
   
   ```

3. **Run the main script:**

   ```
   python main.py
   
   ```

   *(Note: Ensure you have Python installed on your system)*

## Project Structure

To maintain clean and modular code, the logic is split into multiple files:

* `main.py` - The central execution script that runs the program loop.

* `utils.py` - Handles the visual menus and user input validation.

* `student_operations.py` - Manages adding, viewing, and deleting students.

* `analytics.py` - Processes data for reporting features.

* `file_handler.py` - Manages reading from and writing to the local text database.

## Non-Functional Requirements Addressed

To ensure reliability and performance, this project focuses on:

* **Usability:** A simple, number-based menu interface that is easy to navigate.

* **Error Handling:** Built-in validation loops prevent the program from crashing if a user enters invalid data (e.g., text instead of a numeric score).

* **Maintainability:** A modular architecture ensures that future updates (like changing the storage method) require minimal code changes.
