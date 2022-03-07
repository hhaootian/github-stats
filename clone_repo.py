#!/usr/bin/env python
import os


def clone(username, token, repos):
    """clone repo and run cloc
    """
    file_names = []

    for repo in repos:
        repo_name = repo.split("/")[-1]
        file_names.append(repo_name + ".txt")

        repo_url = "/".join(repo.split("/")[-2:])
        repo_url = f"https://{username}:{token}@github.com/" + repo_url

        os.system(f"git clone {repo_url} -q")

        # run cloc
        os.system(f"cloc {repo_name} --out {repo_name}.txt --quiet")

    os.system("cloc --sum-reports %s --out=everything" % " ".join(file_names))
