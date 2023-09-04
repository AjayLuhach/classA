from src.domain.models.class_model import db,class_model
from src.domain.student import student

class repository_interface:
    def __init__(self, session):
        self.session = session
    def add(self,name,rollno,address):
        new_student = class_model(name=name,rollno=rollno,address=address)
        db.session.add(new_student)
        db.session.commit()
        
    def search_by_rollno(self,rollno):
        studentis = self.session.query(class_model).filter_by(rollno=rollno).first()
        return studentis
    
    def delete_student(self,rollno):
        self.session.delete(rollno)
        self.session.commit()
            
    def update_student(self,studentis):
        db.session.commit()
        
    def all_student(self):
       return self.session.query(class_model).all()
        
        
        

