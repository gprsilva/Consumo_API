# Consumo_API

Este projeto Python demonstra o consumo de uma API externa para obter cotações de moedas, utilizando variáveis de ambiente para a chave da API e gerenciamento de dependências com `venv` e `requirements.txt`.

## Funcionalidades

- **Consumo de API:** Obtém dados de cotação de moedas de uma API externa.
- **Variáveis de Ambiente:** Utiliza um arquivo `.env` para armazenar a chave da API de forma segura.
- **Ambiente Virtual:** Gerencia as dependências do projeto usando um ambiente virtual (`venv`).

## Tecnologias Utilizadas

- Python
- `requests` (para requisições HTTP)
- `python-dotenv` (para carregar variáveis de ambiente)

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.x instalado.
- Acesso à internet para consumir a API de cotação de moedas.
- Uma chave de API da ExchangeRate-API.com (ou similar) para acessar os dados de cotação.

### Configuração

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/gprsilva/Consumo_API.git
    cd Consumo_API
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Crie o arquivo `.env`:**

    Na raiz do projeto, crie um arquivo chamado `.env` e adicione sua chave de API:

    ```
    API_KEY=SUA_CHAVE_DA_API_AQUI
    ```

    Substitua `SUA_CHAVE_DA_API_AQUI` pela sua chave de API real obtida da ExchangeRate-API.com.

### Execução

Para executar o script que consome a API e exibe as cotações filtradas, utilize o seguinte comando:

```bash
python consulta.py
```

O script irá imprimir no console as cotações das moedas `BRL`, `EUR` e `JPY` em relação ao `USD`.

## Estrutura do Projeto

```
Consumo_API/
├── .gitignore
├── .env (arquivo a ser criado por você)
├── consulta.py
├── requirements.txt
└── README.md
```

- `.gitignore`: Ignora arquivos e diretórios que não devem ser versionados (como o ambiente virtual e o arquivo `.env`).
- `.env`: Contém a chave da API (não versionado).
- `consulta.py`: Script principal para consumir a API e processar os dados.
- `requirements.txt`: Lista as dependências do projeto.
- `README.md`: Este arquivo, com a documentação do projeto.
