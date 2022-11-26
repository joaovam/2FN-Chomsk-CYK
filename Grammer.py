class Grammer:
    def __init__(self):

        self.variables = []
        self.alphabet = []
        self.rules = {}
        self.startSymbol = ""

    def readGrammer(self, filename):#$ == lambda, simbo
        with open(filename, 'r', encoding='utf8') as file:

            self.variables = file.readline().strip().split(" ")

            self.startSymbol = self.variables[0]

            self.alphabet = file.readline().strip().split(" ")

            if set(self.variables) & set(self.alphabet):
                print("Variables and alphabet cannot have any elements in common!")
                exit(1)

            print(self.variables)
            print(self.alphabet)
            for line in file:
                if line == '*':
                    break
                variable, rules = line.split('->')
                self.rules[variable.strip()] = [rule.strip() for rule in rules.split('|')]

            print(self.rules)
    def print(self):
        print("Start symbol = {}".format(self.startSymbol))
        for key,value in self.rules.items():
            print(f'{key} -> {"".join([val+" | " for val in value])}')



def convertToChownsky(gramatic:Grammer):
    i = 0
    while(1):
        if "S{}".format(i) in gramatic.variables:
            i = i+1
        else:
            newStart = "S{}".format(i)
            gramatic.variables.append(newStart)
            gramatic.rules[newStart] = list(gramatic.startSymbol)
            gramatic.startSymbol = newStart
            break

def removeLambdaProductions():


def removeUnitProductions():

def removeUselessProductions():


