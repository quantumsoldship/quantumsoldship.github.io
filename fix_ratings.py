import re

# Need to accurately parse and sort the players by skill rating

ratings = {
    "Sam C.": 92,
    "Josh N.": 76,
    "Isaac N.": 76,
    "Bennett C.": 56,
    "Joshua H.": 71,
    "Matthew Z.": 71,
    "Bobby T.": 56,
    "Graham G.": 46,
    "Jackson F.": 54,
    "Thomas H.": 63,
    "Caleb J.": 62,
    "Grayson G.": 52,
    "Caleb M.": 59,
    "Zoe C.": 46,
    "Simon Z.": 47,
    "Aly T.": 47,
    "Tina F.": 53,
    "Maddox T.": 52,
    "Matthew F.": 54,
    "Sebastian R.": 55,
    "Levi C.": 45
}

sorted_ratings = sorted(ratings.items(), key=lambda item: item[1], reverse=True)

html = """            <div class="column">
                <div class="ranking-card">
                    <div class="ranking-card-header">
                        <h3>Skill Rating Rankings</h3>
                        <p>Rating considers opponent strength, game scores, and overall performance. Players highlighted are championship qualifiers.</p>
                    </div>

                    <div class="detailed-rankings">\n"""

for i, (name, rating) in enumerate(sorted_ratings):
    # Just highlighting first 4 for now
    highlight_class = " highlight-item" if i < 4 else ""
    html += f"""                        <div class="detailed-ranking-item{highlight_class}">
                            <div class="ranking-number">
                                <span class="rank-circle small">{i+1}</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">{name} – {rating}</span>
                            </div>
                        </div>\n"""

html += """                    </div>
                </div>
            </div>"""

with open("leagues.html", "r") as f:
    content = f.read()

# Replace the current column for Skill Rating Rankings
pattern = re.compile(r'<div class="column">\s*<div class="ranking-card">\s*<div class="ranking-card-header">\s*<h3>Skill Rating Rankings</h3>.*?</div>\s*</div>\s*</div>', re.DOTALL)

content = pattern.sub(html, content)

with open("leagues.html", "w") as f:
    f.write(content)
