from compiler import Compiler
from compiler import Quadruple
import numpy as np
import sys

# 'global': {'int': 5000, 'float': 8000, 'char': 10000, 'string': 13000, 'bool': 14000},
# 'local': {'int': 15000, 'float': 18000, 'char': 20000, 'string': 23000, 'bool': 24000},
# 'temp': {'int': 25000, 'float': 28000, 'char': 31000, 'string': 33000, 'bool': 34000, 'dir': 50000},
# 'ctes': {'int': 35000, 'float': 38000, 'char': 41000, 'string': 43000, 'bool': 44000}

class Memory():
    def __init__(self):
        self.int = {}
        self.float = {}
        self.char = {}
        self.string = {}
        self.bool = {}

class VirtualMachine():
    def __init__(self,arch):
        """Deja todo listo para que la VM pueda interpretar los cuadruplos
         ,toma las constantes, los cuadruplos y las variables con sus nombres
         del compiler y los pone en variables para usarse en la VM


        Arguments:
            arch {string} -- El nombre del archivo a ejecutar, por default en la carpeta /Pruebas
        """
        c = Compiler(arch)
        self.quadruples, ctes, self.addrNames = c.compile()
        ctesInt =  {key: value for key, value in ctes.items() if key < 38000}
        ctesFloat =  {key: value for key, value in ctes.items() if key > 37999 and key < 41000}
        ctesChar =  {key: value for key, value in ctes.items() if key > 40999}
        memGlobal = Memory()
        memLocal = {'temps': Memory(), 'local': Memory()}
        memCtes = Memory()
        memCtes.int = ctesInt
        memCtes.float = ctesFloat
        memCtes.char = ctesChar
        self.memories = {'global' : memGlobal,'local': memLocal, 'ctes':memCtes}

    def execute(self):
        """Función principal de la VM, se va recorriendo por los cuadruplos y hace las funciones
        correspondientes para que todo se ejecute bien.
        """
        quadruples = self.quadruples
        stackMemories = []
        stackParams = []
        stackPointers = []
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
                value = self.getValue(quadruples[current].addr1)
                newPointer = quadruples[current].addr2

                if not value:
                    current = newPointer
                else:
                    current += 1
            elif operation == 'gotov':
                stepOne = False
                value = self.getValue(quadruples[current].addr1)
                newPointer = quadruples[current].addr2

                if not value:
                    current += 1
                else:
                    current = newPointer
            elif operation == 'era':
                pass
            elif operation == 'param':
                stackParams.append({'addr': quadruples[current].addr2,'value': self.getValue(quadruples[current].addr1)})
            elif operation == 'gosub':
                stackMemories.append(self.memories['local'])
                newMemory = {'temps': Memory(), 'local': Memory()}
                self.memories['local'] = newMemory

                for param in stackParams:
                    self.setValue(param['addr'],param['value'])

                newPointer = quadruples[current].addr2 - 1
                stackPointers.append(quadruples[current].addr3)

                stepOne = False
                current = newPointer
            elif operation == 'endproc':
                stepOne = False

                current = stackPointers.pop()

                self.memories['local'] = stackMemories.pop()
            elif operation == 'print':
                if type(quadruples[current].addr1) is str:
                    # print("entre")
                    print(quadruples[current].addr1)
                else:
                    addr = quadruples[current].addr1
                    if addr >= 55000:
                        array = self.memories['local']['local'].int[addr]
                        print(array)
                    elif quadruples[current].addr3 == 'arreglo':
                        dim1 = quadruples[current+1].addr2
                        dim2 = quadruples[current+1].addr3
                        self.printArray(addr,dim1,dim2)
                        stepOne = False
                        current += 2
                    else:
                        value = self.getValue(int(addr))
                        print(value)
            elif operation == 'lee':
                addr = int(quadruples[current].addr1)
                # print(addr)
                value = input()
                if addr > 49999:
                    addr = self.memories['local']['temps'].int[addr]
                self.setValue(addr,value)
            elif operation == 'verify':
                value = self.getValue(int(quadruples[current].addr1))
                baseAddr = self.getValue(int(quadruples[current].addr2))
                limit = quadruples[current].addr3
                if value > limit:
                    self.error(baseAddr,2)
            elif operation in ['%','#','$','@','~','?','!']:
                addr1 = quadruples[current].addr1
                addr2 = quadruples[current].addr3

                dim1 = quadruples[current+1].addr2
                dim2 = quadruples[current+1].addr3
                if operation not in ['!','?']:
                    value = self.specialArray(operation,addr1,dim1,dim2)
                    self.setValue(addr2,value)
                else:
                    value = self.specialArray(operation,addr1,dim1,dim2,addr2)
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
                    array = self.memories['local']['local'].int[arr1]
                    self.aritmeticArray(op,array,arr2,dim1,dim2,res,True)
                else:
                    self.aritmeticArray(op,arr1,arr2,dim1,dim2,res,False)
                stepOne = False
                current +=2
            elif operation in ['+','-','*','/','&','||','>','<','==']:
                left = self.getValue(quadruples[current].addr1)
                right = self.getValue(quadruples[current].addr2)
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

                self.setValue(resultAddr,result)
            elif operation == 'ret':
                value = getValue(quadruples[current].addr1)
                addr = int(quadruples[current].addr2)

                self.setValue(addr,value)
            elif operation == '=':
                assignationType = quadruples[current].addr3
                if  assignationType == 'arreglo':
                    arr1 = quadruples[current].addr1
                    arr2 = quadruples[current].addr2

                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3

                    if arr1 >= 55000:
                        array = self.memories['local']['local'].int[arr1]
                        self.copyArray(array,arr2,dim1,dim2,True)
                    else:
                        self.copyArray(arr1,arr2,dim1,dim2,False)
                    stepOne = False
                    current +=2
                elif assignationType == 'arrSingle':
                    realAddr = self.memories['local']['temps'].int[quadruples[current].addr2]
                    value = self.getValue(quadruples[current].addr1)
                    self.setValue(realAddr,value)
                else:
                    value = self.getValue(quadruples[current].addr1)
                    addr = int(quadruples[current].addr2)
                    self.setValue(addr,value)
            else:
                print(quadruples[current].imprimir())

            if stepOne:
                current +=1
        # print(self.memories['local']['temps'].int)
        # print(self.memories['ctes'].int)

    def error(self,addr,type):
        """Función que nos ayuda a imprimir los errores, busca el nombre de la variable para que los
           errores sean más significativos para los usuarios y den mejor explicación

        Arguments:
            addr {int} -- Address de la variable que causa el error.
            type {int} -- Tipo de error que se está generando.
        """
        varName = self.addrNames[addr]['var']
        pos1 = self.addrNames[addr].get('pos1', None)
        pos2 = self.addrNames[addr].get('pos2', None)
        if type == 1:
            if pos1 == None and pos2 == None:
                var = varName
            elif pos1 != None and pos2 == None:
                var = "{}[{}]".format(varName,pos1)
            elif pos1 != None and pos2 != None:
                var = "{}[{}][{}]".format(varName,pos1,pos2)
            msg = "Variable '{}' no asignada.".format(var)
        elif type == 2:
            msg = "Variable '{}' fuera de los límites.".format(varName)
        print("Error ->",msg)
        exit()

    def getValue(self,addr):
        """Función que toma un address y lo busca en la memoria, dependiendo de su rango se sabe
           en que memoria se tiene que buscar, si no se encuentra arroja un error con la función error.

        Arguments:
            addr {int} -- El address de la variable a buscar

        Returns:
            [int|float|char|bool|error] -- Regresa el valor del address
        """

        if addr > 49999:
            addr = self.memories['local']['temps'].int[addr]
            # print(dir)
        if addr > 4999 and addr < 15000:
            mem = self.memories['global']
            relative = addr - 5000
            base = 5000
            #global
        elif addr > 14999 and addr < 24000:
            mem = self.memories['local']['local']
            relative = addr - 15000
            base = 15000
            #local
        elif addr > 24999 and addr < 35000:
            mem = self.memories['local']['temps']
            relative = addr - 25000
            base = 25000
            #temp
        elif addr > 34999 and addr < 44000:
            mem = self.memories['ctes']
            relative = addr - 35000
            base = 35000

        realAddr = base+relative

        if relative < 3000:
            try:
              return int(mem.int[realAddr])
            except:
              self.error(realAddr,1)
        elif relative > 2999 and relative < 5000:
            try:
              return float(mem.float[realAddr])
            except:
              self.error(realAddr,1)
        elif relative > 4999 and relative < 8000:
            # print(realAddr)
            try:
              return mem.char[realAddr]
            except:
              self.error(realAddr,1)
        elif relative > 7999 and relative < 9000:
            try:
              return mem.string[realAddr]
            except:
              self.error(realAddr,1)
        elif relative > 8999:
            try:
              return mem.bool[realAddr]
            except:
              self.error(realAddr,1)

        else:
            return False;

    def setValue(self,addr,value):
        """Función que toma un valor y lo pone dentro de la memoria correspondiente dependiendo del rango del address

        Arguments:
            addr {int} -- Address de la variable en la que se guarda el valor
            value {int|float|char|bool} -- El valor que se guarda en el address
        """
        if addr > 4999 and addr < 15000:
            mem = self.memories['global']
            relative = addr - 5000
            base = 5000
            #global
        elif addr > 14999 and addr < 24000:
            mem = self.memories['local']['local']
            relative = addr - 15000
            base = 15000
            #local
        elif addr > 24999 and addr < 35000:
            mem = self.memories['local']['temps']
            relative = addr - 25000
            base = 25000
            #temp
        elif addr > 34999 and addr < 44000:
            mem = self.memories['ctes']
            relative = addr - 35000
            base = 35000
        elif addr > 49999:
            mem = self.memories['local']['temps']
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

    def aritmeticArray(self,op,arr1,arr2,dim1,dim2,res,isArray):
        """Función que ayuda a que se puedan realizar operaciones aritmeticas con los arreglos/matrices

        Arguments:
            op {string} -- El tipo de operación a realizar
            arr1 {int} -- La dirección base del arreglo1
            arr2 {int} -- La dirección base del arreglo 2
            dim1 {int} -- El limite superior de la dim 1
            dim2 {int} -- El limite superior de la dim 2
            res {int} -- La dirección donde se va a guardar el resultado
            isArray {bool} -- Te dice si uno de los arreglos ya se transformó en un npArray previamente
        """
        if not isArray:
            array1 = []
        array2 = []
        if dim2 == False:
            for i in range(dim1):
                if not isArray:
                    dir1 = arr1 + i
                    array1.append(self.getValue(dir1))
                dir2 = arr2 + i
                array2.append(self.getValue(dir2))
            if not isArray:
                npArray1 = np.array(array1)
            npArray2 = np.array(array2)
                # ir sacando cada valor y ponerlo en una matrix
        else:
            for i in range(dim1):
                for j in range(dim2):
                    if not isArray:
                        dir1 = arr1 + i * dim2 + j
                        array1.append(self.getValue(dir1))
                    dir2 = arr2 + i * dim2 + j
                    array2.append(self.getValue(dir2))
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
        self.memories['local']['local'].int[res] = matrizResultado
        # print("aqui",memories['local']['local'].int[res])

    ##funciones especiales
    def specialArray(self,op,addr,dim1,dim2,res=False):
        """Función que ayuda a que se puedan realizar las operaciones especiales sobre los arreglos

        Arguments:
            op {string} -- El tipo de operación a realizar
            addr {int} -- La dirección base del arreglo
            dim1 {int} -- El limite superior de la dim1
            dim2 {int} -- El limite superior de la dim2

        Keyword Arguments:
            res {bool|int} -- Le pasa la dirección a guardar el arreglo de ser necesario (default: {False})

        Returns:
            int|float -- Regresa el valor calculado de la operación especial
        """
        # equis = inv([[-3,1][5,0]])
        # print(equis)
        # b = np.array([[2,3],[4,5]])
        # b = np.linalg.inv(b)
        # print(b)
        arr = []
        if dim2 == False:
            for i in range(dim1):
                arr.append(self.getValue(addr+i))
                # ir sacando cada valor y ponerlo en una matrix
            npArray = np.array(arr)
        else:
            for i in range(dim1):
                for j in range(dim2):
                    realAddr = addr + i * dim2 + j
                    arr.append(self.getValue(realAddr))
            npArray = np.array(arr).reshape(dim1, dim2)
        # print(npArray)

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
            # print(result)
            return result
        else:
            # print("3lseeee",res)
            # print(result)
            self.memories['local']['local'].int[res] = result
        # print("normal")
        # print(npArray)

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
    def copyArray(self,arr1,arr2,dim1,dim2,isArray):
        """Copia todos los elementos de un arreglo a otro, sirve para la asignación de un arreglo a otro

        Arguments:
            arr1 {int} -- La dirección base del arreglo 1
            arr2 {int} -- La dirección base del arreglo 2
            dim1 {int} -- El limite superior de la dim 1
            dim2 {int} -- El limite superior de la dim 2
            isArray {bool} -- Te dice si ya se guardo anteriormente como un npArray
        """
        if dim2 == False:
            for i in range(dim1):
                if isArray:
                    value = arr1[i]
                else:
                    value = self.getValue(arr1+i)
                self.setValue(arr2+i,value)
        else:
            for i in range(dim1):
                for j in range(dim2):
                    relativeAddr = i * dim2 + j
                    if isArray:
                        value = arr1[i][j]
                    else:
                        value = self.getValue(arr1+relativeAddr)
                    self.setValue(arr2+relativeAddr,value)

    def printArray(self,addr,dim1,dim2):
        """Imprime todo un arreglo/matriz

        Arguments:
            addr {int} -- La dirección base del arreglo
            dim1 {int} -- El limite superior de la dim 1
            dim2 {int} -- El limite superior de la dim 2
        """
        array = []
        if dim2 == False:
            for i in range(dim1):
                realAddr = addr + i
                array.append(self.getValue(realAddr))
            npArray = np.array(array)
                # ir sacando cada valor y ponerlo en una matrix
        else:
            for i in range(dim1):
                for j in range(dim2):
                    realAddr = addr + i * dim2 + j
                    array.append(self.getValue(realAddr))
            npArray = np.array(array).reshape(dim1, dim2)
        print(npArray)

def main():
    arch = sys.argv[1]
    vm = VirtualMachine(arch)
    vm.execute()

if __name__ == '__main__':
    main()
