# app/__init__.py
from flask import Flask
from src.domain.models.class_model import db
from src.controlers.class_controler import class_controler
from src.infrastructure.repository_interface import repository_interface
from src.services.class_service import service

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

# Register the controller blueprint
app.register_blueprint(class_controler, url_prefix='/')

cl_service = service(db.session)    


if __name__ == "__main__":
     
    app.run(debug=True)
 
