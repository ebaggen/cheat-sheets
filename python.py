'''
DECORATORS 

Decorators are functions that take another function as an argument, enabling
consistent pre- and post-processing of a function
'''
def decorator(function):
    print('Decorator called')

    def wrapper(*args, **kwargs):
        # Pre-processing happens here
        print('Doing some stuff before calling the function')

        # Calling the function argument actually runs the function that is being deocorated
        function()

        # Post-processing happens here
        print('Doing some stuff after calling the function')

    return wrapper

# This is a decorator in use:
@decorator
def hello_world():
    print('Hello world!')

# output:
# >>> Doing some stuff before calling the function
# >>> Hello world!
# >>> Doing some stuff after calling the function