
from sqlalchemy.dialects.postgresql import TEXT

from database import db


class Diagnosa(db.Model):
    __tablename__ = 'diagnosas'

    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.TIMESTAMP(timezone=True), default=db.func.now())
    diagnosa = db.Column(TEXT)  # Corrected column name
    therapy = db.Column(db.String(100))
    pasien_id = db.Column(db.Integer, db.ForeignKey('pasiens.id'), nullable=False)
    pasien = db.relationship("Pasien", back_populates="diagnosa")  # Adjusted back_populates
