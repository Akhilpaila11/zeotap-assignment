from flask import Flask, request, jsonify  
from rule_engine import create_rule, evaluate_rule, Node  

# Create the Flask application instance  
app = Flask(__name__)  

@app.route('/create_rule', methods=['GET','POST'])  
def create_rule_api():  
    rule_string = request.json.get('rule_string')  
    try:  
        ast = create_rule(rule_string)  
        if ast:  
            return jsonify({"message": "Rule created!", "ast": ast.to_dict()}), 201  
        else:  
            return jsonify({"error": "Invalid rule string."}), 400  
    except Exception as e:  
        return jsonify({"error": str(e)}), 400  


@app.route('/evaluate_rule', methods=['GET','POST'])  
def evaluate_rule_api():  
    rule_ast = request.json.get('ast')  
    data = request.json.get('data')  
    try:  
        ast_tree = Node.from_dict(rule_ast)  
        result = evaluate_rule(ast_tree, data)  
        return jsonify({"result": result}), 200  
    except Exception as e:  
        return jsonify({"error": str(e)}), 400  


if __name__ == '__main__':  
    app.run(debug=True)
