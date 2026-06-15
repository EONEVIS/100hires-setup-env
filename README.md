# 100Hires Tool Setup & Evaluation Log
 
This repository tracks my step-by-step process for setting up the local environment and tools required for the 100Hires Junior Growth Marketer evaluation.
 
---
 
## 🛠️ Tools & Extensions Installed
 
* **Cursor IDE**: Installed the core code editor via the newer Cursor Agents launcher hub.
* **Claude Code Extension**: Installed the official Anthropic extension (`anthropic.com`) to connect to my Anthropic profile.
* **Codex Extension**: Installed the official OpenAI extension (`openai.com`) to connect to my ChatGPT account.
* **GitHub**: Set up a public repository to handle version control using terminal commands.
 
---
 
## 🚀 Steps Completed
 
1. **Downloaded Cursor**: Went to `cursor.com` and ran the installer. It initialized the unified Cursor Agents window first.
2. **Opened the Editor**: Navigated into the primary code editor window from the main dashboard.
3. **Installed Extensions**: Found, verified, and installed both the authentic Claude Code and Codex plugins.
4. **Logged In**: Used online guides to open the terminal panels and successfully link both extensions to my primary accounts.
5. **Set Up GitHub**: Created a public repository named `100hires-setup-env` on my GitHub account (`EONEVIS`) and cloned it to my laptop using the Cursor terminal.
6. **Wrote Documentation**: Drafted this `README.md` file to track the setup history.
7. **Pushed Code Live**: Used Git commands in the terminal to save my progress and upload the files to the web.
 
---
 
## 🔍 Issues Found & Fixed
 
### 1. The 'Cursor Agents' Layout
* **Issue**: Clicking download on the website gave me the updated "Cursor Agents" launcher rather than a standard, basic code editor window. This made the standard extensions tab hard to find at first.
* **Resolution**: I searched online and found out that clicking the **Editor Window** on the top right opens the Cursor IDE. I did that, and it instantly opened the classic Cursor IDE workspace.
 
### 2. Finding the Extension Login Button
* **Issue**: After installing Claude Code and Codex, there wasn't a clear, obvious "Login" button on the screen to link my accounts. 
* **Resolution**: I jumped on YouTube and found a 2026 video tutorial titled *"How to Add Claude Code in Cursor"* (https://www.youtube.com/watch?v=4L2DNpq8ufE). It showed me how to use the shortcut commands to open the Claude Interface, so I did it and logged in using my Anthropic Account. I faced the same issue for Codex, so I applied the same solution—it worked perfectly, allowing me to open the interface and successfully log in using ChatGPT.
 
### 3. Terminal Setup and Cloning the Project
* **Issue**: I needed to quickly link my remote GitHub setup to my local laptop project folder.
* **Resolution**: I took the help of Gemini (since I have the Pro plan), which gave me the exact steps: *"On your new GitHub repository page, click the green Code button and copy the HTTPS link. Open your Cursor IDE window, open the terminal (Ctrl + ~ or Cmd + ~), navigate to your preferred workspace folder, and clone it by typing: `git clone https://github.com/EONEVIS/100hires-setup-env.git`"*. After getting it done, I opened the local project and created this `README.md`.
 
### 4. Saving and Uploading via the Command Line
* **Issue**: I needed to register my local file changes and upload them to the cloud repository using the proper terminal sequence. Additionally, during my first commit attempt, Git threw a fatal security error (`Author identity unknown`) because my global user profile wasn't configured on this machine yet.
* **Resolution**: Instead of guessing the command strings or setup parameters, I consulted Gemini AI. It mapped out the initial configuration commands to stamp my credentials onto Git, followed by the standard deployment sequence. I ran these lines directly in the Cursor terminal to clear the error and push the project live to GitHub:
  ```bash
  # Fixing the identity error
  git config --global user.email "elijahnevis@gmailcom"
  git config --global user.name "EONEVIS"

  # Deploying the files
  git add README.md
  git commit -m "Final project setup markdown log complete"
  git push origin main

  Programmatic B2B Outbound Research Project (Phase 2)
This workspace contains research assets analyzing modern programmatic outbound architectures for B2B SaaS.  

Why I Chose Programmatic B2B Cold Outreach
B2B outbound customer acquisition has shifted from generic volume blasting to a technical data pipeline. Success in 2026 relies on strict deliverability physics (horizontal sending setup, DNS authentication, and removing tracking pixels) paired with automated intent triggers (such as technographic changes or hiring signals).  

Repository Directory Map
/research/sources.md: A curated index of 10 industry practitioners (e.g., Jesse Ouellette, Nick Abraham, Mark Colgan, and AJ Cassata) who build real GTM pipelines, including links and annotations .

/research/linkedin-posts/: Scraped copy templates showing actual practitioner engagement and copy structures for deliverability (Jesse Ouellette) and CTAs (AJ Cassata).  

/research/youtube-transcripts/: Real transcripts fetched from expert YouTube channels to detail simplified, high-impact data enrichment workflows.  

/research/other/: Custom code scripts (Python with the Supadata API and JavaScript with the ScrapeCreators API) demonstrating how to programmatically extract structured context from the web.  

Completed and logged by Elijah.