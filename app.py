from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/login', methods=['PUT'])
def login():
    # リクエストボディからusernameとpasswordを取得
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # usernameとpasswordを結合しSHA1のチェックサムを計算
    if username and password:
        token = hashlib.sha1(f"{username}{password}".encode()).hexdigest()
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Missing username or password"}), 400

@app.route('/flag', methods=['PUT'])
def flag():
    # flagの値を取得し、レスポンスに返却
    data = request.get_json()
    flag = data.get("flag")
    if flag:
        return jsonify({"flag_received": flag})
    else:
        return jsonify({"error": "Missing flag"}), 400

if __name__ == '__main__':
    app.run()