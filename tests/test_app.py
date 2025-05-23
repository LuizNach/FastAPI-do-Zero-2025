from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_must_return_hello_world_message() -> None:
    """
    Esse teste tem 3 estapas (AAA):
    - A: Arrange - Arranjo
    - A: Act - executa a coisa que queremos testar (o SUT, system under test)
    - A: Assert - garante que algo resultado seria o mesmo que o requerido

    Outras escolas de testes utilziam testes em 4 etapas:
    Setup, Exercise, Assert, Teardown
    """
    # Arrange
    client: TestClient = TestClient(app=app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_html_page_must_return_ola_mundo_page() -> None:

    client: TestClient = TestClient(app=app)

    response = client.get('/html_page')

    assert response.status_code == HTTPStatus.OK
    assert "Olá Mundo" in response.content.decode()
    assert "<title>Hello</title>" in response.content.decode()
