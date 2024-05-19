# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Message(BaseModel):
#     __tablename__ = 'message'

#     message_body = db.Column(TEXT, nullable=False)
#     status = db.Column(BOOLEAN, nullable=False)
    
#     appointment_id = db.Column(VARCHAR(36), ForeignKey('appointment.id'), nullable=False, unique=True)
#     appointment = relationship("Appointment", back_populates="messages")