---
name: yt-search
description: Search YouTube for videos on a topic. Returns title, URL, channel, views, duration, and upload date for each result. Use this when the user asks to find YouTube videos, research a topic on YouTube, or needs video URLs to send to NotebookLM.
argument-hint: "<query> [count]"
allowed-tools: Bash
---

Search YouTube for: $ARGUMENTS

## Instructions

Run the yt_search.py script located at:
`/Users/user/Documents/chaseai/yt-research/yt_search.py`

Use the venv Python interpreter:
`/Users/user/Documents/chaseai/yt-research/.venv/bin/python`

Parse the first argument as the search query and the optional second argument as the result count (default: 10).

### Command format:
```
/Users/user/Documents/chaseai/yt-research/.venv/bin/python \
  /Users/user/Documents/chaseai/yt-research/yt_search.py \
  "<query>" <count>
```

### After running:
1. Display results in a clear table with: title, channel, views, duration, URL
2. Summarize what you found (e.g. "Found 10 videos, most popular is X with 500k views")
3. Ask if the user wants to send these URLs to NotebookLM for analysis
