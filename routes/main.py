from flask import render_template, jsonify, request
from . import main_bp
from models.user import User
from extensions import db

@main_bp.route('/')
def home():
    return "Hello, World!"

@main_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'username': user.username, 'email': user.email})

@main_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@main_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
