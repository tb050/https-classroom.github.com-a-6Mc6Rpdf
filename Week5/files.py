#Ty B - showcase different ways to read the lines in a file
with open("/etc/passwd", "r") as passwdfile:
    print(len(passwdfile.read()))
    print("This len() counts number of character in the file.")
    print("Use this read function when you need the full contents of the file as a string.")


with open("/etc/passwd", "r") as passwdfile:
    print(len(passwdfile.readlines()))
    print("This len() counts number of lines in the file.")
    print("Use this read function when you want to iterate or inspect individual lines from a file.")


    with open("/etc/passwd", "r") as passwdfile:
        contents = ""
        while True:
            line = passwdfile.readline()
            if not line:
                break
            contents = contents + line
        print(len(contents))
        print("Use this read function when you want to iterate or inspect only specific lines within a file.")