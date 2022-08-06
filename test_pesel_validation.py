import unittest
from task_2 import pesel_validation


class TestPeselValidation(unittest.TestCase):
    def test_pesel_validation(self):
        self.assertTrue(pesel_validation("01322008493"))
        self.assertFalse(pesel_validation("01322008491"))
        self.assertFalse(pesel_validation("01322008492"))
        self.assertFalse(pesel_validation("01322008495"))
        self.assertFalse(pesel_validation("01322008494"))


if __name__ == "__main__":
    unittest.main()
