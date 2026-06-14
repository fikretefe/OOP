from creditcard import CreditCard
from paypal import PayPal

payments = [
    CreditCard(),
    PayPal()
]

for p in payments:
    p.pay(100)