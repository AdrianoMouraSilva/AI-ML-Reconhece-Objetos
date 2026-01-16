# ========================================
# COMO USAR A API SEGURA - GUIA PRÁTICO
# ========================================
# Este arquivo mostra EXEMPLOS DE USO
# Você pode testar aqui!

# ========================================
# PASSO 1: INSTALAR BIBLIOTECAS
# ========================================
"""
Abra o terminal e rode:
pip install flask pyjwt requests

Explicação:
- flask = nossa API
- pyjwt = para trabalhar com tokens
- requests = para testar a API
"""

# ========================================
# PASSO 2: COMO FAZER LOGIN (Exemplo 1)
# ========================================
import requests

# URL da nossa API
URL_BASE = "http://localhost:5000"

# Dados do usuário que quer fazer login
usuario = {
    "email": "admin@example.com",
    "senha": "senha123"
}

print("=== PASSO 1: FAZER LOGIN ===")
print()

# Fazer requisição POST para /login
resposta = requests.post(f"{URL_BASE}/login", json=usuario)

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")
print()

# Pegar o token da resposta
dados_resposta = resposta.json()
token = dados_resposta['token']

print(f"Token recebido: {token}")
print()


# ========================================
# PASSO 3: USAR O TOKEN (Exemplo 2)
# ========================================
print("=== PASSO 2: ACESSAR DADOS PROTEGIDOS ===")
print()

# Cabeçalho com o token
# Sempre no formato: "Authorization: Bearer seu_token"
cabecalho = {
    "Authorization": f"Bearer {token}"
}

# Fazer requisição GET para /dados-secretos
resposta = requests.get(f"{URL_BASE}/dados-secretos", headers=cabecalho)

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")
print()


# ========================================
# PASSO 4: ACESSAR ROTA PÚBLICA (Exemplo 3)
# ========================================
print("=== PASSO 3: ACESSAR ROTA PÚBLICA (SEM TOKEN) ===")
print()

# Não precisa de token!
resposta = requests.get(f"{URL_BASE}/publica")

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")
print()


# ========================================
# PASSO 5: TENTAR ACESSAR SEM TOKEN (Exemplo 4)
# ========================================
print("=== PASSO 4: TENTAR ACESSAR SEM TOKEN (VAI DAR ERRO) ===")
print()

# Tentar acessar sem token
resposta = requests.get(f"{URL_BASE}/dados-secretos")

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")
print()


# ========================================
# PASSO 6: VER INFORMAÇÕES DO USUÁRIO (Exemplo 5)
# ========================================
print("=== PASSO 5: VER INFORMAÇÕES DO USUÁRIO ===")
print()

# Com o token
cabecalho = {
    "Authorization": f"Bearer {token}"
}

resposta = requests.get(f"{URL_BASE}/meu-perfil", headers=cabecalho)

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")
print()


# ========================================
# PASSO 7: RENOVAR TOKEN (Exemplo 6)
# ========================================
print("=== PASSO 6: RENOVAR TOKEN ===")
print()

# Enviar o token antigo para renovar
dados_renovacao = {
    "token": token
}

resposta = requests.post(f"{URL_BASE}/renovar-token", json=dados_renovacao)

print(f"Status: {resposta.status_code}")
print(f"Resposta: {resposta.json()}")

if resposta.status_code == 200:
    novo_token = resposta.json()['novo_token']
    print(f"Novo token: {novo_token}")
print()


# ========================================
# RESUMO: COMO FUNCIONA
# ========================================
print("""
========================================
RESUMO DO SISTEMA DE SEGURANÇA COM TOKENS
========================================

1️⃣ LOGIN:
   - Você envia: email + senha
   - API retorna: token (tipo um crachá)
   
2️⃣ USAR O TOKEN:
   - Você envia: Authorization: Bearer seu_token
   - API verifica: Token é válido?
   - Se SIM: retorna os dados secretos
   - Se NÃO: bloqueia o acesso

3️⃣ TOKEN EXPIRA:
   - Após alguns dias, o token vence
   - Você pode renovar para um novo

4️⃣ SEGURANÇA:
   - Token é criptografado
   - Só quem tem a chave secreta consegue ler
   - Token pode expirar automaticamente

========================================
ANALOGIA DO MUNDO REAL
========================================

Imagine um cinema:
🎬 Sem token:
   - Você quer entrar
   - Segurança: "Mostra seu ticket"
   - Você: "Não tenho"
   - Segurança: "Então não entra!" ❌

🎬 Com token:
   - Você compra um ticket
   - Mostra para a segurança
   - Segurança verifica se é real
   - Segurança: "Pode entrar!" ✅

🎬 Token expirado:
   - Seu ticket é de 2020
   - Segurança: "Isso expirou!"
   - Você: "Vou comprar um novo"
   - Segurança: "Agora pode entrar!" ✅

========================================
""")


# ========================================
# EQUIVALENTE EM PYTHON (SEM REQUESTS)
# ========================================
"""
Se quiser testar de forma mais manual:

Usando curl no terminal:

# 1. Fazer login:
curl -X POST http://localhost:5000/login \\
  -H "Content-Type: application/json" \\
  -d '{"email":"admin@example.com","senha":"senha123"}'

# 2. Acessar dados protegidos:
curl -H "Authorization: Bearer SEU_TOKEN_AQUI" \\
  http://localhost:5000/dados-secretos

# 3. Acessar rota pública:
curl http://localhost:5000/publica

# 4. Renovar token:
curl -X POST http://localhost:5000/renovar-token \\
  -H "Content-Type: application/json" \\
  -d '{"token":"SEU_TOKEN_AQUI"}'
"""
