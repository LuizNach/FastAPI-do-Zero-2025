# FastAPI-do-Zero-2025
Este é um repositório de estudos para o curso do material FastAPI do Zero do autor @dunossauro @livedepython
Referências: 
* [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com/4.0/)
* [dunossauro/fastapi-do-zero](https://github.com/dunossauro/fastapi-do-zero?tab=readme-ov-file)

## Ferramentas

Ferramentas utilizadas para desenvolvimento:
* [Ubuntu OS](https://ubuntu.com/)
* [Homebrew](https://brew.sh/)
* [asdf](https://asdf-vm.com/)
* [Poetry](https://python-poetry.org/)

## Install

### Passo a passo

Utilizando o [Ubuntu OS](https://ubuntu.com/), decidi instalar a maior parte das ferramentas por meio do [asdf](https://asdf-vm.com/) que por sua vez foi instalado com [Homebrew](https://brew.sh/). Vou deixar os passos de instalação aqui caso alguém gostaria de replicar passo a passo como instalá-los.  
  
Instalando a versão do python e setando ele como global.  
```sh
asdf plugin list all | grep python
asdf plugin add python
asdf plugin update --all
asdf list all python | grep 3.13
asdf install python 3.13.2
cd ~
asdf set python 3.13.2
```

Instalando poetry e setando a versão global.  
```sh
asdf plugin list all | grep poetry
asdf plugin add poetry
asdf plugin update --all
asdf list all poetry
asdf install poetry 2.1.3
cd ~
asdf set poetry 2.1.3
```

Instalando pipx e setando a versão global.  
```sh
asdf plugin list all | grep pipx
asdf plugin add pipx
asdf plugin update --all
asdf list all pipx
asdf install pipx 1.7.1
cd ~
asdf set pipx 1.7.1
```

Configurando poetry e iniciando o repositório.  
```sh
poetry 
poetry config --help
poetry config --list

poetry self add poetry-plugin-shell
poetry self show plugins

poetry config virtualenvs.in-project true  
poetry new --flat FastAPI-Zero
poetry env list
poetry env info
```

Instalando fastapi.  
```sh
cd FastAPI-do-Zero-2025
poetry shell
poetry add "fastapi[standard]"
poetry show --tree
```

Instalando a ferramenta ruff para checar formatação.  
```sh
# Ruff
poetry add --group dev ruff
ruff check .
ruff format .
```

Instalando a ferramentas pytest para testes como dependência de desenvolvimento.  
```sh
# Pytest
poetry add --group dev pytest pytest-cov
pytest
pytest --cov=fastapi_zero -vv
coverage html
```
Instalando a ferramenta taskipy para criar atalhos para comandos mais fáceis.  
Detalhe, Taskipy requer que a versão do python esteja definida no pyproject.toml como <4.0 e >=3.6  
```sh
# Taskipy
poetry add --group dev taskipy
```

Executando o servidor  
```sh
fastapi dev fastapi_zero
```

Criando o `.gitignore`  
```sh
pipx run ignr -p python > .gitignore
```

### Ruff

[Ruff](https://docs.astral.sh/ruff/)

`I (Isort)`: ordenação de imports em ordem alfabética  
`F (Pyflakes)`: procura por alguns erros em relação a boas práticas de código  
`E (pycodestyle)`: `error` - erros de esitlo de código  
`W (pycodestyle)`: `warning` - avisos sobre estilo de código  
`PL (Pylint)`: "erros" em relação a boas práticas de código  
`PT (flake8-pytest)`: boas práticas do pytest  

