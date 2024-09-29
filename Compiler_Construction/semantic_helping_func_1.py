
memberTable_=[]
mainTable_ = []
functionTable_ = []
scopeStack = [0]
highestScope = 0

typeCompatibility = {
    "intint+": "int",
    "INTINT+": "int",
    "INTint+": "int",
    "intint-": "int",
    "INTINT-": "int",
    "INTint-": "int",
    "intint*": "int",
    "INTINT*": "int",
    "INTint*": "int",
    "intint/": "int",
    "INTINT/": "int",
    "INTint/": "int",
    "intint%": "int",
    "INTINT%": "int",
    "INTint%": "int",
    "intINT=": "int",
    "intint==": " bool",
    "intint!=": "bool",
    "intint<=": "bool",
    "intint<": "bool",
    "intint>": "bool",
    "intint>=": "bool",
    "intfloat+": "float",
    "FLTFLT+": "float",
    "FLTfloat+": "float",
    "intfloat-": "float",
    "FLTFLT-": "float",
    "FLTfloat-": "float",
    "intfloat*": "float",
    "FLTFLT*": "float",
    "FLTfloat*": "float",
    "intfloat/": "float",
    "FLTFLT/": "float",
    "FLTfloat/": "float",
    "FLTint+"  : "float",
    "floatINT=": "int",
    "intfloat==": "bool",
    "intfloat!=": "bool",
    "intfloat<=": "bool",
    "intfloat<": "bool",
    "intfloat>": "bool",
    "intfloat>=": "bool",
    "intchar+": "int",  #Check the char type compatibility with others as char is considered as ASCII codes in python
    "intchar-": "int",
    "intchar*": "int",
    "intchar/": "int",
    "intchar%": "int",
    "intchar=": "int",
    "intchar==": "bool",
    "intchar!=": "bool",
    "intchar<=": "bool",
    "intchar<": "bool",
    "intchar>": "bool",
    "intchar>=": "bool",
    "intbool+": "int",
    "intbool-": "int",
    "intbool*": "int",
    "intbool/": "int",
    "intbool%": "int",
    "intbool=": "int",
    "intbool==":  "bool",
    "intbool!=": "bool",
    "intbool<=": "bool",
    "intbool<": "bool",
    "intbool>": "bool",
    "intbool>=": "bool",
    "floatfloat+": "float",
    "floatfloat-": "float",
    "floatfloat*": "float",
    "floatfloat/": "float",
    "FLTfloat=": "float",
    "floatfloat==": "bool",
    "floatfloat!=": "bool",
    "floatfloat<=": "bool",
    "floatfloat<": "bool",
    "floatfloat>": "bool",
    "floatfloat>=": "bool",
    "floatchar+": "float",
    "floatchar-": "float",
    "floatchar*": "float",
    "floatchar/": "float",
    "floatchar%": "float",
    "floatchar=": "float",
    "floatchar==": "bool",
    "floatchar!=": "bool",
    "floatchar<=": "bool",
    "floatchar<": "bool",
    "floatchar>": "bool",
    "floatchar>=": "bool",
    "floatbool+": "float",
    "floatbool-": "float",
    "floatbool*": "float",
    "floatbool/": "float",
    "floatbool=": "bool",
    "floatbool==": "bool",
    "floatbool!=": "bool",
    "floatbool<=": "bool",
    "floatbool<": "bool",
    "floatbool>": "bool",
    "floatbool>=": "bool",
    "stringstring+": "string",
    "stringSTR=":  "string",
    "stringstring==": "bool",
    "stringstring!=": "bool",
    "stringstring<=": "bool",
    "stringstring<": "bool",
    "stringstring>": "bool",
    "stringstring>=": "bool",
    "stringint=": "int",
    "stringfloat=": "int",
    "stringchar+": "string",
    "stringCHAR=": "string",
    "stringbool=": "string",
    "charchar+": "int",
    "CHARCHAR+": "int",
    "CHARchar+": "int",
    "charchar-": "int",
    "charchar*": "int",
    "charchar/": "int",
    "charchar%": "int",
    "charCHAR=": "char",
    "charchar==": "bool",
    "charchar!=": "bool",
    "charchar<=": "bool",
    "charchar<": "bool",
    "charchar>": "bool",
    "charchar>=": "bool",
    "charint+": "char",
    "charint-": "char",
    "charint*": "char",
    "charint/": "char",
    "charint%": "int",
    "charint=": "char",
    "charint==": "bool",
    "charint!=": "bool",
    "charint<=": "bool",
    "charint<": "bool",
    "charint>": "bool",
    "charint>=": "bool",
    "charfloat+": "float",
    "charfloat-": "float",
    "charfloat*": "float",
    "charfloat/": "float",
    "charfloat=": "char",
    "charfloat==": "bool",
    "charfloat!=": "bool",
    "charfloat<=": "bool",
    "charfloat<": "bool",
    "charfloat>": "bool",
    "charfloat>=": "bool",
    "charstring+": "string",
    "charbool+":  "int",
    "charbool-": "int",
    "charbool*": "int",
    "charbool/": "int",
    "charbool%": "int",
    "charbool=": "char",
    "charbool==": "bool",
    "charbool!=": "bool",
    "charbool<=": "bool",
    "charbool<": "bool",
    "charbool>": "bool",
    "charbool>=": "bool",
    "boolbool+": "bool",
    "boolbool-": "bool",
    "boolbool*": "bool",
    "boolbool/": "bool",
    "boolbool%": "bool",
    "boolbool=": "bool",
    "boolbool==": "bool",
    "boolbool!=": "bool",
    "boolbool<=": "bool",
    "boolbool<": "bool",
    "boolbool>": "bool",
    "boolbool>=": "bool",
    "boolbool&": "bool",
    "boolbool|": "bool",
    "boolint+": "int",
    "boolint-": "int",
    "boolint*": "int",
    "boolint/": "int",
    "boolint%": "int",
    "boolint=": "bool",
    "boolint==": "bool",
    "boolint!=": "bool",
    "boolint<=": "bool",
    "boolint<": "bool",
    "boolint>": "bool",
    "boolint>=": "bool",
    "boolfloat-": "float",
    "boolfloat*": "float",
    "boolfloat/": "float",
    "boolfloat%": "float",
    "boolfloat=": "bool",
    "boolfloat==": "bool",
    "boolfloat!=": "bool",
    "boolfloat<=": "bool",
    "boolfloat<": "bool",
    "boolfloat>": "bool",
    "boolfloat>=": "bool",
    "boolchar+": "int",
    "boolchar-": "int",
    "boolchar*": "int",
    "boolchar/": "int",
    "boolchar%": "int",
    "boolchar=": "bool",
    "boolchar==": "bool",
    "boolchar!=": "bool",
    "boolchar<=": "bool",
    "boolchar<": "bool",
    "boolchar>": "bool",
    "boolchar>=": "bool",
#    "char!": "bool",
#    "int!": "bool",
    "int++": "int",
    "int--": "int",
#    "float!": "bool"
}



class mainTable:        # Definition Table
    def __init__(self, name, ofType, accessMod, typeMod, parent):
        self.name = name
        self.type = ofType
        self.accessMod = accessMod
        self.typeMod = typeMod
        self.parent = parent
        self.memTable = []


class memberTable:       # Member Table
    def __init__(self, name, params, ofType, accessMod, typeMod, const):
        self.name = name
        self.params = params
        self.type = ofType
        self.accessMod = accessMod
        self.typeMod = typeMod
        self.const = const


class functionTable:          # Symbol Table 
    def __init__(self, name, ofType, scope):
        self.name = name
        self.type = ofType
        self.scope = scope


def lookupMainTable(name):
    x = next((j for j in mainTable_ if j.name == name), "")
    if (x == ""):
        return False
    # print("\tLookUp Main Table")
    # print(vars(x))          vars() is a built-in function that returns the __dict__ attribute of an object.
    return x


def insertMainTable(name, ofType, accessMod, typeMod, parent):
    if (lookupMainTable(name) == False):
        obj = mainTable(name, ofType, accessMod, typeMod, parent)
        mainTable_.append(obj)
        # print("\tMain Table")
        # # for t in mainTable:
        # print(vars(t))
        return True
    return False

def lookupMemberTable(name, paramList, ofName):
    x = lookupMainTable(ofName)
    if x:
        if paramList=="":  # Variable checking
            print("3333333333333333333333333")  # variable checking
            for j in x.memTable:
                print("yyyyyyyyyyyyyyyyyyyyy")
                print("j.name"+j.name)
                print("name : ",name)
                print("8888888888888888888888")
                if j.name == name:
                    print(name + "3454")
                    print(paramList + "67676")
                    print(ofName + "89898")
                    print("lololololo")
                    print("Lookup Member table")
                    print(vars(j))
                    return j
                

            print("65555555556565")
            print("uuuuuuuuuuuu")
            return False
        else:  # Function checking
            for j in x.memTable:
                if j.name == name and j.params == paramList:
                    print("Lookup Member table")
                    print(vars(j))
                    return j

            return False

    return False


# def lookupMemberTable(name, paramList, ofName):         # ref of class name : ofName
#     x = lookupMainTable(ofName)
#     if (x != False):
#         if (paramList == ""):  
#             print("3333333333333333333333333")              # variable checking
#             y = next((j for j in x.memTable if j.name == name), "")
#             print(name+"3454")
#             print(paramList+"67676")
#             print(ofName+"89898")
#             if (y == ""):
#                 print("65555555556565")
#                 return False
#             # print("\tLookUp mem Table")
#             # print(vars(y))
#             print("lololololo")
#             return y
#         else:                             # function checking
#             y = next((j for j in x.memTable if j.name ==
#                      name and j.params == paramList), "")
#             if (y == ""):
#                 return False
#             # print("\tLookUp mem Table")
#             # print(vars(y))
#             return y
#     return False


def insertMember(name, params, ofType, accessMod, typeMod, const, ofName):
    if(lookupMemberTable(name, params, ofName) == False):
        for i in mainTable_:
            if i.name == ofName:
                print("666666666666666666666666666666666")
                obj = memberTable(name, params, ofType,
                                     accessMod, typeMod, const)
                print("555555555555555555555555555555555")
                i.memTable.append(obj)
                print("4444444444444444444444444444444444444")
                print("\tMem Table")
                for t in i.memTable:
                    print(vars(t))
                return True
    return False

# def lookupMemberTable(name, paramList, ofName):         # ref of class name : ofName
#     x = lookupMainTable(ofName)
#     if (x != False):
#         if (paramList == ""):                # variable checking
#             y = next((j for j in x.memTable if j.name == name), "")
#             if (y == ""):
#                 return False
#             print("\tLookUp mem Table")
#             print(vars(y))
#             return y
#         else:                             # function checking
#             y = next((j for j in x.memTable if j.name ==
#                      name and j.params == paramList), "")
#             if (y == ""):
#                 return False
#             print("\tLookUp mem Table")
#             print(vars(y))
#             return y
#     return False


# def insertMember(name, params, ofType, accessMod, typeMod, const, ofName):
#     if(lookupMemberTable(name, params, ofName) == False):
#         for i in mainTable_:
#             if i.name == ofName:
#                 # i.memberTable_.append(i.name,i.p
#                 obj = memberTable(name, params, ofType,
#                                      accessMod, typeMod, const)
#                 memberTable_.append(obj)
#                 # print("\tMem Table")
#                 # for t in i.memberTable_:
#                 # print(vars(memberTable_))
#                 return True
#     return False

'''
def lookupFunctionTable(name):
    for i in scopeStack:
        x = next((j for j in functionTable_ if j.scope ==
                 i and j.name == name), "")
        
        if (x != ""):
            print("\tLookUp Func Table")
            print(vars(x))
            print("i", i)
            #print("j", j.scope)
            return x.type
    return False
'''
'''
def lookupFunctionWithType(name, typeToCheck):
    for i in scopeStack:
        x = next((j for j in functionTable_ if j.scope == i and j.name == name and j.type == typeToCheck), "")

        if (x != ""):
            print("\tLookUp Func Table")
            print(vars(x))
            print("i", i)
            return x.type

    return False
'''
'''
def lookupFunctionTable(name):
    for i in scopeStack:                # 0 1
        print("i", i)
        for j in functionTable_: 
            print("j=", j)            # 0 1 0
            if j.currentScope == i and j.name == name:  #0==0  1==1
                print("i", i)
                print("j.name", j.name)
                print("j", j.scope)
                print("\tLookUp Func Table")
                print(vars(j))
                return j.type
        
    return False
'''

def lookupFunctionTable(name, current_scope):
    for entry in functionTable_:
        if entry.scope == current_scope and entry.name == name:
            print("\tLookUp Func Table")
            print("PPP")
            print(vars(entry))
            return entry.type
    
    return False

def lookupFunctionWithType(name, typeToCheck, current_scope):
    for entry in functionTable_:
        if entry.scope == current_scope and entry.name == name and entry.type == typeToCheck:
            print("\tLookUp Func Table")
            print("IOIO")
            print(vars(entry))
            return entry.type
    return False
    

def insertFunctionTable(name, ofType, scope):
    if(lookupFunctionTable(name, scope) == False):
        obj = functionTable(name, ofType, scope)
        functionTable_.append(obj)
        #print("\tFunction Table")
        #for t in functionTable:
        #    print(vars(t))
        return True
    return False

def insertFunctionTableWithType(name, ofType, scope):
    if(lookupFunctionWithType(name, ofType, scope) == False):
        obj = functionTable(name, ofType, scope)
        functionTable_.append(obj)
        #print("\tFunction Table")
        #for t in functionTable:
        #    print(vars(t))
        return True
    return False

def createScope():
    global highestScope
    highestScope += 1
    x = highestScope
    # print("createdScope:\t", x)
    scopeStack.insert(0, x)
    return scopeStack[0]


def destroyScope():
    x = scopeStack.pop(0)
    # print("destroyedScope:\t", x)
    return scopeStack[0]


def binTypeCompatible(left, right, op):
    check = left + right + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    check = right + left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False


def uniTypeCompatible(left, op):
    check = left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False


def createTypeExpression(returnType, *inputTypes):
    typeExpression = ", ".join(inputTypes) + " -> " + returnType
    return typeExpression

def plist( *inputTypes):
    typeExpression = ", ".join(inputTypes) 
    return typeExpression