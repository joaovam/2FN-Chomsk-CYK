import pprint
import sys

from time import time

import src.helper as helper
from src.Grammar import Grammar, cfgToCnf, cfgTo2nf
from src.CYK import cyk_parser, nullable, constructGraph, discoverReach, cyk_parser_LangeLeiss

# python main.py [CYK, CYK_Mod] [filename] [single sentence] [filename of sentences] [True, False depending on Testing time]

if __name__ == '__main__':
    if(len(sys.argv)-1 == 5):
        algorithm_version = sys.argv[1]
        filename = "grammar/" + sys.argv[2]
        sentence_input = sys.argv[3]
        file_sentence = "sentence/" + sys.argv[4]
        isExperiment = False if sys.argv[5] == 'False' else True
    else:
        algorithm_version = 'CYK_Mod' # Modified
        filename = 'grammar/grammar_1'
        sentence_input = '00111'
        file_sentence = 'sentence/input_grammar_1'
        isExperiment = False


    grammar = Grammar()

    grammar.readGrammar(filename)

    if(algorithm_version == 'CYK'):
        if(isExperiment):
            with open(file_sentence, 'r') as sentences:
                duration_sentences = []
                for sentence in sentences:
                    sentence = sentence.strip()
                    now = time()

                    cfgToCnf(grammar)
                    isMember = cyk_parser(grammar, sentence)

                    duration = time() - now
                    duration_sentences.append(( len(sentence), duration))

                    if(isMember):
                        print("The sentence " + sentence + " belongs to the grammar.")
                    else:
                        print("The sentence " + sentence + " DOES NOT belong to the grammar.")

                helper.create_output_experiment(filename, grammar, duration_sentences)
        else:
            now = time()

            cfgToCnf(grammar)
            isMember = cyk_parser(grammar, sentence_input)

            duration = time() - now

            if(isMember):
                print("The sentence " + sentence_input + " belongs to the grammar.")
            else:
                print("The sentence " + sentence_input + " DOES NOT belong to the grammar.")

            print("Duration: " + str(duration) + " s")

            helper.create_output(filename, grammar, sentence_input, isMember, duration)

    elif(algorithm_version == 'CYK_Mod'):
        if(isExperiment):
            with open(file_sentence, 'r') as sentences:
                duration_sentences = []
                for sentence in sentences:
                    sentence = sentence.strip()
                    now = time()

                    cfgTo2nf(grammar)
                    nullables = nullable(grammar)
                    inverseUnitGraph = constructGraph(grammar, nullables)

                    isMember = cyk_parser_LangeLeiss(grammar, inverseUnitGraph, sentence)

                    duration = time() - now
                    duration_sentences.append(( len(sentence), duration))

                    if(isMember):
                        print("The sentence " + sentence + " belongs to the grammar.")
                    else:
                        print("The sentence " + sentence + " DOES NOT belongs to the grammar.")


                helper.create_output_experiment(filename, grammar, duration_sentences, True)
        else:
            now = time()

            cfgTo2nf(grammar)
            nullables = nullable(grammar)
            inverseUnitGraph = constructGraph(grammar, nullables)

            isMember = cyk_parser_LangeLeiss(grammar, inverseUnitGraph, sentence_input)

            duration = time() - now

            if(isMember):
                print("The sentence " + sentence_input + " belongs to the grammar.")
            else:
                print("The sentence " + sentence_input + " DOES NOT belongs to the grammar.")

            print("Duration: " + str(duration) + " s")

            helper.create_output(filename, grammar, sentence_input, isMember, duration,True, nullables, inverseUnitGraph)

    """ g = Grammar()
    g.readGrammar('test')
    #g.readGrammar('test_LangeLeiss')
    #g.print()
    #grammar = cfgToCnf(g) # to Chomsky
    grammar = cfgTo2nf(g) # to binary form
    #print(grammar)

   
   

    print("CHEGOU AQ!")

    null = nullable(grammar)
    print("Null: ", end="")
    print(null)
    print("Inverse Unit Graph: ",end="")
    graph = constructGraph(grammar, null)
    print(graph)
    print("Rules: ", end="")
    print(grammar.rules)

    #sentence_1 = "(a0+b)*a"
    sentence_1 = "cbaaa"
    print("Sentence: " + sentence_1)

    #print(discoverReach(graph, ['c']))

    isMember = cyk_parser_LangeLeiss(grammar, graph, sentence_1)
    print(isMember)
    #print("Pertence:", cyk_alg(terms=term, varies=var, inp=sentence_1)) """



""" 
    term = helper.findRulesRelatedToTerminals(g)
    var = helper.findRulesRelatedToVariables(g)
    print(term)
    print(var)
    sentence_1 = "aaacb"
    isMember = cyk_parser(g, sentence_1)
    print("Is member?", isMember)
    pprint.pprint(isMember)  """