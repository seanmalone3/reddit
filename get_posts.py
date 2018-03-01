# import requests
# import requests.auth
# from config import *
# import json

import praw
from config import *
from praw.models import MoreComments

r = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent=user_agent,
                     username=username)
posts = r.subreddit('science').top(limit=5)
for post in posts:
    submission = r.submission(id=post)
    comment_count = 0
    comment_sum = 0
    for comment in submission.comments[0:4]:
        comment_sum += comment.score
        comment_count += 1
    print('\nPost_title:', submission.title, '\nScore:', submission.score, 'Ratio:', submission.upvote_ratio, 'Comments:', submission.num_comments, 'Top Comment Average:', comment_sum/comment_count, '\nURL:', submission.url)

# submission = r.submission(id='3g1jfi')
#
# for top_level_comment in submission.comments:
#     if isinstance(top_level_comment, MoreComments):
#         continue
#     print(top_level_comment.body)