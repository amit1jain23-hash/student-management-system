# Student Management System

A web-based Student Management System built using Flask and PostgreSQL.

## Features

* Add new students
* View all student records
* Search students by name
* Update student details
* Delete student records
* Dashboard showing total number of students
* Responsive user interface using HTML and CSS

## Technologies Used

* Python
* Flask
* PostgreSQL
* HTML
* CSS
* Jinja2

## Project Structure

student-management-system/

├── app.py

├── db.py

├── requirements.txt

├── static/

│   └── style.css

├── templates/

│   ├── index.html

│   ├── add_student.html

│   ├── view_students.html

│   ├── edit_student.html

│   └── search_student.html

└── README.md

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure PostgreSQL database in `db.py`

6. Run the application

```bash
python app.py
```

7. Open in browser

```text
http://127.0.0.1:5000
```

## Author

Amit Jain
