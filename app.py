from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "mi_token_verificacion"

@app.get("/")
def home():
    return "OK", 200

@app.get("/webhook")
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        return challenge, 200

    return "Forbidden", 403

@app.post("/webhook")
def receive():
    data = request.get_json(silent=True)
    print("INCOMING:", data)
    return "EVENT_RECEIVED", 200
