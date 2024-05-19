# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class User(BaseModel):
#     __tablename__ = 'user'

#     name = db.Column(VARCHAR(100), nullable=False)
#     email = db.Column(VARCHAR(100), nullable=False)
#     password = db.Column(VARCHAR(255), nullable=False)
    
#     doctor_id = db.Column(VARCHAR(36), ForeignKey('doctor.id'), unique=True)
#     clinic_id = db.Column(VARCHAR(36), ForeignKey('clinic.id'), unique=True)
#     doctor = relationship("Doctor", back_populates="user")
#     clinic = relationship("Clinic", back_populates="user")
#     roles = relationship("Role", uselist=False, back_populates="user")