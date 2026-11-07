# Requisitos — Simulador de Gastos

## 1. Sobre o projeto

Aplicação desenvolvida em Python para gerenciamento de movimentações financeiras pessoais.

## 2. Objetivo

Permitir que o usuário registre, consulte, edite, exclua e filtre suas movimentações financeiras, além de consultar seu saldo.

## 3. Funcionalidades principais

- [x] Cadastrar movimentações.
- [x] Listar movimentações.
- [x] Atualizar movimentações.
- [x] Remover movimentações.
- [x] Calcular e consultar o saldo.
- [x] Categorizar movimentações.
- [x] Filtrar movimentações por categoria.
- [x] Filtrar movimentações por período.
- [x] Salvar e carregar dados em JSON.
- [x] Validar informações fornecidas.
- [x] Testar funcionalidades com Pytest.

## 4. Tecnologias

- Python
- Visual Studio Code
- Git
- GitHub
- Pytest
- JSON

SQLite poderá ser utilizado futuramente como alternativa de armazenamento.

## 5. Status

Versão inicial implementada, com funcionalidades principais e testes automatizados.

## 6. Informações das movimentações

Cada movimentação possui:

- Identificador (campo ID opcional).
- Descrição.
- Valor.
- Tipo de movimentação.
- Categoria.
- Data.

## 7. Tipos de movimentação

- Entrada: representa uma receita.
- Saída: representa uma despesa.

## 8. Regras de negócio

- Não aceitar valores negativos ou iguais a zero.
- Validar os tipos de dados informados.
- Não permitir descrição ou categoria vazias.
- Calcular o saldo automaticamente.
- Salvar as movimentações em arquivo JSON.
- Permitir atualização e remoção de movimentações.
- Validar os índices utilizados nas operações.
- Validar as datas utilizadas nos filtros.

## 9. Armazenamento

O armazenamento atual utiliza arquivos JSON.

Os dados são salvos em:

`data/movimentacoes.json`

O sistema carrega as movimentações armazenadas ao iniciar e salva as alterações realizadas.

## 10. Melhorias futuras

- Gerar identificadores únicos automaticamente.
- Solicitar confirmação antes de remover uma movimentação.
- Implementar armazenamento com SQLite.
- Desenvolver uma interface gráfica ou API REST.

## Outros:

Validação de dados é o processo de verificar se as informações fornecidas pelo usuário respeitam as regras do sistema.

Uma classe pode criar diversos objetos. Cada objeto é uma instância independente daquela classe.