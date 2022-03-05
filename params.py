#!/usr/bin/env python

EXCLUDED = "CSV"

QUERY = """
query {
  viewer {
    login,
    repositoriesContributedTo(
      first: 100,
      includeUserRepositories: true
    ) {
      totalCount
    }
    repositories(
      first: 100,
      isFork: false
    ) {
      nodes {
        name
        url
        owner {
          login
        }
        stargazerCount
        forkCount
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
    }
  }
}
"""
