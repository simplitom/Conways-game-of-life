class LocalNeighborhood:

    def __init__(self, inputlist):
        self.mylist = inputlist

    def countNeighbors(self):
        output = 0
        for x in self.mylist:
            output = output + x
        output = output - self.mylist[4]
        return output

    def liveCell(self):
        return self.mylist[4]==1

    def next_tick_alive(self):
        nr_of_neighbours = self.countNeighbors()
        if self.liveCell():
            if nr_of_neighbours== 2 or nr_of_neighbours== 3:
                return True
            else:
                return False
        else:
            if nr_of_neighbours == 3:
                return True
            else:
                return False

