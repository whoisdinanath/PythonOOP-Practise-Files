import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price : float, qty: int=0):
        # Run validations to the recieved aruments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert qty >= 0, f"Quantity {qty} is not greater than or equal to 0"


        #Assign to self objects
        self.__name = name #__name(__ makes the attribute private) beacause we need to set this as a read only attribute
        self.__price = price
        self.qty = qty

        # Actions to execute
        Item.all.append(self)


    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    @property
    #Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("The name exceeds the max length!")
        else:
            self.__name = new_name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.qty})"

    def calculate_total_price(self):
        return self.__price * self.qty
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                qty = int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        #we will count out the floats
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()

        elif isinstance(num, int):
            return True

        else:
            return False



