agenda = {}

while True:
   
    print("\n--- Menu da Agenda ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Ver Todos os Contatos")
    print("5. Sair")
    
    
    escolha = input("Escolha uma opção (1-5): ")

   
    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        
        if nome in agenda:
            print(f"❌ Erro: O contato '{nome}' já existe.")
        else:
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            
            agenda[nome] = {"telefone": telefone, "email": email}
            print(f"✅ Contato '{nome}' adicionado com sucesso!")

    #
    elif escolha == '2':
        nome = input("Digite o nome do contato para remover: ")
     
        if nome in agenda:
            del agenda[nome]
            print(f"🗑️ Contato '{nome}' removido.")
        else:
            print(f"❌ Erro: O contato '{nome}' não foi encontrado.")

    elif escolha == '3':
        nome = input("Digite o nome do contato para buscar: ")
        if nome in agenda:
            contato = agenda[nome]
            print(f"\n--- Detalhes do Contato: {nome} ---")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("---------------------------------------")
        else:
            print(f"❌ Erro: O contato '{nome}' não foi encontrado.")
            
    elif escolha == '4':
        if not agenda:
            print("📝 Sua agenda está vazia.")
        else:
            print("\n--- Todos os Contatos ---")
            for nome, detalhes in agenda.items():
                print(f"Nome: {nome}")
                print(f"  Telefone: {detalhes['telefone']}")
                print(f"  Email: {detalhes['email']}")
                print("-------------------------")
            
    elif escolha == '5':
        print("👋 Saindo da agenda. Até mais!")
        break 
    
    else:
        print("🚫 Opção inválida. Por favor, digite um número de 1 a 5.")