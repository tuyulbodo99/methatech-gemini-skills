# Mode 1 — Web Scraper Builder

## Stack priority
1. Plain HTTP requests first (`requests`, `httpx`, `curl`).
2. HTML/JSON parser (`beautifulsoup4`, `lxml`, `jq`).
3. Browser automation only when JS rendering is unavoidable.

## Requirements per scraper
- Pagination handling, retry with backoff, timeouts on every request.
- Conservative rate limiting (default ≥1s between requests unless the site allows more).
- Respect `robots.txt`, Terms of Service, and site rate limits.
- If the site offers an official API → use it instead of scraping HTML.
- Never attempt to bypass CAPTCHA, login walls, or access-control mechanisms.

## Project layout
```
project/
├── README.md
├── requirements.txt / package.json
├── config.example.json
├── src/
│   ├── scraper.py
│   ├── parser.py
│   └── exporter.py
├── tests/
└── output/
```

## Output formats
JSON, JSONL, CSV, or SQLite — pick one primary, keep the exporter modular so others are trivial to add.

## Test matrix (minimum)
HTTP 200 / 404 / 429 / 500, network timeout, pagination across ≥2 pages, duplicate-data dedup, empty response, malformed HTML/JSON.
