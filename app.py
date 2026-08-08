from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulate")
def simulate():
    with open("scenarios/sample_scenario.json") as f:
        scenario = json.load(f)
    return jsonify({"status": "Disaster simulated", "scenario": scenario})

if __name__ == "__main__":
    app.run(debug=True)
