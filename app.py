import hashlib
import os

from flask import Flask, request

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/usr/share/nginx/html"


@app.route("/")
def index():
    return "Hello."


@app.route("/save", methods=["POST"])
def save():
    if "file" not in request.files:
        return "no file uploaded", 400
    file = request.files["file"]
    if file.filename == "":
        return "no filename found", 400
    filename = hashlib.sha256(file.read()).hexdigest()
    file.seek(0)
    if "prefix" in request.form:
        filename = "%s_%s" % (request.form["prefix"], filename)
    if "suffix" in request.form:
        filename = "%s_%s" % (filename, request.form["suffix"])
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return filename


if __name__ == "__main__":
    app.run(use_debugger=True, use_reloader=True, port=8000, host="0.0.0.0")