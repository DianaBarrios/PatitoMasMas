from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
from antlr4.error.ErrorListener import ErrorListener
import sys
import pprint

"""
    Cubo semantico para que hagas verificaciones de las posibles operaciones
"""
arithmeticCube = {
    '+': {
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
    '-': {
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
    '/': {
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
    '*': {
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
    '>': {
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
    '<': {
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
    '||': {
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
    '&': {
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
    '==': {
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
    '!=': {
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
    '=': {
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


class MyErrorListener(ErrorListener):
    """Clase para imprimir los errores del parser bonitos
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Error línea-> {}:{} -> {}".format(line, column, msg))
        exit()


class Quadruple:
    def __init__(self, op, addr1, addr2, addr3):
        """Clase para tener una estructura de los cuadruplos

        Arguments:
            op {string} -- El tipo de operación que se tiene que ejecutar
            addr1 {int|string} -- Casi siempre es una dirección menos cuando es un print de string
            addr2 {int} -- Casi siempre es una dirección o un limite superior de alguna dimensión
            addr3 {int} -- Casi siempre es una dirección o un limite superior de alguna dimensión
        """
        self.op = op
        self.addr1 = addr1
        self.addr2 = addr2
        self.addr3 = addr3

    def imprimir(self):
        """Le da formato a un cuadruplo y lo regresa

        Returns:
            string -- Cuadruplo formateado para imprimir
        """
        str = "quad: {} {} {} {}".format(
            self.op, self.addr1, self.addr2, self.addr3)
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
            'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000, 'dir': 50000, 'dirArreglo': 55000},
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

    def error(self, tree, mensaje):
        """Función para sacar la linea y la columna del error en cuestion e imprimirlo

        Arguments:
            tree {[type]} -- Regla gramatical donde se encontró el error
            mensaje {string} -- El mensaje para el error
        """
        line = tree.getSymbol().line
        column = tree.getSymbol().column
        print("Error línea-> {}:{} -> {}".format(line, column, mensaje))
        exit()

    def execute(self):
        """Función parent que manda llamar a las otras y organiza la información que estas regresan
        """
        varGlobales = {}
        varGlobales2 = {}
        globalCounters = {}
        if self.tree.dec_variables() != None:
            self.decVariables(self.tree.dec_variables(), varGlobales,
                          varGlobales2, globalCounters, "", 'global')
        self.dirFunciones['global'] = {
            'vars': varGlobales, 'counters': globalCounters, 'varsAddr': varGlobales2}
        self.stackQuads.append(Quadruple('goto', 'global', 0, 0))
        if self.tree.dec_functions() != None:
            self.decFunciones(self.tree.dec_functions())

        self.pilaSaltos.append(len(self.stackQuads)+1)
        self.dirFunciones['global']['startQuad'] = len(self.stackQuads)+1
        self.evaluarBloqueEst(self.tree.principal().bloque_est(), 'global')
        #self.temp = 0
        self.tempsCounter = {}
        self.stackQuads.append(Quadruple('end', 0, 0, 0))
        self.stackQuads[0] = Quadruple(
            'goto', self.dirFunciones['global']['startQuad'], 0, 0)

    def printAll(self):
        """Función que imprime los cuadruplos, dir de funciones y la memoria despues de compilar el programa.
        """
        self.execute()
        pprint.pprint(self.getAllNames())
        # Imprime cuadruplos
        print("===== Cuadruplos =====")
        for i in range(len(self.stackQuads)):
            print(i+1, ".-", self.stackQuads[i].imprimir())

        # Imprime el directorio de funciones
        print("===== Dir Funciones =====")
        pprint.pprint(self.dirFunciones)

        for k in self.dirFunciones.keys():
            self.memory[k] = self.dirFunciones[k]['vars']

        # Imprime memoria
        print("===== Memory =====")
        pprint.pprint(self.memory)

    # VERIFICACIONES
    def checksDuplicateVar(self, var):
        """Función que te dice si una variable con ese nombre ya existe

        Arguments:
            var {string} -- Nombre de la variable a verificar

        Returns:
            bool -- Regresa verdadero si ya existe
        """
        # return True
        for func in self.dirFunciones:
            for currentVar in self.dirFunciones[func]['vars']:
                if var == currentVar:
                    return True
        return False

    def checksFunctionExists(self, function):
        """Función que te dice si una función con ese nombre ya existe

        Arguments:
            function {string} -- Nombre de la funcion a verificar

        Returns:
            bool -- Regresa verdadero si ya existe
        """
        if self.dirFunciones.get(function, None) == None:
            return False
        return True

    def checksVariableExists(self, var, function):
        """Función que checa si una variable existe en el contexto o no

        Arguments:
            var {string} -- Nombre de la variable a verificar
            function {string} -- Funcion donde se esta verificando

        Returns:
            bool -- Regresa verdadero si existe la variable
        """
        if var in self.dirFunciones['global']['vars']:
            return True
        else:
            if var in self.dirFunciones[function]['vars']:
                return True

        return False

    # GETS
    def getAllNames(self):
        """Función helper para la VM donde a cada dirección se le pone su nombre
        para mejor manejo de errores en la VM

        Returns:
            dict -- Diccionario con la dirección como clave y el nombre como valor
        """
        temp = {}
        for i in self.dirFunciones:
            temp[i] = {}
            for j in self.dirFunciones[i]['varsAddr']:
                dim1 = self.dirFunciones[i]['varsAddr'][j].get('dim1', None)
                if dim1 != None:
                    # print(dim1)
                    dim2 = self.dirFunciones[i]['varsAddr'][j].get(
                        'dim2', None)
                    if dim2 == None:
                        for cont in range(dim1):
                            temp[i][j+cont] = {'var': self.dirFunciones[i]
                                               ['varsAddr'][j]['nombre'], 'pos1': cont}
                    else:
                        for cont in range(dim1):
                            for cont2 in range(dim2):
                                realAddr = j + cont * dim2 + cont2
                                temp[i][realAddr] = {
                                    'var': self.dirFunciones[i]['varsAddr'][j]['nombre'], 'pos1': cont, 'pos2': cont2}
                    # print(dim2)
                    # print(j, "tiene dim wuwuw")
                else:
                    # print(self.dirFunciones[i]['varsAddr'][j]['nombre'], "no tiene")
                    temp[i][j] = {'var': self.dirFunciones[i]
                                  ['varsAddr'][j]['nombre']}
        return temp

    def getQuads(self):
        """Función helper para la VM donde regresa todos los cuadruplos generados

        Returns:
            stack -- Stack con todos los cuadruplos de clase Cuadruple
        """
        return self.stackQuads

    def getConstants(self):
        """Función helper para la VM donde regresa todas las constantes usadas

        Returns:
            dict -- Diccionario con la dirección como clave y el valor de la constante como valor
        """
        return self.memory['ctesDir']

    def getDimOfAddr(self, var, function, dim):
        """Función que te da el limite superior de la dimensión solicitada de una dirección

        Arguments:
            var {int} -- Dirección base del arreglo
            function {string} -- Función donde se va a buscar esta variable
            dim {int} -- Número de dimensión (1 o 2)

        Returns:
            bool|int -- Falso si no tiene esa dimensión o el limite superior si existe
        """
        res = self.dirFunciones['global']['varsAddr'].get(var, None)
        if res != None:
            # print("global")
            checaDim = self.dirFunciones['global']['varsAddr'][var].get(
                "{}{}".format("dim", dim), None)
            if checaDim != None:
                return self.dirFunciones['global']['varsAddr'][var]["{}{}".format("dim", dim)]
            else:
                return False
        if function != "global":
            if res == None:
                res = self.dirFunciones[function]['varsAddr'].get(var, None)
                if res == None:
                    return False
                else:
                    checaDim = self.dirFunciones[function]['varsAddr'][var].get(
                        "{}{}".format("dim", dim), None)
                    if checaDim != None:
                        return self.dirFunciones[function]['varsAddr'][var]["{}{}".format("dim", dim)]
                    else:
                        return False
            else:
                return False
        return False

    def getReturnsArray(self, function):
        """Función que te dice si el tipo de retorno de una función es un array o no

        Arguments:
            function {string} -- Nombre de la función

        Returns:
            bool -- True si es array, False si no es
        """
        res = self.dirFunciones['global']['vars'][function].get('array', None)
        if res != None:
            return True
        return False

    # Funcion que regresa el tipo de una variable
    def getTypeOfVariable(self, var, function):
        """Función que te da el tipo de una variable(nombre)

        Arguments:
            var {string} -- Nombre de la variable
            function {string} -- Función donde se va a buscar esta variable

        Returns:
            string|bool -- Falso si no existe la variable o el tipo si la encuentra
        """
        if self.checksVariableExists(var, function):
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

    # Funcion que regresa tipo con base en la direccion

    def getTypeOfAddr(self, addr):
        """Función que te da el tipo de una variable(dirección) con base a sus rangos

        Arguments:
            addr {int} -- Dirección de la variable

        Returns:
            string -- El tipo de la variable
        """
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

    def getInitialAddrFunction(self, function):
        """Función que te da el cuadruplo donde empieza una funcion

        Arguments:
            function {string} -- Nombre de la función

        Returns:
            int|bool -- Falso si no existe o el número de cuadruplo donde empieza
        """
        if self.checksFunctionExists(function):
            return self.dirFunciones[function]['startQuad']
        else:
            return False

    def getAddrOfVariable(self, varName, function):
        """Función que te da la dirección de una variable(nombre)

        Arguments:
            varName {string} -- Nombre de la variable a buscar
            function {string} -- Función donde se va a buscar esta variable

        Returns:
            int|bool -- Falso si no existe o la dirección
        """
        exists = self.checksVariableExists(varName, function)
        if not exists:
            return False
        if varName in self.dirFunciones[function]['vars']:
            return self.dirFunciones[function]['vars'][varName]['dir']
        else:
            return self.dirFunciones['global']['vars'][varName]['dir']

    def getNameOfAddr(self, addr, function):
        """Función que te da el nombre de una variable a partir de su dirección

        Arguments:
            addr {int} -- Dirección de la variable a buscar
            function {string} -- Función donde se va a buscar esta dirección

        Returns:
            string -- El nombre de la variable
        """
        if addr in self.dirFunciones[function]['varsAddr']:
            return self.dirFunciones[function]['varsAddr'][addr]['nombre']
        else:
            return self.dirFunciones['global']['varsAddr'][addr]['nombre']

    # HELPERS
    # Funcion que te da la siguiente direccion
    def nextRelativeAddr(self, local_counters, type, increment=1):
        """Función que te da la siguiente dirección relativa para asignar dependiendo de
        la función de la que se mande llamar

        Arguments:
            local_counters {dict} -- Diccionario con los contadores de las variables actuales
            type {string} -- Tipo de variable que quieres asignar

        Keyword Arguments:
            increment {int} -- Te dice cuantos incrementar si es un arreglo/matriz (default: {1})

        Returns:
            int -- La siguiente dirección relativa
        """
        if increment != 1:
            if type in local_counters:
                aux = local_counters[type]
                local_counters[type] += increment
                return aux + 1
            else:
                local_counters[type] = increment
                return 0
        else:
            if type in local_counters:
                local_counters[type] += 1
            else:
                local_counters[type] = 0
        return local_counters[type]

    # PARSE VARS Y FUNCIONES
    # Funcion que regresa el JSON con la info de las vars
    def decVariables(self, tree, varsFunc, varsDir, local_counters, varType, function):
        """Función que pone todas las variables en un diccionario junto con su nombre, dirección, tipo y dimensiones
        dec_var
            : tipo lista_ids+ ';'
            ;

        lista_ids
            : ids (','  lista_ids)?
            ;

        ids
            : ID dimension? dimension?
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            varsFunc {dict} -- Diccionario donde se guardan las variables con el nombre como key
            varsDir {dict} -- Diccionario donde se guardan las variables con dirección como key
            local_counters {dict} -- Diccionario que te dice cuantas variables hay de cada tipo
            varType {string} -- Tipo de variable a declarar en este momento.
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "dec_var":
                varType = tree.tipo().getText()

            elif self.rules[tree.getRuleIndex()] == "ids":
                varName = tree.ID().getText()
                numDim = 0
                for child in tree.children:
                    if not isinstance(child, TerminalNodeImpl):
                        if self.rules[child.getRuleIndex()] == "dimension":
                            numDim += 1
                            if numDim == 1:
                                dim1 = int(child.CTE_INT().getText())
                            elif numDim == 2:
                                dim2 = int(child.CTE_INT().getText())

                # print(numDim)
                if varName in varsFunc:
                    msg = "Var '{}' duplicada".format(varName)
                    return self.error(tree.ID(), msg)

                if function != 'global':
                    offset = self.memory_limits['local'][varType]
                    if self.checksDuplicateVar(varName):
                        msg = "Var '{}' duplicada".format(varName)
                        return self.error(tree.ID(), msg)
                else:
                    offset = self.memory_limits['global'][varType]

                if numDim == 0:
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType) + offset
                    varsFunc[varName] = {'tipo': varType, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName}
                elif numDim == 1:
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType, dim1) + offset
                    varsFunc[varName] = {'tipo': varType,
                                         'dim1': dim1, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName, 'dim1': dim1}
                elif numDim == 2:
                    dims = dim1 * dim2
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType, dims) + offset
                    varsFunc[varName] = {
                        'tipo': varType, 'dim1': dim1, 'dim2': dim2, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName,
                                        'dim1': dim1, 'dim2': dim2}
            else:
                pass
            for child in tree.children:
                self.decVariables(child, varsFunc, varsDir,
                                  local_counters, varType, function)

    # Funcion que actualiza el dir de decFunciones con los
    # datos de las decFunciones del programa
    def decFunciones(self, tree):
        """Función que guarda en el directorio de funciones la información de todas las funciones en el programa.

          dec_functions
              : funcion+
              ;

          funcion
              : Function tipo_ret ID '(' params? ')' ';' dec_variables? bloque_est
              ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "funcion":
                functionName = tree.ID().getText()
                if(self.checksFunctionExists(functionName)):
                    msg = "Función '{}' ya declarada".format(functionName)
                    return self.error(tree.ID(), msg)
                else:
                    jsontemp = {}
                    tipo_ret = tree.tipo_ret()

                    if tipo_ret.getText() == "void":
                        returnType = "void"
                    else:
                        returnType = tipo_ret.tipo().getText()
                        globalCounters = self.dirFunciones['global']['counters']
                        offset = self.memory_limits['global'][returnType]
                        functionVarAddr = self.nextRelativeAddr(
                            globalCounters, returnType) + offset
                        self.dirFunciones['global']['vars'][functionName] = {
                            'tipo': returnType, 'dir': functionVarAddr}

                    typeParams = []
                    dirParams = []
                    varsFunc = {}
                    #tempVar = {}
                    varsDir = {}

                    # Local counter of types of vars and params
                    localCounters = {}
                    if tree.params() != None:
                        self.decParamsFun(tree.params(
                        ), varsFunc, varsDir, typeParams, dirParams, functionName, localCounters)
                    if tree.dec_variables() != None:
                        self.decVariables(tree.dec_variables(
                        ), varsFunc, varsDir, localCounters, "", functionName)
                    # self.decVariables(tree.dec_variables(),tempVar,tempVar2,localCounters,"",functionName)

                    #varsFunc = dict(list(varsParams.items()) + list(tempVar.items()))

                    cuadEmpieza = len(self.stackQuads) + 1
                    jsontemp["paramsType"] = typeParams
                    jsontemp["paramsAddr"] = dirParams
                    jsontemp["vars"] = varsFunc
                    jsontemp["varsAddr"] = varsDir
                    jsontemp["returnType"] = returnType
                    jsontemp["startQuad"] = cuadEmpieza
                    jsontemp["counters"] = localCounters
                    self.dirFunciones[functionName] = jsontemp
                    self.evaluarBloqueEst(tree.bloque_est(), functionName)
                    if 'returned' not in self.dirFunciones[functionName] and returnType != 'void':
                        msg = "Función '{}' sin estatuto de retorno".format(functionName)
                        return self.error(tree.ID(), msg)
                    self.dirFunciones[functionName]['tempsCounters'] = self.tempsCounter
                    self.tempsCounter = {}
                    #self.temp = 0
                    self.stackQuads.append(Quadruple('endproc', 0, 0, 0))
            else:
                for child in tree.children:
                    self.decFunciones(child)
        else:
            pass

    def decParamsFun(self, tree, varsFunc, varsDir, typeParams, dirParams, function, local_counters):
        """Función que pone todos los parametros en un diccionario junto con su nombre, dirección, tipo y dimensiones

          params
              : tipo ids (',' params)?
              ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            varsFunc {dict} -- Diccionario donde se guardan las variables con el nombre como key
            varsDir {dict} -- Diccionario donde se guardan las variables con dirección como key
            typeParams {array} -- Arreglo con los tipos de los parametros
            dirParams {array} -- Arreglo con las direcciones de los parametros
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            local_counters {dict} -- Diccionario que te dice cuantas variables hay de cada tipo
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                varName = tree.ids().ID().getText()
                numDim = 0
                for child in tree.ids().children:
                    if not isinstance(child, TerminalNodeImpl):
                        if self.rules[child.getRuleIndex()] == "dimension":
                            numDim += 1
                            if numDim == 1:
                                dim1 = int(child.CTE_INT().getText())
                            elif numDim == 2:
                                dim2 = int(child.CTE_INT().getText())

                if varName in varsFunc or self.checksDuplicateVar(varName):
                    msg = "Var '{}' duplicada".format(varName)
                    return self.error(tree.ids().ID(), msg)

                varType = tree.tipo().getText()
                typeParams.append(varType)
                offset = self.memory_limits['local'][varType]

                if numDim == 0:
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType) + offset
                    varsFunc[varName] = {'tipo': varType, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName}
                elif numDim == 1:
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType, dim1) + offset
                    varsFunc[varName] = {'tipo': varType,
                                         'dim1': dim1, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName, 'dim1': dim1}
                elif numDim == 2:
                    dims = dim1 * dim2
                    varAddr = self.nextRelativeAddr(
                        local_counters, varType, dims) + offset
                    varsFunc[varName] = {
                        'tipo': varType, 'dim1': dim1, 'dim2': dim2, 'dir': varAddr}
                    varsDir[varAddr] = {'nombre': varName,
                                        'dim1': dim1, 'dim2': dim2}
                dirParams.append(varAddr)
            for child in tree.children:
                self.decParamsFun(child, varsFunc, varsDir,
                                  typeParams, dirParams, function, local_counters)
        else:
            pass

    # EXPRESION
    def expresion(self, tree, function):
        """Función padre que crea las pilas para usarse en la evaluación de la expresión

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo

        Returns:
            int -- La última dirección en la pila de operandos
        """
        stacks = {
            'pOperandos': [],
            'pOperadores': [],
            'pTipos': [],
            'pDim': [],
            'pNegativos': []
        }
        self.expresionAux(tree, function, stacks)
        #print("function calling",function)
        # print("stacks",stacks)
        return stacks['pOperandos'][0]

    def expresionAux(self, tree, function, stacks):
        """
        expresion
            : exp
            | expresion op_log expresion
            | exp op_comp exp
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "expresion":
                # print("expresion")
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child, function, stacks)
                        if stacks['pOperadores']:
                            opSymbol = stacks['pOperadores'][-1]
                            if opSymbol == '<' or opSymbol == '>' or opSymbol == '==' or opSymbol == '!=':
                                if len(stacks['pOperandos']) > 1:
                                    stacks['pOperadores'].pop()

                                    rightAddr = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()

                                    leftAddr = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()

                                    resultType = arithmeticCube[opSymbol][rightType][leftType]
                                    # print("tipo res:", resultType)
                                    if resultType == "x":
                                        if opSymbol == '<':
                                            opName = 'menor que'
                                        elif opSymbol == '>':
                                            opName = 'mayor que'
                                        elif opSymbol == '==':
                                            opName = 'igual'
                                        else:
                                            opName = 'no igual'
                                        print(
                                            "Error -> Operación '{}' no posible entre {} y {}".format(opName, leftType, rightType))
                                        exit()

                                    offset = self.memory_limits['temp'][resultType]
                                    tempAddr = self.nextRelativeAddr(
                                        self.tempsCounter, resultType) + offset

                                    self.stackQuads.append(
                                        Quadruple(opSymbol, leftAddr, rightAddr, tempAddr))

                                    stacks['pOperandos'].append(tempAddr)
                                    stacks['pTipos'].append(resultType)

                                else:
                                    pass

                            else:
                                pass
                    elif ruleChild == "op_log":
                        opSymbol = child.getText()
                        stacks['pOperadores'].append(opSymbol)
                    elif ruleChild == "op_comp":
                        opSymbol = child.getText()
                        stacks['pOperadores'].append(opSymbol)
                    elif ruleChild == "expresion":
                        self.expresionAux(child, function, stacks)
                        if stacks['pOperadores']:
                            opSymbol = stacks['pOperadores'][-1]
                            if opSymbol == '||' or opSymbol == '&':
                                if len(stacks['pOperandos']) > 1:
                                    stacks['pOperadores'].pop()

                                    rightAddr = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()

                                    leftAddr = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()

                                    resultType = arithmeticCube[opSymbol][rightType][leftType]

                                    if resultType == "x":
                                        opName = 'AND' if opSymbol == '&' else 'OR'
                                        print(
                                            "Error -> Operación '{}' no posible entre {} y {}".format(opName, leftType, rightType))
                                        exit()

                                    offset = self.memory_limits['temp'][resultType]
                                    tempAddr = self.nextRelativeAddr(
                                        self.tempsCounter, resultType) + offset

                                    self.stackQuads.append(
                                        Quadruple(opSymbol, leftAddr, rightAddr, tempAddr))

                                    stacks['pOperandos'].append(tempAddr)
                                    stacks['pTipos'].append(resultType)

                                else:
                                    pass

                            else:
                                pass
        else:
            pass

    def expAux(self, tree, function, stacks):
        """
        exp
            : term
            | term op_arit exp
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "exp":
                # print("exp")
                # print(len(tree.children))
                # rules = []
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "exp":
                        self.expAux(child, function, stacks)
                    elif ruleChild == "op_arit":
                        opSymbol = child.getText()
                        stacks['pOperadores'].append(opSymbol)
                        # print("encontre + o -")
                    elif ruleChild == "term":
                        self.termAux(child, function, stacks)

                        if stacks['pOperadores']:
                            opSymbol = stacks['pOperadores'][-1]
                            if opSymbol == '+' or opSymbol == '-':
                                if len(stacks['pOperandos']) > 1:
                                    stacks['pOperadores'].pop()
                                    opName = 'suma' if opSymbol == '+' else 'resta'

                                    rightAddr = stacks['pOperandos'].pop()
                                    rightType = stacks['pTipos'].pop()

                                    leftAddr = stacks['pOperandos'].pop()
                                    leftType = stacks['pTipos'].pop()
                                    resultType = arithmeticCube[opSymbol][rightType][leftType]

                                    if resultType == "x":
                                        print(
                                            "Error -> Operación '{}' no posible entre {} y {}".format(opName, leftType, rightType))
                                        exit()

                                    leftDim1 = self.getDimOfAddr(
                                        leftAddr, function, 1)
                                    leftDim2 = self.getDimOfAddr(
                                        leftAddr, function, 2)

                                    rightDim1 = self.getDimOfAddr(
                                        rightAddr, function, 1)
                                    rightDim2 = self.getDimOfAddr(
                                        rightAddr, function, 2)

                                    if leftDim1 != False and (leftDim1 != rightDim1 or leftDim2 != rightDim2):
                                        if rightDim1 == False:
                                            print("f1")
                                            print(
                                                "Error -> Operación '{}' no posible entre un arreglo y una constante".format(opName))
                                            exit()
                                        else:
                                            print(
                                                "Error -> Operación '{}' no posible entre diferentes tamaños de arreglos".format(opName))
                                            exit()
                                    if rightDim1 != False and leftDim1 == False:
                                        if leftAddr < 55000 and rightAddr < 55000:
                                            print(
                                                "Error -> Operación '{}' no posible entre un arreglo y una constante".format(opName))
                                            exit()

                                    if leftDim1 != False and leftDim1 == rightDim1 and leftDim2 == rightDim2 or leftAddr >= 55000:
                                        offset = self.memory_limits['temp']['dirArreglo']
                                        tempAddr = self.nextRelativeAddr(self.ctesCounter, 'dir') + offset

                                        self.memory['temp'][function] = {}
                                        self.memory['temp'][function][tempAddr] = {'tipo': opSymbol, 'dim1':leftDim1, 'dim2':leftDim2}

                                        opArray = "{}Arreglos".format(opSymbol)

                                        self.stackQuads.append(
                                            Quadruple(opArray, leftAddr, rightAddr, tempAddr))
                                        self.stackQuads.append(
                                            Quadruple('dimensiones', 0, rightDim1, rightDim2))
                                    else:
                                        offset = self.memory_limits['temp'][resultType]
                                        tempAddr = self.nextRelativeAddr(self.tempsCounter, resultType) + offset
                                        self.stackQuads.append(Quadruple(opSymbol, leftAddr, rightAddr, tempAddr))

                                    stacks['pOperandos'].append(tempAddr)
                                    stacks['pTipos'].append(resultType)
                                    # print("pilitas",stacks['pTipos'])
                            else:
                                pass
        else:
            pass

    def termAux(self, tree, function, stacks):
        """
        term
            : factor
            | factor op_prod term
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "term":
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    # rules.append(ruleChild)
                    if ruleChild == "factor":
                        self.factorAux(child, function, stacks)

                        if stacks['pOperadores'] and len(stacks['pOperandos']) > 1:
                            opSymbol = stacks['pOperadores'][-1]
                            if opSymbol == '*' or opSymbol == '/':
                                stacks['pOperadores'].pop()
                                opName = 'multiplicación' if opSymbol == '*' else 'división'
                                rightAddr = stacks['pOperandos'].pop()
                                rightType = stacks['pTipos'].pop()

                                leftAddr = stacks['pOperandos'].pop()
                                leftType = stacks['pTipos'].pop()

                                resultType = arithmeticCube[opSymbol][rightType][leftType]

                                if resultType == "x":
                                    print(
                                        "Error -> Operación '{}' no posible entre {} y {}".format(opName, leftType, rightType))
                                    exit()

                                leftDim1 = self.getDimOfAddr(
                                    leftAddr, function, 1)
                                leftDim2 = self.getDimOfAddr(
                                    leftAddr, function, 2)

                                rightDim1 = self.getDimOfAddr(
                                    rightAddr, function, 1)
                                rightDim2 = self.getDimOfAddr(
                                    rightAddr, function, 2)
                                
                                if leftDim1 != False and (leftDim1 != rightDim1 or leftDim2 != rightDim2):
                                    if rightDim1 == False:
                                        print(
                                            "Error -> Operación '{}' no posible entre un arreglo y una constante".format(opName))
                                        exit()
                                    else:
                                        print(
                                            "Error -> Operación '{}' no posible entre diferentes tamaños de arreglos".format(opName))
                                        exit()

                                if rightDim1 != False and leftDim1 == False:
                                    if leftAddr < 55000 and rightAddr < 55000:
                                        print(
                                            "Error -> Operación '{}' no posible entre un arreglo y una constante".format(opName))
                                        exit()

                                if leftDim1 != False and leftDim1 == rightDim1 and leftDim2 == rightDim2 or leftAddr >= 55000:
                                    offset = self.memory_limits['temp']['dirArreglo']
                                    tempAddr = self.nextRelativeAddr(
                                        self.ctesCounter, 'dir') + offset

                                    opArray = "{}Arreglos".format(opSymbol)

                                    self.stackQuads.append(
                                        Quadruple(opArray, leftAddr, rightAddr, tempAddr))
                                    self.stackQuads.append(
                                        Quadruple('dimensiones', 0, rightDim1, rightDim2))
                                else:
                                    offset = self.memory_limits['temp'][resultType]
                                    tempAddr = self.nextRelativeAddr(
                                        self.tempsCounter, resultType) + offset
                                    self.stackQuads.append(
                                        Quadruple(opSymbol, leftAddr, rightAddr, tempAddr))

                                stacks['pOperandos'].append(tempAddr)
                                stacks['pTipos'].append(resultType)
                                # print("pila",stacks['pTipos'])
                                # print(res)
                                # print("mayor a dos"
                            else:
                                pass
                    elif ruleChild == "op_prod":
                        opSymbol = child.getText()
                        stacks['pOperadores'].append(opSymbol)
                    elif ruleChild == "term":
                        self.termAux(child, function, stacks)
        else:
            pass

    def factorAux(self, tree, function, stacks):
        """
        factor
          : var op_esp?
          | (op_arit)? var_cte
          | llamada
          | exp_par
          ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..

        Returns:
            [type] -- [description]
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "factor":
                for child in tree.children:
                    ruleChild = self.rules[child.getRuleIndex()]
                    if ruleChild == "var":
                        self.varAux(child, function, stacks)
                    elif ruleChild == "var_cte":
                        self.varcteAux(child, function, stacks)
                    elif ruleChild == "op_esp":
                        opSymbol = child.getText()
                        topAddr = stacks['pOperandos'][-1]

                        dim1 = self.getDimOfAddr(topAddr, function, 1)
                        dim2 = self.getDimOfAddr(topAddr, function, 2)

                        if opSymbol == '?':
                            opName = "inversa"
                        elif opSymbol == '$':
                            opName = "determinante"
                        elif opSymbol == '%':
                            opName = "promedio"
                        elif opSymbol == '@':
                            opName = "suma"
                        elif opSymbol == '~':
                            opName = "minimo"
                        elif opSymbol == '#':
                            opName = "maximo"
                        else:
                            opName = "transpuesta"

                        if opSymbol == '!' or opSymbol == '?':
                            # print("aca")
                            offset = self.memory_limits['temp']['dirArreglo']
                            tempAddr = self.nextRelativeAddr(
                                self.ctesCounter, 'dir') + offset
                            self.stackQuads.append(
                                Quadruple(opSymbol, topAddr, 0, tempAddr))
                        else:
                            tipo = stacks['pTipos'][-1]
                            offset = self.memory_limits['temp'][tipo]
                            tempAddr = self.nextRelativeAddr(
                                self.ctesCounter, tipo) + offset
                            self.stackQuads.append(
                                Quadruple(opSymbol, topAddr, 0, tempAddr))
                            # print("aqui")

                        stacks['pOperandos'].pop()
                        stacks['pOperandos'].append(tempAddr)

                        if opSymbol == '?' or opSymbol == '$':
                            if dim1 != dim2:
                                varName = self.getNameOfAddr(topAddr, function)
                                msg = "No se puede calcular la {} de '{}' si no es cuadrada.".format(
                                    opName, varName)
                                return self.error(child.ESP(), msg)

                        self.stackQuads.append(
                            Quadruple('dimensiones', 0, dim1, dim2))

                    elif ruleChild == "op_arit":
                        stacks['pNegativos'].append(child.getText())

                    elif ruleChild == "exp_par":
                        self.parentesisAux(child, function, stacks)
                    elif ruleChild == "llamada":
                        self.est_llamada_est(child, function, stacks,True)
        else:
            pass

    def parentesisAux(self, tree, function, stacks):
        """
        exp_par
            : par_empieza expresion par_termina
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
        """
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
                        self.expresionAux(child, function, stacks)
        else:
            pass

    def varAux(self, tree, function, stacks, brackets=False):
        """
        var
            : ID dim? dim?
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..

        Keyword Arguments:
            brackets {bool} -- [description] (default: {False})

        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var":
                varName = tree.ID().getText()
                # print("Var : " , varName)
                # print("function::",function)
                varType = self.getTypeOfVariable(varName, function)

                #print("var aux: nombre, varType: ",varName,varType)

                if varType == False:
                    msg = "No se encontró la var '{}'".format(varName)
                    return self.error(tree.ID(), msg)

                stacks['pTipos'].append(varType)
                varAddr = self.getAddrOfVariable(varName, function)
                hasDims = self.getDimOfAddr(varAddr, function, 1)
                # print(varAddr)
                # print(varAddr)
                stacks['pOperandos'].append(varAddr)

                # dims = []
                # numdims = len(tree.children) -1
                # print(numdims)
                if hasDims != False:
                    currentAddr = ""
                    currentType = ""
                    currentDim = 1
                    for child in tree.children:
                        if not isinstance(child, TerminalNodeImpl):
                            ruleChild = self.rules[child.getRuleIndex()]
                            # rules.append(ruleChild)
                            if ruleChild == "dim":
                                brackets = True
                                if currentDim == 1:
                                    currentAddr = stacks['pOperandos'].pop()
                                    currentType = stacks['pTipos'].pop()
                                    stacks['pOperadores'].append("$")

                                self.dimAux(child, function, currentDim,
                                            stacks, currentAddr, currentType)
                                currentDim += 1
        else:
            pass

    def dimAux(self, tree, function, dim, stacks, id, type):
        """Función que genera los cuadruplos para una dimension de la indexacion de una variable

        dim
            : '[' expresion ']'
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            dim {int} -- Número de dimension actual a evaluar
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
            id {int} -- Dirección base del arreglo indexado
            type {string} -- Tipo del arreglo indexado
        """
        # print("entra")
        stacks2 = {
            'pOperandos': [],
            'pOperadores': [],
            'pTipos': [],
            'pDim': [],
            'pNegativos': []
        }
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                ruleChild = self.rules[child.getRuleIndex()]
                # rules.append(ruleChild)
                if ruleChild == "expresion":
                    # print(stacks2['pOperandos'])
                    self.expresionAux(child, function, stacks2)

        if id in self.memory['ctes']:
            baseAddr = self.memory['ctes'][id]['dir']
        else:
            offset = self.memory_limits['ctes']['int']
            baseAddr = self.nextRelativeAddr(self.ctesCounter, 'int') + offset
            self.memory['ctes'][id] = {'tipo': 'int', 'dir': baseAddr}
            self.memory['ctesDir'][baseAddr] = id

        if dim == 1:
            resExp = stacks2['pOperandos'][-1]
            lsdim1 = self.getDimOfAddr(id, function, 1)
            lsdim2 = self.getDimOfAddr(id, function, 2)

            self.stackQuads.append(
                Quadruple('verify', resExp, baseAddr, lsdim1))

            if lsdim2 == False:
                offset = self.memory_limits['temp']['dir']
                addr = self.nextRelativeAddr(self.ctesCounter, 'dir') + offset
                self.stackQuads.append(Quadruple('+', resExp, baseAddr, addr))
                stacks['pOperandos'].append(addr)
                stacks['pTipos'].append(type)
                stacks['pOperadores'].pop()
            else:
                if lsdim2 in self.memory['ctes']:
                    lsdim2addr = self.memory['ctes'][lsdim2]['dir']
                else:
                    offset = self.memory_limits['ctes']['int']
                    lsdim2addr = self.nextRelativeAddr(
                        self.ctesCounter, 'int') + offset
                    self.memory['ctes'][lsdim2] = {
                        'tipo': 'int', 'dir': lsdim2addr}
                    self.memory['ctesDir'][lsdim2addr] = lsdim2
                offset = self.memory_limits['temp']['int']
                addr = self.nextRelativeAddr(self.ctesCounter, 'int') + offset
                self.stackQuads.append(
                    Quadruple('*', resExp, lsdim2addr, addr))
                stacks['pDim'].append(addr)
                # print(stacks['pDim'])
        elif dim == 2:
            resExp = stacks2['pOperandos'][-1]
            lsdim2 = self.getDimOfAddr(id, function, 2)
            # print("dim",id, self.getDimOfAddr(5000,function,2))
            # print(stacks['pDim'])
            temp1 = stacks['pDim'].pop()
            self.stackQuads.append(
                Quadruple('verify', resExp, baseAddr, lsdim2))

            offset = self.memory_limits['temp']['int']
            addr1 = self.nextRelativeAddr(self.ctesCounter, 'int') + offset
            self.stackQuads.append(Quadruple('+', resExp, temp1, addr1))

            offset = self.memory_limits['temp']['dir']
            addr2 = self.nextRelativeAddr(self.ctesCounter, 'dir') + offset
            self.stackQuads.append(Quadruple('+', addr1, baseAddr, addr2))

            stacks['pOperandos'].append(addr2)
            stacks['pTipos'].append(type)
            # print("addr2",addr2,stacks['pOperandos'])
            # stacks['pOperadores'].pop()

        # traverse(tree,self.rules)

    def varcteAux(self, tree, function, stacks):
        """
        var_cte
            : var
            | CTE_INT
            | CTE_FLOAT
            | CTE_CHAR
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "var_cte":
                for child in tree.children:
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "var":
                            self.varAux(child, function, stacks)
                    else:
                        if stacks['pNegativos']:
                            operator = stacks['pNegativos'].pop()
                            constant = operator + tree.getText()
                        else:
                            constant = tree.getText()
                        if constant[0] == "'":
                            constantType = "char"
                            constant = constant[1]
                            # print("encontre un char")
                        elif constant.find('.') != -1:
                            constantType = "float"
                        else:
                            constantType = "int"

                        if constant in self.memory['ctes']:
                            constantAddr = self.memory['ctes'][constant]['dir']
                        else:
                            offset = self.memory_limits['ctes'][constantType]
                            constantAddr = self.nextRelativeAddr(
                                self.ctesCounter, constantType) + offset
                            self.memory['ctes'][constant] = {
                                'tipo': constantType, 'dir': constantAddr}
                            self.memory['ctesDir'][constantAddr] = constant

                        stacks['pTipos'].append(constantType)
                        # diana
                        stacks['pOperandos'].append(constantAddr)

        else:
            pass

    # ESTATUTOS

    def evaluarBloqueEst(self, tree, function):
        """Función que delega y detecta que tipo de estatuto son dentro de un bloque y los manda
        a sus respectivas funciones

        estatuto
            : asignacion_est
            | retorno
            | lectura
            | decision
            | repeticion
            | llamada_est
            | escritura
            ;
        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
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
                                self.est_retorno(child2, function)
                            elif rule == "lectura":
                                # print("*** Lee ***")
                                self.est_lectura(child2, function)
                            elif rule == "asignacion_est":
                                # print("*** asignacion ***")
                                self.est_asignacion(
                                    child2.asignacion(), function)
                            elif rule == "decision":
                                # print("*** Decision ***")
                                self.est_decision(child2, function)
                            elif rule == "repeticion":
                                # print("*** Repeticion ***")
                                self.est_repeticion(child2, function)
                            elif rule == "llamada_est":
                                # print("*** Llamada ***")
                                self.est_llamada_est(
                                    child2.llamada(), function)
                            elif rule == "escritura":
                                # print("*** Print ***")
                                self.est_escritura(child2, function)

        else:
            pass

    def est_retorno(self, tree, function):
        """Función que genera los cuadruplos para el return

        retorno
            : Regresa '(' expresion ')' ';'
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo

        """
        self.dirFunciones[function]['returned'] = True
        if function == "global":
            msg = "La función main no tiene retorno"
            return self.error(tree.Regresa(), msg)
        elif self.dirFunciones[function]['returnType'] == "void":
            msg = "Retorno en función '{}' de tipo void".format(function)
            return self.error(tree.Regresa(), msg)

        addrExp = self.expresion(tree.expresion(), function)
        typeExp = self.getTypeOfAddr(addrExp)
        addrVar = self.getAddrOfVariable(function, 'global')
        addrDim1 = self.getDimOfAddr(addrExp, function, 1)
        addrDim2 = self.getDimOfAddr(addrExp, function, 2)
        if typeExp != self.dirFunciones[function]['returnType']:
            msg = "Tipo de retorno en '{}' no corresponde al tipo declarado".format(function)
            return self.error(tree.Regresa(), msg)
        if addrDim1 != False:
            self.dirFunciones['global']['vars'][function]['array'] = True
            self.stackQuads.append(
                Quadruple('ret', addrExp, addrVar, 'arreglo'))
            self.stackQuads.append(
                Quadruple('dimensiones', 0, addrDim1, addrDim2))

        else:
            self.stackQuads.append(Quadruple('ret', addrExp, addrVar, 0))

    def est_lectura(self, tree, function):
        """Función que genera los cuadruplos para la lectura
        lectura
            : Lee '(' lista_vars ')' ';'
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        stacks = {
            'pOperandos': [],
            'pOperadores': [],
            'pTipos': [],
            'pDim': [],
            'pNegativos': []
        }
        self.est_lectura_aux(tree.lista_vars(), stacks, function)
        #print("Res in est lectura:",res)
        for var in stacks['pOperandos']:
            self.stackQuads.append(Quadruple('lee', var, 0, 0))
        # print(res)

    def est_lectura_aux(self, tree, stacks, function):
        """Función que almacena todos los operandos de un estatuto de lectura
        en la pila de operandos

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            stacks {dict} -- Diccionario de pilas con info de los operadores, etc..
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                regla = self.rules[child.getRuleIndex()]
                if regla == "var":
                    varName = child.ID().getText()
                    # print("Var : " , varName)
                    # print("function::",function)
                    varType = self.getTypeOfVariable(varName, function)

                    #print("var aux: nombre, varType: ",varName,varType)

                    if varType == False:
                        msg = "No se encontró la var '{}'".format(varName)
                        return self.error(child.ID(), msg)

                    stacks['pTipos'].append(varType)
                    varAddr = self.getAddrOfVariable(varName, function)
                    hasDims = self.getDimOfAddr(varAddr, function, 1)
                    # print(varAddr)
                    # print(varAddr)
                    stacks['pOperandos'].append(varAddr)

                    # dims = []
                    # numdims = len(tree.children) -1
                    # print(numdims)
                    if hasDims != False:
                        currentAddr = ""
                        currentType = ""
                        currentDim = 0
                        for child2 in child.children:
                            if not isinstance(child2, TerminalNodeImpl):
                                ruleChild = self.rules[child2.getRuleIndex()]
                                # rules.append(ruleChild)
                                if ruleChild == "dim":
                                    brackets = True
                                    currentDim += 1
                                    if currentDim == 1:
                                        currentAddr = stacks['pOperandos'].pop(
                                        )
                                        currentType = stacks['pTipos'].pop()
                                        stacks['pOperadores'].append("$")

                                    self.dimAux(
                                        child2, function, currentDim, stacks, currentAddr, currentType)
                        if currentDim == 0:
                            msg = "No se puede leer toda la matriz '{}'".format(
                                varName)
                            return self.error(child.ID(), msg)
                    # print(child.ID().getText())
                elif regla == "lista_vars":
                    self.est_lectura_aux(child, stacks, function)
                    # traverse(child,self.rules)
                # print(regla)

    def est_asignacion(self, tree, function):
        """Función que genera los cuadruplos para la asignacion ya sea de:
           una expresion a una variable, una variable a otra, un arreglo a otro
           o una expresion/variable a una posicion del arreglo/matriz

           asignacion
            : (var '=')+ expresion
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        # traverse(tree,self.rules)
        # print(len(tree.children))
        # print(tree.getText())
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "asignacion":
                # print("asign")
                pilas = {
                    'pOperandos': [],
                    'pOperadores': [],
                    'pTipos': [],
                    'pDim': [],
                    'tieneBrackets': [],
                    'pNegativos': []
                }
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        # rules.append(ruleChild)
                        if ruleChild == "var":
                            varName = child.ID().getText()
                            varType = self.getTypeOfVariable(varName, function)
                            varAddr = self.getAddrOfVariable(varName, function)

                            if not varType or not varAddr:
                                msg = "No se encontró la var '{}'".format(
                                    varName)
                                return self.error(child.ID(), msg)

                            brackets = False
                            tieneDim = self.getDimOfAddr(varAddr, function, 1)
                            if tieneDim != False:
                                currentDim = 1
                                for child2 in child.children:
                                    if not isinstance(child2, TerminalNodeImpl):
                                        ruleChild = self.rules[child2.getRuleIndex(
                                        )]
                                        # rules.append(ruleChild)
                                        if ruleChild == "dim":
                                            if currentDim == 1:
                                                brackets = True
                                                pilas['tieneBrackets'].append(
                                                    True)
                                                # pilas['pOperandos'].append(varAddr)
                                                # print("flag 1", pilas['pOperandos'])
                                                pilas['pTipos'].append(varType)
                                                pilas['pOperadores'].append(
                                                    "$")
                                            self.dimAux(
                                                child2, function, currentDim, pilas, varAddr, varType)
                                            # print("flag 3", pilas['pOperandos'])
                                            currentDim += 1

                            # if function == "main":
                            #     function = "global"
                            c = child.ID()
                            if len(pilas['pOperandos']) > 1:
                                tipo_anterior = pilas['pTipos'][-1]
                                
                                if varType != tipo_anterior:
                                    msg = "Asignación invalida entre '{}' y '{}'.".format(
                                        varName, pilas['pTipos'][-1], varType)
                                    return self.error(c, msg)
                            if tieneDim == False or brackets == False:
                                pilas['tieneBrackets'].append(False)
                                pilas['pOperandos'].append(varAddr)
                                # print("flag 2", pilas['pOperandos'])
                                pilas['pTipos'].append(varType)

                        elif ruleChild == "expresion":
                            # print("exp")
                            exp = self.expresion(child, function)
                            tipo_exp = self.getTypeOfAddr(exp)

                            topTipos = pilas['pTipos'][-1]
                            # topOperandos = pilas['pOperandos'][-1]
                            if exp > 50000:
                                pilas['tieneBrackets'].append(True)
                            else:
                                pilas['tieneBrackets'].append(False)
                            # topName = self.getNameOfAddr(topOperandos,function)
                            if not exp >= 55000 and tipo_exp != topTipos:
                                msg = "Asignación invalida entre '{}' y '{}'.".format(
                                    topTipos, tipo_exp)
                                return self.error(c, msg)

                # print(pilas['pOperandos'])
                # print("bracksss", pilas['tieneBrackets'])
                # AGREGAR ALGO PARA SABER SI varAddr Y EXP TENIAN [][] O NO
                leftAddr = pilas['pOperandos'][-1]
                leftType = pilas['pTipos'].pop()
                bracketsDer = pilas['tieneBrackets'].pop()
                bracketsIzq = pilas['tieneBrackets'][-1]
                leftDim1 = self.getDimOfAddr(varAddr, function, 1)
                leftDim2 = self.getDimOfAddr(varAddr, function, 2)
                rightDim1 = self.getDimOfAddr(exp, function, 1)
                rightDim2 = self.getDimOfAddr(exp, function, 2)
                # print("en",leftAddr,exp,rightDim1,rightDim2)
                # print("bra",bracketsIzq,bracketsDer)
                if exp >= 55000 and not bracketsIzq:
                    if function in self.memory['temp']:
                        if exp in self.memory['temp'][function]:
                            dataExp = self.memory['temp'][function][exp]
                            expDim1 = dataExp['dim1']
                            expDim2 = dataExp['dim2']
                    
                            if expDim1 != leftDim1 or expDim2 != leftDim2:
                                msg = "No se puede asignar porque sus dimensiones no corresponden "
                                return self.error(c, msg)

                    self.stackQuads.append(
                        Quadruple('=', exp, leftAddr, 'arreglo'))
                    self.stackQuads.append(
                        Quadruple('dimensiones', 0, leftDim1, leftDim2))
                elif bracketsIzq and not bracketsDer:
                    self.stackQuads.append(
                        Quadruple('=', exp, leftAddr, 'arrSingle'))
                    # pilas['pOperandos'].pop()
                elif not bracketsIzq and not bracketsDer:
                    # n = self.getNameOfAddr(leftAddr,function)
                    # print(n,leftDim1)

                    if leftDim1 != False:
                        if rightDim1 != False:
                            if (leftDim1 == rightDim1) and (leftDim2 == rightDim2):
                                self.stackQuads.append(
                                Quadruple('=', exp, leftAddr, 'arreglo'))
                                self.stackQuads.append(
                                    Quadruple('dimensiones', 0, leftDim1, leftDim2))
                            else:
                                msg = "Arreglos de tamaños incompatibles"
                                # print(msg)
                                return self.error(c, msg)
                        if (leftDim1 == rightDim1) and (leftDim2 == rightDim2):
                            self.stackQuads.append(
                                Quadruple('=', exp, leftAddr, 'arreglo'))
                            self.stackQuads.append(
                                Quadruple('dimensiones', 0, leftDim1, leftDim2))
                        else:
                            self.stackQuads.append(
                                Quadruple('=', exp, leftAddr, 'arrWhole'))
                            self.stackQuads.append(
                                Quadruple('dimensiones', 0, leftDim1, leftDim2))
                    else:
                        self.stackQuads.append(
                            Quadruple('=', exp, leftAddr, 0))
                elif not bracketsIzq and bracketsDer:
                    self.stackQuads.append(Quadruple('=', exp, leftAddr, 0))
                elif bracketsIzq != bracketsDer and exp > 50000:
                    msg = "No se puede asignar un arreglo a un {}.".format(
                        leftType)
                    return self.error(c, msg)
                elif bracketsIzq and bracketsDer:
                    self.stackQuads.append(
                        Quadruple('=', exp, leftAddr, 'arrSingle'))
                else:
                    # n = self.getNameOfAddr(leftAddr,function)
                    # print(n)
                    # if bracketsIzq != bracketsDer and exp > 50000:
                    #     msg = "No se puede asignar un arreglo a un {}.".format(leftType)
                    #     return self.error(c,msg)
                    if exp >= 50000 and leftDim1 != False:
                        self.stackQuads.append(
                            Quadruple('=', exp, leftAddr, 'arreglo'))
                        self.stackQuads.append(
                            Quadruple('dimensiones', 0, leftDim1, leftDim2))
                        # print("si entre")
                    else:
                        if leftDim1 != False and rightDim1 != False:
                            if (leftDim1 == rightDim1) and (leftDim2 == rightDim2):
                                self.stackQuads.append(
                                    Quadruple('=', exp, leftAddr, 'arreglo'))
                                self.stackQuads.append(
                                    Quadruple('dimensiones', 0, leftDim1, leftDim2))
                            else:
                                leftName = self.getNameOfAddr(
                                    varAddr, function)
                                rightName = self.getNameOfAddr(exp, function)
                                msg = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(
                                    leftName, rightName)
                                # print(msg)
                                return self.error(c, msg)
                        else:
                            self.stackQuads.append(
                                Quadruple('=', exp, leftAddr, 0))
                lenPila = len(pilas['pOperandos']) - 1
                # print(lenPila)
                # print(pilas['pOperandos'],"actual", len(self.stackQuads)+1)
                # print(pilas['tieneBrackets'])
                if lenPila >= 1:
                    for i in range(lenPila+1):
                        # print("bracks adentro for",i, pilas['tieneBrackets'])
                        bracketsDer = bracketsIzq
                        bracketsIzq = pilas['tieneBrackets'].pop()
                        # print("for", i , pilas['pOperandos'])
                        # print("entra for")
                        # leftAddr = pilas['pOperandos'].pop()
                        # leftDim1 = self.getDimOfAddr(leftAddr,function,1)
                        # leftDim2 = self.getDimOfAddr(leftAddr,function,2)

                        rightAddr = pilas['pOperandos'].pop()
                        rightDim1 = self.getDimOfAddr(rightAddr, function, 1)
                        rightDim2 = self.getDimOfAddr(rightAddr, function, 2)
                        if bracketsIzq and not bracketsDer:
                            self.stackQuads.append(
                                Quadruple('=', exp, rightAddr, 'arrSingle'))
                            pilas['pOperandos'].pop()
                        elif not bracketsIzq and not bracketsDer:
                            # n = self.getNameOfAddr(leftAddr,function)
                            # print(n,leftDim1)
                            if leftDim1 != False:
                                if rightDim1 != False:
                                    if (leftDim1 == rightDim1) and (leftDim2 == rightDim2):
                                        self.stackQuads.append(
                                        Quadruple('=', exp, leftAddr, 'arreglo'))
                                        self.stackQuads.append(
                                            Quadruple('dimensiones', 0, leftDim1, leftDim2))
                                    else:
                                        msg = "Arreglos de tamaños incompatibles"
                                        # print(msg)
                                        return self.error(c, msg)
                                self.stackQuads.append(
                                    Quadruple('=', leftAddr, rightAddr, 'arrWhole'))
                                self.stackQuads.append(
                                    Quadruple('dimensiones', 0, rightDim1, rightDim2))
                            else:
                                self.stackQuads.append(
                                    Quadruple('=', exp, rightAddr, 0))
                        elif not bracketsIzq and bracketsDer:
                            self.stackQuads.append(
                                Quadruple('=', exp, rightAddr, 0))
                        elif bracketsIzq != bracketsDer and exp > 50000:
                            msg = "No se puede asignar un arreglo a un {}.".format(
                                leftType)
                            return self.error(c, msg)
                        elif bracketsIzq and not bracketsDer:
                            self.stackQuads.append(
                                Quadruple('=', exp, leftAddr, 'arrSingle'))
                        else:
                            if leftDim1 != False and rightDim1 != False:
                                if (leftDim1 == rightDim1) and (leftDim2 == rightDim2):
                                    self.stackQuads.append(
                                        Quadruple('=', leftAddr, rightAddr, 'arreglo'))
                                    self.stackQuads.append(
                                        Quadruple('dimensiones', 0, leftDim1, leftDim2))
                                else:
                                    leftName = self.getNameOfAddr(
                                        leftAddr, function)
                                    rightName = self.getNameOfAddr(
                                        rightAddr, function)
                                    msg = "Los arreglos '{}' y '{}' no son del mismo tamaño".format(
                                        leftName, rightName)
                                    # print(msg)
                                    return self.error(c, msg)
                            else:
                                self.stackQuads.append(
                                    Quadruple('=', exp, rightAddr, 0))
                # print(pilas['pTipos'])

        else:
            pass
        # traverse(codigo,self.rules)
        # chec var existe en function
        # llama al exp y asigna el valor

    def est_decision(self, tree, function):
        """Función que genera los cuadruplos del print ya sea con else o sin else

        decision
            : Si '(' expresion ')' Entonces bloque_est (Sino bloque_est)?
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
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
                            var = self.expresion(child, function)
                            #print("quad: gotof varAnterior pos")
                            self.stackQuads.append(
                                Quadruple('gotof', var, 'pos', 0))
                            numGotof = len(self.stackQuads)
                            # pSaltos.append(len(self.stackQuads)-1)
                        elif ruleChild == "bloque_est":
                            if primerBloque:
                                # print("Entonces: ")
                                self.evaluarBloqueEst(child, function)
                                #print("quad: goto pos")

                                # pSaltos.append(len(self.stackQuads)-1)
                            else:

                                hayElse = True

                                self.stackQuads.append(
                                    Quadruple('goto', 'pos', 0, 0))
                                numGoto = len(self.stackQuads)
                                # false = pSaltos.pop()
                                # pSaltos.append(len(self.stackQuads)-1)
                                # print("Si no: ")
                                numElse = len(self.stackQuads)
                                self.evaluarBloqueEst(child, function)

                            primerBloque = False

                            # print("exp")
                numEnd = len(self.stackQuads)
                if hayElse:
                    self.stackQuads[numGotof -
                                    1] = Quadruple('gotof', var, numElse+1, 0)
                    self.stackQuads[numGoto -
                                    1] = Quadruple('goto', numEnd+1, 0, 0)

                else:
                    self.stackQuads[numGotof -
                                    1] = Quadruple('gotof', var, numEnd+1, 0)

        else:
            pass
        # traverse(codigo,self.rules)
        # chec var existe en function
        # llama al exp y asigna el valor

    def est_repeticion(self, tree, function):
        """Función que delega a la función de condicional o no condicional dependiendo del caso.

        repeticion
            : condicional
            | no_condicional
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "repeticion":
                for child in tree.children:
                    rule = self.rules[child.getRuleIndex()]
                    if rule == "condicional":
                        self.est_condicional(child, function)
                    elif rule == "no_condicional":
                        self.est_nocondicional(child, function)

    def est_condicional(self, tree, function):
        """Función que genera los cuadruplos del while

        condicional
            : Mientras expresion Haz bloque_est
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        pSaltos = []
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "condicional":
                for child in tree.children:
                    # print("hijo")
                    if not isinstance(child, TerminalNodeImpl):
                        ruleChild = self.rules[child.getRuleIndex()]
                        if ruleChild == "expresion":
                            pSaltos.append(len(self.stackQuads))
                            var = self.expresion(child, function)
                            #print("var if true or false:", var)
                            #print("quad: gotof varAnterior pos")

                            self.stackQuads.append(
                                Quadruple('gotof', var, 'pos', 0))
                            pSaltos.append(len(self.stackQuads))
                        elif ruleChild == "bloque_est":
                            self.evaluarBloqueEst(child, function)
                            self.stackQuads.append(
                                Quadruple('goto', 'pos', 0, 0))
                            pSaltos.append(len(self.stackQuads))

                self.stackQuads[pSaltos[1] -
                                1] = Quadruple('gotof', var, pSaltos[2]+1, 0)
                self.stackQuads[pSaltos[2] -
                                1] = Quadruple('goto', pSaltos[0]+1, 0, 0)

        else:
            pass

    def est_nocondicional(self, tree, function):
        """Función que genera los cuadruplos del for

        no_condicional
            : Desde asignacion Hasta expresion Hacer bloque_est
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
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
                            self.est_asignacion(child, function)
                            for child2 in child.children:
                                if not isinstance(child2, TerminalNodeImpl):
                                    if self.rules[child2.getRuleIndex()] == 'var':
                                        var = child2.getText()
                                        addrVar = self.getAddrOfVariable(
                                            var, function)
                                        # print(child2.getText())
                        elif ruleChild == "expresion":
                            # print("Expresion")
                            # pSaltos.append(len(self.stackQuads)+1)
                            exp = self.expresion(child, function)
                            # self.stackQuads.append(Quadruple('>',addr,exp,0))
                            # self.stackQuads.append(Quadruple('gotov','final',0,0))

                            local_counters = self.dirFunciones[function]['counters']
                            offset = self.memory_limits['temp']['bool']
                            addrTemp = self.nextRelativeAddr(
                                local_counters, 'bool') + offset

                            self.stackQuads.append(
                                Quadruple('==', addrVar, exp, addrTemp))
                            pSaltos.append(len(self.stackQuads))
                            self.stackQuads.append(
                                Quadruple('gotov', addrTemp, 'addr', 0))
                            pSaltos.append(len(self.stackQuads))
                        elif ruleChild == "bloque_est":
                            if 1 in self.memory['ctes']:
                                addrUno = self.memory['ctes'][1]['dir']
                            else:
                                offset = self.memory_limits['ctes']['int']
                                addrUno = self.nextRelativeAddr(
                                    self.ctesCounter, 'int') + offset
                                self.memory['ctes'][1] = {
                                    'tipo': 'int', 'dir': addrUno}
                                self.memory['ctesDir'][addrUno] = 1
                            self.evaluarBloqueEst(child, function)
                            self.stackQuads.append(
                                Quadruple('+', addrUno, addrVar, addrVar))
                            self.stackQuads.append(
                                Quadruple('goto', 'start', 0, 0))
                            pSaltos.append(len(self.stackQuads))
                            # print(child.getText())
                # self.stackQuads[pSaltos[]]
                self.stackQuads[pSaltos[1] -
                                1] = Quadruple('gotov', addrTemp, pSaltos[2]+1, 0)
                self.stackQuads[pSaltos[2] -
                                1] = Quadruple('goto', pSaltos[0], 0, 0)
                # self.stackQuads[pSaltos[2]-1] = Quadruple('goto',pSaltos[0],0,0)
                # print(pSaltos)

    def est_llamada_est(self, tree, function, stacks=False,insideExp=False):
        """Función que genera los cuadruplos de las llamadas a una función

        llamada
            : ID '(' params_llamada? ')'
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo

        Keyword Arguments:
            stacks {bool} -- [description] (default: {False})
        """
        functionName = tree.ID().getText()

        # Checa que exista y su inicio
        initialAddr = self.getInitialAddrFunction(functionName)
        if not initialAddr:
            msg = "No se encontró la función '{}'".format(functionName)
            return self.error(tree.ID(), msg)

        # Guarda el tipo de Retorno
        returnType = self.dirFunciones[functionName]['returnType']

        if insideExp and returnType == "void":
            msg = "Función '{}' de tipo void.".format(functionName)
            return self.error(tree.ID(), msg)

        self.stackQuads.append(Quadruple('era', functionName, 0, 0))
        functionParams = len(self.dirFunciones[functionName]['paramsType'])
        arbol = Trees.toStringTree(tree,self.rules)
        currentParams = arbol.count("params_llamada")

        if tree.params_llamada() != None and functionParams != 0:
            if currentParams == functionParams:
                self.est_llamada_est_aux(
                    tree.params_llamada(), function, functionName, tree.ID())
            else:
                msg = "Función '{}' acepta {} parámetros y se recibieron {}.".format(functionName,functionParams,currentParams)
                return self.error(tree.ID(), msg)
            # print(functionParams,currentParams)
        elif tree.params_llamada() == None and functionParams == 0:
            pass
        else:
            msg = "Función '{}' acepta {} parámetros y se recibieron {}.".format(functionName,functionParams,currentParams)
            return self.error(tree.ID(), msg)

        self.stackQuads.append(
            Quadruple('gosub', functionName, initialAddr, len(self.stackQuads)+1))

        if returnType != "void":
            #quad = "quad: = {} temp".format(functionName)
            #print("nombe fun: en llamada:",function,functionName)

            varAddr = self.getAddrOfVariable(functionName, function)
            varType = self.getTypeOfAddr(varAddr)

            #print("dir de function/var:",addr)

            isArray = self.getReturnsArray(functionName)
            if isArray:
                offset = self.memory_limits['temp']['dirArreglo']
                tempAddr = self.nextRelativeAddr(
                    self.ctesCounter, 'dir') + offset
                self.stackQuads.append(
                    Quadruple('=', varAddr, tempAddr, 'retArray'))
            else:
                offset = self.memory_limits['temp'][varType]
                tempAddr = self.nextRelativeAddr(
                    self.tempsCounter, varType) + offset
                self.stackQuads.append(Quadruple('=', varAddr, tempAddr, 0))

            if stacks != False:
                stacks['pOperandos'].append(tempAddr)
                stacks['pTipos'].append(varType)

    def est_llamada_est_aux(self, tree, targetFunction, callingFunction, error, counter=0):
        """[summary]

        params_llamada
            : expresion (',' params_llamada)?
            ;

        Arguments:
            tree {[type]} -- [description]
            targetFunction {[type]} -- [description]
            callingFunction {[type]} -- [description]
            error {[type]} -- [description]

        Keyword Arguments:
            counter {int} -- [description] (default: {0})
        """
        # tree2 = tree.params_llamada()
        for child in tree.children:
            if not isinstance(child, TerminalNodeImpl):
                rule = self.rules[child.getRuleIndex()]
                if rule == "expresion":
                    exp = self.expresion(child, targetFunction)
                    # if counter in self.dirFunciones[callingFunction]['paramsAddr']:
                    addr = self.dirFunciones[callingFunction]['paramsAddr'][counter]

                    callingType = self.getTypeOfAddr(exp)
                    targetType = self.getTypeOfAddr(addr)

                    if callingType != targetType:
                        msg = "Tipos incompatibles en la llamada a '{}'.".format(
                            callingFunction)
                        return self.error(error, msg)

                    callingDim1 = self.getDimOfAddr(exp, targetFunction, 1)
                    callingDim2 = self.getDimOfAddr(exp, targetFunction, 2)

                    targetDim1 = self.getDimOfAddr(addr, callingFunction, 1)
                    targetDim2 = self.getDimOfAddr(addr, callingFunction, 2)

                    if callingDim1 != targetDim1 or callingDim2 != targetDim2:
                        msg = "Tamaños incompatibles en la llamada a '{}'.".format(
                            callingFunction)
                        return self.error(error, msg)

                    if callingDim1 != False and callingDim1 == targetDim1:
                        self.stackQuads.append(
                            Quadruple('param', exp, addr, 'arreglo'))
                        self.stackQuads.append(
                            Quadruple('dimensiones', 0, callingDim1, callingDim2))
                    else:
                        self.stackQuads.append(
                            Quadruple('param', exp, addr, 0))
                    # print("param call",callingDim1,callingDim2, "param target",targetDim1,targetDim2)

                    counter += 1
                elif rule == "params_llamada":
                    self.est_llamada_est_aux(
                        child, targetFunction, callingFunction, error, counter)

    def est_escritura(self, tree, function):
        """Función que genera los cuadruplos de print ya sea para arreglos, strings o expresiones

        escrituras
            : (string | expresion) (',' escrituras)?
            ;

        Arguments:
            tree {antlr4tree} -- Arbol con los tokens y las reglas
            function {string} -- Nombre de la función desde la que se ejecuta este estatuo
        """
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "expresion":
                resultExp = self.expresion(tree, function)
                dim1 = self.getDimOfAddr(resultExp, function, 1)
                if dim1 != False:
                    dim2 = self.getDimOfAddr(resultExp, function, 2)
                    self.stackQuads.append(
                        Quadruple('print', resultExp, 0, 'arreglo'))
                    self.stackQuads.append(
                        Quadruple('dimensiones', resultExp, dim1, dim2))
                else:
                    self.stackQuads.append(Quadruple('print', resultExp, 0, 0))

            elif self.rules[tree.getRuleIndex()] == "string":
                # print("es un string")
                self.stackQuads.append(
                    Quadruple('print', tree.getText()[1:-1], 0, 0))
            else:
                for child in tree.children:
                    self.est_escritura(child, function)

        else:
            pass


class Compiler:
    def __init__(self, file):
        """Clase que actua como el compilador

        Arguments:
            file {string} -- El archivo a compilar, dentro de la carpeta /Pruebas
        """
        self.arch = file

    def compile(self):
        """Función que pone las instrucciones para ejecutar todo y regresar los datos correspondientes
        a la VM

        Returns:
            dicts -- Regresa tres diccionarios con todo lo necesario para que la VM jale.
        """
        archivo = "Pruebas/{}".format(self.arch)
        try:
            open(archivo, 'r')
        except FileNotFoundError:
            print("El archivo no existe.")
            exit()
        input_stream = FileStream(archivo, encoding = 'utf8')
        lexer = PatitoMasMasLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PatitoMasMasParser(stream)
        parser._listeners = [MyErrorListener()]
        startRoute = parser.start().programa()

        p = Program(startRoute, parser.ruleNames)
        p.execute()
        return p.getQuads(), p.getConstants(), p.getAllNames()


def main():
    """Función para imprimir todos los cuadruplos,directorios de funciones, variables,etc.
       Jala cuando corres el archivo compiler no el de la VM.
    """
    arch = sys.argv[1]
    input_stream = FileStream("Pruebas/{}".format(arch))
    lexer = PatitoMasMasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoMasMasParser(stream)
    startRoute = parser.start().programa()

    # traverse(rutaInicio,parser.ruleNames)

    p = Program(startRoute, parser.ruleNames)
    p.printAll()


def traverse(tree, rule_names, indent=0):
    """Función que imprime todos los tokens y reglas según la gramatica

    Arguments:
        tree {antlr4tree} -- Desde donde quieres que imprima
        rule_names {dict} -- Las reglas gramaticales del lenguaje

    Keyword Arguments:
        indent {int} -- Número de espacios a indentar(para que se vea bonito) (default: {0})
    """
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
