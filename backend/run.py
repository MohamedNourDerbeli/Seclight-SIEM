from flask import Flask, request

app = Flask(__name__)

def check_bruteforce(log_message: str) -> bool:
    # Simple keyword detection example
    return "Failed password" in log_message

@app.route("/api/logs", methods=["POST"])
def receive_logs():
    data = request.get_json()
    log_text = data.get("message") or data.get("event").get("original", "")
    if check_bruteforce(log_text):
        print(f"ALERT: Potential brute force detected: {log_text}")
        exit(1)
    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run(port=5000)
