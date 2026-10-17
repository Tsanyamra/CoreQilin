# test_coreqilin.py
"""
Tests for CoreQilin module.
"""

import unittest
from coreqilin import CoreQilin

class TestCoreQilin(unittest.TestCase):
    """Test cases for CoreQilin class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreQilin()
        self.assertIsInstance(instance, CoreQilin)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreQilin()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
