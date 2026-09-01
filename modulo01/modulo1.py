p1_nome = "açaí comum"
p1_estoque = 100
p1_preco = 8.90
p1_validade = "10/12/2026"
p1_descricao = "Açaí comum, ideal para quem gosta de um sabor clássico."


p2_nome = "açaí guarana"
p2_estoque = 50
p2_preco = 12.90
p2_validade = "10/10/2026"
p2_descricao = "Açaí guarana, com sabor refrescante e ingredientes de qualidade."

p3_nome = "açaí cupuaçu"
p3_estoque = 130
p3_preco = 15.90
p3_validade = "10/12/2026"
p3_descricao = "Açaí cupuaçu, com ingredientes locais e sabor autêntico."


while True: 
    print('-' * 48 + '\n')
    print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar venda')

    print('0 - Sair')
    print('\n--------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
        if p1_nome == "":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')           
        elif p2_nome == "":
                p2_nome = input('Digite o nome do produto: ')
                p2_estoque = int(input('Digite a quantidade em estoque: '))
                p2_preco = float(input('Digite o preço do produto: '))
                p2_validade = input('Digite a validade do produto: ')    
                p2_descricao = input('Digite a descrição do produto: ')
                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_validade = input('Digite a validade do produto: ')    
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')
            
        else:
            print('❌ Sistema cheio! Limite de 3 produtos atingido.')

    elif opcao == '2':
        print('Listando produtos...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":

            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            
            if p1_nome != "":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Validade: {p1_validade} | Descrição: {p1_descricao}")

                print('🔥' * 30)
                
         
            if p2_nome != "":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Validade: {p2_validade} | Descrição: {p2_descricao}")

                print('🔥' * 30)
                
            
            if p3_nome != "":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")

                print('🔥' * 30)

    elif opcao == '3':
        print('Realizando venda...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print(f'Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')

    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')