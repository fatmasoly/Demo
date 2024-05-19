# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Governorate(BaseModel):
#     __tablename__ = 'governorate'

#     governorate_name = db.Column(VARCHAR(100), nullable=False)
#     clinics = relationship("Clinic", back_populates="governorate")