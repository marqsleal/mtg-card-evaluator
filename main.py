import model.card_service as CardService
from model.card_tag import CardTag


def main():
    carta_nome = input('Digite o nome da carta: ')
    carta = CardService.create_card(carta_nome)

    CardService.add_tag(carta, [CardTag.RAMP.value])

    print(carta)

if __name__ == '__main__':
    main()