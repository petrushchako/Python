import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        x, y = "Alpha", "Alpha"
        self.assertEqual(x, y)


if __name__ == "__main__":
    unittest.main()
