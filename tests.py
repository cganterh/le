"""Tests for le bot."""

from argparse import ArgumentParser

from unittest import (
    main,
    TestCase,
)

from unittest.mock import (
    MagicMock,
    patch,
)

from le import create_argument_parser


class TestParserPlugins(TestCase):
    """Test that the le module can load and use parser plugins."""

    @patch('le.iter_entry_points')
    def setUp(self, iter_entry_points):
        """Set up the argument parser."""
        parser = ArgumentParser(add_help=False)
        parser.add_argument('-f', '--foo')

        entry_point = MagicMock()
        entry_point.load.return_value = parser
        iter_entry_points().__iter__.return_value = iter([entry_point])

        self.arguments = create_argument_parser().parse_args(
            ['jdhjdifbahs74he', '-d', '-f', 'hola'])

    def test_debug_argument_is_true(self):
        """Test the debug argument is true."""
        self.assertIn('debug', self.arguments)
        self.assertTrue(self.arguments.debug)

    def test_external_argument(self):
        """Test the external argument from plugin was parsed."""
        self.assertIn('foo', self.arguments)
        self.assertEqual(self.arguments.foo, 'hola')


if __name__ == '__main__':
    main()
