# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Specialization(BaseModel):
#     __tablename__ = 'specialization'
    
#     specialization_name = db.Column(VARCHAR(100), nullable=False)
#     doctors = relationship("Doctor", back_populates="specialization")