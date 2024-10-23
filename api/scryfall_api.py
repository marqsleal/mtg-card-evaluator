import requests

def search_card(card_name: str) -> dict:
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)
    return response.json()
