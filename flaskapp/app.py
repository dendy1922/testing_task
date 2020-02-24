from flask import Flask, jsonify
from utils import generate_prime_numb

app = Flask(__name__)


@app.route('/number', methods = ['GET'])
def number():
    return jsonify({'number':generate_prime_numb()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
