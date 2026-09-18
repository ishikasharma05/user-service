from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify(status="ok", service="user-service", env=os.getenv("ENVIRONMENT", "dev"))

@app.route('/users')
def users():
    return jsonify(users=[{"id": 1, "name": "Ishika"}, {"id": 2, "name": "Test User"}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
