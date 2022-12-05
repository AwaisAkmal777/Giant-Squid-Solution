import numpy as np
import requests


def convert_list_from_string_to_int(data):
    final = []
    for value in data:
        final.append(int(value))
    return final

with open("input.txt" , 'r' , encoding='utf-8' ) as f:

    raw_data = f.read().split("\n\n")
    f.close()
    numbers = raw_data[0]
    list_of_numbers = convert_list_from_string_to_int(numbers.split(","))
    cards_list = []

    for card in raw_data[1:]:
        rows = card.split("\n")
        final = []
        for row in rows:
            final.append(convert_list_from_string_to_int(row.split()))
        cards = np.array(final)
        card = {"card": cards, "bingo": False}
        cards_list.append(card)
results = []
for num in list_of_numbers:
    for card in cards_list:
        if not card["bingo"]:

            card["card"] = np.where(card["card"] == num, 100, card["card"])

            if 500 in np.sum(card["card"], axis=1) or 500 in np.sum(card["card"], axis=0):

                card["card"] = np.where(card["card"] == 100, 0, card["card"])

                results.append(np.sum(card["card"]) * num)
                card["bingo"] = True

print(f"Solution: {results[-1]}")

url = 'https://customer-api.krea.se/coding-tests/api/squid-game'
myobj = {   "answer": str(results[-1]),
            "name": "Muhamamd awais akmal"
        }

x = requests.post(url, json = myobj)

print(x.text)
    