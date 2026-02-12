# Temperature Conversion Program

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15


# Taking user input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

if unit == "C":
    f = celsius_to_fahrenheit(temperature)
    k = celsius_to_kelvin(temperature)
    print(f"\nTemperature in Fahrenheit: {f:.2f} °F")
    print(f"Temperature in Kelvin: {k:.2f} K")

elif unit == "F":
    c = fahrenheit_to_celsius(temperature)
    k = celsius_to_kelvin(c)
    print(f"\nTemperature in Celsius: {c:.2f} °C")
    print(f"Temperature in Kelvin: {k:.2f} K")

elif unit == "K":
    c = kelvin_to_celsius(temperature)
    f = celsius_to_fahrenheit(c)
    print(f"\nTemperature in Celsius: {c:.2f} °C")
    print(f"Temperature in Fahrenheit: {f:.2f} °F")

else:
    print("Invalid unit entered. Please use C, F, or K.")
