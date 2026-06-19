# Junior-Growth-Marketing-Specialist-Task - First Test

## 1. Tools Installed
In the initial phase of this assessment, I set up and configured the essential environment required:
* **Cursor**: An AI-based code editor used as the primary development software/platform in this test.
* **Claude Code Add-on**: An AI extension from Anthropic within Cursor, utilized for automating tasks and streamlining text-based analysis.
* **Codex Add-on**: An AI extension within Cursor, designed to optimize code and script-writing efficiency.
* **Git & GitHub**: Version control system used to track changes, document project progress, and host the repository, accessible through a browser and by cloning a local repository.

---

## 2. Steps Completed
The following milestones were successfully achieved during this technical test:
1. Downloaded and installed the latest version of **Cursor IDE** directly from the official website using Google Chrome.
2. Initialized the application, completed the onboarding/login process, and navigated to the Extensions marketplace to install **Claude Code** and **Codex**.
3. Created a new public GitHub repository via the web interface, naming it `Junior-Growth-Marketing-Specialist-Task`.
4. Cloned the remote repository onto my local machine and opened the workspace inside Cursor IDE.
5. Generated this `README.md` file to thoroughly document the technical steps, challenges encountered, and solutions applied.

---

## 3. Issues Encountered & Solutions

### Issue 1: UI Navigation and AI Extension Configuration
* **Problem**: As a first-time user of Cursor IDE, I needed a few moments to acclimate to its unique interface layout. While the core design is intuitive, I initially found it challenging to locate the Extensions marketplace because the application launched directly into the "Cursor Agent" interface, which features a different menu structure than the standard code editor view.
* **Solution**: After exploring the interface and cross-referencing documentation, I identified the architectural difference between the Cursor Agent window and the main Editor workspace. I realized that the Extensions menu resides within the Editor view, which can also be quickly accessed using the `Ctrl + Shift + X` shortcut on Windows. Once located, both Claude Code and Codex were successfully installed, authenticated, and verified.

### Issue 2: Local Git Environment and Repository Cloning
* **Problem**: I encountered an error when executing the `git clone` command to sync my newly created GitHub repository with my local machine. While I have frequently used GitHub in the past to download scripts and tools, I realized that the underlying Git binary was missing from my current system path, causing the cloning process to fail.
* **Solution**: I leveraged Cursor's built-in AI capabilities directly within the editor to diagnose the environment issue. Recognizing that Git had been previously uninstalled from this machine, I instructed the AI to guide me through a programmatic installation. The AI successfully executed a system installation via Windows Package Manager (`winget`) and completed the cloning process seamlessly in a single workflow.

The automated system confirmation log for this solution is captured below:
```text
The repository is cloned into your workspace.

*Note: Git was not installed on your system, so it was installed first via winget (Git 2.54.0), then the clone was run.

The repository clone completed successfully. Git was installed via winget (2.54.0) because it wasn’t available on your system, then the repo was cloned into your workspace on main at commit 92ad1a9.
