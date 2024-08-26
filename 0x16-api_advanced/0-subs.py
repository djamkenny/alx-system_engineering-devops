#!/usr/bin/python3  

import requests  


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-app/0.1'}  

    try:  
        response = requests.get(url, headers=headers, allow_redirects=False)  
        if response.status_code == 200:
                data = response.json()  
                return data['data']['subscribers']  
        else:
            return 0  
    except Exception as e:  
        print(f"An error occurred: {e}")  
        return 0