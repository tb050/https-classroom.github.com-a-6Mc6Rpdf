# Author: Ty Brien
# Description: Midterm pt 2
print("Name: Ty Brien")

password_database = {"Username": "dnedry", "Password": "please"}
command_database = {"reboot": "OK. I will reboot all park systems.",
                    "shutdown": "OK. I will shut down all park systems.",
                    "done": "I hate all this hacker stuff."}

white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0 and counter < 3:
    input_user = input("Username: ")
    input_password = input("Password: ")

    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object = 1
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        command = input(f"Please enter a command {list(command_database.keys())}:")
        print(command_database.get(command, "The Lysine Contingency has been put into effect."))
    else:
        counter += 1
        if counter == 3:
            print(f"You didn't say the magic word\n" * 25)
        else:
            print(f"You didn't say the magic word. {counter}")