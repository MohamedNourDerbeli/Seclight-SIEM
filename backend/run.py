from flask import Flask, jsonify, request
import logging
import json

logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

def check_bruteforce(log_message: str) -> bool:
    # Simple keyword detection example
    return "Failed password" in log_message

@app.route("/api/logs", methods=["POST"])
def receive_logs():
    log_data = request.json
    print("Received log data:", log_data)  # Dev use only
    logging.info(json.dumps(log_data))     # Structured logging
    return jsonify({"status": "received"})

# Add this health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint for Docker Compose.
    Returns a simple JSON response to indicate the service is running.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
