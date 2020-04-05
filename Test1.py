#Test.py
import Kod
import unittest



class TestMax(unittest.TestCase):
			def test_Max_zero1(self):
				result=Kod.Max(1,2,3)
				self.assertEqual(result,3)
			def test_Max_zero2(self):
				result=Kod.Max(3,2,1)
				self.assertEqual(result,3)
			def test_Max_zero3(self):
				result=Kod.Max(3,2,1)
				self.assertEqual(result,3)

if __name__ == '__main__':
    unittest.main()			
			
					