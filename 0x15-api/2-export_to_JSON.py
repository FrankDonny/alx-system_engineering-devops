#!/usr/bin/python3
"""gather data from api using this module and parse into csv"""
import json
import requests
from sys import argv


def main():
    """main code to be run"""
    base1 = "https://jsonplaceholder.typicode.com/todos/"
    base2 = "https://jsonplaceholder.typicode.com/users/"
    response1 = requests.get(base1).json()
    response2 = requests.get(base2).json()

    ls = []
    dict_list = []
    contain = {}
    for item in response2:
        if item['id'] == int(argv[1]):
            ls.append(item['username'])
    for dict_ in response1:
        if dict_['userId'] == int(argv[1]):
            new_dict = {"task": dict_['title'], "completed": dict_['completed'], "username": ls[0]}
            dict_list.append(new_dict)
    contain[argv[1]] = dict_list
    with open(argv[1] + '.json', 'w', encoding="utf-8") as file:
        json.dump(contain, file)


if __name__ == "__main__":
    main()