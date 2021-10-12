from flask_restx import Namespace, fields

class SuperAdminDto:
    api = Namespace('superAdmin', description='SuperAdmin Related operation')
    get_data = api.model('get_data', {
        'input_data_path': fields.String(required=True,description='location of Input data')
    })