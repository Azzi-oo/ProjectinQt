
def decorator(func_to_be_called):

    def wrapper(*args, **kwargs):
        print('Some text before calling func')
        func_to_be_called(*args, **kwargs)
        print('Some text after calling func')
    return wrapper

@decorator
def print_func(text):
    print('Your text is:', text)

print_func('Hello')
