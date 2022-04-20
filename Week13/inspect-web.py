# Ty Brien
# Week 13 assignment 
import bs4

if __name__ == "__main__":
    with open("my_web_file.html", "r") as webfile:
        webdata = webfile.read()
    html = bs4.BeautifulSoup(webdata, features="html.parser")
    print(html.title.text)
    for link in html.findAll("a"):
        print(link.get("href"))
