from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

user_profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@user_profile_bp.route('/', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.find_by_id(current_user_id)
    if user:
        return jsonify({'username': user.username, 'email': user.email}), 200
    return jsonify({'msg': 'Utilisateur non trouvé'}), 404

@user_profile_bp.route('/', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()
    user = User.find_by_id(current_user_id)
    if not user:
        return jsonify({'msg': 'Utilisateur non trouvé'}), 404

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    # ... (ajouter la logique pour la modification du mot de passe, etc.)
    user.save()
    return jsonify({'msg': 'Profil mis à jour'}), 200
  
