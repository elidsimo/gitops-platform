import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        message="Bonjour depuis la plateforme GitOps",
        pod=socket.gethostname(),
        version=os.getenv("APP_VERSION", "dev"),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")
