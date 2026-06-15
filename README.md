# Student Management System

1. PROJECT OVERVIEW
StudentManager is a structured data management system built in Python using built-in modules. It demonstrates the fundamental pipeline of CRUD operations with data persistence using JSON. The system uses auto ID generation + grade calculation + search/filter for enhanced usability.

This project satisfies the "TASK 7 SPECIFICATION: STUDENT MANAGEMENT SYSTEM" requirements for a validated structured student data system.

2. FEATURES & REQUIREMENTS MET

ADD STUDENT: Auto-generates unique ID and captures name, age, marks
UPDATE STUDENT: Modifies existing records with validation and auto grade recalc
DELETE STUDENT: Removes records with confirmation prompt
STORAGE OPTION: File (JSON) - `students.json` stores all records persistently
VALIDATION: Age and marks validation prevents invalid data entry
ENHANCEMENT: Search by ID/name + filter by grade + backup + class analytics

3. HOW TO RUN

Prerequisites:
- Python 3.9+ installed

Steps:
1. Open terminal and run: python student_manager.py
2. Select options 1-8 from the menu
3. Data auto-saves to students.json after every operation
4. Use option 7 to create timestamped backups

4. PROJECT STRUCTURE

student_management_system/
├── student_manager.py - Main CRUD pipeline logic
├── students.json - Auto-generated data file
├── backup_*.json - Auto-generated backup files
└── README.md - This file

5. HOW IT WORKS - THE IPO MODEL
1. Input: `input()` captures student details. `json.load()` reads existing data
2. Process: `calculate_grade()` converts marks to A+ to F. `generate_id()` creates unique ID
3. Output: Formatted table displays records. `json.dump()` saves to file

6. KEY CONCEPTS DEMONSTRATED
1. CRUD Operations: Create, Read, Update, Delete implemented for student records
2. Data Persistence: JSON file ensures data survives program restart
3. Data Validation: Try/except blocks prevent invalid age/marks entry
4. Auto Computation: Grade and average calculated automatically from marks
5. Data Integrity: Confirmation on delete + timestamped backups prevent data loss
6. Search & Filter: Linear search by ID/name + grade-based filtering

