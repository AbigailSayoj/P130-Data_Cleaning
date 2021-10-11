from bs4 import BeautifulSoup
import requests
import time
import csv

df = df[df['column_name'].notna()]

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
time.sleep(10)
headers = ["Name", "Distance", "Mass", "Radius"]
star_data = []
new_star_data = []

del df["NAN values"]
del df["Luminosity"]
del df["NAN values"]

def scrape():
    for i in range(1, 430):
        while True:
            time.sleep(2)

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs = {"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs = {"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_star_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)
scrape()