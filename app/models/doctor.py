# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Doctor(BaseModel):
#     __tablename__ = 'doctor'
    
#     name = db.Column(VARCHAR(100), nullable=False)
#     phone = db.Column(INTEGER, nullable=False)
#     email = db.Column(VARCHAR(100), nullable=False)
#     photo = db.Column(VARCHAR(255))
#     price = db.Column(VARCHAR(50))
    
#     specialization_id = db.Column(VARCHAR(36), ForeignKey('specialization.id'), nullable=False)
#     clinic_id = db.Column(VARCHAR(36), ForeignKey('clinic.id'), nullable=False)
#     user = relationship("User", uselist=False, back_populates="doctor")
#     specialization = relationship("Specialization", back_populates="doctors")
#     clinic = relationship("Clinic", back_populates="doctors")
#     appointments = relationship("Appointment", back_populates="doctor")
