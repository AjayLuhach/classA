from flask import jsonify,Blueprint,request
from src.services.class_service import service 
from src.domain.models.class_model import db

cl_service = service(db.session)
class_controler = Blueprint('class_controler',__name__)


# # curl -X POST -H "Content-Type: application/json" -d '{
#   "name": "Anuj",
#   "rollno": "2",
#   "address": "Rohtak"
# }' http://localhost:5000/add
@class_controler.route('/add',methods=['POST'])
def add():
    data = request.get_json()
    name = data.get('name')
    rollno = data.get('rollno')
    address = data.get('address')
    new_student = cl_service.add(name,rollno,address)
    return f"Created student: {name}"

#curl command to delete curl -X DELETE http://localhost:5000/delete/1
@class_controler.route('/delete/<int:rollno>',methods=['DELETE'])
def delete(rollno):    
    cl_service.delete_student(rollno)
    return f"Deleted student: {rollno}"

#localhost:5000/students
@class_controler.route('/students', methods=['GET'])
def all_students():
    students = cl_service.all_student()
    student_list = [{"name": student.name, "rollno":student.rollno,"address":student.address} for student in students]
    return jsonify(student_list)

@class_controler.route('/update/<int:rollno>', methods=['PUT'])
def update_student(rollno):
    data = request.json
    name = data.get('name')
    rollno = data.get('rollno')
    address = data.get('address')

    # Update the student using servic 
    # curl -X PUT -H "Content-Type: application/json" -d '{"name": "Ajay", "rollno": "12345", "address": "jind"}' http://localhost:5000/update/2
    updated_student = cl_service.update_student(name,rollno,address)
    

    if updated_student:
        return f"Updated todo: {updated_student.name}"
    else:
        return "Todo not found", 404

# curl -X PUT -H "Content-Type: application/json" -d '{
#     "name": "New Name",
#     "rollno": "12345",
#     "address": "New Address"
# }' http://localhost:5000/update/12345
