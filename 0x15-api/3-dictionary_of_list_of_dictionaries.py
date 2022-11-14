#!/usr/bin/python3
"""gather all employee data using this module and parse into csv"""
import json
import requests


def main():
    """main code to be run"""
    base1 = "https://jsonplaceholder.typicode.com/todos/"
    base2 = "https://jsonplaceholder.typicode.com/users/"
    response1 = requests.get(base1).json()
    response2 = requests.get(base2).json()

    ls = []
    ids = []
    contain = {}
    for item in response2:
        ls.append(item['username'])
        ids.append(item['id'])

    i = 0
    dict_ = {}
    for num in ids:
        dict_list = []
        for di in response1:
            if di['userId'] == num:
                new_dict = {"task": di['title'],
                            "completed": di['completed'],
                            "username": ls[i]}
                dict_list.append(new_dict)
        contain[num] = dict_list
        dict_.update(contain)
        i += 1
    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        json.dump(dict_, file)


if __name__ == "__main__":
    main()
