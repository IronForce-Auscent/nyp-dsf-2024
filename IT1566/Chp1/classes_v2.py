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
        self.__make: str = None
        self.__model: str = None
        self.__price: int | float | str = None
    
    def set_make(self, make: str):
        self.__make = make
        return 1
    
    def set_model(self, model: str):
        self.__model = model
        return 1
    
    def set_price(self, mobile_number: str | int):
        if not str(mobile_number).isnumeric(): 
            self.__price = 0
            return f"Price should be in numbers."
        self.__price = int(mobile_number) 
        return 1
    
    def get_make(self) -> str:
        return f"Make: {self.__make}"

    def get_model(self) -> str:
        return f"Model: {self.__model}"
    
    def get_price(self) -> str:
        return f"Price: {self.__price}"
    
    def get_phone_info(self) -> str:
        return f"The price of the {self.__make} {self.__model} is ${self.__price:.2f}"
    
class Salesperson():
    def __init__(self):
        self.__name: str = None
        self.__commission: int | float = 0
        self.__COMMISSION_RATE = 0.02
    
    def set_name(self, name: str):
        self.__name = name
        return 1
    
    def get_name(self) -> str:
        return f"Name: {self.__name}"
    
    def salesperson_commission(self, payment_received: float):
        self.__commission = payment_received * self.__COMMISSION_RATE
        return 1
    
    def __str__(self) -> str:
        return f"The commission for salesperson {self.__name} is ${self.__commission:.2f}"