class Customer():
    def __init__(self, name: str, email: str, mobile_number: str | int):
        self.__name: str = name
        self.__email: str = email
        self.__mobile_number: str | int = mobile_number

    def get_customer_info(self) -> str:
        return f"Name: {self.__name}, Email: {self.__email}, Mobile Number: {self.__mobile_number}"

class Phone():
    def __init__(self, make: str, model: str, price: int | float | str):
        self.__make: str = make
        self.__model: str = model
        self.__price: int | float | str = price
    
    def get_phone_info(self) -> str:
        return f"The price for a {self.__make} {self.__model} is ${self.__price:.2f}"