from flask import Flask, request, jsonify
import hashlib
import time
import threading

app = Flask(__name__)

FLAG = "CTF{}"
PASSWORD_FILE = "/home/navi/Uni/it-sec/iap/presentation/race-condition/app/passwd"

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

@app.route('/write', methods=['POST'])
def write_to_password_file():
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"error": "Invalid request"}), 400

    content = data['content']
    try:
        with open(PASSWORD_FILE, 'w') as f:
            f.write(content)
        return jsonify({"message": "Write successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

