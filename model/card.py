class Card:
    def __init__(self, carta_json: dict):
        self._card_name = carta_json.get('name', 'N/A')
        self._mana_cost = carta_json.get('mana_cost', 'N/A')
        self._cmc = carta_json.get('cmc', 'N/A')
        self._type_line = carta_json.get('type_line', 'N/A')
        self._oracle_text = carta_json.get('oracle_text', 'N/A')
        self._colors = carta_json.get('colors', 'N/A')
        self._color_identity = carta_json.get('color_identity', 'N/A')
        self._keywords = carta_json.get('keywords', 'N/A')
        self._produced_mana = carta_json.get('produced_mana', 'N/A')
        self._card_tag = []

    @property
    def card_name(self):
        return self._card_name

    @property
    def card_cost(self):
        return self._mana_cost

    @property
    def card_mv(self):
        return self._cmc

    @property
    def card_type(self):
        return self._type_line

    @property
    def card_text(self):
        return self._oracle_text

    @property
    def card_color(self):
        return self._colors

    @property
    def card_identity(self):
        return self._color_identity

    @property
    def card_keyword(self):
        return self._keywords

    @property
    def card_mana_prod(self):
        return self._produced_mana

    @property
    def card_tag(self):
        return self._card_tag

    @card_tag.setter
    def card_tag(self, value):
        if isinstance(value, list):
            self._card_tag = value
        else:
            raise ValueError("card_tag deve ser uma lista.")

    def __str__(self):
        return (f"Card: {self._card_name}\n"
                f"Mana Cost: {self._mana_cost}\n"
                f"Mana Value: {self._cmc}\n"
                f"Card Type: {self._type_line}\n"
                f"Card Text: {self._oracle_text}\n"
                f"Card Color: {self._colors}\n"
                f"Card Identity: {self._color_identity}\n"
                f"Card Keywords: {self._keywords}\n"
                f"Card Mana Production: {self._produced_mana}\n"
                f"Tags: {', '.join(self._card_tag) if self._card_tag else 'N/A'}")