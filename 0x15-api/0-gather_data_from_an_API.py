#!/usr/bin/python3
"""gather data from api using this module"""
import requests
from sys import argv


def main():
    """main code to be run"""
    base1 = "https://jsonplaceholder.typicode.com/todos/"
    base2 = "https://jsonplaceholder.typicode.com/users/"
    response1 = requests.get(base1).json()
    response2 = requests.get(base2).json()

    ct = 0
    true_ = 0
    ls = []
    titles = ""
    for dict_ in response1:
        for user in response2:
            if user['id'] == int(argv[1]):
                ls.append(user['name'])
                break
        if dict_['userId'] == int(argv[1]):
            ct += 1
            if dict_['completed'] == bool('True'):
                true_ += 1
                titles = titles + '\t ' + dict_['title'] + '\n'

    print("Employee {} is done with tasks({}/{}):\n{}".
          format(ls[0], true_, ct, titles))


if __name__ == "__main__":
    main()
