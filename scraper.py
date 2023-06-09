import requests
from bs4 import BeautifulSoup
import csv
import os
import traceback

# urls to scrape from
urls = ['https://www.dtu.dk/uddannelse/ansoegning-og-optagelse/diplomingenioer-bachelor-optagelse/adgangskvotienter?accordion=0',
        'https://www.sdu.dk/da/uddannelse/bachelor/gennemsnit', 'https://www.ug.dk/kot-tal', ]

# specify the workign directory and the name of the CSV file to store the collected grades
directory = r'C:\Users\olars\Documents\code_projects\WebScraper'
filename = 'entrance_grades.csv'

# create a CSV file to store the collected grades
csv_file_path = os.path.join(directory, filename)
os.makedirs(directory, exist_ok=True)

# write header row to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header row
    csv_writer.writerow(['Universitet', 'Studie', 'Snit Krav'])

# loop through the URLs and collect grades
for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # extract grades from specific HTML tags or attributes
            grades = soup.find_all('span', {'class': 'grade'})

            # extract additional information as needed, such as university name or program name
            university = 'DTU' if 'dtu' in url else 'SDU'
            program = 'Diplomingeniør' if 'dtu' in url else 'Bachelor'

            # write the extracted grades to the CSV file
            for grade in grades:
                csv_writer.writerow([university, program, grade.text])
                
         except Exception as e:
            error_msg = f"Error scraping URL: {url}\nError message: {str(e)}\nStack trace:\n{traceback.format_exc()}\n"
            with open('error.log', 'a') as error_file:
                error_file.write(error_msg)
            print(error_msg)

csv_file.close()
print("Entrance grades have been collected and saved to 'entrance_grades.csv'")
print(f"CSV file created at: {os.path.abspath(csv_file_path)}")
