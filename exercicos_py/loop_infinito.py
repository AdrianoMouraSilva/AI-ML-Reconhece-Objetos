import time

# ❌ Loop infinito - comentado para não travar
# i = 0
# while i < 5:
#     print(i)
#     # Falta: i += 1

print("--- ✅ Solução 1: Incrementar i ---")
i = 0
while i < 5:
    print(i)
    i += 1  # ESSENCIAL: incrementar a variável

print("\n--- ✅ Solução 2: Usar for (mais recomendado) ---")
for i in range(5):
    print(i)

print("\n--- ✅ Solução 3: While com condição de saída ---")
count = 0
while count < 5:
    print(count)
    count += 1

print("\n--- 📊 Teste: Comparação de métodos ---")
print("\nMétodo 1 (while com incremento):")
i = 0
while i < 3:
    print(f"  Iteração {i}")
    i += 1

print("\nMétodo 2 (for range):")
for i in range(3):
    print(f"  Iteração {i}")
