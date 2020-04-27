from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
import sys
import pprint

cubo = {
    '+' : {
        'int': {
            'int': 'int',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '-' : {
        'int': {
            'int': 'int',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '/' : {
        'int': {
            'int': 'float',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '*' : {
        'int': {
            'int': 'int',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '>' : {
        'int': {
            'int': 'bool',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'bool',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '<' : {
        'int': {
            'int': 'bool',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'bool',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '||' : {
        'int': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'bool',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '&' : {
        'int': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'bool',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '==' : {
        'int': {
            'int': 'bool',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'x',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'bool',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'bool',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '!=' : {
        'int': {
            'int': 'bool',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'x',
            'float': 'bool',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'bool',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'bool',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    },
    '=' : {
        'int': {
            'int': 'OK',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'float': {
            'int': 'x',
            'float': 'OK',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        },
        'char': {
            'int': 'x',
            'float': 'x',
            'char': 'OK',
            'bool': 'x',
            'void': 'x'
        },
        'bool': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'OK',
            'void': 'x'
        },
        'void': {
            'int': 'x',
            'float': 'x',
            'char': 'x',
            'bool': 'x',
            'void': 'x'
        }
    }
}

class Programa:
    def __init__(self, tree, rules):
        self.tree = tree
        self.rules = rules
        self.varGlobales = {}
        self.dirFunciones = {}
        self.pilaCuad = []

    def error(self,tipo,mensaje):
        print(tipo,mensaje)

    def imprimeTodo(self):
        # self.evaluar(self.tree.principal().bloque_est(),"main")
        # for child in self.tree.principal().bloque_est().children:
        #     print("hijo")
        print("===== Nombre Programa =====")
        print(self.tree.ID())
        print("===== Variables =====")
        # traverse(self.tree.dec_variables(),self.rules)
        # self.variablesGlobales(self.tree.variables().var(),self.rules)
        # print(self.tree.dec_variables().getText())
        self.decVariables(self.tree.dec_variables(),self.varGlobales,"")
        pprint.pprint(self.varGlobales)
        # print(self.varGlobales)
        # p1.llamadaglobales(p1.tree.variables().var(),p1.rules)
        # variablesGlobales(programa.variables().var(),reglas)
        print("===== Funciones =====")
        self.decFunciones(self.tree.dec_functions())
        # print(self.dirFunciones)
        pprint.pprint(self.dirFunciones)
        # print(self.existeVar("nice","fact"))
        # if not self.checaFun("fact",["int"]):
        #     print("no existe")
        # else:
        #     print("si existe")
        # print(self.checaParams("dos",["int","int"]))
        # print(self.regresaTipo("nice","fact"))
        # # decFunciones(programa.functions(),reglas)
        print("===== Main =====")
        self.evaluarBloqueEst(self.tree.principal().bloque_est(),"main")

        for i in range(len(self.pilaCuad)):
            print(i+1, ".-",self.pilaCuad[i])
        # print(self.pilaCuad)
        # self.evaluarFun(self.tree.principal().bloque_est(),"main")

        # evaluarFun(programa.principal().bloque_est().estatutos(),reglas)

    ##### VERIFICACIONES

    def checaFun(self,funcion,params):
        if not self.existeFun(funcion):
            return False
        if self.checaParams(funcion,params):
            return True
        return False

    def checaParams(self,funcion,params):
        if self.dirFunciones[funcion]['params']['num'] != len(params):
            return False
        paramsFuncion = self.dirFunciones[funcion]['params']['tipo']
        if paramsFuncion == params:
            return True
        return False

    def existeFun(self,funcion):
        if self.dirFunciones.get(funcion, None) == None:
            return False
        return True

    def existeVar(self,var,funcion):
        res = self.varGlobales.get(var, None)
        if res != None:
            return True
        if funcion != "main":
            if res == None:
                res = self.dirFunciones[funcion]['vars'].get(var, None)
                if res == None:
                    return False
                else:
                    return True
            else:
                return False
        return False

    #Funcion que regresa el tipo de una variable
    def regresaTipo(self,var,funcion):
        if self.existeVar(var,funcion):
            res = self.varGlobales.get(var, None)
            if res != None:
                return self.varGlobales[var]['tipo']
            if funcion != "main":
                if res == None:
                    res = self.dirFunciones[funcion]['vars'].get(var, None)
                    if res == None:
                        return False
                    else:
                        return self.dirFunciones[funcion]['vars'][var]['tipo']
                else:
                    return False
        else:
            return False

    ##### PARSE VARS Y FUNCIONES

    #Funcion que regresa el JSON con la info de las vars
    def decVariables(self,tree,temp,tipo):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "dec_var":
                tipo = tree.tipo().getText()
            elif self.rules[tree.getRuleIndex()] == "ids":
                elem = tree.getText()
                # print(tree.getText())
                # traverse(tree,self.rules)
                if elem.find("[") == -1:
                    temp[elem] = {'tipo': tipo}
                else:
                    count = elem.count("[")
                    if count == 1:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        nombre = elem[:indexInicio]
                        dim = elem[indexInicio+1:indexFinal]
                        temp[nombre] = {'tipo': tipo,'dim1': dim}
                    if count == 2:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        indexInicio2 = elem.find("[", indexInicio + 1)
                        indexFinal2 = elem.find("]", indexFinal + 1)
                        nombre = elem[:indexInicio]
                        dim = elem[indexInicio+1:indexFinal]
                        dim2 = elem[indexInicio2+1:indexFinal2]
                        temp[nombre] = {'tipo': tipo,'dim1': dim,'dim2':dim2}

            else:
                pass
            for child in tree.children:
                self.decVariables(child,temp,tipo)

    #Funcion que actualiza el dir de decFunciones con los
    #datos de las decFunciones del programa
    def decFunciones(self, tree):
        if not isinstance(tree, TerminalNodeImpl):
            # variablesGlobales(child, rule_names)
            # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
            if self.rules[tree.getRuleIndex()] == "funcion":
                nombreFun = tree.ID().getText()
                jsontemp = {}

                # jsontemp["nombre"] = tree.ID().getText()

                # print("Funcion: ", tree.ID())
                # traverse(tree.params(),rule_names)
                # self.evaluarFun(tree.bloque_est().estatutos(),rules)
                tempVar = {}
                self.decVariables(tree.dec_variables(),tempVar,"")

                # print(tempVar)
                # print("vars func: ", tree.variables().var().getText())


                # print("Main de la funcion: ", tree.bloque_est().getText())
                tipo_ret = tree.tipo_ret()
                if tipo_ret.getText() == "void":
                    ret = "void"
                    # print("Tipo ret: void")
                else:
                    ret = tipo_ret.tipo().getText()
                    # print("Tipo ret: ",tipo_ret.tipo().getText())

                arregloTipo = []
                arregloNoms = []
                self.decParamsFun(tree.params(),arregloTipo,arregloNoms)

                jsontemp["vars"] = tempVar
                jsontemp["params"] = {"num": len(arregloTipo), "tipo": arregloTipo, "nombres": arregloNoms }
                jsontemp["tipoRet"] = ret
                jsontemp["main"] = tree.bloque_est()
                jsontemp["mainTextp"] = tree.bloque_est().getText()
                # jsontemp["mainTexto"] = tree.bloque_est().estatuto().getText()

                self.dirFunciones[nombreFun] = jsontemp
                # pprint.pprint(jsontemp)
            else:
                for child in tree.children:
                        self.decFunciones(child)

            # elif rules[tree.getRuleIndex()] == "params":
            #     count = 0
            #     print(tree.getText())
            #     self.decParamsFun(tree,{},count)
            #     print(count)
                # print("Tipo var: ", tree.tipo().getText())
                # print("Nombre var: ", tree.ID())


        else:
            pass

    def decParamsFun(self,tree,temp1,temp2):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                temp1.append(tree.tipo().getText())
                temp2.append(tree.ID().getText())

            for child in tree.children:
                self.decParamsFun(child,temp1,temp2)
        else:
            pass

    #### EXPRESION

    def expresion(self,tree,funcion):
        pilas = {
            'pOperandos' : [],
            'pOperadores' : [],
            'pTipos' : []
        }
        self.expresionAux(tree,funcion,pilas)
        # for child in tree.children:
        #     rule = self.rules[tree.getRuleIndex()]
        #     print("Rule: ", rule)
        # print("==== Final ====")
        # print("Pila operandos:",pilas['pOperandos'])
        # print("Pila tipos:",pilas['pTipos'])
        # print("Pila operadores:",pilas['pOperadores'])

    def genQuad(self,op,left,right):
        if op == '*':
            res = left * right
        elif op == '/':
            res = left / right
        elif op == '+':
            res = left + right
        elif op == '-':
            res = left - right
        elif op == '<':
            res = left < right
        elif op == '>':
            res = left > right
        elif op == '==':
            res = (left == right)
        elif op == '!=':
            res = (left != right)
        elif op == '&':
            res = (left and right)
        elif op == '||':
            res = (left or right)
        return res

    def expresionAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("expresion")
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child,funcion,pilas)
                        if pilas['pOperadores']:
                            op = pilas['pOperadores'][-1]
                            if op == '<' or op == '>' or op == '==' or op == '!=':
                                if len(pilas['pOperandos']) > 1:

                                    pilas['pOperadores'].pop()

                                    right = pilas['pOperandos'].pop()
                                    rightType = pilas['pTipos'].pop()
                                    left = pilas['pOperandos'].pop()
                                    leftType = pilas['pTipos'].pop()
                                    tipoRes = cubo[op][rightType][leftType]
                                    if tipoRes == "x":
                                        print("Operacion no valida")
                                    elif tipoRes == "int":
                                        right = int(right)
                                        left = int(left)
                                    elif tipoRes == "float":
                                        right = float(right)
                                        left = float(left)
                                    elif rightType == "float":
                                        right = float(right)
                                        left = float(left)
                                    elif leftType == "float":
                                        right = float(right)
                                        left = float(left)
                                    else:
                                        right = int(right)
                                        left = int(left)
                                    
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    quad = "quad: " + op + " " + str(left) + " " + str(right) + " " + str(res)
                                    self.pilaCuad.append(quad)


                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)
                                    #
                                    # print("= Pilas temporales =")
                                    # print("Pila operandos:",pilas['pOperandos'])
                                    # print("Pila tipos:",pilas['pTipos'])
                                    # print("Pila operadores:",pilas['pOperadores'])
                                    # print(res)
                                    # print("mayor a dos")
                                else:
                                    pass

                            else:
                                pass
                    elif ruleChild == "op_log":
                        op = child.getText()
                        pilas['pOperadores'].append(op)
                    elif ruleChild == "op_comp":
                        op = child.getText()
                        pilas['pOperadores'].append(op)
                    elif ruleChild == "expresion":
                        self.expresionAux(child,funcion,pilas)
                        if pilas['pOperadores']:
                            op = pilas['pOperadores'][-1]
                            if op == '||' or op == '&':
                                if len(pilas['pOperandos']) > 1:

                                    pilas['pOperadores'].pop()

                                    right = pilas['pOperandos'].pop()
                                    rightType = pilas['pTipos'].pop()
                                    left = pilas['pOperandos'].pop()
                                    leftType = pilas['pTipos'].pop()
                                    tipoRes = cubo[op][rightType][leftType]
                                    
                                    if tipoRes == "x":
                                        print("Operacion no valida")
                                    
                                    # elif tipoRes == "int":
                                    #    right = int(right)
                                    #    left = int(left)
                                    # elif tipoRes == "float":
                                    #    right = float(right)
                                    #    left = float(left)

                                    if right == "True":
                                        right = True
                                    elif right == "False":
                                        right = False

                                    if left == "True":
                                        left = True
                                    elif left == "False":
                                        left = False

                                    #print("rightType",type(right))
                                    #print("leftType",type(left))
                                    #print("right",right)
                                    #print("left",left)                                      
                                
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    quad = "quad: " + op + " " + str(left) + " " + str(right) + " " + str(res)
                                    self.pilaCuad.append(quad)

                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)

                                    # print("= Pilas temporales =")
                                    # print("Pila operandos:",pilas['pOperandos'])
                                    # print("Pila tipos:",pilas['pTipos'])
                                    # print("Pila operadores:",pilas['pOperadores'])
                                    # # print(res)
                                    # print("mayor a dos")
                                else:
                                    pass

                            else:
                                pass
        else:
            pass

    def expAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "exp":
                # print("exp")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child,funcion,pilas)
                    elif ruleChild == "op_arit":
                        op = child.getText()
                        pilas['pOperadores'].append(op)
                        # print("encontre + o -")
                    elif ruleChild == "term":
                        self.termAux(child,funcion,pilas)

                        if pilas['pOperadores']:
                            op = pilas['pOperadores'][-1]
                            if op == '+' or op == '-':
                                if len(pilas['pOperandos']) > 1:

                                    pilas['pOperadores'].pop()

                                    right = pilas['pOperandos'].pop()
                                    rightType = pilas['pTipos'].pop()
                                    left = pilas['pOperandos'].pop()
                                    leftType = pilas['pTipos'].pop()
                                    tipoRes = cubo[op][rightType][leftType]
                                    if tipoRes == "x":
                                        print("Operacion no valida")
                                    elif tipoRes == "int":
                                        right = int(right)
                                        left = int(left)
                                    elif tipoRes == "float":
                                        right = float(right)
                                        left = float(left)
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    quad = "quad: " + op + " " + str(left) + " " + str(right) + " " + str(res)
                                    self.pilaCuad.append(quad)

                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)
                                    #
                                    # print("= Pilas temporales =")
                                    # print("Pila operandos:",pilas['pOperandos'])
                                    # print("Pila tipos:",pilas['pTipos'])
                                    # print("Pila operadores:",pilas['pOperadores'])
                                    # # print(res)
                                    # print("mayor a dos")
                                else:
                                    pass

                            else:
                                pass

        else:
            pass

    def termAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "term":
                # print("term")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "factor":
                        self.factorAux(child,funcion,pilas)

                        if pilas['pOperadores'] and len(pilas['pOperandos']) > 1:
                            op = pilas['pOperadores'][-1]
                            if op == '*' or op == '/':
                                pilas['pOperadores'].pop()
                                right = pilas['pOperandos'].pop()
                                rightType = pilas['pTipos'].pop()
                                left = pilas['pOperandos'].pop()
                                leftType = pilas['pTipos'].pop()
                                tipoRes = cubo[op][rightType][leftType]
                                if tipoRes == "x":
                                    print("Operacion no valida")
                                elif tipoRes == "int":
                                    right = int(right)
                                    left = int(left)
                                elif tipoRes == "float":
                                    right = float(right)
                                    left = float(left)
                                # print("der: ",right,"izq:",left)
                                res = self.genQuad(op,left,right)
                                # print(res)
                                #print("quad: ", op, left,right,res)

                                quad = "quad: " + op + " " + str(left) + " " + str(right) + " " + str(res)
                                self.pilaCuad.append(quad)

                                # print("= Pilas temporales =")
                                # print("Pila operandos:",pilas['pOperandos'])
                                # print("Pila tipos:",pilas['pTipos'])
                                # print("Pila operadores:",pilas['pOperadores'])

                                pilas['pOperandos'].append(str(res))
                                pilas['pTipos'].append(tipoRes)
                                    # print(res)
                                    # print("mayor a dos"
                            else:
                                pass
                    elif ruleChild == "op_prod":
                        op = child.getText()
                        pilas['pOperadores'].append(op)
                    elif ruleChild == "term":
                        self.termAux(child,funcion,pilas)
        else:
            pass

    def factorAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "factor":
                # print("factor")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "var":
                        self.varAux(child,funcion,pilas)
                        # self.factorAux(child,funcion,pilas)
                    elif ruleChild == "var_cte":
                        self.varcteAux(child,funcion,pilas)
                    elif ruleChild == "op_esp":
                        print("encontre $ ? ¡")
                    elif ruleChild == "op_arit":
                        print("encontre + -")
                    elif ruleChild == "exp_par":
                        # print("encontre algo con parentesis")
                        self.parentesisAux(child,funcion,pilas)
                    elif ruleChild == "llamada":
                        print("encontre llamada a fun")
                        # self.termAux(child,funcion,pilas)
        else:
            pass

    def parentesisAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "exp_par":
                # print("exp_par")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "par_empieza":
                        pilas['pOperadores'].append('$')
                        # print("meti el par")
                    elif ruleChild == "par_termina":
                        if pilas['pOperadores'][-1] == '$':
                            pilas['pOperadores'].pop()
                            # print("saque el par")
                    elif ruleChild == "expresion":
                        self.expresionAux(child,funcion,pilas)
        else:
            pass

    def varAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var":
                nomVar = tree.ID().getText()
                # print("Var : " , nomVar)
                tipo = self.regresaTipo(tree.ID().getText(),funcion)

                pilas['pTipos'].append(tipo)
                pilas['pOperandos'].append(nomVar)

                if tipo == False:
                    print("Error, no existe la variable")
                    return

                # dims = []
                for child in tree.children:
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "dim":
                            self.expresionAux(child.expresion(),funcion,pilas)
                            # print(child.expresion().getText())
                            # dims.append(child.getText())
                # print(dims)
        else:
            pass

    def varcteAux(self,tree,funcion,pilas):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var_cte":
                for child in tree.children:
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "var":
                            self.varAux(child,funcion,pilas)
                    else:
                        cte = tree.getText()
                        if cte.find('.') != -1:
                            tipo = "float"
                        elif cte.find("''") != -1:
                            tipo = "char"
                            cte = cte.replace("'","")
                        else:
                            tipo = "int"

                        pilas['pTipos'].append(tipo)
                        pilas['pOperandos'].append(cte)
                        # print("= Pilas temporales =")
                        # print("Pila operandos:",pilas['pOperandos'])
                        # print("Pila tipos:",pilas['pTipos'])
                        # print("Pila operadores:",pilas['pOperadores'])

                            # print(child.expresion().getText())
                            # dims.append(child.getText())
                # print(dims)
        else:
            pass

    #### ESTATUTOS

    def evaluarBloqueEst(self, tree,funcion):
        if not isinstance(tree, TerminalNodeImpl):
            for child in tree.children:
                if not isinstance(child, TerminalNodeImpl):
                    if self.rules[child.getRuleIndex()] == "estatuto":
                        for child2 in child.children:
                            regla = self.rules[child2.getRuleIndex()]
                            if regla == "retorno":
                                # print("*** Retorno ***")
                                self.est_retorno(child2,funcion)
                            elif regla == "lectura":
                                # print("*** Lee ***")
                                self.est_lectura(child2)
                            elif regla == "asignacion":
                                # print("*** asignacion ***")
                                self.est_asignacion(child2,funcion)
                            elif regla == "decision":
                                # print("*** Decision ***")
                                self.est_decision(child2,funcion)
                            elif regla == "repeticion":
                                # print("*** Repeticion ***")
                                self.est_repeticion(child2,funcion)
                            elif regla == "llamada_est":
                                # print("*** Llamada ***")
                                self.est_llamada_est(child2.llamada_est().llamada().ID().getText(),tree.llamada_est().llamada().params_llamada())
                            elif regla == "escritura":
                                # print("*** Print ***")
                                self.est_escritura(child2,funcion)

        else:
            pass

    def est_retorno(self, tree,funcion):
        if funcion == "main":
            print("error: el main no tiene retorno","idk")
        elif self.dirFunciones[funcion]['tipoRet'] == "void":
            print("error:  la funcion es void","idk")
        self.expresion(tree.expresion(),funcion)
        #else mandar llamar expresion con el codigo
        # print(tree.expresion().getText())

    def est_lectura(self, tree):
        # for child in tree.lista_vars().children:
        #     if not isinstance(child, TerminalNodeImpl):
        #         regla = self.rules[child.getRuleIndex()]
        #         print(regla)
        #
        # print(tree.lista_vars().getText())
        # traverse(tree.lista_vars(),self.rules)
        res = []
        self.lecturaAux(tree.lista_vars(),res)
        for var in res:
            #print("quad: lee",var)

            quad = "quad: lee " + var
            self.pilaCuad.append(quad)
        # print(res)

    def lecturaAux(self,tree,res):
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                regla = self.rules[child.getRuleIndex()]
                if regla == "var":
                    res.append(child.ID().getText())
                    # print(child.ID().getText())
                elif regla == "lista_vars":
                    self.lecturaAux(child,res)
                    # traverse(child,self.rules)
                # print(regla)

    def est_asignacion(self, tree,funcion):
        # traverse(tree,self.rules)
        # print(len(tree.children))
        # print(tree.getText())
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "asignacion":
                # print("asign")
                pila = []
                tipos = []
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "var":
                            nombre = child.ID().getText()
                            tipo = self.regresaTipo(nombre,funcion)

                            if not tipo:
                                print("Error, no se encontro la var")

                            pila.append(nombre)
                            tipos.append(tipo)
                        elif ruleChild == "expresion":
                            # print("exp")
                            self.expresion(child,funcion)

                #print("quad: = EXP", pila[-1])

                quad = "quad: = EXP " + pila[-1]
                self.pilaCuad.append(quad)

                if len(pila) > 1:
                    for i in range(len(pila) - 1):
                        var1 = pila.pop()
                        #print("quad: =", var1, pila[-1])
                        tipo1 = tipos.pop()
                        posible = cubo['='][tipo1][tipos[-1]]
                        if posible == 'OK':
                            quad = "quad: = " + var1 + " " + pila[-1]
                            self.pilaCuad.append(quad)
                        else:
                            print("error, no se puede asignar tipos diferentes")
                # print(pila)
                # print(tipos)

        else:
            pass
        # traverse(codigo,self.rules)
        #chec var existe en funcion
        #llama al exp y asigna el valor

    def est_decision(self, tree,funcion):
        pSaltos = []
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "decision":
                primerBloque = True
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "expresion":
                            self.expresion(child,funcion)
                            #print("quad: gotof varAnterior pos")

                            quad = "quad: gotof varAnterior pos"
                            self.pilaCuad.append(quad)
                            pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            if primerBloque:
                                # print("Entonces: ")
                                self.evaluarBloqueEst(child,funcion)
                                #print("quad: goto pos")

                                quad = "quad: goto pos"
                                self.pilaCuad.append(quad)
                                pSaltos.append(len(self.pilaCuad))
                            else:
                                # print("Si no: ")
                                self.evaluarBloqueEst(child,funcion)
                                pSaltos.append(len(self.pilaCuad))


                            primerBloque = False

                            # print("exp")

                self.pilaCuad[pSaltos[0]-1] = "quad: gotof varAnt " + str(pSaltos[1]+1)
                self.pilaCuad[pSaltos[1]-1] = "quad: goto " + str(pSaltos[2]+1)
                # print(pSaltos)
                # print(pila)
                # print(tipos)

        else:
            pass
        # traverse(codigo,self.rules)
        #chec var existe en funcion
        #llama al exp y asigna el valor

    def est_repeticion(self, tree,funcion):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "repeticion":
                for child in tree.children:
                    regla = self.rules[child.getRuleIndex()]
                    if regla == "condicional":
                        self.est_condicional(child,funcion)
                    elif regla == "no_condicional":
                        self.est_nocondicional(child,funcion)

    def est_condicional(self, tree,funcion):
        pSaltos = []
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "condicional":
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "expresion":
                            pSaltos.append(len(self.pilaCuad))
                            self.expresion(child,funcion)
                            #print("quad: gotof varAnterior pos")

                            quad = "quad: gotof varAnterior pos"
                            self.pilaCuad.append(quad)
                            pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            self.evaluarBloqueEst(child,funcion)
                            quad = "quad: goto pos"
                            self.pilaCuad.append(quad)
                            pSaltos.append(len(self.pilaCuad))
                            # if primerBloque:
                            #     # print("Entonces: ")
                            #     self.evaluarBloqueEst(child,funcion)
                            #     #print("quad: goto pos")
                            #
                            #     quad = "quad: goto pos"
                            #     self.pilaCuad.append(quad)
                            #     pSaltos.append(len(self.pilaCuad))
                            # else:
                            #     # print("Si no: ")
                            #     self.evaluarBloqueEst(child,funcion)
                            #     pSaltos.append(len(self.pilaCuad))



                            # print("exp")
                self.pilaCuad[pSaltos[1]-1] = "quad: gotof varAnt " + str(pSaltos[2]+1)
                self.pilaCuad[pSaltos[2]-1] = "quad: goto " + str(pSaltos[0]+1)
                # self.pilaCuad[pSaltos[0]-1] = "quad: gotof varAnt " + str(pSaltos[1]+1)
                # self.pilaCuad[pSaltos[1]-1] = "quad: goto " + str(pSaltos[2]+1)
                # print(pSaltos)
                # print(pila)
                # print(tipos)

        else:
            pass

    def est_nocondicional(self, tree,funcion):
        print("es no condicional")

    ##falta
    #los params pueden ser exp
    #checar que sea valida la llamada
    #checar que los params sean compatibles
    def est_llamada_est(self,funcion,params):
        print("Nombre fun:", funcion)
        print("Params fun:", params.getText())
        # print("una llamada una funcion")
        # traverse(codigo,self.rules)
        # print(codigo.llamada_est().llamada().ID())
        # nombre = codigo.llamada_est().llamada().ID().getText()
        # estatutos = self.dirFunciones[nombre]['main']
        # self.evaluarFun(estatutos,nombre)
        # print(estatutos)

    def est_escritura(self, tree,funcion):
        res = []
        str = ""
        self._extraePrint(tree,res,funcion)
        for index, item in enumerate(res):
            res[index] = res[index][1:-1]
            str += res[index] + " "
        #print("quad: print", str)

        quad = "quad: print " + str
        self.pilaCuad.append(quad)

    ##falta
    #los valores pueden ser exp
    def _extraePrint(self, tree,res,funcion):

        # traverse(codigo,self.rules)
        # lista = codigo.getRuleContext().getText()
        # lista = lista.split(",")
        # print(lista)
        # for valor in lista:
        #     if valor[0] == '\'':
        #         print("string")
        #     else:
        #         lista.remove(valor)
        #         # pass
        # print(lista)
        if not isinstance(tree, TerminalNodeImpl):
        #     # print(codigo.getRuleContext().getText())
        #     # traverse(codigo,self.rules)
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("***** EXP *****")
                # print(codigo.getText())
                # traverse(codigo,self.rules)
                self.expresion(tree,funcion)
                #mandar llamar expresion con el codigo
                res.append("'EXP'")
                # print("")
            elif self.rules[tree.getRuleIndex()] == "string":
                # print("es un string")
                res.append(tree.getText())
            else:
                # traverse(codigo,self.rules)
                # print("no string")
        #         print("lo ignoramos")
                for child in tree.children:
                    # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                    #     print("Estatuto: ", tree)
                    self._extraePrint(child,res,funcion)
        #

        else:
            pass


def main():
    arch = sys.argv[1]
    if arch == '1':
        input_stream = FileStream("prueba.txt")
    elif arch == '2':
        input_stream = FileStream("prueba2.txt")
    elif arch == '3':
        input_stream = FileStream("prueba3.txt")
    elif arch == '4':
        input_stream = FileStream("prueba4.txt")

    lexer = PatitoMasMasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoMasMasParser(stream)
    rutaInicio = parser.start().programa()

    # traverse(rutaInicio,parser.ruleNames)

    programa = Programa(rutaInicio,parser.ruleNames)
    programa.imprimeTodo()

def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)


if __name__ == '__main__':
    main()
