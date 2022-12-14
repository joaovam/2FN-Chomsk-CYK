import re
import itertools

left, right = 0, 1


def union(lst1, lst2):
    final_list = list(set().union(lst1, lst2))
    return final_list


def loadModel(modelPath):
    file = open(modelPath).read()
    K = (file.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", ""))
    V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n", "").replace("\n", ""))
    P = (file.split("Productions:\n")[1])

    return cleanAlphabet(K), cleanAlphabet(V), cleanProduction(P)


# Make production easy to work with
def cleanProduction(expression):
    result = []
    # remove spaces and explode on ";"
    rawRulse = expression.replace('\n', '').split(';')

    for rule in rawRulse:
        # Explode evry rule on "->" and make a couple7
        leftSide = rule.split(' -> ')[0].replace(' ', '')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
            result.append((leftSide, term.split(' ')))
    return result


def cleanAlphabet(expression):
    return expression.replace('  ', ' ').split(' ')


def seekAndDestroy(target, productions):
    trash, ereased = [], []
    for production in productions:
        if target in production[right] and len(production[right]) == 1:
            trash.append(production[left])
        else:
            ereased.append(production)

    return trash, ereased


def setupDict(productions, variables, terms):
    result = {}
    for production in productions:
        #
        if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result


def rewrite(target, production):
    result = []
    # get positions corresponding to the occurrences of target in production right side
    # positions = [m.start() for m in re.finditer(target, production[right])]
    positions = [i for i, x in enumerate(production[right]) if x == target]
    # for all found targets in production
    for i in range(len(positions) + 1):
        # for all combinations of all possible lenght phrases of targets
        for element in list(itertools.combinations(positions, i)):
            # Example: if positions is [1 4 6]
            # now i've got: [] [1] [4] [6] [1 4] [1 6] [4 6] [1 4 6]
            # erease position corresponding to the target in production right side
            tadan = [production[right][i] for i in range(len(production[right])) if i not in element]

            if tadan != []:
                result.append((production[left], tadan))
    return result


def dict2Set(dictionary):
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    return result


def pprintRules(rules):
    for rule in rules:
        tot = ""
        for term in rule[right]:
            tot = tot + " " + term
        print(rule[left] + " -> " + tot)


def prettyForm(rules):
    dictionary = {}
    for rule in rules:
        if rule[left] in dictionary:
            dictionary[rule[left]] += ' | ' + ' '.join(rule[right])
        else:
            dictionary[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dictionary:
        result += key + " -> " + dictionary[key] + "\n"
    return result


def startingRuleFirst(grammar):
    for rule in grammar.rules:
        if rule[0] == grammar.initial:
            initial_rule = rule
            grammar.rules.remove(rule)
            grammar.rules.insert(0, initial_rule)

    grammar.variables.remove(grammar.initial)
    grammar.variables.insert(0, grammar.initial)

    return grammar

def findRulesRelatedToTerminals(grammar):
    X = []
    for lhs, rhs in grammar.rules:
        for x in rhs:
            if len(x) == 1:
                if x in grammar.terminals:
                    X.append((lhs, rhs))
    return X


def findRulesRelatedToVariables(grammar):
    X = []
    for lhs, rhs in grammar.rules:

        if rhs[0] in grammar.variables:
            if len(rhs) > 1:
                if rhs[0] in grammar.variables or rhs[1] in grammar.variables:
                    X.append((lhs, rhs))
            else:
                X.append((lhs, rhs))
        elif len(rhs) > 1:
            if rhs[1] in grammar.variables:
                if rhs[0] in grammar.variables or rhs[1] in grammar.variables:
                    X.append((lhs, rhs))
            
    return X

def create_output(filename, grammar, sentence, isMember, duration,isMod=False,nullables=None, inverseUnitGraph=None):
    folder,file_output = filename.split("/")
    
    file_output = file_output.split(".")[0] + "_output.txt" if '.' in file_output else file_output + "_output.txt"
    file_output = "CYK_" + file_output if not isMod else "CYK_Mod_" + file_output
    foutput = open(folder + "/" + file_output, "w")

    array_output = [f'''
Grammar:

Variables: {str(grammar.variables)} 
Terminals: {str(grammar.terminals)} 
Rules: {str(grammar.rules)} 

Sentence: {str(sentence)}
''']

    foutput.writelines(array_output)

    if(nullables != None and inverseUnitGraph != None):
        array_output = [f'''
Nullables: {str(nullables)}
Inverse Unit Graph: {str(inverseUnitGraph)}

''']
        foutput.writelines(array_output)
    
    if(isMember):
        foutput.write("The sentence " + sentence + " belongs to the grammar.")
    else:
        foutput.write("The sentence " + sentence + " DOES NOT belongs to the grammar.")

    foutput.write("\nDuration: " + str(duration) + " s")

    foutput.close()
        
def create_output_experiment(filename, grammar, information, isMod=False):
    folder,file_output = filename.split("/")
    
    file_output = file_output.split(".")[0] + "_output.txt" if '.' in file_output else file_output + "_output.txt"
    file_output = "CYK_" + file_output if not isMod else "CYK_Mod_" + file_output
    foutput = open("output/" + file_output, "w")

    array_output = [f'''
Grammar:

Variables: {str(grammar.variables)} 
Terminals: {str(grammar.terminals)} 
Rules: {str(grammar.rules)} 

''']

    foutput.writelines(array_output)

    total_time = 0
    for info in information:
        foutput.write("\n|W|: " + str(info[0]) + "      Duration: " + str(info[1]))
        total_time += info[1]
    
    foutput.write("\nAverage time: " + str(total_time/len(information)) + " s")

    foutput.close()
