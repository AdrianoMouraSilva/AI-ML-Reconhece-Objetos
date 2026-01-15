print("--- ❌ Versão com erro ---")
def dobro_errado(n):
    n * 2  # Calcula mas não retorna

resultado = dobro_errado(7)
print(f"dobro_errado(7) = {resultado}")  # Imprime: None

print("\n--- ✅ Solução: Adicionar return ---")
def dobro(n):
    return n * 2

resultado = dobro(7)
print(f"dobro(7) = {resultado}")  # Imprime: 14

print("\n--- 📊 Testes com diferentes valores ---")
valores_teste = [3, 5, 7, 10, 15]

for valor in valores_teste:
    resultado = dobro(valor)
    print(f"dobro({valor}) = {resultado}")

print("\n--- 🔍 Boas práticas ---")
# Com documentação e type hints
def triplo(n: int) -> int:
    """Retorna o triplo do número."""
    return n * 3

print(f"triplo(5) = {triplo(5)}")

# Função com múltiplas operações
def operacoes(n: int) -> dict:
    """Retorna dicionário com várias operações."""
    return {
        "dobro": n * 2,
        "triplo": n * 3,
        "quadrado": n ** 2
    }

resultado = operacoes(4)
print(f"\nOperações com 4: {resultado}")
