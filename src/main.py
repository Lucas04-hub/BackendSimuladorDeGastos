from datetime import date
from decimal import Decimal, InvalidOperation

from financeiro.movimentacao import (
    Movimentacao,
    TipoMovimentacao
)

from financeiro.gerenciador import GerenciadorFinanceiro


def exibir_menu():
    print("\n========== SIMULADOR DE GASTOS ==========")
    print("1 - Listar movimentações")
    print("2 - Consultar saldo")
    print("3 - Cadastrar movimentação")
    print("4 - Atualizar movimentação")
    print("5 - Remover movimentação")
    print("6 - Filtrar por categoria")
    print("7 - Filtrar por período")
    print("8 - Sair")
    print("=========================================")


def main():
    gerenciador = GerenciadorFinanceiro()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        # 1 - Listar movimentações
        if opcao == "1":
            print("\n=== MOVIMENTAÇÕES FINANCEIRAS ===")

            movimentacoes = gerenciador.listar()

            if not movimentacoes:
                print("Nenhuma movimentação cadastrada.")
            else:
                for indice, movimentacao in enumerate(movimentacoes):
                    print(f"\nÍndice: {indice}")
                    print(f"Descrição: {movimentacao.descricao}")
                    print(f"Valor: R$ {movimentacao.valor:.2f}")
                    print(f"Tipo: {movimentacao.tipo.value}")
                    print(f"Categoria: {movimentacao.categoria}")
                    print(f"Data: {movimentacao.data}")

        # 2 - Consultar saldo
        elif opcao == "2":
            saldo = gerenciador.calcular_saldo()
            print(f"\nSaldo atual: R$ {saldo:.2f}")

        # 3 - Cadastrar movimentação
        elif opcao == "3":
            print("\n=== NOVA MOVIMENTAÇÃO ===")

            try:
                descricao = input("Descrição: ")

                valor = Decimal(
                    input("Valor: R$ ").replace(",", ".")
                )

                categoria = input("Categoria: ")

                print("\nTipo de movimentação:")
                print("1 - Entrada")
                print("2 - Saída")

                escolha_tipo = input("Escolha: ")

                if escolha_tipo == "1":
                    tipo = TipoMovimentacao.ENTRADA
                elif escolha_tipo == "2":
                    tipo = TipoMovimentacao.SAIDA
                else:
                    print("Tipo de movimentação inválido.")
                    continue

                data_movimentacao = date.fromisoformat(
                    input("Data (AAAA-MM-DD): ")
                )

                movimentacao = Movimentacao(
                    descricao=descricao,
                    valor=valor,
                    tipo=tipo,
                    categoria=categoria,
                    data=data_movimentacao
                )

                gerenciador.adicionar(movimentacao)

                print("\nMovimentação cadastrada com sucesso!")

            except (ValueError, InvalidOperation) as erro:
                print(f"\nNão foi possível cadastrar: {erro}")

        # 4 - Atualizar movimentação
        elif opcao == "4":
            print("\n=== ATUALIZAR MOVIMENTAÇÃO ===")

            movimentacoes = gerenciador.listar()

            if not movimentacoes:
                print("Não existem movimentações para atualizar.")
                continue

            for indice, movimentacao in enumerate(movimentacoes):
                print(
                    f"{indice} - {movimentacao.descricao} "
                    f"| R$ {movimentacao.valor:.2f}"
                )

            try:
                indice = int(input("\nDigite o índice da movimentação: "))

                if indice < 0 or indice >= len(movimentacoes):
                    raise IndexError("Movimentação não encontrada.")

                descricao = input("Nova descrição: ")

                valor = Decimal(
                    input("Novo valor: R$ ").replace(",", ".")
                )

                categoria = input("Nova categoria: ")

                print("\nTipo de movimentação:")
                print("1 - Entrada")
                print("2 - Saída")

                escolha_tipo = input("Escolha: ")

                if escolha_tipo == "1":
                    tipo = TipoMovimentacao.ENTRADA
                elif escolha_tipo == "2":
                    tipo = TipoMovimentacao.SAIDA
                else:
                    print("Tipo inválido.")
                    continue

                data_movimentacao = date.fromisoformat(
                    input("Nova data (AAAA-MM-DD): ")
                )

                movimentacao_atualizada = Movimentacao(
                    id=movimentacoes[indice].id,
                    descricao=descricao,
                    valor=valor,
                    tipo=tipo,
                    categoria=categoria,
                    data=data_movimentacao
                )

                gerenciador.atualizar(
                    indice,
                    movimentacao_atualizada
                )

                print("\nMovimentação atualizada com sucesso!")

            except (ValueError, InvalidOperation, IndexError) as erro:
                print(f"\nNão foi possível atualizar: {erro}")

        # 5 - Remover movimentação
        elif opcao == "5":
            print("\n=== REMOVER MOVIMENTAÇÃO ===")

            movimentacoes = gerenciador.listar()

            if not movimentacoes:
                print("Não existem movimentações para remover.")
                continue

            for indice, movimentacao in enumerate(movimentacoes):
                print(
                    f"{indice} - {movimentacao.descricao} "
                    f"| R$ {movimentacao.valor:.2f}"
                )

            try:
                indice = int(
                    input(
                        "\nDigite o índice da movimentação "
                        "que deseja remover: "
                    )
                )

                removida = gerenciador.remover(indice)

                print(
                    f"\nMovimentação '{removida.descricao}' "
                    "removida com sucesso!"
                )

            except (ValueError, IndexError) as erro:
                print(f"\nNão foi possível remover: {erro}")

        # 6 - Filtrar por categoria
        elif opcao == "6":
            print("\n=== FILTRAR POR CATEGORIA ===")

            try:
                categoria = input("Digite a categoria desejada: ")

                resultado = gerenciador.listar_por_categoria(categoria)

                if not resultado:
                    print(
                        "Nenhuma movimentação encontrada "
                        "nessa categoria."
                    )
                else:
                    for movimentacao in resultado:
                        print("\n----------------------------")
                        print(f"Descrição: {movimentacao.descricao}")
                        print(f"Valor: R$ {movimentacao.valor:.2f}")
                        print(f"Tipo: {movimentacao.tipo.value}")
                        print(f"Categoria: {movimentacao.categoria}")
                        print(f"Data: {movimentacao.data}")

            except (ValueError, TypeError) as erro:
                print(f"\nNão foi possível filtrar: {erro}")

        # 7 - Filtrar por período
        elif opcao == "7":
            print("\n=== FILTRAR POR PERÍODO ===")

            try:
                data_inicio = date.fromisoformat(
                    input("Data inicial (AAAA-MM-DD): ")
                )

                data_fim = date.fromisoformat(
                    input("Data final (AAAA-MM-DD): ")
                )

                resultado = gerenciador.listar_por_periodo(
                    data_inicio,
                    data_fim
                )

                if not resultado:
                    print(
                        "Nenhuma movimentação encontrada "
                        "nesse período."
                    )
                else:
                    for movimentacao in resultado:
                        print("\n----------------------------")
                        print(f"Descrição: {movimentacao.descricao}")
                        print(f"Valor: R$ {movimentacao.valor:.2f}")
                        print(f"Tipo: {movimentacao.tipo.value}")
                        print(f"Categoria: {movimentacao.categoria}")
                        print(f"Data: {movimentacao.data}")

            except ValueError as erro:
                print(f"\nNão foi possível filtrar: {erro}")

        # 8 - Sair
        elif opcao == "8":
            print("\nObrigado por utilizar o Simulador de Gastos!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
