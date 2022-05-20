import unittest
import grid


class testGrid(unittest.TestCase):

    def test_grid(self):
        gr=grid.Grid(((0,0),(1,1)))
        self.assertEqual(gr.livecellonlocation(0,0),1)
        self.assertEqual(gr.livecellonlocation(0,1),0)

    def test_to_local(self):
        gr = grid.Grid(((0, 0), (1, 1)))
        self.assertEqual(gr.localneighborhood(0,0).liveCell(),True)
        self.assertEqual(gr.localneighborhood(0, 1).liveCell(), False)
