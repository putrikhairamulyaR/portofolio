import os
import re

html_files = [
    "index.html",
    "project.html",
    "profile-details.html",
    "prediksi rumah.html",
    "superstore.html",
    "HeartDisease.html",
    "chatbot FIT.html"
]

for file_name in html_files:
    file_path = os.path.join(r"c:\bismillah kerja sukse\porto", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find <style>...</style> and replace
    new_content = re.sub(
        r"<style>.*?</style>",
        r'<link rel="stylesheet" href="style.css" />',
        content,
        flags=re.DOTALL
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
print("Replaced <style> with <link> in all HTML files.")
