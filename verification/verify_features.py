from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open the local file
        # We need absolute path
        cwd = os.getcwd()
        path = f"file://{cwd}/verification/repro.html"
        page.goto(path)

        # Take a screenshot
        screenshot_path = "verification/features_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
