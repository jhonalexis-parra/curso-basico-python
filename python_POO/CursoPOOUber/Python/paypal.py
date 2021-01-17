from payment import Payment


class Paypal (Payment):
    email = str
    password = str


    def __init__(self,id, amount, email, password):
        super().__init__(id, amount)
        self.email = email
        self.password = password