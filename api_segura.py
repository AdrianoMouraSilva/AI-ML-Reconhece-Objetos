# ========================================
# EXEMPLO DE API SEGURA COM TOKENS
# ========================================
# Uma API é um "garçom de restaurante"
# Ele: recebe pedidos e traz a comida
# 
# Mas nosso garçom pede um crachá primeiro!
# Se você não tiver, não entra!

from flask import Flask, request, jsonify
from security import criar_token, verificar_token, requer_token, renovar_token
import os

# Criar a aplicação Flask
app = Flask(__name__)

# Chave secreta para segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sua-chave-secreta-super-segura-aqui')

# ========================================
# USUÁRIOS FALSOS PARA EXEMPLO
# ========================================
# Normalmente isso viria de um banco de dados
# Mas para aprender, vamos usar isso:
USUARIOS = {
    'admin@example.com': {
        'id': 1,
        'senha': 'senha123'  # Na vida real, guardar criptografado!
    },
    'usuario@example.com': {
        'id': 2,
        'senha': 'senha456'  # Na vida real, guardar criptografado!
    }
}


# ========================================
# ROTA 1: LOGIN (Pegar token)
# ========================================
@app.route('/login', methods=['POST'])
def login():
    """
    Esta função:
    1. Recebe email e senha
    2. Verifica se está correto
    3. Se sim, cria um token
    4. Devuelve o token
    
    Exemplo de requisição:
    POST /login
    {
        "email": "admin@example.com",
        "senha": "senha123"
    }
    
    Resposta:
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "mensagem": "Login realizado com sucesso!"
    }
    """
    try:
        # Pegar email e senha do pedido
        dados = request.get_json()
        email = dados.get('email')
        senha = dados.get('senha')
        
        # Verificar se enviou email e senha
        if not email or not senha:
            return jsonify({'mensagem': 'Email e senha são obrigatórios'}), 400
        
        # Procurar o usuário
        usuario = USUARIOS.get(email)
        
        # Se não encontrou o usuário
        if not usuario:
            return jsonify({'mensagem': 'Email não encontrado'}), 401
        
        # Verificar se a senha está correta
        if usuario['senha'] != senha:
            return jsonify({'mensagem': 'Senha incorreta'}), 401
        
        # Se tudo OK, criar um token
        token = criar_token(usuario_id=usuario['id'])
        
        return jsonify({
            'mensagem': 'Login realizado com sucesso!',
            'token': token,
            'usuario_id': usuario['id']
        }), 200
    
    except Exception as erro:
        return jsonify({'mensagem': f'Erro: {str(erro)}'}), 500


# ========================================
# ROTA 2: DADOS PROTEGIDOS
# ========================================
@app.route('/dados-secretos', methods=['GET'])
@requer_token  # Este é o protetor! Só deixa entrar com token válido
def dados_secretos():
    """
    Esta função só funciona se você tiver um token válido!
    
    Exemplo de requisição:
    GET /dados-secretos
    Headers:
    {
        "Authorization": "Bearer seu_token_aqui"
    }
    
    Resposta:
    {
        "mensagem": "Esses são os dados secretos!",
        "dados": [...]
    }
    """
    return jsonify({
        'mensagem': 'Esses são os dados secretos!',
        'dados': ['info1', 'info2', 'info3']
    }), 200


# ========================================
# ROTA 3: RENOVAR TOKEN
# ========================================
@app.route('/renovar-token', methods=['POST'])
def renovar():
    """
    Renova um token antigo por um novo
    (Seu crachá está quase vencendo? Troque por um novo!)
    
    Exemplo de requisição:
    POST /renovar-token
    {
        "token": "seu_token_antigo"
    }
    
    Resposta:
    {
        "novo_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "mensagem": "Token renovado com sucesso!"
    }
    """
    try:
        # Pegar o token antigo
        dados = request.get_json()
        token_antigo = dados.get('token')
        
        if not token_antigo:
            return jsonify({'mensagem': 'Token é obrigatório'}), 400
        
        # Renovar o token
        novo_token = renovar_token(token_antigo)
        
        if not novo_token:
            return jsonify({'mensagem': 'Token inválido ou expirado'}), 401
        
        return jsonify({
            'mensagem': 'Token renovado com sucesso!',
            'novo_token': novo_token
        }), 200
    
    except Exception as erro:
        return jsonify({'mensagem': f'Erro: {str(erro)}'}), 500


# ========================================
# ROTA 4: TESTE SEM PROTEÇÃO
# ========================================
@app.route('/publica', methods=['GET'])
def publica():
    """
    Esta função é pública!
    Não precisa de token para acessar
    
    Exemplo de requisição:
    GET /publica
    
    Resposta:
    {
        "mensagem": "Olá! Você não precisa de token aqui!"
    }
    """
    return jsonify({
        'mensagem': 'Olá! Você não precisa de token aqui!'
    }), 200


# ========================================
# ROTA 5: INFORMAÇÕES DO USUÁRIO
# ========================================
@app.route('/meu-perfil', methods=['GET'])
@requer_token  # Protetor!
def meu_perfil():
    """
    Mostra informações do usuário logado
    
    Exemplo de requisição:
    GET /meu-perfil
    Headers:
    {
        "Authorization": "Bearer seu_token_aqui"
    }
    
    Resposta:
    {
        "usuario_id": 1,
        "email": "admin@example.com"
    }
    """
    # Pegar o token do cabeçalho
    auth_header = request.headers['Authorization']
    token = auth_header.split(" ")[1]
    
    # Verificar o token
    dados = verificar_token(token)
    
    # Procurar o usuário por ID
    for email, usuario in USUARIOS.items():
        if usuario['id'] == dados['usuario_id']:
            return jsonify({
                'usuario_id': usuario['id'],
                'email': email
            }), 200
    
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404


# ========================================
# TRATAMENTO DE ERROS
# ========================================
@app.errorhandler(404)
def nao_encontrado(erro):
    """
    Se a rota não existe, mostrar erro amigável
    """
    return jsonify({'mensagem': 'Rota não encontrada'}), 404


@app.errorhandler(500)
def erro_servidor(erro):
    """
    Se algo der muito errado no servidor
    """
    return jsonify({'mensagem': 'Erro interno do servidor'}), 500


# ========================================
# RODAR A APLICAÇÃO
# ========================================
if __name__ == '__main__':
    # Modo debug: código recarrega automaticamente
    app.run(
        debug=True,  # Modo desenvolvimento
        host='0.0.0.0',  # Acessível de qualquer lugar
        port=5000  # Porta onde roda
    )
