# Example 1: Handling multiple exceptions with separate blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 2: Handling exceptions with a single except block
try:
    result = 10 / 'a'
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")

# Example 3: Handling specific exceptions with different blocks
try:
    result = 10 / 'a'
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 4: Using else block with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("No error occurred")

# Example 5: Using finally block with try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
finally:
    print("Finally block executed")

# Example 6: Using finally block without except
try:
    result = 10 / 2
finally:
    print("Finally block executed")

# Example 7: Handling exceptions with custom error message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 8: Raising an exception with custom error message
try:
    raise ValueError("Custom error message")
except ValueError as e:
    print(f"Error: {e}")

# Example 9: Raising an exception without arguments
try:
    raise ValueError
except ValueError:
    print("Error: ValueError raised")

# Example 10: Catching exception instance
try:
    result = 10 / 0
except Exception as e:
    print("Error:", e.__class__.__name__)

# Example 11: Handling exceptions in a loop
for i in range(5):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
    except Exception as e:
        print("Error:", e)

# Example 12: Using assert statement
x = 10
try:
    assert x == 5, "x should be 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

# Example 13: Nested try-except blocks
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner Error: Division by zero occurred")
except Exception as e:
    print("Outer Error:", e)

# Example 14: Accessing traceback information
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()

# Example 15: Using specific exceptions with else block
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input")
else:
    print("Square of the number:", result ** 2)

# Example 16: Catching exception in a function
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero occurred"

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# Example 17: Using custom exception classes
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print(f"CustomError: {e}")

# Example 18: Re-raising an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
    raise

# Example 19: Handling exceptions with context managers
with open('nonexistent_file.txt', 'r') as file:
    data = file.read()

# Example 20: Using contextlib.suppress to ignore exceptions
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('nonexistent_file.txt', 'r') as file:
        data = file.read()

# Example 21: Handling exceptions with except clause only
try:
    result = 10 / 0
except:
    print("Error occurred, but not handled specifically")

# Example 22: Handling exceptions with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 23: Using multiple except blocks with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 24: Handling exceptions with multiple except clauses
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Error: Division by zero or invalid type occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 25: Using except clause without specifying exception names
try:
    result = 10 / 0
except:
    print("An error occurred")

# Example 26: Using except clause with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")

# Example 27: Using except clause with multiple specific exception names
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Error: Division by zero or invalid type occurred")

# Example 28: Using except clause with generic exception name
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

# Example 29: Using except clause with specific and generic exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 30: Handling multiple specific exceptions with separate blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 31: Using else block with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("No error occurred")

# Example 32: Using finally block with try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
finally:
    print("Finally block executed")

# Example 33: Using finally block without except
try:
    result = 10 / 2
finally:
    print("Finally block executed")

# Example 34: Handling exceptions with custom error message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 35: Raising an exception with custom error message
try:
    raise ValueError("Custom error message")
except ValueError as e:
    print(f"Error: {e}")

# Example 36: Raising an exception without arguments
try:
    raise ValueError
except ValueError:
    print("Error: ValueError raised")

# Example 37: Catching exception instance
try:
    result = 10 / 0
except Exception as e:
    print("Error:", e.__class__.__name__)

# Example 38: Handling exceptions in a loop
for i in range(5):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
    except Exception as e:
        print("Error:", e)

# Example 39: Using assert statement
x = 10
try:
    assert x == 5, "x should be 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

# Example 40: Nested try-except blocks
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner Error: Division by zero occurred")
except Exception as e:
    print("Outer Error:", e)

# Example 41: Accessing traceback information
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()

# Example 42: Using specific exceptions with else block
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input")
else:
    print("Square of the number:", result ** 2)

# Example 43: Catching exception in a function
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero occurred"

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# Example 44: Using custom exception classes
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print(f"CustomError: {e}")

# Example 45: Re-raising an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
    raise

# Example 46: Handling exceptions with context managers
with open('nonexistent_file.txt', 'r') as file:
    data = file.read()

# Example 47: Using contextlib.suppress to ignore exceptions
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('nonexistent_file.txt', 'r') as file:
        data = file.read()

# Example 48: Handling exceptions with except clause only
try:
    result = 10 / 0
except:
    print("Error occurred, but not handled specifically")
