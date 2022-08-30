from popular_repos import resources, server
import json


def test_pop_repos(monkeypatch):

    def mock_get(url):
        with open('tests/fixtures/repos.json') as read_file:
            r = json.load(read_file)
            return r

    monkeypatch.setattr(resources, "get_repos", mock_get)

    with open('tests/fixtures/modified_repos.json') as expected_file:
        result = server.api.app.test_client().get('/api/top/bob?limit=5')
        assert result.text == expected_file.read()
