from bs4 import BeautifulSoup
import requests
from unidecode import unidecode

# Mapping for converting Cyrillic characters to Latin
CYRILLIC_TO_LATIN_MAPPING = {
    'ц': 'c',
    'ж': ['ž', 'z'],
    'ш': ['š', 's'],
    'ч': ['č', 'c'],
    'ћ': ['ć', 'c'],
    'ђ': ['đ', 'dj'],
    'џ': ['dž', 'dz']
}

def find_articles(base_url):
    """
    Main function to initiate the web scraping process.

    Parameters:
    - base_url (str): The base URL of the website.

    Returns:
    None
    """
    # Input for search parameters
    search_keyword = input("Enter a keyword to search for in article names (or press Enter to skip): ").lower()
    search_article_type = input("Enter a keyword to search for in article types (or press Enter to skip): ").lower()
    search_date = input("Enter year (or press Enter to skip): ").lower()

    # Initial web request and parsing
    url = base_url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    articles = soup.find_all("div", class_="col s12 m12 l4")

    # Process articles on the current page
    process_articles(articles, search_keyword, search_article_type, search_date)

    # Process additional pages if present
    page_number = 2
    while True:
        url = f"{base_url}/page/{page_number}/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        articles = soup.find_all("div", class_="col s12 m12 l4")
        if not articles:
            break
        process_articles(articles, search_keyword, search_article_type, search_date)
        page_number += 1

def map_cyrillic_to_latin(text):
    """
    Function to map Cyrillic characters to Latin based on predefined mapping.

    Parameters:
    - text (str): Input text with Cyrillic characters.

    Returns:
    str: Transformed text with Latin characters.
    """
    for cyrillic, latin_options in CYRILLIC_TO_LATIN_MAPPING.items():
        for latin in latin_options if isinstance(latin_options, list) else [latin_options]:
            text = text.replace(cyrillic, latin)
    return text

def process_articles(articles, search_keyword, search_article_type, search_date):
    """
    Function to process and print relevant information for each article.

    Parameters:
    - articles (list): List of BeautifulSoup article elements.
    - search_keyword (str): Keyword for filtering article names.
    - search_article_type (str): Keyword for filtering article types.
    - search_date (str): Year for filtering articles by date.

    Returns:
    None
    """
    for article in articles:
        article_type_tag = article.find("span", class_="chip deep-purple white-text allcaps")
        if article_type_tag:
            article_type = unidecode(map_cyrillic_to_latin(article_type_tag.text)).lower()
            search_article_type_unidecoded = unidecode(map_cyrillic_to_latin(search_article_type)).lower()
            if not search_article_type or any(word.lower() in article_type for word in search_article_type_unidecoded.split()):
                date = article.find("ul", class_="collection").li.text
                if not search_date or search_date.lower() in date.lower():
                    article_name = article.find("h2", class_="card-title").text.lower()
                    article_name = unidecode(map_cyrillic_to_latin(article_name)).lower()
                    search_keyword_unidecoded = unidecode(map_cyrillic_to_latin(search_keyword)).lower()
                    if not search_keyword or any(word.lower() in article_name for word in search_keyword_unidecoded.split()):
                        more_info = article.find("article").h2.a["href"]

                        # Formatting the output
                        print(f"\nArticle Name: {article_name}")
                        print(f"Article Type: {article_type}")
                        print(f"Date: {date}")
                        print(f"More Info: {more_info}\n\n")




if __name__ == "__main__":
    base_url = "https://www.kcns.org.rs/kategorija/knjizevni-i-govorni-program"
    find_articles(base_url)
