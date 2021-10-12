from app.main.service.stage_01_load_and_save import get_data, get_data_new
from app.main.util.authDto import AuthDto
from flask import request
from flask_restx import Resource
from app.main.util.superadminDto import SuperAdminDto
api = SuperAdminDto.api
_get_data = SuperAdminDto.get_data

@api.route('/get_data')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @api.doc('load data')
    @api.expect(_get_data, validate=True)
    def post(self):
        """Logs in existing users"""
        #get post data
        post_data = request.json
        return get_data_new(data=post_data)