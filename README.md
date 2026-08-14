# Accuknox Assignments

This repository contains the Accuknox assignment work. The `AIML` folder holds three
Python tasks demonstrating API data retrieval, data processing, visualization, and
database operations. The `PM-tasks` folder holds the product management assignment
material.

## AIML Tasks

### 1. API Data Retrieval and Storage
- Fetches book data from an external REST API.
- Stores the retrieved data in a local SQLite database.
- Retrieves and displays the stored book information.

### 2. Data Processing and Visualization
- Fetches student score data from an API.
- Displays sample student scores.
- Calculates the average math score.
- Creates a bar chart to visualize the scores.

### 3. CSV Data Import to Database
- Reads user information from a CSV file.
- Creates a SQLite database and users table.
- Inserts the CSV data into the database.
- Retrieves and displays the stored user information.

## Technologies Used

- Python
- REST APIs
- SQLite
- CSV
- Matplotlib

## Repository Structure

```text
Accuknox-Assignments/
│
├── AIML/
│   ├── Task1_API_Data_Retrieval/
│   │   ├── task1_books.py
│   │   └── books.db
│   │
│   ├── Task2_Data_Processing_Visualization/
│   │   └── task2_student_scores.py
│   │
│   └── Task3_CSV_Data_Import/
│       ├── task3_csv_database.py
│       ├── users.csv
│       └── users.db
│
├── PM-tasks/
│   └── Accuknox PM assignment.pdf
│
└── README.md
```

## How to Run

Each script uses paths relative to its own folder, so run it from inside that folder:

```bash
cd AIML/Task1_API_Data_Retrieval && python task1_books.py
cd AIML/Task2_Data_Processing_Visualization && python task2_student_scores.py
cd AIML/Task3_CSV_Data_Import && python task3_csv_database.py
```

Tasks 1 and 2 require an internet connection. Install the dependencies with:

```bash
pip install requests matplotlib
```