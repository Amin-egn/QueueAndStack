# standard
import unittest
# internal
from src.stack import Stack

class TestStack(unittest.TestCase):
    """Test Stack Method"""
    def test_push(self):
        expected_result = [1, 2, 3]
        stk = Stack(3)
        for i in expected_result:
            stk.push(i)

        self.assertListEqual(stk._stack, expected_result)

    def test_pop(self):
        stk = Stack(3)
        expected_pop_result = [1 ,2 ,3]
        stk_pop = []
        for i in expected_pop_result:
            stk.push(i)

        for i in expected_pop_result:
            stk_pop.append(stk.pop())

        expected_pop_result.reverse()

        self.assertListEqual(expected_pop_result, stk_pop)

    def test_full_push(self):
        expected_msg = 'Stack is full'

        stk = Stack(1)
        stk.push(1)
        try:
            stk.push(2)
        except Exception as e:
            msg = str(e)
        self.assertEqual(msg, expected_msg)

    def test_empty_pop(self):
        expected_msg = 'Stack was empty'
        stk = Stack(1)
        try:
            stk.pop()
        except Exception as e:
            msg = str(e)

        self.assertEqual(msg, expected_msg)

if __name__ == '__main__':
    unittest.main()