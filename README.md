# ☕ Catuapi

Sistema completo para gerenciamento de cafés especiais, desenvolvido como MVP da disciplina **Desenvolvimento Full Stack Básico** — **Engenharia de Software | PUC-Rio**.

O projeto é composto por uma **API REST em Flask** e uma **SPA em HTML/CSS/JavaScript puro**, organizados como um monorepo com separação clara entre backend e frontend.

---

## 📁 Estrutura do Repositório

```
catuapi/
├── api/                  # Backend — API REST em Flask
└── coffee_signup_form/   # Frontend — SPA em HTML/CSS/JS
```

---

## 🚀 Funcionalidades

- Cadastrar cafés especiais com nome, produtor, variedade, processo e notas sensoriais
- Listar todos os cafés em uma tabela interativa
- Editar cafés existentes
- Excluir cafés cadastrados
- Documentação automática via Swagger / OpenAPI

---

## 🛠 Tecnologias

| Camada | Tecnologias |
|---|---|
| Backend | Python 3, Flask, Flask-SQLAlchemy, Flask-CORS, Flask-OpenAPI3, Pydantic, SQLite |
| Frontend | HTML5, CSS3, JavaScript (ES6), Font Awesome |

---

## ⚙️ Como Executar

### Pré-requisito

Ambos devem rodar ao mesmo tempo. Inicie o **backend primeiro**.

---

### 🔧 Backend (`/api`)

```bash
cd api

# Crie e ative o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute a API
python main.py
```

A API estará disponível em: `http://127.0.0.1:5000/`  
Documentação Swagger em: `http://127.0.0.1:5000/openapi`

---

### 🖥 Frontend (`/coffee_signup_form`)

Não requer servidor local. Basta abrir o arquivo diretamente no navegador:

```
coffee_signup_form/index.html  →  duplo clique ou abrir pelo navegador
```

> Certifique-se de que o backend está rodando em `http://localhost:5000` antes de usar a interface.

---

## 🔗 Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/catuapi/cafes` | Lista todos os cafés |
| POST | `/catuapi/cafes` | Cadastra um novo café |
| PUT | `/catuapi/cafes/{id}` | Atualiza um café pelo ID |
| DELETE | `/catuapi/cafes/{id}` | Remove um café pelo ID |

---

## 🗄 Banco de Dados

- **Banco:** SQLite
- **Arquivo:** `CAFES_ESPECIAIS.db`  
- **Tabela:** `CAFES`

| Campo | Tipo | Descrição |
|---|---|---|
| id | Integer | Chave primária, auto-increment |
| nome | String | Nome do café |
| produtor | String | Nome do produtor |
| variedade | String | Variedade do café |
| processo | String | Processo de produção |
| sensorial_docura | Integer | Nota de doçura |
| sensorial_acidez | Integer | Nota de acidez |
| sensorial_corpo | Integer | Nota de corpo |
| sensorial_amargor | Integer | Nota de amargor |

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Boniolo** | Engenharia de Software — PUC-Rio
