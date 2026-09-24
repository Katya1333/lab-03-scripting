#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    '''Retrieve events from GitHub using requests (this is the variable, response).
    Since response is a JSON text string, pass it through json.loads to convert it to a dictionary (dict_response).
    Return the dictionary.'''
    response = requests.get(url).text
    dict_response = json.loads(response)
    return dict_response

def print_events(events, n=5):
    '''Print the first n events from the list of events.'''
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    events = retrieve_events(url)
    print(GHUSER)
    print(url)
    print_events(events)

if __name__ == "__main__":
    main()