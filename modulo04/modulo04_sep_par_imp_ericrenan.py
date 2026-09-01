numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = []
impares = [] 
print("--- Verificando os números... ---")
for numero in numeros:
    
    if numero % 2 == 0:
        
        print(f"O número {numero} é PAR.")
        pares.append(numero)
    else:
        # Se não for par, ele é ÍMPAR.
        print(f"O número {numero} é ÍMPAR.")
        impares.append(numero)


print("\n--- Resultado Final ---")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")