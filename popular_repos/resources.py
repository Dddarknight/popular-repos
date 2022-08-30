import asyncio
import json
from flask import request, Response
from flask_restful import Resource
from flask_caching import Cache
from popular_repos.adapted_repos import adapt_github_repos
from popular_repos.github_api import get_repos_from_github


DEFAULT_REPOS_COUNT = 10
DEFAULT_TIMEOUT = 60
INDENT = 4


cache = Cache()


class Repos(Resource):

    @cache.cached(timeout=DEFAULT_TIMEOUT, query_string=True)
    def get(self, username):
        url = build_url(username)
        try:
            repos = get_repos(url)
        except KeyError:
            return 'The user was not found. Please, check Username.', 404
        adapted_repos = adapt_github_repos(repos)
        limit = int(request.args.get('limit')) if (
            request.args.get('limit')) else DEFAULT_REPOS_COUNT
        return Response(make_json_repos(adapted_repos, limit),
                        content_type='application/json')


def build_url(username):
    return f"https://api.github.com/users/{username}/repos"


def get_repos(url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    repos = loop.run_until_complete(get_repos_from_github(url))
    return repos


def make_json_repos(adapted_repos, limit):
    return json.dumps(adapted_repos[:limit], indent=INDENT)
