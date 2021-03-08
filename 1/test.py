import requests


def gen():
    yield 'hi'
    yield 'there'

r = requests.post('https://github.com/', data=gen())
print(r.request)