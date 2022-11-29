#!/usr/bin/python3
'''return number of subs with reddit api'''
import requests


def number_of_subscribers(subreddit):
    '''Gets number of reddit subscribers'''
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/107.0.0.0 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
