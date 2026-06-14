from payment import Payment

class PayPal(Payment):
    
    def pay(self, amount):
        print(f"PayPal ile {amount} TL ödendi")