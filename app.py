from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "mi_token_verification"  # cámbialo por el tuyo (sin espacios)

@app.get("/webhook")
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200  # IMPORTANTE: devolver SOLO el challenge
    return "Forbidden", 403

@app.post("/webhook")
def receive_webhook():
    # Por ahora solo confirmamos recepción
    data = request.get_json(silent=True)
    return "OK", 200
