from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# from models.user import User
# from models.doctor import Doctor
# from models.patient import Patient
# from models.appointment import Appointment
# from models.clinic import Clinic
# from models.message import Message
# from models.specialization import Specialization
# from models.governorate import Governorate
# from models.role import Role

# classes = {
#     "User": User,
#     "Doctor": Doctor,
#     "Patient": Patient,
#     "Appointment": Appointment,
#     "Clinic": Clinic,
#     "Message": Message,
#     "Specialization": Specialization,
#     "Governorate": Governorate,
#     "Role": Role
# }


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import routes 
    # import blueprints

    return app
