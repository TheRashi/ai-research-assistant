def calculator(expression):
    try:
        return eval(expression)
    except:
        return"Invalid Expression"