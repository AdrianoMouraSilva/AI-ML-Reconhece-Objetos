# 🔐 GUIA DE SEGURANÇA COM TOKENS JWT

## 📚 O que é um Token?

Um **token** é como um **crachá de segurança**:
- 🎫 Você entra e recebe um crachá
- 🚪 Usa o crachá para acessar áreas restritas
- ⏰ O crachá expira depois de alguns dias
- 🔄 Você pode renovar para um novo

---

## 🏗️ Arquivos Criados

### 1️⃣ `security.py`
**O "cofre" de segurança** - Contém:
- `criar_token()` - Cria um novo crachá (token)
- `verificar_token()` - Verifica se o crachá é real
- `renovar_token()` - Cria um crachá novo
- `@requer_token` - Protetor de funções

### 2️⃣ `api_segura.py`
**A API protegida** - Com as rotas:
- `POST /login` - Fazer login (receber token)
- `GET /publica` - Sem proteção (pública)
- `GET /dados-secretos` - COM proteção (precisa token)
- `GET /meu-perfil` - COM proteção (precisa token)
- `POST /renovar-token` - Renovar o token

### 3️⃣ `exemplos_uso.py`
**Exemplos práticos** de como usar a API

---

## 🚀 Como Usar

### PASSO 1: Instalar dependências
```bash
pip install flask pyjwt requests
```

### PASSO 2: Rodar a API
```bash
python api_segura.py
```

A API estará em: `http://localhost:5000`

### PASSO 3: Fazer Login
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","senha":"senha123"}'
```

**Resposta:**
```json
{
  "mensagem": "Login realizado com sucesso!",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "usuario_id": 1
}
```

### PASSO 4: Usar o Token
```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." \
  http://localhost:5000/dados-secretos
```

**Resposta:**
```json
{
  "mensagem": "Esses são os dados secretos!",
  "dados": ["info1", "info2", "info3"]
}
```

---

## 📊 Fluxo de Funcionamento

```
┌─────────────────┐
│   1. LOGIN      │
│ Email + Senha   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  API Verifica   │
│  Dados estão    │
│  corretos?      │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
   SIM        NÃO
    │          │
    ▼          ▼
┌──────┐   ┌──────────┐
│TOKEN │   │ ERRO 401 │
│CRIADO│   │ Bloqueado│
└──────┘   └──────────┘
    │
    ▼
┌─────────────────┐
│  2. USAR TOKEN  │
│  GET /dados     │
│  + Bearer Token │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  API Verifica   │
│  Token é       │
│  válido?        │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
   SIM        NÃO
    │          │
    ▼          ▼
┌──────────┐ ┌──────────┐
│  DADOS   │ │ ERRO 401 │
│ SECRETOS │ │ Bloqueado│
└──────────┘ └──────────┘
```

---

## 🔒 Usuários Padrão

Para testar, use:

| Email | Senha | ID |
|-------|-------|-----|
| admin@example.com | senha123 | 1 |
| usuario@example.com | senha456 | 2 |

---

## 🛡️ Segurança: O que NÃO fazer

❌ **Nunca compartilhe o `SECRET_KEY`**
- É como a chave da sua casa
- Quem tem, consegue criar tokens falsos

❌ **Nunca guarde senhas em texto plano**
- Sempre criptografe com `bcrypt` ou `argon2`

❌ **Nunca expire tokens muito rápido**
- Tokens com 1 minuto são chatos
- Use 7-30 dias

❌ **Nunca coloque dados sensíveis no token**
- Token é criptografado, mas alguém pode copiar
- Coloque só o ID do usuário

---

## 🎯 O Que Acontece em Cada Situação

### ✅ Sucesso: Token Válido
```
Cliente: GET /dados-secretos + Token ✓
API: Token é válido? SIM ✓
Cliente: Recebe os dados secretos 🎉
```

### ❌ Erro: Sem Token
```
Cliente: GET /dados-secretos (sem token)
API: Token é obrigatório!
Cliente: Erro 401 (não autorizado) ❌
```

### ❌ Erro: Token Expirado
```
Cliente: GET /dados-secretos + Token (de 2020)
API: Token expirou!
Cliente: Pode renovar: POST /renovar-token ⏰
```

### ❌ Erro: Token Falso
```
Cliente: GET /dados-secretos + Token (inventado)
API: Token inválido! Não consigo decodificar
Cliente: Erro 401 (não autorizado) ❌
```

---

## 🔄 Como Renovar Token

**Seu token está quase vencendo?**

```bash
curl -X POST http://localhost:5000/renovar-token \
  -H "Content-Type: application/json" \
  -d '{"token":"seu_token_antigo"}'
```

**Resposta:**
```json
{
  "mensagem": "Token renovado com sucesso!",
  "novo_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

Agora use o novo token! ✨

---

## 📝 Resumo Rápido

| O que? | Como? |
|--------|-------|
| Fazer login | `POST /login` com email + senha |
| Acessar dados protegidos | `GET /dados-secretos` + token no header |
| Token expirou? | `POST /renovar-token` com token antigo |
| Rota pública | Nenhum token necessário! |

---

## 🎓 Conceitos Importantes

### JWT (JSON Web Token)
- É um padrão internacional
- Formato: `header.payload.signature`
- Criptografado, mas não secreto
- Qualquer um consegue ler, mas não consegue forjar

### HS256
- Algoritmo de criptografia
- "H" = HMAC (chave compartilhada)
- "S256" = SHA-256 (muito seguro)

### exp (expiration)
- Data e hora que o token vence
- Depois disso, o token não funciona mais
- Serve para segurança (se roubar, não dura pra sempre)

### iat (issued at)
- Data e hora que o token foi criado
- Ajuda a rastrear tokens antigos

---

## 🚨 Erros Comuns

### Erro: `ModuleNotFoundError: No module named 'jwt'`
**Solução:** Instale a biblioteca
```bash
pip install pyjwt
```

### Erro: `AuthenticationError` ao tentar acessar dados
**Solução:** Verifique se o token está correto no header
```bash
# ✅ Correto
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...

# ❌ Errado
Authorization: eyJ0eXAiOiJKV1QiLCJhbGc...
Authorization: Bearer__eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Erro: Token inválido
**Solução:** Token expirou ou não é válido
```bash
# Renove o token
curl -X POST http://localhost:5000/renovar-token \
  -H "Content-Type: application/json" \
  -d '{"token":"seu_token"}'
```

---

## 💡 Dicas Extras

### 1. Usar Variáveis de Ambiente
Não coloque a chave secreta no código:
```python
# ❌ Ruim
SECRET_KEY = 'senha123'

# ✅ Bom
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_padrao')
```

### 2. Armazenar Senhas com Hash
```bash
pip install bcrypt

import bcrypt
senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
```

### 3. Usar HTTPS em Produção
Sempre! HTTPS + Token = muito seguro!

### 4. Logs de Acesso
Registre quem tentou acessar o quê e quando

### 5. Rate Limiting
Limite quantas requisições uma pessoa consegue fazer

---

## 📚 Próximos Passos

1. ✅ Entender tokens JWT
2. ✅ Criar uma API segura
3. 🔜 Integrar com banco de dados
4. 🔜 Adicionar autenticação com Google/GitHub
5. 🔜 Usar HTTPS
6. 🔜 Implementar 2FA (autenticação de dois fatores)

---

## 🎉 Parabéns!

Você aprendeu segurança básica com tokens!

Agora sua API está muito mais segura! 🔒

Se tiver dúvidas, releia os comentários nos arquivos.
Eles explicam tudo como se fosse para uma criança! 👶

