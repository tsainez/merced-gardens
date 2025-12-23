from playwright.sync_api import sync_playwright
import os

def verify_focus_styles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "verification/test_focus.html")

        page.goto("file://" + file_path)

        page.keyboard.press("Tab")

        # Wait a bit for styles to apply if any transition (though local file is instant)
        page.wait_for_timeout(500)

        page.screenshot(path="verification/focus_style.png")
        print("Screenshot taken.")
        browser.close()

if __name__ == "__main__":
    verify_focus_styles()
