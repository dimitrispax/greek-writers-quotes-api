from flask import jsonify 
from bs4 import BeautifulSoup
import requests

# At first, accessing the greeka site, which is static and easy to scrape data.
URL = "https://www.greeka.com/greece-history/greek-people-quotes/"

# Get the contents of the page from URL.
page = requests.get(URL)

# Parse the page data with the use of the BeautifulSoup library.
soup = BeautifulSoup(page.content, "html.parser")

# Located using inspector the containers of each quotes.
quotesContainer = soup.find_all('blockquote')

quotes = [] # Initializing the final result list.
# Iterating through each quote container and grab each quote's data.
for quoteContainer in quotesContainer:
    quote = {} # Initialing each quote's dictionary.
    
    author = quoteContainer.find('h3') # Grabbing the author's name.
    authorInfo = quoteContainer.find_all('p')[0] # Grabbing the author's info.
    text = quoteContainer.find_all('p')[1] # Grabbing the actual quote.
    
    # Adding each data in dictionary so it can be later transformed to JSON.
    quote["author"] = author.get_text()
    quote["authorInfo"] = authorInfo.get_text()
    quote["text"] = text.get_text()
    quotes.append(quote)

  