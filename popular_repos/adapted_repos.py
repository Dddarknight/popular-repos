import enum


class RepoParams(enum.Enum):
    id = 'id'
    name = 'name'
    stars = 'stargazers_count'
    html_url = 'html_url'


def adapt(repo):
    adapted_repo = {}
    for parameter in RepoParams:
        adapted_repo.update({parameter.name: repo.get(parameter.value)})
    return adapted_repo


def adapt_github_repos(repos):
    adapted_repos = []
    for repo in repos:
        if isinstance(repo, dict):
            adapted_repos.append(adapt(repo))
    adapted_repos.sort(key=lambda repo: repo['stars'], reverse=True)
    return adapted_repos
