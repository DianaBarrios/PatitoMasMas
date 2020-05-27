from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
from antlr4.error.ErrorListener import ErrorListener
import sys
import pprint

arithmeticCube = {
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

class Quadruple:
    def __init__(self,op,addr1,addr2,addr3):
         self.op = op
         self.addr1 = addr1
         self.addr2 = addr2
         self.addr3 = addr3
    def imprimir(self):
        str = "quad: {} {} {} {}".format(self.op,self.addr1,self.addr2,self.addr3)
        return str

class Program:
    def __init__(self, tree, rules):
        self.tree = tree
        self.rules = rules
        # self.varGlobales = {}
        self.dirFunciones = {}
        self.stackQuads = []
        self.pilaSaltos = []
        self.memory_limits = {
            'global': {'int': 5000, 'float': 8000, 'char': 10000, 'string': 13000, 'bool': 14000},
            'local': {'int': 15000, 'float': 18000, 'char': 20000, 'string': 23000, 'bool': 24000},
            'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000, 'dir': 50000,'dirArreglo':55000},
            'ctes': {'int': 35000, 'float': 38000, 'char': 41000, 'string': 43000, 'bool': 44000}
        }
        self.memory = {
            'temp': {},
            'ctes': {},
            'ctesDir': {}
        }
        self.ctesCounter = {}
        self.tempsCounter = {}
        self.temp = 0

    def error(self,tree,mensaje):
        line = tree.getSymbol().line
        column = tree.getSymbol().column
        print("Error linea-> {}:{} -> {}".format(line,column,mensaje))

    def execute(self):
        varGlobales = {}
        varGlobales2 = {}
        globalCounters = {}
        self.decVariables(self.tree.dec_variables(),varGlobales,varGlobales2,globalCounters,"",'global')
        self.dirFunciones['global'] = {'vars': varGlobales, 'counters': globalCounters, 'varsDir': varGlobales2}
        self.stackQuads.append(Quadruple('goto','global',0,0))
        self.decFunciones(self.tree.dec_functions())

        self.pilaSaltos.append(len(self.stackQuads)+1)
        self.dirFunciones['global']['empieza'] = len(self.stackQuads)+1
        self.evaluarBloqueEst(self.tree.principal().bloque_est(),'global')
        #self.temp = 0
        self.tempsCounter = {}
        self.stackQuads.append(Quadruple('end',0,0,0))
        self.stackQuads[0] = Quadruple('goto',self.dirFunciones['global']['empieza'],0,0)

    def printAll(self):
        self.execute()

        #Imprime cuadruplos
        print("===== Cuadruplos =====")
        for i in range(len(self.stackQuads)):
            print(i+1, ".-",self.stackQuads[i].imprimir())

        #Imprime el directorio de funciones
        print("===== Dir Funciones =====")
        pprint.pprint(self.dirFunciones)

        for k in self.dirFunciones.keys():
            self.memory[k] = self.dirFunciones[k]['vars']

        #Imprime memoria
        print("===== Memory =====")
        pprint.pprint(self.memory)

    ##### VERIFICACIONES
    def checksDuplicateVar(self,var):
        # return True
        for func in self.dirFunciones:
            for var_actual in self.dirFunciones[func]['vars']:
                if var == var_actual:
                    return True

    def checksFunctionExists(self,function):
        if self.dirFunciones.get(function, None) == None:
            return False
        return True

    def checksVariableExists(self,var,function):
        if var in self.dirFunciones['global']['vars']:
            return True
        else:
            if var in self.dirFunciones[function]['vars']:
                return True

        return False

    ##### GETS
    def getQuads(self):
        return self.stackQuads

    def getConstants(self):
        return self.memory['ctesDir']

    def getDimOfAddr(self,var,function,dim):
        res = self.dirFunciones['global']['varsDir'].get(var, None)
        if res != None:
            # print("global")
            checaDim = self.dirFunciones['global']['varsDir'][var].get("{}{}".format("dim",dim), None)
            if checaDim != None:
                return self.dirFunciones['global']['varsDir'][var]["{}{}".format("dim",dim)]
            else:
                return False
        if function != "global":
            if res == None:
                res = self.dirFunciones[function]['varsDir'].get(var, None)
                if res == None:
                    return False
                else:
                    checaDim = self.dirFunciones[function]['varsDir'][var].get("{}{}".format("dim",dim), None)
                    if checaDim != None:
                        return self.dirFunciones[function]['varsDir'][var]["{}{}".format("dim",dim)]
                    else:
                        return False
            else:
                return False
        return False

    #Funcion que regresa el tipo de una variable
    def getTypeOfVariable(self,var,function):
        if self.checksVariableExists(var,function):
            res = self.dirFunciones['global']['vars'].get(var, None)
            if res != None:
                return self.dirFunciones['global']['vars'][var]['tipo']
            if function != "global":
                if res == None:
                    res = self.dirFunciones[function]['vars'].get(var, None)
                    if res == None:
                        return False
                    else:
                        return self.dirFunciones[function]['vars'][var]['tipo']
                else:
                    return False
        else:
            return False

    #Funcion que regresa tipo con base en la direccion
    def getTypeOfAddr(self,addr):
        if addr >= 50000:
            return 'int'
        while(addr > 14999):
            addr = addr - 10000
        if addr >= 5000 and addr < 8000:
            return 'int'
        elif addr >= 8000 and addr < 10000:
            return 'float'
        elif addr >= 10000 and addr < 13000:
            return 'char'
        elif addr >= 13000 and addr < 14000:
            return 'string'
        elif addr >= 14000 and addr < 15000:
            return 'bool'

    def getInitialAddrFunction(self,function):
        if self.checksFunctionExists(function):
            return self.dirFunciones[function]['empieza']
        else:
            return False

    def getAddrOfVariable(self, nombre, scope):
        if nombre in self.dirFunciones[scope]['vars']:
            return self.dirFunciones[scope]['vars'][nombre]['dir']
        else:
            return self.dirFunciones['global']['vars'][nombre]['dir']

    def getNameOfAddr(self, addr, scope):
        if addr in self.dirFunciones[scope]['varsDir']:
            return self.dirFunciones[scope]['varsDir'][addr]['nombre']
        else:
            return self.dirFunciones['global']['varsDir'][addr]['nombre']

    ##### HELPERS
    #Funcion que te da la siguiente direccion
    def nextRelativeAddr(self,local_counters,type,increment=1):
        if increment != 1:
            if type in local_counters:
                aux = local_counters[type]
                local_counters[type] += increment
                return aux
            else:
                local_counters[type] = increment
                return 0
        else:
            if type in local_counters:
                local_counters[type] += 1
            else:
                local_counters[type] = 0
        return local_counters[type]

    def solveParams(self,tree,targetFunction,callingFunction,counter=0):
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                rule = self.rules[child.getRuleIndex()]
                if rule == "expresion":
                    exp = self.expresion(child,targetFunction)
                    addr = self.dirFunciones[callingFunction]['paramsDir'][counter]
                    self.stackQuads.append(Quadruple('param',exp,addr,0))
                    counter += 1
                elif rule == "params_llamada":
                    self.solveParams(child,targetFunction,callingFunction,counter)

    def lecturaAux(self,tree,res,function):
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                regla = self.rules[child.getRuleIndex()]
                if regla == "var":
                    nom = child.ID().getText()
                    if self.checksVariableExists(nom,function):
                        addr = self.getAddrOfVariable(nom,function)
                        res.append(addr)
                    else:
                        msg = "No se encontró la var '{}'".format(nom)
                        return self.error(child.ID(),msg)
                    # print(child.ID().getText())
                elif regla == "lista_vars":
                    self.lecturaAux(child,res,function)
                    # traverse(child,self.rules)
                # print(regla)

    ##### PARSE VARS Y FUNCIONES
    #Funcion que regresa el JSON con la info de las vars
    def decVariables(self,tree,temp,temp2,local_counters,tipo,function):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "dec_var":
                tipo = tree.tipo().getText()

            elif self.rules[tree.getRuleIndex()] == "ids":
                elem = tree.getText()

                if elem in temp:
                    msg = "Var '{}' duplicada".format(elem)
                    return self.error(tree.ID(),msg)

                if function != 'global':
                    scope = 'local'
                    if self.checksDuplicateVar(elem):
                        msg = "Var '{}' duplicada".format(elem)
                        return self.error(tree.ID(),msg)
                else:
                    scope = 'global'

                # print(tree.getText())
                # traverse(tree,self.rules)
                offset = self.memory_limits[scope][tipo]

                if elem.find('[') == -1:
                    addr = self.nextRelativeAddr(local_counters,tipo) + offset
                    temp[elem] = {'tipo': tipo, 'dir': addr}
                    temp2[addr] = {'nombre':elem}
                else:
                    count = elem.count("[")
                    if count == 1:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        nombre = elem[:indexInicio]
                        dim = int(elem[indexInicio+1:indexFinal])
                        addr = self.nextRelativeAddr(local_counters,tipo,dim) + offset
                        temp[nombre] = {'tipo': tipo,'dim1': dim, 'dir': addr}
                        temp2[addr] = {'nombre':nombre,'dim1': dim}
                    if count == 2:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        indexInicio2 = elem.find("[", indexInicio + 1)
                        indexFinal2 = elem.find("]", indexFinal + 1)
                        nombre = elem[:indexInicio]
                        dim = int(elem[indexInicio+1:indexFinal])
                        dim2 = int(elem[indexInicio2+1:indexFinal2])
                        dims = dim * dim2
                        addr = self.nextRelativeAddr(local_counters,tipo,dims) + offset
                        temp[nombre] = {'tipo': tipo,'dim1': dim,'dim2':dim2, 'dir': addr}
                        temp2[addr] = {'nombre':nombre,'dim1': dim,'dim2':dim2}
            else:
                pass
            for child in tree.children:
                self.decVariables(child,temp,temp2,local_counters,tipo,function)

    #Funcion que actualiza el dir de decFunciones con los
    #datos de las decFunciones del programa
    def decFunciones(self, tree):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "funcion":
                functionName = tree.ID().getText()
                if(self.checksFunctionExists(functionName)):
                    msg = "Ya existe una function definida con el mismo nombre '{}'".format(functionName)
                    return self.error(tree.ID(),msg)
                else:
                    jsontemp = {}
                    tipo_ret = tree.tipo_ret()

                    if tipo_ret.getText() == "void":
                        returnType = "void"
                    else:
                        returnType = tipo_ret.tipo().getText()
                        globalCounters = self.dirFunciones['global']['counters']
                        offset = self.memory_limits['global'][returnType]
                        addr = self.nextRelativeAddr(globalCounters,returnType) + offset
                        self.dirFunciones['global']['vars'][functionName] = {'tipo' : returnType, 'dir': addr}

                    tablaParams = []
                    tablaDirs = []
                    varsParams = {}
                    #tempVar = {}
                    tempVar2 = {}

                    #Local counter of types of vars and params
                    localCounters = {}

                    self.decParamsFun(tree.params(),varsParams,tablaParams,tablaDirs,functionName,localCounters)
                    self.decVariables(tree.dec_variables(),varsParams,tempVar2,localCounters,"",functionName)
                    #self.decVariables(tree.dec_variables(),tempVar,tempVar2,localCounters,"",functionName)

                    varsFunc = varsParams
                    #varsFunc = dict(list(varsParams.items()) + list(tempVar.items()))

                    cuadEmpieza = len(self.stackQuads) + 1
                    jsontemp["params"] = tablaParams
                    jsontemp["paramsDir"] = tablaDirs
                    jsontemp["vars"] = varsFunc
                    jsontemp["varsDir"] = tempVar2
                    jsontemp["tipoRet"] = returnType
                    jsontemp["empieza"] = cuadEmpieza
                    jsontemp["counters"] = localCounters
                    self.dirFunciones[functionName] = jsontemp
                    self.evaluarBloqueEst(tree.bloque_est(),functionName)
                    self.dirFunciones[functionName]['tempsCounters'] = self.tempsCounter
                    self.tempsCounter = {}
                    #self.temp = 0
                    self.stackQuads.append(Quadruple('endproc',0,0,0))
            else:
                for child in tree.children:
                        self.decFunciones(child)
        else:
            pass

    def decParamsFun(self,tree,varsParams,tablaParams,tablaDirs,function,local_counters):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                varName = tree.ID().getText()

                if varName in varsParams or self.checksDuplicateVar(varName):
                    msg = "Var '{}' duplicada".format(varName)
                    return self.error(tree.ID(),msg)

                varType = tree.tipo().getText()
                tablaParams.append(varType)
                offset = self.memory_limits['local'][varType]
                varAddr = self.nextRelativeAddr(local_counters,varType) + offset
                tablaDirs.append(varAddr)
                #self.dirFunciones[functionName]['vars'][nombre] = {'tipo': tipo, 'dir': addr}
                varsParams[varName] = {'tipo': varType, 'dir': varAddr}

            for child in tree.children:
                self.decParamsFun(child,varsParams,tablaParams,tablaDirs,function,local_counters)
        else:
            pass

    #### EXPRESION

    def expresion(self,tree,function):
        stacks = {
            'pOperandos' : [],
            'pOperadores' : [],
            'pTipos' : [],
            'pDim': [],
            'pNegativos': []
        }
        self.expresionAux(tree,function,stacks)
        #print("function calling",function)
        #print("stacks",stacks)
        return stacks['pOperandos'][0]

    def expresionAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("expresion")
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child,function,stacks)
                        if stacks['pOperadores']:
                            op = stacks['pOperadores'][-1]
                            if op == '<' or op == '>' or op == '==' or op == '!=':
                                if len(stacks['pOperandos']) > 1:

                                    stacks['pOperadores'].pop()

                                    right = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()
                                    left = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()
                                    resultType = arithmeticCube[op][rightType][leftType]
                                    # print("tipo res:", resultType)
                                    if resultType == "x":
                                        print("Operacion no valida")


                                    # print("der: ",right,"izq:",left)
                                    # res = self.genQuad(op,left,right)
                                    offset = self.memory_limits['temp'][resultType]
                                    addr = self.nextRelativeAddr(self.tempsCounter,resultType) + offset

                                    #res = self.temp
                                    #self.temp += 1
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    self.stackQuads.append(Quadruple(op,left,right,addr))


                                    stacks['pOperandos'].append(addr)

                                    stacks['pTipos'].append(resultType)

                                else:
                                    pass

                            else:
                                pass
                    elif ruleChild == "op_log":
                        op = child.getText()
                        stacks['pOperadores'].append(op)
                    elif ruleChild == "op_comp":
                        op = child.getText()
                        stacks['pOperadores'].append(op)
                    elif ruleChild == "expresion":
                        self.expresionAux(child,function,stacks)
                        if stacks['pOperadores']:
                            op = stacks['pOperadores'][-1]
                            if op == '||' or op == '&':
                                if len(stacks['pOperandos']) > 1:

                                    stacks['pOperadores'].pop()

                                    right = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()
                                    left = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()
                                    resultType = arithmeticCube[op][rightType][leftType]

                                    if resultType == "x":
                                        print("Operacion no valida")

                                    """
                                    if right == "True":
                                        right = True
                                    elif right == "False":
                                        right = False

                                    if left == "True":
                                        left = True
                                    elif left == "False":
                                        left = False
                                    """
                                    # print("der: ",right,"izq:",left)
                                    #res = self.genQuad(op,left,right)

                                    #res = self.temp
                                    #self.temp += 1
                                    offset = self.memory_limits['temp'][resultType]
                                    addr = self.nextRelativeAddr(self.tempsCounter,resultType) + offset

                                    self.stackQuads.append(Quadruple(op,left,right,addr))

                                    stacks['pOperandos'].append(addr)
                                    stacks['pTipos'].append(resultType)

                                else:
                                    pass

                            else:
                                pass
        else:
            pass

    def expAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "exp":
                # print("exp")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child,function,stacks)
                    elif ruleChild == "op_arit":
                        op = child.getText()
                        stacks['pOperadores'].append(op)
                        # print("encontre + o -")
                    elif ruleChild == "term":
                        self.termAux(child,function,stacks)

                        if stacks['pOperadores']:
                            op = stacks['pOperadores'][-1]
                            if op == '+' or op == '-':
                                if len(stacks['pOperandos']) > 1:

                                    stacks['pOperadores'].pop()

                                    right = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()
                                    left = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()
                                    resultType = arithmeticCube[op][rightType][leftType]
                                    if resultType == "x":
                                        print("Operacion no valida")

                                    dim1Left = self.getDimOfAddr(left,function,1)
                                    dim2Left = self.getDimOfAddr(left,function,2)
                                    dim1Right = self.getDimOfAddr(right,function,1)
                                    dim2Right = self.getDimOfAddr(right,function,2)
                                    if dim1Left != False and dim1Left == dim1Right and dim2Left == dim2Right or left >= 55000:
                                        offset = self.memory_limits['temp']['dirArreglo']
                                        addr = self.nextRelativeAddr(self.ctesCounter,'dir') + offset
                                        opAct = "{}Arreglos".format(op)
                                        self.stackQuads.append(Quadruple(opAct,left,right,addr))
                                        self.stackQuads.append(Quadruple('dimensiones',0,dim1Right,dim2Right))
                                    else:
                                        offset = self.memory_limits['temp'][resultType]
                                        addr = self.nextRelativeAddr(self.tempsCounter,resultType) + offset
                                        self.stackQuads.append(Quadruple(op,left,right,addr))


                                    stacks['pOperandos'].append(addr)
                                    stacks['pTipos'].append(resultType)
                                    # print("pilitas",stacks['pTipos'])

                                else:
                                    pass

                            else:
                                pass

        else:
            pass

    def termAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "term":
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "factor":
                        self.factorAux(child,function,stacks)

                        if stacks['pOperadores'] and len(stacks['pOperandos']) > 1:
                            op = stacks['pOperadores'][-1]
                            if op == '*' or op == '/':
                                stacks['pOperadores'].pop()
                                right = stacks['pOperandos'].pop()
                                rightType = stacks['pTipos'].pop()
                                left = stacks['pOperandos'].pop()
                                leftType = stacks['pTipos'].pop()
                                resultType = arithmeticCube[op][rightType][leftType]
                                if resultType == "x":
                                    print("Operacion no valida")
                                # print("der: ",right,"izq:",left)
                                #res = self.genQuad(op,left,right)
                                #res = self.temp
                                #self.temp += 1
                                dim1Left = self.getDimOfAddr(left,function,1)
                                dim2Left = self.getDimOfAddr(left,function,2)
                                dim1Right = self.getDimOfAddr(right,function,1)
                                dim2Right = self.getDimOfAddr(right,function,2)
                                if dim1Left != False and dim1Left == dim1Right and dim2Left == dim2Right or left >= 55000:
                                    offset = self.memory_limits['temp']['dirArreglo']
                                    addr = self.nextRelativeAddr(self.ctesCounter,'dir') + offset
                                    opAct = "{}Arreglos".format(op)
                                    self.stackQuads.append(Quadruple(opAct,left,right,addr))
                                    self.stackQuads.append(Quadruple('dimensiones',0,dim1Right,dim2Right))
                                else:
                                    offset = self.memory_limits['temp'][resultType]
                                    addr = self.nextRelativeAddr(self.tempsCounter,resultType) + offset
                                    self.stackQuads.append(Quadruple(op,left,right,addr))

                                stacks['pOperandos'].append(addr)
                                stacks['pTipos'].append(resultType)
                                # print("pila",stacks['pTipos'])
                                    # print(res)
                                    # print("mayor a dos"
                            else:
                                pass
                    elif ruleChild == "op_prod":
                        op = child.getText()
                        stacks['pOperadores'].append(op)
                    elif ruleChild == "term":
                        self.termAux(child,function,stacks)
        else:
            pass

    def factorAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "factor":
                # print("factor")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "var":
                        # print("si se llamo")
                        self.varAux(child,function,stacks)
                        # self.factorAux(child,function,stacks)
                    elif ruleChild == "var_cte":
                        # print("lo hago despues")
                        self.varcteAux(child,function,stacks)
                    elif ruleChild == "op_esp":
                        # print("encontre $ ? ¡")
                        # print(stacks['pOperadores'])
                        op = child.getText()
                        addr = stacks['pOperandos'][-1]

                        dim1 = self.getDimOfAddr(addr,function,1)
                        dim2 = self.getDimOfAddr(addr,function,2)

                        if op == '?':
                            operacion = "inversa"
                        elif op == '$':
                            operacion = "determinante"
                        elif op == '%':
                            operacion = "promedio"
                        elif op == '@':
                            operacion = "suma"
                        elif op == '~':
                            operacion = "minimo"
                        elif op == '#':
                            operacion = "maximo"
                        else:
                            operacion = "transpuesta"
                        if op != '!' or op != '?':
                            tipo = stacks['pTipos'][-1]
                            offset = self.memory_limits['temp'][tipo]
                            addr1 = self.nextRelativeAddr(self.ctesCounter,tipo) + offset
                            self.stackQuads.append(Quadruple(op,addr,0,addr1))

                            # print("que hay adentro",stacks['pOperandos'])
                        else:
                            offset = self.memory_limits['temp']['dirArreglo']
                            addr1 = self.nextRelativeAddr(self.ctesCounter,'dir') + offset
                            self.stackQuads.append(Quadruple(op,addr,0,addr1))
                        stacks['pOperandos'].pop()
                        stacks['pOperandos'].append(addr1)
                        if op == '?' or op == '$':
                            if dim1 != dim2:
                                msg = "No se puede calcular la {} si no es cuadrada".format(operacion)
                                return self.error(child.ESP(),msg)

                        self.stackQuads.append(Quadruple('dimensiones',0,dim1,dim2))
                    elif ruleChild == "op_arit":
                        # print("encontre + -")
                        # traverse(child,self.rules)
                        stacks['pNegativos'].append(child.getText())
                        # print("stacks", stacks['pNegativos'])
                        # self.varcteAux(child.var_cte(),function,stacks)
                        # print("no se va a regresar")

                    elif ruleChild == "exp_par":
                        # print("encontre algo con parentesis")
                        self.parentesisAux(child,function,stacks)
                    elif ruleChild == "llamada":
                        self.est_llamada_est(child,function,stacks)
                        # self.termAux(child,function,stacks)
        else:
            pass

    def parentesisAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "exp_par":
                # print("exp_par")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "par_empieza":
                        stacks['pOperadores'].append('$')
                        # print("meti el par")
                    elif ruleChild == "par_termina":
                        if stacks['pOperadores'][-1] == '$':
                            stacks['pOperadores'].pop()
                            # print("saque el par")
                    elif ruleChild == "expresion":
                        self.expresionAux(child,function,stacks)
        else:
            pass

    def varAux(self,tree,function,stacks,brackets=False):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var":
                nomVar = tree.ID().getText()
                # print("Var : " , nomVar)
                #print("function::",function)
                tipo = self.getTypeOfVariable(nomVar,function)

                #print("var aux: nombre, tipo: ",nomVar,tipo)

                if tipo == False:
                    msg = "No se encontró la var '{}'".format(nomVar)
                    return self.error(tree.ID(),msg)

                stacks['pTipos'].append(tipo)
                addr = self.getAddrOfVariable(nomVar,function)
                tieneDim = self.getDimOfAddr(addr,function,1)
                # print(addr)
                # print(addr)
                stacks['pOperandos'].append(addr)

                # dims = []
                # numdims = len(tree.children) -1
                # print(numdims)
                if tieneDim != False:
                    id = ""
                    type = ""
                    dim = 1
                    for child in tree.children:
                        if not isinstance(child, TerminalNodeImpl):
                            ruleChild = self.rules[child.getRuleIndex()]
                            # rules.append(ruleChild)
                            if ruleChild == "dim":
                                brackets = True
                                if dim == 1:
                                    id = stacks['pOperandos'].pop()
                                    type = stacks['pTipos'].pop()
                                    # print("pila",stacks['pOperandos'])
                                    stacks['pOperadores'].append("$")
                                self.dimAux(child,function,dim,stacks,id,type)
                                dim+=1
        else:
            pass

    def dimAux(self,tree,function,dim,stacks,id,type):
        stacks2 = {
            'pOperandos' : [],
            'pOperadores' : [],
            'pTipos' : [],
            'pDim': [],
            'pNegativos': []
        }
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                ruleChild = self.rules[child.getRuleIndex()]
                # rules.append(ruleChild)
                if ruleChild == "expresion":
                    # print(stacks2['pOperandos'])
                    self.expresionAux(child,function,stacks2)

        if dim == 1:
            resExp = stacks2['pOperandos'][-1]
            lsdim1 = self.getDimOfAddr(id,function,1)
            lsdim2 = self.getDimOfAddr(id,function,2)

            self.stackQuads.append(Quadruple('verify',resExp,0,lsdim1))

            if lsdim2 == False:
                if id in self.memory['ctes']:
                    baseAddr = self.memory['ctes'][id]['dir']
                else:
                    offset = self.memory_limits['ctes']['int']
                    baseAddr = self.nextRelativeAddr(self.ctesCounter,'int') + offset
                    self.memory['ctes'][id] = {'tipo': 'int', 'dir': baseAddr}
                    self.memory['ctesDir'][baseAddr] = id
                offset = self.memory_limits['temp']['dir']
                addr = self.nextRelativeAddr(self.ctesCounter,'dir') + offset
                self.stackQuads.append(Quadruple('+',resExp,baseAddr,addr))
                stacks['pOperandos'].append(addr)
                stacks['pTipos'].append(type)
                stacks['pOperadores'].pop()
            else:
                if lsdim2 in self.memory['ctes']:
                    lsdim2addr = self.memory['ctes'][lsdim2]['dir']
                else:
                    offset = self.memory_limits['ctes']['int']
                    lsdim2addr = self.nextRelativeAddr(self.ctesCounter,'int') + offset
                    self.memory['ctes'][lsdim2] = {'tipo': 'int', 'dir': lsdim2addr}
                    self.memory['ctesDir'][lsdim2addr] = lsdim2
                offset = self.memory_limits['temp']['int']
                addr = self.nextRelativeAddr(self.ctesCounter,'int') + offset
                self.stackQuads.append(Quadruple('*',resExp,lsdim2addr,addr))
                stacks['pDim'].append(addr)
                # print(stacks['pDim'])
        elif dim == 2:
            resExp = stacks2['pOperandos'][-1]
            lsdim2 = self.getDimOfAddr(id,function,2)
            # print("dim",id, self.getDimOfAddr(5000,function,2))
            # print(stacks['pDim'])
            temp1 = stacks['pDim'].pop()
            self.stackQuads.append(Quadruple('verify',resExp,0,lsdim2))

            offset = self.memory_limits['temp']['int']
            addr1 = self.nextRelativeAddr(self.ctesCounter,'int') + offset
            self.stackQuads.append(Quadruple('+',resExp,temp1,addr1))

            if id in self.memory['ctes']:
                baseAddr = self.memory['ctes'][id]['dir']
            else:
                offset = self.memory_limits['ctes']['int']
                baseAddr = self.nextRelativeAddr(self.ctesCounter,'int') + offset
                self.memory['ctes'][id] = {'tipo': 'int', 'dir': baseAddr}
                self.memory['ctesDir'][baseAddr] = id
            offset = self.memory_limits['temp']['dir']
            addr2 = self.nextRelativeAddr(self.ctesCounter,'dir') + offset
            self.stackQuads.append(Quadruple('+',addr1,baseAddr,addr2))

            stacks['pOperandos'].append(addr2)
            stacks['pTipos'].append(type)
            # print("addr2",addr2,stacks['pOperandos'])
            stacks['pOperadores'].pop()

        # traverse(tree,self.rules)

    def varcteAux(self,tree,function,stacks):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var_cte":
                for child in tree.children:
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "var":
                            self.varAux(child,function,stacks)
                    else:
                        if stacks['pNegativos']:
                            operador = stacks['pNegativos'].pop()
                            cte = operador + tree.getText()
                        else:
                            cte = tree.getText()
                        if cte.find('.') != -1:
                            tipo = "float"
                        elif cte.find("''") != -1:
                            tipo = "char"
                            cte = cte.replace("'","")
                        else:
                            tipo = "int"

                        if cte in self.memory['ctes']:
                            addr = self.memory['ctes'][cte]['dir']
                        else:
                            offset = self.memory_limits['ctes'][tipo]
                            addr = self.nextRelativeAddr(self.ctesCounter,tipo) + offset
                            self.memory['ctes'][cte] = {'tipo': tipo, 'dir': addr}
                            self.memory['ctesDir'][addr] = cte

                        stacks['pTipos'].append(tipo)
                        #diana
                        stacks['pOperandos'].append(addr)

        else:
            pass

    #### ESTATUTOS

    def evaluarBloqueEst(self, tree, function):
        # print("entre")
        if not isinstance(tree, TerminalNodeImpl):
            for child in tree.children:
                if not isinstance(child, TerminalNodeImpl):
                    if self.rules[child.getRuleIndex()] == "estatuto":
                        for child2 in child.children:
                            rule = self.rules[child2.getRuleIndex()]
                            if rule == "retorno":
                                # self.error(tree,"hola")
                                # print("*** Retorno ***")
                                self.est_retorno(child2,function)
                            elif rule == "lectura":
                                # print("*** Lee ***")
                                self.est_lectura(child2,function)
                            elif rule == "asignacion_est":
                                # print("*** asignacion ***")
                                self.est_asignacion(child2.asignacion(),function)
                            elif rule == "decision":
                                # print("*** Decision ***")
                                self.est_decision(child2,function)
                            elif rule == "repeticion":
                                # print("*** Repeticion ***")
                                self.est_repeticion(child2,function)
                            elif rule == "llamada_est":
                                # print("*** Llamada ***")
                                self.est_llamada_est(child2.llamada(),function)
                            elif rule == "escritura":
                                # print("*** Print ***")
                                self.est_escritura(child2,function)

        else:
            pass

    def est_retorno(self, tree, function):
        if function == "global":
            msg = "La function main no tiene retorno"
            return self.error(tree.Regresa(),msg)
        elif self.dirFunciones[function]['tipoRet'] == "void":
            msg = "Retorno en function '{}' de tipo void".format(function)
            return self.error(tree.Regresa(),msg)


        addrExp = self.expresion(tree.expresion(),function)
        addrVar = self.getAddrOfVariable(function,'global')

        self.stackQuads.append(Quadruple('ret',addrExp,addrVar,0))

    def est_lectura(self,tree,function):
        res = []
        self.lecturaAux(tree.lista_vars(),res,function)
        #print("Res in est lectura:",res)
        for var in res:
            self.stackQuads.append(Quadruple('lee',var,0,0))
        # print(res)

    def est_asignacion(self, tree, function):
          # traverse(tree,self.rules)
          # print(len(tree.children))
          # print(tree.getText())
          if not isinstance(tree, TerminalNodeImpl):
              if self.rules[tree.getRuleIndex()] == "asignacion":
                  # print("asign")
                  stacks = {
                      'pOperandos' : [],
                      'pOperadores' : [],
                      'pTipos' : [],
                      'pDim': [],
                      'tieneBrackets' : [],
                      'pNegativos': []
                  }
                  for child in tree.children:
                      # print("hijo")
                      if not isinstance(child, TerminalNodeImpl):
                          ruleChild = self.rules[child.getRuleIndex()]
                          # rules.append(ruleChild)
                          if ruleChild == "var":
                              varName = child.ID().getText()
                              varType = self.getTypeOfVariable(varName,function)
                              varAddr = self.getAddrOfVariable(varName,function)

                              if not varType:
                                  msg = "No se encontró la var '{}'".format(varName)
                                  return self.error(child.ID(),msg)

                              brackets = False
                              dim1 = self.getDimOfAddr(varAddr,function,1)
                              if dim1 != False:
                                  currentDim = 1
                                  for child2 in child.children:
                                      if not isinstance(child2, TerminalNodeImpl):
                                          ruleChild = self.rules[child2.getRuleIndex()]
                                          # rules.append(ruleChild)
                                          if ruleChild == "currentDim":
                                              if currentDim == 1:
                                                  brackets = True
                                                  stacks['tieneBrackets'].append(True)
                                                  stacks['pOperandos'].append(varAddr)
                                                  stacks['pTipos'].append(varType)
                                                  stacks['pOperadores'].append("$")
                                              self.dimAux(child2,function,currentDim,stacks,varAddr,varType)
                                              currentDim+=1

                              #stacks['pOperandos'].append(varName)
                              # if function == "main":
                              #     function = "global"
                              c = child.ID()
                              if len(stacks['pOperandos']) > 1:
                                  tipo_anterior = stacks['pTipos'][-1]
                                  if varType != tipo_anterior:
                                      msg = "Asignacion invalida {}({}) a {}({})".format(varAddr,varType,stacks['pOperandos'][-1],stacks['pTipos'][-1])
                                      return self.error(c,msg)
                              if dim1 == False or brackets == False:
                                  stacks['tieneBrackets'].append(False)
                                  stacks['pOperandos'].append(varAddr)
                                  stacks['pTipos'].append(varType)

                              # print("oila", stacks['pOperandos'])
                              # print("oila", stacks['pTipos'])
                          elif ruleChild == "expresion":
                              # print("exp")
                              exp = self.expresion(child,function)
                              tipo_exp = self.getTypeOfAddr(exp)
                              # print(exp,tipo_exp)

                              topTipos = stacks['pTipos'][-1]
                              topOperandos = stacks['pOperandos'][-1]
                              if tipo_exp != topTipos:
                                  msg = "Asignacion invalida {}({}) a {}({})".format(exp,tipo_exp,topOperandos,topTipos)
                                  #print("error", msg)
                                  #print("child:",child)
                                  return self.error(c,msg)



                  ####AGREGAR ALGO PARA SABER SI ADDR Y EXP TENIAN [][] O NO
                  addrIzq = stacks['pOperandos'][-1]
                  bracketsIzq = stacks['tieneBrackets'].pop()
                  dim1Left = self.getDimOfAddr(varAddr,function,1)
                  dim2Left = self.getDimOfAddr(varAddr,function,2)
                  dim1Right = self.getDimOfAddr(exp,function,1)
                  dim2Right = self.getDimOfAddr(exp,function,2)
                  # print("en",addrIzq,exp,dim1Right,dim2Right)

                  if bracketsIzq:
                      self.stackQuads.append(Quadruple('=',exp,addrIzq,'arrSingle'))
                      stacks['pOperandos'].pop()
                  else:
                      if exp >= 50000 and dim1Left != False:
                          self.stackQuads.append(Quadruple('=',exp,addrIzq,'arreglo'))
                          self.stackQuads.append(Quadruple('dimensiones',0,dim1Left,dim2Left))
                          # print("si entre")
                      else:
                          # nom1 = self.getNameOfAddr(varAddr,function)
                          # # nom2 = self.getNameOfAddr(exp,function)
                          # msg = "No se puede asignar un valor a todo el arreglo '{}'".format(nom1)
                          # return self.error(c,msg)
                      # print("si son iguales")
                      # print("izq:",dim1Left,dim2Left)
                      # print("der:",dim1Right,dim2Right)
                          if dim1Left != False and dim1Right != False:
                              if (dim1Left == dim1Right) and (dim2Left == dim2Right):
                                  self.stackQuads.append(Quadruple('=',exp,addrIzq,'arreglo'))
                                  self.stackQuads.append(Quadruple('dimensiones',0,dim1Left,dim2Left))
                              else:
                                  nom1 = self.getNameOfAddr(varAddr,function)
                                  nom2 = self.getNameOfAddr(exp,function)
                                  msg = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(nom1,nom2)
                                  # print(msg)
                                  return self.error(c,msg)
                          else:
                              self.stackQuads.append(Quadruple('=',exp,addrIzq,0))
                  lenPila = len(stacks['pOperandos'])
                  if lenPila > 1:
                      for i in range(lenPila-1):
                          addrIzq = stacks['pOperandos'].pop()
                          dim1Left = self.getDimOfAddr(addrIzq,function,1)
                          dim2Left = self.getDimOfAddr(addrIzq,function,2)

                          addrDer = stacks['pOperandos'][-1]
                          dim1Right = self.getDimOfAddr(addrDer,function,1)
                          dim2Right = self.getDimOfAddr(addrDer,function,2)

                          if dim1Left != False and dim1Right != False:
                              if (dim1Left == dim1Right) and (dim2Left == dim2Right):
                                  self.stackQuads.append(Quadruple('=',addrIzq,addrDer,'arreglo'))
                                  self.stackQuads.append(Quadruple('dimensiones',0,dim1Left,dim2Left))
                              else:
                                  nom1 = self.getNameOfAddr(addrIzq,function)
                                  nom2 = self.getNameOfAddr(addrDer,function)
                                  msg = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(nom1,nom2)
                                  # print(msg)
                                  return self.error(c,msg)
                          else:
                              self.stackQuads.append(Quadruple('=',addrIzq,addrDer,0))
                  # print(stacks['pTipos'])


                  #self.stackQuads.append(Quadruple('=',exp,str(stacks['pOperandos'][-1]),0))
          else:
              pass
          # traverse(codigo,self.rules)
          #chec var existe en function
          #llama al exp y asigna el valor

    def est_decision(self, tree,function):
        pSaltos = []
        primerBloque = True
        hayElse = False
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "decision":
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "expresion":
                            var = self.expresion(child,function)
                            #print("quad: gotof varAnterior pos")

                            self.stackQuads.append(Quadruple('gotof',var,'pos',0))
                            pSaltos.append(len(self.stackQuads))
                        elif ruleChild == "bloque_est":
                            if primerBloque:
                                # print("Entonces: ")
                                self.evaluarBloqueEst(child,function)
                                #print("quad: goto pos")


                                pSaltos.append(len(self.stackQuads))
                            else:
                                hayElse = True
                                self.stackQuads.append(Quadruple('goto','pos',0,0))
                                # print("Si no: ")
                                self.evaluarBloqueEst(child,function)
                                pSaltos.append(len(self.stackQuads))

                            primerBloque = False

                            # print("exp")

                self.stackQuads[pSaltos[0]-1] = Quadruple('gotof',var,pSaltos[1]+1,0)
                # print(pSaltos)
                # print(hayElse)
                if hayElse:
                    self.stackQuads[pSaltos[1]] = Quadruple('goto',pSaltos[2]+1,0,0)
                # print(pSaltos)
                # print(pila)
                # print(tipos)

        else:
            pass
        # traverse(codigo,self.rules)
        #chec var existe en function
        #llama al exp y asigna el valor

    def est_repeticion(self, tree,function):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "repeticion":
                for child in tree.children:
                    rule = self.rules[child.getRuleIndex()]
                    if rule == "condicional":
                        self.est_condicional(child,function)
                    elif rule == "no_condicional":
                        self.est_nocondicional(child,function)

    def est_condicional(self, tree,function):
        pSaltos = []
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "condicional":
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "expresion":
                            pSaltos.append(len(self.stackQuads))
                            var = self.expresion(child,function)
                            #print("var if true or false:", var)
                            #print("quad: gotof varAnterior pos")

                            self.stackQuads.append(Quadruple('gotof',var,'pos',0))
                            pSaltos.append(len(self.stackQuads))
                        elif ruleChild == "bloque_est":
                            self.evaluarBloqueEst(child,function)
                            self.stackQuads.append(Quadruple('goto','pos',0,0))
                            pSaltos.append(len(self.stackQuads))

                self.stackQuads[pSaltos[1]-1] = Quadruple('gotof',var,pSaltos[2],0)
                self.stackQuads[pSaltos[2]-1] = Quadruple('goto',pSaltos[0]+1,0,0)


        else:
            pass

    def est_nocondicional(self, tree,function):
        # traverse(tree,self.rules)
        # print("es no condicional")
        asignar = True
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
                            self.est_asignacion(child,function)
                            for child2 in child.children:
                                if not isinstance(child2, TerminalNodeImpl):
                                    if self.rules[child2.getRuleIndex()] == 'var':
                                        var = child2.getText()
                                        addrVar = self.getAddrOfVariable(var,function)
                                        # print(child2.getText())
                        elif ruleChild == "expresion":
                            # print("Expresion")
                            # pSaltos.append(len(self.stackQuads)+1)
                            exp = self.expresion(child,function)
                            # self.stackQuads.append(Quadruple('>',addr,exp,0))
                            # self.stackQuads.append(Quadruple('gotov','final',0,0))

                            local_counters = self.dirFunciones[function]['counters']
                            offset = self.memory_limits['temp']['bool']
                            addrTemp = self.nextRelativeAddr(local_counters,'bool') + offset

                            self.stackQuads.append(Quadruple('==',addrVar,exp,addrTemp))
                            pSaltos.append(len(self.stackQuads))
                            self.stackQuads.append(Quadruple('gotov',addrTemp,'addr',0))
                            pSaltos.append(len(self.stackQuads))
                        elif ruleChild == "bloque_est":
                            if 1 in self.memory['ctes']:
                                addrUno = self.memory['ctes'][1]['dir']
                            else:
                                offset = self.memory_limits['ctes']['int']
                                addrUno = self.nextRelativeAddr(self.ctesCounter,'int') + offset
                                self.memory['ctes'][1] = {'tipo': 'int', 'dir': addrUno}
                                self.memory['ctesDir'][addrUno] = 1
                            self.evaluarBloqueEst(child,function)
                            self.stackQuads.append(Quadruple('+',addrUno,addrVar,addrVar))
                            self.stackQuads.append(Quadruple('goto','start',0,0))
                            pSaltos.append(len(self.stackQuads))
                            # print(child.getText())
                # self.stackQuads[pSaltos[]]
                self.stackQuads[pSaltos[1]-1] = Quadruple('gotov',addrTemp,pSaltos[2],0)
                self.stackQuads[pSaltos[2]-1] = Quadruple('goto',pSaltos[0],0,0)
                # self.stackQuads[pSaltos[2]-1] = Quadruple('goto',pSaltos[0],0,0)
                # print(pSaltos)

    def est_llamada_est(self,tree,function,stacks=False):
        functionName = tree.ID().getText()

        #Checa que exista y su inicio
        initialAddr = self.getInitialAddrFunction(functionName)
        if not initialAddr:
            msg = "No se encontró la function '{}'".format(functionName)
            return self.error(tree.ID(),msg)

        #Guarda el tipo de Retorno
        returnType = self.dirFunciones[functionName]['tipoRet']

        self.stackQuads.append(Quadruple('era',functionName,0,0))

        self.solveParams(tree.params_llamada(),function,functionName)

        self.stackQuads.append(Quadruple('gosub',functionName,initialAddr,len(self.stackQuads)+1))

        if returnType != "void":
            #quad = "quad: = {} temp".format(functionName)
            #print("nombe fun: en llamada:",function,functionName)

            varAddr = self.getAddrOfVariable(functionName,function)
            varType = self.getTypeOfAddr(varAddr)

            #print("dir de function/var:",addr)

            offset = self.memory_limits['temp'][varType]
            tempAddr = self.nextRelativeAddr(self.tempsCounter,varType) + offset

            self.stackQuads.append(Quadruple('=',varAddr,tempAddr,0))

            if stacks != False:
                stacks['pOperandos'].append(tempAddr)
                stacks['pTipos'].append(varType)

    def est_escritura(self, tree,function):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "expresion":
                res = self.expresion(tree,function)
                dim1 = self.getDimOfAddr(res,function,1)
                if dim1 != False:
                    dim2 = self.getDimOfAddr(res,function,2)
                    self.stackQuads.append(Quadruple('print',res,0,'arreglo'))
                    self.stackQuads.append(Quadruple('dimensiones',res,dim1,dim2))
                else:
                    self.stackQuads.append(Quadruple('print',res,0,0))
            elif self.rules[tree.getRuleIndex()] == "string":
                # print("es un string")
                self.stackQuads.append(Quadruple('print',tree.getText()[1:-1],0,0))
            else:
                for child in tree.children:
                    self.est_escritura(child,function)

        else:
            pass

class Compiler:
    def __init__(self, file):
        self.arch = file
        self.input_stream = FileStream("Pruebas/prueba{}.txt".format(file))
    def compile(self):
        lexer = PatitoMasMasLexer(self.input_stream)
        stream = CommonTokenStream(lexer)
        parser = PatitoMasMasParser(stream)
        startRoute = parser.start().programa()

        # traverse(rutaInicio,parser.ruleNames)
        p = Program(startRoute,parser.ruleNames)
        p.execute()
        return p.getQuads(),p.getConstants()

def main():
    arch = sys.argv[1]
    input_stream = FileStream("Pruebas/prueba{}.txt".format(arch))
    lexer = PatitoMasMasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoMasMasParser(stream)
    startRoute = parser.start().programa()

    # traverse(rutaInicio,parser.ruleNames)

    p = Program(startRoute,parser.ruleNames)
    p.printAll()

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
