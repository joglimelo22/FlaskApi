from flask import Flask, jsonify

from pages.users import users_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint)

app.run(port=3000, debug=True)