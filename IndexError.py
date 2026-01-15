nomes = ["Ana", "Bia", "Caio"]

# ✅ Solução 1: Usar len() para iterar corretamente
print("Solução 1 - Com range(len()):")
for i in range(len(nomes)):
    print(f"  {i}: {nomes[i]}")

# ✅ Solução 2: Iterar diretamente (mais Pythônico)
print("\nSolução 2 - Iteração direta:")
for nome in nomes:
    print(f"  {nome}")

# ✅ Solução 3: Com enumerate
print("\nSolução 3 - Com enumerate:")
for i, nome in enumerate(nomes):
    print(f"  {i}: {nome}")