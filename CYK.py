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
    print("Vars: " + str(vars))

    oneVar = []
    twoVar = []

    occurs = {}

    for var in grammar.variables:
        occurs[var] = []

    for lhs, rhs in vars:
        if len(rhs) == 1 and rhs[0] in grammar.variables:
            oneVar.append((lhs[0], rhs[0]))
        elif len(rhs) == 2 and rhs[0] in grammar.variables and rhs[1] in grammar.variables:
            twoVar.append((lhs[0], rhs))

    for lhs, rhs in oneVar:
        print(lhs)
        # if lhs not in occurs.keys():
        #     occurs[lhs] = []
        occurs[rhs].append(lhs)

    for lhs, rhs in twoVar:
        # if lhs[0] not in occurs.keys():
        #     occurs[lhs[0]] = []
        # if lhs[1] not in occurs.keys():
        #     occurs[lhs[1]] = []
        occurs[rhs[0]].append((lhs, rhs[1]))

        occurs[rhs[1]].append((lhs, rhs[0]))

    for lhs, rhs in grammar.rules:
        if rhs[0] == "$":
            null.append(lhs)
            todo.append(lhs)

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
    graph = {}

    for lhs, rhs in grammar.rules:
        if len(rhs) > 1:
            if rhs[0] in nullables:
                if rhs[1] in grammar.terminals:
                    if(graph.get(rhs[1]) == None):
                        graph[rhs[1]] = []
                    graph[rhs[1]].append(lhs)

            if rhs[1] in nullables:
                if rhs[0] in grammar.terminals:
                    if(graph.get(rhs[0]) == None):
                        graph[rhs[0]] = []
                    graph[rhs[0]].append(lhs)

        else:
            if rhs[0] in grammar.terminals:
                if(graph.get(rhs[0]) == None):
                        graph[rhs[0]] = []
                graph[rhs[0]].append(lhs)

    return graph

def dfs(graph, node):  #function for dfs 
    if(graph.get(node) == None):
        return [node]
    
    visited = [node]
    togo = [node]

    for i in range(0, len(node)):
        togo.append(graph[node][i])
        visited.append(graph[node][i])

    while len(togo) != 0:
        next = togo.pop()
        if graph.get(next) != None:
            for edge in range(0,len(graph[next])):
                vertex = graph[next][edge]
                if vertex not in visited:
                    togo.append(vertex)
                    visited.append(vertex)
    
    return visited

def discoverReach(graph, word_list):
    canReach = set()
    for node in word_list:
        visited = dfs(graph, node)
        for i in range(0, len(visited)):
            canReach.add(visited[i])
    canReach.discard(visited[0])

    return list(canReach)


def cyk_parser_LangeLeiss(grammar, graph, word):
    terms = helper.findRulesRelatedToTerminals(grammar)
    vars = helper.findRulesRelatedToVariables(grammar)

    n = len(word)
    r = len(grammar.variables)

    table = [[[] for _ in range(n)] for _ in range(n)]
    tablePrime = [[[] for _ in range(n)] for _ in range(n)]
    # pprint.pprint(table)
    for i in range(0, n):
        terminal = word[i]
        for rule in terms:
            reach = discoverReach(graph, [word[i]])
            if len(reach) > 1:
                table[i][i] = reach

                
    print("Table: ")
    for i in range(0, n):
        for j in range(0, n):
            print(table[i][j], end="")
        print("")
    print("")

    print("TablePrime: ")
    for i in range(0, n):
        for j in range(0, n):
            print(tablePrime[i][j], end="")
        print("")
    print("")


    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            tablePrime[i][j].clear()
            for h in range(i, j):
                for rule in grammar.rules:
                    if(len(rule[1]) == 2):
                        #print("I: " + str(i) + " H:" + str(h) + " J: "+ str(j) )
                        #print("RULE: " + str(rule))
                        
                        A = rule[0]
                        B = rule[1][0]
                        C = rule[1][1]

                        #print("A: " + str(A) + "\nB: "+ str(B) + "\nC: "+ str(C))

                        if B in table[i][h] and C in table[h + 1][j]:
                            tablePrime[i][j].append(A)
            table[i][j] = discoverReach(graph, tablePrime[i][j])

    print("Table: ")
    for i in range(0, n):
        for j in range(0, n):
            print(table[i][j], end="")
        print("")
    print("")

    print("TablePrime: ")
    for i in range(0, n):
        for j in range(0, n):
            print(tablePrime[i][j], end="")
        print("")
    print("")

    return grammar.variables[0] in table[0][n - 1]