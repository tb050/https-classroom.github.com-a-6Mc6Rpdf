# Ty Brien  
# Week 14 assignment 

import requests
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON from a web address")
    parser.add_argument("--ipaddress", type=str, help="An Ip address to retrieve JSON")
    args = parser.parse_args()

    response = requests.get(f"http://ipinfo.io/{args.ipaddress}/json")
    json_dict = json.loads(response.text)
    for key, value in json_dict.items():
        print(f"{key} : {value}")