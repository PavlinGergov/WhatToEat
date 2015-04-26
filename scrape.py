# mkdir pycon-scraper
# virtualenv venv
# cd venv
# source bin/activate
# (venv) $ pip3 install requests beautifulsoup4

import json
import requests
import bs4
import time


recipe_index = 1
result = []

for page in range(1, 194):
    response = requests.get('http://www.1001recepti.com/recipes/show/by_type/?list_id=3-salati&page=' + str(page))
    response.encoding = 'windows-1251'
    # response.text -> za proverka samo :)
    # print(res.text) --> samo za info!

    soup = bs4.BeautifulSoup(response.text)
    links = soup.select('.rec .ss a')
    links = [a.attrs.get('href') for a in soup.select('.rec .ss a')]

    print('Downloaded recipe list ' + str(page))

    for link in links:
        current_recipe = {}
        recipe_page_html = requests.get(link)
        recipe_page_html.encoding = 'windows-1251'
        recipe_page = bs4.BeautifulSoup(recipe_page_html.text)

        ingredients = recipe_page.select('.recipe_ingr')[0].text
        current_recipe['ingredients'] = ingredients.replace('\t', '').replace('\n' * 5, '\n').replace('\n\r\n', ' ').replace('\n\n\n\n', '').strip()

        instructions = recipe_page.select('#rtext')[0].text
        current_recipe['instructions'] = instructions.replace('\t', '')

        calories = recipe_page.select('.tr0.pt3 .dv.str span')[0].text
        current_recipe['calories'] = calories

        result.append(current_recipe)
        print('saved recipe ' + str(recipe_index))
        recipe_index += 1

    time.sleep(5)

    with open("salati-pages1-" + str(page) + ".json", "w") as current_file:
        json.dump(result, current_file, indent=True, ensure_ascii=False)


with open("scrape.json", "w") as f:
    json.dump(result, f, indent=True, ensure_ascii=False)
