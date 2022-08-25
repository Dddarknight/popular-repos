def modify_external_repos(repos):
    modified_repos = []
    for repo in repos:
        if isinstance(repo, dict):
            modified_repos.append({
                "id": repo.get('id'),
                "name": repo.get('name'),
                "stars": repo.get('stargazers_count'),
                "html_url": repo.get('html_url')
            })
    modified_repos.sort(key=lambda repo: repo['stars'], reverse=True)
    return modified_repos
