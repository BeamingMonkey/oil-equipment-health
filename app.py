from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('equipment_data.json') as f:
        data = json.load(f)
    return render_template('dashboard.html', equipment=data)

@app.route('/api/data')
def api_data():
    with open('equipment_data.json') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
