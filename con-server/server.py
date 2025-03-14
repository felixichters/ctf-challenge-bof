from flask import Flask, jsonify, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/status', methods=['GET'])
def status():
    arg = request.args.get('arg', '')  # Get 'arg' from URL, with a default value
    
    # Run the subprocess with user-provided input
    result = subprocess.run(['./vuln', '../con-start/passwd', arg], input='test_input', capture_output=True, text=True)
    
    print("Output of C program:")
    print(result.stdout)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
