from sqlalchemy.dialects.postgresql import TEXT

from database import db

class Diagnosa(db.Model):
    __tablename__ = 'diagnosas'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    diagnosa = db.Column(db.String(255), nullable=False)  # Ensure this matches the database column
    tanggal = db.Column(db.Date, nullable=False)  # Assuming there is a 'tanggal' column for date
    therapy = db.Column(db.String(255), nullable=True)  # Assuming there is a 'therapy' column

    pasien_id = db.Column(db.Integer, db.ForeignKey('pasiens.id'), nullable=False)
    pasien = db.relationship('Pasien', back_populates='diagnosas')

    def __init__(self, diagnosa='', tanggal=None, therapy='', pasien_id=None):
        self.diagnosa = diagnosa
        self.tanggal = tanggal
        self.therapy = therapy
        self.pasien_id = pasien_id

    def __repr__(self):
        return f"<Diagnosa {self.diagnosa}>"
