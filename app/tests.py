from django.test import TestCase
from app.models import FibonacciCheck

from Fibonacci import *
from app.views import fibonacci

class FibonacciTest(TestCase):
    msg = "Input to fibonacci sequence must be a non-negative integer"

    def testCase1(self):
        self.assertEqual(6765,fibonacci(20), "Case1 unit test")

    def testCase2(self):
        self.assertEqual(2, fibonacci(3), "Case2 unit test")




    





# Create your tests here.
