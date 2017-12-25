import collections, math, ast, random, string, functools, itertools


# TYPE CHECKER

is_numeric = lambda argument: isinstance(argument, int) or isinstance(argument, float)

# VECTORIZER

def vecmonad(arg, monad, cond):
    return monad(arg) if cond(arg) else [vecmonad(x, monad, cond) for x in arg]

def vecdyad(arg1, arg2, dyad, cond1, cond2):
    if cond1(arg1):
        if cond2(arg2):
            return dyad(arg1, arg2)
        else:
            return [vecdyad(arg1, x, dyad, cond1, cond2) for x in arg2]
    else:
        return [vecdyad(x, arg2, dyad, cond1, cond2) for x in arg1]

# BUILT-INS


add = lambda a, b: vecdyad(a, b, (lambda x, y: x + y), is_numeric, is_numeric)
concatenate = lambda a, b: a + b
subtract = lambda a, b: vecdyad(a, b, (lambda x, y: x - y), is_numeric, is_numeric)

def bagwise_subtraction(a, b):
    acopy = list(a)
    for elem in b:
        if elem in acopy:
            acopy.remove(elem)
    return ''.join(acopy) if isinstance(a, str) else acopy

multiply = lambda a, b: vecdyad(a, b, (lambda x, y: x * y), is_numeric, is_numeric)
divide = lambda a, b: vecdyad(a, b, (lambda x, y: x / y), is_numeric, is_numeric)
integer_divide = lambda a, b: vecdyad(a, b, (lambda x, y: x // y), is_numeric, is_numeric)
power = lambda a, b: vecdyad(a, b, (lambda x, y: x ** y), is_numeric, is_numeric)
root = lambda a, b: 1 if b == 0 else vecdyad(a, b, (lambda x, y: x ** (1 / y)), is_numeric, is_numeric)
