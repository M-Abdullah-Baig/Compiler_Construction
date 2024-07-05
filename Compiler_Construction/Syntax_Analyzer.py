
# import sys

i = 0
tokenList = []
# syntaxErr = True
errorAt = 0
synError = ""


def syntaxAnalyzer(tokens):
    global i, tokenList, errorAt, synError
    i = 0
    errorAt = 0
    tokenList = tokens
    result = start()
    if (not result):
        synError += "\nTOKEN UNEXPECTED:\n\tValue:\t" + tokenList[errorAt].value + "\n\tType:\t" + tokenList[errorAt].type + \
              "\n\tFile:\t\'.\\source_file.txt\' [@ " + str(tokenList[errorAt].line) + "]\n\tToken:\t" + str(errorAt) + "\n\n\n"
        #print("\nTOKEN UNEXPECTED:\n\tValue:\t" + tokenList[errorAt].value + "\n\tType:\t" + tokenList[errorAt].type +
        #     "\n\tFile:\t\'.\\source_file.txt\' [@ " + str(tokenList[errorAt].line) + "]\n\tToken:\t" + str(errorAt))
    return synError, result


def syntaxError():
    global i, tokenList, errorAt
    if (i > errorAt):
        errorAt = i
    return False

try: 
    def start():
    
        if dec():
            return True
        elif OE():
            return True
        elif obj_call():
            return True
        
        
        return syntaxError()
        
# Declaration and Initialization:

    def dec():
        global i, tokenList
        if DT1():
            if (tokenList[i].type == "ID"):
                i += 1
                if init():
                    if (tokenList[i].type == ";"):
                        i += 1
                        return True
       
        return syntaxError()
    
    def DT1():
        global i, tokenList
        if (tokenList[i].type == "const"):
            i += 1
            if DT():
                return True
        elif (DT()):
            return True
    
        return syntaxError()
    

    def DT():
        global i, tokenList
        #if (tokenList[i].type == "int" or tokenList[i].type == "float" or tokenList[i].type == "char" or tokenList[i].type == "string" or tokenList[i].type == "bool"):
        if (tokenList[i].type == "DT"):
            i += 1
            return True
        return syntaxError()
    
    def const():
        global i, tokenList
        if (tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR"):
            i += 1
            return True
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
        global i, tokenList
        #if (tokenList[i].type == "="):
        if (SA() and init5()):
            return True
        elif (tokenList[i].type == "["):
            i += 1
            return init1()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError
    
    def init6():
        global i, tokenList
        if (tokenList[i].type == "="):
            if (SA() and init7()):
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init5():
        global i, tokenList
        if (OE()):
            return True
        #elif(take()):
        #    return True
        return syntaxError()
    
    def init7():
        global i, tokenList
        if (tokenList[i].type == "{"):
            i += 1
            if (OE() and init2()):
                if (tokenList[i].type == "}"):
                    i += 1
                    if (init2()):
                        return True
        return syntaxError()
    
    def init2():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            return True
            if (OE() and init2()):
                return True
        elif (tokenList[i].type == "{"):
            i += 1
            if (OE() and init2()):
                if (tokenList[i].type == "}"):
                    i += 1
                    if (init2()):
                        return True
        elif (tokenList[i].type == "}" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init1():
        global i, tokenList
        if (OE()):
            return True
        elif (tokenList[i].type == "]"):
            i += 1
            if (Arr() and init6()):
                return True
        elif (tokenList[i].type == "]"):
            i += 1
            if (Arr() and init6()):
                return True
        return syntaxError()
    
# Expression (OE):    
    
    def OE():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (AE() and OE_()):
                return True 
        return syntaxError()
    
    def OE_():
        global i, tokenList
        if (tokenList[i].type == "|"):
            i += 1
            if (AE() and AE_()):
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def AE():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (RE() and AE_()):
                return True
        return syntaxError()
    
    def AE_():
        global i, tokenList
        if (tokenList[i].type == "&"):
            i += 1
            if (RE() and AE_()):
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "|" or tokenList[i].type == "&"):
            return True
        return syntaxError()
    
    def RE():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (E() and RE_()):
                return True
        return syntaxError()
    
    def RE_():
        global i, tokenList
        if (tokenList[i].type == "<" or tokenList[i].type == ">" or tokenList[i].type == "!" or tokenList[i].type == "="):
            if (RO() and E() and RE_()):
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "|" or tokenList[i].type == "&"):
            return True
        return syntaxError()
    
    def E():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (T() and E_()):
                return True
        return syntaxError()
    
    def E_():
        global i, tokenList
        if (tokenList[i].type == "PM"):
            i += 1
            if (t() and e_()):
                return True
        elif (tokenList[i].type == "<") or (tokenList[i].type == ">") or (tokenList[i].type == "!") or (tokenList[i].type == "=") or (tokenList[i].type == "&") or (tokenList[i].type == "|") or (tokenList[i].type == ")"):
            return True 
        return syntaxError()
    
    def T():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (F() and T_()):
                return True
        return syntaxError()
    
    def T_():
        global i, tokenList
        if (tokenList[i].type == "MDM"):
            i += 1
            if (F() and T_()):
                return True
        elif (tokenList[i].type == "+" or tokenList[i].type == "-" or tokenList[i].type == "<" or tokenList[i].type == ">" or tokenList[i].type == "!" or tokenList[i].type == "=" or tokenList[i].type == "&" or tokenList[i].type == "|" or tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def F():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (const()):
                return True
        elif (Inc_Dec_obj_call()):
            return True
        elif (tokenList[i].type == "("):
            i += 1
            if (OE()):
                if (tokenList[i].type == ")"):
                    return True
        elif (tokenList[i].type == "!"):
            i += 1
            return True
        elif (obj_call()):
            return True
        return syntaxError()
    
 
    def RO():
        global i, tokenList
        if (tokenList[i].type == "<" or tokenList[i].type == ">" or tokenList[i].type == "!" or tokenList[i].type == "="):
            i += 1
            return True
        return syntaxError()
    
    def Arr():    # Issue in follow up
        global i, tokenList
        if (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return Arr()
        elif (tokenList[i].type == "PM"):
            return True
        return syntaxError()
   
# Inc_Dec_obj_call:

    def Inc_Dec_obj_call():
        global i, tokenList
        if (tokenList[i].type == "Inc_Dec"):
            i += 1
            if (B1()):
                if (tokenList[i].type == ";"):
                    return True
        return syntaxError()
    
    def B1():
        global i, tokenList
        if (tokenList[i].type == "ID"):
            i += 1
            if (dot() and inc_dec_op()):
                return True
        elif (tokenList[i].type == "Inc/Dec"):
            i += 1
            return X11()
        elif(tokenList[i].type == "(" or tokenList[i].type == "this"):
            i += 1
            if (B2() and inc_dec_op()):
                return True
        return syntaxError()
        
    
    def B2():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "this"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return dot()
        return syntaxError()
    
    def X11():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "ID"):
                i += 1
                return dot()
        return syntaxError()
    
    def para():
        global i, tokenList
        if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
            if (OE() and para1()):
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def para1():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (OE() and para1()):
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    

    def dot():                                        
        global i, tokenList
        if (tokenList[i].type == "."):
            i += 1
            if (tokenList[i].type == "ID"):
                return dot()
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return dot()
        elif (tokenList[i].type == "("):
            i += 1
            if (para()):
                if (tokenList[i].type == ")"):
                    i += 1
                    return dot()
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()

 
   
  
# object_call:        
    
    def obj_call():
        global i, tokenList
        if (tokenList[i].type == "ID" or tokenList[i].type == "(" or tokenList[i].type == "this"):
            return B_()
        return syntaxError()
    
    def B_():
        global i, tokenList
        if (tokenList[i].type == "ID"):
            i += 1
            return dot()
        elif (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "this"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return dot()
        return syntaxError()
    
# struct_obj:

    def struct_obj():
        global i, tokenList
        if (tokenList[i].type == "st"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (tokenList[i].type == "ID"):
                    i += 1
                    if (list_A() and initA()):
                        if (tokenList[i].type == ";"):
                            return True
                    
        return syntaxError()
            
    def list_A():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return list_A
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return list_A
        elif (tokenList[i].type == "=" or tokenList[i].type == ";"):
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
    
# func_call1:

    def func_call1():
        global i, tokenList
        if (tokenList[i].type == "this"):
            if (p1()):
                if (tokenList[i].type == "ID"):
                    i += 1
                    if (tokenList[i].type == "("):
                        i += 1
                        if (para()):
                            if (tokenList[i] == ")"):
                                i += 1
                                if (tokenList[i].type == ";"):
                                    return True
        return syntaxError()
    
    
                
            
                    
        
        
                    
            
            
    
    
    
            
    
    
    
            
    
        
            
    
    
    
    
    
            
      
            
                 


              

except LookupError:
    print("Tree Incomplete... Input Completely Parsed")




    '''        
          
        if destructor():
            return True 
        elif funct_st():
            return True
        elif if_else():
            return True
        elif try_catch():
            return True
        elif for_st():
            return True
        elif Print():
            return True
        elif struct_dec():
            return True
        elif class_dec():
            return True
        elif OE():
            return True
        elif struct_obj():
            return True
        elif obj_decl():
            return True
        elif assign_st():
            return True
        
        return syntaxError() 
          
    def destructor():
        global i, tokenList
        if (tokenList[i].type == "~"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return indexD()
        return syntaxError()

    
    def indexD():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == ")"):
                i += 1
                if (tokenList[i].type == "{"):
                    i += 1
                    if (tokenList[i].type == "}"):
                        i += 1
                        return True
        return syntaxError()

    '''   
    
# OE    
    
    def OE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (AE() and OE_()):
            return True 
        return syntaxError()
    
    def OE_():
        global i, tokenList
        if (tokenList[i].type == "OR"):
            i += 1
            if (AE() and AE_()):
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def AE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (RE() and AE_()):
            return True
        return syntaxError()
    
    def AE_():
        global i, tokenList
        if (tokenList[i].type == "AND"):
            i += 1
            if (RE() and AE_()):
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND"):
            return True
        return syntaxError()
    
    def RE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (E() and RE_()):
            return True
        return syntaxError()
    
    def RE_():
        global i, tokenList
        if (tokenList[i].type == "RO_P"):
            i += 1
            if (E() and RE_()):
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND"):
            return True
        return syntaxError()
    
    def E():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (T() and E_()):
            return True
        return syntaxError()
    
    def E_():
        global i, tokenList
        if (tokenList[i].type == "PM"):
            i += 1
            if (t() and e_()):            # possible issue
                return True
        elif (tokenList[i].type == "R_OP") or (tokenList[i].type == "R_OP") or (tokenList[i].type == "NOT") or (tokenList[i].type == "=") or (tokenList[i].type == "AND") or (tokenList[i].type == "OR") or (tokenList[i].type == ")"):
            return True 
        return syntaxError()
    
    def T():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (F() and T_()):
            return True
        return syntaxError()
    
    def T_():
        global i, tokenList
        if (tokenList[i].type == "MDM"):
            i += 1
            if (F() and T_()):
                return True
        elif (tokenList[i].type == "PM" or tokenList[i].type == "R_OP" or tokenList[i].type == "NOT" or tokenList[i].type == "AO" or tokenList[i].type == "AND" or tokenList[i].type == "OR" or tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def F():
        global i, tokenList
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (const()):
            return True
        elif (Inc_Dec_obj_call()):
            return True
        elif (tokenList[i].type == "("):
            i += 1
            if (OE()):
                if (tokenList[i].type == ")"):
                    return True
        elif (tokenList[i].type == "NOT"):
            i += 1
            if (F()):
                return True
        elif (obj_call()):
            return True
        return syntaxError()
    
 
    def RO():
        global i, tokenList
        if (tokenList[i].type == "R_OP" or tokenList[i].type == "R_OP" or tokenList[i].type == "R_OP" or tokenList[i].type == "R_OP" or tokenList[i].type == "R_OP" or tokenList[i].type == "R_OP"):
            i += 1
            return True
        return syntaxError()
    
    def Arr():    # Issue in follow up
        global i, tokenList
        if (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return Arr()
        elif (tokenList[i].type == "PM" or tokenList[i].type == "AO" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    
# for_st

    def for_st():
        global i, tokenList
        if tokenList[i].type == "FOR":
            i += 1
            if tokenList[i].type == "(":
                i += 1
                #if init11() and tokenList[i].type == ";" and cond11() and tokenList[i].type == ";" and inc_dec11() and tokenList[i].type == ")":
                if init11():
                    if tokenList[i].type == ";": 
                        i += 1
                        if cond11():
                            if tokenList[i].type == ";": 
                                i += 1
                                if inc_dec11():
                                    if tokenList[i].type == ")":
                                        i += 1
                                        return for_body()
        return syntaxError()

    def init11():
        #if tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "char" or tokenList[i].type == "STR" or tokenList[i].type == "bool":
        if dec() or assign_st():
            return True
        #elif(tokenList[i]=="assign"):#first of assign st
        #    if(assign_st()):
        #        return True
        elif(tokenList[i].type == ";"): 
            return True
        return syntaxError()

    def cond11():
        #if tokenList[i].type in ["this","int_const", "flt_const", "string_const", "char_const", "(", "!", "Inc_Dec", "ID"]:
        if OE():
            return True
        elif(tokenList[i]==";"):
            return True
        return syntaxError()  

    def inc_dec11():
        if(tokenList[i].type=="Inc_Dec"):
            if Inc_Dec_obj_call():
                return True
        elif(tokenList[i].type==")"):
            return True
        return syntaxError()

    def for_body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1
            if funct_SST() and tokenList[i].type == "}":
                i += 1
                return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()

    def for_SST():
        global i, tokenList
        if dec() or func_st() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st():
            return for_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return for_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon
    