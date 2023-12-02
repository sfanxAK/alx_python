import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    print(f"Number of argument{'s' if num_arguments != 1 else ''}: {num_arguments}", end='')

    if num_arguments > 0:
        print(", followed by:")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")
    else:
        print(".")

if __name__ == "__main__":
    print_arguments()



