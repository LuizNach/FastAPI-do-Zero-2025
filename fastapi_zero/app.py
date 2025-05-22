from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root() -> dict[str, str]:
    return {'message': 'Olá mundo!'}
