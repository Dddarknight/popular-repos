FROM python:3.10
ENV POETRY_VERSION=1.1.13
RUN python3 -m pip install poetry==$POETRY_VERSION
COPY ./poetry.lock ./pyproject.toml ./requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev
WORKDIR /popular_repos
COPY popular_repos/server.py .
COPY popular_repos/github_api.py popular_repos/github_api.py
COPY popular_repos/adapted_repos.py popular_repos/adapted_repos.py
COPY popular_repos/resources.py popular_repos/resources.py
COPY popular_repos/config.py popular_repos/config.py
CMD python server.py