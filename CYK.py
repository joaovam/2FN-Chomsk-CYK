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

    # pprint.pprint(table)

# def cyk_parser(grammar, sentence):
#     """
#     implementation of CYK algorithm
#     :param vars: rules related to variables
#     :param terms: rules related to terminals
#     :param sentence: input string
#     :return: resulting table
#     """
#
#     terms = helper.findRulesRelatedToTerminals(grammar)
#     vars = helper.findRulesRelatedToVariables(grammar)
#
#     n = len(sentence)
#     r = len(grammar.variables)
#     backtrack = []
#
#     table = [[[False for _ in range(r)]for _ in range(n)] for _ in range(n)]
#     #pprint.pprint(table)
#
#     for i in range(0, n):
#         terminal = sentence[i]
#         for rule in terms:
#             if terminal in rule[1]:
#                 j = grammar.variables.index(rule[0])
#                 #print(i, j)
#                 table[i][0][j] = True
#     print("AFTER first iter")
#     pprint.pprint(table)
#     print("==================================")
#
#     for i in range(1, n):
#         for j in range(0, n - i + 1):
#             for k in range(1, i-1):
#
#                 for rule in vars:
#                     A = grammar.variables.index(rule[0])
#                     B = grammar.variables.index(rule[1][0])
#                     C = grammar.variables.index(rule[1][1])
#                     #print(i, j, k)
#                     if table[j][k][B] and table[j+k][i-k][C]:
#                         pprint.pprint(table)
#                         table[j][i][A] = True
#                         backtrack.append((rule[0], [rule[1]]))
#     #pprint.pprint(table)
#     for i in range(0, r):
#         print(n,i)
#         if table[0][n-1][i]:
#             print(backtrack)
#             return True
#
#     return False


# def cyk_alg(varies, terms, inp):
#     """
#     implementation of CYK algorithm
#     :param varies: rules related to variables
#     :param terms: rules related to terminals
#     :param inp: input string
#     :return: resulting table
#     """
#
#     length = len(inp)
#     var0 = [va[0] for va in varies]
#     var1 = [va[1] for va in varies]
#
#     # table on which we run the algorithm
#     table = [[set() for _ in range(length-i)] for i in range(length)]
#
#     # Deal with variables
#     for i in range(length):
#         for te in terms:
#             if inp[i] == te[1]:
#                 table[0][i].add(te[0])
#
#     # Deal with terminals
#     # its complexity is O(|G|*n^3)
#     for i in range(1, length):
#         for j in range(length - i):
#             for k in range(i):
#                 row = create_cell(table[k][j], table[i-k-1][j+k+1])
#                 for ro in row:
#                     if ro in var1:
#                         table[i][j].add(var0[var1.index(ro)])
#
#     # if the last element of table contains "S" the input belongs to the grammar
#     for x in table:
#         for y in x:
#             for z in y:
#                 print(z)
#     return table

# def create_cell(first, second):
#     """
#     creates set of string from concatenation of each character in first
#     to each character in second
#     :param first: first set of characters
#     :param second: second set of characters
#     :return: set of desired values
#     """
#     res = set()
#     if first == set() or second == set():
#         return set()
#     for f in first:
#         for s in second:
#             res.add(f+s)
#     return res
