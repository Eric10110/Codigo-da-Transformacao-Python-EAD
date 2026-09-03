def mostrar_menu():
    print("\n--- Menu de Operações ---")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Sair")
    print("------------------------")

def obter_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            resultado = num1 + num2
            print(f"Resultado da adição: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            num1, num2 = obter_numeros()
            resultado = num1 - num2
            print(f"Resultado da subtração: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
