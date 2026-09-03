def mostrar_menu():
    print("\n--- Menu de Comparação de Números ---")
    print("1. Comparar Dois Números")
    print("2. Sair")
    print("------------------------------------")

def obter_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

def verificar_par_impar(numero):
    if int(numero) % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            print(f"\nComparando {num1} e {num2}:")
            if num1 > num2:
                print(f"O maior número é: {num1}")
            elif num2 > num1:
                print(f"O maior número é: {num2}")
            else:
                print("Os números são iguais.")
            print(f"{num1} é {verificar_par_impar(num1)}.")
            print(f"{num2} é {verificar_par_impar(num2)}.")
        elif escolha == '2':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()