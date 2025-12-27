from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the dummy HTML file
        page.goto(f"file://{os.path.abspath('verification/post_test.html')}")

        # Verify the navigation links exist
        expect(page.locator("text=Previous")).to_be_visible()
        expect(page.locator("text=Next")).to_be_visible()
        expect(page.locator("text=All Posts")).to_be_visible()

        # Verify Aria Labels
        expect(page.locator("a[aria-label='Previous post: Previous Title']")).to_be_visible()
        expect(page.locator("a[aria-label='Next post: Next Title']")).to_be_visible()
        expect(page.locator("a[aria-label='Back to Blog']")).to_be_visible()

        # Take a screenshot
        page.screenshot(path="verification/post_nav_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
