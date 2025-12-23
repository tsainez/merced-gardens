from playwright.sync_api import sync_playwright
import os

def verify_favicon():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the HTML file directly
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/_layouts/default.html")

        # We can't easily verify the favicon visual in headless mode without a server serving it correctly,
        # but we can verify the DOM elements are present and correct.

        # Check for SVG icon
        svg_icon = page.locator('link[rel="icon"][type="image/svg+xml"]')
        href_svg = svg_icon.get_attribute("href")
        print(f"SVG Icon href: {href_svg}")

        if "favicon.svg" in href_svg:
            print("SUCCESS: Found SVG favicon link")
        else:
            print(f"FAILURE: Expected favicon.svg in href, got {href_svg}")

        # Check for PNG fallback
        png_icon = page.locator('link[rel="alternate icon"][type="image/png"]')
        href_png = png_icon.get_attribute("href")
        print(f"PNG Icon href: {href_png}")

        if "noun-botanical-garden.png" in href_png:
             print("SUCCESS: Found PNG fallback link")
        else:
             print(f"FAILURE: Expected noun-botanical-garden.png in href, got {href_png}")

        browser.close()

if __name__ == "__main__":
    verify_favicon()
