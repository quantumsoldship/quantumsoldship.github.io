import re

ratings_data = [
    ("Sam C.", 92),
    ("Levi C.", 77),
    ("Josh N.", 76),
    ("Isaac N.", 76),
    ("Bennett C.", 75),
    ("Joshua H.", 71),
    ("Matthew Z.", 71),
    ("Bobby T.", 69),
    ("Graham G.", 69),
    ("Jackson F.", 64),
    ("Thomas H.", 63),
    ("Caleb J.", 62),
    ("Grayson G.", 59),
    ("Caleb M.", 59),
    ("Zoe C.", 47),
    ("Simon Z.", 47),
    ("Aly T.", 46),
    ("Tina F.", 46),
    ("Maddox T.", 45),
    ("Matthew F.", 43),
]

# Looking at the user's data:
# Bobby T. 56
# Bennett C. 56
# Sebastian R. 55
# Matthew F. 54
# Jackson F. 54
# Tina F. 53
# Maddox T. 52
# Grayson G. 52
# Aly T. 47
# Zoe C. 46
# Graham G. 46
# Levi C. 45

# Wait, let me restore the skill rating section using a python script.

def restore_skill_ratings():
    html = """            <div class="column" style="width: 100%; max-width: 600px; margin: 0 auto;">
                <div class="ranking-card">
                    <div class="ranking-card-header">
                        <h3>Skill Rating Rankings</h3>
                        <p>Rating considers opponent strength, game scores, and overall performance. Players highlighted are championship qualifiers.</p>
                    </div>

                    <div class="detailed-rankings">
                        <div class="detailed-ranking-item highlight-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">1</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Sam C. – 92</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">2</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Levi C. – 45</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item highlight-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">3</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Josh N. – 76</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">4</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Isaac N. – 76</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">5</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Bennett C. – 56</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item highlight-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">6</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Joshua H. – 71</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item highlight-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">6</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Matthew Z. – 71</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">7</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Bobby T. - 56</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">8</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Graham G. - 46</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">9</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Jackson F. – 54</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">10</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Thomas H. – 63</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">11</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Caleb J. – 62</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">12</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Grayson G. – 52</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">13</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Caleb M. – 59</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">14</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Zoe C. – 46</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">15</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Simon Z. – 47</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">16</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Aly T. – 47</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">17</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Tina F. – 53</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">18</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Maddox T. – 52</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">19</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Matthew F. – 54</span>
                            </div>
                        </div>
                        <div class="detailed-ranking-item">
                            <div class="ranking-number">
                                <span class="rank-circle small">20</span>
                            </div>
                            <div class="ranking-text">
                                <span class="player-name">Sebastian R. – 55</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""
    
    with open("leagues.html", "r") as f:
        content = f.read()
    
    # We replaced the entire columns section previously, giving the single column style="width: 100%; max-width: 600px; margin: 0 auto;".
    # Let's fix that.
    
    # Find the current column
    match = re.search(r'<div class="column".*?>.*?</div>\n        </div>\n\n        <!-- Explanation Note -->', content, re.DOTALL)
    if match:
        old_cols = match.group(0)
        # remove the style attribute to go back to 2 columns
        new_cols = old_cols.replace('style="width: 100%; max-width: 600px; margin: 0 auto;"', '')
        
        # insert the new column before the closing div of "columns"
        new_cols_full = new_cols.replace('        </div>\n\n        <!-- Explanation Note -->', f'\n{html}\n        </div>\n\n        <!-- Explanation Note -->')
        
        content = content.replace(old_cols, new_cols_full)
        
        with open("leagues.html", "w") as f:
            f.write(content)
            
restore_skill_ratings()
