from flask import Flask, jsonify
import os
import sys
import platform

app = Flask(__name__)

@app.route("/")
def hello():
    return "Timeweb Cloud + Flask = ❤️"

@app.route("/health")
def health():
    packages = {}
    try:
        import flask
        packages['flask'] = flask.__version__
    except ImportError:
        packages['flask'] = 'NOT INSTALLED'
    
    try:
        import sqlalchemy
        packages['sqlalchemy'] = sqlalchemy.__version__
    except ImportError:
        packages['sqlalchemy'] = 'NOT INSTALLED'
        
    try:
        import requests
        packages['requests'] = requests.__version__
    except ImportError:
        packages['requests'] = 'NOT INSTALLED'
    
    return jsonify({
        "status": "healthy",
        "python_version": platform.python_version(),
        "packages": packages
    })

if __name__ == "__main__":
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)
