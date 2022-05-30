from flask import request
from flask_restx import Resource, Namespace

from hw_19.dao.model.user import UserSchema
from hw_19.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200


    def post(self):
        req_json = request.json
        user_service.create_user(req_json)
        return '', 201



@user_ns.route('/<int:uid>')
class UserView(Resource):

    def put(self, uid: int):

        data = request.json
        if "id" not in data:
            data["id"] = uid
        user_service.update(data)
        return '', 201

    # @admin_required
    def delete(self, uid: int):
        user_service.delete(uid)

        return '', 204


