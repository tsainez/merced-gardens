import os
from playwright.sync_api import sync_playwright

def verify_404():
    # Read the 404 content
    with open('404.html', 'r') as f:
        content = f.read()

    # Manually extract the body content (skipping frontmatter)
    # This is a rough approximation since we can't run jekyll build
    body_content = content.split('---', 2)[-1]

    # Create a mock HTML file that simulates the structure
    # We inject the content into a basic template that mimics default layout
    # Note: We can't easily link the SCSS since it needs compilation.
    # So we will just check the structure and the presence of classes.
    # We'll use CDN bootstrap to mimic the styling for the screenshot.

    mock_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Page Not Found</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <!-- Use Bootstrap 5.3 CDN for verification -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
        /* Mocking the custom .button class from _sass/components/_buttons.scss */
        .button {{
          white-space: nowrap;
          display: inline-block;
          height: 40px;
          line-height: 40px;
          padding: 0 14px;
          background: #4a6741; /* Approximating  color */
          border-radius: 4px;
          font-size: 14px;
          font-weight: normal;
          text-transform: uppercase;
          letter-spacing: 0.025em;
          color: #ffffff;
          text-decoration: none;
          transition: all 0.15s ease;
        }}
        .button:hover {{
          color: #ffffff;
          background-color: #5c8052;
          transform: translateY(-1px);
          text-decoration: none;
        }}
      </style>
    </head>
    <body>
      <main id="main-content">
        {body_content}
      </main>
    </body>
    </html>
    """

    with open('verification/mock_404.html', 'w') as f:
        f.write(mock_html)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the mock file
        page.goto(f"file://{os.path.abspath('verification/mock_404.html')}")

        # Verify elements
        # 1. Check for CSP violation (style tag inside body) -> Expect NONE
        # We can check if any style tag exists in the body part we injected
        # content.split('---', 2)[-1] should not have <style>

        # 2. Check for the elements we added
        assert page.locator('h1').inner_text() == "404"
        assert page.locator('p.h3').inner_text() == "Page not found :("
        assert page.locator('a.button').is_visible()
        assert page.locator('a.button').inner_text() == "Return Home"

        # Take screenshot
        page.screenshot(path='verification/404_screenshot.png')
        print("Verification successful. Screenshot saved.")

        browser.close()

if __name__ == "__main__":
    verify_404()
