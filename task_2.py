from typing import List
from bs4 import BeautifulSoup
import json
import os
import requests

def animals_json(letter: str, animals_array: List[str]) -> None:
    file_name = 'animals.json'
    if os.path.exists("animals.json"):
        data = json.load(open(file_name, encoding='utf-8'))
    else:
        data = {}
    if letter in data:
        data[letter] += animals_array
    else:
        data[letter] = animals_array
    json.dump(data, open(file_name, mode='w', encoding='utf-8'))


def parse_wiki_animal() -> None:
    print("Start parse, wait please!")
    if os.path.exists("animals.json"):
        os.remove("animals.json")
    base_url = "https://ru.wikipedia.org"
    path = "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
        
    while True:
        res = requests.get(base_url + path)
        soup = BeautifulSoup(res.text, "lxml")
        path = soup.find("a",text="Следующая страница").get("href")

        animal_blocks = soup.find("div", id="mw-pages").find_all("div", {'class': "mw-category-group"})

        for block in animal_blocks:
            letter = block.find("h3").text
            if letter == "A":
                print("Parse done!")
                data = json.load(open("animals.json", encoding='utf-8'))
                for k, v in data.items():
                    print(f"{k}: {len(set(v))}")
                return
            animals_li = block.find("ul").find_all("li")
            animals = [i.find("a").text for i in animals_li]
            animals_json(letter, animals)
    
    
if __name__ == "__main__":
    parse_wiki_animal()