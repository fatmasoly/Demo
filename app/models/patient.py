# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Patient(BaseModel):
#     __tablename__ = 'patient'

#     name = db.Column(VARCHAR(100), nullable=False)
#     phone = db.Column(INTEGER, nullable=False)
#     email = db.Column(VARCHAR(100), nullable=False)
    
#     appointments = relationship("Appointment", back_populates="patient")