# 🤖 Multi-Agent Blog Post Generator

A system where **4 AI agents work together** to automatically write a full blog post for you — just give it a topic and it does the rest.

---

## What Does This Actually Do?

You type a topic like `"benefits of drinking water"` and the system:

1. **Researches** the topic (finds key facts and angles)
2. **Plans** a structure (creates a blog outline)
3. **Writes** the full blog post
4. **Reviews** and polishes it

Then saves the finished blog post as a `.txt` file on your computer.

That's it. You give a topic, you get a blog post.

---

## What is a "Multi-Agent System"?

Think of it like hiring a small team:

| Person | Job |
|--------|-----|
| 🔍 Researcher | Goes and finds information about your topic |
| 📋 Planner | Organizes that info into a logical structure |
| ✍️ Writer | Actually writes the blog post |
| 🔎 Editor | Reads the draft and makes it better |

In this system, each "person" is an **AI agent** — a Python function that sends a task to an AI model (Groq's LLaMA 3.1) and gets back a result. Each agent does its job, then passes the result to the next one.

---

## What Are the Libraries Used?

You don't need to deeply understand these, but here's a plain-English explanation:

| Library | What it does | Think of it as... |
|---------|-------------|-------------------|
| **LangChain** | Talks to the AI model for you | A translator between your Python code and the AI |
| **LangGraph** | Controls the order agents run in | A traffic controller that says "researcher goes first, then outliner..." |
| **Groq API** | The actual AI brain (LLaMA 3.1) | The AI that reads your prompts and writes responses |
| **python-dotenv** | Loads your API key from a file | Keeps your secret key out of your code |

---

## How the Data Flows

```
You type a topic
       ↓
Agent 1 🔍 Researcher
  → Reads: your topic
  → Writes: research notes (key facts, subtopics, audience info)
       ↓
Agent 2 📋 Outliner
  → Reads: research notes
  → Writes: blog outline (title, sections, what to cover)
       ↓
Agent 3 ✍️ Writer
  → Reads: research notes + outline
  → Writes: full blog post draft (800–1200 words)
       ↓
Agent 4 🔎 Reviewer
  → Reads: draft
  → Writes: polished final version + review notes
       ↓
Saved to a .txt file on your computer
```

All 4 agents share a common "state" — like a shared Google Doc. Each agent reads what the previous one wrote and adds its own output.

---

## Project Structure

```
multi-agent-system/
│
├── backend/                        ← All the Python code (this is what you run)
│   │
│   ├── multi_agent_system.py       ← START HERE — run this file
│   │
│   ├── agents/                     ← The 4 AI agents
│   │   ├── researcher.py           ← Agent 1: researches the topic
│   │   ├── outliner.py             ← Agent 2: creates the outline
│   │   ├── writer.py               ← Agent 3: writes the blog post
│   │   └── reviewer.py             ← Agent 4: reviews and polishes
│   │
│   ├── graph/
│   │   ├── state.py                ← The shared "whiteboard" all agents read/write
│   │   └── workflow.py             ← Connects the agents in order (1→2→3→4)
│   │
│   ├── utils/
│   │   ├── prompts.py              ← The instructions given to each AI agent
│   │   └── config.py               ← Loads your API key and settings
│   │
│   ├── requirements.txt            ← Python packages to install
│   ├── .env.example                ← Template for your API key file
│   └── .env                        ← Your actual API key (you create this)
│
└── frontend/                       ← Optional React UI (not required to run)
```

---

## Setup & Running (Step by Step)

### Step 1 — Get a free Groq API key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free (no credit card needed)
3. Click **API Keys** → **Create API Key**
4. Copy the key (it starts with `gsk_...`)

### Step 2 — Install Python packages

Open your terminal, navigate to the backend folder, and run:

```bash
cd multi-agent-system/backend
pip install -r requirements.txt
```

### Step 3 — Create your `.env` file

```bash
cp .env.example .env
```

Open the new `.env` file and replace the placeholder with your real key:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

### Step 4 — Run it

```bash
python multi_agent_system.py
```

### Step 5 — Enter a topic

```
Enter your blog topic: how to stay focused while studying
```

Then wait ~30–60 seconds while the 4 agents do their work. You'll see live progress printed in the terminal.

---

## What You'll See in the Terminal

```
🔍 AGENT 1: TOPIC RESEARCHER - Starting...
   ✅ Research complete!

📋 AGENT 2: CONTENT OUTLINER - Starting...
   ✅ Outline created!

✍️  AGENT 3: CONTENT WRITER - Starting...
   ✅ Draft written! Word count: ~950 words

🔎 AGENT 4: QUALITY REVIEWER - Starting...
   ✅ Review complete!
   🎉 Blog post is ready!

💾 Blog post saved to: blog_post_how_to_stay_focused_2025-04-24.txt
```

---

## Common Questions

**Q: Do I need to pay for anything?**
No. Groq's API is free with generous rate limits. LLaMA 3.1 is free to use via Groq.

**Q: Where does the blog post get saved?**
In the same folder where you ran the command (`multi-agent-system/backend/`), as a `.txt` file.

**Q: Can I change the topic?**
Yes — every time you run the program it asks you for a new topic. You can also run it again and type a different one.

**Q: What if I get an API error?**
Make sure your `.env` file has the correct `GROQ_API_KEY` and that you copied it correctly from the Groq console.

**Q: What is the frontend folder for?**
It's an optional React UI that shows the agent progress visually. You don't need it — the backend works perfectly on its own from the terminal.

---

## Tech Stack

- **Python 3.9+**
- **LangChain** — AI model integration
- **LangGraph** — Multi-agent workflow orchestration
- **Groq API + LLaMA 3.1** — The AI model (free)
- **React + Vite** — Optional frontend UI
