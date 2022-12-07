from Grammar import Grammar, cfgToCnf




if __name__ == '__main__':
    g = Grammar()
    g.readGrammar('test')
    #g.print()
    grammar = cfgToCnf(g)
    #print(grammar)
    #g.print()



