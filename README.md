# Web Scraper

Scrapes any webpage and returns its content as clean Markdown using the Firecrawl API.

## Requirements

```bash
pip install firecrawl-py
```

## Setup

Replace `"Your API Key"` in `Web_Scrapper.py` with your actual Firecrawl API key.

Get one at: https://www.firecrawl.dev

## Usage

```bash
python Web_Scrapper.py
```

Prompts for a URL, then prints the first 1000 characters of the scraped Markdown content.

## Example

```
Enter your Sitelink: https://example.com
# Example Domain
This domain is for use in illustrative examples...
```

## Notes

- Output is truncated to 1000 characters in the print statement — remove `[:1000]` to get full content
- Returns error message string on failure instead of raising
