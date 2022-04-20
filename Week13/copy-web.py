# Ty Brien
# Week 13 assignment
import requests

if __name__ == "__main__":
    response = requests.get("https://notpurple.com")
    if response.ok:
        with open("my_web_file.html", "w+") as webfile:
            webfile.write(response.text)
