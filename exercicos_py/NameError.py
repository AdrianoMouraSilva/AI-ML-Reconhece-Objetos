def area_retangulo(base, altura):
    return base * altura

# ❌ Erro: variável 'largura' não foi definida
# print(area_retangulo(largura, 10))

# ✅ Solução 1: Definir a variável antes de usar
print("--- Solução 1: Definir variável ---")
largura = 5
altura = 10
resultado = area_retangulo(largura, altura)
print(f"Área do retângulo: {resultado}")

# ✅ Solução 2: Usar valores diretos
print("\n--- Solução 2: Valores diretos ---")
print(f"Área: {area_retangulo(7, 4)}")

# ✅ Solução 3: Usar variáveis com nomes descritivos
print("\n--- Solução 3: Nomes descritivos ---")
base_retangulo = 6
altura_retangulo = 8
area = area_retangulo(base_retangulo, altura_retangulo)
print(f"Base: {base_retangulo}, Altura: {altura_retangulo}")
print(f"Área: {area}")

# 📊 Teste: Calcular várias áreas
print("\n--- 📊 Teste com múltiplos retângulos ---")
medidas = [
    (3, 4),
    (5, 5),
    (10, 2),
    (7, 8)
]

for base, altura in medidas:
    area = area_retangulo(base, altura)
    print(f"Retângulo {base}x{altura}: Área = {area}")
