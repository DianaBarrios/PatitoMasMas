from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.InputStream import InputStream
from PatitoMasMasLexer import PatitoMasMasLexer
from PatitoMasMasParser import PatitoMasMasParser
import sys


def variablesGlobales(tree, rule_names):

    if not isinstance(tree, TerminalNodeImpl):
        # variablesGlobales(child, rule_names)
        # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
        if rule_names[tree.getRuleIndex()] == "var":
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
            variablesGlobales(child, rule_names)
    else:
        pass

def funciones(tree, rule_names):
    if not isinstance(tree, TerminalNodeImpl):
        # variablesGlobales(child, rule_names)
        # print("{0}TOKEN='{1}'".format("  ", tree.getText()))
        if rule_names[tree.getRuleIndex()] == "functions":
            print("Funcion: ", tree.ID())
            # traverse(tree.params(),rule_names)
            mainFunction(tree.bloque_est().estatutos(),rule_names)
            # print("Main de la funcion: ", tree.bloque_est().getText())
            tipo_ret = tree.tipo_ret()
            if tipo_ret.getText() == "void":
                print("Tipo ret: void")
            else:
                print("Tipo ret: ",tipo_ret.tipo().getText())
        elif rule_names[tree.getRuleIndex()] == "params":
            print("Tipo var: ", tree.tipo().getText())
            print("Nombre var: ", tree.ID())
        for child in tree.children:
            funciones(child, rule_names)
    else:
        pass

def retorno(codigo):
    print(codigo)

def lectura(codigo):
    print(codigo)

def asignacion(codigo):
    print(codigo)

def decision(codigo):
    print(codigo)

def repeticion(codigo):
    print(codigo)

def llamada_est(codigo):
    print(codigo)

def escritura(codigo):
    print(codigo)

def mainFunction(tree,rule_names):
    if not isinstance(tree, TerminalNodeImpl):
        if rule_names[tree.getRuleIndex()] == "estatuto":
            print("** Estatuto nuevo **")
            # print("Estatuto : ", tree.getText())
            # print(rule_names[child.getRuleIndex()])
            for child in tree.children:
                regla = rule_names[child.getRuleIndex()]
                if regla == "retorno":
                    retorno(tree.getText())
                    print("Regresa algo")
                elif regla == "lectura":
                    lectura(tree.getText())
                    print("lectura algo")
                elif regla == "asignacion":
                    asignacion(tree.getText())
                    print("asignacion algo")
                elif regla == "decision":
                    decision(tree.getText())
                    print("decision algo")
                elif regla == "repeticion":
                    repeticion(tree.getText())
                    print("repeticion algo")
                elif regla == "llamada_est":
                    llamada_est(tree.getText())
                    print("llamada_est algo")
                elif regla == "escritura":
                    escritura(tree.getText())
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
            mainFunction(child, rule_names)
    else:
        pass

def handleMultiply(expr):
    multiplying = True
    value = 1
    for child in expr.getChildren():
        if isinstance(child, antlr4.tree.Tree.TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value /= int(child.getText())

    return value

def handleExpression(expr):
    adding = True
    value = 0
    for child in expr.getChildren():
        # print("exp: ", expr.getText())
        print("child:", child.getText())
    #     if isinstance(child, antlr4.tree.Tree.TerminalNode):
    #         adding = child.getText() == "+"
    #     else:
    #         multValue = handleMultiply(child)
    #         if adding:
    #             value += multValue
    #         else:
    #             value -= multValue
    # print("Parsed expression %s has value %s" % (expr.getText(), value))

def PatitoMasMasPrintListener(PatitoMasMasListener):
    def ID(self, ctx):
        print("Hello: %s" % ctx.ID())

def imprimeTodo(programa,reglas):
    print("===== Nombre Programa =====")
    print(programa.ID())
    print("===== Variables =====")
    variablesGlobales(programa.variables().var(),reglas)
    print("===== Funciones =====")
    funciones(programa.functions(),reglas)
    print("===== Main =====")
    mainFunction(programa.principal().bloque_est().estatutos(),reglas)

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

    # print(tree.getText())
    # print(list(tree.getChildren()))
    # tree = parser.start().programa().variables().getText()
    # variablesGlobales(parser.start().programa().variables())
    # print(parser.start().programa().functions())
    # print(tree)
    # handleExpression(tree)

if __name__ == '__main__':
    main()
