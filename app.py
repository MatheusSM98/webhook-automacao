from flask import Flask, request, jsonify

# Inicializa o aplicativo Flask (o seu servidor)
app = Flask(__name__)

# Cria uma "rota" (uma porta de entrada) chamada /webhook
# A Pluggy só sabe mandar mensagens do tipo POST
@app.route('/webhook', methods=['POST'])
def receber_webhook():
    # 1. Captura a mensagem (o pacote de dados JSON) que a Pluggy enviou
    dados = request.json
    
    # Se não houver dados, retorna um erro
    if not dados:
        return jsonify({"erro": "Nenhum dado recebido"}), 400

    # 2. Extrai as informações importantes do aviso
    evento = dados.get('event')      # Ex: 'item/updated' ou 'transactions/new'
    item_id = dados.get('itemId')    # O ID da conexão do banco
    
    print("\n" + "="*40)
    print(f"🔔 NOVO AVISO DA PLUGGY RECEBIDO!")
    print(f"Evento: {evento}")
    print(f"Item ID: {item_id}")
    print("="*40 + "\n")

    # 3. Lógica de Negócio: O que fazer com esse aviso?
    if evento == 'item/updated':
        print("-> O extrato foi atualizado no banco!")
        # É NESTE MOMENTO que o seu código acionaria aquela função que 
        # escrevemos antes para baixar as transações e atualizar a 
        # planilha de controle financeiro da empresa de engenharia.
        
    elif evento == 'item/error':
        print("-> Ops, a conexão falhou. O cliente precisa reautenticar.")

    # 4. Responde para a Pluggy: "Recebi a mensagem, muito obrigado!"
    # Se você não retornar 200 (OK), a Pluggy acha que seu servidor caiu e tenta mandar de novo.
    return jsonify({"status": "sucesso", "mensagem": "Webhook recebido"}), 200

# Esta parte faz o servidor rodar de fato quando você executa o script
if __name__ == '__main__':
    print("🚀 Servidor Webhook rodando na porta 5000...")
    # O debug=True faz o servidor reiniciar sozinho se você alterar o código
    app.run(port=5000, debug=True)