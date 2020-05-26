from compiler import Compilador
from compiler import Cuadruplo
import numpy as np
import sys

class Memoria():
    def __init__(self):
        self.int = {}
        self.float = {}
        self.char = {}
        self.string = {}
        self.bool = {}

# 'global': {'int': 5000, 'float': 8000, 'char': 10000, 'string': 13000, 'bool': 14000},
# 'local': {'int': 15000, 'float': 18000, 'char': 20000, 'string': 23000, 'bool': 24000},
# 'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000, 'dir': 50000},
# 'ctes': {'int': 35000, 'float': 38000, 'char': 41000, 'string': 43000, 'bool': 44000}
def getValor(dir,memorias):
    #print("dir:",dir)

    if dir > 49999:
        dir = memorias['local']['temps'].int[dir]
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
    dirReal = base+relativa
    if relativa < 3000:
        return int(mem.int[dirReal])
    elif relativa > 2999 and relativa < 5000:
        return float(mem.float[dirReal])
    elif relativa > 4999 and relativa < 8000:
        return mem.char[dirReal]
    elif relativa > 7999 and relativa < 9000:
        return mem.string[dirReal]
    elif relativa > 8999:
        return mem.bool[dirReal]

def asignar(dir,valor,memorias):
    # print(type(dir))
    # print(dir)
    # if dir > 49999:
    #     dir = getValor(dir,memorias)
    # else:

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
    elif dir > 49999:
        mem = memorias['local']['temps']
        relativa = dir - 50000
        base = 50000
    dirReal = base+relativa
    if relativa < 3000:
        mem.int[dirReal] = valor
    elif relativa > 2999 and relativa < 5000:
        mem.float[dirReal] = valor
    elif relativa > 4999 and relativa < 8000:
        mem.char[dirReal] = valor
    elif relativa > 7999 and relativa < 9000:
        mem.string[dirReal] = valor
    elif relativa > 8999:
        mem.bool[dirReal] = valor

def opArreglo(op,arr1,arr2,dim1,dim2,res,memorias,yaEsArreglo):
    if not yaEsArreglo:
        arreglo1 = []
    arreglo2 = []
    if dim2 == False:
        for i in range(dim1):
            if not yaEsArreglo:
                dir1 = arr1 + i
                arreglo1.append(getValor(dir1,memorias))
            dir2 = arr2 + i
            arreglo2.append(getValor(dir2,memorias))
        if not yaEsArreglo:
            npArray1 = np.array(arreglo1)
        npArray2 = np.array(arreglo2)
            # ir sacando cada valor y ponerlo en una matrix
    else:
        for i in range(dim1):
            for j in range(dim2):
                if not yaEsArreglo:
                    dir1 = arr1 + i * dim2 + j
                    arreglo1.append(getValor(dir1,memorias))
                dir2 = arr2 + i * dim2 + j
                arreglo2.append(getValor(dir2,memorias))
        if not yaEsArreglo:
            npArray1 = np.array(arreglo1).reshape(dim1, dim2)
        else:
            npArray1 = arr1
        npArray2 = np.array(arreglo2).reshape(dim1, dim2)
    # print(npArray1)
    # print(npArray2)

    if op == '+':
        matrizResultado = np.add(npArray1, npArray2)
    elif op == '-':
        matrizResultado = np.subtract(npArray1, npArray2)
    elif op == '*':
        matrizResultado = np.matmul(npArray1, npArray2)
    elif op == '/':
        matrizResultado = np.divide(npArray1, npArray2)
    memorias['local']['local'].int[res] = matrizResultado
    # print("aqui",memorias['local']['local'].int[res])

##funciones especiales
def opEsps(op,dir,dim1,dim2,memorias,res=False):
    # equis = inv([[-3,1][5,0]])
    # print(equis)
    # b = np.array([[2,3],[4,5]])
    # b = np.linalg.inv(b)
    # print(b)
    arr = []
    if dim2 == False:
        for i in range(dim1):
            arr.append(getValor(dir+i,memorias))
            # ir sacando cada valor y ponerlo en una matrix
        npArray = np.array(arr)
    else:
        for i in range(dim1):
            for j in range(dim2):
                dirReal = dir + i * dim2 + j
                arr.append(getValor(dirReal,memorias))
        npArray = np.array(arr).reshape(dim1, dim2)
    if op == '$':
        det = np.linalg.det(npArray)
        return det
        # print(det)
    elif op == '?':
        mat = np.linalg.inv(npArray)
        memorias['local']['local'].int[res] = mat
        # mat = inv(npArray)
        # print(mat)
    elif op == '!':
        mat = np.transpose(npArray)
        memorias['local']['local'].int[res] = mat
    elif op == '%':
        det = np.mean(npArray)
        return det
    elif op == '@':
        det = np.sum(npArray)
        return det
    elif op == '~':
        det = np.min(npArray)
        return det
    elif op == '#':
        det = np.max(npArray)
        return det
    print("normal")
    print(npArray)

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
def copiaArreglo(dir1,dir2,dim1,dim2,memorias,yaEsArreglo):
    if dim2 == False:
        for i in range(dim1):
            if yaEsArreglo:
                valor = dir1[i]
            else:
                valor = getValor(dir1+i,memorias)
            # print("dir1",dir1+i,"dir2",dir2+i)
            # print(dir2 + dir)
            asignar(dir2+i,valor,memorias)
    else:
        for i in range(dim1):
            for j in range(dim2):
                # cont+=1
                dir = i * dim2 + j
                # print(dir1 + dir)
                if yaEsArreglo:
                    valor = dir1[i][j]
                else:
                    valor = getValor(dir1+dir,memorias)
                # print("dir1",dir1+dir,"dir2",dir2+dir)
                # print(dir2 + dir)
                asignar(dir2+dir,valor,memorias)
                # print(i,j)

def imprimeArreglo(dir,dim1,dim2,memorias):
    arreglo = []
    if dim2 == False:
        for i in range(dim1):
            dir1 = dir + i
            arreglo.append(getValor(dir1,memorias))
        npArray = np.array(arreglo)
            # ir sacando cada valor y ponerlo en una matrix
    else:
        for i in range(dim1):
            for j in range(dim2):
                dir1 = dir + i * dim2 + j
                arreglo.append(getValor(dir1,memorias))
        npArray = np.array(arreglo).reshape(dim1, dim2)
    print(npArray)

def main():
    # arch = 11
    arch = sys.argv[1]
    c = Compilador(arch)
    cuadruplos, ctes = c.compilar()
    print(ctes)
    ctesInt =  {key: value for key, value in ctes.items() if key < 38000}
    ctesFloat =  {key: value for key, value in ctes.items() if key > 37999}

    memGlobal = Memoria()
    memLocal = {'temps': Memoria(), 'local': Memoria()}
    # memTemp = Memoria()
    # memLocal = Memoria()
    memCtes = Memoria()
    # print(ctes)
    memorias = {'global' : memGlobal,'local': memLocal, 'ctes':memCtes}
    memCtes.int = ctesInt
    memCtes.float = ctesFloat

    # print(ctes)
    pilaMemorias = []
    pilaParams = []
    pilaIP = []
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
        elif operacion == 'era':
            pass
        elif operacion == 'param':
            pilaParams.append({'dir': cuadruplos[actual].dir2,'valor': getValor(cuadruplos[actual].dir1,memorias)})
        elif operacion == 'gosub':
            pilaMemorias.append(memorias['local'])
            nuevaLocal = {'temps': Memoria(), 'local': Memoria()}
            memorias['local'] = nuevaLocal
            # print(memorias['local']['local'].int)
            for param in pilaParams:
                # print("Estoy asignando")
                asignar(param['dir'],param['valor'],memorias)
            nuevo = cuadruplos[actual].dir2 - 1
            pilaIP.append(cuadruplos[actual].dir3)
            # print("pila",pilaIP)
            avanzaUno = False
            actual = nuevo
            # actual = int(cuadruplos[actual].dir2)
        elif operacion == 'endproc':
            avanzaUno = False
            # actual = 10
            actual = pilaIP.pop()
            # print(actual)
            memorias['local'] = pilaMemorias.pop()
        elif operacion == 'print':
            if type(cuadruplos[actual].dir1) is str:
                # print("entre")
                print(cuadruplos[actual].dir1)
            else:
                dir1 = cuadruplos[actual].dir1
                if cuadruplos[actual].dir3 == 'arreglo':
                    dim1 = cuadruplos[actual+1].dir2
                    dim2 = cuadruplos[actual+1].dir3
                    imprimeArreglo(dir1,dim1,dim2,memorias)
                    avanzaUno = False
                    actual += 2
                else:
                    valor = getValor(int(dir1),memorias)
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
            dir1= cuadruplos[actual].dir1
            dir2 = cuadruplos[actual].dir3
            # print("dir2",dir2)
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            valor = opEsps('$',dir1,dim1,dim2,memorias)
            asignar(dir2,valor,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '%':
            # print("dollar sign")
            dir1= cuadruplos[actual].dir1
            dir2 = cuadruplos[actual].dir3
            # print("dir2",dir2)
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            valor = opEsps('%',dir1,dim1,dim2,memorias)
            asignar(dir2,valor,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '@':
            # print("dollar sign")
            dir1= cuadruplos[actual].dir1
            dir2 = cuadruplos[actual].dir3
            # print("dir2",dir2)
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            valor = opEsps('@',dir1,dim1,dim2,memorias)
            asignar(dir2,valor,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '~':
            # print("dollar sign")
            dir1= cuadruplos[actual].dir1
            dir2 = cuadruplos[actual].dir3
            # print("dir2",dir2)
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            valor = opEsps('~',dir1,dim1,dim2,memorias)
            asignar(dir2,valor,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '#':
            # print("dollar sign")
            dir1= cuadruplos[actual].dir1
            dir2 = cuadruplos[actual].dir3
            # print("dir2",dir2)
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print(dir,dim1,dim2)
            valor = opEsps('#',dir1,dim1,dim2,memorias)
            asignar(dir2,valor,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '?':
            # print("dollar sign")
            dir = cuadruplos[actual].dir1
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            opEsps('?',dir,dim1,dim2,memorias,res)
            # print(dir,dim1,dim2)
            # arreglo(dir,dim1,dim2,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '!':
            # print("dollar sign")
            dir = cuadruplos[actual].dir1
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            opEsps('!',dir,dim1,dim2,memorias,res)
            # print(dir,dim1,dim2)
            # arreglo(dir,dim1,dim2,memorias)
            avanzaUno = False
            actual += 2
        elif operacion == '*Arreglos':
            arr1 = cuadruplos[actual].dir1
            arr2 = cuadruplos[actual].dir2
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print("ds",dim1,dim2)
            if arr1 >= 55000:
                arreglo = memorias['local']['local'].int[arr1]
                opArreglo('*',arreglo,arr2,dim1,dim2,res,memorias,True)
            else:
                opArreglo('*',arr1,arr2,dim1,dim2,res,memorias,False)
            avanzaUno = False
            actual +=2
            # print(memorias['local']['temps'].int)
        elif operacion == '/Arreglos':
            arr1 = cuadruplos[actual].dir1
            arr2 = cuadruplos[actual].dir2
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print("ds",dim1,dim2)
            if arr1 >= 55000:
                arreglo = memorias['local']['local'].int[arr1]
                opArreglo('/',arreglo,arr2,dim1,dim2,res,memorias,True)
            else:
                opArreglo('/',arr1,arr2,dim1,dim2,res,memorias,False)
            avanzaUno = False
            actual +=2
            # print(memorias['local']['temps'].int)
        elif operacion == '+Arreglos':
            arr1 = cuadruplos[actual].dir1
            arr2 = cuadruplos[actual].dir2
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print("ds",dim1,dim2)
            if arr1 >= 55000:
                arreglo = memorias['local']['local'].int[arr1]
                opArreglo('+',arreglo,arr2,dim1,dim2,res,memorias,True)
            else:
                opArreglo('+',arr1,arr2,dim1,dim2,res,memorias,False)
            avanzaUno = False
            actual +=2
            # print(memorias['local']['temps'].int)
        elif operacion == '-Arreglos':
            arr1 = cuadruplos[actual].dir1
            arr2 = cuadruplos[actual].dir2
            res = cuadruplos[actual].dir3
            dim1 = cuadruplos[actual+1].dir2
            dim2 = cuadruplos[actual+1].dir3
            # print("ds",dim1,dim2)
            if arr1 >= 55000:
                arreglo = memorias['local']['local'].int[arr1]
                opArreglo('-',arreglo,arr2,dim1,dim2,res,memorias,True)
            else:
                opArreglo('-',arr1,arr2,dim1,dim2,res,memorias,False)
            avanzaUno = False
            actual +=2
            # print(memorias['local']['temps'].int)
        elif operacion == '+':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq + opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
            # print(memorias['local']['temps'].int)
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
                # checaArreglo = type(memorias['local']['local'].int[cuadruplos[actual].dir1]) is np.ndarray
                # print(checaArreglo)
                arr1 = cuadruplos[actual].dir1

                arr2 = cuadruplos[actual].dir2
                dim1 = cuadruplos[actual+1].dir2
                dim2 = cuadruplos[actual+1].dir3
                # print("ds",dim1,dim2)
                if arr1 >= 55000:
                    arreglo = memorias['local']['local'].int[arr1]
                    copiaArreglo(arreglo,arr2,dim1,dim2,memorias,True)
                else:
                    copiaArreglo(arr1,arr2,dim1,dim2,memorias,False)
                avanzaUno = False
                actual +=2
                ##mandar llamar a la funcion que copia los arreglos
                # print("hago algo con los arreglos", arr1,arr2)
            elif tipo == 'arrSingle':
                dirReal = memorias['local']['temps'].int[cuadruplos[actual].dir2]
                valor = getValor(cuadruplos[actual].dir1,memorias)
                # print(dirReal,valor)
                asignar(dirReal,valor,memorias)

                # asigna = getValor(cuadruplos[actual].dir2,memorias)
                # valor = getValor(cuadruplos[actual].dir1,memorias)
                # print(asigna,valor)
                # asignar(asigna,valor,memorias)
                # print(memorias['global'].int)
                # print(memorias['local']['temps'].int)
                # print(memorias['ctes'].int)
                # print(memorias['local']['temps'].int[int(cuadruplos[actual].dir2)])
                # valor =
                # asig = getValor(cuadruplos[actual].dir2,memorias)
                # asignar

                # print("Asigne con arr",valor,asig)
            else:
                valor = getValor(cuadruplos[actual].dir1,memorias)
                asig = int(cuadruplos[actual].dir2)
                asignar(asig,valor,memorias)
                # print(memorias['local']['temps'].int)
                # print(memorias['ctes'].int)
                # print("asigne la dir",asig)
        else:
            print(cuadruplos[actual].imprimir())

        if avanzaUno:
            actual +=1
    print(memorias['local']['temps'].int)
    print(memorias['ctes'].int)
    #     # elif operacion == 'goto':


if __name__ == '__main__':
    main()
