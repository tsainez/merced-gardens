import os
from playwright.sync_api import sync_playwright

def verify_frontend():
    # Since we can't run Jekyll to serve the site, we'll create a dummy HTML file
    # that mimics the contact page structure to verify the form rendering.

    # Read the necessary file contents
    with open("_includes/newsletter.html", "r") as f:
        form_content = f.read()

    # Create a dummy HTML file
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Verification</title>
        <!-- Mocking some styles -->
        <style>
            .button {{
                background: #007bff;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
            }}
            .form-control {{
                display: block;
                width: 100%;
                padding: 0.375rem 0.75rem;
                font-size: 1rem;
                line-height: 1.5;
                color: #495057;
                background-color: #fff;
                background-clip: padding-box;
                border: 1px solid #ced4da;
                border-radius: 0.25rem;
            }}
            .mb-3 {{ margin-bottom: 1rem; }}
        </style>
    </head>
    <body>
        <h1>Contact Page Mockup</h1>
        <p>Please, feel free to reach out...</p>
        <h2>Join our Mailing List</h2>
        {form_content}
    </body>
    </html>
    """

    with open("verification/dummy_contact.html", "w") as f:
        f.write(html_content)

    # Use Playwright to render and screenshot
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath('verification/dummy_contact.html')}")

        # Verify elements exist
        if page.is_visible("form[name='newsletter']"):
            print("Form is visible")
        if page.is_visible("input[type='email']"):
             print("Email input is visible")

        page.screenshot(path="verification/contact_page_mockup.png")
        print("Screenshot saved to verification/contact_page_mockup.png")
        browser.close()

if __name__ == "__main__":
    verify_frontend()
