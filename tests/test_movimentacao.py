from datetime import date, datetime
from decimal import Decimal
import pytest

from financeiro.movimentacao import (
    Movimentacao,
    TipoMovimentacao
)

def test_criar_movimentacao():
    movimentacao = Movimentacao(
        descricao="Salário",
        valor=Decimal("3000.00"),
        tipo=TipoMovimentacao.ENTRADA,
        categoria="Trabalho",
        data=date.today()
    )

    assert movimentacao.descricao == "Salário"
    assert movimentacao.valor == Decimal("3000.00")
    assert movimentacao.tipo == TipoMovimentacao.ENTRADA
    assert movimentacao.categoria == "Trabalho"

def test_descricao_invalida():
    with pytest.raises(TypeError):
        Movimentacao(
            descricao=123,
            valor=Decimal("100.00"),
            tipo=TipoMovimentacao.ENTRADA,
            categoria="Trabalho",
            data=date.today()
        )

def test_tipo_invalido():
    with pytest.raises(TypeError):
        Movimentacao(
            descricao="Teste",
            valor=Decimal("100.00"),
            tipo="transferencia",
            categoria="Trabalho",
            data=date.today()
        )


def test_valor_com_tipo_invalido():
    with pytest.raises(TypeError):
        Movimentacao(
            descricao="Salário",
            valor=100,
            tipo=TipoMovimentacao.ENTRADA,
            categoria="Trabalho",
            data=date.today()
        )


def test_data_com_horario_invalida():
    with pytest.raises(TypeError):
        Movimentacao(
            descricao="Salário",
            valor=Decimal("3000.00"),
            tipo=TipoMovimentacao.ENTRADA,
            categoria="Trabalho",
            data=datetime.now()
        )


def test_data_com_tipo_invalido():
    with pytest.raises(TypeError):
        Movimentacao(
            descricao="Salário",
            valor=Decimal("3000.00"),
            tipo=TipoMovimentacao.ENTRADA,
            categoria="Trabalho",
            data="06/11/2026"
        )
