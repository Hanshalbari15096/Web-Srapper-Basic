from firecrawl import Firecrawl 
app = Firecrawl(api_key="fc-0dfdf81098d54524baced761267aa2ca")

def scrape(target_url):
    try:
        result=app.scrape(
            target_url,
            formats=["markdown"]
        )
        clean_content=result.get("markdown", "")
        return clean_content
    except Exception as e:
        return f"Scraping failed: {str(e)}"

url_to_scrape = input("Enter your Sitelink:")
extracted_data = scrape(url_to_scrape)
print(extracted_data[:1000])