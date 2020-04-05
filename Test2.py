#Test.py
import Kod
import unittest



class TestSearch(unittest.TestCase):
			def test_Search_zero1(self):
				result=Kod.Search('H')
				self.assertEqual(result,"Yes")
				

if __name__ == '__main__':
    unittest.main()			
			
					