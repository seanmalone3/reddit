# import requests
# import requests.auth
# from config import *
# import json
#
# client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
# post_data = {"grant_type": "password", "username": username, "password": password}
# headers = {"User-Agent": "DictionaryBot/0.1 by thewhiteone3"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# response.json()
# res = json.loads(response.text)
# token = res['access_token']
# print(token)

import praw
from config import *
from praw.models import MoreComments
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent=user_agent,
                     username=username)
# print(reddit.user.me())
submission = reddit.submission(id='3g1jfi')

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)