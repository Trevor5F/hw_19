from hw_19.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create_user(self, user):
        user_ent = User(**user)
        self.session.add(user_ent)
        self.session.commit()
        return user_ent


    def update(self, user_data):
        uid = user_data.get('id')

        user = self.get_one(uid)

        user.username = user_data.get('username')
        user.password = user_data.get('password')


    def get_all(self):
        return self.session.query(User).all()


    def get_one(self, uid):
        return self.session.query(User).get(uid)


    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()


