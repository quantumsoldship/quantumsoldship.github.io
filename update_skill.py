import re

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

def generate_detailed_rankings():
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

# find the Skill Rating Rankings block and replace its detailed-rankings contents
pattern = re.compile(r'<h3>Skill Rating Rankings</h3>.*?<div class="detailed-rankings">(.*?)</div>\s*</div>\s*</div>', re.DOTALL)
new_block = f"""<h3>Skill Rating Rankings</h3>
                        <p>Rating considers opponent strength, game scores, and overall performance. Players highlighted are championship qualifiers.</p>
                    </div>

                    <div class="detailed-rankings">
{generate_detailed_rankings()}
                    </div>
                </div>
            </div>"""
content = pattern.sub(new_block, content)

# I should also fix the styling if I messed it up in the first pass (where I set width: 100%)
# Actually wait, in the first step the script had: `columns_pattern = re.compile(r'<div class="columns">.*?<!-- Explanation Note -->', re.DOTALL)`
# Wait I overwrote the entire columns div in python in step 1, but I'll undo those first! Let's checkout leagues.html and re-apply correctly.
