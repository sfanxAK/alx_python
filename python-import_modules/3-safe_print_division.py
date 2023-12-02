# Write a function that divides 2 integers and prints the result.
a = int()
b = int()
def safe_print_division(a, b):
  result = a / b

result = safe_print_division(a, b)
if result == 0:
  result = 'None'
  print('Inside result: {:d}'.format(result))
  print('{:d} / {:d} = {:d}'.format(a, b, result))
elif result != 0:
  print('Inside result: {:d}'.format(result))
  print('{:d} / {:d} = {:d}'.format(a, b, result))





