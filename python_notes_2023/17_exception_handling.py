# # Example 1
# try:
#     userData=int(input("Enter a number:"))
#     print(f"Entered number is:{userData}")
# except ValueError:
#     print("Please Enter Integer ONLY")


# # Example 2
# try:
#     userData=int(input("Enter a number:"))
# except ValueError:
#     print("Please Enter Integer ONLY")
# else:
#     print(f"Entered number is:{userData}")


# # Example 3
# # break keyword is used in this condition as if user enter the desired value it will break out of loop but if there is no break statement then loop will run for ever.asking the user to enter the value
# while True:
#     try:
#         userData=int(input("Enter a number:"))
#     except ValueError:
#         print("Please Enter Integer ONLY")
#     else:
#        break

# print(f"Entered number is:{userData}")


# # Example 4
# def get_int():
#     while True:
#         try:
#             userData=int(input("Enter a number:"))  
#         except ValueError:
#             print("Please Enter Integer ONLY")
#         else:
#             break
#     return print(f"Entered number is:{userData}")

# get_int()


# Example 5
def get_int():
    while True:
        try:
            return int(input("Enter a number:"))  
        except:
            pass
        else:
            break
   
userData=get_int()
print(f"Entered number is:{userData}")


# Example 6
num=int(input("enter num:"))
dnum=int(input("enter dnum:"))
try:
    ans=num/dnum
    print(int(ans))
except ZeroDivisionError:
    print("Division by zero not possible")

# Example 7
# The raise keyword is used to explicitly raise an exception in Python. It allows you to generate custom exceptions or handle exceptional situations in your code. You can specify the type of exception to raise and an optional error message
def calculate_square_root(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return num ** 0.5

try:
    result = calculate_square_root(-4)
    print(result)
except ValueError as err:
    print(err)






"""List of Exception/Errors

Exception	Cause of Error
AssertionError	Raised when an assert statement fails.
AttributeError	Raised when attribute assignment or reference fails.
EOFError	Raised when the input() function hits end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raise when a generator's close() method is called.
ImportError	Raised when the imported module is not found.
IndexError	Raised when the index of a sequence is out of range.
KeyError	Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError	Raised when an operation runs out of memory.
NameError	Raised when a variable is not found in local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	Raised when system operation causes system related error.
OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	Raised when an error does not fall under any other category.
StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	Raised when interpreter detects internal error.
SystemExit	Raised by sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero."""