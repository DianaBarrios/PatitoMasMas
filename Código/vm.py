from compiler import Compilador
from compiler import Cuadruplo

def main():
    c = Compilador(3)
    cuadruplos = c.compilar()
    actual = 0
    while actual != len(cuadruplos):
        operacion = cuadruplos[actual].op

        if operacion == 'goto':
            actual = cuadruplos[actual].dir1 - 1
            # print(actual)
        elif operacion == 'print':
            print(cuadruplos[actual].dir1)
        elif operacion == 'lee':
            aux = input()
            print(aux)
        elif operacion == '+':
            opIzq = cuadruplos[actual].dir1
            opDer = cuadruplos[actual].dir2
            aux = opIzq + opDer
            print(aux)
        elif operacion == '-':
            opIzq = cuadruplos[actual].dir1
            opDer = cuadruplos[actual].dir2
            aux = opIzq - opDer
            print(aux)
        elif operacion == '*':
            opIzq = cuadruplos[actual].dir1
            opDer = cuadruplos[actual].dir2
            aux = opIzq * opDer
            print(aux)
        elif operacion == '/':
            opIzq = cuadruplos[actual].dir1
            opDer = cuadruplos[actual].dir2
            aux = opIzq / opDer
            print(aux)
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
