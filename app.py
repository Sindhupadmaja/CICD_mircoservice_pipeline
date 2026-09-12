from flask import Flask, jsonify, request
import os

app = Flask(__name__)
orders = []

@app.get("/health")
def health():
    return jsonify(status="healthy", version=os.getenv("APP_VERSION", "dev"))

@app.get("/orders")
def list_orders():
    return jsonify(orders)

@app.post("/orders")
def create_order():
    payload = request.get_json(silent=True) or {}
    if "item" not in payload:
        return jsonify(error="item is required"), 400
    order = {"id": len(orders) + 1, "item": payload["item"]}
    orders.append(order)
    return jsonify(order), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
