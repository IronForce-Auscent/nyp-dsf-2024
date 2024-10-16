class Customer():
    def __init__(self):
        self.__name: str = None
        self.__model: str = None
        self.__price: str | int = None
    
    def set_name(self, make: str):
        self.__name = make
        return 1
    
    def set_email(self, email: str):
        self.__email = email
        return 1
    
    def set_mobile_number(self, mobile_number: str | int):
        self.__mobile_number = mobile_number
        return 1
    
    def get_name(self) -> str:
        return f"Name: {self.__name}"

    def get_email(self) -> str:
        return f"Email: {self.__email}"
    
    def get_mobile_number(self) -> str:
        return f"Mobile Number: {self.__mobile_number}"
    

class Phone():
    def __init__(self):
        self._make: str = None
        self._model: str = None
        self._price: int | float | str = None
        self._quantity: int = 0
    
    def set_make(self, make: str):
        self._make = make
        return 1
    
    def set_model(self, model: str):
        self._model = model
        return 1
    
    def set_price(self, mobile_number: str | int):
        if not str(mobile_number).isnumeric(): 
            self._price = 0
            return f"Price should be in numbers."
        self._price = int(mobile_number) 
        return 1
    
    def set_quantity(self, quantity: int):
        self._quantity = quantity
        return 1
    
    def get_make(self) -> str:
        return f"Make: {self._make}"

    def get_model(self) -> str:
        return f"Model: {self._model}"
    
    def get_price(self) -> str:
        return f"Price: {self._price}"
    
    def __str__(self) -> str:
        return f"The phone created is {self._make} {self._model} priced at ${self._price:.2f}. Now has {self._quantity} {"phone" if self._quantity == 1 else "phones"} in stock."
    
class Salesperson():
    def __init__(self):
        self.__name: str = None
        self.__commission: int | float = 0
        self.__COMMISSION_RATE = 0.02
        self.__phone: Phone = None
    
    def set_name(self, name: str):
        self.__name = name
        return 1
    
    def get_name(self) -> str:
        return f"Name: {self.__name}"
    
    def salesperson_commission(self, payment_received: float):
        self.__commission = payment_received * self.__COMMISSION_RATE
        return 1

    def salesperson_sold(self, phone: Phone):
        self.__phone = phone
        self.salesperson_commission(phone._price)
        return 1
    
    def __str__(self) -> str:
        return f"Salesperson {self.__name} sold {self.__phone._make} {self.__phone._model} at ${self.__phone._price} and earned a commission of ${self.__commission:.2f}."