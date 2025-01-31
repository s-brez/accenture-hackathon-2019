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


#------------------------ INDEX ENDPOINTS ------------------------------
@app.route('/')
def index():
    return "API for the DeFiBank app"


#------------------------ USERS ENDPOINTS ------------------------------        
# Use this json to test the user endpoints using Postman
#   {
#         "user_id": "U001",
#         "first_name": "Nhi",
#         "last_name": "Huynh",
#         "email": "nhi.huynh@gmail.com",
#         "password_hash": "password", 
#         "account_id": "A001"
#     }

# Test with a second user
# {
#     "user_id": "U002",
#     "first_name": "Sam",
#     "last_name": "Breznika",
#     "email": "sam.brez@gmail.com",
#     "password_hash": "password", 
#     "account_id": "A002",
#     "account_type": "standard_user"
# }
# 

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


#------------------------ ACCOUNTS ENDPOINTS ------------------------------    
# Use this json to test the account endpoints using Postman
# {
#     "account_id": "A001",
#     "duration": "365",
#     "initial_deposit": "1000",
#     "current_balance": "1000",
#     "current_interest_rate": "10", 
#     "avg_interest_rate": "8.5",
#     "interest_paid_to_date": "0",
#     "hedge_id": "H001",
#     "loan_id": "L001",
#     "user_id": "U001",
#     "account_balance_history": "none"
#     "net_interest_history": "none"
# }
# 

@app.route('/accounts', methods=["GET"])
def get_accounts():
    return jsonify(account_controller.get_entities())

@app.route('/accounts/<account_id>', methods=["GET"])
def get_account_by_id(account_id):
    return jsonify(account_controller.get_entity(account_id))

@app.route('/accounts', methods=["POST"])
def create_account():
    return jsonify(account_controller.create_entity(request.json))

@app.route('/accounts/<account_id>', methods = ["PUT"])
def update_account(account_id):
    return jsonify(account_controller.update_entity(request.json))

@app.route('/accounts/<account_id>', methods = ["DELETE"])
def delete_account(account_id):
    return jsonify(account_controller.delete_entity(account_id))




#------------------------ LOANS ENDPOINTS ------------------------------    
# Use this json to test the account endpoints using Postman
#   "total" is a reserved key word so change it to "total_loan"
# {
#     "loan_id": "L001",
#     "asset": "Bitcoin",
#     "total_loan": "1000",
#     "current_price": "7000",
#     "current_interest_rate": "10", 
#     "close_date": "2019-11-27 14:09:01.772253",
#     "active": "true",
#     "account_id": "A001",
#     "interest_rate_history": ""
# }
# 

@app.route('/loans', methods=["GET"])
def get_loans():
    return jsonify(loan_controller.get_entities())

@app.route('/loans/<loan_id>', methods=["GET"])
def get_loan_by_id(loan_id):
    return jsonify(loan_controller.get_entity(loan_id))

@app.route('/loans', methods=["POST"])
def create_loan():
    return jsonify(loan_controller.create_entity(request.json))

@app.route('/loans/<loan_id>', methods = ["PUT"])
def update_loan(loan_id):
    return jsonify(loan_controller.update_entity(request.json))

@app.route('/loans/<loan_id>', methods = ["DELETE"])
def delete_loan(loan_id):
    return jsonify(loan_controller.delete_entity(loan_id))



#------------------------ HEDGES ENDPOINTS ------------------------------    
# Use this json to test the account endpoints using Postman
#   "value" is a reserved key word so change it to "hedge_value"
# {
#     "hedge_id": "H001",
#     "asset": "Bitcoin",
#     "value": "1000",
#     "default_instrument": "XBTUSD",
#     "current_instrument": "XBTUSD", 
#     "close_date": "2019-11-27 14:09:01.772253",
#     "rollover_date": "2019-12-27 14:09:01.772253",
#     "active": "true",
#     "account_id": "A001",
#     "funding_rate_history": "none"
# }
# 

@app.route('/hedges', methods=["GET"])
def get_hedges():
    return jsonify(hedge_controller.get_entities())

@app.route('/hedges/<hedge_id>', methods=["GET"])
def get_hedge_by_id(hedge_id):
    return jsonify(hedge_controller.get_entity(hedge_id))

@app.route('/hedges', methods=["POST"])
def create_hedge():
    return jsonify(hedge_controller.create_entity(request.json))

@app.route('/hedges/<hedge_id>', methods = ["PUT"])
def update_hedge(hedge_id):
    return jsonify(hedge_controller.update_entity(request.json))

@app.route('/hedges/<hedge_id>', methods = ["DELETE"])
def delete_hedge(hedge_id):
    return jsonify(hedge_controller.delete_entity(hedge_id))




#------------------------ BALANCES ENDPOINTS ------------------------------    
# Use this json to test the account endpoints using Postman
#   "value" is a reserved key word so change it to "balances_value"
# {
#     "timestamp": "2019-11-27 14:09:01.772253",
#     "account_id": "A001",
#     "balance": "1000"
# }
# 

@app.route('/balances', methods=["GET"])
def get_balances():
    return jsonify(balance_controller.get_entities())

@app.route('/balances/<account_id>', methods=["GET"])
def get_balances_by_id(account_id):
    return jsonify(balance_controller.query_entities(account_id))

@app.route('/balances', methods=["POST"])
def create_balances():
    return jsonify(balance_controller.create_entity(request.json))

@app.route('/balances/<account_id>', methods=["DELETE"])
def delete_balances_by_id(account_id):
    return jsonify(balance_controller.delete_selective_entities(account_id))

@app.route('/balances', methods=["DELETE"])
def delete_balances():
    return jsonify(balance_controller.delete_entities())



#------------------------ NET INTERESTS ENDPOINTS ------------------------------    
# Use this json to test the interests endpoints using Postman
# {
#     "timestamp": "2019-11-27 14:09:01.772253",
#     "account_id": "A001",
#     "net_interest": "10"
# }
# 

@app.route('/net_interests', methods=["GET"])
def get_net_interests():
    return jsonify(loan_interest_controller.get_entities())

@app.route('/net_interests/<account_id>', methods=["GET"])
def get_net_interests_by_id(account_id):
    return jsonify(loan_interest_controller.query_entities(account_id))

@app.route('/net_interests', methods=["POST"])
def create_net_interest():
    return jsonify(loan_interest_controller.create_entity(request.json))

@app.route('/net_interests/<account_id>', methods=["DELETE"])
def delete_net_interests_by_id(account_id):
    return jsonify(loan_interest_controller.delete_selective_entities(account_id))

@app.route('/net_interests', methods=["DELETE"])
def delete_net_interests():
    return jsonify(loan_interest_controller.delete_entities())



#------------------------ LOAN INTERESTS ENDPOINTS ------------------------------    
# Use this json to test the interests endpoints using Postman
# {
#     "timestamp": "2019-11-27 14:09:01.772253",
#     "account_id": "A001",
#     "loan_interest": "1000"
# }
# 

@app.route('/loan_interests', methods=["GET"])
def get_loan_interests():
    return jsonify(loan_interest_controller.get_entities())

@app.route('/loan_interests/<account_id>', methods=["GET"])
def get_loan_interests_by_id(account_id):
    return jsonify(loan_interest_controller.query_entities(account_id))

@app.route('/loan_interests', methods=["POST"])
def create_loan_interest():
    return jsonify(loan_interest_controller.create_entity(request.json))

@app.route('/loan_interests/<account_id>', methods=["DELETE"])
def delete_loan_interests_by_id(account_id):
    return jsonify(loan_interest_controller.delete_selective_entities(account_id))

@app.route('/loan_interests', methods=["DELETE"])
def delete_loan_interests():
    return jsonify(loan_interest_controller.delete_entities())



#------------------------ FUNDING RATE ENDPOINTS ------------------------------    
# Use this json to test the funding_rates endpoints using Postman
# {
#     "timestamp": "2019-11-27 14:09:01.772253",
#     "account_id": "A001",
#     "funding_rate": "1000"
# }
# 

@app.route('/funding_rates', methods=["GET"])
def get_funding_rates():
    return jsonify(funding_rate_controller.get_entities())

@app.route('/funding_rates/<account_id>', methods=["GET"])
def get_funding_rates_by_id(account_id):
    return jsonify(funding_rate_controller.query_entities(account_id))

@app.route('/funding_rates', methods=["POST"])
def create_funding_rate():
    return jsonify(funding_rate_controller.create_entity(request.json))

@app.route('/funding_rates/<account_id>', methods=["DELETE"])
def delete_funding_rates_by_id(account_id):
    return jsonify(funding_rate_controller.delete_selective_entities(account_id))

@app.route('/funding_rates', methods=["DELETE"])
def delete_funding_rates():
    return jsonify(funding_rate_controller.delete_entities())



#--------------------------- MAIN --------------------------------

if __name__ == '__main__':
    app.run()