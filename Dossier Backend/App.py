from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from flask_babel import Babel

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
mongo = PyMongo(app)
babel = Babel(app)

from routes import auth, job_scraping, job_applications, user_profile
from models import user, job_offer, application

if __name__ == '__main__':
    app.run(debug=True)
  
