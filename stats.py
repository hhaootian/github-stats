#!/usr/bin/env python
import requests
import os
import sys


username = sys.argv[1]
token = sys.argv[2]

headers = {"Authorization": f"token {token}"}

r = requests.get(
    f"https://api.github.com/users/{username}/repos",
    headers=headers
)

repos = r.json()
file_names = []

for repo in repos:
    repo_name = repo['name']
    file_names.append(repo_name + ".txt")
    repo_url = f"https://{username}:{token}@github.com/{username}/{repo_name}"
    os.system("git clone " + repo_url)
    os.system(f"cloc {repo_name} --out {repo_name}.txt")

os.system("cloc --sum-reports %s --out=everything" % " ".join(file_names))
