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
    def __init__(self,op,dir1,dir2,dir3):
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
        self.memory_limits = {
            'global': {'int': 5000, 'float': 8000, 'char': 10000, 'string': 13000, 'bool': 14000},
            'local': {'int': 15000, 'float': 18000, 'char': 20000, 'string': 23000, 'bool': 24000},
            'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000, 'dir': 50000},
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

    def ejectuar(self):
        varGlobales = {}
        varGlobales2 = {}
        globalCounters = {}
        self.decVariables(self.tree.dec_variables(),varGlobales,varGlobales2,globalCounters,"",'global')
        self.dirFunciones['global'] = {'vars': varGlobales, 'counters': globalCounters, 'varsDir': varGlobales2}
        self.pilaCuad.append(Cuadruplo('goto','global',0,0))
        self.decFunciones(self.tree.dec_functions())

        self.pilaSaltos.append(len(self.pilaCuad)+1)
        self.dirFunciones['global']['empieza'] = len(self.pilaCuad)+1
        self.evaluarBloqueEst(self.tree.principal().bloque_est(),'global')
        #self.temp = 0
        self.tempsCounter = {}
        self.pilaCuad.append(Cuadruplo('end',0,0,0))
        self.pilaCuad[0] = Cuadruplo('goto',self.dirFunciones['global']['empieza'],0,0)

    def cuadruplos(self):
        return self.pilaCuad

    def ctes(self):
        return self.memory['ctesDir']

    def imprimeTodo(self):
        self.ejectuar()

        #Imprime cuadruplos
        print("===== Cuadruplos =====")
        for i in range(len(self.pilaCuad)):
            print(i+1, ".-",self.pilaCuad[i].imprimir())

        #Imprime el directorio de funciones
        print("===== Dir Funciones =====")
        pprint.pprint(self.dirFunciones)

        for k in self.dirFunciones.keys():
            self.memory[k] = self.dirFunciones[k]['vars']

        #Imprime memoria
        print("===== Memory =====")
        pprint.pprint(self.memory)

    ##### VERIFICACIONES
    def varDuplicada(self,var):
        # return True
        for func in self.dirFunciones:
            for var_actual in self.dirFunciones[func]['vars']:
                if var == var_actual:
                    return True

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
        if var in self.dirFunciones['global']['vars']:
            return True
        else:
            if var in self.dirFunciones[funcion]['vars']:
                return True

        return False

    def existeCte(self,cte,tipo):
        if cte in self.memory['ctes']:
            return True
        else:
            return False

    def regresaDim(self,var,funcion,dim):
        res = self.dirFunciones['global']['varsDir'].get(var, None)
        if res != None:
            # print("global")
            checaDim = self.dirFunciones['global']['varsDir'][var].get("{}{}".format("dim",dim), None)
            if checaDim != None:
                return self.dirFunciones['global']['varsDir'][var]["{}{}".format("dim",dim)]
            else:
                return False
        if funcion != "global":
            if res == None:
                res = self.dirFunciones[funcion]['varsDir'].get(var, None)
                if res == None:
                    return False
                else:
                    checaDim = self.dirFunciones[funcion]['varsDir'][var].get("{}{}".format("dim",dim), None)
                    if checaDim != None:
                        return self.dirFunciones[funcion]['varsDir'][var]["{}{}".format("dim",dim)]
                    else:
                        return False
            else:
                return False
        return False

    #Funcion que regresa el tipo de una variable
    def regresaTipoVar(self,var,funcion):
        if self.existeVar(var,funcion):
            res = self.dirFunciones['global']['vars'].get(var, None)
            if res != None:
                return self.dirFunciones['global']['vars'][var]['tipo']
            if funcion != "global":
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

    #Funcion que regresa tipo con base en la direccion
    def regresaTipoDir(self,dir):
        if dir >= 50000:
            return 'int'
        while(dir > 14999):
            dir = dir - 10000

        if dir >= 5000 and dir < 8000:
            return 'int'
        elif dir >= 8000 and dir < 10000:
            return 'float'
        elif dir >= 10000 and dir < 13000:
            return 'char'
        elif dir >= 13000 and dir < 14000:
            return 'string'
        elif dir >= 14000 and dir < 15000:
            return 'bool'

    def regresaInicioFun(self,funcion):
        if self.existeFun(funcion):
            return self.dirFunciones[funcion]['empieza']
        else:
            return False
    ##### PARSE VARS Y FUNCIONES

    #Funcion que te da la siguiente direccion
    def sigDireccionRelativa(self,local_counters,tipo,aumentar=1):
        if aumentar != 1:
            if tipo in local_counters:
                aux = local_counters[tipo]
                local_counters[tipo] += aumentar
                return aux
            else:
                local_counters[tipo] = aumentar
                return 0
        else:
            if tipo in local_counters:
                local_counters[tipo] += 1
            else:
                local_counters[tipo] = 0

        return local_counters[tipo]

    #Funcion que regresa el JSON con la info de las vars
    def decVariables(self,tree,temp,temp2,local_counters,tipo,nomFun):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "dec_var":
                tipo = tree.tipo().getText()

            elif self.rules[tree.getRuleIndex()] == "ids":
                elem = tree.getText()

                if elem in temp:
                    msj = "Var '{}' duplicada".format(elem)
                    return self.error(tree.ID(),msj)

                if nomFun != 'global':
                    scope = 'local'
                    if self.varDuplicada(elem):
                        msj = "Var '{}' duplicada".format(elem)
                        return self.error(tree.ID(),msj)
                else:
                    scope = 'global'

                # print(tree.getText())
                # traverse(tree,self.rules)
                offset = self.memory_limits[scope][tipo]

                if elem.find('[') == -1:
                    addr = self.sigDireccionRelativa(local_counters,tipo) + offset
                    temp[elem] = {'tipo': tipo, 'dir': addr}
                    temp2[addr] = {'nombre':elem}
                else:
                    count = elem.count("[")
                    if count == 1:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        nombre = elem[:indexInicio]
                        dim = int(elem[indexInicio+1:indexFinal])
                        r = 1
                        r = (dim + 1) * r
                        m1 = r / (dim +1)
                        addr = self.sigDireccionRelativa(local_counters,tipo,dim) + offset
                        temp[nombre] = {'tipo': tipo,'dim1': dim, 'dir': addr,'m1': m1}
                        temp2[addr] = {'nombre':nombre,'dim1': dim}
                    if count == 2:
                        indexInicio = elem.index("[")
                        indexFinal = elem.index("]")
                        indexInicio2 = elem.find("[", indexInicio + 1)
                        indexFinal2 = elem.find("]", indexFinal + 1)
                        nombre = elem[:indexInicio]
                        dim = int(elem[indexInicio+1:indexFinal])
                        dim2 = int(elem[indexInicio2+1:indexFinal2])
                        r = 1
                        r = (dim + 1) * r
                        m1 = r / (dim +1)
                        r = m1
                        r = (dim2 + 1) * r
                        m2 = r / (dim2 +1)
                        dims = dim * dim2
                        addr = self.sigDireccionRelativa(local_counters,tipo,dims) + offset
                        temp[nombre] = {'tipo': tipo,'dim1': dim,'dim2':dim2, 'dir': addr,'m1': m1,'m2': m2}
                        temp2[addr] = {'nombre':nombre,'dim1': dim,'dim2':dim2}
            else:
                pass
            for child in tree.children:
                self.decVariables(child,temp,temp2,local_counters,tipo,nomFun)

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
                    tipo_ret = tree.tipo_ret()

                    if tipo_ret.getText() == "void":
                        ret = "void"
                    else:
                        ret = tipo_ret.tipo().getText()
                        globalCounters = self.dirFunciones['global']['counters']
                        offset = self.memory_limits['global'][ret]
                        addr = self.sigDireccionRelativa(globalCounters,ret) + offset
                        self.dirFunciones['global']['vars'][nombreFun] = {'tipo' : ret, 'dir': addr}

                    tablaParams = []
                    tablaDirs = []
                    varsParams = {}
                    #tempVar = {}
                    tempVar2 = {}

                    #Local counter of types of vars and params
                    localCounters = {}

                    self.decParamsFun(tree.params(),varsParams,tablaParams,tablaDirs,nombreFun,localCounters)
                    self.decVariables(tree.dec_variables(),varsParams,tempVar2,localCounters,"",nombreFun)
                    #self.decVariables(tree.dec_variables(),tempVar,tempVar2,localCounters,"",nombreFun)

                    varsFunc = varsParams
                    #varsFunc = dict(list(varsParams.items()) + list(tempVar.items()))

                    cuadEmpieza = len(self.pilaCuad) + 1
                    jsontemp["params"] = tablaParams
                    jsontemp["paramsDir"] = tablaDirs
                    jsontemp["vars"] = varsFunc
                    jsontemp["varsDir"] = tempVar2
                    jsontemp["tipoRet"] = ret
                    jsontemp["empieza"] = cuadEmpieza
                    jsontemp["counters"] = localCounters
                    self.dirFunciones[nombreFun] = jsontemp
                    self.evaluarBloqueEst(tree.bloque_est(),nombreFun)
                    self.tempsCounter = {}
                    #self.temp = 0
                    self.pilaCuad.append(Cuadruplo('endproc',0,0,0))
            else:
                for child in tree.children:
                        self.decFunciones(child)
        else:
            pass

    def decParamsFun(self,tree,varsParams,tablaParams,tablaDirs,nombreFun,local_counters):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                nombre = tree.ID().getText()

                if nombre in varsParams or self.varDuplicada(nombre):
                    msj = "Var '{}' duplicada".format(nombre)
                    return self.error(tree.ID(),msj)

                tipo = tree.tipo().getText()
                tablaParams.append(tipo)
                offset = self.memory_limits['local'][tipo]
                addr = self.sigDireccionRelativa(local_counters,tipo) + offset
                tablaDirs.append(addr)
                #self.dirFunciones[nombreFun]['vars'][nombre] = {'tipo': tipo, 'dir': addr}
                varsParams[nombre] = {'tipo': tipo, 'dir': addr}

            for child in tree.children:
                self.decParamsFun(child,varsParams,tablaParams,tablaDirs,nombreFun,local_counters)
        else:
            pass

    #### EXPRESION

    def expresion(self,tree,funcion):
        pilas = {
            'pOperandos' : [],
            'pOperadores' : [],
            'pTipos' : [],
            'pDim': []
        }
        self.expresionAux(tree,funcion,pilas)
        return pilas['pOperandos'][0]

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
                                    """
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
                                    """

                                    # print("der: ",right,"izq:",left)
                                    # res = self.genQuad(op,left,right)
                                    offset = self.memory_limits['temp'][tipoRes]
                                    addr = self.sigDireccionRelativa(self.tempsCounter,tipoRes) + offset

                                    #res = self.temp
                                    #self.temp += 1
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    self.pilaCuad.append(Cuadruplo(op,left,right,addr))


                                    pilas['pOperandos'].append(addr)

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
                                    offset = self.memory_limits['temp'][tipoRes]
                                    addr = self.sigDireccionRelativa(self.tempsCounter,tipoRes) + offset

                                    self.pilaCuad.append(Cuadruplo(op,left,right,addr))

                                    pilas['pOperandos'].append(addr)
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
                                    """
                                    elif tipoRes == "int":
                                        right = int(right)
                                        left = int(left)
                                    elif tipoRes == "float":
                                        right = float(right)
                                        left = float(left)
                                        """

                                    # print("der: ",right,"izq:",left)
                                    #res = self.genQuad(op,left,right)
                                    #res = self.temp
                                    #self.temp += 1
                                    offset = self.memory_limits['temp'][tipoRes]
                                    addr = self.sigDireccionRelativa(self.tempsCounter,tipoRes) + offset
                                    # print(res)
                                    #print("quad: ", op, left,right,res)

                                    self.pilaCuad.append(Cuadruplo(op,left,right,addr))

                                    pilas['pOperandos'].append(addr)
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
                                """
                                elif tipoRes == "int":
                                    right = int(right)
                                    left = int(left)
                                elif tipoRes == "float":
                                    right = float(right)
                                    left = float(left)
"""

                                # print("der: ",right,"izq:",left)
                                #res = self.genQuad(op,left,right)
                                #res = self.temp
                                #self.temp += 1
                                offset = self.memory_limits['temp'][tipoRes]
                                addr = self.sigDireccionRelativa(self.tempsCounter,tipoRes) + offset
                                # print(res)
                                #print("quad: ", op, left,right,res)

                                self.pilaCuad.append(Cuadruplo(op,left,right,addr))

                                # print("= Pilas temporales =")
                                # print("Pila operandos:",pilas['pOperandos'])
                                # print("Pila tipos:",pilas['pTipos'])
                                # print("Pila operadores:",pilas['pOperadores'])

                                pilas['pOperandos'].append(addr)
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
                        # print("si se llamo")
                        self.varAux(child,funcion,pilas)
                        # self.factorAux(child,funcion,pilas)
                    elif ruleChild == "var_cte":
                        self.varcteAux(child,funcion,pilas)
                    elif ruleChild == "op_esp":
                        # print("encontre $ ? ¡")
                        # print(pilas['pOperadores'])
                        op = child.getText()
                        dir = pilas['pOperandos'][-1]
                        self.pilaCuad.append(Cuadruplo(op,dir,0,dir))
                        dim1 = self.regresaDim(dir,funcion,1)
                        dim2 = self.regresaDim(dir,funcion,2)
                        if dim2 != False:
                            self.pilaCuad.append(Cuadruplo('dimensiones',dir,dim1,dim2))
                        else:
                            self.pilaCuad.append(Cuadruplo('dimensiones',dir,dim1,-1))
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

    def getDirVar(self, nombre, scope):
        if nombre in self.dirFunciones[scope]['vars']:
            return self.dirFunciones[scope]['vars'][nombre]['dir']
        else:
            return self.dirFunciones['global']['vars'][nombre]['dir']

    def getNomDir(self, dir, scope):
        if dir in self.dirFunciones[scope]['varsDir']:
            return self.dirFunciones[scope]['varsDir'][dir]['nombre']
        else:
            return self.dirFunciones['global']['varsDir'][dir]['nombre']

    def varAux(self,tree,funcion,pilas,brackets=False):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var":
                nomVar = tree.ID().getText()
                # print("Var : " , nomVar)
                tipo = self.regresaTipoVar(nomVar,funcion)
                # print(nomVar,tipo)

                if tipo == False:
                    msj = "No se encontró la var '{}'".format(nomVar)
                    return self.error(tree.ID(),msj)

                pilas['pTipos'].append(tipo)
                addr = self.getDirVar(nomVar,funcion)
                tieneDim = self.regresaDim(addr,funcion,1)
                # print(addr)
                # print(addr)
                pilas['pOperandos'].append(addr)

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
                                    id = pilas['pOperandos'].pop()
                                    type = pilas['pTipos'].pop()
                                    # print("pila",pilas['pOperandos'])
                                    pilas['pOperadores'].append("$")
                                self.dimAux(child,funcion,dim,pilas,id,type)
                                dim+=1
        else:
            pass

    def dimAux(self,tree,funcion,dim,pilas,id,type):
        pilas2 = {
            'pOperandos' : [],
            'pOperadores' : [],
            'pTipos' : [],
            'pDim': []
        }
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                ruleChild = self.rules[child.getRuleIndex()]
                # rules.append(ruleChild)
                if ruleChild == "expresion":
                    # print(pilas2['pOperandos'])
                    self.expresionAux(child,funcion,pilas2)

        if dim == 1:
            resExp = pilas2['pOperandos'][-1]
            lsdim1 = self.regresaDim(id,funcion,1)
            lsdim2 = self.regresaDim(id,funcion,2)

            self.pilaCuad.append(Cuadruplo('verify',resExp,0,lsdim1))

            if lsdim2 == False:
                if id in self.memory['ctes']:
                    baseaddr = self.memory['ctes'][id]['dir']
                else:
                    offset = self.memory_limits['ctes']['int']
                    baseaddr = self.sigDireccionRelativa(self.ctesCounter,'int') + offset
                    self.memory['ctes'][id] = {'tipo': 'int', 'dir': baseaddr}
                    self.memory['ctesDir'][baseaddr] = id
                offset = self.memory_limits['temp']['dir']
                addr = self.sigDireccionRelativa(self.ctesCounter,'dir') + offset
                self.pilaCuad.append(Cuadruplo('+',resExp,baseaddr,addr))
                pilas['pOperandos'].append(addr)
                pilas['pTipos'].append(type)
                pilas['pOperadores'].pop()
            else:
                if lsdim2 in self.memory['ctes']:
                    lsdim2addr = self.memory['ctes'][lsdim2]['dir']
                else:
                    offset = self.memory_limits['ctes']['int']
                    lsdim2addr = self.sigDireccionRelativa(self.ctesCounter,'int') + offset
                    self.memory['ctes'][lsdim2] = {'tipo': 'int', 'dir': lsdim2addr}
                    self.memory['ctesDir'][lsdim2addr] = lsdim2
                offset = self.memory_limits['temp']['int']
                addr = self.sigDireccionRelativa(self.ctesCounter,'int') + offset
                self.pilaCuad.append(Cuadruplo('*',resExp,lsdim2addr,addr))
                pilas['pDim'].append(addr)
                # print(pilas['pDim'])
        elif dim == 2:
            resExp = pilas2['pOperandos'][-1]
            lsdim2 = self.regresaDim(id,funcion,2)
            # print("dim",id, self.regresaDim(5000,funcion,2))
            # print(pilas['pDim'])
            temp1 = pilas['pDim'].pop()
            self.pilaCuad.append(Cuadruplo('verify',resExp,0,lsdim2))

            offset = self.memory_limits['temp']['int']
            addr1 = self.sigDireccionRelativa(self.ctesCounter,'int') + offset
            self.pilaCuad.append(Cuadruplo('+',resExp,temp1,addr1))

            if id in self.memory['ctes']:
                baseaddr = self.memory['ctes'][id]['dir']
            else:
                offset = self.memory_limits['ctes']['int']
                baseaddr = self.sigDireccionRelativa(self.ctesCounter,'int') + offset
                self.memory['ctes'][id] = {'tipo': 'int', 'dir': baseaddr}
                self.memory['ctesDir'][baseaddr] = id
            offset = self.memory_limits['temp']['dir']
            addr2 = self.sigDireccionRelativa(self.ctesCounter,'dir') + offset
            self.pilaCuad.append(Cuadruplo('+',addr1,baseaddr,addr2))

            pilas['pOperandos'].append(addr2)
            pilas['pTipos'].append(type)
            # print("addr2",addr2,pilas['pOperandos'])
            pilas['pOperadores'].pop()

        # traverse(tree,self.rules)

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

                        if cte in self.memory['ctes']:
                            addr = self.memory['ctes'][cte]['dir']
                        else:
                            offset = self.memory_limits['ctes'][tipo]
                            addr = self.sigDireccionRelativa(self.ctesCounter,tipo) + offset
                            self.memory['ctes'][cte] = {'tipo': tipo, 'dir': addr}
                            self.memory['ctesDir'][addr] = cte

                        pilas['pTipos'].append(tipo)
                        #diana
                        pilas['pOperandos'].append(addr)
                        #pilas['pOperandos'].append(cte)
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

    def evaluarBloqueEst(self, tree, funcion):
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
        if funcion == "global":
            msj = "La funcion main no tiene retorno"
            return self.error(tree.Regresa(),msj)
        elif self.dirFunciones[funcion]['tipoRet'] == "void":
            msj = "Retorno en funcion '{}' de tipo void".format(funcion)
            return self.error(tree.Regresa(),msj)
        self.expresion(tree.expresion(),funcion)
        #else mandar llamar expresion con el codigo
        # print(tree.expresion().getText())

    def est_lectura(self,tree,funcion):
        res = []
        self.lecturaAux(tree.lista_vars(),res,funcion)
        #print("Res in est lectura:",res)
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
                        addr = self.getDirVar(nom,funcion)
                        res.append(addr)
                    else:
                        msj = "No se encontró la var '{}'".format(nom)
                        return self.error(child.ID(),msj)
                    # print(child.ID().getText())
                elif regla == "lista_vars":
                    self.lecturaAux(child,res,funcion)
                    # traverse(child,self.rules)
                # print(regla)

    def est_asignacion(self, tree, funcion):
        # traverse(tree,self.rules)
        # print(len(tree.children))
        # print(tree.getText())
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "asignacion":
                # print("asign")
                pilas = {
                    'pOperandos' : [],
                    'pOperadores' : [],
                    'pTipos' : [],
                    'pDim': [],
                    'tieneBrackets' : []
                }
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
                            addr = self.getDirVar(nombre,funcion)
                            # print(tipo)
                            if not tipo:
                                msj = "No se encontró la var '{}'".format(nombre)
                                return self.error(child.ID(),msj)

                            tieneDim = self.regresaDim(addr,funcion,1)
                            if tieneDim != False:
                                dim = 1
                                for child2 in child.children:
                                    if not isinstance(child2, TerminalNodeImpl):
                                        ruleChild = self.rules[child2.getRuleIndex()]
                                        # rules.append(ruleChild)
                                        if ruleChild == "dim":
                                            if dim == 1:
                                                pilas['tieneBrackets'].append(True)
                                                pilas['pOperandos'].append(addr)
                                                pilas['pTipos'].append(tipo)
                                                pilas['pOperadores'].append("$")
                                            self.dimAux(child2,funcion,dim,pilas,addr,tipo)
                                            dim+=1

                            #pila.append(nombre)
                            # if funcion == "main":
                            #     funcion = "global"
                            c = child.ID()
                            if len(pila) > 1:
                                tipo_anterior = tipos[-1]
                                if tipo != tipo_anterior:
                                    msj = "Asignacion invalida {}({}) a {}({})".format(addr,tipo,pila[-1],tipos[-1])
                                    return self.error(c,msj)
                            if tieneDim == False:
                                pilas['tieneBrackets'].append(False)
                                pilas['pOperandos'].append(addr)
                                pilas['pTipos'].append(tipo)

                            # print("oila", pila)
                            # print("oila", tipos)
                        elif ruleChild == "expresion":
                            # print("exp")
                            exp = self.expresion(child,funcion)
                            tipo_exp = self.regresaTipoDir(exp)

                            topTipos = pilas['pTipos'][-1]
                            topOperandos = pilas['pOperandos'][-1]
                            if tipo_exp != topTipos:
                                msj = "Asignacion invalida {}({}) a {}({})".format(exp,tipo_exp,topOperandos,topTipos)
                                #print("error", msj)
                                #print("child:",child)
                                return self.error(c,msj)


                #print("quad: = EXP", pila[-1])
                #quad = "quad: = EXP " + str(pila[-1])
                """
                print("pila:", pila)
                print("tipos:",tipos)
                print("tipo exp:",self.regresaTipoDir(exp))
                print("exp",exp)
                """
                ####AGREGAR ALGO PARA SABER SI ADDR Y EXP TENIAN [][] O NO
                addrIzq = pilas['pOperandos'][-1]
                bracketsIzq = pilas['tieneBrackets'].pop()
                dim1Izq = self.regresaDim(addr,funcion,1)
                dim2Izq = self.regresaDim(addr,funcion,2)

                dim1Der = self.regresaDim(exp,funcion,1)
                dim2Der = self.regresaDim(exp,funcion,2)
                if bracketsIzq:
                    self.pilaCuad.append(Cuadruplo('=',exp,addrIzq,'arrSingle'))
                    pilas['pOperandos'].pop()
                else:
                    if dim1Izq != False and dim1Der == False:
                        nom1 = self.getNomDir(addr,funcion)
                        # nom2 = self.getNomDir(exp,funcion)
                        msj = "No se puede asignar un valor a todo el arreglo '{}'".format(nom1)
                        return self.error(c,msj)
                    # print("si son iguales")
                    # print("izq:",dim1Izq,dim2Izq)
                    # print("der:",dim1Der,dim2Der)
                    if dim1Izq != False and dim1Der != False:
                        if (dim1Izq == dim1Der) and (dim2Izq == dim2Der):
                            self.pilaCuad.append(Cuadruplo('=',exp,addrIzq,'arreglo'))
                        else:
                            nom1 = self.getNomDir(addr,funcion)
                            nom2 = self.getNomDir(exp,funcion)
                            msj = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(nom1,nom2)
                            # print(msj)
                            return self.error(c,msj)
                    else:
                        self.pilaCuad.append(Cuadruplo('=',exp,addrIzq,0))
                lenPila = len(pilas['pOperandos'])
                if lenPila > 1:
                    for i in range(lenPila-1):
                        addrIzq = pilas['pOperandos'].pop()
                        dim1Izq = self.regresaDim(addrIzq,funcion,1)
                        dim2Izq = self.regresaDim(addrIzq,funcion,2)

                        addrDer = pilas['pOperandos'][-1]
                        dim1Der = self.regresaDim(addrDer,funcion,1)
                        dim2Der = self.regresaDim(addrDer,funcion,2)

                        if dim1Izq != False and dim1Der != False:
                            if (dim1Izq == dim1Der) and (dim2Izq == dim2Der):
                                self.pilaCuad.append(Cuadruplo('=',addrIzq,addrDer,'arreglo'))
                            else:
                                nom1 = self.getNomDir(addrIzq,funcion)
                                nom2 = self.getNomDir(addrDer,funcion)
                                msj = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(nom1,nom2)
                                # print(msj)
                                return self.error(c,msj)
                        else:
                            self.pilaCuad.append(Cuadruplo('=',addrIzq,addrDer,0))


                #self.pilaCuad.append(Cuadruplo('=',exp,str(pila[-1]),0))
        else:
            pass
        # traverse(codigo,self.rules)
        #chec var existe en funcion
        #llama al exp y asigna el valor

    def est_decision(self, tree,funcion):
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
                            var = self.expresion(child,funcion)
                            #print("quad: gotof varAnterior pos")

                            self.pilaCuad.append(Cuadruplo('gotof',var,'pos',0))
                            pSaltos.append(len(self.pilaCuad))
                        elif ruleChild == "bloque_est":
                            if primerBloque:
                                # print("Entonces: ")
                                self.evaluarBloqueEst(child,funcion)
                                #print("quad: goto pos")


                                pSaltos.append(len(self.pilaCuad))
                            else:
                                hayElse = True
                                self.pilaCuad.append(Cuadruplo('goto','pos',0,0))
                                # print("Si no: ")
                                self.evaluarBloqueEst(child,funcion)
                                pSaltos.append(len(self.pilaCuad))

                            primerBloque = False

                            # print("exp")

                self.pilaCuad[pSaltos[0]-1] = Cuadruplo('gotof',var,pSaltos[1]+1,0)
                # print(pSaltos)
                # print(hayElse)
                if hayElse:
                    self.pilaCuad[pSaltos[1]] = Cuadruplo('goto',pSaltos[2]+1,0,0)
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
                            var = self.expresion(child,funcion)
                            #print("var if true or false:", var)
                            #print("quad: gotof varAnterior pos")

                            self.pilaCuad.append(Cuadruplo('gotof',var,'pos',0))
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
                self.pilaCuad[pSaltos[1]-1] = Cuadruplo('gotof',var,pSaltos[2]+1,0)
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
                            exp = self.expresion(child,funcion)
                            self.pilaCuad.append(Cuadruplo('>',var,exp,0))
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
        self.pilaCuad.append(Cuadruplo('gosub',nombreFun,dirInicio,len(self.pilaCuad)+1))

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
                    exp = self.expresion(child,funcion)
                    dir = self.dirFunciones[funcion]['paramsDir'][cont]
                    self.pilaCuad.append(Cuadruplo('param',exp,dir,0))
                    cont += 1
                elif regla == "params_llamada":
                    self.resolverParams(child,funcion,cont)



    def est_escritura(self, tree,funcion):
        if not isinstance(tree, TerminalNodeImpl):
        #     # print(codigo.getRuleContext().getText())
        #     # traverse(codigo,self.rules)
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("***** EXP *****")
                # print(codigo.getText())
                # traverse(codigo,self.rules)
                res = self.expresion(tree,funcion)
                self.pilaCuad.append(Cuadruplo('print',res,0,0))
                #mandar llamar expresion con el codigo
                # res.append("EXP")
                # print("")
            elif self.rules[tree.getRuleIndex()] == "string":
                # print("es un string")
                self.pilaCuad.append(Cuadruplo('print',tree.getText()[1:-1],0,0))
            else:
                # traverse(codigo,self.rules)
                # print("no string")
        #         print("lo ignoramos")
                for child in tree.children:
                    # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                    #     print("Estatuto: ", tree)
                    self.est_escritura(child,funcion)
        #

        else:
            pass
        # for index, item in enumerate(res):
        #     res[index] = res[index][1:-1]
        #     str += res[index] + " "
        #print("quad: print", str)

        # self.pilaCuad.append(Cuadruplo('print',str,0,0))

    ##falta
    #los valores pueden ser exp
    def _extraePrint(self, tree,funcion):
        if not isinstance(tree, TerminalNodeImpl):
        #     # print(codigo.getRuleContext().getText())
        #     # traverse(codigo,self.rules)
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("***** EXP *****")
                # print(codigo.getText())
                # traverse(codigo,self.rules)
                self.expresion(tree,funcion)
                self.pilaCuad.append(Cuadruplo('print',"EXP",0,0))
                #mandar llamar expresion con el codigo
                # res.append("EXP")
                # print("")
            elif self.rules[tree.getRuleIndex()] == "string":
                # print("es un string")
                self.pilaCuad.append(Cuadruplo('print',tree.getText(),0,0))
            else:
                # traverse(codigo,self.rules)
                # print("no string")
        #         print("lo ignoramos")
                for child in tree.children:
                    # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                    #     print("Estatuto: ", tree)
                    self._extraePrint(child,funcion)
        #

        else:
            pass

class Compilador:
    def __init__(self, arch):
        self.arch = arch
        self.input_stream = FileStream("prueba{}.txt".format(arch))
    def compilar(self):
        lexer = PatitoMasMasLexer(self.input_stream)
        stream = CommonTokenStream(lexer)
        parser = PatitoMasMasParser(stream)
        rutaInicio = parser.start().programa()

        # traverse(rutaInicio,parser.ruleNames)
        programa = Programa(rutaInicio,parser.ruleNames)
        programa.ejectuar()
        return programa.cuadruplos(),programa.ctes()

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
    elif arch == '6':
        input_stream = FileStream("prueba6.txt")
    elif arch == '7':
        input_stream = FileStream("prueba7.txt")
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
