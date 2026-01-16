# ❌ Erro: print não está indentado
# def saudacao(nome):
# print("Olá,", nome)

# ✅ Solução: Indentar o corpo da função com 4 espaços
def saudacao(nome):
    print("Olá,", nome)

print("--- Teste 1: Função simples ---")
saudacao("Wilck")

# ✅ Mais exemplos com indentação correta
print("\n--- Teste 2: Múltiplas saudações ---")
nomes = ["Ana", "Bruno", "Carla", "Diego"]
for nome in nomes:
    saudacao(nome)

print("\n--- Teste 3: Função com múltiplas linhas ---")
def apresentacao(nome, idade):
    print(f"Olá, {nome}!")
    print(f"Você tem {idade} anos")
    print("Bem-vindo ao Python!")

apresentacao("Wilck", 25)

print("\n--- Teste 4: Função com condição ---")
def saudacao_personalizada(nome, hora):
    if hora < 12:
        print(f"Bom dia, {nome}!")
    elif hora < 18:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")

saudacao_personalizada("Wilck", 10)
saudacao_personalizada("Wilck", 14)
saudacao_personalizada("Wilck", 20)
