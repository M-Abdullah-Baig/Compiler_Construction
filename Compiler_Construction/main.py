
from lexicalAnalyzer import generateOuput, classifyToken, breakWords
from func_file import syntaxAnalyzer
from Semantic_Analyzer1 import semanticAnalyzer


with open("source_file.txt", "r") as inputfile:
    input_text = inputfile.read()

tokenList = classifyToken(breakWords(input_text))
with open("output_tokens_file.txt", "w") as outputfile:
        outputfile.write(generateOuput(tokenList))

#Syntax checking
synError, check = syntaxAnalyzer(tokenList)
if (check):
    print("\nSyntax Result : No Syntax Error")
    print("\n-----Source File (INPUT) COMPLETELY PARSED WITH COMPLETE TREE----\n")

else:
    print("\n-----SYNTAX ERROR-----")
    print("ERROR:",synError)

    with open("output_syntax_error_file.txt", "w") as outputfile:
        outputfile.write(synError)
        #outputfile.write(generateOuput(tokenList))


# Semantic Checking        
semantic_analyzer = semanticAnalyzer(tokenList)
print("Semantic Analyzer", semantic_analyzer)
