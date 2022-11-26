from Grammer import Grammer, convertToChownsky




if __name__ == '__main__':
    g = Grammer()
    g.readGrammer('test')
    g.print()
    convertToChownsky(g)
    g.print()
