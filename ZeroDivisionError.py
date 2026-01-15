def media(total, qtd):
    """Calcula a média, validando se qtd é zero"""
    if qtd == 0:
        return 0  # Ou lançar uma exceção personalizada
    return total / qtd

# ========== TESTES ==========
print("Teste 1 - Divisão normal:")
print(f"media(10, 2) = {media(10, 2)}")  # Output: 5.0

print("\nTeste 2 - Divisão por zero (corrigida):")
print(f"media(10, 0) = {media(10, 0)}")  # Output: 0 (sem erro!)

print("\nTeste 3 - Outros valores:")
print(f"media(30, 3) = {media(30, 3)}")  # Output: 10.0
print(f"media(100, 4) = {media(100, 4)}")  # Output: 25.0