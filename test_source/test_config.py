from utils import config
import unittest


class TestConfig(unittest.TestCase):
    conf = config.Config("app.conf")

    def test_get_string(self):
        self.assertEqual(self.conf.get_string("DB", "host"), '"localhost"')


if __name__ == '__main__':
    unittest.main()

