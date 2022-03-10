# Author: Ty Brien
# Description: Part one of midterm

print("Name: Ty Brien")
Total = 0
keywords = ["gmeach18@ed.gov", "248.253.63.149", "Whiteland",
            "80.222.19.190", "Kayley", "dcassyqw@microsoft.com"]

with open("midterm-if.txt", "r") as midterm_file:
    for line in midterm_file.readlines():
        line_list = line.strip("\n").split(",")
        for keyword in keywords:
            if keyword in line_list:
                print(line)
                Total += int(line_list[0])

print(f"The total is: {Total}")