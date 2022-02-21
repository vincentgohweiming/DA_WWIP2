import unittest
class newscrapy(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(),"FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("FOO".isupper())
if __name__ == "__main__":
    unittest.main()