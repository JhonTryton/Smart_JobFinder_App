from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.application import Application
# ... potentiellement des fonctions pour l'IA et l'envoi d'emails

job_applications_bp = Blueprint('applications', __name__, url_prefix='/applications')

@job_applications_bp.route('/apply/<job_id>', methods=['POST'])
@jwt_required()
def apply_to_job(job_id):
    current_user_id = get_jwt_identity()
    # Récupérer les informations de la candidature (CV, lettre, etc.) depuis la requête
    # ...
    new_application = Application(user_id=current_user_id, job_id=job_id, ...)
    new_application.save()
    return jsonify({'msg': 'Candidature enregistrée'}), 201

@job_applications_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_applications():
    current_user_id = get_jwt_identity()
    applications = Application.find_by_user_id(current_user_id)
    return jsonify([app.to_dict() for app in applications]), 200
  
