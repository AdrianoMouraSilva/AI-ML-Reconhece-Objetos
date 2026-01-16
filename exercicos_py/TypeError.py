idade = input("Digite sua idade: ")

# ✅ Conversão correta: converter string para inteiro
idade_int = int(idade)  # Converter string em número
proxima_idade = idade_int + 1

print("Ano que vem você terá " + str(proxima_idade))

# ========== TESTES ADICIONAIS ==========
print("\n--- Teste 1: Modo 1 (como acima) ---")
idade = "25"
idade_int = int(idade)
print("Ano que vem você terá " + str(idade_int + 1))

print("\n--- Teste 2: Modo 2 (com f-string) ---")
idade = "30"
print(f"Ano que vem você terá {int(idade) + 1}")

print("\n--- Teste 3: Modo 3 (input direto) ---")
idade = "18"
print("Ano que vem você terá", int(idade) + 1)