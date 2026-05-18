# Student Grade Analysis System

## 📌 Overview
This project is a Python-based student grade analysis system.  
It reads student exam data from a CSV file, calculates averages, generates rankings, and produces detailed reports and graphs.

The main goal of this project is to automate academic evaluation without using any graphical user interface.

---

## 🎯 Features
- Reads student data from a CSV file
- Calculates:
  - Course averages for each student
  - General average per student
- Creates:
  - Individual student report files (.txt)
  - Course-based ranking files
- Generates:
  - Class success graph
  - Separate graphs for each course
- Organizes all outputs into folders automatically

---

## 📂 Dataset Structure
The CSV file must follow this structure:

- Student number and full name
- Four exam scores for each course:
  - Turkish
  - Mathematics
  - Science
  - Social Studies
  - English

Example columns:

---

## 📁 Output Files
After running the program, the following folders are created:

- `ogrenci_raporlari/`
  - One `.txt` file per student with averages
- `ders_raporlari/`
  - Ranking files for each course
- Graphs are displayed using matplotlib

---

## 🛠 Used Libraries
- pandas
- numpy
- matplotlib
- csv
- statistics
- time
- os

---

## 🚀 How to Run
1. Place the CSV file in the same directory as the script
2. Make sure required libraries are installed
3. Run the Python file
4. Reports and rankings will be generated automatically

---

## 📜 License
This project is licensed under the MIT License.

---

## 👤 Developer
**hypernova-developer**

## Completed
This project is no longer under development.18/05/2026 23:17
