# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Appointment(BaseModel):
#     __tablename__ = 'appointment'

#     date = db.Column(DATE, nullable=False)
#     time = db.Column(TIME, nullable=False)
#     status = db.Column(BOOLEAN, nullable=False)
#     seen = db.Column(BOOLEAN, nullable=False)
    
#     clinic_id = db.Column(VARCHAR(36), ForeignKey('clinic.id'), nullable=False)
#     patient_id = db.Column(VARCHAR(36), ForeignKey('patient.id'), nullable=False)
#     doctor_id = db.Column(VARCHAR(36), ForeignKey('doctor.id'), nullable=False)
#     clinic = relationship("Clinic", back_populates="appointments")
#     patient = relationship("Patient", back_populates="appointments")
#     doctor = relationship("Doctor", back_populates="appointments")
#     messages = relationship("Message", uselist=False, back_populates="appointment")