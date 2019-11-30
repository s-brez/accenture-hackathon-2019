from flask import Flask, jsonify, request

from entity_controller import EntityController

app = Flask(__name__)

# Create controllers to control each entity
user_controller = EntityController("Users", "user_id", "last_name")
account_controller = EntityController("Accounts", "account_id", "user_id")
loan_controller = EntityController("Loans", "loan_id")
hedge_controller = EntityController("Hedges", "hedge_id")

# A controller to the balance table
balance_controller = EntityController("Balances", "timestamp", "account_id")

# A controller to the net interests of the account
net_interest_controller = EntityController("Net_interests", "timestamp", "account_id")

# A controller to the loan interests of the account
loan_interest_controller = EntityController("Loan_interests", "timestamp", "account_id")

# A controller to the funding rates of the account
funding_rate_controller = EntityController("Funding_rates", "timestamp", "account_id")

@app.route('/')
def index():
    return "API for the DeFiBank app"

@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(user_controller.get_entities())

@app.route('/users/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    return jsonify(user_controller.get_entity(user_id))

@app.route('/users', methods=["POST"])
def create_user():
    return jsonify(user_controller.create_entity(request.json))

@app.route('/users/<user_id>', methods = ["PUT"])
def update_user(user_id):
    return jsonify(user_controller.update_entity(request.json))

@app.route('/users/<user_id>', methods = ["DELETE"])
def delete_user(user_id):
    return jsonify(user_controller.delete_entity(user_id))