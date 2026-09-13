import sys
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin  # Library to handle relative URLs

# Function to scrape the book catalog
def scrape_book_catalog(start_url):
    extracted_data = []
    current_url = start_url

    # Main loop to navigate through the catalog pages
    while current_url:
        print(f"[*] Extracting data from: {current_url}")
        
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[!] Connection error: {e}")
            break  # Exit loop on network error

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        # Current page data extraction
        for book in books:
            title = book.h3.a['title']
            price_raw = book.find('p', class_='price_color').text
            price = float(price_raw.replace('£', '').replace('Â', '').strip())
            availability = book.find('p', class_='instock availability').text.strip()
            
            extracted_data.append({
                'Title': title,
                'Price_GBP': price,
                'Status': availability
            })

        # Pagination handling block
        next_button = soup.find('li', class_='next')
        
        if next_button:
            next_page_url = next_button.a['href']
            current_url = urljoin(current_url, next_page_url)
        else:
            print("[*] No more pages found. Catalog end reached.")
            current_url = None  # Terminates the loop

    # Save the extracted data to a CSV file
    print(f"[*] Extraction finished. Total books extracted: {len(extracted_data)}")
    df = pd.DataFrame(extracted_data)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'complete_books_catalog.csv')
    
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"[*] Data successfully saved to: {output_path}")

# Execution block to allow command line argument for URL
if __name__ == "__main__":
    if len(sys.argv) > 1:
        TARGET_URL = sys.argv[1]
    else:
        # Fall back to a default URL if none is provided
        TARGET_URL = "http://books.toscrape.com/index.html"
        print("[!] No URL provided. Using default test URL.")
    
    scrape_book_catalog(TARGET_URL)