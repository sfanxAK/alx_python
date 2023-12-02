def safe_print_division(a, b):
    try:
        result = a / b
        print('Inside result: {:.1f}'.format(result))
    except ZeroDivisionError:
        result = None 
        print('Inside result: None')
    finally:
        if result is not None:
            print('{:d} / {:d} = {:.1f}'.format(a, b, result))
        else:
            print('{:d} / {:d} = None'.format(a, b))

# Example usage
a = int(input('Enter the numerator: '))
b = int(input('Enter the denominator: '))
safe_print_division(a, b)



