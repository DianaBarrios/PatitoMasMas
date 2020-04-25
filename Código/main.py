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
    }
}

class Programa:
    def __init__(self, tree, rules):
        self.tree = tree
        self.rules = rules
        self.varGlobales = {}
        self.dirFunciones = {}

    def error(self,tipo,mensaje):
        print(tipo,mensaje)

    def imprimeTodo(self):
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
        self.funciones(self.tree.dec_functions())
        # print(self.dirFunciones)
        pprint.pprint(self.dirFunciones)
        # print(self.existeVar("nice","fact"))
        # if not self.checaFun("fact",["int"]):
        #     print("no existe")
        # else:
        #     print("si existe")
        # print(self.checaParams("dos",["int","int"]))
        # print(self.regresaTipo("nice","fact"))
        # # funciones(programa.functions(),reglas)
        print("===== Main =====")
        self.evaluarFun(self.tree.principal().bloque_est(),"main")

        # evaluarFun(programa.principal().bloque_est().estatutos(),reglas)
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

    def params(self,tree,temp1,temp2):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                temp1.append(tree.tipo().getText())
                temp2.append(tree.ID().getText())

            for child in tree.children:
                self.params(child,temp1,temp2)
        else:
            pass

    #Funcion que actualiza el dir de funciones con los
    #datos de las funciones del programa
    def funciones(self, tree):
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
                self.params(tree.params(),arregloTipo,arregloNoms)

                jsontemp["vars"] = tempVar
                jsontemp["params"] = {"num": len(arregloTipo), "tipo": arregloTipo, "nombres": arregloNoms }
                jsontemp["tipoRet"] = ret
                jsontemp["main"] = tree.bloque_est().estatuto()
                # jsontemp["mainTexto"] = tree.bloque_est().estatuto().getText()

                self.dirFunciones[nombreFun] = jsontemp
                # pprint.pprint(jsontemp)
            else:
                for child in tree.children:
                        self.funciones(child)

            # elif rules[tree.getRuleIndex()] == "params":
            #     count = 0
            #     print(tree.getText())
            #     self.params(tree,{},count)
            #     print(count)
                # print("Tipo var: ", tree.tipo().getText())
                # print("Nombre var: ", tree.ID())


        else:
            pass

    def resolverLlamada(self,funcion,params):
        print("Nombre funcion: ", funcion)
        print("Params: ", params.getText())

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
        print("==== Final ====")
        print("Pila operandos:",pilas['pOperandos'])
        print("Pila tipos:",pilas['pTipos'])
        print("Pila operadores:",pilas['pOperadores'])

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
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    print("quad: ", op, left,right,res)

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
                                    elif tipoRes == "int":
                                        right = int(right)
                                        left = int(left)
                                    elif tipoRes == "float":
                                        right = float(right)
                                        left = float(left)
                                    # print("der: ",right,"izq:",left)
                                    res = self.genQuad(op,left,right)
                                    # print(res)
                                    print("quad: ", op, left,right,res)

                                    pilas['pOperandos'].append(str(res))
                                    pilas['pTipos'].append(tipoRes)

                                    print("= Pilas temporales =")
                                    print("Pila operandos:",pilas['pOperandos'])
                                    print("Pila tipos:",pilas['pTipos'])
                                    print("Pila operadores:",pilas['pOperadores'])
                                    # print(res)
                                    print("mayor a dos")
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
                                    print("quad: ", op, left,right,res)

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
                                print("quad: ", op, left,right,res)

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

    def helper(self,tree,funcion):
        # for child in tree.children:
        #     if not isinstance(child, TerminalNodeImpl):
        #         rule = self.rules[tree.getRuleIndex()]
        #         print("Rule: ", rule)
        #         # self.expresion2(child,funcion)
        #         # traverse(child,self.rules)
        #         print("No term: ", child.getText())
        if not isinstance(tree, TerminalNodeImpl):
            rule = self.rules[tree.getRuleIndex()]
            if rule == "llamada":
                self.resolverLlamada(tree.ID().getText(),tree.params_llamada())
            elif rule == "var":
                print("Var : " , tree.getText())
                tipo = self.regresaTipo(tree.ID().getText(),funcion)
                print("Tipo: ", tipo)
                # print("Llamada a : " , tree.ID().getText())
                # print(tree.params_llamada().getText())
                # traverse(tree,self.rules)
            elif rule == "var_cte":
                print("Const: ",tree.getText())
            else:
                for child in tree.children:
                    # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                    #     print("Estatuto: ", tree)
                    self.expresion(child,funcion)
        else:
            pass

    def evaluarFun(self, tree,funcion):
            if not isinstance(tree, TerminalNodeImpl):
                if self.rules[tree.getRuleIndex()] == "estatuto":
                    # print("Estatuto : ", tree.getText())
                    # print(rule_names[child.getRuleIndex()])
                    for child in tree.children:
                        regla = self.rules[child.getRuleIndex()]
                        if regla == "retorno":
                            print("*** Retorno ***")
                            self._retorno(tree.getText(),funcion)
                        elif regla == "lectura":
                            print("*** Lee ***")
                            self._lectura(tree.getText())
                        elif regla == "asignacion":
                            print("*** asignacion ***")
                            self._asignacion(tree,funcion)
                        elif regla == "decision":
                            print("*** Decision ***")
                            self._decision(tree.getText())
                        elif regla == "repeticion":
                            print("*** Repeticion ***")
                            self._repeticion(tree.getText())
                        elif regla == "llamada_est":
                            print("*** Llamada ***")
                            self._llamada_est(tree.llamada_est().llamada().ID().getText(),tree.llamada_est().llamada().params_llamada())
                        elif regla == "escritura":
                            print("*** Print ***")
                            self._escritura(tree.escritura(),funcion)
                        # print("Tipo Estatuto: ", rule_names[child.getRuleIndex()])
                        # estatutos(child, rule_names)
                    # traverse(tree,rule_names)
                    # print("Estatuto : ", rule_names[tree.getRuleIndex()])
                    # print("Funcion: ", tree.ID())
                    # # traverse(tree.params(),rule_names)
                    # print("Main de la funcion: ", tree.bloque_est().getText())
                    # tipo_ret = tree.tipo_ret()
                    # if tipo_ret.getText() == "void":
                    #     print("Tipo ret: void")
                    # else:
                    #     print("Tipo ret: ",tipo_ret.tipo().getText())
                # elif rule_names[tree.getRuleIndex()] == "params":
                #     print("Tipo var: ", tree.tipo().getText())
                #     print("Nombre var: ", tree.ID())
                for child in tree.children:
                    # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                    #     print("Estatuto: ", tree)
                    self.evaluarFun(child,funcion)
            else:
                pass
   

    def _retorno(self, codigo,funcion):
        if funcion == "main":
            return self.error("error: el main no tiene retorno","idk")
        if self.dirFunciones[funcion]['tipoRet'] == "void":
            return self.error("error:  la funcion es void","idk")
        #else mandar llamar expresion con el codigo
        print(codigo)

    def _lectura(self, codigo):
        print(codigo)

    def _asignacion(self, codigo,funcion):
        # traverse(codigo,self.rules)
        #chec var existe en funcion
        #llama al exp y asigna el valor

        print(codigo)

    def _decision(self, codigo):
        print(codigo)

    def _repeticion(self, codigo):
        print(codigo)

    ##falta
    #los params pueden ser exp
    #checar que sea valida la llamada
    #checar que los params sean compatibles
    def _llamada_est(self,funcion,params):
        print("Nombre fun:", funcion)
        print("Params fun:", params.getText())
        # print("una llamada una funcion")
        # traverse(codigo,self.rules)
        # print(codigo.llamada_est().llamada().ID())
        # nombre = codigo.llamada_est().llamada().ID().getText()
        # estatutos = self.dirFunciones[nombre]['main']
        # self.evaluarFun(estatutos,nombre)
        # print(estatutos)

    def _escritura(self, tree,funcion):
        res = []
        str = ""
        self._extraePrint(tree,res,funcion)
        for index, item in enumerate(res):
            res[index] = res[index][1:-1]
            str += res[index] + " "
        print("Estoy imprimiendo:", str)

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
                print("***** EXP *****")
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
    if sys.argv[1] == '1':
        input_stream = FileStream("prueba.txt")
    else:
        input_stream = FileStream("prueba2.txt")

    lexer = PatitoMasMasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoMasMasParser(stream)
    rutaInicio = parser.start().programa()

    # traverse(rutaInicio,parser.ruleNames)

    programa = Programa(rutaInicio,parser.ruleNames)
    programa.imprimeTodo()
    print(cubo['==']['int']['int'])

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
