#!/usr/bin/env python3
"""
YouTube search script using yt-dlp.
Returns video metadata: title, URL, views, channel, duration, upload date.

Usage:
    python yt_search.py "query" [count]

Examples:
    python yt_search.py "claude code skills" 20
    python yt_search.py "notebooklm tutorial" 10
"""

import json
import sys
from datetime import datetime

import yt_dlp


def search_youtube(query: str, count: int = 10) -> list[dict]:
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }

    results = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_url = f"ytsearch{count}:{query}"
        info = ydl.extract_info(search_url, download=False)

        for entry in info.get("entries", []):
            if not entry:
                continue

            duration_sec = entry.get("duration") or 0
            minutes, seconds = divmod(int(duration_sec), 60)
            hours, minutes = divmod(minutes, 60)
            if hours:
                duration_fmt = f"{hours}:{minutes:02d}:{seconds:02d}"
            else:
                duration_fmt = f"{minutes}:{seconds:02d}"

            upload_date = entry.get("upload_date") or ""
            if upload_date:
                try:
                    upload_date = datetime.strptime(upload_date, "%Y%m%d").strftime("%Y-%m-%d")
                except ValueError:
                    pass

            results.append({
                "title": entry.get("title", ""),
                "url": f"https://www.youtube.com/watch?v={entry.get('id', '')}",
                "channel": entry.get("channel") or entry.get("uploader", ""),
                "views": entry.get("view_count") or 0,
                "duration": duration_fmt,
                "upload_date": upload_date,
            })

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python yt_search.py <query> [count]", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    results = search_youtube(query, count)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
