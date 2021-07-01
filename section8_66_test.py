import unittest
import section8_66


class TestSection8(unittest.TestCase):

    def test_one(self):
        bal = 1000
        result = section8_66.BankAccount("Pranav", 100).deposit(bal)
        self.assertEqual(result, 'Available Balance {}'.format(1100))


if __name__ == "__main__":
    unittest.main()
