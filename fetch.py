# -*- coding: utf-8 -*-
import requests
import os

print("Script started")  # ← tambahkan ini
SUPADATA_API_KEY = "sd_84103921b4fafaa68e174316d3858212"

videos = [
    {
        "id": "QFnBD-4OQBk",
        "title": "How to Create High-Quality AI SEO Content That Ranks",
        "date": "2025-06-12",
        "expert": "ahrefs"
    },
    {
        "id": "7XR60oB3BD8",
        "title": "Is SEO Actually Dead in 2025",
        "date": "2025-02-28",
        "expert": "ahrefs"
    },
    {
        "id": "MLKgbeDeCxU",
        "title": "What is AEO - AEO Course by Ahrefs",
        "date": "2026-04-29",
        "expert": "ahrefs"
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
        print(f"Error {response.status_code} for {video_id}: {response.text}")
        return None

def save_transcript(expert, video_id, title, date, data):
    folder = f"research/youtube-transcripts/{expert}"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{video_id}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"- **Video ID:** {video_id}\n")
        f.write(f"- **URL:** https://www.youtube.com/watch?v={video_id}\n")
        f.write(f"- **Date:** {date}\n")
        f.write(f"- **Expert:** {expert.title()}\n\n")
        f.write("---\n\n## Transcript\n\n")
        content = data.get("content", "")
        if isinstance(content, list):
            for chunk in content:
                f.write(chunk.get("text", "") + " ")
        else:
            f.write(str(content))
    print(f"✅ Saved: {filename}")

for video in videos:
    print(f"Fetching: {video['title']}...")
    data = fetch_transcript(video["id"])
    if data:
        save_transcript(
            expert=video["expert"],
            video_id=video["id"],
            title=video["title"],
            date=video["date"],
            data=data
        )

print("\nDone! Check research/youtube-transcripts/ahrefs/")