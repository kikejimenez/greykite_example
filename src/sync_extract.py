from requests_html import HTMLSession

s = HTMLSession()

user = 'emqx'
repo = 'emqx'
url = f'https://github.com/{user}/{repo}/graphs/contributors'

response = s.get(url)
response.html.render()

print(response)