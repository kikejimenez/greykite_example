from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup

asession = AsyncHTMLSession()


async def get_emqx():

    user = 'emqx'
    repo = 'emqx'
    url = f'https://github.com/{user}/{repo}/graphs/contributors'

    r = await asession.get(url, timeout=10)
    return r


# async def get_pythonorg():
#     r = await asession.get('https://python.org/')
#     return r


# export
def _parse(response) -> dict:

    soup = BeautifulSoup(response.content, "lxml")

    clss = soup.findAll("div", class_="Subhead")

    if clss:
        for cl in clss:
            print(cl.text)


results = asession.run(get_emqx)

for result in results:

    print(_parse(result))