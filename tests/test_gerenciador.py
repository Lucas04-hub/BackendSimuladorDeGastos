from datetime import date, datetime
from decimal import Decimal
import json
import pytest

from financeiro.movimentacao import Movimentacao, TipoMovimentacao
from financeiro.gerenciador import GerenciadorFinanceiro


def criar_movimentacao(descricao, valor, tipo):
    return Movimentacao(
        descricao=descricao,
        valor=Decimal(valor),
        tipo=tipo,
        categoria="Teste",
        data=date.today()
    )


def test_adicionar_movimentacao(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    gerenciador.adicionar(movimentacao)

    assert len(gerenciador.listar()) == 1
    assert gerenciador.listar()[0].descricao == "Salário"

def test_calcular_saldo(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    entrada = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    saida = criar_movimentacao(
        "Mercado",
        "150.00",
        TipoMovimentacao.SAIDA
    )

    gerenciador.adicionar(entrada)
    gerenciador.adicionar(saida)

    assert gerenciador.calcular_saldo() == Decimal("2850.00")

def test_atualizar_movimentacao(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    original = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    atualizada = criar_movimentacao(
        "Salário atualizado",
        "3500.00",
        TipoMovimentacao.ENTRADA
    )

    gerenciador.adicionar(original)
    gerenciador.atualizar(0, atualizada)

    assert len(gerenciador.listar()) == 1
    assert gerenciador.listar()[0].descricao == "Salário atualizado"
    assert gerenciador.listar()[0].valor == Decimal("3500.00")

def test_remover_movimentacao(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Compra de mercado",
        "150.00",
        TipoMovimentacao.SAIDA
    )

    gerenciador.adicionar(movimentacao)

    removida = gerenciador.remover(0)

    assert len(gerenciador.listar()) == 0
    assert removida.descricao == "Compra de mercado"
    assert removida.valor == Decimal("150.00")

def test_carregar_movimentacoes(tmp_path):
    arquivo = tmp_path / "movimentacoes.json"

    gerenciador = GerenciadorFinanceiro(arquivo)

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    gerenciador.adicionar(movimentacao)

    # Criamos um novo gerenciador para simular uma nova execução.
    novo_gerenciador = GerenciadorFinanceiro(arquivo)

    assert len(novo_gerenciador.listar()) == 1
    assert novo_gerenciador.listar()[0].descricao == "Salário"
    assert novo_gerenciador.listar()[0].valor == Decimal("3000.00")
    assert novo_gerenciador.listar()[0].tipo == TipoMovimentacao.ENTRADA

def test_atualizar_indice_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    with pytest.raises(IndexError):
        gerenciador.atualizar(0, movimentacao)

def test_remover_indice_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(IndexError):
        gerenciador.remover(0)

def test_adicionar_objeto_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(TypeError):
        gerenciador.adicionar("Isso não é uma movimentação")

    assert len(gerenciador.listar()) == 0


def test_carregar_json_invalido(tmp_path):
    arquivo = tmp_path / "movimentacoes.json"
    arquivo.write_text("{conteudo invalido}", encoding="utf-8")

    with pytest.raises(ValueError, match="JSON inválido"):
        GerenciadorFinanceiro(arquivo)


def test_carregar_json_vazio(tmp_path):
    arquivo = tmp_path / "movimentacoes.json"
    arquivo.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="JSON inválido"):
        GerenciadorFinanceiro(arquivo)


def test_filtrar_categoria_tipo_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(TypeError):
        gerenciador.listar_por_categoria(123)


def test_filtrar_categoria_vazia(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(ValueError):
        gerenciador.listar_por_categoria("   ")


def test_filtrar_categoria_ignora_maiusculas(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Compra",
        "100.00",
        TipoMovimentacao.SAIDA
    )

    movimentacao.categoria = "Mercado"
    gerenciador.adicionar(movimentacao)

    resultado = gerenciador.listar_por_categoria(" mercado ")

    assert len(resultado) == 1
    assert resultado[0].categoria == "Mercado"


def test_atualizar_indice_tipo_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    with pytest.raises(TypeError):
        gerenciador.atualizar("abc", movimentacao)


def test_remover_indice_tipo_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(TypeError):
        gerenciador.remover("abc")


def test_atualizar_indice_tipo_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    with pytest.raises(TypeError):
        gerenciador.atualizar("abc", movimentacao)


def test_remover_indice_tipo_invalido(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        tmp_path / "movimentacoes.json"
    )

    with pytest.raises(TypeError):
        gerenciador.remover("abc")


def test_filtrar_periodo_rejeita_datetime(tmp_path):
    gerenciador = GerenciadorFinanceiro(
        arquivo=tmp_path / "teste.json"
    )

    data_inicio = datetime(2026, 1, 1, 10, 30)
    data_fim = date(2026, 12, 31)

    with pytest.raises(TypeError):
        gerenciador.listar_por_periodo(
            data_inicio,
            data_fim
        )


def test_salvar_id_movimentacao(tmp_path):
    arquivo = tmp_path / "movimentacoes.json"

    gerenciador = GerenciadorFinanceiro(arquivo)

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    movimentacao.id = 10

    gerenciador.adicionar(movimentacao)

    with open(arquivo, "r", encoding="utf-8") as dados:
        conteudo = json.load(dados)

    assert conteudo[0]["id"] == 10


def test_carregar_id_movimentacao(tmp_path):
    arquivo = tmp_path / "movimentacoes.json"

    gerenciador = GerenciadorFinanceiro(arquivo)

    movimentacao = criar_movimentacao(
        "Salário",
        "3000.00",
        TipoMovimentacao.ENTRADA
    )

    movimentacao.id = 25

    gerenciador.adicionar(movimentacao)

    novo_gerenciador = GerenciadorFinanceiro(arquivo)

    movimentacoes = novo_gerenciador.listar()

    assert movimentacoes[0].id == 25