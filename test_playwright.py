from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.example.com")
    print("Page title:", page.title())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
