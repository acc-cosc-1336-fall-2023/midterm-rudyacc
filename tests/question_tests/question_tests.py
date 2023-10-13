#write function tests here, don't add input('') statements here!
import unittest
from src.question_c.question_c import is_prime
from src.question_b.question_b import use_global
from src.question_d.question_d import sales

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string, test_config


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    """def test_reverse_string():
        assert reverse_string("hello world") == "dlrow olleh"
        assert reverse_string("hello") == "olleh"
while True:
    user_input = input("Enter a string (or 'q' to quit): ")
    if user_input == 'q':
        break
    reversed_result = reverse_string(user_input)
    print("Reversed:", reversed_result)

global_var = 10

def use_global():
    global global_var
    global_var += 5

def test_use_global():
    use_global()
    assert global_var == 15

test_use_global()

global_var = 100

def use_global():
    global global_var
    global_var += 25

use_global()

print("Global variable after change:", global_var)

print("is.prime(4) returns:", is_prime(4))

print("is.prime(5) returns:", is_prime(5))

print("is.prime(11) returns:", is_prime(11))




while True:

    user_input = input("Enter a number to check if it is prime (or 'q' to quit): ")

    if user_input == 'q':

        break

    try:

            num = int(user_input)

            if is_prime(num):

                print(f"{num} is prime.")

            else:

                print(f"{num} is not prime.")

    except ValueError:

            print("Invalid input. Please enter a valid number.")"""
    
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (-1), "Invalid Argument")
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (200), "Bonus will be 10")
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (600), "Bonus will be 36")
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (1000), "Bonus will be 70")
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (1500), "Bonus will be 120")
    def test_get_bonus_pay_amount(self):
        self.assertEqual(sales (2000), "Invalid Argument")

    test_get_bonus_pay_amount()


