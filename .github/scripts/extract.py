from github import Github
from github import Auth
import sys
import json


# Replace with your GitHub token or credentials
github_token = sys.argv[1]

auth = Auth.Token(github_token)

g = Github(auth=auth)

repo = g.get_repo("rakeshdyx/issues-comment-poc")

issue = repo.get_issue(number=2)

## Get the issue comment
comments = issue.get_comments()

## Get Body of the comment as json
for comment in comments:
    comment_body_json = comment.body

## Convert json to dictionary
try:
    comment_body_dict = json.loads(comment_body_json)
except json.JSONDecodeError as e:
    print("Error decoding JSON", e)

for value in comment_body_dict:
    print(value)


