from database import db

class Pasien(db.Model):
    __tablename__ = 'pasiens'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    umur = db.Column(db.Integer)
    pekerjaan = db.Column(db.String(100))
    alamat = db.Column(db.String(100))
    phone = db.Column(db.String(15), nullable=False, index=True)
    
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.now(), onupdate=db.func.now())
    is_active = db.Column(db.Boolean, default=True)

    diagnosas = db.relationship('Diagnosa', back_populates='pasien', lazy='dynamic')

    def __init__(self, nama='', umur=None, pekerjaan='', alamat='', phone=''):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.alamat = alamat
        self.phone = phone

    def __repr__(self):
        return f"<Pasien {self.nama}>"


