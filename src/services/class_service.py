from src.infrastructure.repository_interface import repository_interface
from src.domain.student import student
class service:
    def __init__(self,session):
        self.repo = repository_interface(session)
        
    def add(self,name,rollno,address):
        new_student = student(name=name,rollno=rollno,address=address)
        return self.repo.add(name,rollno,address)
    def all_student(self):
        return self.repo.all_student()
    def delete_student(self,rollno):
        studentis = self.search_by_rollno(rollno)
        if studentis:
            return self.repo.delete_student(studentis)
        return None
    def search_by_rollno(self,rollno):
        return self.repo.search_by_rollno(rollno)
    def update_student(self,name,rollno,address):
        studentis = self.search_by_rollno(rollno)
        if studentis:
            studentis.name = name
            studentis.rollno = rollno
            studentis.address = address
            self.repo.update_student(studentis)
        return studentis
        
        
    