import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


# export
def _parse(content) -> dict:

    soup = BeautifulSoup(content, "lxml")

    clss = soup.findAll("div", class_="Subhead")

    if clss:
        for cl in clss:
            print(cl.text)


user = 'emqx'
repo = 'emqx'
url = f'https://github.com/{user}/{repo}/graphs/contributors'


async def emqx():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(3 * 10**3)
        page_content = await page.content()
        print(_parse(page_content))
        await browser.close()


asyncio.run(emqx())