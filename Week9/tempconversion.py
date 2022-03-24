import c2f, f2c

if __name__== "__main__":
    user_temp = int(input("Please enter a temperature: "))
    user_format = input("Is the above temperature in Fahrenheit or Celsius? ")
    if user_format.lower() == "fahrenheit":
        print(f"{f2c.fahrenheit_to_celsius(user_temp)} Celsius")
    elif user_format.lower() == "celsius":
        print(f"{c2f.celsius_to_fahrenheit(user_temp)} Fahrenheit")
    else:
        print("Did not recognize temperature format. Please try again. ")