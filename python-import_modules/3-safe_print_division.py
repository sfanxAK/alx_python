def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Inside result: {:d}'.format(result))
    finally:
        if result != 0:
          print('{:d} / {:d} = {:.2f}'.format(a, b, result))
        else:
          print('{:d} / {:d} = {:.2f}'.format(a, b, result))



