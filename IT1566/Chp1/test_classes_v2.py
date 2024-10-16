from classes_v2 import *
import unittest

# Test case for the MyClass
class TestClasses(unittest.TestCase):

    def setUp(self):
        """This method is called before every test."""
        # Initialize a new MyClass instance for each test
        pass

    def tearDown(self):
        """This method is called after every test."""
        # Clean up (if necessary)
        pass

    def test_customer(self):
        customer = Customer()
        customer.set_name("John")
        customer.set_email("john@nyp.edu.sg")
        customer.set_mobile_number("92345678")
        self.assertEqual(customer.get_name(), "Name: John")
        self.assertEqual(customer.get_email(), "Email: john@nyp.edu.sg")
        self.assertEqual(customer.get_mobile_number(), "Mobile Number: 92345678")

    def test_phone(self):
        phone = Phone()
        phone.set_make("Apple")
        phone.set_model("iPhone 12")
        phone.set_price(1200)
        phone.set_quantity(1)
        self.assertEqual(phone.get_make(), "Make: Apple")
        self.assertEqual(phone.get_model(), "Model: iPhone 12")
        self.assertEqual(phone.get_price(), "Price: 1200")
        self.assertEqual(phone.__str__(), "The phone created is Apple iPhone 12 priced at $1200.00. Now has 1 phone in stock.")

    def test_phone_error(self):
        phone = Phone()
        phone.set_make("Apple")
        phone.set_model("iPhone 12")
        self.assertEqual(phone.set_price("ABC"), "Price should be in numbers.")
        phone.set_quantity(1)
        self.assertEqual(phone.get_make(), "Make: Apple")
        self.assertEqual(phone.get_model(), "Model: iPhone 12")
        self.assertEqual(phone.get_price(), "Price: 0")
        self.assertEqual(phone.__str__(), "The phone created is Apple iPhone 12 priced at $0.00. Now has 1 phone in stock.")

    def test_salesperson(self):
        phone = Phone()
        phone.set_make("Apple")
        phone.set_model("iPhone 12")
        phone.set_price(1200)
        phone.set_quantity(1)
        self.assertEqual(phone.__str__(), "The phone created is Apple iPhone 12 priced at $1200.00. Now has 1 phone in stock.")  
        salesperson = Salesperson()
        salesperson.set_name("Mary")
        salesperson.salesperson_sold(phone)
        self.assertEqual(salesperson.get_name(), "Name: Mary")
        self.assertEqual(salesperson.__str__(), "Salesperson Mary sold Apple iPhone 12 at $1200 and earned a commission of $24.00.")

# This block ensures that the tests run when the script is executed
if __name__ == '__main__':
    unittest.main()
