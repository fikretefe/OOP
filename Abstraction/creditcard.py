from payment import Payment

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Kredi kartı ile {amount} TL ödendi") 