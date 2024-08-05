import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books_to_scrape():
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    book_titles = []
    book_prices = []
    book_ratings = []

    books = soup.find_all('article', class_='product_pod')
    for book in books:
        # Get the title
        title = book.h3.a['title']
        
        # Get the price
        price = book.find('p', class_='price_color').text.strip('£')
        
        # Get the rating
        rating = book.p['class'][1]
        
        # Append extracted data to lists
        book_titles.append(title)
        book_prices.append(float(price[2:]))
        book_ratings.append(rating)

    # Ensure that the lists are not None and have the same length
    if not (book_titles and book_prices and book_ratings):
        print("Error: One or more lists are empty or None.")
        return

    if not (len(book_titles) == len(book_prices) == len(book_ratings)):
        print("Error: Lists have different lengths.")
        return

    # Create a DataFrame with the extracted data
    data = pd.DataFrame({
        'Title': book_titles,
        'Price (£)': book_prices,
        'Rating': book_ratings
    })

    # Export the DataFrame to a CSV file
    data.to_csv('books.csv', index=False)
    print("Data has been successfully scraped and stored in 'books.csv'.")

scrape_books_to_scrape()
