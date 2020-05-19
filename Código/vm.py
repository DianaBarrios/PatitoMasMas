from compiler import Compilador
from compiler import Cuadruplo

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
    if dir > 4999 and dir < 14000:
        mem = memorias['global']
        relativa = dir - 5000
        base = 5000
        #global
    elif dir > 14999 and dir < 24000:
        mem = memorias['local']['local']
        relativa = dir - 15000
        base = 15000
        #local
    elif dir > 24999 and dir < 34000:
        mem = memorias['local']['temps']
        relativa = dir - 25000
        base = 25000
        #temp
    elif dir > 33999 and dir < 44000:
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
        return bool(mem.bool[base+relativa])

def asignar(dir,valor,memorias):
    # print(type(dir))
    # print(dir)
    if dir > 4999 and dir < 14000:
        mem = memorias['global']
        relativa = dir - 5000
        base = 5000
        #global
    elif dir > 14999 and dir < 24000:
        mem = memorias['local']['local']
        relativa = dir - 15000
        base = 15000
        #local
    elif dir > 24999 and dir < 34000:
        mem = memorias['local']['temps']
        relativa = dir - 25000
        base = 25000
        #temp
    elif dir > 33999 and dir < 44000:
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
    # asignar(5001,10,memorias)
    # print("valor 5001: ",getValor(5001,memorias))
    # print(memGlobal.int)
    actual = 0
    while actual != len(cuadruplos) - 1:
        print(memorias['local']['temps'].int)
        operacion = cuadruplos[actual].op

        if operacion == 'goto':
            actual = cuadruplos[actual].dir1 - 1
            # print(actual)
        elif operacion == 'print':
            if type(cuadruplos[actual].dir1) is str:
                print(cuadruplos[actual].dir1)
            else:
                print("dir",cuadruplos[actual].dir1)
                valor = getValor(int(cuadruplos[actual].dir1),memorias)
                print(valor)
        elif operacion == 'lee':
            aux = input()
            print(aux)
        elif operacion == '+':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq + opDer
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
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq > opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '<':
            opIzq = getValor(cuadruplos[actual].dir1,memorias)
            opDer = getValor(cuadruplos[actual].dir2,memorias)
            aux = opIzq < opDer
            asignar(int(cuadruplos[actual].dir3),aux,memorias)
        elif operacion == '=':
            valor = getValor(cuadruplos[actual].dir1,memorias)
            asig = int(cuadruplos[actual].dir2)
            asignar(asig,valor,memorias)
        else:
            print(cuadruplos[actual].imprimir())

        if operacion != 'goto':
            actual +=1
        # elif operacion == 'goto':
    # print("===== Cuadruplos =====")
    # for i in range(len(cuadruplos)):
    #     print(i+1, ".-",cuadruplos[i].imprimir())

if __name__ == '__main__':
    main()
