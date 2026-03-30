from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BRAWL_API_TOKEN")

@app.route("/")
def home():
    return "OK", 200

@app.route("/player")
def player():
    tag = request.args.get("tag", "").strip().upper().replace("#", "")

    if not tag:
        return jsonify({"error": "missing_tag"}), 400

    url = f"https://api.brawlstars.com/v1/players/%23{tag}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    r = requests.get(url, headers=headers, timeout=15)
    return (r.text, r.status_code, {"Content-Type": "application/json"})
