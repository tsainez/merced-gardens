import yaml
import os

def verify_contact_update():
    # Verify _data/contact.yml
    print("Verifying _data/contact.yml...")
    if not os.path.exists("_data/contact.yml"):
        print("FAIL: _data/contact.yml does not exist")
        return False

    with open("_data/contact.yml", "r") as f:
        data = yaml.safe_load(f)
        if data.get("email") == "info@mercedgardens.org":
            print("PASS: Email updated correctly.")
        else:
            print(f"FAIL: Email is {data.get('email')}")
            return False

    # Verify contact.md
    print("Verifying contact.md...")
    if not os.path.exists("contact.md"):
        print("FAIL: contact.md does not exist")
        return False

    with open("contact.md", "r") as f:
        content = f.read()
        if "{% include newsletter.html %}" in content and "## Join our Mailing List" in content:
            print("PASS: contact.md updated correctly.")
        else:
            print("FAIL: contact.md content incorrect")
            return False

    # Verify _includes/newsletter.html
    print("Verifying _includes/newsletter.html...")
    if not os.path.exists("_includes/newsletter.html"):
        print("FAIL: _includes/newsletter.html does not exist")
        return False

    with open("_includes/newsletter.html", "r") as f:
        content = f.read()
        if 'data-netlify="true"' in content and '<form' in content:
             print("PASS: _includes/newsletter.html looks correct.")
        else:
             print("FAIL: _includes/newsletter.html content incorrect")
             return False

    return True

if __name__ == "__main__":
    if verify_contact_update():
        print("All checks passed.")
    else:
        print("Checks failed.")
        exit(1)
