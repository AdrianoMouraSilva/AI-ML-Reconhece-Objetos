# ========================================
# SEGURANÇA COM TOKENS - Como funciona?
# ========================================
# Um token é como um "crachá de acesso"
# Você mostra o crachá e consegue entrar!

# Importar as coisas que vamos usar
import jwt  # JWT = linguagem de tokens
import os
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

# ========================================
# CONFIGURAÇÃO DE SEGURANÇA
# ========================================
# Esta é a "chave secreta" - tipo uma senha mestre
# NUNCA, NUNCA compartilhe isso com ninguém!
# É como a chave da sua casa - bem guardada!
SECRET_KEY = os.getenv('SECRET_KEY', 'sua-chave-secreta-super-segura-aqui')

# ========================================
# FUNÇÃO PARA CRIAR TOKEN
# ========================================
def criar_token(usuario_id, dias_validade=7):
    """
    Cria um token de segurança
    
    Pense assim:
    - usuario_id = qual usuário está entrando
    - dias_validade = quanto tempo o crachá funciona
    
    Exemplo:
    token = criar_token(usuario_id=1, dias_validade=7)
    """
    try:
        # Quando o token foi criado
        tempo_agora = datetime.utcnow()
        
        # Quando o token vai expirar (parar de funcionar)
        tempo_expiracao = tempo_agora + timedelta(days=dias_validade)
        
        # Informações que vão no token (tipo dados do crachá)
        dados_token = {
            'usuario_id': usuario_id,  # Qual usuário é
            'iat': tempo_agora,  # Quando foi criado
            'exp': tempo_expiracao  # Quando expira
        }
        
        # Criar o token usando a chave secreta
        token = jwt.encode(
            dados_token,  # O que colocar dentro
            SECRET_KEY,  # A chave secreta
            algorithm='HS256'  # Tipo de criptografia
        )
        
        return token
    except Exception as erro:
        print(f"Erro ao criar token: {erro}")
        return None


# ========================================
# FUNÇÃO PARA VERIFICAR TOKEN
# ========================================
def verificar_token(token):
    """
    Verifica se o token é válido
    
    Retorna:
    - Se válido: dados do token (quem é o usuário)
    - Se inválido: None
    
    Exemplo:
    dados = verificar_token(token_recebido)
    """
    try:
        # Decodificar o token usando a chave secreta
        dados = jwt.decode(
            token,  # O token para verificar
            SECRET_KEY,  # A chave secreta
            algorithms=['HS256']  # Tipo de criptografia esperado
        )
        return dados
    
    # Se o token expirou
    except jwt.ExpiredSignatureError:
        print("Token expirou!")
        return None
    
    # Se o token é inválido
    except jwt.InvalidTokenError:
        print("Token inválido!")
        return None
    
    # Qualquer outro erro
    except Exception as erro:
        print(f"Erro ao verificar token: {erro}")
        return None


# ========================================
# PROTETOR DE FUNÇÕES (Decorador)
# ========================================
def requer_token(funcao):
    """
    Este é um "guarda" para suas funções!
    
    Ele:
    1. Verifica se tem um token
    2. Verifica se o token é válido
    3. Se tudo OK, deixa entrar
    4. Se não, bloqueia
    
    Exemplo de uso:
    @requer_token
    def minha_funcao_secreta():
        return "Dados secretos!"
    """
    @wraps(funcao)
    def decorador(*args, **kwargs):
        # Pega o token do cabeçalho da requisição
        # Os clientes devem enviar assim:
        # Authorization: Bearer seu_token_aqui
        
        token = None
        
        if 'Authorization' in request.headers:
            # Pegar o token do cabeçalho
            auth_header = request.headers['Authorization']
            try:
                # Separar "Bearer" do token
                # Formato: "Bearer seu_token_aqui"
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'mensagem': 'Token mal formatado'}), 401
        
        # Se não tem token
        if not token:
            return jsonify({'mensagem': 'Token não fornecido'}), 401
        
        # Verificar se o token é válido
        dados = verificar_token(token)
        
        if not dados:
            return jsonify({'mensagem': 'Token inválido ou expirado'}), 401
        
        # Se passou em tudo, executar a função
        return funcao(*args, **kwargs)
    
    return decorador


# ========================================
# FUNÇÃO PARA RENOVAR TOKEN
# ========================================
def renovar_token(token_antigo):
    """
    Renova um token antigo por um novo
    
    Pense assim:
    - Seu crachá está quase vencendo?
    - Vamos trocar por um novo!
    
    Exemplo:
    novo_token = renovar_token(token_velho)
    """
    # Verificar se o token antigo é válido
    dados = verificar_token(token_antigo)
    
    if not dados:
        return None
    
    # Criar um novo token com o mesmo usuário
    novo_token = criar_token(
        usuario_id=dados['usuario_id'],
        dias_validade=7
    )
    
    return novo_token
