import unittest
import LocalNeighbourhoodModule


class testLocalNeighbourhood(unittest.TestCase):

    def test_LocalNeighbourhoodtest(self):
        ln = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0,1,1,0,1,0,0))
        self.assertEqual(ln.countNeighbors(), 3)
        ln2 = LocalNeighbourhoodModule.LocalNeighborhood((1, 0, 0,1,0,0,1,0,0))
        self.assertEqual(ln2.countNeighbors(), 3)


if __name__ == '__main__':
    unittest.main()
