lista_de_compras = []


while True:
    
    print("\n--- Menu ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver a lista")
    print("4. Sair")

    
    escolha = input("Escolha uma opção (1-4): ")

    
    if escolha == '1':
        item = input("Digite o nome do item: ")
        
        lista_de_compras.append(item)
        print(f"✅ '{item}' adicionado!")

    
    elif escolha == '2':
        item_a_remover = input("Digite o nome do item para remover: ")
        
        if item_a_remover in lista_de_compras:
            
            lista_de_compras.remove(item_a_remover)
            print(f"🗑️ '{item_a_remover}' removido da lista.")
        else:
            
            print(f"❌ Erro: '{item_a_remover}' não está na lista.")

    
    elif escolha == '3':
        
        if lista_de_compras:
            print("\n🛒 Sua lista de compras:")
            
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
        else:
            
            print("📝 Sua lista está vazia.")

    
    elif escolha == '4':
        print("👋 Até mais!")
        break

  
    else:
        print("🚫 Opção inválida. Tente novamente.")
        