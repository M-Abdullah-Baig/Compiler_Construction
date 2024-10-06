# import sys

from lexicalAnalyzer import token
from semantic_helping_func_1 import createScope, destroyScope,plist, insertMember, insertFunctionTable, insertMainTable, insertFunctionTableWithType, lookupMemberTable, lookupFunctionTable, lookupMainTable, lookupFunctionWithType, scopeStack, binTypeCompatible, uniTypeCompatible, mainTable_, functionTable_, createTypeExpression, memberTable_


i = 0
j = 0
k = 0
tokenList = []
# syntaxErr = True
error = ""
input_types=[]
accessModi = "private"
#access_Modi="private"
ofName=""
paramList=""
parentList=""
typeMod=""
pm=""
palist=""
over_ride=""
para=""

const_name=""
currentClass = ""
currentFunction = 0
currentScope = 0
ofType = ""
ofType1 = ""
op = ""
ofvalue = []
name = ""
ofType2 = ""
ofType3 = ""
#complist = []
check = ""
name1 = ""
op2 = ""
currentObj=""

def semanticAnalyzer(tokens):
    global i, tokenList
    i = 0
    tokenList = tokens
    result = start()
    print(report())
    return result



def report():
    global currentClass, currentFunction, currentScope, scopeStack, errorAt, mainTable_, functionTable_, error, memberTable_
    report = error + "\n"
#    report += "\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\n"
#    report += "\t\t\t\t\t\t  R\t  E\t  S\t  U\t  L\t  T\n"
#    report += "\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\t~~~~~\n\n"
#    report += "\nLast Updated Class:\t" + currentClass + "\n"
#    report += "Last Function Scope:\t" + str(currentFunction) + "\n"
#    report += "Scope @ End:\t\t" + str(currentScope) + "\n\n"
    report += "###########################################################################\n"
    report += "Main Table:\n\n"
    for i in mainTable_:
        report += "Name:\t\t'" + i.name + "'\nType:\t\t'" + i.type + \
           "'\nAccessMod:\t\t" + i.accessMod + "'\nTypeMod:\t'" + i.typeMod + "'\nParent:\t\t'" + i.parent + "'\n"
        report += "Member:\n"
    for j in memberTable_:
        report += str(vars(j))
        report += "\n"
    report += "-------------------------\n"
    report += "\n"
    report += "###########################################################################\n"
    report += "Function Table:\n\n"
    for i in functionTable_:
        report += str(vars(i))
        report += "\n"
    return report


def syntaxError():
    global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, errorAt
    return False

'''
def reDeclarationError(name, detail):
    global i, error
    error += "\n\t***  Re-Declaration Error  ***\n\tID:\t\t" + str(name) + "\n\tAs:\t\t" + \
        str(detail), "\n\tLine #:\t       ", str(tokenList[i].line) + "\n"
    return
'''

'''def reDeclarationError(name, detail):
    global i, error
    error += f"\n\t***  Re-Declaration Error  ***\n\tID:\t\t{name}\n\tAs:\t\t{detail}\n\tLine #:\t       {tokenList[i].line}\n"
    return'''

def reDeclarationError(name, message, scope):
    global i, error
    error += f"\n\t***  Re-Declaration Error  ***\n\tID:\t\t{name}\n\tAs:\t\t{message}\n\tScope:\t{scope}\n\tLine #:\t       {tokenList[i].line}\n"
    return


'''
def unDeclaredError(name, detail):
    global i, error
    error += "\n\t***  Un-Declared Error  ***\n\tID:\t\t" + name + "\n\tAs:\t\t" + \
        detail + "\n\tLine #:\t       " + str(tokenList[i].line) + "\n"
    return
'''

def unDeclaredError(name, detail):
    global i, error
    error += f"\n\t***  Un-Declared Error  ***\n\tID:\t\t{name}\n\tAs:\t\t{detail}\n\tLine #:\t       {tokenList[i].line}\n"
    return

'''
def binTypeMismatchedError(left, right, op):
    global i, error
    error += "\n\t***  Type Mismatched Error  ***\n\t"+"Cant Apply:\t" + op + " on " + \
        left + " and " + right + \
        "\n\tLine #:\t       " + str(tokenList[i].line) + "\n"
    return
'''

def binTypeMismatchedError(left, right, op):
    global i, error
    error += f"\n\t***  Type Mismatched Error  ***\n\tCant Apply:\t{op} on {left} and {right}\n\tLine #:\t       {tokenList[i].line}\n"
    return

'''
def uniTypeMismatchedError(operand, op):
    global i, error
    error += "\n\t***  Type Mismatched Error  ***\n\t"+"Cant Apply:\t" + op, " on " + \
        operand + "\n\tLine #:\t       " + str(tokenList[i].line) + "\n"
    return
'''
def uniTypeMismatchedError(operand, op):
    global i, error
    error += f"\n\t***  Type Mismatched Error  ***\n\tCant Apply:\t{op} on {operand}\n\tLine #:\t       {tokenList[i].line}\n"
    return

def randomError(note):
    global i, error
    error += f"\n\t***  Assertion Error  ***\n\t{note}\n\tLine #:\t       {tokenList[i].line}\n"
    return



try: 
    def start():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack
        #print("^^^^^^^^^^^^^^^")
        if start_body():
            
                       
            if tokenList[i].type == "MAIN":
                
                i += 1  # Consume "main"
                if tokenList[i].type == "(":
                    i += 1  # Consume "("
                    if tokenList[i].type == ")":
                        i += 1  # Consume ")"
                        if tokenList[i].type == "{":
                            i += 1  # Consume "{"
                            if main_body():
                                if tokenList[i].type == "}":
                                    return True
        elif tokenList[i].type == "$":
            return True
        return syntaxError()
        
    '''
    def start_body():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack
        if(tokenList[i].type == "DT" or tokenList[i].type == "CONST" or tokenList[i].type == "DEF" or tokenList[i].type == "VIRTUAL" or tokenList[i].type == "STRUCT" or tokenList[i].type == "CLASS" or tokenList[i].type == "ST" or tokenList[i].type == "OBJ" or tokenList[i].type == "MAIN"):
            print("&&&&&&&&&&&&&&&")
            if dec():
                return start_body()
            elif func_st():
                return start_body()
            elif struct_dec():
                return start_body()
            elif class_dec():
                return start_body()
            elif struct_obj():
                return start_body()
            elif obj_decl():
                return start_body()
            elif OE():
                if tokenList[i].type == ";":
                    i += 1  # Consume ";"
                return start_body()
            elif tokenList[i].type == "MAIN":
                i += 1
                return True 
        return syntaxError()  # Return True for epsilon    
    '''
    
    
    def start_body():
        global i, tokenList
        if dec() or func_st() or struct_dec() or class_dec() or struct_obj() or obj_decl():
            return start_body()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return start_body()
        elif tokenList[i].type == "MAIN":
            return True 
        return syntaxError()  # Return True for epsilon 
       
    
    def main_body():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or return_() or break_() or continue_():
            return main_body()
        elif OE():
            if tokenList[i].type == ";":
                #i += 1  # Consume ";"
                return main_body()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon 
    '''
    
    def main_body():
        global i, tokenList
        if dec():
            return main_body()
        elif if_else():
            return main_body()
        elif try_catch():
            return main_body()
        elif for_st():
            return main_body()
        elif print_():
            return main_body()
        elif struct_dec():
            return main_body()
        elif class_dec():
            return main_body()
        elif struct_obj():
            return main_body()
        elif obj_decl():
            return main_body()
        elif assign_st():
            return main_body()
        elif return_():
            return main_body()
        elif break_():
            return main_body()
        elif continue_():
            return main_body()
        elif OE():
            return main_body()
        '''
    
        
# Declaration and Initialization:
    
    def dec():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType,accessModi
        #print("RRRRRRRRRRRRRR")
        if DT1():
            if (tokenList[i].type == "ID"):
                input_types.clear()
                name = tokenList[i].value 
                #print("ythttgttgsgss")
                #print("currentScope : ",currentScope)
                # print("currentClass : ",currentClass)
                if(currentClass!="" and currentScope!=0):
                    print("pppppppppppooooooooooo")
                    check3=lookupMemberTable(name,"",currentClass)
                else:
                    print("printttttttttttt")
                    check3=lookupFunctionTable(name,currentScope)
                if check3 == False:
                    if(currentClass==""):
                        print("***************")
                        insertFunctionTable(name, ofType, currentScope)
                    else:
                        insertMember(name,"",ofType,accessModi,"","",currentClass) 
                else:
                    reDeclarationError(name, "ID already exists", currentScope)
                
                i += 1
                if init():
                    print("a[2]")
                    if (tokenList[i].type == ";"):
                        print(";")
                        i+=1
                        print("::::::::::::::::::::::::::")
                        return True
                    # print("yyy")
                    # else:
                    #     return syntaxError()
        #print("ghghguhu")
        return syntaxError()
    
    def DT1():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType
        if (tokenList[i].type == "CONSTANT"):
            i += 1
            if DT():
                return True
        elif (DT()):
            return True
    
        return syntaxError()
    
    def dec11():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType,paramList
        if (DT1()):
            print("current token  :  ",tokenList[i-1].value)
            paramList+=tokenList[i-1].value
            print("hello")
            if tokenList[i].type == "ID":
                name = tokenList[i].value
                print("SCOPE", currentScope)
                print("SCOPESTACK", scopeStack)
                check = lookupFunctionTable(name, currentScope)
                
                if check == False:
                    insertFunctionTable(name, ofType, currentScope)
                else:
                    reDeclarationError(name, "ID already exists", currentScope)
                #print("ghgh")
                i += 1
                return init22()
        return syntaxError()
    
    def init22():
        global i, tokenList
        if tokenList[i].type == "AO":
            i += 1
            return OE()
        elif tokenList[i].type == "[":
            i += 1
            return init33()
        elif tokenList[i].type == "," or tokenList[i].type == ")":
            #print("hjkhjk")
            return True
        return syntaxError()
    
    def init33():
        global i, tokenList
        if OE():
            if tokenList[i].type == "]":
                i += 1
                return Arr()
        elif tokenList[i].type == "]":
            i += 1
            return Arr()
        return syntaxError()    
    
    def DT():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, input_types,paramList
        #if (tokenList[i].type == "int" or tokenList[i].type == "float" or tokenList[i].type == "char" or tokenList[i].type == "string" or tokenList[i].type == "bool"):
        if (tokenList[i].type == "DT"):
            ofType = tokenList[i].value
            # paramList+=tokenList[i].value
            # print("paramList           :      ",paramList)
            input_types.append(ofType)
            print("input List", input_types)
            i += 1
            return ofType, input_types
        return syntaxError()
    
    def const():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType1, ofvalue,check,palist
        if (tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR"):
            ofType1 = tokenList[i].type
            ofvalue1 = tokenList[i].value
            ofvalue.append(ofvalue1)
            palist+=tokenList[i].type
        #    complist.append(ofType1)
        #    print("complist", complist)
        #    if len(complist) == 3:
        #        check = binTypeCompatible(complist[0], complist[2], complist[1])
        #        if check == False:
        #            binTypeMismatchedError(complist[0], complist[2], complist[1])
            i += 1
            return ofType1, ofvalue, check
        return syntaxError()  
    
    def SA():
        global i, tokenList
        if (tokenList[i].type == "AO"):
            i += 1
            return True
        return syntaxError()
    
    def or_():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            return True
        return syntaxError()
    
    def init():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, ofType1, op, check
        if (tokenList[i].type == "AO"):
            op2 = tokenList[i].value
            i += 1
            if (init5()):
                #check = binTypeCompatible(ofType, ofType1, op)
                if check == "":
                    check = binTypeCompatible(ofType, ofType1, op2)
                    if check == False:
                        binTypeMismatchedError(ofType, ofType1, op2) 
                else:
                    check = binTypeCompatible(ofType, check, op2)
                    if check == False:
                        binTypeMismatchedError(ofType, check, op2)
                return True
        elif (tokenList[i].type == "["):
            i += 1
            print("[")
            return init1()
        elif (tokenList[i].type == ","):
            i += 1
            if (tokenList[i].type == "ID"):
                name = tokenList[i].value
                check = lookupFunctionTable(name, currentScope)
                if check == False:
                    insertFunctionTable(name, ofType, currentScope)
                else:
                    reDeclarationError(name, "ID already exists", currentScope)
                i += 1
                return init()
        elif (tokenList[i].type == ";"):
            print("QQQQQQQQQQ")
            return True
        return syntaxError()
    
    def init6():
        global i, tokenList
        if (tokenList[i].type == "AO"):
            print("=")
            i += 1
            if (init7()):
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init5():
        global i, tokenList
        if (OE()):
            print(init5())
            return True
        elif(take()):
            return True
        return syntaxError()
    
    def init7():
        global i, tokenList
        if (tokenList[i].type == "{"):
            print("{")
            i += 1
            if (init2()):
                if (tokenList[i].type == "}"):
                    i += 1
                    #if (init2()):
                    return True
        return syntaxError()
    
    def init2():
        global i, tokenList
        if (tokenList[i].type == ","):
            print("{2,")
            i += 1
            if (init8()):
                print("{")
                return True
        elif (OE() and init2()):
            return True
        elif (tokenList[i].type == "{"):
            print("{")
            i += 1
            if (OE() and init2()):
                print("A")
                if (tokenList[i].type == "}"):
                    i += 1
                    if (init2()):
                        return True
        elif (tokenList[i].type == "}"):
            i += 1
            #return True
            return init2()
        elif (tokenList[i].type == "}" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init8():
        global i, tokenList
        if (OE() and init2()):
            return True
        elif (tokenList[i].type == "{"):
            i += 1
            if (OE() and init2()):
                if (tokenList[i].type == "}"):
                    return True
        return syntaxError()
    
    def init1():
        global i, tokenList
        if (OE()):
            print("2")
            if (tokenList[i].type == "]"):
                print("]")
                i += 1
                if (Arr() and init6()):
                    print("Arr and init6")
                    return True
        elif (tokenList[i].type == "]"):
            print("Init1-follow")
            i += 1
            if (Arr() and init16()):
                return True
        return syntaxError()
  

    def init16():
        global i, tokenList
        if SA():
            return init7()
        return syntaxError()
    

    def struct_obj11():
        global i, tokenList, paramList
        if tokenList[i].type == "ST":
            i += 1
            if tokenList[i].type == "ID":
                i += 1
                if tokenList[i].type == "ID":
                    i += 1
                    return listA11()
        return syntaxError()
    
    def listA11():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1
            if OE():
                if tokenList[i].type == ']':
                    i += 1
                    return Arr()
        elif (tokenList[i].type == "," or tokenList[i].type == ")"):
            return True
        return syntaxError()
    

    def param():
        global i, tokenList,paramList
        if dec11():
            #print("look")
            return param1()
        elif struct_obj11():
            return param1()
        elif obj_decl():
            return param1()
        elif tokenList[i].type == ")":
            return True
        return syntaxError()
    
    
    def param2():
        global i, tokenList,paramList
        if (dec11()):
            print("pppp")
            return True
        elif struct_obj11():
            return True
        elif obj_decl():
            return True
        return syntaxError()
    
# assign_st  
    
    def assign_st():                 
        print("EEEEEEEEEEEEEEE")    
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, ofType1, op, op2
        if (tokenList[i].type=="ASSIGN"):
            print("OOOOOOOOOOOO")
            i+=1
            if(D2() and X2() and list_()):
                print("LLLLLLLLL", op2)
                check1 = binTypeCompatible(ofType1, ofType, op)
                if check1 == False:
                    binTypeMismatchedError(ofType1, ofType, op)

                if(tokenList[i].type==";"):
                    print(";")
                    i+=1
                    return True
        return syntaxError()     

    def D2():
        global i, tokenList
        if(tokenList[i].type=="Inc_Dec"):
            i+=1
            if(inc_dec_op()):
                return p()
        elif(tokenList[i].type=="THIS"):
            i += 1
            return True
        elif (tokenList[i].type=="ID" or tokenList[i].type=="("):
            print("NULL(D2)")
            return True
        return syntaxError()

    def X2():
        global i, tokenList,currentClass,currentObj,currentScope
        if(tokenList[i].type=="ID"):
            name = tokenList[i].value
            check=True
            check = lookupFunctionTable(name, currentScope)
            # print("opopopopo")
            # print("currentClass : ",currentClass)
            # print("currentScope : ",currentScope)
            # if(currentClass!="" and currentScope!=0):
            #     print("pppppppppppooooooooooo")
            #     print("ooooooooo000000000000000000000000000000ooooooooooooooooooooooooooo")
            #     check=lookupMemberTable(name1, "",currentClass)
            #     print("checckkkkkkkkkkkk:",check)
            # else:
            #     print("printttttttttttt")
            #     check=lookupFunctionTable(name1,currentScope)
                            
            if check == False:
                unDeclaredError(name, "ID does not exist")
            print("a")
            i+=1
            return dot22() 
        elif(tokenList[i].type=="("):
            i+=1
            if(tokenList[i].type=="ID"):
                i+=1
                if(dot22()):
                    if(tokenList[i].type==")"):
                        i+=1
                        return True
        elif tokenList[i].type == "AO":
            return True
        return syntaxError()
   
    def dot22():
        global i, tokenList
        if tokenList[i].type == ".":
            i += 1
            if tokenList[i].type == "ID":
                i += 1
                return dot22()
        elif tokenList[i].type == "(":
            i += 1
            if para():
                if tokenList[i].type == ")":
                    i += 1
                    if tokenList[i].type == ".":
                        i += 1
                        if tokenList[i].type == "ID":
                            i += 1
                            return dot22()
        elif tokenList[i].type == "[":
            if OE():
                if tokenList[i].type == "]":
                    i += 1
                    return dot22()
        elif tokenList[i].type == ")" or tokenList[i].type == "AO":
            return True
        return syntaxError()                    
            
    
    def list_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, op
        if (tokenList[i].type == "AO"):    # AO or AO_D(+=,-=,...)
            op = tokenList[i].value
            i += 1
            if(SSA()):
                
                return op, True
        elif tokenList[i].type == ";":
            return True
        return syntaxError()
    
    def p1():
        global i, tokenList
        if (tokenList[i].type == "THIS"):
            i += 1
            if (tokenList[i].type == "."):
                return True
        return syntaxError()
    
    def take():
        global i, tokenList
        if(tokenList[i].type=="TAKE"):
            return IndexA
        return syntaxError() 
    
    def SSA():              # issue 
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType
        if(OE()):
            return True
        elif(tokenList[i].type=="TAKE"):
            return take()
        return syntaxError()
    
    def IndexA():
        global i, tokenList
        if(tokenList[i].type=="(" and const()):
            if (tokenList[i].type==")"):
                i+=1
                if(tokenList[i].type==";"):
                    i+=1
                    return True
        return syntaxError()
    
    
    
  
    

    
# Inc_Dec_obj_call:

    def Inc_Dec_obj_call():
        global i, tokenList
        if (tokenList[i].type == "Inc_Dec"):
            print("INC_DEC")
            typeMod = tokenList[i].type
            i += 1
            if (B1()):
                print("B1")
                return True
        
        return syntaxError()
    
    def B1():
        global i, tokenList
        if (tokenList[i].type == "ID"):
            name = tokenList[i].value
            i += 1
            if (dot() and inc_dec_op()):
                check = lookupFunctionTable(name, currentScope)
                if check == False:
                    unDeclaredError(name, "ID is not declared")
                print("Inc_Dec i++")
                return True
        elif (tokenList[i].type == "Inc/Dec"):
            typeMod = tokenList[i].type
            i += 1
            return X11()
        elif(tokenList[i].type == "(" or tokenList[i].type == "THIS"):
            typeMod = tokenList[i].type           # Check this
            i += 1
            if (B2() and inc_dec_op()):
                return True
        return syntaxError()
        
    
    def B2():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                name = tokenList[i].value
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "THIS"):
            typeMod = tokenList[i].type
            i += 1
            if (tokenList[i].type == "ID"):
                name = tokenList[i].value
            #    check = lookupFunctionTable(name, currentScope)
            #    if check == False:
            #        unDeclaredError(name, "ID is not declared")
                i += 1
                return dot()
        return syntaxError()
    
    def X11():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                name = tokenList[i].value
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "ID"):
            name = tokenList[i].value
            check = lookupFunctionTable(name, currentScope)
            
            if check == False:
                unDeclaredError(name, "ID is not declared")
            i += 1                
            return dot()
        return syntaxError()
    
    def para():
        global i, tokenList, palist
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (OE() and para1()):
            # palist+=tokenList[i-2].type
            return True
        
        elif (tokenList[i].type == ")"):
            palist=""
            return True
        return syntaxError()
    
    def para1():
        global i, tokenList,palist
        if (tokenList[i].type == ","):
            palist+=","
            i += 1
            if (OE() and para1()):
                # palist+=","+tokenList[i-2].type
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    

    def dot():                                        
        global i, tokenList,currentScope,palist,name,ofName,currentClass,ofType,currentObj
        check=True
        if (tokenList[i].type == "."):
            print(".")
            i += 1
            if (tokenList[i].type == "ID"):
                name=tokenList[i].value
                check=True
                print("name : "+name+" , ofName : "+ofName+" 9999999999 ")
                print("currentClass : ",currentObj," currentScope : ",currentScope)
                if(currentObj!="" and currentScope==0 and tokenList[i+1].value!="("):
                    print("yuyeru::::::::::::")
                    check=lookupMemberTable(name, "",ofName)
                    print("ioioi))))))))))))")
                elif (tokenList[i+1].value!="("):
                    print("ererer@@@@@@@@@@@@")
                    check=lookupFunctionTable(name,currentScope)
                print("check ++++++++++++       ",check)
                if(check==False):
                    unDeclaredError(name,"doesn't exist .... 780")
                i += 1
                return dot()
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return dot()
        elif (tokenList[i].type == "("):
            print("(")
            i += 1
            if (para()):
                check=True
                palist=palist.lower()
                print("name : "+name+" , paList : " + palist + " ofName : "+ofName  +"+ofName+"+" 9999999999 "+ "CurrentObject : "+currentObj)
                if(currentObj!=""):
                    print("qwqwqw90909009")
                    check=lookupMemberTable(name, palist,currentObj)
                    print("palist"+palist)
                    print("name"+name)
                    print("ofName"+currentObj)
                    print("check",check,"90989898")
                else:
                    print("dfdfdf88888888888888")
                    print("tttttttttttttttttttt")
                    check=lookupFunctionWithType(name,palist,currentScope)
                    print("check"+check+"34555555555555")
                    print(";;;;;;;;;;;;;;;;;;;;;;;")
                if(check==False):
                    unDeclaredError(name,"doesn't exist..345")
                if (tokenList[i].type == ")"):
                    print(")")
                    i += 1
                    palist=""
                    return dot()       
        elif (tokenList[i].type == ")"  or tokenList[i].type == "Inc/Dec" or tokenList[i].type == ";" or tokenList[i].type == "]" or tokenList[i].type == "{"  or tokenList[i].type == "}" or  tokenList[i].type == "," or tokenList[i].type == "AND" or tokenList[i].type == "OR" or tokenList[i].type == "PM" or tokenList[i].type == "MDM" or tokenList[i].type == "R_OP"):
            print("NULL(dot)")
            return True
        return syntaxError()
 
   
  
# object_call:        
    
    def obj_call():
        global i, tokenList
        #if (tokenList[i].type == "ID" or tokenList[i].type == "(" or tokenList[i].type == "this"):
        if B_():
            return True
        return syntaxError()
    
    def B_():
        global i, tokenList,currentScope,ofName,ofType,currentObj
        check=True
        if (tokenList[i].type == "ID"):                    # 3
            name=tokenList[i].value
            check=lookupFunctionTable(name,currentScope)
            if check == False:
                unDeclaredError(name, "ID does not exist..455")
            
            i += 1
            return dot()
        elif (tokenList[i].type == "THIS"):
            typeMod = tokenList[i].type
            i += 1
            if (tokenList[i].type == "ID"):
                name=tokenList[i].value
                if(currentClass!="" and currentScope!=0 and tokenList[i+1]!="("):
                    check=lookupMemberTable(name, "",ofName)
                elif (tokenList[i+1]!="("):
                    check=lookupFunctionTable(name,currentScope)
                if check == False:
                    unDeclaredError(name, "ID does not exist..909")
            
                i += 1
                return dot()
        return syntaxError()
    
# struct_obj:

    def struct_obj():
        global i, tokenList,paramList,ofName,ofType, access_Modi
        if (tokenList[i].type == "ST"):
            i += 1
            if (tokenList[i].type == "ID"):
                ofType=tokenList[i].value
                check = lookupMainTable(ofType)
                if check == False:
                    unDeclaredError(ofType,"ID does not exist..897")
                i += 1
                if (tokenList[i].type == "ID"):
                    struct_name_obj=tokenList[i].value
                    check = lookupFunctionTable(struct_name_obj,currentScope)
                    if check == False:
                        insertFunctionTable(struct_name_obj,ofType,currentScope)
                    else:
                        reDeclarationError(ofType, "ID already exists")
                    i += 1
                    if (list_A() and initA()):
                        if (tokenList[i].type == ";"):
                            return True
                    
        return syntaxError()
            
    def list_A():
        global i, tokenList,ofType
        if (tokenList[i].type == ","):
            i += 1
            if (tokenList[i].type == "ID"):
                struct_name_obj=tokenList[i].value
                check = lookupFunctionTable(struct_name_obj,currentScope)
                if check == False:
                    insertFunctionTable(struct_name_obj,ofType,currentScope)
                else:
                    reDeclarationError(ofType, "ID already exists")
                i += 1
                return list_A
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return list_A
        elif (tokenList[i].type == "AO" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def initA():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            if (tokenList[i].type == "{"):
                i += 1
                if (OE() and list_B()):
                    if (tokenList[i].type == "}"):
                        return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def list_B():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (OE() and list_B()):
                return True
        elif (tokenList[i].type == "}"):
            return True
        return syntaxError()
 
 
    
# if-else: 
    
    def if_else():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, op, ofvalue
        if tokenList[i].type == "IF":
            i += 1
            if if2():
        
                return True
        return syntaxError()

    def if2():
        global i, j, k, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, op, ofvalue

        if tokenList[i].type == "(":
            i += 1
            if cond():
                print("TTTTTTTTT", ofvalue)
                #for j in range(len(ofvalue)-1):
                #    if ofvalue[0] < ofvalue[j + 1]:
                #        randomError("Value is out of range")
                if tokenList[i].type == ")":
                    
                    i += 1
                    if (if_body() and elif_()):
                        return True
        return syntaxError()

    def elif_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, op, ofvalue
        if tokenList[i].type == "ELIF":
            i += 1
            if if2():
                
                return True
        elif tokenList[i].type == "ELSE":
            i += 1
            if tokenList[i].type == ":":
                i += 1
                if if_body():
                    return True
        elif tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CONST" or tokenList[i].type == "STR" or tokenList[i].type == "BOOL" or tokenList[i].type == "CHAR" or tokenList[i].type == "DEF" or tokenList[i].type == "VIRTUAL" or tokenList[i].type == "THROW" or tokenList[i].type == "ACCESS MODIFIER" or tokenList[i].type == "IF" or tokenList[i].type == "BREAK" or tokenList[i].type == "CONTINUE" or tokenList[i].type == "THIS" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "DT" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "ID" or tokenList[i].type == "RETURN" or tokenList[i].type == "CHECK" or tokenList[i].type == "FOR" or tokenList[i].type == "PRINT" or tokenList[i].type == "ST" or tokenList[i].type == "OBJ" or tokenList[i].type == "ASSIGN" or tokenList[i].type == "STRUCT" or tokenList[i].type == "CLASS" or tokenList[i].type == "}" or tokenList[i].type == "MAIN" or tokenList[i].type == "~" or tokenList[i].type == "ELIF" or tokenList[i].type == "ELSE" or tokenList[i].type == "CONSTRUCT":
            print("!!!!!!!!!!!!!")
            return True
        return syntaxError()

    def cond():
        global i, tokenList
        if OE():
            print("OE-")
            return True
        return syntaxError()

    def if_body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1
            if if_SST():
               if tokenList[i].type == "}":
                   i += 1 
                   return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()
    
    def if_SST():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or OE() or return_() or break_() or continue_() or throw():
            return if_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return if_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon
    
# struct_dec:

    def struct_dec():
        global i, tokenList,access_Modi
        if (tokenList[i].type == "STRUCT"):
            ofType=tokenList[i].value
            i += 1
            if (tokenList[i].type == "ID"):
                struct_name=tokenList[i].value
                check = lookupMainTable(struct_name)
                if check == False:
                    insertMainTable(struct_name, ofType, access_Modi, "", "")
                else:
                    reDeclarationError(struct_name, "ID already exists")
                i += 1
                return struct_body()
        return syntaxError()
    
    def struct_body():
        global i, tokenList
        if (tokenList[i].type == "{"):
            currentScope=createScope()
            i += 1
            if (struct_sst()):
                if (tokenList[i].type == "}"):
                    currentScope=destroyScope()
                    i += 1
                    return True
        elif (tokenList[i].type == ";"):
            i += 1
            return True
        return syntaxError()
    
    def struct_sst():
    # Check if there are any statements in the struct_SST
        if (dec() or assign_st() or struct_obj() or obj_decl() or func_st() or print_()):   # direct function given without non-terminal first-set
        # After processing a statement, continue with struct_SST
            return struct_sst()
        elif (tokenList[i].type == "}"):
            return True
        # If no statements match, it's an epsilon (empty) production
        return syntaxError()
    
# break

    def break_():
        global i, tokenList
        if (tokenList[i].type == "BREAK"):
            i += 1  
            if (tokenList[i].type == ";"):
                i += 1 
                return True
        return syntaxError()
    
# continue

    def continue_():
        global i, tokenList
        if (tokenList[i].type == "CONTINUE"):
            i += 1  
            if (tokenList[i].type == ";"):
                i += 1  
                return True
        return syntaxError()
    
# return
 
    def return_():
        global i, tokenList
        if (tokenList[i].type == "RETURN"):
            i += 1  
            if (index1()): 
                if (tokenList[i].type == ";"):
                    i += 1  
                    return True  
        return syntaxError()
        
    def index1():
        global i, tokenList
        if (OE()):
            return True
        elif (tokenList[i].type == ";"):
            return True  
        return syntaxError()

# throw

    def throw():
        global i, tokenList
        if (tokenList[i].type == "THROW"):
            i += 1 
            if index():
                return True
        return syntaxError()
    
# print_

    def print_():
        global i, tokenList
        if (tokenList[i].type == "PRINT"):
            i += 1  
            if index():
                if (tokenList[i].type == ";"):
                    i += 1  
                    return True
        return syntaxError()

    def index():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1 
            if (OE()):
                if (tokenList[i].type == ")"):
                    i += 1 
                    return True  
        return syntaxError()
    
# inc_dec

    def inc_dec_op():
        global i, tokenList
        if tokenList[i].type == "Inc/Dec":
            i += 1  # Consume the "++" or "--"
            return True
        return syntaxError()

    def Arr():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1  # Consume the opening square bracket "["
            print("ARR1")
            if OE():
                if tokenList[i].type == "]":
                    i += 1  # Consume the closing square bracket "]"
                    return Arr()  # Recursively check for more arrays
        elif tokenList[i].type == "AO" or tokenList[i].type == ";" or tokenList[i].type == "Inc/Dec" or tokenList[i].type == "," or tokenList[i].type == ")":
            print("ARR")
            return True 
        return syntaxError()  # Return True for epsilon

    def IDC():
        global i, tokenList
        if p():
            if tokenList[i].type == "ID":
                i += 1  # Consume the identifier (ID)
                if Arr():
                    if inc_dec_op():
                        return True
        elif inc_dec_op():
            if tokenList[i].type == "ID":
                i += 1  # Consume the identifier (ID)
                if Arr():
                    return True
        return syntaxError()

# p()
    
    def p():
        global i, tokenList
        if(tokenList[i]=="THIS"):
            return True
        elif(tokenList[i].type=="ID" or tokenList[i].type=="("):
            return True
        return syntaxError()
    
# obj_declare:

    def parameter1():
        global i, tokenList
        if tokenList[i].type == ",":
            i += 1  # Consume the comma ","
            if OE() and parameter1():
                name=tokenList[i].value
                ofType=tokenList[i].type
                obj_check=lookupFunctionTable(name,currentScope)
                if( obj_check==False):
                    insertFunctionTable(name, ofType, currentScope)
                else:
                    reDeclarationError(name,"Object already exist")  
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()  # Return True for epsilon

    def parameter():
        global i, tokenList,name,ofType,currentScope
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if OE() and parameter1():
            name=tokenList[i].value
            ofType=tokenList[i].type
            obj_check=lookupFunctionTable(name,currentScope)
            if( obj_check==False):
                insertFunctionTable(name, ofType, currentScope)
            else:
                reDeclarationError(name,"Object already exist")       

            return True
        return syntaxError()

    def N5():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            return OE()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N4():
        global i, tokenList
        if tokenList[i].type == ",":
            i += 1  
            if OE() and N4():
                return True
        elif tokenList[i].type == "{":
            i += 1  # Consume "{"
            if OE() and N4():
                if tokenList[i].type == "}":
                    i += 1  # Consume "}"
                    return N4()  # Recursively check for more occurrences
        elif (tokenList[i].type == "}" or tokenList[i].type == ";"):
            return True        
        return syntaxError()  # Return True for epsilon

    def N3():
        global i, tokenList
        if (tokenList[i].type == "{"):
            i += 1
            if OE() and N4():
                if (tokenList[i].type == "}"):
                    i += 1
                    return N4()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N2():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            return N3()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N1():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1  # Consume "["
            if OE():
                if (tokenList[i].type == "]"):
                    i += 1 
                    return Arr() and N2()
        elif tokenList[i].type == "(":
            i += 1  # Consume "("    
            if parameter():
                if tokenList[i].type == ")":
                    i += 1  # Consume ")"
                    return N5()  # Check for SA and OE
        elif tokenList[i].type == "=": 
            i += 1
            if OE():
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def obj_decl():
        global i, tokenList,currentClass,ofType,currentObj
        if tokenList[i].type == "OBJ":
            i += 1  # Consume "obj"
            if tokenList[i].type == "ID":
                currentObj=tokenList[i].value
                ofType=tokenList[i].value
                check=lookupMainTable(ofType)
                if(check==False):
                    unDeclaredError(ofType,"class doesn't exist..5673")
                
                i += 1  # Consume the first ID
                if tokenList[i].type == "ID":
                    obj_name=tokenList[i].value
                    scope=currentScope
                    obj_check=lookupFunctionTable(obj_name,scope)
                    
                    
                    if( obj_check==False):
                        insertFunctionTable(obj_name, ofType, scope)
                    else:
                        reDeclarationError(obj_name,"Object already exist")           
                    i += 1  # Consume the second ID
                    if N1():
                        if tokenList[i].type == ";":
                            i += 1  # Consume the semicolon
                            return True
        return syntaxError()

# destructor

    def destructor():
        global i, tokenList,  ofType, ofName
        if (tokenList[i].type == "~"):
            i += 1
            if (tokenList[i].type == "ID"):
                ofName = tokenList[i].value
                
                i += 1
                return indexD()
        return syntaxError()

    
    def indexD():
        global i, tokenList, ofName, pm, accessModi, typeMod
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == ")"):
                check = lookupMemberTable(ofName, pm, ofName)
                if check == False:
                    insertMember(ofName, pm, ofType, accessModi, typeMod, "-", ofName)
                i += 1
                if (tokenList[i].type == "{"):
                    i += 1
                    if (tokenList[i].type == "}"):
                        i += 1
                        return True
        return syntaxError()
        
    def destructor_SST():    
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or struct_obj() or obj_decl() or assign_st() or OE() or class_dec():
            return constructor_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return constructor_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()    
        
# class

    def class_dec():
        global i, tokenList, parentList,currentClass,ofType,ofName
        if sealed():
            
            
            if tokenList[i].type == "CLASS":
                ofType = tokenList[i].type
                i += 1
                if tokenList[i].type == "ID":
                    ofName = tokenList[i].value
                    currentClass=tokenList[i].value
                    check = lookupMainTable(ofName)
                    if check != False:
                        
                        reDeclarationError(ofName, "Class already exists", currentScope)
                    i += 1
                    if class_dec1():
                        if tokenList[i].type == ";":
                            i += 1
                            return True
        return syntaxError()

    def class_dec1():
        global i,tokenList, ofName, ofType, accessModi, typeMod, parentList
        if inherit():
            print("87878787878787878787")
            print("ofName:",ofName)
            print("ofType :",ofType)
            print("accessModi :",accessModi)
            print("typeMod : ",typeMod)
            print("parentList",parentList)                           
            insertMainTable(ofName, ofType, accessModi, typeMod, parentList)
            parentList = ""
            print("0909090909099999999999999999")

            if class_body():
                return True
        return syntaxError()

    def inherit():
        global i, tokenList, ofName, ofType, parentList, typeMod
        if tokenList[i].type == ":":
            i += 1
            if access_mod():
                parentType=access_mod()
                
                if (parentType=="private" or parentType=="protected"):
                    randomError(f"On {parentType} access modifier, class  can't be inherited")
                if tokenList[i].type == "ID":
                    parent_name = tokenList[i].value
                    check = lookupMainTable(parent_name)
                    
                    if check==False:
                        
                        unDeclaredError(parent_name, "Class does not exist")
                    
                    else:
                        if check.typeMod == "sealed":
                            randomError("Sealed class can't be inherited.")
                        else:
                            parentList+=parent_name
                        
                    
                    i += 1
                    if multiple_inherit():
                        return True
        elif tokenList[i].type == "{" or tokenList[i].type == ";":
            return True
        return syntaxError()

    def multiple_inherit():
        global i, tokenList, parentList,typeMod
        if tokenList[i].type == ",":
              
            i += 1
            if access_mod():
                parent1_Type=access_mod()
                print("parent1",parent1_Type)
                if (parent1_Type=="private" or parent1_Type=="protected"):
                    randomError(f"On {parent1_Type} access modifier, class  can't be inherited")
                if tokenList[i].type == "ID":
                    parent1_name = tokenList[i].value
                    multi_check = lookupMainTable(parent1_name)
                    if multi_check==False:
                        unDeclaredError(parent1_name,"Class does no exist.")
                    
                    else:
                        
                        if multi_check.typeMod == "sealed":
                            randomError("Sealed class can't be inherited.")
                        else:
                            parentList += "," + tokenList[i].value
                    i+=1
                    return multiple_inherit()
        elif tokenList[i].type == "{" or tokenList[i].type == ";":
            return True
        return syntaxError()

    def class_body():
        global i, tokenList, currentClass, currentScope
        if(tokenList[i].type=="{"):
            currentScope=createScope()
            i+=1
            if(class_SST()):
                
                if(tokenList[i].type =="}"):
                    currentClass=""
                    currentScope=destroyScope()
                    i+=1
                    return True
        elif(tokenList[i].type==";"):
            return True
        return syntaxError()
    
    def sealed():
        global i, tokenList, typeMod
        if (tokenList[i].type == "SEALED"):
            typeMod=tokenList[i].value
           
            i+=1
            return typeMod
        elif(tokenList[i].type=="CLASS"):
            typeMod="-"
            print("elif", typeMod)
            return typeMod
        return syntaxError()
    
    def access_mod():
        global i, tokenList, accessModi
        if(tokenList[i].type=="ACCESS MODIFIER"):
            accessModi=tokenList[i].value
            i+=1
            return accessModi
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        elif(tokenList[i].type=="ID" or tokenList[i].type==":"):
            return accessModi       
        return syntaxError()
    
    def class_SST():
        global i, tokenList
        print("123")
        if access_mod():
            print("A")
            if (tokenList[i].type == ":"):
                i+=1
                return class_SST()
        elif dec():
            return class_SST()
            print("B")
        elif func_st() and class_SST():
            print("C")
            return True
        elif constructor() and class_SST():
            print("D")
            return True
        elif destructor() and class_SST():
            print("E")
            return True
        elif if_else() and class_SST():
            print("F")
            return True
        elif try_catch() and class_SST():
            print("G")
            return True
        elif for_st() and class_SST():
            print("H")
            return True
        elif print_() and class_SST():
            print("I")
            return True
        elif class_dec() and class_SST():
            print("J")
            return True
        elif struct_dec() and class_SST():
            print("K")
            return True
        elif OE():
            print("L")
            if (tokenList[i].type == ";"):
                i += 1
                return class_SST()
        elif struct_obj() and class_SST():
            print("M")
            return True
        elif obj_decl() and class_SST():
            print("N")
            return True
        elif assign_st() and class_SST():
            print("O")
            return True
        elif tokenList[i].type == "}":
            print("P")
            return True
        
        return syntaxError()

# constructor


    def interface():
        global i, tokenList
        if(tokenList[i].type=="INTERFACE"):
            ofType=tokenList[i].type
            i+=1
            if(tokenList[i].type=="ID"):
                name=tokenList[i].value
                i+=1
                if(semi()):
                    if(tokenList[i].type=="{"):
                        i+=1
                        if(init_body()):
                            if(tokenList[i].type=="}"):
                                return True
        return syntaxError()
    
    def semi():
        global i, tokenList
        if(tokenList[i].type==":"):
            i+=1
            if(tokenList[i].type=="ID"):
                return True
        elif(tokenList[i].type==":" or "{"):
            return True
        
        return syntaxError()
        
    def init_body():
        global i, tokenList
        if(var()):
            return init_body()
        elif(int_func):
            return init_body()
        #elif():

        return syntaxError()
    def var():
        global i, tokenList
        if(DT1):
            if(tokenList[i].type=="ID"):
                i+=1
                if(tokenList[i].type==";"):
                    i+=1
                    return True
        return syntaxError
 
    def int_func():
        global i, tokenList
        if(DT2()):
            if(tokenList[i].type=="ID"):
                i+=1
                if(tokenList[i].type=="("):
                    i+=1
                    if(param()):
                        if(tokenList[i].type==";"):
                            i+=1
                            return True
        return syntaxError()



    

    def constructor_Body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1  # Consume "{"
            if constructor_SST():
                if tokenList[i].type == "}":
                    i += 1  # Consume "}"
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()

    def constructor_SST():
        global i, tokenList, currentScope
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or OE():
            return constructor_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
                return constructor_SST()
        elif tokenList[i].type == "}":
            currentScope=destroyScope()
            return True
        return syntaxError()

    def indexC():
        global i, tokenList,const_name,pm,ofType,ofName
        if tokenList[i].type == "(":
            currentScope = createScope()
            i += 1  # Consume "("
            if param():
                if tokenList[i].type == ")":
                    check_obj=lookupMemberTable(ofName,pm,ofName)
                    if check_obj == False:
                        insertMember(ofName, pm, ofType, accessModi, typeMod, "-", ofName)
                    print(input_types)
                    pm=plist(*input_types)        
                    i += 1  # Consume ")"
                    return constructor_Body()            
        return syntaxError()

    def constructor():
        global i, tokenList, currentClass, ofName, typeMod, pm
        pm=plist()
        if tokenList[i].type == "CONSTRUCT":
            
            i += 1  # Consume "construct"
            if tokenList[i].type == "ID":
                ofName=tokenList[i].value
                print("1695", ofName)
                check=lookupMainTable(ofName)
                print("1696", check)
                if check == False:
                    print("1699", ofName)
                    unDeclaredError(ofName,"class doesn't exist")
                i += 1  # Consume "ID"
                if indexC():
                    if (tokenList[i].type == ";"):
                        i += 1
                        return True
        return syntaxError()
    
    
# function_st

 
    def func_st():                # def int A(){}
        
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, name1, ofType1
        if(key()):
        
            if(tokenList[i].type =="DEF"):
          
                i+=1
                if(DT2() and tokenList[i].type=="ID"):
                    name1 = tokenList[i].value
                    '''check = lookupFunctionTable(name, currentScope)
                    print("POPOPOP", ofType)
                    ofType2 = f"{ofType} , {ofType} -> {ofType1}"
                    if check == False:
                        insertFunctionTable(name, ofType2, currentScope)
                    else:
                        reDeclarationError(name, "function already exists")'''
                    i+=1
                    if(func_I()):
                        return True
        return syntaxError()    

    def func_I():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType, name1, ofType1, ofType2, ofType3, input_types,accessModi,over_ride,paramList,ofName
        if tokenList[i].type == "(":
            name1=tokenList[i-1].value
            currentScope1 = currentScope  # before this (){}, it is in previous scope (for, def etc)
            currentScope = createScope()
            i += 1
            if param() and tokenList[i].type == ")":
                i += 1
                if override():
                    print(input_types)
                    print(ofType1)
                    result1 = createTypeExpression(ofType1, *input_types)
                    input_types.clear()     # make list clear after a function is completed
                    print(input_types)

                    print("opopopopo")
                    print("currentClass : ",currentClass)
                    print("currentScope : ",currentScope)
                    if(currentClass!="" and currentScope!=0):
                        print("pppppppppppooooooooooo")
                        check3=lookupMemberTable(name1, paramList,currentClass)
                    else:
                        print("printttttttttttt")
                        check3=lookupFunctionWithType(name1,result1,currentScope1)
                    if check3 == False:
                        if(currentClass==""):
                            print("***************")
                            insertFunctionTableWithType(name1, result1, currentScope1)
                        else:
                            print("++++++++++++++")
                            print("name1: ", name1)
                            print("result1 : ",paramList)
                            print("ofType : ",ofType)
                            print("accessModi",accessModi)
                            print("currentScope:",currentScope)
                            insertMember(name1,paramList,ofType,accessModi,"","",ofName)
                            print("00000000000000000000000000000000")
                            

                    elif (over_ride==""):
                        print("Redeclaration Error")
                        reDeclarationError(name1, "function already exists", currentScope1)
                    paramList=""
                    if funct_body():
                        return True
        return syntaxError()

    def override():
        global i, tokenList,over_ride
        if tokenList[i].type=="OVERRIDE":
            over_ride="override"
            i+=1
            return True
        elif funct_body():
            return True     
        return syntaxError()

    def param1():
        global i, tokenList,paramList
        if tokenList[i].type == ",":
            print("------------------")
            paramList+=","
            i += 1
            if param2() and param1():
                return True
        elif(tokenList[i].type ==")"):
            return True
        return syntaxError()
     
                   
    
    
    
    def key():
        print("@@@@@@@@@@@")
        global i, tokenList
        if tokenList[i].type == "VIRTUAL":
            i += 1
            return True
        elif tokenList[i].type == "DEF":
            print("|||||||||||||||")
            return True
        return syntaxError()
    
    def funct_body():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType
        if tokenList[i].type == "{":
            i += 1
            if funct_SST() and tokenList[i].type == "}":
                currentScope = destroyScope()
                i += 1
                return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()


    def funct_SST():
        global i, tokenList
        if dec() or func_st() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or break_() or continue_() or OE() or return_():
            return funct_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return funct_SST()
        elif tokenList[i].type == "}":
            return True 
        return syntaxError()  # Return True for epsilon

    def DT2():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, ofType1
        #if tokenList[i].type == "void" or tokenList[i].type == "int" or tokenList[i].type == "float" or tokenList[i].type == "char" or tokenList[i].type == "string" or tokenList[i].type == "bool":
        if tokenList[i].type == "DT":
            ofType1 = tokenList[i].value
            i += 1
            #return True
            return ofType1
        return syntaxError()
    
# try_catch

    def try_catch():
        global i, tokenList
        if tokenList[i].type == "CHECK":
            i += 1
            if tokenList[i].type == "{":
                i += 1
                if try_SST():
                    if tokenList[i].type == "}":
                        i += 1
                        if catch():
                            return catch1() 
        return syntaxError()

    def catch1():
        global i, tokenList
        if catch() and catch1():
            return True
        elif tokenList[i].type == "DT" or tokenList[i].type == "DEF" or tokenList[i].type == "VIRTUAL" or tokenList[i].type == "THROW" or tokenList[i].type == "ACCESS MODIFIER" or tokenList[i].type == "IF" or tokenList[i].type == "BREAK" or tokenList[i].type == "CONTINUE" or tokenList[i].type == "CONST" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "THIS" or tokenList[i].type == "(" or tokenList[i].type == "ID" or tokenList[i].type == "NOT" or tokenList[i].type == "RETURN" or tokenList[i].type == "CHECK" or tokenList[i].type == "FOR" or tokenList[i].type == "PRINT" or tokenList[i].type == "ST" or tokenList[i].type == "OBJ" or tokenList[i].type == "ASSIGN" or tokenList[i].type == "STRUCT" or tokenList[i].type == "CLASS" or tokenList[i].type == "}" or tokenList[i].type == "CONSTRUCT" or tokenList[i].type == "~" or tokenList[i].type == "MAIN" or tokenList[i].type == "ELIF" or tokenList[i].type == "ELSE":
            print("[[[[[[[[[[[[]]]]]]]]]]]]")
            return True
   
    def try_SST():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or throw() or OE() or return_():
            return try_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return try_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon

    def catch():
        global i, tokenList
        if tokenList[i].type == "CATCH":
            i += 1
            if tokenList[i].type == "(":
                i += 1
                if catch_para():
                    if tokenList[i].type == ")":
                        i += 1
                    if tokenList[i].type == "{":
                        i += 1
                        if catch_SST():
                            if tokenList[i].type == "}":
                                i += 1
                                return True
        return syntaxError()

    def catch_para():
        global i, tokenList
        if obj_decl():
            return True
        elif tokenList[i].type == "...":
            i += 1
            return True
        return syntaxError()

    def catch_SST():
        global i, tokenList
        if dec() or if_else() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or throw() or OE() or return_():
            return catch_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return catch_SST()
        elif tokenList[i].type == "}":
            return True 
        return syntaxError()  # Return True for epsilon

# for-st
    def for_st():
        global i, tokenList, ofvalue, currentClass, currentFunction, currentScope, scopeStack
        if(tokenList[i].type=="FOR"):
            i+=1
            if(tokenList[i].type=="("):
                currentScope = createScope()
                print("WERTYUI", currentScope)
                i+=1
                if(init11()):
                    print("1st cond")
                    #if(tokenList[i].type==";"):
                    print(";")
                    #i+=1
                    if(cond11()):         # issue (for-loop)
                        print(ofvalue)
                        if (ofvalue[0] > ofvalue[1]):
                            randomError("Value is out of range")
                        if(tokenList[i].type==";"):
                            print("WWWWWWWW")
                            i+=1
                            if(inc_dec11()):
                                print("Inc_Dec i++")
                                if(tokenList[i].type==")"):
                                    i+=1
                                    return for_body()
            return syntaxError()
    
    def init11():
        global i, tokenList
        if dec():
            return True
        elif(assign_st()):
            return True
        elif(tokenList[i].type == ";"): 
            return True
        return syntaxError()
    
    def cond11():
        global i, tokenList
        if OE():
            print("for-OE")
            return True
        elif(tokenList[i].type ==";"):
            print("for-;")
            return True
        return syntaxError() 
 
    def inc_dec11():
        global i, tokenList
        print("Inc_dec11")
        if Inc_Dec_obj_call():
            print("I?C")
            return True
        elif(tokenList[i].type==")"):
            #print("??")
            return True
        return syntaxError() 
        
    def for_body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1
            if funct_SST() and tokenList[i].type == "}":
                currentScope = destroyScope()
                i += 1
                return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()

    def for_SST():
        global i, tokenList
        if dec() or func_st() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or break_() or continue_() or return_() or OE():
            return for_SST()
        elif OE():
         if tokenList[i].type == ";":
                i += 1  
                return for_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()

    
# OE:
    def OE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (AE() and OE_()):
            print("555555555555", ofType)
            return True 
        return syntaxError()
    
    def OE_():
        global i, tokenList
        if (tokenList[i].type == "OR"):
            op = tokenList[i].value
            i += 1
            if (AE() and AE_()):
                print("OE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type ==";" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="," or tokenList[i].type =="]"):
            print(",")
            return True
        return syntaxError()
    
    def AE():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (RE() and AE_()):
            print("AE")
            return True
        return syntaxError()
    
    def AE_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        if (tokenList[i].type == "AND"):
            op = tokenList[i].value
            i += 1
            if (RE() and AE_()):
                print("AE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="]" or tokenList[i].type ==";" or tokenList[i].type ==","):
            print(",")
            return True
        return syntaxError()
    
    def RE():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (E() and RE_()):
            print(",RE")
            return True
        return syntaxError()
    
    def RE_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        if (tokenList[i].type == "R_OP"):
            op = tokenList[i].value
            #complist.append(op)
            i += 1
            if (E() and RE_()):
                print("RE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="]" or tokenList[i].type ==";" or tokenList[i].type ==","):
            print(",RE__")
            return True
        return syntaxError()
    
    def E():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (T() and E_()):
            print("E()")
            return True
        return syntaxError()
    
    def E_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        if (tokenList[i].type == "PM"):
            op = tokenList[i].value
            #complist.append(op)
            i += 1
            if (T() and E_()):            # possible issue
                print("E_")
                return True
        elif (tokenList[i].type == "R_OP") or (tokenList[i].type == "AND") or (tokenList[i].type == "OR") or (tokenList[i].type == ")") or (tokenList[i].type == "{" or (tokenList[i].type == "}") or (tokenList[i].type == "]") or (tokenList[i].type == ";")or (tokenList[i].type == ",")    ) :
            print(",E__")
            return True 
        return syntaxError()
    
    def T():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (F() and T_()):
            print("T()")
            return True
        return syntaxError()
    
    def T_():
        global i, tokenList, currentClass, currentFunction, currentScope, scopeStack, op
        if (tokenList[i].type == "MDM"):
            op = tokenList[i].value
            #complist.append(op)
            i += 1
            if (F() and T_()):
                print("T_")
                return True
        elif (tokenList[i].type == "PM") or (tokenList[i].type == "R_OP") or (tokenList[i].type == "AND") or (tokenList[i].type == "OR") or (tokenList[i].type == ")") or (tokenList[i].type == "{" or (tokenList[i].type == "}") or (tokenList[i].type == "]") or (tokenList[i].type == ";")or (tokenList[i].type == ",")    ) :
            print(",T__") 
            return True
        return syntaxError()
    
    def F():
        global i, tokenList, currentClass, currentFunction, currentScope, ofvalue, ofType
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (const()):
            print("2222222222", ofvalue)
            return True
        elif (Inc_Dec_obj_call()):
            print("Inc_Dec_obj_call1")
            return True
        elif (tokenList[i].type == "("):
            #print("(")
            i += 1
            if (OE()):
                if (tokenList[i].type == ")"):
                    #i += 1
                    #print("Inside OE")
                    return True
        elif (tokenList[i].type == "NOT"):
            op = tokenList[i].value
            i += 1
            if (F()):
                #print("Inside F")
                return True
        elif (obj_call()):
            print("i")
            return True
        return syntaxError()
    
    
except LookupError:
    print("Tree Incomplete... Source File (Input) Completely Parsed")
    
    
    
    
# class_dec
'''
    def class_dec():
        global i, tokenList, accessModi, name, typeMod,ofType,ofName, parentList
        if sealed():
            typeMod1 = sealed()
            print("TYPE", typeMod1)
            if tokenList[i].type == "CLASS":
                ofType = tokenList[i].type
                i += 1
                if tokenList[i].type == "ID":
                    ofName = tokenList[i].value
                    insertMainTable(ofName, ofType, accessModi, typeMod, parentList)
                    i += 1
                    if class_dec1():
                        if tokenList[i].type == ";":
                            # parent = ""
                            print("1386.............", parentList)
                            insertMainTable(ofName, ofType, accessModi, typeMod, parentList)
                            print("1387.................")
                            i += 1
                            return True
        return syntaxError()

    def class_dec1():
        global i,tokenList, ofName, ofType, accessModi, typeMod, parentList
        if inherit():
         
            if class_body():
                return True
        return syntaxError()

    def inherit():
        global i, tokenList, ofName, ofType, parentList, typeMod
        if tokenList[i].type == ":":
            i += 1
            if access_mod():
                #parentType=tokenList[i].value
                parentType=access_mod()
                print("1352",parentType)
                if (parentType=="private" or parentType=="protected"):
                    randomError("Can't Inherited")
                if tokenList[i].type == "ID":
                    parent_name = tokenList[i].value
                    check = lookupMainTable(parent_name)
                    print("1406", check.typeMod)
                    if check==False:
                        
                        unDeclaredError(parent_name, "Class does not exist")
                    
                    else:
                        if check.typeMod == "sealed":
                            randomError("Sealed class can't be inherited.")
                        parentList+=tokenList[i].value
                    i += 1
                    if multiple_inherit():
                        return True
        elif tokenList[i].type == "{" or tokenList[i].type == ";":
            return True
        return syntaxError()

    def multiple_inherit():
        global i, tokenList, parentList,typeMod
        if tokenList[i].type == ",":
              
            i += 1
            if access_mod():

                parent1_Type=tokenList[i].value
                print("parent1",parent1_Type)
                if (parent1_Type=="private" or parent1_Type=="protected"):
                    randomError("Can't Inherited")
                if tokenList[i].type == "ID":
                    parent1_name = tokenList[i].value
                    multi_check = lookupMainTable(parent1_name)
                    print(multi_check,"1432")
                    if multi_check==False:
                        unDeclaredError(parent1_name,"Class does no exist.")
                    #elif multi_check == True:

                        #print(multi_check,"1437")
                        #typeMod=sealed()
                        #print("1433", typeMod)
                        #if multi_check.typeMod == "sealed":
                         #   randomError("Sealed class can't be inherited.")



                    else:
                        typeMod=sealed()
                        print("1433", typeMod)
                        if multi_check.typeMod == "SEALED":
                            randomError("Sealed class can't be inherited.")

                        parentList += "," + tokenList[i].value
                    i+=1
                    return multiple_inherit()
        elif tokenList[i].type == "{" or tokenList[i].type == ";":
            return True
        return syntaxError()

    def class_body():
        global i, tokenList
        if(tokenList[i].type=="{"):
            print("BBB")
            i+=1
            if(class_SST()):
                print("AZZZ")
                if(tokenList[i].type =="}"):
                    print("}")
                    i+=1
                    return True
        elif(tokenList[i].type==";"):
            return True
        return syntaxError()
    
    def sealed():
        global i, tokenList, typeMod
        if (tokenList[i].type == "SEALED"):
            typeMod=tokenList[i].value
            print(typeMod,"1478----------------------------")
            i+=1
            return typeMod
        elif(tokenList[i].type=="CLASS"):
            typeMod="-"
            print("elif", typeMod)
            return typeMod
        return syntaxError()
    
    def access_mod():
        global i, tokenList, accessModi
        if(tokenList[i].type=="ACCESS MODIFIER"):
            accessModi=tokenList[i].value
            i+=1
            return accessModi
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        elif(tokenList[i].type=="ID" or tokenList[i].type==":"):
            return accessModi       
        return syntaxError()
    
    def class_SST():
        global i, tokenList
        print("123")
        if access_mod():
            print("A")
            if (tokenList[i].type == ":"):
                i+=1
                return class_SST()
        elif dec():
            return class_SST()
            print("B")
        elif func_st() and class_SST():
            print("C")
            return True
        elif constructor() and class_SST():
            print("D")
            return True
        elif destructor() and class_SST():
            print("E")
            return True
        elif if_else() and class_SST():
            print("F")
            return True
        elif try_catch() and class_SST():
            print("G")
            return True
        elif for_st() and class_SST():
            print("H")
            return True
        elif print_() and class_SST():
            print("I")
            return True
        elif class_dec() and class_SST():
            print("J")
            return True
        elif struct_dec() and class_SST():
            print("K")
            return True
        elif OE():
            print("L")
            if (tokenList[i].type == ";"):
                i += 1
                return class_SST()
        elif struct_obj() and class_SST():
            print("M")
            return True
        elif obj_decl() and class_SST():
            print("N")
            return True
        elif assign_st() and class_SST():
            print("O")
            return True
        elif tokenList[i].type == "}":
            print("P")
            return True
        
        return syntaxError()
'''