def conway(num):

    return num

def count_live_cells(topleft, topmid, topright, midleft, midmid, midright, bottomleft, bottommid,bottomright):
    return topleft + topmid + topright + midleft + midmid + midright + bottomleft + bottommid+bottomright

def count_dead_cells(topleft, topmid, topright, midleft, midmid, midright, bottomleft, bottommid,bottomright):
    return 9 - count_live_cells(topleft, topmid, topright, midleft, midmid, midright, bottomleft, bottommid,bottomright)