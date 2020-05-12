from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
from antlr4.error.ErrorListener import ErrorListener
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

class Cuadruplo:
    def __init__(self, op,dir1,dir2,dir3):
         self.op = op
         self.dir1 = dir1
         self.dir2 = dir2
         self.dir3 = dir3
    def imprimir(self):
        str = "quad: {} {} {} {}".format(self.op,self.dir1,self.dir2,self.dir3)
        return str

class Programa:
    def __init__(self, tree, rules):
        self.tree = tree
        self.rules = rules
        # self.varGlobales = {}
        self.dirFunciones = {}
        self.pilaCuad = []
        self.pilaSaltos = []

    def error(self,tree,mensaje):
        line = tree.getSymbol().line
        column = tree.getSymbol().column
        print("Error linea-> {}:{} -> {}".format(line,column,mensaje))

    def imprimeTodo(self):
        varGlobales = {}
        self.decVariables(self.tree.dec_variables(),varGlobales,"")
        self.dirFunciones['global'] = {'vars': varGlobales}
        self.pilaCuad.append(Cuadruplo('goto','main',0,0))
        self.decFunciones(self.tree.dec_functions())
        self.pilaSaltos.append(len(self.pilaCuad)+1)
        self.dirFunciones['global']["empieza"] = len(self.pilaCuad)+1
        self.evaluarBloqueEst(self.tree.principal().bloque_est(),"main")
        self.pilaCuad.append(Cuadruplo('end',0,0,0))
        #Imprime cuadruplos
        print("===== Cuadruplos =====")
        for i in range(len(self.pilaCuad)):
            print(i+1, ".-",self.pilaCuad[i].imprimir())
        print("===== Dir Funciones =====")
        pprint.pprint(self.dirFunciones)


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
        res = self.dirFunciones['global']['vars'].get(var, None)
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
    def regresaTipoVar(self,var,funcion):
        if self.existeVar(var,funcion):
            res = self.dirFunciones['global']['vars'].get(var, None)
            if res != None:
                return self.dirFunciones['global']['vars'][var]['tipo']
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

    def regresaInicioFun(self,funcion):
        if self.existeFun(funcion):
            return self.dirFunciones[funcion]['empieza']
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
            if self.rules[tree.getRuleIndex()] == "funcion":
                nombreFun = tree.ID().getText()
                if(self.existeFun(nombreFun)):
                    msj = "Ya existe una funcion definida con el mismo nombre '{}'".format(nombreFun)
                    return self.error(tree.ID(),msj)
                else:
                    jsontemp = {}

                    tempVar = {}
                    self.decVariables(tree.dec_variables(),tempVar,"")

                    tipo_ret = tree.tipo_ret()
                    if tipo_ret.getText() == "void":
                        ret = "void"
                    else:
                        ret = tipo_ret.tipo().getText()
                        self.dirFunciones['global']['vars'][nombreFun] = {'tipo' : ret}
                    tablaParams = []
                    varsParams = {}
                    self.decParamsFun(tree.params(),varsParams,tablaParams)
                    varsFunc = dict(list(varsParams.items()) + list(tempVar.items()))
                    cuadEmpieza = len(self.pilaCuad) + 1
                    jsontemp["params"] = tablaParams
                    jsontemp["vars"] = varsFunc
                    jsontemp["tipoRet"] = ret
                    jsontemp["empieza"] = cuadEmpieza
                    self.dirFunciones[nombreFun] = jsontemp
                    self.evaluarBloqueEst(tree.bloque_est(),nombreFun)
                    self.pilaCuad.append(Cuadruplo('endproc',0,0,0))
            else:
                for child in tree.children:
                        self.decFunciones(child)
        else:
            pass

    def decParamsFun(self,tree,varsParams,tablaParams):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                nombre = tree.ID().getText()
                tipo = tree.tipo().getText()
                tablaParams.append(tipo)
                varsParams[nombre] = {'tipo': tipo}

            for child in tree.children:
                self.decParamsFun(child,varsParams,tablaParams)
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
                                    # print("tipo res:", tipoRes)
                                    if tipoRes == "x":
                                        print("Operacion no valida")
                                    elif tipoRes == "int":
                                        right = int(right)
                                        left = int(left)
                                    elif tipoRes == "float":
                                        right = float(right)
                                        left = float(left)
                                    elif rightType == "float" or leftType == "float":
                                        right = float(right)
                                        left = float(left)
                                    else:
                                        right = int(right)
                                        left = int(left)

                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    self.pilaCuad.append(Cuadruplo(op,left,right,res))


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


                                    if right == "True":
                                        right = True
                                    elif right == "False":
                                        right = False

                                    if left == "True":
                                        left = True
                                    elif left == "False":
                                        left = False
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)

                                    self.pilaCuad.append(Cuadruplo(op,left,right,res))

                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)

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

                                    self.pilaCuad.append(Cuadruplo(op,left,right,res))

                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)
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

                                self.pilaCuad.append(Cuadruplo(op,left,right,res))

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
                        self.est_llamada_est(child,funcion)
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
                tipo = self.regresaTipoVar(tree.ID().getText(),funcion)

                pilas['pTipos'].append(tipo)
                pilas['pOperandos'].append(nomVar)

                if tipo == False:
                    msj = "No se encontró la var '{}'".format(nomVar)
                    return self.error(tree.ID(),msj)

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
        # print("entre")
        if not isinstance(tree, TerminalNodeImpl):
            for child in tree.children:
                if not isinstance(child, TerminalNodeImpl):
                    if self.rules[child.getRuleIndex()] == "estatuto":
                        for child2 in child.children:
                            regla = self.rules[child2.getRuleIndex()]
                            if regla == "retorno":
                                # self.error(tree,"hola")
                                # print("*** Retorno ***")
                                self.est_retorno(child2,funcion)
                            elif regla == "lectura":
                                # print("*** Lee ***")
                                self.est_lectura(child2,funcion)
                            elif regla == "asignacion_est":
                                # print("*** asignacion ***")
                                self.est_asignacion(child2.asignacion(),funcion)
                            elif regla == "decision":
                                # print("*** Decision ***")
                                self.est_decision(child2,funcion)
                            elif regla == "repeticion":
                                # print("*** Repeticion ***")
                                self.est_repeticion(child2,funcion)
                            elif regla == "llamada_est":
                                # print("*** Llamada ***")
                                self.est_llamada_est(child2.llamada(),funcion)
                            elif regla == "escritura":
                                # print("*** Print ***")
                                self.est_escritura(child2,funcion)

        else:
            pass

    def est_retorno(self, tree,funcion):
        if funcion == "main":
            msj = "La funcion main no tiene retorno"
            return self.error(tree.Regresa(),msj)
        elif self.dirFunciones[funcion]['tipoRet'] == "void":
            msj = "Retorno en funcion '{}' de tipo void".format(funcion)
            return self.error(tree.Regresa(),msj)
        self.expresion(tree.expresion(),funcion)
        #else mandar llamar expresion con el codigo
        # print(tree.expresion().getText())

    def est_lectura(self, tree,funcion):
        res = []
        self.lecturaAux(tree.lista_vars(),res,funcion)
        for var in res:
            self.pilaCuad.append(Cuadruplo('lee',var,0,0))
        # print(res)

    def lecturaAux(self,tree,res,funcion):
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                regla = self.rules[child.getRuleIndex()]
                if regla == "var":
                    nom = child.ID().getText()
                    if self.existeVar(nom,funcion):
                        res.append(nom)
                    else:
                        msj = "No se encontró la var '{}'".format(nom)
                        return self.error(child.ID(),msj)

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
                            tipo = self.regresaTipoVar(nombre,funcion)
                            # print(tipo)

                            if not tipo:
                                msj = "No se encontró la var '{}'".format(nombre)
                                return self.error(child.ID(),msj)

                            pila.append(nombre)
                            tipos.append(tipo)
                            # print("oila", pila)
                            # print("oila", tipos)
                        elif ruleChild == "expresion":
                            # print("exp")
                            self.expresion(child,funcion)

                #print("quad: = EXP", pila[-1])

                quad = "quad: = EXP " + pila[-1]
                self.pilaCuad.append(Cuadruplo('=','exp',pila[-1],0))

                if len(pila) > 1:
                    for i in range(len(pila) - 1):
                        var1 = pila.pop()
                        #print("quad: =", var1, pila[-1])
                        tipo1 = tipos.pop()
                        posible = cubo['='][tipo1][tipos[-1]]
                        if posible == 'OK':
                            self.pilaCuad.append(Cuadruplo('=',var1,pila[-1],0))
                        else:
                            msj = "Asignacion invalida {}({}) a {}({})".format(var1,tipo1,pila[-1],tipos[-1])
                            return self.error(child,msj)
                            # print("error, no se puede asignar tipos diferentes")
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

                            self.pilaCuad.append(Cuadruplo('gotof','var','pos',0))
                            pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            if primerBloque:
                                # print("Entonces: ")
                                self.evaluarBloqueEst(child,funcion)
                                #print("quad: goto pos")

                                self.pilaCuad.append(Cuadruplo('goto','pos',0,0))
                                pSaltos.append(len(self.pilaCuad))
                            else:
                                # print("Si no: ")
                                self.evaluarBloqueEst(child,funcion)
                                pSaltos.append(len(self.pilaCuad))

                            primerBloque = False

                            # print("exp")

                self.pilaCuad[pSaltos[0]-1] = Cuadruplo('gotof','var',pSaltos[1]+1,0)
                self.pilaCuad[pSaltos[1]-1] = Cuadruplo('goto',pSaltos[2]+1,0,0)
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

                            self.pilaCuad.append(Cuadruplo('gotof','var','pos',0))
                            pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            self.evaluarBloqueEst(child,funcion)
                            self.pilaCuad.append(Cuadruplo('goto','pos',0,0))
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
                self.pilaCuad[pSaltos[1]-1] = Cuadruplo('gotof','var',pSaltos[2]+1,0)
                self.pilaCuad[pSaltos[2]-1] = Cuadruplo('goto',pSaltos[0]+1,0,0)
                # self.pilaCuad[pSaltos[0]-1] = "quad: gotof varAnt " + str(pSaltos[1]+1)
                # self.pilaCuad[pSaltos[1]-1] = "quad: goto " + str(pSaltos[2]+1)
                # print(pSaltos)
                # print(pila)
                # print(tipos)

        else:
            pass

    def est_nocondicional(self, tree,funcion):
        # traverse(tree,self.rules)
        # print("es no condicional")
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "no_condicional":
                pSaltos = []
                var = ""
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "asignacion":
                            # print("Asignacion")
                            self.est_asignacion(child,funcion)
                            for child2 in child.children:
                                if not isinstance(child2, TerminalNodeImpl):
                                    if self.rules[child2.getRuleIndex()] == 'var':
                                        var = child2.getText()
                                        # print(child2.getText())
                            # traverse(child,self.rules)
                            # print(child.var())
                            # print(child.getText())
                            # pSaltos.append(len(self.pilaCuad))
                            # self.expresion(child,funcion)
                            # #print("quad: gotof varAnterior pos")
                            #
                            # quad = "quad: gotof varAnterior pos"
                            # self.pilaCuad.append(quad)
                            # pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "expresion":
                            # print("Expresion")
                            pSaltos.append(len(self.pilaCuad)+1)
                            self.expresion(child,funcion)
                            self.pilaCuad.append(Cuadruplo('>',var,"exp",0))
                            self.pilaCuad.append(Cuadruplo('gotov','final',0,0))
                            pSaltos.append(len(self.pilaCuad))
                            # quad = "quad: == EXP1 EXP2 " + var + " temp"
                            # self.pilaCuad.append(quad)
                            # print(child.getText())
                            # self.evaluarBloqueEst(child,funcion)
                            # quad = "quad: goto pos"
                            # self.pilaCuad.append(quad)
                            # pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            # print("Bloque est")
                            self.evaluarBloqueEst(child,funcion)
                            self.pilaCuad.append(Cuadruplo('+',1,var,"temp"))
                            self.pilaCuad.append(Cuadruplo('=','temp',var,0))
                            self.pilaCuad.append(Cuadruplo('goto','start',0,0))
                            pSaltos.append(len(self.pilaCuad))
                            # print(child.getText())

                self.pilaCuad[pSaltos[1]-1] = Cuadruplo('gotov','exp',pSaltos[2]+1,0)
                self.pilaCuad[pSaltos[2]-1] = Cuadruplo('goto',pSaltos[0],0,0)
                # print(pSaltos)

    ##falta
    #los params pueden ser exp
    #checar que sea valida la llamada
    #checar que los params sean compatibles
    def est_llamada_est(self,tree,funcion):
        nombreFun = tree.ID().getText()

        #Checa que exista y su inicio
        dirInicio = self.regresaInicioFun(nombreFun)
        if not dirInicio:
            msj = "No se encontró la funcion '{}'".format(nombreFun)
            return self.error(tree.ID(),msj)

        #Guarda el tipo de Retorno
        tipoRet = self.dirFunciones[nombreFun]['tipoRet']

        self.pilaCuad.append(Cuadruplo('era',nombreFun,0,0))
        self.resolverParams(tree.params_llamada(),nombreFun)
        self.pilaCuad.append(Cuadruplo('gosub',nombreFun,dirInicio,0))

        if tipoRet != "void":
            quad = "quad: = {} temp".format(nombreFun)
            self.pilaCuad.append(Cuadruplo('=',nombreFun,"temp",0))
        # print("llamada")
        # if funcion == "main":
        #     print("main")
        # else:
        #     print("no main")
        # print("Nombre fun:", funcion)
        # print("Params fun:", params.getText())
        # print("una llamada una funcion")
        # traverse(codigo,self.rules)
        # print(codigo.llamada_est().llamada().ID())
        # traverse(tree.llamada().params_llamada(),self.rules)
        # res = []

        # nombre = tree.ID().getText()
        # # print(nombre)
        # estatutos = self.dirFunciones[nombre]['main']
        # self.evaluarBloqueEst(estatutos,nombre)
        # print(estatutos)

    def resolverParams(self,tree,funcion,cont=0):
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                regla = self.rules[child.getRuleIndex()]
                if regla == "expresion":
                    self.expresion(child,funcion)
                    quad = "quad: param EXP param" + str(cont)
                    self.pilaCuad.append(Cuadruplo('param',"exp",cont,0))
                    cont += 1
                elif regla == "params_llamada":
                    self.resolverParams(child,funcion,cont)



    def est_escritura(self, tree,funcion):
        res = []
        str = ""
        self._extraePrint(tree,res,funcion)
        for index, item in enumerate(res):
            res[index] = res[index][1:-1]
            str += res[index] + " "
        #print("quad: print", str)

        self.pilaCuad.append(Cuadruplo('print',str,0,0))

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
    elif arch == '5':
        input_stream = FileStream("prueba5.txt")
    elif arch == '8':
        input_stream = FileStream("prueba8.txt")

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
