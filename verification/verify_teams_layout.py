
import re

def verify_teams_layout(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Look for the assigned variable and its usage
    pattern_assign = r'{%\s*assign\s+team_url\s*=\s*team.external_url\s*\|\s*default:\s*team.url\s*\|\s*relative_url\s*%}'
    pattern_usage = r'<h2 class="team-name"><a href="{{ team_url }}">{{ team.title }}</a></h2>'

    if re.search(pattern_assign, content) and re.search(pattern_usage, content):
        print("Verification SUCCESS: external_url logic found.")
    else:
        print("Verification FAILED: external_url logic not found or incorrect.")
        # Debug info
        print("\nSearching for assignment pattern:", pattern_assign)
        print("Searching for usage pattern:", pattern_usage)
        # Check partial matches
        if re.search(r'assign\s+team_url', content):
            print("Found assignment variable 'team_url'")
        else:
            print("Did not find assignment variable 'team_url'")

if __name__ == "__main__":
    verify_teams_layout("_layouts/teams.html")
