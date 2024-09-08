from flask import Blueprint, request, jsonify

# import the alpha_functions function from the alpha module
from features.alpha.alpha import alpha_function1, alpha_function2, alpha_function3

# importing the beta functions from the beta module
from features.beta.beta import beta_function1, beta_function2, beta_function3

# importing the gamma functions from the gamma module
from features.gamma.gamma import gamma_function1, gamma_function2, gamma_function3

app = Blueprint("routes", __name__)


@app.route("/")
def hello_world():
    return {"response": " Hello, World!"}


@app.route("/features/alpha_function1", methods=["POST"])
def route_alpha_function1():
    print("\n In alpha_function1 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        alpha_function1_result = alpha_function1(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"alpha_function1_result": alpha_function1_result}), 200


@app.route("/features/alpha_function2", methods=["POST"])
def route_alpha_function2():
    print("\n In alpha_function2 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        alpha_function2_result = alpha_function2(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"alpha_function2_result": alpha_function2_result}), 200


@app.route("/features/alpha_function3", methods=["POST"])
def route_alpha_function3():
    print("\n In alpha_function1 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        alpha_function1_result = alpha_function3(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"alpha_function3_result": alpha_function1_result}), 200


@app.route("/features/beta_function1", methods=["POST"])
def route_beta_function1():
    """
    This endpoint loads Context from a knowledge graph
    :num1: prompt - Modified user prompt coming from the back-end preprocessing logic
    :num2: user_id Provide the user id to store user requests and responses

    :return: context
    """
    print("\n In beta_function1 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        # This is the returned context
        beta_function1_result = f"{num1} {num2}"
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify(
        {"beta_function1_result": beta_function1_result}
    ), 200


@app.route("/features/beta_function2", methods=["POST"])
def route_beta_function2():
    """
    This endpoint takes scraped data chunk about a single Attorney and tries to store it on a knowledge graph.

    :num1: Attorney data
    :num2: Context (data source, url, any other metadata)
    :return: The stored context
    """
    print("\n In beta_function2 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        beta_function2_result = "Successfully stored"
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"beta_function2_result": beta_function2_result}), 200


@app.route("/features/beta_function3", methods=["POST"])
def route_beta_function3():
    print("\n In beta_function3 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        beta_function3_result = beta_function3(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"beta_function3_result": beta_function3_result}), 200


@app.route("/features/gamma_function1", methods=["POST"])
def route_gamma_function1():
    print("\n In gamma_function1 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        gamma_function1_result = gamma_function1(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"gamma_function1_result": gamma_function1_result}), 200


@app.route("/features/gamma_function2", methods=["POST"])
def route_gamma_function2():
    print("\n In gamma_function2 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        gamma_function2_result = gamma_function2(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"gamma_function2_result": gamma_function2_result}), 200


@app.route("/features/gamma_function3", methods=["POST"])
def route_gamma_function3():
    print("\n In gamma_function3 route.")

    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing data"}), 400
    try:
        gamma_function3_result = gamma_function3(num1, num2)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"gamma_function3_result": gamma_function3_result}), 200
