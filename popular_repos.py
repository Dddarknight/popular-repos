import asyncio
import json
from flask import Flask
from flask import request, Response
from flask_restful import Api, Resource
from flask_caching import Cache
from internal_repos import modify_external_repos
from external_repos import get_repos_from_github
from config import BaseConfig


DEFAULT_REPOS_COUNT = 10
DEFAULT_TIMEOUT = 60
INDENT = 4
EXCEPTION_VALUE = "Not found"


app = Flask(__name__)
app.config.from_object(BaseConfig)
cache = Cache(app)
api = Api(app)


class Repos(Resource):
    
    @cache.cached(timeout=DEFAULT_TIMEOUT, query_string=True)
    def get(self, username):
        url = build_url(username)
        repos = get_repos(url)
        if repos == EXCEPTION_VALUE:
            return 'The user was not found. Please, check Username.', 404
        modified_repos = modify_external_repos(repos)
        limit = int(request.args.get('limit')) if (
            request.args.get('limit')) else DEFAULT_REPOS_COUNT
        return Response(json.dumps(
            modified_repos[:limit], indent=INDENT), content_type='application/json')


def build_url(username):
    return f"https://api.github.com/users/{username}/repos"


def get_repos(url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    repos = loop.run_until_complete(get_repos_from_github(url))
    return repos


api.add_resource(Repos, "/api/top/<username>")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
