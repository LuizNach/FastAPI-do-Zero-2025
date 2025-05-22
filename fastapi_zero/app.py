from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root() -> dict[str, str]:
    return {'message': 'Olá mundo!'}


@app.get('/default', status_code=HTTPStatus.OK, response_model=Message)
def default_api() -> Message:
    # FastAPI gera a documentação do end-point se fizermos
    # a declaração do type do retorno da chamada da api.
    # Podemos fazer isso de duas maneiras:
    # - declarando o retorno da api com type hints
    # - declarando o retorno da api no decorator de fastapi com
    # o argumento response_model. [Referencia](https://fastapi.tiangolo.com/tutorial/response-model/)
    # Detalhe: se não houver o tipo de retorno declarado na api,
    # dentro da [documentação](http://localhost:8000/docs) o schema estará
    # declarado como 'any'

    return Message(message='Hello, there')
    # Correto. Pydantic aceita. Mypy aceita. Ruff aceita.

    # return 123
    # Incorreto. Uma vez estabelecido o tipo de retorno é
    # uma quebra de contrato.
    # Pydantic apresenta erro em tempo de execução.
    # Mypy nao aceita.
    # Pylance nao aceita.

    # return {'message': "hello"}
    # Pydantic aceita. Mypy nao aceita. Pylance nao aceita.
