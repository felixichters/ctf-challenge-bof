from flask import Flask, request
import subprocess

app = Flask(__name__)
C_PROGRAM_PATH = "./vuln"

@app.route('/run', methods=['POST'])
def run():
    filename = request.args.get('filename')  # Equivalent to argv[1]
    user_input = request.form.get('input')   # Equivalent to scanf input
    
    if not filename or not user_input:
        return "Missing filename or input", 400
    
    subprocess.run([C_PROGRAM_PATH, filename], 
                    input=user_input, text=True, 
                    capture_output=True)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
