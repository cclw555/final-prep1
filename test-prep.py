from github import Github
import yaml
data = yaml.safe_load(open('credentials.yml'))
# task 0
token = data['creds']['token'].strip()
user = data['creds']['username'].strip()


g = Github(token)
repo = g.get_repo(user)

branch = repo.get_branches()
for b in branch:
    print(b)

commits = repo.get_commits(sha='my-new-branch')  # Get commits from the 'main' branch
print("\nCommits in my-new-branch branch:")
for commit in commits:
    print(f'{commit.sha} - {commit.commit.message}')