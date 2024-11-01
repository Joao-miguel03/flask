from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employeed(db.Model):
    __tablename__ = "table"
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
    def __init__(self, employee_id,name,age,position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"    
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(80),unique = True, nullable = False)
    autor = db.Column(db.String(80), nullable = False)
    num_pags = db.Column(db.Integer, nullable = False)
    editora = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
    
