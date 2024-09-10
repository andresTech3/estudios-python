import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://parascrapear.com/")
soup = BeautifulSoup(page.text, 'html.parser')

blockquote_items = soup.find_all('blockquote')


with open("scraping\\BeautifulSoup\\fileScripting.csv", 'w', encoding="UTF-8") as file:
    writeScripting = csv.writer(file)
    for blockquote in blockquote_items:
        autor = blockquote.find(class_="author").text
        categoria = blockquote.find(class_="cat").text
        frase = blockquote.find('q').text
            
        writeScripting.writerow([autor, categoria,frase])
    
