# test_kafkastream.py
"""
Tests for KafkaStream module.
"""

import unittest
from kafkastream import KafkaStream

class TestKafkaStream(unittest.TestCase):
    """Test cases for KafkaStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KafkaStream()
        self.assertIsInstance(instance, KafkaStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KafkaStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
