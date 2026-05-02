import re

with open("champions.html", "r") as f:
    content = f.read()

new_champ = """    <!-- 2026 Championship -->
    <div class="championship-card">
      <div class="card-header">
        <h2>Airball Championship</h2>
        <div class="year-badge">2026</div>
      </div>

      <div class="champion-section">
        <div class="champion-card">
          <div class="champion-avatar">
            <div class="avatar-placeholder champion">
              <span class="avatar-initials">SC</span>
            </div>
          </div>
          <div class="champion-info">
            <h3>Sam Cullum</h3>
            <p class="champion-title">Champion</p>
          </div>
        </div>

        <div class="runner-up-card">
          <div class="runner-up-avatar">
            <div class="avatar-placeholder runner-up">
              <span class="avatar-initials">JN</span>
            </div>
          </div>
          <div class="runner-up-info">
            <h4>Josh Northington</h4>
            <p class="runner-up-title">Runner-up</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 2024 Championship -->"""

content = content.replace("    <!-- 2024 Championship -->", new_champ)

with open("champions.html", "w") as f:
    f.write(content)

