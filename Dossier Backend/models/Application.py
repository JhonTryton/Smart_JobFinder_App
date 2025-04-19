from app import mongo
from bson.objectid import ObjectId

class Application:
    def __init__(self, user_id, job_id, cv_path=None, letter_path=None, submission_date=None, _id=None):
        self.user_id = user_id
        self.job_id = job_id
        self.cv_path = cv_path
        self.letter_path = letter_path
        self.submission_date = submission_date
        self.id = _id

    def save(self):
        app_data = {'user_id': self.user_id, 'job_id': self.job_id, 'cv_path': self.cv_path, 'letter_path': self.letter_path, 'submission_date': self.submission_date}
        if self.id:
            mongo.db.applications.update_one({'_id': self.id}, {'$set': app_data})
        else:
            result = mongo.db.applications.insert_one(app_data)
            self.id = result.inserted_id

    @staticmethod
    def find_by_user_id(user_id):
        applications = mongo.db.applications.find({'user_id': user_id})
        return [Application(**app
      
