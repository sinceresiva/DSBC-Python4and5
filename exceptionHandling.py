'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''
def divideByZero():
    try:
        x=5/0
    except ZeroDivisionError as e:
        print("You cant divide by zero {}".format(e.__class__))

divideByZero()