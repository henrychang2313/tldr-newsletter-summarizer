# tldr-newsletter-summarizer

This project pulls recent emails from a Gmail inbox, cleans and consolidates newsletter content into a single markdown file, and then uses a local LLM through Ollama to turn that content into a daily blog-style summary.

The idea was simple: instead of reading several newsletters one by one, build a pipeline that collects everything, removes the noise, and produces one coherent write-up of what actually mattered.

## What it does

- Connects to Gmail and fetches recent emails
- Extracts newsletter content from email bodies
- Converts HTML emails into readable text
- Removes common newsletter clutter like sponsor sections, footers, and link dumps
- Writes everything into a single markdown file
- Uses a local LLM through Ollama to read that markdown file
- Generates a blog-style summary with:
  - major headlines
  - companies worth watching
  - recurring themes
  - forward-looking takeaways

## Project flow

```text
Gmail inbox
  -> fetch_emails.py
  -> parser.py
  -> cleaner.py
  -> markdown_writer.py
  -> newsletters_last_2_days.md
  -> llm_client.py
  -> blog-style output
````

## Tech stack

* Python
* Gmail IMAP
* BeautifulSoup
* Ollama
* OpenAI Python SDK
* python-dotenv

This project runs locally and does not require paid model APIs.

## Project structure

```text
newsletter-summaries/
├── fetch_emails.py
├── parser.py
├── cleaner.py
├── markdown_writer.py
├── llm_client.py
├── config.py
├── .env
├── requirements.txt
└── data/
    └── newsletters_last_2_days.md
```

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Gmail setup

This project uses Gmail through IMAP.

In your `.env` file, set:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
IMAP_SERVER=imap.gmail.com
```

Use a Gmail App Password here, not your normal Gmail password.

## Ollama setup

Install Ollama locally, then start the server:

```bash
ollama serve
```

Pull the model you want to use:

```bash
ollama pull llama3.2
```

Then set the following in `.env`:

```env
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.2
OLLAMA_API_KEY=ollama
OUTPUT_MARKDOWN=./data/newsletters_last_2_days.md
```

## Running the project

### Step 1: Fetch emails and build the markdown file

```bash
python3 fetch_emails.py
```

This writes newsletter content into:

```text
./data/newsletters_last_2_days.md
```

### Step 2: Generate the blog summary

```bash
python3 llm_client.py
```

This reads the markdown file and generates a blog-style summary in the terminal.

## Why this project is useful

The interesting part is that the model is not just summarizing one email at a time. It looks across the full markdown context and tries to piece together the bigger picture.

That makes it better at spotting:

* overlapping stories across newsletters
* recurring companies and themes
* larger shifts in AI, finance, infrastructure, and markets
* signals that are easy to miss when reading each email separately

The result feels closer to a daily briefing than a simple summary.

## Current limitations

* Right now the project loads the full markdown file into the model context

  * that works well for one or two days of newsletters
  * it would need chunking or retrieval later for larger archives

* Newsletter filtering is still fairly simple

  * some senders and layouts may need custom cleanup rules

* Output is currently generated as one long-form blog post

  * this could be expanded into separate outputs like headlines, companies, and themes

* There is no frontend yet

  * everything runs from local scripts for now

## Future improvements

A few obvious next steps:

* wrap the pipeline in FastAPI
* create separate endpoints for headlines, companies, and trends
* support multiple newsletter sources
* add historical trend tracking
* add vector search or RAG for longer time windows
* build a simple frontend or dashboard

## Why local

This project was designed to run locally for two reasons:

1. no API costs
2. email content stays on your machine

That made Ollama a good fit for the first version.

## Summary

This started as a small automation project and turned into a lightweight local intelligence pipeline:

* Gmail inbox ingestion
* newsletter parsing and cleanup
* markdown consolidation
* local LLM synthesis

It is still simple, but it already solves a real problem: turning a pile of newsletter emails into one readable daily summary.

```
```
