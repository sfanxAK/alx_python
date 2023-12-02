if __name__ == "__main__":
  import sys

  def print_arguments():
      # Get the command-line arguments
      arguments = sys.argv[1:]

      # Calculate the number of arguments
      num_arguments = len(arguments)

      # Print the number of arguments and appropriate pluralization
      print(f"Number of argument{'s' if num_arguments != 1 else ''}: {num_arguments}", end='')

      if num_arguments > 0:
          print(", followed by:")
          # Print each argument with its position
          for i, arg in enumerate(arguments, start=1):
              print(f"{i}: {arg}")
      else:
          print(".")

  if __name__ == "__main__":
      print_arguments()



