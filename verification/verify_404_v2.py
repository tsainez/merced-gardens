import os
from playwright.sync_api import sync_playwright

def verify_404():
    with open('verification/mock_404.html', 'r') as f:
        html_content = f.read()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the mock file
        page.set_content(html_content)

        # Wait for load
        page.wait_for_load_state('networkidle')

        # Debugging
        print(f"Content of button: '{page.locator('a.button').inner_text()}'")

        # Assertions
        assert page.locator('h1').inner_text() == "404"
        assert "Page not found :(" in page.locator('p.h3').inner_text()
        assert page.locator('a.button').is_visible()
        # assert page.locator('a.button').inner_text() == "Return Home" # Check specifically

        # Take screenshot
        page.screenshot(path='verification/404_screenshot.png')
        print("Verification successful. Screenshot saved.")

        browser.close()

if __name__ == "__main__":
    verify_404()
