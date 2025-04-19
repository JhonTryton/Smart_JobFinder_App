from flask import Blueprint, request, jsonify
from models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'msg': 'Tous les champs sont requis'}), 400

    if User.find_by_email(email):
        return jsonify({'msg': 'Cet email est déjà enregistré'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    new_user.save()

    return jsonify({'msg': 'Utilisateur créé avec succès'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    current_user = User.find_by_email(email)

    if current_user and bcrypt.check_password_hash(current_user.password, password):
        access_token = create_access_token(identity=str(current_user.id))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'msg': 'Identifiants invalides'}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.find_by_id(current_user_id)
    return jsonify({'msg': f'Bonjour, {user.username}'}), 200
  
