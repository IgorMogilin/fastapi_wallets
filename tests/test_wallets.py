import os
import pytest
from fastapi.testclient import TestClient

from app.main import app


os.environ["TESTING"] = "true"


@pytest.fixture
def client():
    """Тестовый клиент."""
    return TestClient(app)


class TestAPI:
    """Набор тестов для API."""

    def test_root_endpoint(self, client):
        """Тест главной страницы."""
        response = client.get("/")
        assert response.status_code == 200

    def test_api_docs(self, client):
        """Тест документации."""
        response = client.get("/api/v1/docs")
        assert response.status_code == 200

    def test_openapi_schema(self, client):
        """Тест схемы API."""
        response = client.get("/api/v1/openapi.json")
        assert response.status_code == 200

    def test_invalid_uuid(self, client):
        """Тест неверного UUID."""
        response = client.get("/api/v1/wallets/invalid-uuid")
        assert response.status_code == 422

    def test_invalid_operation(self, client):
        """Тест неверной операции."""
        from uuid import uuid4
        fake_uuid = uuid4()
        response = client.post(
            f"/api/v1/wallets/{fake_uuid}/operation",
            json={"operation_type": "INVALID", "amount": -10}
        )
        assert response.status_code == 422

    def test_wrong_method(self, client):
        """Тест неверного метода."""
        from uuid import uuid4
        fake_uuid = uuid4()
        response = client.put(f"/api/v1/wallets/{fake_uuid}")
        assert response.status_code == 405
