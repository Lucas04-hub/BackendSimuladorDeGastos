def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: Por favor, digite um número válido!")

def exibir_menu():
    opcoes_menu = [
        "1 - Soma",
        "2 - Subtração",
        "3 - Multiplicação",
        "4 - Divisão",
        "5 - Sair"
    ]
    print("\n==== CALCULADORA ====")
    [print(opcao) for opcao in opcoes_menu]

operacoes = {
    "1": (lambda x, y: x + y, "soma"),
    "2": (lambda x, y: x - y, "subtração"),
    "3": (lambda x, y: x * y, "multiplicação"),
    "4": (lambda x, y: x / y if y != 0 else None, "divisão")
}

def executar_operacao(opcao, num1, num2):
    operacao, nome = operacoes[opcao]
    if opcao == "4" and num2 == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        resultado = operacao(num1, num2)
        print(f"Resultado da {nome}: {resultado}")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "5":
            print("Até logo!")
            break

        if opcao in {"1", "2", "3", "4"}:
            num1 = obter_numero("Insira o primeiro número: ")
            num2 = obter_numero("Insira o segundo número: ")
            executar_operacao(opcao, num1, num2)
        else:
            print("Opção inválida. Tente novamente.")
            continue
        continuar = input("Deseja continuar? s/n ").strip().lower()
        if continuar != "s":
            print("Programa encerrado pelo usuário.")
            break

if __name__ == "__main__":
    main()
