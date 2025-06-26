# Define decorator_one: logs before and after the function call
def decorator_one(func):
    def wrapper(self, a, b):
        print("[decorator_one] Before:", func.__name__)
        result = func(self, a, b)
        print("[decorator_one] After :", func.__name__)
        return result
    return wrapper

# Define decorator_two: logs around the subtraction
def decorator_two(func):
    def wrapper(self, a, b):
        print("[decorator_two] Starting:", func.__name__)
        result = func(self, a, b)
        print("[decorator_two] Finished:", func.__name__)
        return result
    return wrapper

class Subtractor:
    """
    Class for subtracting two numbers with decorated method.
    """

    @decorator_one
    @decorator_two
    def subtract(self, a, b):
        """
        Subtract b from a and return the result.
        Decorators wrap this method: decorator_two is innermost.
        """
        print(f"  -> Inside subtract: {a} - {b}")
        return a - b

# Demonstrate the behavior
if __name__ == "__main__":
    obj = Subtractor()
    print("Calling subtract(10, 3):")
    output = obj.subtract(10, 3)
    print("Result:", output)
