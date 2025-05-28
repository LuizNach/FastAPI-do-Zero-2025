from http import HTTPStatus

from fastapi.testclient import TestClient
from httpx import Response


def test_root_must_return_hello_world_message(client: TestClient) -> None:
    """
    Esse teste tem 3 estapas (AAA):
    - A: Arrange - Arranjo
    - A: Act - executa a coisa que queremos testar (o SUT, system under test)
    - A: Assert - garante que algo resultado seria o mesmo que o requerido

    Outras escolas de testes utilziam testes em 4 etapas:
    Setup, Exercise, Assert, Teardown
    """
    # Arrange
    # client: TestClient = TestClient(app=app)

    # Act
    response: Response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_html_page_must_return_ola_mundo_page(client: TestClient) -> None:
    response = client.get('/html_page')

    assert response.status_code == HTTPStatus.OK
    assert 'Olá Mundo' in response.content.decode()
    assert '<title>Hello</title>' in response.content.decode()


def test_user_can_be_created(client: TestClient) -> None:
    user_input: dict[str, str] = {
        'username': 'test user',
        'password': 'batatinhas fritas123',
        'email': 'email+alias@email.org.br',
    }

    response: Response = client.post(url='/users', json=user_input)
    response_body = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert response_body['username'] == user_input['username']
    assert response_body['email'] == user_input['email']

    key: str = 'password'
    assert key not in response_body

    key = 'id'
    assert key in response_body


def test_read_users(client: TestClient) -> None:

    user_input: dict[str, str] = {
        'username': 'Cebolinha',
        'password': 'monica',
        'email': 'email+alias@email.org.br',
    }

    response: Response = client.post(url='/users', json=user_input)
    assert response.status_code == HTTPStatus.CREATED
    response = client.get(url='/read_all_users')
    assert response.status_code == HTTPStatus.OK

    response_body = response.json()
    public_user = response_body["users"][-1]  # last user created in memory

    assert public_user['username'] == user_input['username']
    assert public_user['email'] == user_input['email']

    key: str = 'password'
    assert key not in public_user

    key = 'id'
    assert key in public_user
