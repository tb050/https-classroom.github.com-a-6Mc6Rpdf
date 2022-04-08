#!/usr/bin/env python3
# Ty Brien
# Week 11 ArgParse Lab
import argparse
import sys

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="This is Ty's arguments.py script")
    parser.add_argument("-m", metavar="BASIC", help="Enter some text")
    parser.add_argument("-i", "--integer", metavar="[an integer]", dest="myInt", default=10, type=int, help="<Required> Enter a simple Integer")
    parser.add_argument("-d", "--float", metavar="[a Float]", dest="myFloat", default=10.5, type=float, help="Enter a simple float")
    parser.add_argument("-s", "--string", metavar="[a string]", dest="myString", type=str, default="Default string", help="Enter a simple string")
    parser.add_argument("-l", nargs="+", metavar="[strings]", dest="myList", type=str, default=["default", "list"], help="Enter a list of strings (space delimited)")
    parser.add_argument("-t", "--set-true", dest="toggle", default=False, action="store_true", help="Toggle from default False to True")
    parser.add_argument("-f", "--set-false", dest="toggle", default=True, action="store_false", help="Toggle from default False to True")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    

    if len(sys.argv) == 1:
        print(parser.print_help())
    else:
        print(f"{args.myInt}\n{args.myString}\n{args.myFloat}\n{args.myList}")