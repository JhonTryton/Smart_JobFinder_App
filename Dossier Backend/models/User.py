from app import mongo

class User:
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self.id = _id

    def save(self):
        user_data = {'username': self.username, 'email': self.email, 'password': self.password}
        if self.id:
            mongo.db.users.update_one({'_id': self.id}, {'$set': user_data})
        else:
            result = mongo.db.users.insert_one(user_data)
            self.id = result.inserted_id

    @staticmethod
    def find_by_email(email):
        user = mongo.db.users.find_one({'email': email})
        if user:
            return User(user['username'], user['email'], user['password'], user['_id'])
        return None

    @staticmethod
    def find_by_id(user_id):
        user = mongo.db.users.find_one({'_id': user_id})
        if user:
            return User(user['username'], user['email'], user['password'], user['_id'])
        return None
      
