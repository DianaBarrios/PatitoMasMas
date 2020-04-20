from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
import sys
import pprint


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


    def decVariables(self,tree,temp,tipo):
        # tipoVar = tree.tipo().getText()
        # print(tipoVar)
        if not isinstance(tree, TerminalNodeImpl):
            # variablesGlobales(child, rule_names)
            # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
            if self.rules[tree.getRuleIndex()] == "dec_var":
                tipo = tree.tipo().getText()
                # print(tipoVar)

                # print(tree.lista_ids())
                # traverse(tree,self.rules)
                # lista = tree.lista_ids().getText()
                # print(lista)
                # lista = lista.split(",")
                # for elem in lista:
                #     if elem.find("[") == -1:
                #         temp[elem] = {'tipo': tipoVar}
                #     else:
                #         count = elem.count("[")
                #         if count == 1:
                #             indexInicio = elem.index("[")
                #             indexFinal = elem.index("]")
                #             nombre = elem[:indexInicio]
                #             dim = elem[indexInicio+1:indexFinal]
                #             temp[nombre] = {'tipo': tipoVar,'dim1': dim}
                #         if count == 2:
                #             indexInicio = elem.index("[")
                #             indexFinal = elem.index("]")
                #             indexInicio2 = elem.find("[", indexInicio + 1)
                #             indexFinal2 = elem.find("]", indexFinal + 1)
                #             nombre = elem[:indexInicio]
                #             dim = elem[indexInicio+1:indexFinal]
                #             dim2 = elem[indexInicio2+1:indexFinal2]
                #             temp[nombre] = {'tipo': tipoVar,'dim1': dim,'dim2':dim2}
            # elif self.rules[tree.getRuleIndex()] == "lista_ids":
            #     print("tiene lista")
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


    def variablesGlobales(self, tree ,rules):
        if not isinstance(tree, TerminalNodeImpl):
            # variablesGlobales(child, rule_names)
            # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
            if rules[tree.getRuleIndex()] == "var":
                print("** Nuevas var**")
                tipoVar = tree.tipo().getText()
                print("Tipo var: ", tipoVar)
                lista = tree.ids().getText()
                lista = lista.split(",")
                for elem in lista:
                    if elem.find("[") == -1:
                        self.varGlobales[elem] = {'tipo': tipoVar}
                    else:
                        count = elem.count("[")
                        if count == 1:
                            indexInicio = elem.index("[")
                            indexFinal = elem.index("]")
                            nombre = elem[:indexInicio]
                            dim = elem[indexInicio+1:indexFinal]
                            self.varGlobales[nombre] = {'tipo': tipoVar,'dim1': dim}
                        if count == 2:
                            indexInicio = elem.index("[")
                            indexFinal = elem.index("]")
                            indexInicio2 = elem.find("[", indexInicio + 1)
                            indexFinal2 = elem.find("]", indexFinal + 1)
                            nombre = elem[:indexInicio]
                            dim = elem[indexInicio+1:indexFinal]
                            dim2 = elem[indexInicio2+1:indexFinal2]
                            self.varGlobales[nombre] = {'tipo': tipoVar,'dim1': dim,'dim2':dim2}

                    # print(elem)
                # print("Nombre var: ", lista)
            # elif rule_names[tree.getRuleIndex()] == "tipo":
            #     print("Tipo var: ", tree.getText())
            # elif rule_names[tree.getRuleIndex()] == "ids":
            #     lista = tree.getText().split(",")
            #     print("Nombre var: ", lista)
            for child in tree.children:
                self.variablesGlobales(child, rules)
        else:
            pass

    def params(self,tree,temp1,temp2):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "params":
                temp1.append(tree.tipo().getText())
                temp2.append(tree.ID().getText())

            for child in tree.children:
                self.params(child,temp1,temp2)
        else:
            pass

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

            # elif rules[tree.getRuleIndex()] == "params":
            #     count = 0
            #     print(tree.getText())
            #     self.params(tree,{},count)
            #     print(count)
                # print("Tipo var: ", tree.tipo().getText())
                # print("Nombre var: ", tree.ID())
            for child in tree.children:
                self.funciones(child)
        else:
            pass

    def evaluarFun(self, tree,funcion):
        if not isinstance(tree, TerminalNodeImpl):
            if self.rules[tree.getRuleIndex()] == "estatuto":
                print("** Estatuto nuevo **")
                # print("Estatuto : ", tree.getText())
                # print(rule_names[child.getRuleIndex()])
                for child in tree.children:
                    regla = self.rules[child.getRuleIndex()]
                    if regla == "retorno":
                        self._retorno(tree.getText(),funcion)
                        print("Regresa algo")
                    elif regla == "lectura":
                        self._lectura(tree.getText())
                        print("lectura algo")
                    elif regla == "asignacion":
                        self._asignacion(tree,funcion)
                        print("asignacion algo")
                    elif regla == "decision":
                        self._decision(tree.getText())
                        print("decision algo")
                    elif regla == "repeticion":
                        self._repeticion(tree.getText())
                        print("repeticion algo")
                    elif regla == "llamada_est":
                        self._llamada_est(tree,funcion)
                        print("llamada_est algo")
                    elif regla == "escritura":
                        self._escritura(tree.escritura())
                        print("escritura algo")
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
    def _llamada_est(self, codigo,funcion):
        print("una llamada una funcion")
        # traverse(codigo,self.rules)
        # print(codigo.llamada_est().llamada().ID())
        # nombre = codigo.llamada_est().llamada().ID().getText()
        # estatutos = self.dirFunciones[nombre]['main']
        # self.evaluarFun(estatutos,nombre)
        # print(estatutos)

    def _escritura(self, codigo):
        res = []
        str = ""
        self._extraePrint(codigo,res)
        for index, item in enumerate(res):
            res[index] = res[index][1:-1]
            str += res[index] + " "
        print("Estoy imprimiendo:", str)

    ##falta
    #los valores pueden ser exp
    def _extraePrint(self, codigo,res):

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
        if not isinstance(codigo, TerminalNodeImpl):
        #     # print(codigo.getRuleContext().getText())
        #     # traverse(codigo,self.rules)
            if self.rules[codigo.getRuleIndex()] == "expresion":
                #mandar llamar expresion con el codigo
                res.append("'EXP'")
                # print("")
            if self.rules[codigo.getRuleIndex()] == "string":
                # print("es un string")
                res.append(codigo.getText())
        #         print("lo ignoramos")
        #
            for child in codigo.children:
                # if not isinstance(child, TerminalNodeImpl) and rule_names[child.getRuleIndex()] == "estatuto":
                #     print("Estatuto: ", tree)
                self._extraePrint(child,res)
        else:
            pass

def imprimeTodo(programa,reglas):
    p1 = Programa(programa,reglas)
    print("===== Nombre Programa =====")
    print(programa.ID())
    print("===== Variables =====")
    p1.variablesGlobales(p1.tree.variables().var(),p1.rules)
    # p1.llamadaglobales(p1.tree.variables().var(),p1.rules)
    # variablesGlobales(programa.variables().var(),reglas)
    print("===== Funciones =====")
    p1.funciones(p1.tree.functions(),p1.rules)
    # funciones(programa.functions(),reglas)
    print("===== Main =====")
    p1.evaluarFun(p1.tree.principal().bloque_est().estatutos(),p1.rules)
    # evaluarFun(programa.principal().bloque_est().estatutos(),reglas)

def main():
    # L = PatitoMasMasLexer.Lexer(f)
    # for token in L:
    #     ## do something with token
    #     print (token)
    # input_stream = None
    # if len(sys.argv) > 1:
    #     input_stream = FileStream("prueba.txt")
    # else:
    #     input_stream = InputStream(sys.stdin.readline())
    input_stream = FileStream("prueba.txt")

    lexer = PatitoMasMasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoMasMasParser(stream)
    rutaInicio = parser.start().programa()

    # traverse(rutaInicio,parser.ruleNames)

    programa = Programa(rutaInicio,parser.ruleNames)
    programa.imprimeTodo()

    # imprimeTodo(programa,parser.ruleNames)
    # traverse(programa.principal().bloque_est().estatutos(),parser.ruleNames)

    #
    # ## ver variables globales
    # ## arbol
    # # traverse(programa.variables().var(),parser.ruleNames)
    # ## bonito


    # ## ver funciones
    # ## arbol
    # # traverse(programa.functions(),parser.ruleNames)
    # ## bonito

    # traverse(programa.principal().bloque_est().estatutos(),parser.ruleNames)

    # for child in tree.getChildren():
    #     print(child.getText())
    # print('Variables')
    # print(len(programa.variables().var()))

    # traverse(programa.variables(), parser.ruleNames)

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
