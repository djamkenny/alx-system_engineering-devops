# #!/usr/bin/python3
# """Function to query subscribers on a given Reddit subreddit."""
# import requests


# def number_of_subscribers(subreddit):
#     """Return the total number of subscribers on a given subreddit."""
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {
#         "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
#     }
#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 404:
#         return 0
#     results = response.json().get("data")
#     print(results)
#     return results.get("subscribers")


import requests  

def number_of_subscribers(subreddit):  
    url = f"https://www.reddit.com/r/{subreddit}/about.json"  
    headers = {'User-Agent': 'my-reddit-app/0.1'}  
    
    try:  
        response = requests.get(url, headers=headers, allow_redirects=False)  
        if response.status_code == 200:  
            data = response.json()  
            print(data['data']['subscribers'] )
            return data['data']['subscribers']  
        else:  
            return 0  
    except Exception as e:  
        print(f"An error occurred: {e}")  
        return 0
    

number_of_subscribers("Python")