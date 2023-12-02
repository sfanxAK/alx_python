import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    

    if num_arguments > 0:
        print(num_arguments,"argument: ")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")
    else:
      print(num_arguments,"argument.")
        

if __name__ == "__main__":
    print_arguments()



