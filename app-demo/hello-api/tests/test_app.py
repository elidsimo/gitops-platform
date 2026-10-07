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
