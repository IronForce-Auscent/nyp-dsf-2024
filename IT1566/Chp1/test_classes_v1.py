from classes_v1 import *
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
        customer = Customer("John", "john@nyp.edu.sg", 92345678)
        self.assertEqual(customer.get_customer_info(), "Name: John, Email: john@nyp.edu.sg, Mobile Number: 92345678")
        customer = Customer("John", "john@nyp.edu.sg", "92345678")
        self.assertEqual(customer.get_customer_info(), "Name: John, Email: john@nyp.edu.sg, Mobile Number: 92345678")

    def test_phone(self):
        phone = Phone("Apple", "iPhone 12 Pro Max", 1500)
        self.assertEqual(phone.get_phone_info(), "The price for a Apple iPhone 12 Pro Max is $1500.00")

# This block ensures that the tests run when the script is executed
if __name__ == '__main__':
    unittest.main()
