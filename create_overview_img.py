#!/usr/bin/env python
import sys


login = sys.argv[1]

output = open("overview_template.svg", "r").read()
data = open("stats.txt", "r").readlines()

for i, name in enumerate(["stars", "repos", "commit", "issue", "pr", "prr"]):
    output = output.replace("{{ " + name + " }}", data[i].strip())

output = output.replace("{{ name }}", login)

with open("overview.svg", "w") as f:
    f.write(output)
