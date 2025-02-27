from flask import Flask, render_template, request, redirect, jsonify
from forms import get, myform
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

DATABASE_URL = 'sqlite:///DB.db'
app = Flask(__name__)
app.config['SECRET_KEY'] = '24681012'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Patient(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    confirmpassword = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"patient('{self.username}')"

with app.app_context():
    db.create_all()

patients = []

@app.route('/', methods=['GET', 'POST'])
def register():
    form = myform()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    
    elif request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirmpassword = form.confirmpassword.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        user_id = form.user_id.data
        birthdate = form.birthdate.data
        
        patient = Patient.query.filter_by(user_id=user_id).first()
        if patient:
            return "Patient has already registered"
        else:
            new_patient = Patient(username=username, email=email, password=password, confirmpassword=confirmpassword, firstname=firstname, lastname=lastname, user_id=user_id, birthdate=birthdate)
            db.session.add(new_patient)
            db.session.commit()
            return redirect('/commoninfo/fetch')

@app.route('/commoninfo/fetch', methods=['GET', 'POST'])
def get_patient():
    form = get()
    if request.method == 'GET':
        return render_template('patient.html', form=form)
    if request.method == 'POST':
        user_id = form.user_id.data
        patient = Patient.query.filter_by(user_id=user_id).first()
        if patient:
            return f"Patient name: {patient.username}, user_id: {patient.user_id}, birthdate: {patient.birthdate.strftime('%Y-%m-%d')}"
        else:
            return "No patient found"

if __name__ == '__main__':    
    app.run(host="0.0.0.0", port=5000, debug=True)
