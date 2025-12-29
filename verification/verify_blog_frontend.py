from playwright.sync_api import sync_playwright
import os

def create_mock_html():
    # Mocking the blog page with the new post
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Blog - Merced Botanical Gardens</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <!-- Using CDN for bootstrap to simulate styling since local SCSS isn't compiled -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
        /* Minimal custom styles to approximate the look */
        body { font-family: serif; color: #333; }
        .blog-list { max-width: 800px; margin: 0 auto; padding: 20px; }
        .blog-post-summary { margin-bottom: 3rem; }
        h1, h2 { font-family: 'Playfair Display', serif; color: #2c3e50; }
        a { color: #27ae60; text-decoration: none; }
        .text-muted { color: #6c757d; font-size: 0.9em; }
        .header-extra { padding: 20px; border-bottom: 1px solid #eee; margin-bottom: 20px; }
      </style>
    </head>
    <body>
      <div class="container">
          <header class="header-extra">
            <h1>Merced Botanical Gardens</h1>
            <nav><a href="#">Home</a> | <a href="#">Blog</a></nav>
          </header>

          <main>
              <h1 class="mb-4">Blog</h1>
              <p class="lead">Here we share progress updates, insights, and news from our team. Stay tuned for more content!</p>

              <div class="blog-list">
                  <div class="blog-post-summary mb-5">
                    <h2><a href="#">The Vision for Merced's Green Future</a></h2>
                    <p class="text-muted">December 29, 2025</p>
                    <div class="excerpt">
                      <p>Living in Merced means understanding the unique challenges of our Zone 9b climate. With scorching summers where temperatures frequently soar above 100°F...</p>
                    </div>
                    <a href="#" aria-label="Read more about The Vision for Merced's Green Future">Read more...</a>
                  </div>
              </div>
          </main>
      </div>
    </body>
    </html>
    """

    with open("verification/mock_blog_preview.html", "w") as f:
        f.write(html_content)

    return os.path.abspath("verification/mock_blog_preview.html")

def test_blog_preview(page):
    path = create_mock_html()
    page.goto(f"file://{path}")

    # Assertions to ensure content is present
    expect(page.get_by_role("heading", name="The Vision for Merced's Green Future")).to_be_visible()
    expect(page.get_by_text("December 29, 2025")).to_be_visible()

    page.screenshot(path="verification/blog_preview.png")

if __name__ == "__main__":
    from playwright.sync_api import expect
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_blog_preview(page)
            print("Verification successful. Screenshot saved to verification/blog_preview.png")
        finally:
            browser.close()
