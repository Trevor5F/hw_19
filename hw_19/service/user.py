import hashlib
import base64
import hmac

from hw_19.dao.user import UserDAO
from hw_19.helpers.constants import PWD_SALT, PWD_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)


    def get_user_by_username(self,username):
        return self.dao.get_user_by_username(username)


    def get_all(self):
        return self.dao.get_all()


    def delete(self, uid):
        self.dao.delete(uid)


    def create_user(self, user):
        user["password"] = self.get_hash(user["password"])
        return self.dao.create_user(user)


    def update(self, user_data):
        user_data["password"] = self.get_hash(user_data["password"])
        self.dao.update(user_data)


    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )

        return base64.b64encode(hash_digest)



    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)





