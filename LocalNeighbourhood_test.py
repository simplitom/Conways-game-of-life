import unittest
import LocalNeighbourhoodModule


class testLocalNeighbourhood(unittest.TestCase):

    def test_count_LocalNeighbours(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0, 1, 1, 0, 1, 0, 0))
        self.assertEqual(ln.countNeighbors(), 3)
        ln2 = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0, 1, 0, 0, 1, 0, 0))
        self.assertEqual(ln2.countNeighbors(), 3)

    def test_alive(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0, 1, 1, 0, 1, 0, 0))
        self.assertTrue(ln.liveCell())
        ln2 = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0, 1, 0, 0, 1, 0, 0))
        self.assertFalse(ln2.liveCell())

    def test_underpopulation_rule(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0, 0, 1, 0, 0, 0, 0))
        self.assertFalse(ln.next_tick_alive())

    def test_next_generation_rule(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 1, 0, 1, 0, 0, 0, 1))
        self.assertTrue(ln.next_tick_alive())

    def test_overpopulation_rule(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 1, 0, 1, 1, 1, 0, 1))
        self.assertFalse(ln.next_tick_alive())

    def test_reproduction_rule(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 1, 0, 0, 1, 1, 0, 1))
        self.assertFalse(ln.next_tick_alive())
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 1, 0, 0, 0, 0, 0, 1))
        self.assertTrue(ln.next_tick_alive())

if __name__ == '__main__':
    unittest.main()
