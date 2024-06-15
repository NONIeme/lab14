def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a or b) and not (a and b)

def greet(boolean_value):
    return "Hello, World!" if boolean_value else "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(boolean_list):
    return boolean_list.count(True)

def parity(integer):
    return bin(integer).count('1') % 2 == 0

def majority_vote(a, b, c):
    return (a + b + c) > 1

def switch(boolean_value):
    return not boolean_value

def ternary_check(condition, result_if_true, result_if_false):
    return result_if_true if condition else result_if_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(boolean_list):
    return [value for value in boolean_list if value]

def multiplexer(a, b, c, integer):
    if a:
        return integer * 2
    elif b:
        return integer * 3
    elif c:
        return integer - 5
    else:
        return integer
