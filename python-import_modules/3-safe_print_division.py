def safe_print_division(a, b):
    try:
        result = a / b
        print('Inside result: {:.2f}'.format(result))
    except ZeroDivisionError:
        result = None
        print('{:d} / {:d} = None'.format(a, b))
    finally:
        print('{:d} / {:d} = {:.2f}'.format(a, b, result))

            


# Example usage

a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
safe_print_division(a, b)
