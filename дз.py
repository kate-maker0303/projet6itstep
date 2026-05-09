def calculator_decorator(func):
    def wrapper(expression):
        try:

            if not isinstance(expression, str):
                return "Error: expression must be a string"

            allowed = "0123456789+-*/(). "

            for char in expression:
                if char not in allowed:
                    return f"Error: invalid character '{char}'"

            # Перевірка порожнього вводу
            if expression.strip() == "":
                return "Error: empty expression"

            # Виконання обчислення
            result = func(expression)

            return f"Result: {result}"

        except ZeroDivisionError:
            return "Error: division by zero"

        except SyntaxError:
            return "Error: invalid syntax"

        except Exception as e:
            return f"Unknown error: {e}"

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)



print(calculate("2 + 3 * 4"))
print(calculate("(10 - 2) / 4"))
print(calculate("10 / 0"))
print(calculate("2 +"))
print(calculate("2 + abc"))
print(calculate(""))