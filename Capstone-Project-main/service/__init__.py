from flask import Flask, request, jsonify
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():

    app = Flask(__name__)

    talisman = Talisman(app)
    talisman.force_https = False

    CORS(app)

    # 🔽 TAMBAHKAN INI
    accounts = []

    @app.route("/accounts", methods=["POST"])
    def create_account():
        data = request.get_json()
        data["id"] = len(accounts) + 1
        accounts.append(data)
        return jsonify(data), 201

    return app