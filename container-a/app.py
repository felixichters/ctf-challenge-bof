#!/usr/bin/env python3

from flask import Flask, request, render_template_string
import subprocess
import threading

app = Flask(__name__)

process = None
lock = threading.Lock()

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CTF BOF Challenge</title>
    <script>
        function askForPayload() {
            const payload = prompt("Enter your payload:");
            if (payload !== null && payload !== "") {
                document.getElementById("payload").value = payload;
                document.getElementById("payloadForm").submit();
            } else {
                alert("Payload cannot be empty!");
            }
        }
    </script>
</head>
<body>
    <h1>Buffer Overflow Challenge</h1>

    {% if leaked_address %}
    <h2>Leaked Address:</h2>
    <pre>{{ leaked_address }}</pre>
    {% endif %}

    {% if output %}
    <h2>Program Output:</h2>
    <pre>{{ output }}</pre>
    {% endif %}

    <form id="payloadForm" method="POST">
        <input type="hidden" name="payload" id="payload">
        <button type="button" onclick="askForPayload()">Submit Payload</button>
    </form>
</body>
</html>
"""

@app.before_request
def start_c_program():
    global process
    if process is None:
        process = subprocess.Popen(
            ["./a.out"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        leaked_address = process.stdout.readline().strip()
        app.config["LEAKED_ADDRESS"] = leaked_address

@app.route("/", methods=["GET", "POST"])
def index():
    global process
    leaked_address = app.config.get("LEAKED_ADDRESS", "")
    output = ""

    if request.method == "POST":
        payload = request.form.get("payload", "")

        with lock:  # Ensure thread safety when interacting with the process
            try:
                # Send the payload to the C program
                process.stdin.write(payload + "\n")
                process.stdin.flush()

                # Read the output
                output = process.stdout.readline().strip()
            except Exception as e:
                output = f"An error occurred: {e}"

    return render_template_string(
        HTML_FORM,
        leaked_address=leaked_address,
        output=output
    )

@app.route("/shutdown", methods=["POST"])
def shutdown():
    global process
    if process:
        process.terminate()
        process = None
    func = request.environ.get("werkzeug.server.shutdown")
    if func:
        func()
    return "Server shutting down..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
