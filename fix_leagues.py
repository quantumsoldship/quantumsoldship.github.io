import re

new_standings = [
    ("Bobby T.", "2-0", "100%"),
    ("Bennett C.", "2-0", "100%"),
    ("Sebastian R.", "2-0", "100%"),
    ("Matthew F.", "2-0", "100%"),
    ("Tina F.", "1-1", "50%"),
    ("Zoe C.", "1-1", "50%"),
    ("Graham G.", "0-2", "0%"),
    ("Grayson G.", "0-2", "0%"),
    ("Aly T.", "0-2", "0%"),
    ("Levi C.", "0-2", "0%"),
    ("Maddox T.", "0-2", "0%")
]

new_skills = [
    ("Bobby T.", "56"),
    ("Bennett C.", "56"),
    ("Sebastian R.", "55"),
    ("Matthew F.", "54"),
    ("Jackson F.", "54"),
    ("Tina F.", "53"),
    ("Maddox T.", "52"),
    ("Grayson G.", "52"),
    ("Aly T.", "47"),
    ("Zoe C.", "46"),
    ("Graham G.", "46"),
    ("Levi C.", "45")
]

def generate_detailed_standings():
    html = ""
    for i, (name, record, pct) in enumerate(new_standings):
        highlight_class = " highlight-item" if i < 4 else ""
        html += f"""                        <div class="detailed-ranking-item{highlight_class}">
                            <div class="ranking-number">
                                <span class="rank-circle small">{i+1}</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">{name} ({record}) – {pct}</span>
                            </div>
                        </div>\n"""
    return html.rstrip()

def generate_detailed_skills():
    html = ""
    for i, (name, rating) in enumerate(new_skills):
        highlight_class = " highlight-item" if i < 4 else ""
        html += f"""                        <div class="detailed-ranking-item{highlight_class}">
                            <div class="ranking-number">
                                <span class="rank-circle small">{i+1}</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">{name} – {rating}</span>
                            </div>
                        </div>\n"""
    return html.rstrip()

with open("leagues.html", "r") as f:
    content = f.read()

# Replace the standings
content = re.sub(r'(<h3>Win Percentage Rankings</h3>.*?<div class="detailed-rankings">)(.*?)(</div>\s*</div>\s*</div>\s*<div class="column")', lambda m: m.group(1) + "\n" + generate_detailed_standings() + "\n                    " + m.group(3), content, flags=re.DOTALL)

# Replace the skills
content = re.sub(r'(<h3>Skill Rating Rankings</h3>.*?<div class="detailed-rankings">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)', lambda m: m.group(1) + "\n" + generate_detailed_skills() + "\n                    " + m.group(3), content, flags=re.DOTALL)

with open("leagues.html", "w") as f:
    f.write(content)

