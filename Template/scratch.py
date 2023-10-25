from itertools import *
from functools import *
from heapq import *
from collections import *
from math import *
from random import *
# from sortedcontainers import *


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print('Calling function:', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(message):
    print(message)

# greet('Hello, World!')
