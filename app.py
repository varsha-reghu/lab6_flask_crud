from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Student model
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    amount_due = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "amount_due": self.amount_due
        }


# Create database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Welcome to the Student CRUD API"

# Create a new student
@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        student_id=data['student_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        amount_due=data['amount_due']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

# Get a student by ID
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify(student.to_dict())

# Update a student by ID
@app.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    student.first_name = data['first_name']
    student.last_name = data['last_name']
    student.dob = data['dob']
    student.amount_due = data['amount_due']

    db.session.commit()
    return jsonify(student.to_dict())

# Delete a student by ID
@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})

# Get all students
@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
