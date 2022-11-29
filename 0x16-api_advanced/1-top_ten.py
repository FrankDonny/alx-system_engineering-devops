#!/usr/bin/python3
'''module to print titles of first ten hot posts'''
import requests


def top_ten(subreddit):
    '''top ten function'''
    url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0\
               Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print(None)
        return

    for i in range(10):
        item = response.json().get('data').get("children")[i]
        print(item.get('data').get('title'))
