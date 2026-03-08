from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch Microsoft Edge
    browser = p.chromium.launch(channel="msedge", headless=False)

    page = browser.new_page()

    # Open Bing
    page.goto("https://www.bing.com")

    # Locate search box using XPath
    search_box = page.locator('//*[@id="sb_form_q"]')

    # Wait a few seconds
    page.wait_for_timeout(5000)

    # Type search query
    search_box.fill("IND vs NZ update")

    # Press Enter
    search_box.press("Enter")

    # Wait until search results appear
    page.wait_for_selector("li.b_algo")

    print("\nTop Bing Results:\n")

    # Capture result titles
    results = page.locator("li.b_algo h2")

    for i in range(min(5, results.count())):
        print(results.nth(i).inner_text())

    # Keep browser open
    page.wait_for_timeout(8000)

    browser.close()