from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from models.diagnosa import Diagnosa

class PasienModelView(ModelView):

    
    
    form_excluded_columns = ('created_at', 'updated_at')
    
    column_auto_select_related = True

    # Customize form field types or widgets if needed
    form_overrides = {
        'deskripsi': TextAreaField
    }

    


