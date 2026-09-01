#importação e definiçoes de campos.
import csv

nome_arquivo = "notas_alunos.csv"
campos = ["Aluno", "Materia", "Nota"]

#Campo de definiçoes do dicionario.
notas = [
    {"Aluno": "Ivan Silva", "Materia": "Matemática", "Nota": 9.5},
    {"Aluno": "Beatriz Vitoria", "Materia": "Portugues", "Nota": 10.0},
    {"Aluno": "Eric Renan", "Materia": "Educação fisica", "Nota": 8.5}
]

# Usa utf-8-sig para garantir poucos erros de acentuação.
with open(nome_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(clientes_notas := notas)

print(f"✅ Notas salvas no arquivo '{nome_arquivo}'!")

# carregamento e exibições.
print("\n--- Lendo o arquivo CSV de Notas ---")
with open(nome_arquivo, "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Aluno: {linha['Aluno']} | Matéria: {linha['Materia']} | Nota: {linha['Nota']}")