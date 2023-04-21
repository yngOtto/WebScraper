# WebScraper

This is a Python script that scrapes data on entrance grades from three different URLs using the `requests` and `beautifulsoup4` libraries. The script collects entrance grades for two programs from two universities, and writes the data to a CSV file.

## Installation and Usage

1. Clone the repository to your local machine using Git.
2. Install the required libraries with the following command:
   
   ```
   pip install requests beautifulsoup4
   ```
   
3. Run the script using the following command:
   
   ```
   python scraper.py
   ```
   
   The script will collect the entrance grades and save them to a CSV file in the specified directory.

## Error Handling

The script now includes error handling to catch exceptions that may occur during scraping. If an error occurs, the script will write an error message to a log file named `error.log`, and continue with the next URL.

## Credits

This script was created by myself, Otto.
