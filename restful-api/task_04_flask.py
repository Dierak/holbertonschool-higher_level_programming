from flask import Flask, jsonify, request

app = Flask(__name__)

# Example dictionary to store users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root URL ("/")
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route to serve JSON data of all usernames
@app.route('/data')
def get_data():
    usernames = list(users.keys())  # Get all usernames
    return jsonify(usernames)

# Route to return status OK
@app.route('/status')
def get_status():
    return "OK"

# Route to get user details by username
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Route to handle adding new users via POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user.get('username', None)
    if username:
        users[username] = new_user
        return jsonify({
            "message": "User added",
            "user": new_user
        }), 201  # HTTP status code 201 for Created
    else:
        return jsonify({"error": "Invalid user data"}), 400  # Bad request

if __name__ == "__main__":
    app.run()
