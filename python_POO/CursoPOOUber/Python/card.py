from payment import Payment 


class Card (Payment):
    card_number = int
    card_date = str
    card_cvv = int


    def __init__(self, id, amount, card_number , card_date, card_cvv):
        super().__init__(id, amount)
        self.card_number
        self.card_date
        self.card_cvv