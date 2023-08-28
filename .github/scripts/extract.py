from github import Github
from github import Auth
from ghapi.all import GhApi
import sys
import json
import requests
import base64
import os


def createRpoVar(repository_name: str, var_name: str, var_value: str, github_token: str):
    api_url = f"https://api.github.com/repos/{repository_name}/actions/secrets/{var_name}"
    headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
    }
    print(headers)

### API request payload
    payload = {
        "encrypted_value": var_value
        }
    response = requests.put(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Secret '{var_name}' created successfully.")
    else:
        print(f"Failed to create secret '{var_name}'.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

github_token = sys.argv[1]
repo_name = "rakeshdyx/issues-comment-poc"
# Replace with your GitHub token or credentials

auth = Auth.Token(github_token)

g = Github(auth=auth)

repo = g.get_repo(repo_name)

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


for key, value in comment_body_dict.items():
    if key == "Job":
        createRpoVar(repo_name, "JOB_NAME", value, github_token)
    elif key == "InstanceName":
        createRpoVar(repo_name, "INSTANCE_NAME", value, github_token)
    elif key == "Environment":
        createRpoVar(repo_name, "ENV", value, github_token)
    else:
        print("Value is unrecognized, Please validate input data")


