from payment import Payment


class Cash(Payment):


    def __init__(self, id, amount):
        super().__init__(id, amount)
