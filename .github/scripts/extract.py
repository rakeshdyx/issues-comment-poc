from github import Github
from github import Auth
import sys

comment_body = []
# Replace with your GitHub token or credentials
github_token = sys.argv[1]

auth = Auth.Token(github_token)

g = Github(auth=auth)

repo = g.get_repo("rakeshdyx/issues-comment-poc")

issue = repo.get_issue(number=2)

comments = issue.get_comments()
for comment in comments:
    comment_body.append(comment.body)
print(comment_body)




# # Replace with your repository and issue or pull request number
# repository_name = "saichitikeshi123/bayer-int/calantic-vm-deploy"
# issue_number = 25

# # Connect to GitHub using your token
# g = Github(github_token)
# repo = g.get_repo(repository_name)
# issue = repo.get_issue(issue_number)

# # Fetch comments from the issue
# comments = issue.get_comments()

# print(comments)

# # Define the key you're looking for
# target_key = "value"

# # Search for the key in comments and extract the associated value
# for comment in comments:
#     comment_body = comment.body
#     key_index = comment_body.find(f"@{target_key}:")
#     if key_index != -1:
#         start_index = key_index + len(target_key) + 2
#         value = comment_body[start_index:].strip()
#         print(f"Value for {target_key}: {value}")
#         break  # Stop after finding the first instance
