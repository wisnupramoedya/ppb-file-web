import enum
from flask import request
from datetime import datetime
from sqlalchemy.sql import func
import uuid
from app import db

class Presence(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(55), index=True)
    nik = db.Column(db.String(16), index=True, unique=True)
    image_mask = db.Column(db.String(255))
    mask = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "<Presence '{}' => '{}'>".format(self.id, self.name)

    def as_dict(self):
        result = { c.name: getattr(self, c.name) for c in self.__table__.columns }
        for index, value in result.items():
           if index.startswith("image_"):
               result[index] = request.url_root + value
        return result

