from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/employee.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    document = db.Column(db.String(200))
    age = db.Column(db.String(200))
    email = db.Column(db.String(200))
    profession = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    position = db.Column(db.String(200))
    salary = db.Column(db.Integer)
    state = db.Column(db.Boolean)

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('index.html', employees = employees)

@app.route('/createEmployee', methods=['POST']) 
def create():
    employee = Employee(
        name=request.form['name'],
        lastName=request.form['lastName'],
        document=request.form['document'],
        age=request.form['age'],
        email=request.form['email'],
        profession=request.form['profession'],
        phone=request.form['phone'],
        position=request.form['position'],
        salary=request.form['salary'],
        state=False
    )

    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    Employee.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:id>')
def edit_user(id):
    employee = Employee.query.get(id)
    return render_template('edit.html', employee=employee)

@app.route('/done/<id>')
def done(id):
    employee = Employee.query.filter_by(id=int(id)).first()
    employee.done = not(employee.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=["POST"])
def update_user(id):
    employee = Employee.query.filter_by(id=int(id)).first()
    name=request.form.get('name')
    lastName=request.form.get('lastName')
    document=request.form.get('document')
    age=request.form.get('age')
    email=request.form.get('email')
    profession=request.form.get('profession')
    phone=request.form.get('phone')
    position=request.form.get('position')
    salary=request.form.get('salary')
    print(name)

    db.session.commit()

    return redirect('/')

if __name__ == '__name__':
    app.run(debug=True)
