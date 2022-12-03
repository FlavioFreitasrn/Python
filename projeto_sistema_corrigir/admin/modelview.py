from msilib.schema import Class
from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    can_delete = True 
    can_create = True
    can_edit = True
    #REMOVE COLUNAS DA EXIBIÇÃO
    column_exclude_list = ['last_login_at', 'current_login_at', 'last_login_ip', 'current_login_ip', 'login_count', 'confirmed_at']

    #REMOVE CAMPOS DO FORMULARIO
    form_excluded_columns = ['last_login_at', 'current_login_at', 'last_login_ip', 'current_login_ip', 'login_count', 'confirmed_at']
    
    
    create_modal = True
    edit_modal = True
    
    