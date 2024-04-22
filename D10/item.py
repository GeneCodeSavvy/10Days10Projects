import csv


class Item:
    
    pay_rate:float = 0.8 #The pay rate after 20% discount
    all:list[object] = []

    def __init__(self, name:str, price:float, quantity:int=5) -> None:
        #Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to Zero"
        assert type(name) == str, f"The name {name} is not a string"
        
        #Assign self objects 
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Add instance to the all list
        Item.all.append(self)

    @property
    # Property decorator: Only for read only attributes {Getter}
    def name(self):
        return self.__name
    
    @name.setter
    # Update name attribute {Setter}
    def name(self, value):
        if len(value) > 10:
            raise Exception("Your name is too long")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self.__price
    
    def apply_increament(self, increament_value):
        self.__price = self.__price + (self.__price * increament_value)
       
    def calculate_total_price(self):
        total_cost = self.__price * self.quantity
        print(total_cost)
        print("done!")
        return total_cost
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("D10/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items:list[dict] = list(reader)

        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True 
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    ################################### This is Abstraction ############
    def __connect(self):
        return "connected to server"
    
    def __email_body(self):
        return "This is a email body"
    
    def __send(self):
        return "email sent"
    
    def send_email(self):
        print(self.__connect())
        print(self.__email_body())
        print(self.__send())
        return "Done"
    
    ############ This was Abstraction ################