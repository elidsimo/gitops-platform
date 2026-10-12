from app import app


def test_health_repond_ok():
    client = app.test_client()
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"status": "ok"}


def test_home_contient_un_message():
    client = app.test_client()
    reponse = client.get("/")
    assert reponse.status_code == 200
    donnees = reponse.get_json()
    assert "message" in donnees
    assert "pod" in donnees
    assert "version" in donnees


def test_metrics_expose_les_compteurs():
    client = app.test_client()
    client.get("/")
    reponse = client.get("/metrics")
    assert reponse.status_code == 200
    texte = reponse.get_data(as_text=True)
    assert "http_requests_total" in texte
    assert "http_request_duration_seconds" in texte
