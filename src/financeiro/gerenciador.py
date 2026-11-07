import json
from pathlib import Path
from decimal import Decimal
from datetime import date, datetime

from financeiro.movimentacao import (
    Movimentacao,
    TipoMovimentacao
)

class GerenciadorFinanceiro:

    def __init__(self, arquivo=None):
        self._movimentacoes = []

        if arquivo is None:
            self._arquivo = Path("data/movimentacoes.json")
        else:
            self._arquivo = Path(arquivo)

        self._arquivo.parent.mkdir(parents=True, exist_ok=True)

        self.carregar()

    def adicionar(self, movimentacao):

        if not isinstance(movimentacao, Movimentacao):
            raise TypeError(
                "É necessário fornecer uma movimentação válida."
                )

        self._movimentacoes.append(movimentacao)
        self.salvar()
    
    def listar(self):
        return list(self._movimentacoes)
    
    
    def listar_por_categoria(self, categoria):
        if not isinstance(categoria, str):
            raise TypeError("A categoria precisa ser um texto.")

        categoria = categoria.strip()

        if not categoria:
            raise ValueError("A categoria não pode ficar vazia.")

        return [
            movimentacao
            for movimentacao in self._movimentacoes
            if movimentacao.categoria.lower() == categoria.lower()
        ]

    
    def listar_por_periodo(self, data_inicio, data_fim):

        if (
            not isinstance(data_inicio, date)
            or isinstance(data_inicio, datetime)
            or not isinstance(data_fim, date)
            or isinstance(data_fim, datetime)
        ):
            raise TypeError("As datas precisam ser objetos do tipo date, sem horário.")

        if data_inicio > data_fim:
            raise ValueError("A data inicial não pode ser maior que a data final.")

        return [
            movimentacao
            for movimentacao in self._movimentacoes
            if data_inicio <= movimentacao.data <= data_fim
        ]
    
    
    def atualizar(self, indice, nova_movimentacao):
        if not isinstance(indice, int) or isinstance(indice, bool):
            raise TypeError("O índice precisa ser um número inteiro.")

        if not isinstance(nova_movimentacao, Movimentacao):
            raise TypeError("É necessário informar uma Movimentacao.")

        if indice < 0 or indice >= len(self._movimentacoes):
            raise IndexError("Movimentação não encontrada.")

        self._movimentacoes[indice] = nova_movimentacao
        self.salvar()


    
    def remover(self, indice):
        if not isinstance(indice, int) or isinstance(indice, bool):
            raise TypeError("O índice precisa ser um número inteiro.")

        if indice < 0 or indice >= len(self._movimentacoes):
            raise IndexError("Movimentação não encontrada.")

        movimentacao_removida = self._movimentacoes.pop(indice)
        self.salvar()

        return movimentacao_removida

    
    def salvar(self):

        dados = []

        for movimentacao in self._movimentacoes:
            dados.append({
                "id": movimentacao.id,
                "descricao": movimentacao.descricao,
                "valor": str(movimentacao.valor),
                "tipo": movimentacao.tipo.value,
                "categoria": movimentacao.categoria,
                "data": movimentacao.data.isoformat()
            })

        with self._arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    
    
    def carregar(self):
        if not self._arquivo.exists():
            return

        try:
            with self._arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

        except json.JSONDecodeError as erro:
            raise ValueError(
                "O arquivo de movimentações contém JSON inválido."
            ) from erro

        if not isinstance(dados, list):
            raise ValueError(
                "O arquivo de movimentações precisa conter uma lista."
            )

        movimentacoes_carregadas = []

        for item in dados:
            movimentacao = Movimentacao(
                id=item.get("id"),
                descricao=item["descricao"],
                valor=Decimal(item["valor"]),
                tipo=TipoMovimentacao(item["tipo"]),
                categoria=item["categoria"],
                data=date.fromisoformat(item["data"])
            )

            movimentacoes_carregadas.append(movimentacao)

        self._movimentacoes = movimentacoes_carregadas

    def calcular_saldo(self):
        saldo = Decimal("0.00")

        for movimentacao in self._movimentacoes:

            if movimentacao.tipo == TipoMovimentacao.ENTRADA:
                saldo += movimentacao.valor

            elif movimentacao.tipo == TipoMovimentacao.SAIDA:
                saldo -= movimentacao.valor

        return saldo