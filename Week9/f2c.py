# Ty Brien
#Temp converter f2c

def fahrenheit_to_celsius(x):
    return (x - 32) * (5/9)

if __name__ == "__main__":
    user_input = int(input("Please enter a Fahrenheit temp to convert to Celsius: "))
    print(fahrenheit_to_celsius(user_input))