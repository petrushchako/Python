try:
    print (7/0)
except ArithmeticError as ae:
    print ('Caught an ArithmeticError')
except ZeroDivisionError as zde:
    print ('Caught a ZeroDivisionError')
else:
    print ('Success!')