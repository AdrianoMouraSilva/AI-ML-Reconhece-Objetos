aluno = {"nome": "João", "nota": 8.5}

# ❌ Erro: chave "idade" não existe
# print(aluno["idade"])

# ✅ Solução 1: Adicionar a chave antes de acessar
print("Solução 1 - Adicionar chave:")
aluno["idade"] = 18
print(f"  Idade: {aluno['idade']}")

# ✅ Solução 2: Usar .get() com valor padrão
print("\nSolução 2 - Usar .get():")
idade = aluno.get("idade", "Não informada")
print(f"  Idade: {idade}")

# ✅ Solução 3: Verificar se chave existe
print("\nSolução 3 - Verificar existência:")
if "idade" in aluno:
    print(f"  Idade: {aluno['idade']}")
else:
    print("  Chave 'idade' não existe no dicionário")

# ✅ Solução 4: Mostrar todas as chaves disponíveis
print("\nSolução 4 - Chaves disponíveis:")
print(f"  Chaves: {list(aluno.keys())}")
