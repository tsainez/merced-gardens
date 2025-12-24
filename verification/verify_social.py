
from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath("verification/test_social.html")
        page.goto(f"file://{file_path}")

        # Verify aria-label
        github_link = page.get_by_role("link", name="Github (opens in a new tab)")
        expect(github_link).to_be_visible()
        expect(github_link).to_have_attribute("target", "_blank")
        expect(github_link).to_have_attribute("rel", "noopener noreferrer")

        # Verify image is hidden from accessibility tree
        # We can't easily check 'hidden from a11y tree' with standard matchers directly in a simple way
        # but we can check the attributes exist.
        img = github_link.locator("img")
        expect(img).to_have_attribute("alt", "")
        expect(img).to_have_attribute("aria-hidden", "true")

        # Take screenshot
        page.screenshot(path="verification/social_links.png")
        print("Verification successful!")

        browser.close()

if __name__ == "__main__":
    run()
