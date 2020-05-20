from compiler import Compilador
from compiler import Cuadruplo
import numpy as np


class Memoria():
    def __init__(self):
        self.int = {}
        self.float = {}
        self.char = {}
        self.string = {}
        self.bool = {}

# 'global': {'int': 5000, 'float': 8000, 'char': 10000, 'string': 13000, 'bool': 14000},
# 'local': {'int': 15000, 'float': 18000, 'char': 20000, 'string': 23000, 'bool': 24000},
# 'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000},
# 'ctes': {'int': 35000, 'float': 38000, 'char': 41000, 'string': 43000, 'bool': 44000}
def getValor(dir,memorias):
    # print(dir)
    if dir > 4999 and dir < 15000:
        mem = memorias['global']
        relativa = dir - 5000
        base = 5000
        #global
    elif dir > 14999 and dir < 24000:
        mem = memorias['local']['local']
        relativa = dir - 15000
        base = 15000
        #local
    elif dir > 24999 and dir < 35000:
        mem = memorias['local']['temps']
        relativa = dir - 25000
        base = 25000
        #temp
    elif dir > 34999 and dir < 44000:
        mem = memorias['ctes']
        relativa = dir - 35000
        base = 35000

    if relativa < 3000:
        return int(mem.int[base+relativa])
    elif relativa > 2999 and relativa < 5000:
        return float(mem.float[base+relativa])
    elif relativa > 4999 and relativa < 8000:
        return mem.char[base+relativa]
    elif relativa > 7999 and relativa < 9000:
        return mem.string[base+relativa]
    elif relativa > 8999:
        return mem.bool[base+relativa]

def asignar(dir,valor,memorias):
    # print(type(dir))
    # print(dir)
    if dir > 4999 and dir < 15000:
        mem = memorias['global']
        relativa = dir - 5000
        base = 5000
        #global
    elif dir > 14999 and dir < 24000:
        mem = memorias['local']['local']
        relativa = dir - 15000
        base = 15000
        #local
    elif dir > 24999 and dir < 35000:
        mem = memorias['local']['temps']
        relativa = dir - 25000
        base = 25000
        #temp
    elif dir > 34999 and dir < 44000:
        mem = memorias['ctes']
        relativa = dir - 35000
        base = 35000
    if relativa < 3000:
        mem.int[base+relativa] = int(valor)
    elif relativa > 2999 and relativa < 5000:
        mem.float[base+relativa] = valor
    elif relativa > 4999 and relativa < 8000:
        mem.char[base+relativa] = valor
    elif relativa > 7999 and relativa < 9000:
        mem.string[base+relativa] = valor
    elif relativa > 8999:
        mem.bool[base+relativa] = valor

##funciones especiales
def arreglo(dir,dim1,dim2,memorias):
    # equis = inv([[-3,1][5,0]])
    # print(equis)
    # b = np.array([[2,3],[4,5]])
    # b = np.linalg.inv(b)
    # print(b)

    if dim2 == -1:
        for i in range(dim1):
            print(dir+i)
            # ir sacando cada valor y ponerlo en una matrix
    else:
        for i in range(dim1):
            for j in range(dim2):
                print(dir + i * dim2 + j)
                # ir sacando cada valor y ponerlo en una matrix
    #transformar la pila en una matrix
    #aplicarle la operacion necesaria
    #### Inversa ?
        # m = np.matrix([[2,3],[4,5]])
        # m = np.linalg.inv(m)
    #### Determinante $
        # m = np.linalg.det(m)
    #### Transpuesta !

        # np.transpose(x)

#dim1 es de donde se copia
#dim2 es a donde se copia
def copiaArreglo(dir1,dir2,dim1,dim2,memorias):
    for i in range(dim1):
        for j in range(dim2):
            dir = i * dim2 + j
            print(dir1 + dir)
            valor = getValor(dir1+dir,memorias)
            print(dir2 + dir)
            asignar(dir2+dir,valor,memorias)
            # print(i,j)

def main():

    c = Compilador(3)
    cuadruplos, ctes = c.compilar()

    memGlobal = Memoria()
    memLocal = {'temps': Memoria(), 'local': Memoria()}
    # memTemp = Memoria()
    # memLocal = Memoria()
    memCtes = Memoria()
    # print(ctes)
    memorias = {'global' : memGlobal,'local': memLocal, 'ctes':memCtes}
    memCtes.int = ctes
    # arreglo(5010,5,1,memorias)
    # copiaArreglo(5000,4000,10,3,memorias)
    # asignar(5001,10,memorias)
    # print("valor 5001: ",getValor(5001,memorias))
    # print(memGlobal.int)
    # print("===== Cuadruplos =====")
    # for i in range(38,len(cuadruplos)):
    #     print(i+1, ".-",cuadruplos[i].imprimir())
    actual = 0
    while actual != len(cuadruplos) - 1:
        avanzaUno = True
        # print(memorias['local']['temps'].int)
        operacion = cuadruplos[actual].op
        # print(actual)
        if operacion == 'goto':
            nuevo = cuadruplos[actual].dir1 - 1
            actual = nuevo
            # print(nuevo)
            avanzaUno = False
        elif operacion == 'gotof':
            avanzaUno = False
            valor = getValor(cuadruplos[actual].dir1,memorias)
            nuevo = cuadruplos[actual].dir2
            # print(nuevo)
            if not valor:
                actual = nuevo
            else:
                actual += 1
        elif operacion == 'gotov':
            avanzaUno = False
            valor = getValor(cuadruplos[actual].dir1,memorias)
            nuevo = cuadruplos[actual].dir2
            # print(nuevo)
            if not valor:
                actual += 1
            else:
                actual = nuevo
        elif operacion == 'print':
            if type(cuadruplos[actual].dir1) is str:
                # print("entre")
                print(cuadruplos[actual].dir1)
            else:
                # print("dir",cuadruplos[actual].dir1)
                valor = getValor(int(cuadruplos[actual].dir1),memorias)
                if int(valor) > 5000:
                    valor2 = getValor(int(valor),memorias)
                    print(valor2)
                else:
                    print(valor)
        elif operacion == 'lee':
            # print("lee")
            dir = int(cuadruplos[actual].dir1)
            aux = input()
            asignar(dir,aux,memorias)
        elif operacion == 'verify':
            # print(cuadruplos[actual].imprimir())
            # print("adentro verify")
            valor = getValor(int(cuadruplos[actual].dir1),memorias)
            ls = cuadruplos[actual].dir3
            if valor > ls:
                print("ERROR")
        elif operacion == '$':
            # print("dollar sign")
            dir = cuadruplos[actual].dir1
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            # arreglo(dir,dim1,dim2,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '?':
            # print("dollar sign")
            dir = cuadruplos[actual].dir1
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            # arreglo(dir,dim1,dim2,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '!':
            # print("dollar sign")
            dir = cuadruplos[actual].dir1
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            # arreglo(dir,dim1,dim2,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '+':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq + opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '+Dir':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = cuadruplos[actual].dir2
            aux = opIzq + opDer
            # print("RES", aux)
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '-':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq - opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '*':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq * opDer
            # print(cuadruplos[actual].dir3)
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
            # print(aux)
        elif operacion == '/':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq / opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '&':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq and opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '||':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq or opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '>':
            # print("compare")
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq > opDer
            # print(aux)
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '<':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq < opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '==':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq == opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '=':
            tipo = cuadruplos[actual].dir3
            if  tipo == 'arreglo':
                arr1 = cuadruplos[actual].dir1
                arr2 = cuadruplos[actual].dir2
                ##mandar llamar a la funcion que copia los arreglos
                print("hago algo con los arreglos", arr1,arr2)
            elif tipo == 'arrSingle':
                valor = getValor(cuadruplos[actual].dir1,memorias)
                asig = getValor(cuadruplos[actual].dir2,memorias)
                asignar(asig,valor,memorias)
                # print("Asigne con arr",valor,asig)
            else:
                valor = getValor(cuadruplos[actual].dir1,memorias)
                asig = int(cuadruplos[actual].dir2)
                asignar(asig,valor,memorias)
                # print("asigne la dir",asig)
        else:
            print(cuadruplos[actual].imprimir())

        if avanzaUno:
            actual +=1
    # print(memorias['local']['temps'].int)
    # print(memorias['ctes'].int)
    #     # elif operacion == 'goto':


if __name__ == '__main__':
    main()
