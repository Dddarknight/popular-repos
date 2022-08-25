import json
import aiohttp
import re
import os


EXCEPTION_VALUE = "Not found"


def get_token():
    token = os.getenv('GITHUB_TOKEN')
    return str(token)


def find_url_in_link(link):
    url = re.findall(r'<([^>]*)>; rel="next"', link)
    if not url:
        return None
    return url[0]


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
                    return EXCEPTION_VALUE
                repos.extend(content)
                if 'Link' in response.headers.keys():
                    next_url = find_url_in_link(response.headers['Link'])
                else:
                    next_url = None
        return repos
