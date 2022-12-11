import pprint

import helper
from Grammar import Grammar, cfgToCnf, cfgTo2nf
from CYK import cyk_parser, nullable, constructGraph, discoverReach, cyk_parser_LangeLeiss



if __name__ == '__main__':
    #TODO mudar remoção de lambda, ele esta simplesmente tirando da gramática
    g = Grammar()
    #g.readGrammar('test')
    g.readGrammar('test_LangeLeiss')
    #g.print()
    #grammar = cfgToCnf(g) # to Chomsky
    grammar = cfgTo2nf(g) # to binary form
    #print(grammar)
    g.print()

    """ term = helper.findRulesRelatedToTerminals(g)
    var = helper.findRulesRelatedToVariables(g)
    print(term)
    print(var)
    sentence_1 = "aaacb"
    isMember = cyk_parser(g, sentence_1)
    print("Is member?", isMember)
    pprint.pprint(isMember)  """
   

    print("CHEGOU AQ!")

    null = nullable(g)
    print("Null: ", end="")
    print(null)
    print("Inverse Unit Graph: ",end="")
    graph = constructGraph(g, null)
    print(graph)
    print("Rules: ", end="")
    print(g.rules)

    sentence_1 = "(a0+b)*a"
    #sentence_1 = "aaacb"
    print("Sentence: " + sentence_1)

    #print(discoverReach(graph, ['c']))

    isMember = cyk_parser_LangeLeiss(g, graph, sentence_1)
    print(isMember)
    #print("Pertence:", cyk_alg(terms=term, varies=var, inp=sentence_1))



