from flask import Flask
from flask_admin import Admin
from database import db
from init import app
from models.pasien import Pasien
from models.diagnosa import Diagnosa
from sqlalchemy.dialects.postgresql import TEXT
from flask_sqlalchemy import SQLAlchemy
from modelview.view_pasien import PasienModelView
from modelview.view_diagnosa import DiagnosaModelView
import os
from flask import Flask, redirect, url_for


# Flask-Admin setup
admin = Admin(app=app, name='Praktek', 
              template_mode='bootstrap3',
              category_icon_classes={'Favorites': 'glyphicon glyphicon-star'})


os.environ['BASE_PATH'] = os.path.abspath(os.getcwd())

# Menu Dashboard
admin.add_view(PasienModelView(Pasien, db.session))
admin.add_view(DiagnosaModelView(Diagnosa, db.session))


@app.route('/')
def index():
    return redirect(url_for('admin.index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        pass

    # Start app
    app.run(debug=True,
            port=8000)
