from flask import Flask, request, Response
import os

app = Flask(__name__)

VERIFY_TOKEN = "12345"  # EXACTAMENTE el mismo que pusiste en Meta

@app.route("/", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verificado correctamente")
        return Response(challenge, status=200)
    else:
        print("Fallo en verificación")
        return Response("Forbidden", status=403)

@app.route("/", methods=["POST"])
def receive_message():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return Response("EVENT_RECEIVED", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
