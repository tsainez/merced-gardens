import re

def verify_blog_a11y():
    filepath = 'blog.html'
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return

    # Check for the problematic link pattern
    # The original link is <a href="{{ post.url | relative_url }}">Read more...</a>
    # We want to find it and ensure it DOES NOT have an aria-label (to confirm issue)
    # or ensure it DOES have one (to confirm fix).

    # Simple regex to find the link.
    # Note: re.DOTALL is not strictly needed if it's on one line, but good practice.

    # Original pattern
    original_pattern = r'<a\s+href="{{ post.url \| relative_url }}">Read more...</a>'

    # Fixed pattern (allowing for flexible whitespace attributes)
    # We look for aria-label containing "Read more about" and {{ post.title ... }}
    fixed_pattern = r'<a\s+href="{{ post.url \| relative_url }}"\s+aria-label="Read more about {{ post.title \| escape }}">Read more...</a>'

    if re.search(fixed_pattern, content):
        print("PASS: Accessible 'Read more' link found.")
    elif re.search(original_pattern, content):
        print("FAIL: Ambiguous 'Read more' link found without aria-label.")
    else:
        print("WARNING: 'Read more' link pattern not found. Has the code changed?")

if __name__ == "__main__":
    verify_blog_a11y()
