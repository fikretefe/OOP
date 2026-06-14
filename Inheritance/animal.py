class Animal:
    def __init__(self):
        self._dna = "ATCG"       # protected
        self.type = "MAMMAL"     # public

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

    def move(self):
        print("Moving...")