import unittest
from app import fun

class FunTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("login")
		cls.user="JAYARAM"
	@classmethod
	def tearDownClass(cls):
		print("logout")
		cls.user=None

	def setUp(self):
		print("create the resource")

	def tearDown(self):
		print("delete the resource")

	def test_10_20(self):
		print("test_10_20")
		print(self.user)
		act= fun(10,20)
		exp=30
		self.assertTrue(act==exp,"test_10_20 failed")

	def test_str1_20(self):
		print("test_str1_20")
		print(self.user)
		act= fun("str1",20)
		exp=None
		self.assertTrue(act==exp,"test_str1_20 failed")

	def test_10_str2(self):
		print("test_10_str2")
		print(self.user)
		act= fun(10,"str2")
		exp=None
		self.assertTrue(act==exp,"test_10_str2 failed")

	def test_str1_str2(self):
		print("test_str1_str2")
		print(self.user)
		act= fun("str1","str2")
		exp="str1str2"
		self.assertTrue(act==exp,"test_10_20 failed")

#unittest.main()

