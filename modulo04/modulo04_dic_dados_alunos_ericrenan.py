aluno = {
    "nome": "João da Silva",
    "idade": 17,
    "notas": [8.5, 7.0, 9.5] 
}


print("--- Ficha do Aluno ---")

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")

media_das_notas = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média das notas: {media_das_notas:.2f}") 

print(f"Notas: {aluno['notas']}")

print("----------------------")


print("\n--- Todos os Dados ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")