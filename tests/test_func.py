import pytest
import popular_repos
import json


def test_pop_repos(monkeypatch):

    def mock_get(url):
        with open('tests/fixtures/repos.json') as read_file:
            r = json.load(read_file)
            return r

    monkeypatch.setattr(popular_repos, "get_repos", mock_get)

    with open('tests/fixtures/modified_repos.json') as expected_file:
        x = popular_repos.api.app.test_client().get('/api/top/bob?limit=5')
        print(x.text)
        assert x.text == expected_file.read()
