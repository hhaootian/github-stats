#!/usr/bin/env python

import requests
import sys
import os
from params import QUERY
from clone_repo import clone


username = sys.argv[1]
token = sys.argv[2]

headers = {"Authorization": f"bearer {token}"}

request = requests.post(
  'https://api.github.com/graphql',
  json={'query': QUERY}, headers=headers
)

data = request.json()['data']['viewer']

stars = 0
repo_urls = []
for repo in data['repositories']['nodes']:
    if repo['owner']['login'] == data['login']:
        stars += repo['stargazerCount']
        repo_urls.append(repo['url'])


repos = data['repositoriesContributedTo']['totalCount']
commit = data['contributionsCollection']['totalCommitContributions']
issue = data['contributionsCollection']['totalIssueContributions']
pr = data['contributionsCollection']['totalPullRequestContributions']
prr = data['contributionsCollection']['totalPullRequestReviewContributions']

for data in [stars, repos, commit, issue, pr, prr]:
    os.system(f"echo {data} >> stats.txt")

clone(username, token, repo_urls)
