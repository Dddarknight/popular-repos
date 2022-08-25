FROM python:3.10
ENV POETRY_VERSION=1.1.13
RUN python3 -m pip install poetry==$POETRY_VERSION
WORKDIR /popular-repos
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev
RUN python3 -m pip install flask
RUN python3 -m pip install flask_caching
RUN python3 -m pip install aiohttp
RUN python3 -m pip install redis
RUN python3 -m pip install python-dotenv
RUN python3 -m pip install flask-restful
RUN python3 -m pip install pytest
RUN python3 -m pip install flake8
COPY . /popular-repos
CMD popular_repos.py