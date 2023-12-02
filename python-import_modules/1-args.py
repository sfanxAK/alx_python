argument = input()
arguments = argument.split()
number_of_arguments = len(arguments)

if number_of_arguments > 0:
    print(number_of_arguments,"arguments:")
    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")
else:
    print(number_of_arguments,"arguments.")

print("\nNumber of arguments:", number_of_arguments)




