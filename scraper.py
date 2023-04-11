import requests
from bs4 import BeautifulSoup
import csv

# Define the URLs of the web pages to crawl
urls = ['https://www.dtu.dk/uddannelse/ansoegning-og-optagelse/diplomingenioer-bachelor-optagelse/adgangskvotienter?accordion=0',
        'https://www.sdu.dk/da/uddannelse/bachelor/gennemsnit']

# Create a CSV file to store the collected grades
csv_file = open('entrance_grades.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['University', 'Program', 'Entrance Grade'])  # Write header row

# Loop through the URLs and collect grades
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract grades from specific HTML tags or attributes
    # Note: You need to inspect the HTML structure of the web pages to identify the correct tags, classes, or attributes
    grades = soup.find_all('span', {'class': 'grade'})

    # Extract additional information as needed, such as university name or program name
    university = 'DTU' if 'dtu' in url else 'SDU'
    program = 'Diplomingeniør Bachelor' if 'dtu' in url else 'Bachelor'

    # Write the extracted grades to the CSV file
    for grade in grades:
        csv_writer.writerow([university, program, grade.text])

csv_file.close()
print("Entrance grades have been collected and saved to 'entrance_grades.csv'")
