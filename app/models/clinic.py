# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Clinic(BaseModel):
#     __tablename__ = 'clinic'
    
#     name = db.Column(VARCHAR(100), nullable=False)
#     phone = db.Column(INTEGER, nullable=False)
#     email = db.Column(VARCHAR(100), nullable=False)
#     address = db.Column(VARCHAR(255), nullable=False)
#     working_hours = db.Column(TIME, nullable=False)
#     photo = db.Column(VARCHAR(255))
    
#     governorate_id = db.Column(VARCHAR(36), ForeignKey('governorate.id'), nullable=False)
#     user = relationship("User", uselist=False, back_populates="clinic")
#     governorate = relationship("Governorate", back_populates="clinics")
#     doctors = relationship("Doctor", back_populates="clinic")
#     appointments = relationship("Appointment", back_populates="clinic")
    