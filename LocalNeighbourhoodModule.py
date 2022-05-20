class LocalNeighborhood:

    def __init__(self, inputlist):
        self.mylist = inputlist

    def countNeighbors(self):
        output = 0
        for x in self.mylist:
            output = output + x
        output = output - self.mylist[4]
        return output

