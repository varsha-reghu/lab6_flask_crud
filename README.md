# Lab 6 – Flask CRUD API for Student Management

This project is a RESTful API built using **Flask** and **SQLite** that performs full CRUD operations on student data.

---

##  Project Structure

lab6_flask_crud/
├── app.py                # Main Flask application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── student.db            # SQLite database file
└── screenshots/          # API testing screenshots

---

##  Features

- Create new student records  
- View student by ID  
- Update student information (including balance)  
- Delete student records  
- View all student entries  

---

##  Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **Thunder Client / Postman**
- **Git & GitHub**
- **VS Code**

---

## API Endpoints

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| POST   | `/student`        | Create a new student     |
| GET    | `/student/<id>`   | View a specific student  |
| PUT    | `/student/<id>`   | Update student info      |
| DELETE | `/student/<id>`   | Delete a student         |
| GET    | `/students`       | View all students        |

---

## How to Run the App

```bash
pip install -r requirements.txt
python app.py

## **Sample Screenshots**

Screenshots for all operations are included in the /screenshots folder:

app_running.png

post_student.png

get_student.png

put_update_balance.png

get_updated_balance.png

delete_student.png

get_all_students.png

github_repo.png


 ## Author

Varsha Reghu
Graduate Certificate
StudentAIDI 2004 – AI in Enterprise Systems
Durham College
