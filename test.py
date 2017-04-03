import unittest
from loan import get_pesa

class loanTest(unittest.TestCase):
    def test_it_works(self):
     self.assertEquals(get_pesa(100000,12,12),112000)
