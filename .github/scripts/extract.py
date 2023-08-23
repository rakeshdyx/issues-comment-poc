from github import Github
from github import Auth
import sys
import json
import requests
import base64


def createSecret(repository_name, secret_name, secret_value, github_token):
    api_url = f"https://api.github.com/repos/{repository_name}/actions/secrets/{secret_name}"
    headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.v3+json"
    }
    print(headers)
### Encode the secret value as base64
    encoded_secret_value = base64.b64encode(secret_value.encode()).decode()
### API request payload
    payload = {
        "encrypted_value": encoded_secret_value,
        "key_id": ""
        }
    response = requests.put(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Secret '{secret_name}' created successfully.")
    else:
        print(f"Failed to create secret '{secret_name}'.")
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
        createSecret(repo_name, "JOB_NAME", value, github_token)
    elif key == "InstanceName":
        createSecret(repo_name, "INSTANCE_NAME", value, github_token)
    elif key == "Environment":
        createSecret(repo_name, "ENV", value, github_token)
    else:
        print("Value is unrecognized, Please validate input data")


