import unittest
import example_test


class TestClip(unittest.TestCase):
    def test_do_stuf(self):
        test_param = 10
        result = example_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuf2(self):
        test_param = "grfg"
        result = example_test.do_stuff(test_param)
        self.assertEqual(result, TypeError)


if __name__ == "__main__":
    unittest.main()
