import unittest  
from rule_engine import create_rule, evaluate_rule, Node  

class TestRuleEngine(unittest.TestCase):  

    def test_create_rule(self):  
        rule_string = "age > 30 AND department = 'Sales'"  
        ast = create_rule(rule_string)  
        self.assertEqual(ast.node_type, "operator")  
        self.assertEqual(ast.left.node_type, "operator")  
        self.assertEqual(ast.left.value, "GT")  
        self.assertEqual(ast.left.left.value[0], "age")  
        self.assertEqual(ast.left.right, 30)  # Assuming parse_value returns integer 30  
        self.assertEqual(ast.right.node_type, "operator")  
        self.assertEqual(ast.right.value, "EQ")  
        self.assertEqual(ast.right.left.value[0], "department")  
        self.assertEqual(ast.right.right, "Sales")

    def test_evaluate_rule(self):  
        rule_string = "age > 30 AND department = 'Sales'"  
        ast = create_rule(rule_string)  
        data = {"age": 35, "department": "Sales"}  
        result = evaluate_rule(ast, data)  
        self.assertTrue(result)  

        data = {"age": 25, "department": "Sales"}  
        result = evaluate_rule(ast, data)  
        self.assertFalse(result)  

if __name__ == '__main__':  
    unittest.main()