# popular-repos
Popular-repos is a web-service that uses GitHub API and shows the most starred repositories of the choosen User.

____

### CI status:

[![Python CI](https://github.com/Dddarknight/popular-repos/actions/workflows/pyci.yml/badge.svg)](https://github.com/Dddarknight/popular-repos/actions)

### CodeClimate:
<a href="https://codeclimate.com/github/Dddarknight/popular-repos/maintainability"><img src="https://api.codeclimate.com/v1/badges/4d0b778f2499458d20cf/maintainability" /></a>

<a href="https://codeclimate.com/github/Dddarknight/popular-repos/test_coverage"><img src="https://api.codeclimate.com/v1/badges/4d0b778f2499458d20cf/test_coverage" /></a>

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |
| [Py.Test](https://pytest.org) | "A mature full-featured Python testing tool" |
| [GitHub API](https://docs.github.com/en/rest) | "REST API, provided by GitHub" |

## Description
The endpoint for the web-service is like '/api/top/{username}?limit=4'.
You can choose any number of the most starred repositories to be shown.
The parameters, which are represented in the response, are: 'id', 'name', 'stars', 'html_url'.


## Installation
```
$ git clone git@github.com:Dddarknight/popular-repos.git
```

## Usage
```
$ cd python-project-lvl2
$ make run

```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)