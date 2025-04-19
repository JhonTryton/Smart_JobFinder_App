from . import auth, job_scraping, job_applications, user_profile
from app import app

app.register_blueprint(auth.auth_bp)
app.register_blueprint(job_scraping.job_scraping_bp)
app.register_blueprint(job_applications.job_applications_bp)
app.register_blueprint(user_profile.user_profile_bp)
