import re

def verify_defer_script():
    with open('_layouts/default.html', 'r') as f:
        content = f.read()

    if 'src="{{ \'/assets/js/scripts.js\' | relative_url }}" defer' in content:
        print("PASS: script.js has defer attribute")
    else:
        print("FAIL: script.js missing defer attribute")

def verify_css_comments():
    with open('assets/css/style.scss', 'r') as f:
        content = f.read()

    if '// @import "bootstrap/tables";' in content:
        print("PASS: bootstrap/tables is commented out")
    else:
        print("FAIL: bootstrap/tables is NOT commented out")

    if '// @import "bootstrap/forms";' in content:
        print("PASS: bootstrap/forms is commented out")
    else:
        print("FAIL: bootstrap/forms is NOT commented out")

if __name__ == "__main__":
    verify_defer_script()
    verify_css_comments()
