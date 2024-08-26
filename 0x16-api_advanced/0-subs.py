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
import sys

def number_of_subscribers(subreddit):  
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
    

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("out of rang (argument)")
    else:
        print(number_of_subscribers(sys.argv[1]))

if __name__ == "__main__":
    main()