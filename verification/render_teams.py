
import os
import glob
import re
from datetime import datetime

# Simple frontmatter parser
def parse_md(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    frontmatter = {}
    body = ""

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_lines = parts[1].strip().split('\n')
            for line in fm_lines:
                if ':' in line:
                    key, val = line.split(':', 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key == 'promoted':
                        val = (val.lower() == 'true')
                    elif key == 'weight':
                        val = int(val)
                    frontmatter[key] = val
            body = parts[2].strip()

    return frontmatter, body

def render_teams():
    team_files = glob.glob('_team/*.md')
    teams = []
    for tf in team_files:
        fm, body = parse_md(tf)
        fm['url'] = '/team/' + os.path.basename(tf).replace('.md', '.html')
        fm['excerpt'] = body[:120] + '...' if len(body) > 120 else body
        teams.append(fm)

    # Sort: promoted first? No, layout separates them.
    promoted_teams = [t for t in teams if t.get('promoted')]
    promoted_teams.sort(key=lambda x: x.get('weight', 99))

    regular_teams = [t for t in teams if not t.get('promoted')]
    regular_teams.sort(key=lambda x: x.get('weight', 99))

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Team Preview</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .team-summary { border: 1px solid #ccc; padding: 20px; border-radius: 8px; }
            .team-name { font-size: 1.5rem; margin-bottom: 0.5rem; }
            .team-description { font-style: italic; color: #666; }
            .team-image img { max-width: 100%; height: auto; border-radius: 50%; }
        </style>
    </head>
    <body>
    <div class="container pt-6 pb-6 mt-5">
        <h1>Team Verification Preview</h1>
        <div class="row">
    """

    # Promoted Loop
    for team in promoted_teams:
        # LOGIC FROM TEMPLATE:
        # {% assign team_url = team.external_url | default: team.url | relative_url %}
        team_url = team.get('external_url', team['url'])

        image_html = ""
        if team.get('image'):
            # Mock relative url
            img_src = team['image']
            image_html = f"""
            <div class="team-image">
                <img width="90" height="90" alt="{team.get('title')}" class="img-fluid mb-2" src="{img_src}" />
            </div>
            """

        linkedin_html = ""
        if team.get('linkedinurl'):
            linkedin_html = f'<a target="_blank" href="{team["linkedinurl"]}" rel="noopener noreferrer">LinkedIn</a>'

        html_content += f"""
        <div class="col-12 col-md-6 mb-2">
            <div class="team team-summary team-summary-large">
                {image_html}
                <div class="team-meta">
                    <h2 class="team-name"><a href="{team_url}">{team.get('title')}</a></h2>
                    <p class="team-description">{team.get('jobtitle')}</p>
                    {linkedin_html}
                </div>
                <div class="team-content">{team['excerpt']}</div>
            </div>
        </div>
        """

    html_content += """
        </div>
        <div class="row pt-6 pb-6">
    """

    # Regular Loop
    for team in regular_teams:
        team_url = team.get('external_url', team['url'])

        image_html = ""
        if team.get('image'):
            img_src = team['image']
            image_html = f"""
            <div class="team-image">
                <img width="60" height="60" alt="{team.get('title')}" class="img-fluid mb-2" src="{img_src}" />
            </div>
            """

        html_content += f"""
        <div class="col-12 col-md-4 mb-3">
            <div class="team team-summary">
                {image_html}
                <div class="team-meta">
                    <h2 class="team-name"><a href="{team_url}">{team.get('title')}</a></h2>
                    <p class="team-description">{team.get('jobtitle')}</p>
                </div>
            </div>
        </div>
        """

    html_content += """
        </div>
    </div>
    </body>
    </html>
    """

    with open('verification/teams_preview.html', 'w') as f:
        f.write(html_content)

    print("Generated verification/teams_preview.html")

if __name__ == "__main__":
    render_teams()
