# Web Scrapper

Scrapes a webpage and returns its content as clean markdown using Firecrawl.

## Setup

```
pip install firecrawl-py
```

Requires a Firecrawl API key (get one at firecrawl.dev).

## Usage

```
python Web_Scrapper.py
```

Prompts for a URL, scrapes it, prints the first 1000 characters of markdown content.

## Security note

API key is hardcoded in the script. Move it to an environment variable before sharing or committing this file.
