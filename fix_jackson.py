import re

new_standings = [
    ("Bobby T.", "2-0", "100%"),
    ("Bennett C.", "2-0", "100%"),
    ("Sebastian R.", "2-0", "100%"),
    ("Matthew F.", "2-0", "100%"),
    ("Jackson F.", "2-0", "100%"),
    ("Tina F.", "1-1", "50%"),
    ("Zoe C.", "1-1", "50%"),
    ("Graham G.", "0-2", "0%"),
    ("Grayson G.", "0-2", "0%"),
    ("Aly T.", "0-2", "0%"),
    ("Levi C.", "0-2", "0%"),
    ("Maddox T.", "0-2", "0%")
]

def generate_top_four_index():
    html = ""
    for i, (name, record, pct) in enumerate(new_standings[:4]):
        circle_class = "rank-circle gold" if i == 0 else "rank-circle"
        top_player = " top-player" if i == 0 else ""
        html += f"""            <div class="ranking-item{top_player}">
                <div class="ranking-number">
                    <span class="{circle_class}">{i+1}</span>
                </div>
                <div class="ranking-details">
                    <span class="player-name">{name}</span>
                    <span class="record">{record} ({pct})</span>
                </div>
            </div>\n"""
    return html.rstrip()

def update_index():
    with open("index.html", "r") as f:
        content = f.read()
    
    pattern = re.compile(r'<div class="rankings">.*?</div>\n\n        <div class="rankings-footer">', re.DOTALL)
    new_block = f'<div class="rankings">\n{generate_top_four_index()}\n        </div>\n\n        <div class="rankings-footer">'
    content = pattern.sub(new_block, content)
    
    with open("index.html", "w") as f:
        f.write(content)

def generate_top_four_leagues():
    html = ""
    for i, (name, record, pct) in enumerate(new_standings[:4]):
        circle_class = "rank-circle gold" if i == 0 else "rank-circle"
        html += f"""            <div class="ranking-item top-player">
                <div class="ranking-number">
                    <span class="{circle_class}">{i+1}</span>
                </div>
                <div class="ranking-details">
                    <span class="player-name">{name}</span>
                    <span class="record">{record} ({pct})</span>
                </div>
            </div>\n"""
    return html.rstrip()

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

def update_leagues():
    with open("leagues.html", "r") as f:
        content = f.read()

    # Top four block
    top_four_pattern = re.compile(r'<div class="rankings">\s*<div class="ranking-item top-player">.*?</div>\s*</section>', re.DOTALL)
    top_four_repl = f'<div class="rankings">\n{generate_top_four_leagues()}\n        </div>\n    </section>'
    content = top_four_pattern.sub(top_four_repl, content)

    # Detailed Standings
    content = re.sub(r'(<h3>Win Percentage Rankings</h3>.*?<div class="detailed-rankings">)(.*?)(</div>\s*</div>\s*</div>\s*<div class="column")', lambda m: m.group(1) + "\n" + generate_detailed_standings() + "\n                    " + m.group(3), content, flags=re.DOTALL)

    with open("leagues.html", "w") as f:
        f.write(content)

update_index()
update_leagues()
