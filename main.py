import asyncio
from datetime import date

from playwright.async_api import async_playwright

# code change


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto("https://www.bbc.com/")
        await page.screenshot(path=f'bbc-hm-pg-{date.today()}.png', full_page=True)
        media_title = await page.query_selector_all('.media__title')
        media_link = await page.query_selector_all('.media__link')

        for title in media_title:
            open(f'bbc-hm-pg-{date.today()}.txt', 'a').write(f'{await title.inner_text()}, \n')

        for link in media_link:
            open(f'bbc-hm-pg-{date.today()}.txt', 'a').write(f'{await link.get_property("href")}, \n')

        await page.close()

asyncio.run(main())
