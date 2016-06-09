"""Sample unit test module."""

import unittest

from sappy import sample


class TestSappy(unittest.TestCase):

    """Sample unit test class."""

    def test_dependency_import(self):
        """Sample test method for dependencies."""
        try:
            import testpackage  # pylint: disable=unused-variable
            assert True
        except ImportError:
            self.fail("dependency not installed")

    def test_branch_coverage(self):
        """Sample test method for branch coverage."""
        self.assertEqual(sample.function(True), 'True')
        self.assertEqual(sample.function(False), 'False')
        self.assertEqual(sample.function(None), 'None')
