# Python function that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperature_input = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = convert_to_celsius(temperature_input)
print(celsius_temp)
