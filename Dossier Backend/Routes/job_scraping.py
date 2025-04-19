from flask import Blueprint, jsonify
from utils.scraper import scrape_jobs  # Supposons une fonction de scraping

job_scraping_bp = Blueprint('job_scraping', __name__, url_prefix='/jobs')

@job_scraping_bp.route('/scrape', methods=['POST'])
def trigger_scrape():
    # Récupérer les critères de recherche depuis la requête (pays, zone, ville)
    data = request.get_json()
    country = data.get('country')
    zone = data.get('zone')
    city = data.get('city')

    if not country or not zone or not city:
        return jsonify({'msg': 'Veuillez fournir les critères de recherche'}), 400

    scrape_jobs(country, zone, city)  # Lancer le scraping en arrière-plan (idéalement)
    return jsonify({'msg': 'Le scraping a été lancé'}), 200

@job_scraping_bp.route('/offers', methods=['GET'])
def get_all_offers():
    from models.job_offer import JobOffer
    offers = JobOffer.get_all()
    return jsonify([offer.to_dict() for offer in offers]), 200
  
