import os
import re

def verify_post():
    post_path = "_posts/2025-12-29-the-vision-for-merceds-green-future.md"

    if not os.path.exists(post_path):
        print(f"Error: {post_path} does not exist.")
        return False

    with open(post_path, 'r') as f:
        content = f.read()

    # Check frontmatter
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        print("Error: No frontmatter found.")
        return False

    frontmatter = match.group(1)

    if 'layout: post' not in frontmatter:
        print("Error: 'layout: post' not found in frontmatter.")
        return False

    if 'title: "The Vision for Merced\'s Green Future"' not in frontmatter:
         print("Error: Title not found or incorrect in frontmatter.")
         return False

    if 'date: 2025-12-29' not in frontmatter:
        print("Error: Date not found or incorrect in frontmatter.")
        return False

    print("Success: Post file exists and frontmatter structure is valid.")
    return True

if __name__ == "__main__":
    verify_post()
