import unittest

from the_prime import prime_num

class test_the_prime(unittest.TestCase):
    def test_integerinput(self):
      self.assertEquals(type(num),int)
    def test_if_it_works(self):
        self.assertEquals(primeFun(10),[2,3,5,7])
        pass