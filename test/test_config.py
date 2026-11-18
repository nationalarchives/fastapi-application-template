from config import Production


def test_production_settings_load_environment_values(monkeypatch):
    monkeypatch.setenv("CONTAINER_IMAGE", "test-image")
    monkeypatch.setenv("BASE_URI", "/custom-api/")
    monkeypatch.setenv("FORCE_HTTPS", "false")

    config = Production()

    assert config.CONTAINER_IMAGE == "test-image"
    assert config.BASE_URI == "custom-api"
    assert config.FORCE_HTTPS is False
