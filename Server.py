from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        print(request.json)
        return jsonify(request.json)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
