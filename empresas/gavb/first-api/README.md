# 📦 DevOps Mentoria API

Esta é uma API simples construída com **FastAPI**, desenvolvida para fins de estudo e mentoria em DevOps.

## 🚀 Funcionalidades

- 🔍 Listar itens disponíveis (`GET /items`)
- ➕ Adicionar novos itens (`POST /items`)
- 📄 Endpoint raiz informativo (`GET /`)

Os itens são mantidos em uma "fake database" (uma lista em memória) durante a execução da aplicação.

## 📁 Estrutura do Projeto

```
.
├── firstapi.py       # Código principal da API
├── main.py           # Arquivo alternativo (código duplicado)
├── requirements.txt  # Dependências do projeto
```

> Obs: `firstapi.py` e `main.py` contêm o mesmo código. Recomenda-se manter apenas um.

## 🛠️ Requisitos

- Python 3.8+
- pip

## 🔧 Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/devops-mentoria-api.git
cd devops-mentoria-api
```

2. Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
uvicorn firstapi:app --reload
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentação interativa disponível em:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📬 Endpoints

### `GET /`
Retorna uma mensagem de boas-vindas.

### `GET /items`
Retorna a lista de todos os itens cadastrados.

### `POST /items`
Adiciona um novo item à lista.

**Exemplo de JSON:**
```json
{
  "name": "Teclado Mecânico",
  "description": "Switch azul, iluminação RGB",
  "price": 249.90
}
```

## 📄 Licença

Este projeto é de uso educacional e está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
Hello