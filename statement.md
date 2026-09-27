# Problem Statement

## Problem Statement

Educational institutions need a simple way to track which students are
enrolled in which courses and what grades they've earned, without the
overhead of a full web application or paid software. This project builds
a lightweight, terminal-based system that an administrator can run locally
to manage this information.

## Scope of the project

- Manage student records (add, view, update, delete)
- Manage course records (add, view, update, delete)
- Enroll students in courses and record grades
- Generate basic reports: individual transcripts, course rosters, and an
  overall enrollment summary
- Persist all data locally using CSV files (no database server required)
- Out of scope: authentication/multi-user access, a graphical or web
  interface, and integration with external student-information systems

## Target users

- College or course administrators who need a fast, no-install way to track
  enrollments for a single class, cohort, or small department
- Students of the Python Essentials course, as a reference implementation
  of a modular, CLI-based data management application

## High-level features

1. **Student management** — full CRUD on student records
2. **Course management** — full CRUD on course records
3. **Enrollment management** — linking students to courses, with grade
   tracking and the ability to drop an enrollment
4. **Reporting** — transcripts, rosters, and enrollment statistics derived
   from the underlying CSV data
