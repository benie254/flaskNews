import unittest
from models import sources

Sources = sources.Sources


class SourcesTestCase(unittest.TestCase):
    """
    Test behavior of the Sources class
    """

    def setUp(self):
        """
        Runs before every test
        """

        self.new_sources = Sources('The Python Beast', 'A new Python Mag','https://newpython.beas/mag?org=123erh', 'general', 'ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))


if __name__ == '__main__':
    unittest.main()
