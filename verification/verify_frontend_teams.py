
from playwright.sync_api import Page, expect, sync_playwright
import os

def test_teams_content(page: Page):
    # Load the generated HTML file
    cwd = os.getcwd()
    file_path = f"file://{cwd}/verification/teams_preview.html"
    page.goto(file_path)

    # Verify Tony Sainez
    tony = page.get_by_role("link", name="Tony Sainez")
    expect(tony).to_be_visible()
    # Check link (internal team link)
    expect(tony).to_have_attribute("href", "/team/tony-sainez.html") # Based on mock logic

    # Verify Job Title for Tony
    expect(page.get_by_text("Founder & Lead Horticulturalist")).to_be_visible()

    # Verify Join the Board
    join = page.get_by_role("link", name="Join the Board")
    expect(join).to_be_visible()
    # Check link (external contact link)
    expect(join).to_have_attribute("href", "/contact/")

    # Verify Content for Join Board
    # Use more specific locator
    expect(page.locator(".team-description").get_by_text("Community Leader")).to_be_visible()
    expect(page.get_by_text("We are actively looking for community leaders")).to_be_visible()

    # Verify absence of Secretary/Treasurer
    expect(page.get_by_role("link", name="Secretary")).not_to_be_visible()
    expect(page.get_by_role("link", name="Treasurer")).not_to_be_visible()

    # Screenshot
    page.screenshot(path="verification/teams_screenshot.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        test_teams_content(page)
