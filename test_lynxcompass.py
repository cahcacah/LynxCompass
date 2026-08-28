# test_lynxcompass.py
"""
Tests for LynxCompass module.
"""

import unittest
from lynxcompass import LynxCompass

class TestLynxCompass(unittest.TestCase):
    """Test cases for LynxCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LynxCompass()
        self.assertIsInstance(instance, LynxCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LynxCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
