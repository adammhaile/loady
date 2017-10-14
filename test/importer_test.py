import unittest

from loady.importer import import_symbol
from test.sub import foo


class ImporterTest(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            import_symbol('')

    def test_single(self):
        import_symbol('math')
        import_symbol('loady')

    def test_failed_single(self):
        with self.assertRaises(ImportError):
            import_symbol('DOESNT_EXIST')

    def test_double(self):
        import_symbol('math.log')
        import_symbol('test.sub')

    def test_failed_double(self):
        with self.assertRaises(ImportError):
            import_symbol('math12.log')

        with self.assertRaises(ImportError):
            import_symbol('math.log12')

        with self.assertRaises(ImportError):
            import_symbol('loady.log12')

    def test_longer(self):
        self.assertIs(import_symbol('test.sub.foo'), foo)
        self.assertIs(import_symbol('test.sub.foo.Bar'), foo.Bar)

    def test_base_path(self):
        self.assertIs(import_symbol('.foo', base_path='test.sub'), foo)
        self.assertIs(import_symbol('.sub.foo.Bar', base_path='test'), foo.Bar)
