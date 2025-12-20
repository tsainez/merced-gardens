from playwright.sync_api import sync_playwright
import os

def check_font():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the verification file
        file_path = os.path.abspath("verification/font_check.html")
        page.goto(f"file://{file_path}")

        # Take a screenshot
        page.screenshot(path="verification/font_verification.png")

        # Verify the font family is applied (computed style)
        element = page.locator("body")
        font_family = element.evaluate("el => getComputedStyle(el).fontFamily")
        print(f"Computed font-family: {font_family}")

        expected_font = "Playfair Display"
        if expected_font not in font_family:
            raise AssertionError(
                f"Expected font '{expected_font}' not applied; computed: {font_family}"
            )

        # Verify that the browser attempted to load the local font
        # We can't easily check network requests for file:// but we can check if it rendered without fallback if we had a weird fallback

        browser.close()

if __name__ == "__main__":
    check_font()
