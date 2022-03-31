# Author: Ty Brien
# Comments go here
import subprocess

if __name__ == "__main__":
    myProc = subprocess.run(["ps", "-axco", "command"], stdout=subprocess.PIPE)
    print(myProc.stdout)
    myProcString = myProc.stdout.decode("utf-8")
    myProcList = myProcString.split("\n")

    for proc in myProcList:
        print(proc)

    print(len(myProcList[1:]))