# CatuAPI Backend

API desenvolvida como parte do MVP da disciplina **Desenvolvimento Full Stack Básico**.  
O backend é construído em **Python com Flask**, fornecendo **rotas CRUD para gerenciamento de cafés especiais**, integrando com o frontend da aplicação.

---

## 🚀 Objetivo
O **CatuAPI Backend** tem como objetivo fornecer um serviço simples e prático para:

- Armazenar cafés com informações de nome, produtor, variedade, processo e notas sensoriais.  
- Listar cafés cadastrados para consumo por frontends ou outras aplicações.  
- Permitir edição e exclusão de cafés existentes.  
- Disponibilizar documentação automática via **Swagger / OpenAPI**.

---

## 🛠 Tecnologias Utilizadas
- **Python 3** para a linguagem principal  
- **Flask** como framework web  
- **Flask-SQLAlchemy** para ORM e gerenciamento do banco SQLite  
- **Flask-CORS** para permitir requisições do frontend  
- **Flask-OpenAPI3** com **Swagger** para documentação e testes  
- **Pydantic** para validação de dados das requisições  

---

## 📂 Estrutura do Projeto
catuapi_back/  
```plaintext
main.py             # Ponto de entrada da API, configuração do Flask e OpenAPI
db.py              # Inicialização do SQLAlchemy
models.py          # Modelos SQLAlchemy (tabela CAFES)
schemas.py         # Modelos Pydantic para validação e Swagger
routes.py          # Rotas CRUD da API
requirements.txt   # Dependências do projeto
```
⚙️ Instalação e Execução

Clone o repositório:

```bash
git clone <link-do-repo>
cd catuapi_back
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
python main.py
```

A API estará disponível em: http://127.0.0.1:5000/

🔗 Rotas Disponíveis

GET    = "/catuapi/cafes"	   // Lista todos os cafés cadastrados
POST   = "/catuapi/cafes"	   // Adiciona um novo café
PUT    = "/catuapi/cafes/{id}" // Atualiza um café existVente pelo ID
DELETE = "/catuapi/cafes/{id}" // Remove um café pelo ID

POST e PUT usam o modelo Pydantic CafeSchema para validação de dados.  

GET e DELETE retornam JSON com as informações dos cafés.

📌 Swagger / OpenAPI

Documentação interativa disponível em:

http://127.0.0.1:5000/openapi
Permite testar todas as rotas diretamente pelo navegador.

Campos do POST/PUT são preenchidos automaticamente com base no CafeSchema.

💾 Banco de Dados

Banco: SQLite

Arquivo: CAFES_ESPECIAIS.db

Tabela principal: CAFES

| Campo | Tipo | Observação |
|---|---|---|
| id | Integer | Primary Key, auto-increment |
| nome | String | Nome do café |
| produtor | String | Nome do produtor |
| variedade | String | Variedade do café |
| processo | String | Processo de produção |
| sensorial\_docura | Integer | Nota de docura |
| sensorial\_acidez | Integer | Nota de acidez |
| sensorial\_corpo | Integer | Nota de corpo |
| sensorial\_amargor | Integer | Nota de amargor |

🧩 Dependências Principais

flask, 
flask-cors, 
flask-sqlalchemy, 
flask-openapi3[swagger], 
pydantic

⚡ Observações

models.py → representa a tabela no banco de dados (SQLAlchemy)

schemas.py → validação de entrada/saída com Pydantic (Swagger)

routes.py → define todas as rotas CRUD usando OpenAPI

Swagger permite testes e documentação automáticos sem ferramentas externas

👨‍💻 Autor

Desenvolvido por Gabriel Boniolo como parte do MVP da disciplina de Desenvolvimento Full Stack Básico | Engenharia de Software - PUC-Rio.
