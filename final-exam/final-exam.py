import argparse
import requests
import bs4
import socket

name = "Ty Brien"

def get_response(url):
    response = requests.get(url)
    return response


def parse_string(url):
    response = requests.get(url)
    secret_string = bs4.BeautifulSoup(response.text, "html.parser").find("h3").text
    regular_string = secret_string[4] + secret_string[6] + secret_string[8] + secret_string[10] + secret_string[12] + secret_string[13] + secret_string[16] + secret_string[18] + secret_string[20]
    return regular_string


def parse_header(url):
    response = requests.get(url)
    return response.headers["MATC-HEADER"]


def parse_json(url):
    response = requests.get(url).json()
    for x in response["Music And Books"]:
        if x["title"] == "The Shining":
            return x["publish_info"]["publisher"]


def socket_client(ip):
    for port in range(5000, 6000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            try:
                s.connect((ip, port))
                s.sendall(b"secret")
                return s.recv(1024).decode("utf-8")
            except Exception as e:
                pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", type=str, required=True)
    parser.add_argument("-f", "--function", type=int, required=True)
    args = parser.parse_args()

    url = f"http://{args.ipaddress}/q{args.function}"
    
    if args.function == 1:
        response = get_response(url).text
    elif args.function == 2:
        response = f"{parse_string(url)} {name}"
    elif args.function == 3:
        response = parse_header(url)
    elif args.function == 4:
        response = parse_json(url)
    elif args.function == 5:
        response = socket_client(args.ipaddress)
    else:
        response = "Unrecognized input for the --function argument."
    print(*[f"Name: {name}\n", f"{url}\n", f"ANSWER: {response}"])
