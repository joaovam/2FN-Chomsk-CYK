class Grammar:
    def __init__(self):

        self.rules = []
        self.terminals = []
        self.variables = []

    def readGrammar(self, filename):  # $ == lambda



        with open(filename, 'r', encoding='utf8') as file:
            self.variables = file.readline().strip().split(" ")
            self.terminals = file.readline().strip().split(" ")

            for line in file:
                if line == '*':
                    break

                variable, rules = line.strip().split('->')

                for rule in rules:
                    rule = rule.split("|")
                    x = []
                    for r in rule:
                        if r.strip() != '':
                            x.append(r)
                    if len(x) > 0:
                        self.rules.append((variable, x))


    def print(self):
        print("Variables:")
        print(self.variables)

        print("Terminals:")
        print(self.terminals)

        print("Rules:")
        for lhs, rhs in self.rules:
            print(f"{lhs} -> {' '.join(rhs)}")







def cfgToCnf(grammar: Grammar):
    # Convert the grammar to CNF
    cnf_grammar = convert_to_cnf(grammar.rules)

    # Print the resulting CNF grammar


    # Helper function for generating new non-terminal symbols


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
