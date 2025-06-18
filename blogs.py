import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {
    "Title": [],
    "Author": [],
    "Tag": []
}

# Scrape only page 1 to 10
for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    # If page not found (extra safety)
    if response.status_code != 200:
        print(f"Page {page} not found. Stopping.")
        break

    print(f"Scraping page {page}...")
    soup = BeautifulSoup(response.content, "html.parser")
    
    quote_blocks = soup.select("div.quote")

    for quote in quote_blocks:
        title = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.select("div.tags a.tag")]
        tag_string = ", ".join(tags)

        print(f"Title: {title}\nAuthor: {author}\nTag: {tag_string}\n")
        print("-" * 40)

        data["Title"].append(title)
        data["Author"].append(author)
        data["Tag"].append(tag_string)

# Save to CSV and Excel
df = pd.DataFrame(data)
df.to_csv("blogs.csv", index=False)
df.to_excel("blogs.xlsx", index=False)
print("✅ Data saved to blogs.csv and blogs.xlsx")
