# Quotes Scraper with Pagination

This is a simple Python project that scrapes quotes, authors, and tags from [quotes.toscrape.com](https://quotes.toscrape.com) using `requests` and `BeautifulSoup`, and saves the data to CSV and Excel formats.

---

## 📌 Features

- Scrapes all 10 pages of quotes
- Extracts:
  - Quote text
  - Author name
  - Tags (comma-separated)
- Saves results to:
  - `blogs.csv`
  - `blogs.xlsx`
- Clean CLI output for each quote

---

## 🚀 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

Install requirements:

```bash
pip install requests beautifulsoup4 pandas
