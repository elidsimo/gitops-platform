import os
import socket
import time

from flask import Flask, Response, g, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

app = Flask(__name__)

REQUETES = Counter(
    "http_requests_total",
    "Nombre de requêtes HTTP reçues",
    ["method", "endpoint", "status"],
)
DUREE = Histogram(
    "http_request_duration_seconds",
    "Durée de traitement des requêtes HTTP en secondes",
    ["method", "endpoint"],
)

ROUTES_NON_COMPTEES = {"/metrics", "/health"}


@app.before_request
def debut_requete():
    g.debut = time.perf_counter()


@app.after_request
def fin_requete(reponse):
    if request.path not in ROUTES_NON_COMPTEES:
        endpoint = request.url_rule.rule if request.url_rule else "inconnu"
        DUREE.labels(request.method, endpoint).observe(time.perf_counter() - g.debut)
        REQUETES.labels(request.method, endpoint, str(reponse.status_code)).inc()
    return reponse


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


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)
