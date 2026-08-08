from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate')
def simulate():
    with open('scenarios/sample_scenario.json') as f:
        data = json.load(f)
    # Render result.html instead of raw JSON
    return render_template('result.html', scenario=data["scenario"], status=data["status"])

if __name__ == "__main__":
    app.run(debug=True)
