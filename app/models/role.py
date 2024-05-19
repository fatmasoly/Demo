# from app import db
# from models.base import BaseModel
# from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, BOOLEAN, DATE, TIME, TEXT
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# class Role(BaseModel):
#     __tablename__ = 'roles'

#     user_id = db.Column(VARCHAR(36), ForeignKey('user.id'), nullable=False, unique=True)
#     role = db.Column(VARCHAR(50), nullable=False)
#     user = relationship("User", back_populates="roles")