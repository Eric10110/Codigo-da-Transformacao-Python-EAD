import tkinter as tk
from tkinter import messagebox, ttk


produtos = {
    "p1": {
        "nome": "Porshe 911 Turbo S ",
        "estoque": 5,
        "preco": 8125000.0,
        "ano": "10/12/2026",
        "descricao": "Carro Esportivo que pode te entergar mais de 700 cavalos de potência."
    },
    "p2": {
        "nome": "Chevrolet Corvette C7",
        "estoque": 2,
        "preco": 700000.0,
        "ano": "10/02/2002",
        "descricao": "Carro SuperEsportivo de tração traseira que pode te entregar um motor v8 chegando de 0 a 100 em 3 segundos"
    },
    "p3": {
        "nome": "Nissan Skyline GT-R R34",
        "estoque": 1,
        "preco": 2000000.0,
        "ano": "10/12/2019",
        "descricao": "Carro Esportivo marcado por sua fama e praticidade"
    }
}



def cadastrar_produto():
    def salvar_cadastro():
        vaga = combo_vaga.get()
        nome = entry_nome.get()
        
        try:
            estoque = int(entry_estoque.get())
            preco = float(entry_preco.get())
        except ValueError:
            messagebox.showerror("Erro", "Estoque deve ser inteiro e Preço deve ser numérico!")
            return
            
        ano = entry_ano.get()
        desc = entry_desc.get()

        if produtos[vaga]["nome"] == "":
            produtos[vaga]["nome"] = nome
            produtos[vaga]["estoque"] = estoque
            produtos[vaga]["preco"] = preco
            produtos[vaga]["ano"] = ano
            produtos[vaga]["descricao"] = desc
            messagebox.showinfo("Sucesso", f"🎉 Produto \"{nome}\" cadastrado na {vaga.upper()}!")
            janela_cadastrar.destroy()
        else:
            messagebox.showwarning("Aviso", f"A {vaga.upper()} já está ocupada!")

    if produtos["p1"]["nome"] != "" and produtos["p2"]["nome"] != "" and produtos["p3"]["nome"] != "":
        messagebox.showerror("Erro", "❌ Sistema cheio! Limite de 3 produtos atingido.")
        return

    janela_cadastrar = tk.Toplevel(root)
    janela_cadastrar.title("Cadastrar Produto")
    janela_cadastrar.geometry("400x350")

    tk.Label(janela_cadastrar, text="Selecione a Vaga:").pack(pady=2)
    combo_vaga = ttk.Combobox(janela_cadastrar, values=["p1", "p2", "p3"], state="readonly")
    combo_vaga.current(0)
    combo_vaga.pack(pady=2)

    tk.Label(janela_cadastrar, text="Nome do Produto:").pack(pady=2)
    entry_nome = tk.Entry(janela_cadastrar, width=40)
    entry_nome.pack(pady=2)

    tk.Label(janela_cadastrar, text="Quantidade em Estoque:").pack(pady=2)
    entry_estoque = tk.Entry(janela_cadastrar, width=40)
    entry_estoque.pack(pady=2)

    tk.Label(janela_cadastrar, text="Preço:").pack(pady=2)
    entry_preco = tk.Entry(janela_cadastrar, width=40)
    entry_preco.pack(pady=2)

    tk.Label(janela_cadastrar, text="Ano:").pack(pady=2)
    entry_ano = tk.Entry(janela_cadastrar, width=40)
    entry_ano.pack(pady=2)

    tk.Label(janela_cadastrar, text="Descrição:").pack(pady=2)
    entry_desc = tk.Entry(janela_cadastrar, width=40)
    entry_desc.pack(pady=2)

    tk.Button(janela_cadastrar, text="Salvar Cadastro", command=salvar_cadastro, bg="#4CAF50", fg="white").pack(pady=15)


def listar_produtos():
    janela_listar = tk.Toplevel(root)
    janela_listar.title("Lista de Produtos")
    janela_listar.geometry("500x400")

    texto = tk.Text(janela_listar, wrap="word", font=("Arial", 10))
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    if produtos["p1"]["nome"] == "" and produtos["p2"]["nome"] == "" and produtos["p3"]["nome"] == "":
        texto.insert("end", "Nenhum produto cadastrado no sistema ainda.\n")
    else:
        for p in ["p1", "p2", "p3"]:
            if produtos[p]["nome"] != "":
                texto.insert("end", f"Nome: {produtos[p]['nome']} | Preço: R$ {produtos[p]['preco']:.2f} | Estoque: {produtos[p]['estoque']} unid.\n")
                texto.insert("end", f"Ano: {produtos[p]['ano']} | Descrição: {produtos[p]['descricao']}\n")
                texto.insert("end", "🔥" * 30 + "\n\n")
    texto.config(state="disabled")


def realizar_venda():
    def efetuará_venda():
        nome_venda = entry_nome_venda.get().strip()
        
        if produtos["p1"]["nome"] == "" and produtos["p2"]["nome"] == "" and produtos["p3"]["nome"] == "":
            messagebox.showwarning("Aviso", "Não há produtos cadastrados para realizar vendas.")
            return

        encontrado = False
        for p in ["p1", "p2", "p3"]:
            if nome_venda.lower() == produtos[p]["nome"].lower().strip() and produtos[p]["nome"] != "":
                encontrado = True
                try:
                    qtd_venda = int(entry_qtd_venda.get())
                except ValueError:
                    messagebox.showerror("Erro", "A quantidade deve ser um número inteiro!")
                    return

                if qtd_venda <= produtos[p]["estoque"]:
                    produtos[p]["estoque"] -= qtd_venda
                    total = qtd_venda * produtos[p]["preco"]
                    messagebox.showinfo("Sucesso", f"✅ Venda realizada! Total: R$ {total:.2f}\nEstoque atual de {produtos[p]['nome']}: {produtos[p]['estoque']} unidades.")
                    janela_venda.destroy()
                else:
                    messagebox.showerror("Erro", f"❌ Estoque insuficiente! Temos apenas {produtos[p]['estoque']}.")
                break
        
        if not encontrado:
            messagebox.showerror("Erro", "🔥 Erro: Produto não encontrado!")

    janela_venda = tk.Toplevel(root)
    janela_venda.title("Realizar Venda")
    janela_venda.geometry("350x200")

    tk.Label(janela_venda, text="Digite o nome do produto:").pack(pady=5)
    entry_nome_venda = tk.Entry(janela_venda, width=30)
    entry_nome_venda.pack(pady=5)

    tk.Label(janela_venda, text="Quantidade de unidades:").pack(pady=5)
    entry_qtd_venda = tk.Entry(janela_venda, width=10)
    entry_qtd_venda.pack(pady=5)

    tk.Button(janela_venda, text="Confirmar Venda", command=efetuará_venda, bg="#2196F3", fg="white").pack(pady=10)


def buscar_por_ano():
    def executar_busca():
        ano_busca = entry_ano_busca.get()
        messagebox.showinfo("Busca", f"Buscando produtos do ano {ano_busca}...")
        janela_busca.destroy()

    if produtos["p1"]["ano"] == "" and produtos["p2"]["ano"] == "" and produtos["p3"]["ano"] == "":
        messagebox.showwarning("Aviso", "Não há produtos com esses anos para realizar vendas.")
        return

    janela_busca = tk.Toplevel(root)
    janela_busca.title("Buscar por Ano")
    janela_busca.geometry("300x150")

    tk.Label(janela_busca, text="Digite o ano de fabricação:").pack(pady=10)
    entry_ano_busca = tk.Entry(janela_busca, width=20)
    entry_ano_busca.pack(pady=5)

    tk.Button(janela_busca, text="Buscar", command=executar_busca).pack(pady=10)


def sobre_nos():
    texto = ("Somos a Industria XYZ uma renomada industria que vem trabalhando com a fabricação de automóveis "
             "de alta performance e qualidade dês de 1990 com o objetivo de poder dar destaque a modelos "
             "incriveis de carros pouco vistos nas ruas atualmente\n\n"
             "Nossos contatos...\n"
             "Telefone: (11) 1234-5678\n"
             "Email: Xyzcarros@gmail.com")
    messagebox.showinfo("Sobre Nós", texto)


def agendamento_visitas():
    texto = ("Dias disponíveis para agendamento de visitas: Segunda a Quinta-feira, das 9h às 18h.\n\n"
             "Para agendar uma visita, entre em contato conosco pelo telefone (11) 1234-5678 "
             "ou pelo email: Xyzcarros@gmail.com")
    messagebox.showinfo("Agendamento de Visitas", texto)


def documentacao_carros():
    def mostrar_doc():
        nome = entry_user.get()
        texto_doc = (f"Olá {nome}, seja bem-vindo à documentação dos carros!\n"
                     "Aqui você encontrará informações detalhadas sobre cada modelo de carro disponível em nosso sistema.\n\n"
                     "1. Porshe 911 Turbo S: IPVA Médio varia de R$ 58.000,00 a mais de R$ 80.000,00, dependendo do ano do veículo e do estado de registro.\n\n"
                     "2. Chevrolet Corvette C7: IPVA médio anual fica entre R$ 20.000 e R$ 35.000, dependendo do ano/modelo e da versão do veículo.\n\n"
                     "3. Nissan Skyline GT-R R34: IPVA Médio cerca de R$ 800.000 a mais de R$ 1 milhão.")
        
        janela_doc.destroy()
        
        janela_texto = tk.Toplevel(root)
        janela_texto.title("Documentação Oficial")
        tk.Label(janela_texto, text=texto_doc, justify="left", padx=15, pady=15, font=("Arial", 10)).pack()

    janela_doc = tk.Toplevel(root)
    janela_doc.title("Acessar Documentação")
    janela_doc.geometry("300x120")
    
    tk.Label(janela_doc, text="Digite seu nome para começar:").pack(pady=5)
    entry_user = tk.Entry(janela_doc, width=25)
    entry_user.pack(pady=5)
    tk.Button(janela_doc, text="Entrar", command=mostrar_doc).pack(pady=5)


def formas_pagamento():
    texto = ("Formas de pagamento disponíveis:\n"
             "1. Cartão de crédito (Visa, MasterCard)\n"
             "2. Boleto bancário\n"
             "3. Transferência bancária\n"
             "4. Pix\n"
             "5. Financiamento (consulte condições na opção 9)")
    messagebox.showinfo("Formas de Pagamento", texto)


def financiamento():
    texto = ("Opção de financiamento:\n"
             "Oferecemos financiamento para a compra de veículos, com condições especiais e taxas "
             "que cabem no seu bolso financiando em até 60 Vezes.\n\n"
             "Para mais informações sobre o financiamento, entre em contato conosco pelo telefone (11) 1234-5678 "
             "ou pelo email: Xyzcarros@gmail.com")
    messagebox.showinfo("Financiamento", texto)


root = tk.Tk()
root.title("Sistema de Vendas - Indústria de Automóveis")
root.geometry("500x550")
root.configure(bg="#f0f0f0")

label_titulo = tk.Label(
    root, 
    text="Bem-vindo ao Sistema de Vendas!\nIndústria de Automóveis", 
    font=("Arial", 14, "bold"), 
    bg="#f0f0f0", 
    fg="#333"
)
label_titulo.pack(pady=20)

estilo_botao = {
    "font": ("Arial", 11),
    "width": 35,
    "bg": "#ffffff",
    "fg": "#333333",
    "bd": 1,
    "relief": "solid",
    "activebackground": "#e0e0e0"
}

tk.Button(root, text="1 - Cadastrar produto", command=cadastrar_produto, **estilo_botao).pack(pady=4)
tk.Button(root, text="2 - Listar produtos", command=listar_produtos, **estilo_botao).pack(pady=4)
tk.Button(root, text="3 - Realizar venda", command=realizar_venda, **estilo_botao).pack(pady=4)
tk.Button(root, text="4 - Buscar por ano de fabricação", command=buscar_por_ano, **estilo_botao).pack(pady=4)
tk.Button(root, text="5 - Sobre nós", command=sobre_nos, **estilo_botao).pack(pady=4)
tk.Button(root, text="6 - Agendamento de visitas", command=agendamento_visitas, **estilo_botao).pack(pady=4)
tk.Button(root, text="7 - Documentação dos carros", command=documentacao_carros, **estilo_botao).pack(pady=4)
tk.Button(root, text="8 - Formas de pagamento", command=formas_pagamento, **estilo_botao).pack(pady=4)
tk.Button(root, text="9 - Financiamento", command=financiamento, **estilo_botao).pack(pady=4)

tk.Label(root, text="--------------------------------------", bg="#f0f0f0", fg="#aaa").pack(pady=10)

tk.Button(root, text="0 - Sair", command=root.quit, font=("Arial", 11, "bold"), width=35, bg="#d32f2f", fg="white", bd=0).pack(pady=4)

label_rodape = tk.Label(root, text="Modo GUI Ativo", font=("Arial", 8), bg="#f0f0f0", fg="#888")
label_rodape.pack(side="bottom", pady=5)

root.mainloop()