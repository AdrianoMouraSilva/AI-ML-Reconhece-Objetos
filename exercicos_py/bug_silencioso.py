print("--- ❌ Versão com bug (substitui em vez de acumular) ---")
valores = [10, 20, 30]
soma_errada = 0
for v in valores:
    soma_errada = v  # ❌ ERRO: substitui, não acumula
    print(f"  Soma = {soma_errada}")
print(f"Resultado final ERRADO: {soma_errada}")

print("\n--- ✅ Versão corrigida (com +=) ---")
valores = [10, 20, 30]
soma = 0
for v in valores:
    soma += v  # ✅ CORRETO: acumula
    print(f"  Soma = {soma}")
print(f"Resultado final CORRETO: {soma}")

print("\n--- 📊 Comparação de operadores ---")
print("= (atribuição): substitui o valor")
print("+=  (incremento): acumula o valor")

x = 10
print(f"\nExemplo:")
print(f"x = {x}")
print(f"x = x + 5 → x = {x + 5}")
print(f"x += 5 → x = {x + 5}")

print("\n--- 🔍 Teste com lista maior ---")
numeros = [5, 10, 15, 20, 25]
total = 0
for num in numeros:
    total += num
    print(f"  Adicionado {num}, total = {total}")
print(f"Soma final: {total}")
