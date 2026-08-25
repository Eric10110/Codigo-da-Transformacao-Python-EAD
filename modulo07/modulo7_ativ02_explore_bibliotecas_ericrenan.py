
import datetime
import os
import random
from faker import Faker

# Inicializa o Faker configurado para Português do Brasil
fake = Faker("pt_BR")

# Códigos de cores ANSI para o terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def definir_situacao(media):
    if media >= 7.0:
        return f"{GREEN}APROVADO{RESET}"
    elif media >= 5.0:
        return f"{YELLOW}RECUPERAÇÃO{RESET}"
    else:
        return f"{RED}REPROVADO{RESET}"


def gerar_dados_pessoais():
    
    perfil = fake.profile()
    return {
        "nome": perfil["name"],
        "cpf": fake.cpf(),
        "nascimento": perfil["birthdate"].strftime("%d/%m/%Y"), # type: ignore
        "genero": "Feminino" if perfil["sex"] == "F" else "Masculino",
        "responsavel": fake.name(),
        "endereco": f"{fake.street_name()}, {fake.building_number()} - {fake.bairro()}, {fake.city()}/{fake.state_abbr()}",
        "matricula": fake.bothify(text="2026-#####"),
    }


def emitir_boletim_cli(dados_aluno, turma, escola, disciplinas, data_emissao):
    limpar_tela()

    media_geral = sum(d["media"] for d in disciplinas) / len(disciplinas)

    if media_geral >= 7.0:
        cor_geral, status_geral = GREEN, "APROVADO"
    elif media_geral >= 5.0:
        cor_geral, status_geral = YELLOW, "RECUPERAÇÃO"
    else:
        cor_geral, status_geral = RED, "REPROVADO"

    print("=" * 76)
    print(f"{BOLD}{escola.upper()}{RESET}".center(84))
    print("=" * 76)

    print(f" {BOLD}--- DADOS PESSOAIS DO ALUNO ---{RESET}")
    print(
        f" {BOLD}Nome:{RESET} {dados_aluno['nome']:<30} | {BOLD}Matrícula:{RESET} {dados_aluno['matricula']}"
    )
    print(
        f" {BOLD}CPF:{RESET} {dados_aluno['cpf']:<31} | {BOLD}Nascimento:{RESET} {dados_aluno['nascimento']}"
    )
    print(
        f" {BOLD}Gênero:{RESET} {dados_aluno['genero']:<28} | {BOLD}Turma:{RESET} {turma}"
    )
    print(f" {BOLD}Responsável Legal:{RESET} {dados_aluno['responsavel']}")
    print(f" {BOLD}Endereço:{RESET} {dados_aluno['endereco']}")
    print(
        f" {BOLD}Emissão do Boletim:{RESET} {data_emissao.strftime('%d/%m/%Y às %H:%M:%S')}"
    )

    print("=" * 76)
    print(
        f" {BOLD}{'DISCIPLINA':<16} | {'N1':<5} | {'N2':<5} | {'N3':<5} | {'MÉDIA':<6} | {'SITUAÇÃO'}{RESET}"
    )
    print("-" * 76)

    for d in disciplinas:
        n1, n2, n3 = d["notas"]
        print(
            f" {d['nome']:<16} | {n1:<5.1f} | {n2:<5.1f} | {n3:<5.1f} | {d['media']:<6.1f} | {d['situacao']}"
        )

    print("-" * 76)
    print(
        f" {BOLD}MÉDIA GERAL:{RESET} {cor_geral}{media_geral:.1f}{RESET}  -->  {BOLD}RESULTADO FINAL:{RESET} {cor_geral}{status_geral}{RESET}"
    )
    print("=" * 76 + "\n")


def cadastrar_disciplinas_manual(materias):
    disciplinas = []
    for materia in materias:
        print(f"\n{BOLD}--- Lançamento de Notas: {materia} ---{RESET}")
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"  -> Digite a {i}ª Nota (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    print(
                        f"     {RED}Nota inválida! Digite um valor entre 0 e 10.{RESET}"
                    )
                except ValueError:
                    print(
                        f"     {RED}Entrada inválida! Digite apenas números.{RESET}"
                    )

        media = sum(notas) / 3
        situacao = definir_situacao(media)
        disciplinas.append(
            {"nome": materia, "notas": notas, "media": media, "situacao": situacao}
        )
    return disciplinas


def gerar_disciplinas_auto(materias):
    disciplinas = []
    for materia in materias:
        notas = [round(random.uniform(3.0, 10.0), 1) for _ in range(3)]
        media = sum(notas) / 3
        situacao = definir_situacao(media)
        disciplinas.append(
            {"nome": materia, "notas": notas, "media": media, "situacao": situacao}
        )
    return disciplinas


def main():
    materias_padrao = [
        "Matemática",
        "Português",
        "História",
        "Geografia",
        "Física",
        "Biologia",
    ]

    while True:
        limpar_tela()
        print(f"{BOLD}========================================={RESET}")
        print(f"{BOLD}    SISTEMA CLI DE BOLETIM ESCOLAR      {RESET}")
        print(f"{BOLD}========================================={RESET}")
        print(" [ 1 ] Gerar Boletim Completo Automático (Faker)")
        print(" [ 2 ] Cadastrar Apenas Notas Manualmente")
        print(" [ 3 ] Sair do Sistema")
        print("-" * 41)

        opcao = input(" Escolha uma opção (1-3): ").strip()

        if opcao == "3":
            print("\nEncerrando o sistema... Até logo!\n")
            break

        if opcao in ["1", "2"]:
            data_emissao = datetime.datetime.now()
            escola = f"Colégio {fake.company()}"
            turma = f"{random.randint(1, 3)}º Ano EM"

            dados_aluno = gerar_dados_pessoais()

            if opcao == "1":
                disciplinas = gerar_disciplinas_auto(materias_padrao)
            else:
                limpar_tela()
                print(
                    f"{BOLD}Aluno Gerado:{RESET} {dados_aluno['nome']} | {BOLD}CPF:{RESET} {dados_aluno['cpf']}"
                )
                disciplinas = cadastrar_disciplinas_manual(materias_padrao)

            emitir_boletim_cli(
                dados_aluno, turma, escola, disciplinas, data_emissao
            )
            input("Pressione [ENTER] para voltar ao menu principal...")

        else:
            input(
                f"\n{RED}Opção inválida! Pressione [ENTER] para tentar novamente...{RESET}"
            )


if __name__ == "__main__":
    main()
    