# Student & Course Management System

A command-line application for managing students, courses, and enrollments,
built as the flipped-course project for **Python Essentials**.

## Overview

The system lets an administrator maintain student and course records, enroll
students into courses, assign grades, and pull simple reports (transcripts,
rosters, enrollment summaries) — all from a terminal menu, with data
persisted to local CSV files.

## Features

- **Student management** — add, view, update, delete
- **Course management** — add, view, update, delete
- **Enrollment management** — enroll a student in a course, assign a grade,
  drop an enrollment
- **Reporting** — per-student transcript, per-course roster, overall
  enrollment summary (including most popular course)
- Input validation (e.g. email format, numeric credits) with clear error
  messages
- Action logging to `data/activity.log`
- Unit tests for the core managers

## Technologies / tools used

- Python 3.8+
- Standard library only: `csv`, `dataclasses`, `logging`, `re`, `uuid`,
  `unittest` — no external dependencies required

## Project structure

```
student_course_management/
├── main.py                      # CLI entry point
├── app/
│   ├── __init__.py
│   ├── models.py                 # Student, Course, Enrollment data classes
│   ├── storage.py                # generic CSV read/write layer
│   ├── utils.py                  # validation + logging helpers
│   ├── student_manager.py        # student CRUD
│   ├── course_manager.py         # course CRUD
│   ├── enrollment_manager.py     # enrollment logic
│   └── reports.py                # analytics/reporting
├── data/                          # CSV data + activity.log (created at runtime)
├── tests/
│   ├── test_student_manager.py
│   └── test_course_manager.py
├── statement.md
├── requirements.txt
└── README.md
```

## Setup and installation

1. **Install Python 3.8 or later.** Check your version:
   ```bash
   python --version
   ```
2. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
3. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   (The file is present for completeness; the project currently uses only
   the Python standard library, so this step installs nothing.)

## Running the project

From the project root:

```bash
python main.py
```

You'll see a numbered menu. Enter the number of the action you want and
follow the prompts. Data is saved automatically to CSV files under `data/`,
which are created on first run.

## Running the tests

```bash
python -m unittest discover tests -v
```

All tests use a separate throwaway CSV file so they never touch your real
data.

## Example workflow

1. Choose `1` to add a student.
2. Choose `5` to add a course.
3. Choose `9` to enroll that student in that course.
4. Choose `10` to record a grade for the enrollment.
5. Choose `13` to view that student's transcript, or `15` for the overall
   enrollment summary.
