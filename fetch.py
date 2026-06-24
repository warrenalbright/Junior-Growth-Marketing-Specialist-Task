# -*- coding: utf-8 -*-
import requests
import os
import re

SUPADATA_API_KEY = "sd_84103921b4fafaa68e174316d3858212"

videos = [
    # Ahrefs / Tim Soulo
    {
        "id": "QFnBD-4OQBk",
        "title": "How to Create High-Quality AI SEO Content That Ranks",
        "filename": "01-How-to-Create-High-Quality-AI-SEO-Content-That-Ranks",
        "date": "2025-06-12",
        "expert": "Ahrefs"
    },
    {
        "id": "7XR60oB3BD8",
        "title": "Is SEO Actually Dead in 2025?",
        "filename": "02-Is-SEO-Actually-Dead-in-2025",
        "date": "2025-02-28",
        "expert": "Ahrefs"
    },
    {
        "id": "MLKgbeDeCxU",
        "title": "What is AEO - AEO Course by Ahrefs",
        "filename": "03-What-is-AEO-AEO-Course-by-Ahrefs",
        "date": "2026-04-29",
        "expert": "Ahrefs"
    },
    # Aleyda Solis - Crawling Mondays
    {
        "id": "BjyF_4UhoOM",
        "title": "The AI Search Optimization Roadmap",
        "filename": "01-The-AI-Search-Optimization-Roadmap",
        "date": "2025-09-09",
        "expert": "Aleyda Solis"
    },
    {
        "id": "LGvbEHyX5oE",
        "title": "Google AI Mode vs Traditional Search",
        "filename": "02-Google-AI-Mode-vs-Traditional-Search",
        "date": "2025-07-01",
        "expert": "Aleyda Solis"
    },
    {
        "id": "4YZ9SFWSK90",
        "title": "Why Topic Clusters Matter More Than Ever in AI Search",
        "filename": "03-Why-Topic-Clusters-Matter-More-Than-Ever-in-AI-Search",
        "date": "2025-08-11",
        "expert": "Aleyda Solis"
    },
]

def fetch_transcript(video_id):
    url = "https://api.supadata.ai/v1/youtube/transcript"
    headers = {"x-api-key": SUPADATA_API_KEY}
    params = {"videoId": video_id, "text": True}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"  Error {response.status_code}: {response.text}")
        return None

def format_transcript(raw_text):
    """Format raw transcript into readable paragraphs."""
    text = raw_text.strip()
    if text:
        text = text[0].upper() + text[1:]
    sentences = re.split(r'(?<=[.!?])\s+', text)
    paragraphs = []
    chunk = []
    for i, sentence in enumerate(sentences):
        chunk.append(sentence.strip())
        if (i + 1) % 4 == 0:
            paragraphs.append(' '.join(chunk))
            chunk = []
    if chunk:
        paragraphs.append(' '.join(chunk))
    return '\n\n'.join(paragraphs)

def save_transcript(video, data):
    expert = video["expert"]
    video_id = video["id"]
    title = video["title"]
    date = video["date"]
    filename = video["filename"]

    folder_name = expert.lower().replace(' ', '-')
    folder = f"research/youtube-transcripts/{folder_name}"
    os.makedirs(folder, exist_ok=True)
    filepath = f"{folder}/{filename}.md"

    content = data.get("content", "")
    if isinstance(content, list):
        raw_text = ' '.join(chunk.get("text", "") for chunk in content)
    else:
        raw_text = str(content)

    formatted = format_transcript(raw_text)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"* **Expert:** {expert}\n")
        f.write(f"* **Video ID:** {video_id}\n")
        f.write(f"* **URL:** https://www.youtube.com/watch?v={video_id}\n")
        f.write(f"* **Date Published:** {date}\n\n")
        f.write("---\n\n")
        f.write("## Transcript\n\n")
        f.write(formatted)

    print(f"  Saved: {filepath}")

# Run
print("Starting transcript fetch...\n")
for video in videos:
    if video["expert"] == "Ahrefs":
        print(f"Skipping (already collected): {video['title']}")
        continue
    print(f"Fetching: {video['title']}...")
    data = fetch_transcript(video["id"])
    if data:
        save_transcript(video, data)
    print()

print("\nDone!")