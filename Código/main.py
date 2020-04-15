from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
import sys

class Programa:
    def __init__(self, tree, rules):
        self.tree = tree
        self.rules = rules

    def variablesGlobales(self, tree ,rules):
        if not isinstance(tree, TerminalNodeImpl):
            # variablesGlobales(child, rule_names)
            # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
            if rules[tree.getRuleIndex()] == "var":
                print("** Nuevas var**")
                print("Tipo var: ", tree.tipo().getText())
                lista = tree.ids().getText()
                lista = lista.split(",")
                print("Nombre var: ", lista)
            # elif rule_names[tree.getRuleIndex()] == "tipo":
            #     print("Tipo var: ", tree.getText())
            # elif rule_names[tree.getRuleIndex()] == "ids":
            #     lista = tree.getText().split(",")
            #     print("Nombre var: ", lista)
            for child in tree.children:
                self.variablesGlobales(child, rules)
        else:
            pass

    def funciones(self, tree ,rules):
        if not isinstance(tree, TerminalNodeImpl):
            # variablesGlobales(child, rule_names)
            # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
            if rules[tree.getRuleIndex()] == "functions":
                print("Funcion: ", tree.ID())
                # traverse(tree.params(),rule_names)
                self.mainFunction(tree.bloque_est().estatutos(),rules)
                # print("Main de la funcion: ", tree.bloque_est().getText())
                tipo_ret = tree.tipo_ret()
                if tipo_ret.getText() == "void":
                    print("Tipo ret: void")
                else:
                    print("Tipo ret: ",tipo_ret.tipo().getText())
            elif rules[tree.getRuleIndex()] == "params":
                print("Tipo var: ", tree.tipo().getText())
                print("Nombre var: ", tree.ID())
            for child in tree.children:
                self.funciones(child, rules)
        else:
            pass

    def mainFunction(self, tree ,rules):
        if not isinstance(tree, TerminalNodeImpl):
            if rules[tree.getRuleIndex()] == "estatuto":
                print("** Estatuto nuevo **")
                # print("Estatuto : ", tree.getText())
                # print(rule_names[child.getRuleIndex()])
                for child in tree.children:
                    regla = rules[child.getRuleIndex()]
                    if regla == "retorno":
                        self.retorno(tree.getText())
                        print("Regresa algo")
                    elif regla == "lectura":
                        self.lectura(tree.getText())
                        print("lectura algo")
                    elif regla == "asignacion":
                        self.asignacion(tree.getText())
                        print("asignacion algo")
                    elif regla == "decision":
                        self.decision(tree.getText())
                        print("decision algo")
                    elif regla == "repeticion":
                        self.repeticion(tree.getText())
                        print("repeticion algo")
                    elif regla == "llamada_est":
                        self.llamada_est(tree.getText())
                        print("llamada_est algo")
                    elif regla == "escritura":
                        self.escritura(tree.getText())
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
                self.mainFunction(child, rules)
        else:
            pass

    def retorno(self, codigo):
        print(codigo)

    def lectura(self, codigo):
        print(codigo)

    def asignacion(self, codigo):
        print(codigo)

    def decision(self, codigo):
        print(codigo)

    def repeticion(self, codigo):
        print(codigo)

    def llamada_est(self, codigo):
        print(codigo)

    def escritura(self, codigo):
        print(codigo)



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
    p1.mainFunction(p1.tree.principal().bloque_est().estatutos(),p1.rules)
    # mainFunction(programa.principal().bloque_est().estatutos(),reglas)

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
    programa = parser.start().programa()
    imprimeTodo(programa,parser.ruleNames)
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
