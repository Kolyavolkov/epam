from math import pi

def print_type(variable):
    """This function prints the type of supplied variable

    Args:
        variable (Any): variable to print type for
    """
    for var in variable:
        print(type(var))


def do_action(variable):
    """Does the action depending on variable's type. (hint: you can either use print function right here, 
    or return the result. For now it doesn't matter)
    Defined actions:
        int: square the number
        float: add π(pi) (from math.pi, don't forget the import~!) to it and print the result
        bool: inverse it (e.g if you have True, make it False) and print the result
        list: print elements in reversed order

    Args:
        variable (Any): variable to perform action on
    """
    for var in variable:
        if type(var) is int:
            print('square of ', var, 'is ', var**2 )
        if isinstance(var, float):
            print('sum of ', var, 'and π(pi) = ', var + pi)
        if isinstance(var, bool):
            print('Inversed', var, 'is ', not var)
        if isinstance(var, list):
            print(var[::-1])

variables = [ 42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]

print_type(variables)

do_action(variables)

# Please, for all elements in `variables` list print the following:
#  the type of variable using `print_type` function
#  and the action for variable using `do_action` function