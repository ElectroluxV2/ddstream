import asyncio
import pyppeteer


async def main():
    #python3 -m electron_inject  --browser --enable-devtools-hotkeys --render-script=test.js - /usr/bin/discord
    fileName = "video-1616"

    browser = await pyppeteer.connect(dict({
        "browserURL": "http://localhost:53323"
    }))

    page = (await browser.pages())[0]

    await page.goto("https://discord.com/channels/457277755722301450/750517869691011103")
    print("1")
    await page.waitFor('div[data-slate-object="block"]')
    print("2")
    await page.type('div[data-slate-object="block"]', 'test2')
    print("3")
    await page.type('body', '\u000d')
    print("4")
    await page.waitFor('a[data-list-item-id="channels___753729704187527312"]')
    print("5")
    await page.evaluate('''() => {
        return document.querySelector('a[data-list-item-id="channels___753729704187527312"]').click();
    }''')
    #await page.click('a[data-list-item-id="channels___753729704187527312"]')
    print("6")
    await page.waitFor('div.rtcConnectionQualityFine-2J6i8z')
    print("6.5")
    await page.waitFor('button[aria-label="Share Your Screen"]')
    print("7")
    await page.click('button[aria-label="Share Your Screen"]')
    print("8")
    await page.waitFor('button[aria-label="Close"]')
    print("9")
    await page.waitFor('div.item-1TLUig.segmentControlOption-1vCKaY')
    print("9.5")
    #await page.click('div.item-1TLUig.segmentControlOption-1vCKaY:nth-child(2)')

    await page.evaluate('''() => {
        const elements = document.querySelector('div.sourceContainer-3LOXkb');
        for (const elem of elements.children) {
            const text = elem.firstElementChild.children[1].innerText;
            if (text.includes("'''+fileName+'''")) {
                elem.click();
            }
        }
    }''')
    print("10")
    #await page.waitFor('div.tile-2w4k5N.tile-8W93rZ')
    print("11")
    #await page.click('div.tile-2w4k5N.tile-8W93rZ')
    print("11.1")
    await page.waitFor('button[type=submit]')
    print("11.2")
    await page.click('button[type=submit]')
    print("12")
    await page.screenshot({'path': 'example.png'})
    print("13")

    dimensions = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')

    print(dimensions)

    await browser.disconnect()


asyncio.get_event_loop().run_until_complete(main())
