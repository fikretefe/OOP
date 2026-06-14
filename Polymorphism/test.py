from dog import Dog
from cat import Cat

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    animal.eat()