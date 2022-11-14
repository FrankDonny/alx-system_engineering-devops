#!/usr/bin/python3
"""gather data from api using this module and parse into csv"""
import csv
import requests
from sys import argv


def main():
    """main code to be run"""
    base1 = "https://jsonplaceholder.typicode.com/todos/"
    base2 = "https://jsonplaceholder.typicode.com/users/"
    response1 = requests.get(base1).json()
    response2 = requests.get(base2).json()

    with open("2.csv", "w") as file:
        writer = csv.writer(file)
        ls = []
        for dict_ in response1:
            for user in response2:
                if user['id'] == int(argv[1]):
                    ls.append(user['username'])
                    break
            if dict_['userId'] == int(argv[1]):
                tup = ('{}'.format(argv[1]), ls[0], dict_['completed'],
                       dict_['title'])
                writer.writerow(tup)


if __name__ == "__main__":
    main()
