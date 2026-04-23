[Skip to content](#main)
[hermes atlas](/)

apr·2026 93·repos hermes·v0.10.0

[map](/)/handbook

beginner's guide · the hermes handbook

# Hermes Agent: The Complete Beginner's Guide (Apr 2026)

Install, pick a model, ship your first workflow, understand the learning loop — with the best community tool for every step.

By [Kevin Simback](https://x.com/ksimback) · Hermes Atlas maintainer · Updated 2026-04-20 · ~18 min read

> Based on 93 ecosystem projects reviewed, 33 research sources, and the live GitHub repo. Updated monthly.

## Table of contents

1. [What Hermes Agent actually is](#1-what-hermes-agent-actually-is)
2. [Who Hermes is for](#2-who-hermes-is-for)
3. [How it's different (vs Claude Code, Cursor, OpenClaw)](#3-how-its-different)
4. [Install in 2 minutes](#4-install-in-2-minutes)
5. [Pick your model (the first-weekend mistake)](#5-pick-your-model)
6. [Your first workflow](#6-your-first-workflow)
7. [The learning loop](#7-the-learning-loop)
8. [Essential skills to install first](#8-essential-skills-to-install-first)
9. [Where to go next](#9-where-to-go-next)
10. [FAQ](#10-faq)

---

## 1. What Hermes Agent actually is

**Hermes Agent is an open-source AI agent by [Nous Research](https://nousresearch.com) that runs on your own machine or a cheap VPS, remembers what it learns across sessions, and writes its own reusable skills as it works. It talks to you through a CLI, Telegram, Discord, email, and many other messaging providers. It hit 104,791 GitHub stars (as of 2026-04-20), and it's the fastest-growing open-source agent of 2026.**

### The 30-second version

You install Hermes with one curl command. You pick a model provider (many popular options) and a model (Claude, GPT-5.4, GLM-5.1, MiniMax, or even a local Ollama model). You give it a job — "summarize my GitHub notifications every morning at 8am," or "help me debug this Python script," or "watch this website and ping me on Telegram when the price drops."

It runs. It learns. A week later, the same job produces tighter output because Hermes has been quietly writing skills — little markdown files that capture what worked — and pulling them into future runs.

That's the whole product. Install, assign tasks, and let it compound.

### The 2-minute version

Most AI tools are stateless: you open a chat, ask a question, close the tab, and the next session starts from zero. Hermes inverts that. It lives on a personal computer or virtual private server. It has persistent memory. It creates skills — procedures it can reuse — every time it figures something out. And it reaches you through whatever channel you prefer: a terminal, a Telegram bot, a scheduled cron job, a webhook.

The big architectural bet is **Harness Engineering**: Nous believes the real unlock in 2026 isn't a smarter model, it's a smarter wrapper around the model. So Hermes invests heavily in five layers around the LLM — instructions, constraints, feedback, memory, orchestration — and lets you swap the model itself. Frontier today, local tomorrow, something else next year.

You'll hear people call this "the agent that grows with you." That's Nous's tagline and it's also a useful mental model: on day one Hermes is a generic assistant. On day thirty it's *your* assistant, with thirty days of learned preferences baked in.

### Preview: the learning loop

Every few tool calls, Hermes pauses and asks itself: *what just happened, what worked, what failed, should this become a skill?* When the answer is yes, it writes a skill file to `~/.hermes/skills/` and uses it going forward. These skills are plain markdown. You can read them, edit them, or delete the ones it got wrong.

This is the single feature that matters most and the one we'll unpack in [chapter 7](#7-the-learning-loop).

---

## 2. Who Hermes is for

Hermes attracts three kinds of people. Figure out which one you are and the rest of the handbook makes more sense.

### The CLI coder

You live in a terminal. You already use Claude Code or Cursor for in-editor coding. You want an agent that sits *outside* your editor — something you can ask to "audit the repo for dead code" or "write a migration plan for our 0.9 → 0.10 upgrade" without leaving the CLI.

**What you'll use first:** the `hermes` CLI, skills, memory. **Ignore for now:** Telegram, cron, multi-agent.

### The automation operator

You don't necessarily code. You want an agent that does recurring jobs — summarize news, watch markets, generate reports, triage your inbox — while you sleep. You'll host Hermes on a Mac Mini or $5 VPS and wire it to whatever channels you use.

**What you'll use first:** cron, messaging gateways, memory. **Ignore for now:** code execution, multi-agent.

### The Telegram-bot operator

You want an always-on agent you can message from your phone. Travel, meetings, gym — doesn't matter, you ping Hermes and it responds. The Telegram integration is the killer feature here.

**What you'll use first:** the messaging gateway, voice, skills. **Ignore for now

[Content truncated — showing first 5,000 of 24,787 chars. LLM summarization timed out. To fix: increase auxiliary.web_extract.timeout in config.yaml, or use a faster auxiliary model. Use browser_navigate for the full page.]