import os

html_files = [
    "index.html",
    "project.html",
    "profile-details.html",
    "prediksi rumah.html",
    "superstore.html",
    "HeartDisease.html",
    "chatbot FIT.html"
]

# 1. Fix missing .container in navbars
for file_name in html_files:
    file_path = os.path.join(r"c:\bismillah kerja sukse\porto", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # If it is <div class="navbar">, replace it with <div class="container navbar">
    # (But be careful not to replace it if it's already container navbar)
    content = content.replace('<div class="navbar">', '<div class="container navbar">')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Navbars fixed.")

# 2. Append missing CSS classes to style.css
missing_css = """
/* ==================================
   PROFILE DETAILS PAGE
=================================== */
.details-grid {
  display: grid;
  gap: 30px;
  margin-bottom: 60px;
}

.detail-card {
  background: rgba(30, 41, 59, 0.4);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.detail-card h2 {
  font-family: 'Outfit', sans-serif;
  font-size: 24px;
  color: #f1f5f9;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.detail-item {
  margin-bottom: 24px;
}

.detail-item:last-child {
  margin-bottom: 0;
}

.detail-item h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 18px;
  color: #60a5fa;
  margin-bottom: 4px;
}

.detail-item > span {
  display: block;
  color: #94a3b8;
  font-size: 13.5px;
  font-weight: 600;
  margin-bottom: 12px;
}

.course-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 12px;
}

.course-list span {
  background: rgba(15, 23, 42, 0.6);
  color: #93c5fd;
  border: 1px solid rgba(56, 189, 248, 0.2);
  border-radius: 8px;
  padding: 6px 14px;
  font-size: 13px;
  transition: all 0.3s;
}

.course-list span:hover {
  background: rgba(56, 189, 248, 0.1);
  border-color: rgba(56, 189, 248, 0.4);
}

.detail-item p {
  color: #cbd5e1;
  font-size: 15px;
  line-height: 1.7;
  margin-bottom: 12px;
}

.detail-item ul {
  margin-left: 20px;
  color: #cbd5e1;
}

.detail-item li {
  font-size: 14.5px;
  margin-bottom: 8px;
}

.detail-item strong {
  color: #38bdf8;
  font-weight: 600;
}

/* ==================================
   PROJECTS FILTERS
=================================== */
.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-bottom: 40px;
}

.filter-btn {
  background: rgba(30, 41, 59, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #cbd5e1;
  padding: 8px 18px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.filter-btn:hover {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
}

.filter-btn.active {
  background: #3b82f6;
  color: #ffffff;
  border-color: #3b82f6;
}

.project-group {
  margin-bottom: 40px;
}

/* Responsive fixes */
@media (max-width: 760px) {
  .skills-list {
    justify-content: center;
  }
}
"""

with open(r"c:\bismillah kerja sukse\porto\style.css", "a", encoding="utf-8") as f:
    f.write(missing_css)

print("CSS appended.")
