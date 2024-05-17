from flask_admin.contrib.sqla import ModelView


class DiagnosaModelView(ModelView):
    form_columns = ['tanggal', 'diagnosa', 'therapy', 'pasien', ]

    pass
 