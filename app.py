from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para o UptimeRobot (Porta da frente)
@app.route('/', methods=['GET'])
def manter_acordado():
    return "Servidor acordado e pronto para a Pluggy!", 200

# Rota para a Pluggy (Porta dos fundos)
@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.json
    
    if not dados:
        return jsonify({"erro": "Nenhum dado recebido"}), 400

    evento = dados.get('event')
    item_id = dados.get('itemId')
    
    print("\n" + "="*40)
    print(f"🔔 NOVO AVISO DA PLUGGY RECEBIDO!")
    print(f"Evento: {evento}")
    print(f"Item ID: {item_id}")
    print("="*40 + "\n")

    return jsonify({"status": "sucesso", "mensagem": "Webhook recebido"}), 200
