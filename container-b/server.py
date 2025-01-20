from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

FLAG = "CTF{FLAG}"
PASSWORD_FILE = "/home/navi/Uni/it-sec/iap/container-b/passwd"

def read_password_file():
    try:
        with open(PASSWORD_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route('/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_password = data['password']
    user_hash = hash_password(user_password)
    current_hash = read_password_file()

    if user_hash == current_hash:
        return jsonify({"message": "Authentication successful!", "flag": FLAG}), 200
    else:
        return jsonify({"error": "Authentication failed"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

