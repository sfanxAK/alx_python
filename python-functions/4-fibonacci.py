# Function that takes a number n as input and returns a list of the first n Fibonacci numbers.
def fibonacci_sequence(n):
    fibunacci = [0, 1]
    while len(fibunacci) < n:
            next_numb = fibunacci[-1] + fibunacci[-2]
            fibunacci = fibunacci + [next_numb]
    return fibunacci[:n]
