# standard
import unittest
# internal
from src.q import Queue


class TestQueue(unittest.TestCase):
    """Test Queue Method"""
    def setUp(self):
        self.expected_result = [1 ,2 ,3]
        self.q = Queue(3)
        self.qp = Queue(1)

    def test_push(self):
        for i in self.expected_result:
            self.q.push(i)
        
        self.assertListEqual(self.expected_result, self.q._queue)

    def test_pop(self):
        q_pop = []
        for i in self.expected_result:
            self.q.push(i)

        for i in self.expected_result:
            q_pop.append(self.q.pop())

        self.assertListEqual(self.expected_result, q_pop)

    def test_full_push(self):
        expected_msg = 'Queue is full'
        self.qp.push(1)
        try:
            self.qp.push(2)
        except Exception as e:
            msg = str(e)

        self.assertEqual(msg, expected_msg)

    def test_empty_pop(self):
        expected_msg = 'Queue was empty'
        
        try:
            self.qp.pop()
        except Exception as e:
            msg = str(e)

        self.assertEqual(msg, expected_msg)
        
        