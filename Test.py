#Test.py
import Kod
import unittest


class TestPow(unittest.TestCase):
															
			#def test_Pow_negative_one(self):
			#	result = Kod.Pow(-2,2)
			#	self.assertEqual(result,4)
			def test_Pow_positive(self):
				result = Kod.Pow(2,2)  
				self.assertEqual(result,4)
			def test_Pow_zero(self):
				result= Kod.Pow(0,1) 
				self.assertEqual(result,0)


if __name__ == '__main__':
    unittest.main()		