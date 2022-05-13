import unittest
import conway

class testconway(unittest.TestCase):

    def test_should_count_live_cells(self):
        self.assertEqual(conway.count_live_cells(1,1,1,1,1,1,1,1,1), 9)
        self.assertEqual(conway.count_live_cells(1, 1, 1, 1, 1, 1, 1, 1, 0), 8)
        self.assertEqual(conway.count_live_cells(0, 0, 0, 0, 0, 0, 0, 0, 0), 0)
        self.assertEqual(conway.count_dead_cells(0, 0, 0, 0, 0, 0, 0, 1, 0), 8)

if __name__ == '__main__':
    unittest.main()
