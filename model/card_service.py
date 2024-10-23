from model.card import Card
from model.card_tag import CardTag
import api.scryfall_api as ScryfallApi

def create_card(card_name: str) -> Card:
    return Card(ScryfallApi.search_card(card_name))

def add_tag(card: Card, tag_list: list[CardTag]):
    invalid_tags = []

    for tag in tag_list:
        if tag in card.card_tag:
            invalid_tags.append(tag)

    if invalid_tags:
        return f'Invalid tags: {", ".join(invalid_tags)} are already present in {card.card_name}.'

    card.card_tag = tag_list

    return f'Tags {", ".join(tag_list)} added to {card.card_name}.'