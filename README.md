# E-Commerce data scraper (Python CLI)

An automation CLI tool designed for large-scale data extraction from e-commerce catalogs. The script autonomously navigates pagination, handles dynamic file paths, and exports structured dataset files in `.csv` format.

## Features & problem solved
*   **Automated Pagination:** Detects the "Next" page element and iteratively crawls entire product categories without hardcoded limits.
*   **Dynamic CLI Interface:** Accepts custom URLs via command-line arguments to target specific categories on demand.
*   **Portable File Handling:** Dynamically handles file-system paths using `os.path` to save outputs in the script's local directory regardless of the terminal location.
*   **Robustness:** Integrated network exception handling and type casting (float prices, clean status strings).

## Tech stack
*   **Python 3** (Standard modules: `sys`, `os`, `urllib.parse`)
*   **Requests:** HTTP calls and status code verification.
*   **BeautifulSoup4:** HTML DOM parsing and CSS selector queries.
*   **Pandas:** Efficient in-memory data structures (DataFrames) and CSV export.

## Getting Started

### 1. Install dependencies
  ```bash
  pip install requests beautifulsoup4 pandas
  ```

### 2. Usage
*   **Default execution (Sandbox Target):**
  ```bash
  python scraper_catalogo.py
  ```

*   **Dynamic target via CLI**
  ```bash
  python scraper_catalogo.py <CATEGORY_URL>
  ```
  Example:
  ```bash
  python scraper_catalogo.py http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html
  ```
##  Output
The script generates a structured complete_books_catalog.csv file for example:

  ```csv
  Title,Price_GBP,Status
  Scott Pilgrim's Precious Little Life,52.29,In stock
  Tipping the Velvet,53.74,In stock
  ```
## Author: Computer & Automation Engineering Student (Politecnico di Bari). Focused on backend software development, web scraping, and automation pipelines.
