def calcular_media(notas):
    # Definimos a nota mínima para aprovação. Você pode mudar esse valor.
    nota_minima_para_aprovar = 7.0

    # Verificamos se a lista não está vazia para evitar um erro de divisão por zero.
    if not notas:
        return "Nenhuma nota fornecida."
    
    # Fazemos a mágica do cálculo: somamos todas as notas e dividimos
    # pelo número total de notas.
    media = sum(notas) / len(notas)

    # Exibimos a média calculada para o usuário.
    print(f"A média do aluno é: {media:.2f}")

    # Usamos uma condição para verificar se o aluno foi aprovado ou não.
    if media >= nota_minima_para_aprovar:
        return "🎉 Aprovado!"
    else:
        return "😞 Reprovado."

# ======================================================================
# 🔄 Passo 2: Usar a função com exemplos
# Vamos testar a função com diferentes listas de notas.

print("--- Cenário 1: Aluno Aprovado ---")
notas_aluno1 = [8.5, 7.0, 9.0]
resultado1 = calcular_media(notas_aluno1)
print(f"Resultado: {resultado1}\n")

print("--- Cenário 2: Aluno Reprovado ---")
notas_aluno2 = [5.5, 6.0, 4.5]
resultado2 = calcular_media(notas_aluno2)
print(f"Resultado: {resultado2}\n")

print("--- Cenário 3: Lista de notas vazia ---")
notas_aluno3 = []
resultado3 = calcular_media(notas_aluno3)
print(f"Resultado: {resultado3}")