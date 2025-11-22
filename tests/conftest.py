"""Shared test fixtures and utilities for pytest."""

from fastapi.testclient import TestClient


def make_test_client(monkeypatch, main_module, fake_api_class):
    """Create a TestClient with monkeypatched API and token.

    Args:
        monkeypatch: pytest monkeypatch fixture
        main_module: The src.main module to patch
        fake_api_class: The fake API class to use

    Returns:
        tuple: (TestClient, response dict from GET /)
    """
    monkeypatch.setattr(main_module, "get_todoist_token", lambda: "fake-token")
    monkeypatch.setattr(main_module, "TodoistAPI", fake_api_class)

    client = TestClient(main_module.app)
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()

    return client, data
