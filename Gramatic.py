class Gramatic:
    def __init__(self):

        self.variables = []
        self.alphabet = []
        self.rules = {}

    def readGramatic(self, filename):#$ == lambda
        with open(filename, 'r', encoding='utf8') as file:

            self.variables = file.readline().strip().split(" ")
            self.alphabet = file.readline().strip().split(" ")
            print(self.variables)
            print(self.alphabet)
            for line in file:
                if line == '*':
                    break
                variable, rules = line.split('->')
                self.rules[variable.strip()] = [rule.strip() for rule in rules.split('|')]

            print(self.rules)




    #A -> sA
