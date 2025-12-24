import os
import yaml

def check_team_file(filepath):
    print(f"Checking {filepath}...")
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Parse front matter
        if not content.startswith('---'):
            print(f"Error: {filepath} does not start with front matter.")
            return False

        parts = content.split('---')
        if len(parts) < 3:
            print(f"Error: {filepath} front matter invalid.")
            return False

        front_matter = yaml.safe_load(parts[1])

        required_fields = ['title', 'jobtitle', 'promoted', 'weight']
        for field in required_fields:
            if field not in front_matter:
                print(f"Error: {filepath} missing field '{field}'.")
                return False

        print(f"Success: {filepath} looks good.")
        return True

    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return False

def check_about_file(filepath):
    print(f"Checking {filepath}...")
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Check for specific strings
        checks = [
            "Merced Gardens is a nonprofit organization",
            "filed for nonprofit status with the Secretary of California",
            "Visit our [Team page](/team)",
            "Secretary",
            "Treasurer"
        ]

        for check in checks:
            if check not in content:
                print(f"Error: {filepath} missing text: '{check}'")
                return False

        print(f"Success: {filepath} looks good.")
        return True
    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return False

files_to_check = ['_team/secretary.md', '_team/treasurer.md']
all_pass = True
for f in files_to_check:
    if not check_team_file(f):
        all_pass = False

if not check_about_file('about.md'):
    all_pass = False

if all_pass:
    print("All checks passed!")
else:
    print("Some checks failed.")
    exit(1)
