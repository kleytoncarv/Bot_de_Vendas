from flask import Flask, request
from plyer import notification

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    username = data.get('username', 'Usuário desconhecido')

    notification.notify(
        title="Novo login no site",
        message=f"O usuário {username} acabou de fazer o login.",
        app_name="Servidor de Notificação",
        timeout=5
    )

    print(f"Usuário {username} efetuou login!")
    # Aqui você pode adicionar lógica para exibir notificações no seu PC
    return 'Notificado com sucesso', 200

if __name__ == '__main__':
    app.run(port=5001)
