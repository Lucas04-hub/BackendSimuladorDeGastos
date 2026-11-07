# Simulador de Gastos — Backend Python

Aplicação de linha de comando desenvolvida em Python para gerenciamento de movimentações financeiras pessoais.

O projeto permite registrar receitas e despesas, consultar o saldo, atualizar e remover movimentações e realizar filtros por categoria e período.

## Funcionalidades

- Cadastrar movimentações financeiras.
- Listar movimentações cadastradas.
- Consultar o saldo atual.
- Atualizar movimentações.
- Remover movimentações.
- Filtrar movimentações por categoria.
- Filtrar movimentações por período.
- Validar os dados informados.
- Salvar e carregar movimentações em arquivo JSON.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- JSON para persistência de dados
- Pytest para testes automatizados
- Git e GitHub para controle de versão e publicação

## Estrutura do projeto

```text
Projeto-SimuladorDeGastos-Backend/
├── data/
│   └── movimentacoes.json
├── src/
│   ├── financeiro/
│   │   ├── __init__.py
│   │   ├── movimentacao.py
│   │   └── gerenciador.py
│   └── main.py
├── tests/
│   ├── test_movimentacao.py
│   └── test_gerenciador.py
├── .gitignore
├── README.md
├── REQUISITOS.md
├── requirements.txt
└── pytest.ini
```

## Requisitos

- Python 3.10 ou superior.
- pip para instalação das dependências.

## Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd Projeto-SimuladorDeGastos-Backend
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no macOS ou Linux:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Executar o simulador

```bash
python src/main.py
```

## Como executar os testes

Para executar os testes automatizados:

```bash
python -m pytest -v
```

## Armazenamento dos dados

As movimentações são armazenadas localmente no arquivo:

```text
data/movimentacoes.json
```

O projeto utiliza JSON para persistência dos dados. A utilização de SQLite poderá ser considerada em uma evolução futura.

## Status do projeto

**Versão inicial implementada.**

O projeto possui as principais funcionalidades de gerenciamento financeiro e testes automatizados.

## Objetivo de aprendizado

Este projeto foi desenvolvido como prática de programação Backend com Python, aplicando conceitos de:

- Classes e objetos.
- Encapsulamento.
- Enum e dataclasses.
- Validação de dados.
- Tratamento de exceções.
- Manipulação de arquivos JSON.
- Testes automatizados.
- Organização de projetos Python.