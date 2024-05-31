#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a strong secret key in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# User Data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

# JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    return jsonify(access_token=new_token)

# Protected Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(debug=True)
