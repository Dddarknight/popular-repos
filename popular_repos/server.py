from flask import Flask
from flask_restful import Api
from popular_repos.config import BaseConfig
from popular_repos.resources import Repos, cache


app = Flask(__name__)
app.config.from_object(BaseConfig)
cache.init_app(app)
api = Api(app)
api.add_resource(Repos, "/api/top/<username>")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
