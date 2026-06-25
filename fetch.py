# -*- coding: utf-8 -*-
import requests
import os
import re
from dotenv import load_dotenv

load_dotenv("API.env")

SUPADATA_API_KEY = os.getenv("SUPADATA_API_KEY")

videos = [
    # Ahrefs / Tim Soulo
    {
        "id": "QFnBD-4OQBk",
        "title": "How to Create High-Quality AI SEO Content That Ranks",
        "filename": "01. How-to-Create-High-Quality-AI-SEO-Content-That-Ranks",
        "date": "2025-06-12",
        "expert": "Ahrefs"
    },
    {
        "id": "7XR60oB3BD8",
        "title": "Is SEO Actually Dead in 2025?",
        "filename": "02. Is-SEO-Actually-Dead-in-2025",
        "date": "2025-02-28",
        "expert": "Ahrefs"
    },
    {
        "id": "MLKgbeDeCxU",
        "title": "What is AEO - AEO Course by Ahrefs",
        "filename": "03. What-is-AEO-AEO-Course-by-Ahrefs",
        "date": "2026-04-29",
        "expert": "Ahrefs"
    },
    # Aleyda Solis - Crawling Mondays
    {
        "id": "BjyF_4UhoOM",
        "title": "The AI Search Optimization Roadmap",
        "filename": "01. The-AI-Search-Optimization-Roadmap",
        "date": "2025-09-09",
        "expert": "Aleyda Solis"
    },
    {
        "id": "LGvbEHyX5oE",
        "title": "Google AI Mode vs Traditional Search",
        "filename": "02. Google-AI-Mode-vs-Traditional-Search",
        "date": "2025-07-01",
        "expert": "Aleyda Solis"
    },
    {
        "id": "T9d4GOCpBIE",
        "title": "SEO for LLMs - Adapting to the AI-first Web",
        "filename": "03. SEO-for-LLMs-Adapting-to-the-AI-first-Web",
        "date": "2025-05-22",
        "expert": "Aleyda Solis"
    },
    # Koray Tuğberk GÜBÜR
    {
        "id": "mSHq_HxOyTA",
        "title": "AI Agents, Semantic SEO and Fortune 500 Secrets - Full Interview",
        "filename": "01. AI-Agents-Semantic-SEO-and-Fortune-500-Secrets",
        "date": "2026-02-05",
        "expert": "Koray Tugberk GUBUR"
    },
    {
        "id": "5PAoIhyalsg",
        "title": "Technical SEO and Semantic SEO Deep Dive",
        "filename": "02. Technical-SEO-and-Semantic-SEO-Deep-Dive",
        "date": "2024-11-04",
        "expert": "Koray Tugberk GUBUR"
    },
    {
        "id": "XlKMWAc0qvM",
        "title": "Advanced SEO Tips 2025",
        "filename": "03. Advanced-SEO-Tips-2025",
        "date": "2025-03-08",
        "expert": "Koray Tugberk GUBUR"
    },
    # Kyle Roof - PageOptimizer Pro
    {
        "id": "CdfYQnE81sw",
        "title": "He Tested 750 SEO Factors - Most of Them Don't Matter",
        "filename": "01. He-Tested-750-SEO-Factors-Most-of-Them-Dont-Matter",
        "date": "2025-07-23",
        "expert": "Kyle Roof"
    },
    {
        "id": "d6kCZvu4jPs",
        "title": "Think SEO Is Dead - Here's Why It's Just Getting Started",
        "filename": "02. Think-SEO-Is-Dead-Here's-Why-Its-Just-Getting-Started",
        "date": "2025-07-03",
        "expert": "Kyle Roof"
    },
    {
        "id": "eWEx2lA6QOM",
        "title": "Mastering On-Page SEO - Kyle Roof Shares The Secrets You're Missing",
        "filename": "03. Mastering-On-Page-SEO-Kyle-Roof-Shares-The-Secrets-You're-Missing",
        "date": "2025-08-26",
        "expert": "Kyle Roof"
    },
    # Michał Suski - Surfer SEO
    {
        "id": "x5CgYCRLgbc",
        "title": "Product-Led SEO in AI Era with Eli Schwartz",
        "filename": "01. Product-Led-SEO-in-AI-Era-with-Eli-Schwartz",
        "date": "2026-04-28",
        "expert": "Michal Suski"
    },
    {
        "id": "OOepA6XL_-s",
        "title": "Learn How to Optimize for AI Search - Live Surfer Demo",
        "filename": "02. Learn-How-to-Optimize-for-AI-Search-Live-Surfer-Demo",
        "date": "2025-10-29",
        "expert": "Michal Suski"
    },
    {
        "id": "tgiBcdDgDz8",
        "title": "SEO 2024 and Beyond - Strategies, Google Updates, and Surfer's Newest Tools",
        "filename": "03. SEO-2024-and-Beyond-Strategies-Google-Updates-and-Surfers-Newest-Tools",
        "date": "2024-05-28",
        "expert": "Michal Suski"
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

    folder_name = expert
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
    if video["expert"] in ["Ahrefs","Aleyda Solis","Koray Tugberk GUBUR","Kyle Roof","Michal Suski"]:
        print(f"Skipping (already collected): {video['title']}")
        continue
    print(f"Fetching: {video['title']}...")
    data = fetch_transcript(video["id"])
    if data:
        save_transcript(video, data)
    print()

print("\nDone!")