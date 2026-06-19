"""
pull_transcripts.py  (updated for youtube-transcript-api v0.7+)
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)
import os
import re

VIDEOS = {
    "eric-nowoslawski_ep02-tech-stack": "https://www.youtube.com/watch?v=7ttZEC6khZ0",
    "eric-nowoslawski_ep04-campaign-breakdowns": "https://www.youtube.com/watch?v=WmrYeN3GE3w",
    "jason-bay_perfect-outbound-pitch": "https://www.youtube.com/watch?v=IywS6oZwKq4",
    "jason-bay_cold-calling-top-20-percent": "https://www.youtube.com/watch?v=4TuHuaZe0bU",
    "josh-braun_outbound-philosophy": "https://www.youtube.com/watch?v=uT6uIAAgFGU",
    "josh-braun_non-salesy-opener": "https://www.youtube.com/watch?v=OJ2VUIlpJfQ",
    "morgan-ingram_next-level-pipeline": "https://www.youtube.com/watch?v=5NfqaBU63AI",
    "morgan-ingram_linkedin-prospecting": "https://www.youtube.com/watch?v=tdg6YBZHF8o",
    "nick-abraham_interview-cold-email": "https://www.youtube.com/watch?v=iRxyDhQ6qDA",
    "nick-abraham_1.5m-emails-per-month": "https://www.youtube.com/watch?v=POIU0L0Lsw8",
    "30mpc_cold-call-masterclass-perfect-script": "https://www.youtube.com/watch?v=2vivv2HeiBU",
    "30mpc_cold-calling-masterclass-52-min": "https://www.youtube.com/watch?v=gtKZ7fP1HZM",
}

OUTPUT_DIR = "raw_transcripts"


def extract_video_id(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError(f"Could not extract video ID from URL: {url}")
    return match.group(1)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    succeeded, failed = [], []

    # v0.7+ uses an instance, not class methods
    api = YouTubeTranscriptApi()

    for slug, url in VIDEOS.items():
        video_id = extract_video_id(url)
        try:
            transcript = api.fetch(video_id)

            # v0.7+ returns objects with .text attribute, not dicts
            full_text = " ".join(chunk.text for chunk in transcript)

            out_path = os.path.join(OUTPUT_DIR, f"{slug}.txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"Source URL: {url}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write("=" * 70 + "\n\n")
                f.write(full_text)

            print(f"OK    {slug}  ({len(full_text)} chars)")
            succeeded.append(slug)

        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            print(f"FAIL  {slug}  -> {type(e).__name__}: {e}")
            failed.append((slug, url, type(e).__name__))
        except Exception as e:
            print(f"FAIL  {slug}  -> unexpected error: {e}")
            failed.append((slug, url, str(e)))

    print("\n--- Summary ---")
    print(f"Succeeded: {len(succeeded)}/{len(VIDEOS)}")
    if failed:
        print("\nThese need manual collection via YouTube 'Show transcript' button:")
        for slug, url, reason in failed:
            print(f"  - {slug}: {url}  ({reason})")


if __name__ == "__main__":
    main()