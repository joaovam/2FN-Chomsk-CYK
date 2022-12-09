# Function to perform the CYK Algorithm
import helper
import pprint
from Grammar import Grammar


def cyk_parser(grammar, sentence):
    terms = helper.findRulesRelatedToTerminals(grammar)
    vars = helper.findRulesRelatedToVariables(grammar)

    n = len(sentence)
    r = len(grammar.variables)

    table = [[[] for _ in range(n)] for _ in range(n)]
    # pprint.pprint(table)
    for i in range(0, n):
        terminal = sentence[i]
        for rule in terms:
            if terminal in rule[1]:
                # print(i, j)
                table[i][i].append(rule[0])

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            table[i][j].clear()
            for h in range(i, j):
                for rule in vars:
                    A = rule[0]
                    B = rule[1][0]
                    C = rule[1][1]

                    if B in table[i][h] and C in table[h + 1][j]:
                        table[i][j].append(A)

    return grammar.variables[0] in table[0][n - 1]


def nullable(grammar):
    null = []
    todo = []

    vars = helper.findRulesRelatedToVariables(grammar)

    oneVar = []
    twoVar = []

    occurs = {}

    for var in grammar.variables:
        occurs[var] = []

    for lhs, rhs in vars:
        if len(rhs) == 1:
            oneVar.append((lhs, rhs))
        else:
            twoVar.append((lhs, rhs))

    for rhs, lhs in oneVar:
        occurs[lhs].append(rhs)

    for rhs, lhs in twoVar:
        occurs[lhs[0]].append((rhs, lhs[1]))

        occurs[lhs[1]].append((rhs, lhs[0]))

    for rhs, lhs in grammar.rules:
        if lhs[0] == "$":
            null.append(rhs)
            todo.append(rhs)

    while len(todo) > 0:

        B = todo.pop()

        X = occurs[B]
        foundTuples = []
        for rules in X:
            if type(rules) is tuple:
                foundTuples.append(rules)
            for tuples in foundTuples:
                if tuples[0] in X:
                    null.append(tuples[0])
                    todo.append([tuples[0]])
    return null

def constructGraph(grammar, nullables):
    graph = []

    for rhs,lhs in grammar.rules:
        if len(lhs) > 1:
            if lhs[0] in nullables:
                if lhs[1] in grammar.terminals:
                    graph.append((lhs[1], rhs))

            elif lhs[1] in nullables:
                if lhs[0] in grammar.terminals:
                    graph.append((lhs[0], rhs))

        else:
            graph.append((lhs, rhs))

    return graph