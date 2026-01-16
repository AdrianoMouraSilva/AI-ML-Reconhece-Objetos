nota = 6

# ❌ Operador incorreto: > (maior que)
# if nota > 6:
#     print("Aprovado")

# ✅ Operador correto: >= (maior ou igual)
if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# 📊 Teste com diferentes notas
print("\n--- Testes com diferentes notas ---")
notas_teste = [4, 5, 6, 7, 10]

for n in notas_teste:
    if n >= 6:
        status = "✅ Aprovado"
    else:
        status = "❌ Reprovado"
    print(f"Nota {n}: {status}")
