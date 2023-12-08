# Web-scraping-project
This project focuses on web scraping the KCNS (Kulturni centar Novog Sada) website to extract information about literary and speech programs. The script allows users to search for articles based on keywords, article types, and publication dates.

Table of Contents
2. Introduction
3. Features
4. Requirements
5. Installation
6. Usage
7. Examples
8. Contributing
9. License

Introduction
Web scraping is a technique used to extract data from websites. In this project, we utilize Python and BeautifulSoup to scrape information from the KCNS website related to literary and speech programs. The script prompts users to input search parameters such as keywords, article types, and dates, allowing for flexible and personalized searches.

Features
Search for articles by name, type, and date.
Conversion of Cyrillic characters to Latin for better search results.
Clear and organized code structure.
Command-line interface for user interaction.

Requirements
Python 3.x
BeautifulSoup4
Requests
Unidecode
Install the required packages using:
pip install beautifulsoup4 requests unidecode

Installation
1. Clone the repository to your local machine:
git clone https://github.com/your-username/Web-scraping-project.git
2. Navigate to the project directory:
cd Web-scraping-projec
3. Run the script:
python main.py

Usage
Input the desired search parameters when prompted.
View the extracted information for matching articles.

Examples
Search for articles with the keyword "knjizevno" (literary) and published in the year 2023:
python main.py
Enter the following when prompted:
Enter a keyword to search for in article names (or press Enter to skip): knjizevno
Enter a keyword to search for in article types (or press Enter to skip):
Enter year (or press Enter to skip): 2023

Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

License
This project is licensed under the MIT License.
