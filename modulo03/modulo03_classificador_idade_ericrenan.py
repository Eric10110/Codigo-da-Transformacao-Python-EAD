from datetime import datetime

def mostrar_menu():
    print("\n--- Menu de Verificação de Idade ---")
    print("1. Informar Idade e Descobrir Ano de Nascimento")
    print("2. Sair")
    print("------------------------------------")

def obter_idade_atual():
    while True:
        try:
            idade_str = input("Digite sua idade atual: ")
            idade = int(idade_str)
            if 0 <= idade <= 120:
                return idade
            else:
                print("Idade inválida. Por favor, digite uma idade entre 0 e 120 anos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            idade_atual = obter_idade_atual()
            ano_atual = datetime.now().year
            ano_nascimento = ano_atual - idade_atual
            print(f"\nConsiderando o ano atual ({ano_atual}) e sua idade de {idade_atual} anos:")
            print(f"Seu ano de nascimento é aproximadamente: {ano_nascimento}")
            if idade_atual >= 18:
                print("Você é **MAIOR** de idade!")
            else:
                print("Você é **MENOR** de idade.")
        elif escolha == '2':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()