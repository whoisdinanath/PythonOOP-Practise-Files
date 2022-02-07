from item import Item
class Phone(Item):
    def __init__(self, name: str, price : float, qty: int, broken_phones =0 ):
        #CALL TO SUPER FUNCTION TO HAVE ACCESS TO ALL ATTRIBUTE.
        super().__init__(name, price, qty)
        # Run validations to the recieved aruments
        assert broken_phones >=0, f"Broken Phones{broken_phones} is not greater than or equal to 0"

        #Assign to self objects
        self.broken_phones = broken_phones
