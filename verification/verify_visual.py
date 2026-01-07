
from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get absolute path to the mock file
    cwd = os.getcwd()
    file_path = f"file://{cwd}/verification/mock_post.html"

    page.goto(file_path)

    # Verify the text content
    text = page.locator(".text-muted").inner_text()
    print(f"Found text: {text}")

    # Take screenshot
    page.screenshot(path="verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
