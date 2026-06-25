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
    # Kevin Indig
    {
        "id": "p3_P0dDspBI",
        "title": "The Great Decoupling - SEO Attribution and AI-Driven Growth Strategies",
        "filename": "01. The-Great-Decoupling-SEO-Attribution-and-AI-Driven-Growth-Strategies",
        "date": "2026-04-23",
        "expert": "Kevin Indig"
    },
    {
        "id": "AqAoKGftsSE",
        "title": "Moving Beyond Old SEO Models in the Age of AI",
        "filename": "02. Moving-Beyond-Old-SEO-Models-in-the-Age-of-AI",
        "date": "2026-01-19",
        "expert": "Kevin Indig"
    },
    {
        "id": "m00bYt1eIQY",
        "title": "SEO Has Changed Forever. What Marketers Need to Know Now",
        "filename": "03. SEO-Has-Changed-Forever-What-Marketers-Need-to-Know-Now",
        "date": "2025-07-10",
        "expert": "Kevin Indig"
    },
    # Lily Ray
    {
        "id": "2nJkT8zOzcM",
        "title": "GEO, AEO, LLMO - Separating Fact from Fiction and How to Win in AI Search",
        "filename": "01. GEO-AEO-LLMO-Separating-Fact-from-Fiction-and-How-to-Win-in-AI-Search",
        "date": "2025-11-11",
        "expert": "Lily Ray"
    },
    {
        "id": "2htSIT0HLjs",
        "title": "The Future of SEO - Google Updates, AI Search and GEO Spam",
        "filename": "02. The-Future-of-SEO-Google-Updates-AI-Search-and-GEO-Spam",
        "date": "2026-03-18",
        "expert": "Lily Ray"
    },
    {
        "id": "DKAGf2lk488",
        "title": "Lily Ray on AI Slop, GEO, and What Actually Works",
        "filename": "03. Lily-Ray-on-AI-Slop-GEO-and-What-Actually-Works",
        "date": "2026-05-13",
        "expert": "Lily Ray"
    },
    # Ben Goodey - Spicy Margarita
    {
        "id": "Z4pdquy2Opg",
        "title": "SEO Strategies That Make Money",
        "filename": "01. SEO-Strategies-That-Make-Money",
        "date": "2025-11-24",
        "expert": "Ben Goodey"
    },
    {
        "id": "_m6Kc6_4WYE",
        "title": "Agency Building and SEO with Ben Goodey",
        "filename": "02. Agency-Building-and-SEO-with-Ben-Goodey",
        "date": "2025-06-06",
        "expert": "Ben Goodey"
    },
    {
        "id": "-biKd8XOVk4",
        "title": "Successful SEO Programs - The SaaS SEO Show",
        "filename": "03. Successful-SEO-Programs-The-SaaS-SEO-Show",
        "date": "2023-11-09",
        "expert": "Ben Goodey"
    },
    # Ryan Law - Ahrefs
    {
        "id": "iVZrVeESnFQ",
        "title": "How to Automate Blog Writing with AI from Keyword to Published",
        "filename": "01. How-to-Automate-Blog-Writing-with-AI-from-Keyword-to-Published",
        "date": "2026-04-28",
        "expert": "Ryan Law"
    },
    {
        "id": "mL1W1SMtTT4",
        "title": "How to Win in AI Search - Real Data No Hype",
        "filename": "02. How-to-Win-in-AI-Search-Real-Data-No-Hype",
        "date": "2025-10-28",
        "expert": "Ryan Law"
    },
    {
        "id": "D7LBx8RFOcQ",
        "title": "AI Writing at Scale: Ahrefs Step-by-Step Workflow | Ryan Law (Ahrefs)",
        "filename": "03. AI-Writing-at-Scale-Ahrefs-Step-by-Step-Workflow-Ryan-Law",
        "date": "2025-08-05",
        "expert": "Ryan Law"
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
    if video["expert"] in ["Ahrefs","Aleyda Solis","Koray Tugberk GUBUR","Kyle Roof","Michal Suski","Kevin Indig","Lily Ray","Ben Goodey","Ryan Law"]:
        print(f"Skipping (already collected): {video['title']}")
        continue
    print(f"Fetching: {video['title']}...")
    data = fetch_transcript(video["id"])
    if data:
        save_transcript(video, data)
    print()

print("\nDone!")