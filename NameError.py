def area_retangulo(base, altura):
    return base * altura

# ========== TESTES ==========
print("Teste 1 - Definindo a variável:")
largura = 5  # ✅ Agora a variável está definida!
altura = 10
resultado = area_retangulo(largura, altura)
print(f"Área do retângulo ({largura} x {altura}) = {resultado}")

print("\nTeste 2 - Usando valores diretos:")
print(f"Área do retângulo (20 x 15) = {area_retangulo(20, 15)}")

print("\nTeste 3 - Com diferentes dimensões:")
dimensoes = [(5, 10), (7, 3), (12, 8)]
for base, alt in dimensoes:
    print(f"Área ({base} x {alt}) = {area_retangulo(base, alt)}")