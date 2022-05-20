import LocalNeighbourhoodModule

class Grid:
    def __init__(self, Live_cell_coordinates):
        self.mylist = Live_cell_coordinates

    def livecellonlocation(self,x,y):
        return self.mylist.count((x,y))

    def localneighborhood(self,x,y):
        return LocalNeighbourhoodModule.LocalNeighborhood(
            (
            self.livecellonlocation(x-1,y+1),
            self.livecellonlocation(x, y+1),
            self.livecellonlocation(x+1, y+1),
            self.livecellonlocation(x-1, y),
            self.livecellonlocation(x, y),
            self.livecellonlocation(x+1, y),
            self.livecellonlocation(x-1, y-1),
            self.livecellonlocation(x, y-1),
            self.livecellonlocation(x+1, y-1)
            )
        )






