from compiler import Compiler
from compiler import Quadruple
import numpy as np
import sys

class Memory():
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
def getValue(addr,memories):
    #print("dir:",dir)

    if addr > 49999:
        addr = memories['local']['temps'].int[addr]
        # print(dir)
    if addr > 4999 and addr < 15000:
        mem = memories['global']
        relative = addr - 5000
        base = 5000
        #global
    elif addr > 14999 and addr < 24000:
        mem = memories['local']['local']
        relative = addr - 15000
        base = 15000
        #local
    elif addr > 24999 and addr < 35000:
        mem = memories['local']['temps']
        relative = addr - 25000
        base = 25000
        #temp
    elif addr > 34999 and addr < 44000:
        mem = memories['ctes']
        relative = addr - 35000
        base = 35000

    realAddr = base+relative

    if relative < 3000:
        return int(mem.int[realAddr])
    elif relative > 2999 and relative < 5000:
        return float(mem.float[realAddr])
    elif relative > 4999 and relative < 8000:
        return mem.char[realAddr]
    elif relative > 7999 and relative < 9000:
        return mem.string[realAddr]
    elif relative > 8999:
        return mem.bool[realAddr]
    else:
        return False;

def setValue(addr,value,memories):
    if addr > 4999 and addr < 15000:
        mem = memories['global']
        relative = addr - 5000
        base = 5000
        #global
    elif addr > 14999 and addr < 24000:
        mem = memories['local']['local']
        relative = addr - 15000
        base = 15000
        #local
    elif addr > 24999 and addr < 35000:
        mem = memories['local']['temps']
        relative = addr - 25000
        base = 25000
        #temp
    elif addr > 34999 and addr < 44000:
        mem = memories['ctes']
        relative = addr - 35000
        base = 35000
    elif addr > 49999:
        mem = memories['local']['temps']
        relative = addr - 50000
        base = 50000

    realAddr = base+relative
    if relative < 3000:
        mem.int[realAddr] = value
    elif relative > 2999 and relative < 5000:
        mem.float[realAddr] = value
    elif relative > 4999 and relative < 8000:
        mem.char[realAddr] = value
    elif relative > 7999 and relative < 9000:
        mem.string[realAddr] = value
    elif relative > 8999:
        mem.bool[realAddr] = value

def aritmeticArray(op,arr1,arr2,dim1,dim2,res,memories,isArray):
    if not isArray:
        array1 = []
    array2 = []
    if dim2 == False:
        for i in range(dim1):
            if not isArray:
                dir1 = arr1 + i
                array1.append(getValue(dir1,memories))
            dir2 = arr2 + i
            array2.append(getValue(dir2,memories))
        if not isArray:
            npArray1 = np.array(array1)
        npArray2 = np.array(array2)
            # ir sacando cada valor y ponerlo en una matrix
    else:
        for i in range(dim1):
            for j in range(dim2):
                if not isArray:
                    dir1 = arr1 + i * dim2 + j
                    array1.append(getValue(dir1,memories))
                dir2 = arr2 + i * dim2 + j
                array2.append(getValue(dir2,memories))
        if not isArray:
            npArray1 = np.array(array1).reshape(dim1, dim2)
        else:
            npArray1 = arr1
        npArray2 = np.array(array2).reshape(dim1, dim2)
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
    memories['local']['local'].int[res] = matrizResultado
    # print("aqui",memories['local']['local'].int[res])

##funciones especiales
def specialArray(op,addr,dim1,dim2,memories,res=False):
    # equis = inv([[-3,1][5,0]])
    # print(equis)
    # b = np.array([[2,3],[4,5]])
    # b = np.linalg.inv(b)
    # print(b)
    arr = []
    if dim2 == False:
        for i in range(dim1):
            arr.append(getValue(addr+i,memories))
            # ir sacando cada valor y ponerlo en una matrix
        npArray = np.array(arr)
    else:
        for i in range(dim1):
            for j in range(dim2):
                realAddr = addr + i * dim2 + j
                arr.append(getValue(realAddr,memories))
        npArray = np.array(arr).reshape(dim1, dim2)

    if op == '$':
        result = np.linalg.det(npArray)
    elif op == '?':
        result = np.linalg.inv(npArray)
    elif op == '!':
        result = np.transpose(npArray)
    elif op == '%':
        result = np.mean(npArray)
    elif op == '@':
        result = np.sum(npArray)
    elif op == '~':
        result = np.min(npArray)
    elif op == '#':
        result = np.max(npArray)

    if op in ['%','#','$','@','~']:
        return result
    else:
        memories['local']['local'].int[res] = result
    print("normal")
    print(npArray)

    #transformar la pila en una matrix
    #aplicarle la operation necesaria
    #### Inversa ?
        # m = np.matrix([[2,3],[4,5]])
        # m = np.linalg.inv(m)
    #### Determinante $
        # m = np.linalg.det(m)
    #### Transpuesta !

        # np.transpose(x)

#dim1 es de donde se copia
#dim2 es a donde se copia
def copyArray(arr1,arr2,dim1,dim2,memories,isArray):
    if dim2 == False:
        for i in range(dim1):
            if isArray:
                value = arr1[i]
            else:
                value = getValue(arr1+i,memories)
            setValue(arr2+i,value,memories)
    else:
        for i in range(dim1):
            for j in range(dim2):
                relativeAddr = i * dim2 + j
                if isArray:
                    value = arr1[i][j]
                else:
                    value = getValue(arr1+relativeAddr,memories)
                setValue(arr2+relativeAddr,value,memories)

def printArray(addr,dim1,dim2,memories):
    array = []
    if dim2 == False:
        for i in range(dim1):
            realAddr = addr + i
            array.append(getValue(realAddr,memories))
        npArray = np.array(array)
            # ir sacando cada valor y ponerlo en una matrix
    else:
        for i in range(dim1):
            for j in range(dim2):
                realAddr = addr + i * dim2 + j
                array.append(getValue(realAddr,memories))
        npArray = np.array(array).reshape(dim1, dim2)
    print(npArray)

def main():
    # arch = 11
    arch = sys.argv[1]
    c = Compiler(arch)
    quadruples, ctes = c.compile()
    print(ctes)
    ctesInt =  {key: value for key, value in ctes.items() if key < 38000}
    ctesFloat =  {key: value for key, value in ctes.items() if key > 37999}

    memGlobal = Memory()
    memLocal = {'temps': Memory(), 'local': Memory()}
    memCtes = Memory()

    memories = {'global' : memGlobal,'local': memLocal, 'ctes':memCtes}
    memCtes.int = ctesInt
    memCtes.float = ctesFloat

    # print(ctes)
    stackMemories = []
    stackParams = []
    stackPointers = []
    # arreglo(5010,5,1,memories)
    # copyArray(5000,4000,10,3,memories)
    # setValue(5001,10,memories)
    # print("valor 5001: ",getValue(5001,memories))
    # print(memGlobal.int)
    # print("===== quadruples =====")
    # for i in range(38,len(quadruples)):
    #     print(i+1, ".-",quadruples[i].imprimir())
    current = 0
    while current != len(quadruples) - 1:
        stepOne = True
        # print(memories['local']['temps'].int)
        operation = quadruples[current].op
        # print(current)
        if operation == 'goto':
            newPointer = quadruples[current].addr1 - 1
            current = newPointer
            # print(nuevo)
            stepOne = False
        elif operation == 'gotof':
            stepOne = False
            value = getValue(quadruples[current].addr1,memories)
            newPointer = quadruples[current].addr2

            if not value:
                current = newPointer
            else:
                current += 1
        elif operation == 'gotov':
            stepOne = False
            value = getValue(quadruples[current].addr1,memories)
            newPointer = quadruples[current].addr2

            if not value:
                current += 1
            else:
                current = newPointer
        elif operation == 'era':
            pass
        elif operation == 'param':
            stackParams.append({'addr': quadruples[current].addr2,'value': getValue(quadruples[current].addr1,memories)})
        elif operation == 'gosub':
            stackMemories.append(memories['local'])
            newMemory = {'temps': Memory(), 'local': Memory()}
            memories['local'] = newMemory

            for param in stackParams:
                setValue(param['addr'],param['value'],memories)

            newPointer = quadruples[current].addr2 - 1
            stackPointers.append(quadruples[current].addr3)

            stepOne = False
            current = newPointer
        elif operation == 'endproc':
            stepOne = False

            current = stackPointers.pop()

            memories['local'] = stackMemories.pop()
        elif operation == 'print':
            if type(quadruples[current].addr1) is str:
                # print("entre")
                print(quadruples[current].addr1)
            else:
                addr = quadruples[current].addr1
                if quadruples[current].addr3 == 'arreglo':
                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3
                    printArray(addr,dim1,dim2,memories)
                    stepOne = False
                    current += 2
                else:
                    value = getValue(int(addr),memories)
                    print(value)
        elif operation == 'lee':
            addr = int(quadruples[current].addr1)
            value = input()
            setValue(addr,value,memories)
        elif operation == 'verify':
            value = getValue(int(quadruples[current].addr1),memories)
            limit = quadruples[current].addr3
            if value > limit:
                print("ERROR")
        elif operation in ['%','#','$','@','~','?','!']:
            addr1 = quadruples[current].addr1
            addr2 = quadruples[current].addr3

            dim1 = quadruples[current+1].addr2
            dim2 = quadruples[current+1].addr3

            value = specialArray(operation,addr1,dim1,dim2,memories)
            setValue(addr2,value,memories)
            stepOne = False
            current += 2
        elif operation in ['*Arreglos','/Arreglos','+Arreglos','-Arreglos']:
            op = operation[0]
            arr1 = quadruples[current].addr1
            arr2 = quadruples[current].addr2
            res = quadruples[current].addr3

            dim1 = quadruples[current+1].addr2
            dim2 = quadruples[current+1].addr3
            # print("ds",dim1,dim2)
            if arr1 >= 55000:
                array = memories['local']['local'].int[arr1]
                aritmeticArray(op,array,arr2,dim1,dim2,res,memories,True)
            else:
                aritmeticArray(op,arr1,arr2,dim1,dim2,res,memories,False)
            stepOne = False
            current +=2
        elif operation in ['+','-','*','/','&','||','>','<','==']:
            left = getValue(quadruples[current].addr1,memories)
            right = getValue(quadruples[current].addr2,memories)
            resultAddr = int(quadruples[current].addr3)

            if operation == '+':
                result = left + right
            elif operation == '-':
                result = left - right
            elif operation == '*':
                result = left * right
            elif operation == '/':
                result = left / right
            elif operation == '&':
                result = left and right
            elif operation == '||':
                result = left or right
            elif operation == '>':
                result = left > right
            elif operation == '<':
                result = left < right
            elif operation == '==':
                result = left == right

            setValue(resultAddr,result,memories)
        elif operation == 'ret':
            value = getValue(quadruples[current].addr1,memories)
            addr = int(quadruples[current].addr2)

            setValue(addr,value,memories)
        elif operation == '=':
            assignationType = quadruples[current].addr3
            if  assignationType == 'arreglo':
                arr1 = quadruples[current].addr1
                arr2 = quadruples[current].addr2

                dim1 = quadruples[current+1].addr2
                dim2 = quadruples[current+1].addr3

                if arr1 >= 55000:
                    array = memories['local']['local'].int[arr1]
                    copyArray(array,arr2,dim1,dim2,memories,True)
                else:
                    copyArray(arr1,arr2,dim1,dim2,memories,False)
                stepOne = False
                current +=2
            elif assignationType == 'arrSingle':
                realAddr = memories['local']['temps'].int[quadruples[current].addr2]
                value = getValue(quadruples[current].addr1,memories)
                setValue(realAddr,value,memories)
            else:
                value = getValue(quadruples[current].addr1,memories)
                addr = int(quadruples[current].addr2)
                setValue(addr,value,memories)
        else:
            print(quadruples[current].imprimir())

        if stepOne:
            current +=1
    print(memories['local']['temps'].int)
    print(memories['ctes'].int)
    #     # elif operation == 'goto':

if __name__ == '__main__':
    main()
