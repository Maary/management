from utils import config
import unittest


class TestConfig(unittest.TestCase):
    conf = config.Config("../app.conf")

    def test_get_string(self):
        self.assertEqual(self.conf.get_string("DB", "host"), '"localhost"')

    def test_get_int_ary(self):
        self.assertEqual(self.conf.get_int_ary("REDIS", "test"), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

