import CFG2CNF as f2c
import helper

class Grammar:
    def __init__(self):

        self.rules = []
        self.terminals = []
        self.variables = []
        self.initial = ""

    def readGrammar(self, filename):  # $ == lambda

        self.terminals, self.variables, self.rules = helper.loadModel(filename)

        """ with open(filename, 'r', encoding='utf8') as file:
            self.variables = file.readline().strip().split(" ")
            self.terminals = file.readline().strip().split(" ")

            for line in file:
                if line == '*':
                    break

                variable, rules = line.strip().split('->')

                for rule in rules:
                    rule = rule.split("|")
                    x = []
                    if isinstance(rules, list):
                        for r in rule:
                            if r.strip() != '':
                                x.append(r)
                        if len(x) > 0:
                            self.rules.append((variable, x))
                    else:
                        self.rules.append((variable, rule)) """


    def print(self):
        print("Variables:")
        print(self.variables)

        print("Terminals:")
        print(self.terminals)

        print("Rules:")
        print(helper.prettyForm(self.rules))






def cfgToCnf(grammar: Grammar):
    # Convert the grammar to CNF
    # cnf_grammar = convert_to_cnf(grammar.rules)
    f2c.defineVariable(grammar.variables)

    # print("STEP 1: " + str(grammar.rules))
    grammar.rules, grammar.initial = f2c.START(grammar.rules, variables=grammar.variables)
    # print("STEP 2: " + str(grammar.rules))
    grammar.rules = f2c.TERM(grammar.rules, variables=grammar.variables, terminals=grammar.terminals)
    # print("STEP 3: " + str(grammar.rules))
    grammar.rules = f2c.BIN(grammar.rules, variables=grammar.variables,)
    # print("STEP 4: " + str(grammar.rules))
    grammar.rules = f2c.DEL(grammar.rules)
    # print("STEP 5: " + str(grammar.rules))
    grammar.rules = f2c.UNIT(grammar.rules, variables=grammar.variables,)
    # print("STEP 6: " + str(grammar.rules))
    
    grammar = helper.startingRuleFirst(grammar)
    # Print the resulting CNF grammar

    # Helper function for generating new non-terminal symbols

def cfgTo2nf(grammar: Grammar):

    f2c.defineVariable(grammar.variables)

    grammar.rules = f2c.BIN(grammar.rules, variables=grammar.variables)

    print(grammar.variables)
    print(grammar.terminals)
    print(grammar.rules)
    
    #grammar = helper.startingRuleFirst(grammar)

def new_symbol(symbols):
    return f"S_{len(symbols)}"

    # Function for converting a grammar to CNF form


def convert_to_cnf(grammar):
    cnf_grammar = []
    symbols = set()

    # Iterate over the production rules in the grammar
    for lhs, rhs in grammar:
        # Handle rules with more than two non-terminal symbols on the right-hand side
        if len(rhs) > 2:
            # Split the rule into multiple rules with exactly two non-terminal symbols on the right-hand side
            for i in range(1, len(rhs) - 1):
                new_lhs = new_symbol(symbols)
                cnf_grammar.append((lhs, [rhs[i - 1], new_lhs]))
                lhs = new_lhs
                symbols.add(lhs)
            cnf_grammar.append((lhs, [rhs[-2], rhs[-1]]))

        # Handle rules with a terminal symbol on the right-hand side
        elif len(rhs) == 1 and not rhs[0].islower():
            # Add a new non-terminal symbol and split the rule into two rules
            new_lhs = new_symbol(symbols)
            cnf_grammar.append((lhs, [rhs[0], new_lhs]))
            cnf_grammar.append((new_lhs, [rhs[0]]))
            symbols.add(new_lhs)

        # Handle all other rules
        else:
            cnf_grammar.append((lhs, rhs))

    # Return the resulting CNF grammar
    return cnf_grammar
