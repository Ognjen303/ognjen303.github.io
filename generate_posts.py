import markdown
import os
import json
from datetime import datetime

def format_date(dt):
    day = dt.day
    suffix = "th" if 4 <= day <= 20 or 24 <= day <= 30 else ["st", "nd", "rd"][day % 10 - 1]
    return dt.strftime(f'{day}{suffix} %B %y')

# Set the fixed title once
title = "Greetings reader"

posts = []
posts_dir = '_posts'
output_dir = 'posts'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                html = markdown.markdown(content, extensions=['extra'])
                date = format_date(datetime.fromtimestamp(os.path.getmtime(filepath)))
                output_file = os.path.join(output_dir, f"{filename.replace('.md', '.html')}")
                output_link = output_file.replace("\\", "/")
                with open(output_file, 'w', encoding='utf-8') as out:
                    out.write(f"{html}")
                posts.append({"date": date, "link": output_link, "content": content})
                print(f"Processed: {filename}")

with open('posts.json', 'w', encoding='utf-8') as json_file:
    json.dump(posts, json_file, ensure_ascii=False, indent=4)
print("Posts saved to posts.json")
