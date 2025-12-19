from playwright.sync_api import sync_playwright

def verify_wip_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/temp_wip.html")
        page.screenshot(path="verification/wip_page.png")
        browser.close()

if __name__ == "__main__":
    verify_wip_page()
