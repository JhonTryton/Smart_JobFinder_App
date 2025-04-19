from app import mongo

class JobOffer:
    def __init__(self, title, company, location, url, date_posted=None, deadline=None, contact_email=None, _id=None):
        self.title = title
        self.company = company
        self.location = location
        self.url = url
        self.date_posted = date_posted
        self.deadline = deadline
        self.contact_email = contact_email
        self.id = _id

    def save(self):
        job_data = {'title': self.title, 'company': self.company, 'location': self.location, 'url': self.url, 'date_posted': self.date_posted, 'deadline': self.deadline, 'contact_email': self.contact_email}
        if self.id:
            mongo.db.job_offers.update_one({'_id': self.id}, {'$set': job_data})
        else:
            result = mongo.db.job_offers.insert_one(job_data)
            self.id = result.inserted_id

    @staticmethod
    def get_all():
        offers = mongo.db.job_offers.find()
        return [JobOffer(**offer) for offer in offers]

    def to_dict(self):
        return {
            '_id': str(self.id),
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'url': self.url,
            'date_posted': self.date_posted,
            'deadline': self.deadline,
            'contact_email': self.contact_email
        }
      
