import json
import aiohttp
import re
import os


PATTERN_NEXT_LINK = '<([^>]*)>; rel="next"'


def get_token():
    token = os.getenv('GITHUB_TOKEN')
    return str(token)


def find_url_in_link(link):
    url = re.findall(PATTERN_NEXT_LINK, link)
    return url[0] if url else None


async def get_repos_from_github(url):
    token = get_token()
    next_url = url
    repos = []
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        while next_url:
            async with session.get(
                    next_url, headers={"Authorization": token}) as response:
                content = json.loads(await response.text())
                if isinstance(content, dict) and (
                        content.get("message") == "Not Found"):
                    raise KeyError
                repos.extend(content)
                next_url = build_next_url(response)
        return repos


def build_next_url(response):
    if 'Link' in response.headers.keys():
        return find_url_in_link(response.headers['Link'])
    return None
