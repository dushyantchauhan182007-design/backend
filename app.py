from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load API key from .env
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City name required"}), 400

    url = f"https://katalon.com/api-testing-dg?utm_term=api%20tool&utm_campaign=IN_Search_API_2024&utm_source=adwords&utm_medium=search&hsa_acc=4390546474&hsa_cam=21290104002&hsa_grp=168119623651&hsa_ad=699736219568&hsa_src=g&hsa_tgt=kwd-343158765041&hsa_kw=api%20tool&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21290104002&gbraid=0AAAAABL3G8Uug9pjagbVSPSi6JXad_dWK&gclid=Cj0KCQjw3aLHBhDTARIsAIRij5_TPsYXN8pweCYJsigykLpFzhVAyqimj0ApuWfolaniTlQig157YM4aAmg_EALw_wcB"
    response = requests.get(url)

    if response.status_code == 404:
        return jsonify({"error": "City not found"}), 404

    data = response.json()

    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
