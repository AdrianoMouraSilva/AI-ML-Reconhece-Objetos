from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def saudacao():
    return {'mensagem': 'Olá, Mundo!'}

@app.route('/status')
def status():
    return {'status': 'ok'}

@app.route('/primo/<int:numero>')
def verificar_primo(numero):
    if numero < 2:
        return jsonify({'numero': numero, 'primo': False})
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return jsonify({'numero': numero, 'primo': False})
    return jsonify({'numero': numero, 'primo': True})

app.run(debug=True, host='0.0.0.0', port=5000)  