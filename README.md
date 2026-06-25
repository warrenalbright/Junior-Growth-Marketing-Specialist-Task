# Junior-Growth-Marketing-Specialist-Task

## 1. Tools Installed
In the initial phase of this assessment, I set up and configured the essential environment required:
* **Cursor**: An AI-based code editor used as the primary development software/platform in this test.
* **Claude Code Add-on**: An AI extension from Anthropic within Cursor, utilized for automating tasks and streamlining text-based analysis.
* **Codex Add-on**: An AI extension within Cursor, designed to optimize code and script-writing efficiency.
* **Git & GitHub**: Version control system used to track changes, document project progress, and host the repository, accessible through a browser and by cloning a local repository.

---

## 2. Steps Completed
The following steps were executed during this test:
### First Test
1. Downloaded and installed the latest version of **Cursor** directly from the official website via my standard browser (Google Chrome).
2. Initialized the application, completed the onboarding/login process, and navigated to the Extensions marketplace to install **Claude Code** and **Codex** extensions.
3. Created a new public GitHub repository via the web, named `Junior-Growth-Marketing-Specialist-Task`.
4. Cloned the repository to my local computer and opened the workspace in Cursor.
5. Generated the `README.md` file to document the technical steps, challenges encountered, and solutions applied.

### Second Test — AI-Powered SEO Content Production Research
1. Created the research folder structure: `/research/sources.md`, `/research/youtube-transcripts/`, `/research/linkedin-posts/`, `/research/other/`.
2. Selected **AI-Powered SEO Content Production** as the research topic, focusing on high-signal practitioners in the SEO and GEO/AEO space.
3. Developed a Python script (`fetch.py`) to collect YouTube transcripts programmatically via the **Supadata API**, including UTF-8 encoding handling and automated paragraph formatting.
4. Identified and curated 10 expert sources based on practitioner-level insight, active content production, and relevance to AI-driven SEO workflows.
5. Collected YouTube transcripts (30 videos total) and LinkedIn posts per expert, organized by author within the repository structure.
6. Supplemented YouTube and LinkedIn data with blog articles, research studies, and interview sources stored in `/research/other/`.

---

## 3. Issues Encountered & Solutions

### Issue 1: UI Navigation and AI Extension Configuration
* **Problem**: As a first-time user of Cursor, I needed a few moments to acclimate to its unique interface layout. While the core design is quite common, like many other applications in various fields, I initially found it challenging to locate the Extensions menu since the application launched directly into the "Cursor Agent" interface, which features a quite different menu layout than the code Editor view.
* **Solution**: After exploring the interface and cross-referencing documentation for several minutes, I identified the architectural difference between the Cursor Agent window and the main Editor window. I realized that the Extensions menu resides within the *Editor* window, which can also be quickly accessed using the `Ctrl + Shift + X` shortcut on Windows. Once located, I immediately searched both Claude Code and Codex extensions, then hit the install button and performed some minor verifications, and everything installed smoothly.

### Issue 2: Local Git and Repository Cloning
* **Problem**: I encountered a slight problem / error when executing the `git clone` command to sync my newly created GitHub repository with my local computer. While I have used GitHub several times in the past for some purposes (i.e., to download programs, scripts, and tools), I realized that the underlying Git binary was missing from my current system path, causing the cloning process to fail. I forgot that I had uninstalled the Git application some time ago since I hadn't used it for a while.
* **Solution**: I leveraged the built-in AI capabilities directly within the Editor to install Git via winget and clone the repository simultaneously. The AI successfully executed a system installation via Windows Package Manager (`winget`) and completed the cloning process seamlessly in a single workflow.

#### The automated system confirmation log for this solution is captured below:
```text
The repository is cloned into your workspace.

Note: Git was not installed on your system, so it was installed first via winget (Git 2.54.0), then the clone was run.

The repository clone completed successfully. Git was installed via winget (2.54.0) because it wasn’t available on your system, then the repo was cloned into your workspace on main at commit 92ad1a9.
```

### Issue 3: Python App Execution Aliases (Windows)
* **Problem**: Running `python fetch.py` returned an error prompting installation from the Microsoft Store, despite Python 3.11 already being installed on the system.
* **Solution**: Disabled the Python App Execution Aliases via **Settings > Apps > Advanced app settings > App execution aliases**, which resolved the conflict and allowed Python to run correctly from the terminal.

### Issue 4: Script Encoding Error (UnicodeDecodeError)
* **Problem**: Running `fetch.py` produced a `UnicodeDecodeError` due to Windows defaulting to `cp1252` encoding, causing the script to fail silently on certain characters.
* **Solution**: Added `# -*- coding: utf-8 -*-` at the top of `fetch.py` to explicitly declare UTF-8 encoding, which resolved the issue immediately and allowed all transcripts to be fetched correctly.

---

## 4. Research Overview

### Topic
**AI-Powered SEO Content Production** — how practitioners are leveraging AI tools and workflows to produce, optimize, and scale SEO content in the context of B2B SaaS, with a focus on emerging disciplines such as Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO).

### Expert Selection Criteria
Experts were selected based on:
* Active content production (not just reputation or follower count)
* Practitioner-level insight grounded in real client data or product experience
* Specific focus on the AI × SEO intersection
* Mix of established voices and emerging GEO/AEO specialists

### Why These Experts

The 10 experts were selected to represent a deliberate mix of perspectives
across the AI-powered SEO content production landscape:

* **Tool builders** who ship the platforms practitioners use daily —
  Tim Soulo (Ahrefs), Michał Suski (Surfer SEO)
* **Independent consultants** with active client work —
  Aleyda Solis (Orainti, SEOFOMO), Jono Alderson (SEO Consultant & Meta), Koray Tuğberk GÜBÜR (Holistic SEO)
* **Agency founders** with documented B2B SaaS results —
  Ben Goodey (Spicy Margarita), James Dooley (PromoSEO & FatRank)
* **Content strategists** embedded in leading SEO platforms —
  Ryan Law (Ahrefs), Kevin Indig (Advisor)
* **Algorithm researchers** with enterprise-level data —
  Lily Ray (Amsive)

Each expert was verified to actively produce content grounded in real
client data, original research, or product experience — not just theory.

### Data Collection Method
* **YouTube transcripts** — collected programmatically via the [Supadata API](https://supadata.ai) using a custom Python script (`fetch.py`)
* **LinkedIn posts** — collected manually due to platform API restrictions; posts selected based on engagement and recency

---

## 5. Research Progress

| Expert | YouTube | LinkedIn | Other | Status |
|--------|---------|----------|-------|--------|
| Tim Soulo | ✅ 3 videos | ✅ 1 post | ✅ 3 resources | *Completed* |
| Aleyda Solis | ✅ 3 videos | ✅ 3 posts | ✅ 3 resources | *Completed* |
| Koray Tuğberk GÜBÜR | ✅ 3 videos | ✅ 3 posts | ✅ 2 resources | *Completed* |
| Jono Alderson | ✅ 3 videos | ✅ 3 posts | ✅ 3 resources | *Completed* |
| Michał Suski | ✅ 3 videos | ✅ 1 post | ✅ 2 resources | *Completed* |
| Kevin Indig | ✅ 3 videos | ✅ 3 posts | — | *Completed* |
| Lily Ray | ✅ 3 videos | ✅ 3 posts | — | *Completed* |
| Ben Goodey | ✅ 3 videos | ✅ 3 posts | ✅ 1 resource | *Completed* |
| Ryan Law | ✅ 3 videos | ✅ 2 posts | ✅ 2 resources | *Completed* |
| James Dooley | ✅ 3 videos | ✅ 1 post | ✅ 1 resource | *Completed* |

---
