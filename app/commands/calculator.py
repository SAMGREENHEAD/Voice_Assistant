# app/commands/calculator.py

def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return "Sorry, I couldn't calculate that."
