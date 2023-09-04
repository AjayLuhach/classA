from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class class_model(db.Model):
    __tablename__ = "class"
    name = db.Column(db.String(25),nullable=False)
    rollno = db.Column(db.Integer(),nullable=False,primary_key=True)
    address = db.Column(db.String(255))
    __tableargs__ = {'extend_existing':True}
    
    
    