from item import Item

class Phone(Item): 
    
    pay_rate = 0.8
    all:list[object] = []

    def __init__(self, name: str, price: float, quantity: int = 5, broken_phones:int = 0) -> None:
        super().__init__(name, price, quantity)

        # Run validations on the 
        assert broken_phones >= 0, f"The quantity should be greater than zero, you have given '{broken_phones}'"
        
        self.broken_phones = broken_phones

        Phone.all.append(self) 

