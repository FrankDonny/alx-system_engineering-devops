#!/usr/bin/python3
"""
module containing the request function
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    script that prints a message depending of the number of arguments.
    """
    response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after),
                            headers={'User-agent': 'Mozilla/5.0\
                                     (Windows NT 10.0; Win64; x64)\
                                     AppleWebKit/537.36 (KHTML, like Gecko)\
                                     Chrome/107.0.0.0 Safari/537.36'},
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    if after is None:
        return hot_list

    for i in response.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))

    after = response.json().get('data').get('after')
    recurse(subreddit, hot_list, after)
    return(hot_list)
