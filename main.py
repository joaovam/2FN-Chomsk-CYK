import pprint

import helper
from Grammar import Grammar, cfgToCnf
from CYK import cyk_parser



if __name__ == '__main__':
    #TODO mudar remoção de lambda, ele esta simplesmente tirando da gramática
    g = Grammar()
    g.readGrammar('test')
    #g.print()
    grammar = cfgToCnf(g) # to Chomsky
    # grammar = cfgTo2nf(g) # to binary form
    #print(grammar)
    g.print()
    """ term = helper.findRulesRelatedToTerminals(g)
    var = helper.findRulesRelatedToVariables(g)
    print(term)
    print(var)
    sentence_1 = "aaacb"
    isMember = cyk_parser(g, sentence_1)
    print("Is member?", isMember)
    pprint.pprint(isMember) """
    #print("Pertence:", cyk_alg(terms=term, varies=var, inp=sentence_1))



