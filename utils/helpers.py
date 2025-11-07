import os
from datetime import datetime

def save_story(story_text):
    os.makedirs("outputs/stories", exist_ok=True)
    filename = datetime.now().strftime("story_%Y%m%d_%H%M%S.txt")
    path = os.path.join("outputs/stories", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(story_text)
    return path
