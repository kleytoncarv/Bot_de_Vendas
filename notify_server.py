from flask import Flask, request
from plyer import notification

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    try:
        data = request.json
        
        username = data.get('username', 'Usuário desconhecido')

        notification.notify(
            title="Novo login no site",
            message=f"O usuário {username} acabou de fazer o login.",
            app_name="Servidor de Notificação",
            timeout=5
        )

        print(f"Usuário {username} efetuou login!")
        return 'Notificado com sucesso', 200
    except Exception as e:
        return f"Erro: {str(e)}", 400

if __name__ == '__main__':
    app.run(port=5001)
