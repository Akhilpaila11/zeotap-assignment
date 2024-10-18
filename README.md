# Rule Engine with AST

## Overview
This project implements a rule engine using an Abstract Syntax Tree (AST) to evaluate rules on user data.

## Requirements
- Python 3.8+

## Setup
1. Clone the repository.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate  # On Windows
   ```
3. Run the test cases:
   ```bash
   python test_rule_engine.py
   ```

## Example
You can define rules like:
```python
rule1 = create_rule("age > 30 and department == 'Sales'")
```

Evaluate the rule against data:
```python
data = {"age": 32, "department": "Sales"}
evaluate_rule(rule1, data)  # Output: True
```
