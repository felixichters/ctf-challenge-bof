#!/usr/bin/env python3

from flask import Flask, request, render_template_string
import subprocess
import sys

app = Flask(__name__)

# HTML template with a simple form
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CTF BOF Challenge</title>
</head>
<body>
    <h1>Enter Payload</h1>
    <form method="POST">
        <label for="payload">Payload:</label>
        <input type="text" name="payload" id="payload">
        <button type="submit">Submit</button>
    </form>

    {% if output %}
    <hr>
    <h2>Program Output:</h2>
    <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        payload = request.form.get("payload", "")

        # Run the vulnerable C program with user input
        try:
            result = subprocess.run(
                ["./a.out", payload],
                capture_output=True,
                text=True
            )
            output = result.stdout
            # In case there's error output
            if result.stderr:
                # For debugging or letting the user see errors
                output += "\nError: " + result.stderr
        except Exception as e:
            output = f"An error occurred: {e}"

    return render_template_string(HTML_FORM, output=output)

if __name__ == "__main__":
    # Debug mode for local testing only (remove for actual CTF server)
    app.run(host="0.0.0.0", port=5000, debug=True)
