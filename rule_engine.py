import operator  

class Node:  
    def __init__(self, node_type, value=None, left=None, right=None):  
        self.node_type = node_type  
        self.value = value  
        self.left = left  
        self.right = right  

    def to_dict(self):  
        return {  
            "type": self.node_type,  
            "value": self.value,  
            "left": self.left.to_dict() if self.left else None,  
            "right": self.right.to_dict() if self.right else None  
        }  

    @staticmethod  
    def from_dict(data):  
        if data is None:  
            return None  
        node = Node(data['type'], data['value'])  
        node.left = Node.from_dict(data['left'])  
        node.right = Node.from_dict(data['right'])  
        return node  

def create_rule(rule_string):  
    # Simple parser. This should handle more cases in a real-world scenario.  
    if "AND" in rule_string:  
        left, right = rule_string.split(" AND ")  
        return Node("operator", "AND", create_condition(left), create_condition(right))  
    else:  
        return create_condition(rule_string) 

def create_condition(condition_string):  
    # This function expects strings of the form "field op value"  
    mapping = {  
        ">": "GT",  
        "<": "LT",  
        "=": "EQ"  
    }  
    for symbol, op in mapping.items():  
        if symbol in condition_string:  
            left, right = condition_string.split(symbol)  
            return Node("operator", op, Node("operand", (left.strip(), op, parse_value(right.strip()))))  
    return None

def parse_value(val):  
    try:  
        return eval(val)  # Be cautious using eval, it's dangerous with untrusted input  
    except:  
        return str(val)  # Treat as a string if there's an issue  

def evaluate_rule(ast, data):  
    return evaluate_node(ast, data)  

def evaluate_node(node, data):  
    if node.node_type == "operand":  
        left, op_str, right = node.value  
        
        op = {  
            'GT': operator.gt,  
            'LT': operator.lt,  
            'EQ': operator.eq,  
        }.get(op_str)  

        if op is None:  
            return False  

        result = op(data.get(left), right) if left in data else False  
        return result  

    elif node.node_type == "operator":  
        left_result = evaluate_node(node.left, data)  
        right_result = evaluate_node(node.right, data)  

        if node.value == 'AND':  
            return left_result and right_result  
        elif node.value == 'OR':  
            return left_result or right_result  
        
    return False