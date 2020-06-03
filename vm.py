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
        self.currentFunction = 'global'

    def execute(self):
        """Función principal de la VM, se va recorriendo por los cuadruplos y hace las funciones
        correspondientes para que todo se ejecute bien.
        """
        quadruples = self.quadruples
        stackMemories = []
        stackNameFunctions = []
        stackParams = []
        stackPointers = []
        current = 0
        while current != len(quadruples) - 1:
            stepOne = True
            # print(memories['local']['temps'].int)
            operation = quadruples[current].op
            addr1 = quadruples[current].addr1
            addr2 = quadruples[current].addr2
            addr3 = quadruples[current].addr3
            if operation == 'goto':
                newPointer = addr1 - 1
                current = newPointer
                # print(nuevo)
                stepOne = False
            elif operation == 'gotof':
                stepOne = False
                value = self.getValue(addr1)
                newPointer = addr2 - 1

                if not value:
                    current = newPointer
                else:
                    current += 1
            elif operation == 'gotov':
                stepOne = False
                value = self.getValue(addr1)
                newPointer = addr2 - 1

                if not value:
                    current += 1
                else:
                    current = newPointer
            elif operation == 'era':
                newMemory = {'temps': Memory(), 'local': Memory()}
                
            elif operation == 'param':
                if addr3 == 'arreglo':
                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3
                    arreglo = self.tempArray(addr1,dim1,dim2)
                    # print(arreglo)
                    stackParams.append({'addr': addr2,'value': arreglo,'array': True,'dim1':dim1,'dim2':dim2})
                    stepOne = False
                    current += 2
                else:
                    stackParams.append({'addr': addr2,'value': self.getValue(addr1)})
            elif operation == 'gosub':
                stackMemories.append(self.memories['local'])
                stackNameFunctions.append(self.currentFunction)

                self.memories['local'] = newMemory
                self.currentFunction = addr1
                for param in stackParams:
                    isArray = param.get('array', None)
                    if isArray != None:
                        self.copyArray(param['value'],param['addr'],param['dim1'],param['dim2'],True)
                    else:
                        self.setValue(param['addr'],param['value'])
                stackParams = []
                newPointer = addr2 - 1
                stackPointers.append(addr3)

                stepOne = False
                current = newPointer
            elif operation == 'endproc':
                stepOne = False

                current = stackPointers.pop()
                self.currentFunction = stackNameFunctions.pop()
                self.memories['local'] = stackMemories.pop()
            elif operation == 'print':
                # print(self.memories['local']['temps'].int)
                # print(self.memories['global'].int)
                if type(addr1) is str:
                    # print("entre")
                    print(addr1)
                else:
                    if addr1 >= 55000:
                        array = self.memories['local']['local'].int[addr1]
                        print(array)
                    elif addr3 == 'arreglo':
                        dim1 = quadruples[current+1].addr2
                        dim2 = quadruples[current+1].addr3
                        self.printArray(addr1,dim1,dim2)
                        stepOne = False
                        current += 2
                    else:
                        value = self.getValue(int(addr1))
                        print(value)
            elif operation == 'lee':
                # print(addr)
                value = input()
                if addr1 > 49999:
                    addr1 = self.memories['local']['temps'].int[addr1]
                self.setValue(addr1,value)
            elif operation == 'verify':
                value = self.getValue(int(addr1))
                baseAddr = self.getValue(int(addr2))
                limit = addr3
                if value > limit:
                    self.error(baseAddr,2)
            elif operation in ['%','#','$','@','~','?','!']:
                dim1 = quadruples[current+1].addr2
                dim2 = quadruples[current+1].addr3
                if operation not in ['!','?']:
                    value = self.specialArray(operation,addr1,dim1,dim2)
                    self.setValue(addr3,value)
                else:
                    value = self.specialArray(operation,addr1,dim1,dim2,addr3)
                stepOne = False
                current += 2
            elif operation in ['*Arreglos','/Arreglos','+Arreglos','-Arreglos']:
                op = operation[0]

                dim1 = quadruples[current+1].addr2
                dim2 = quadruples[current+1].addr3
                # print("ds",dim1,dim2)
                if addr1 >= 55000:
                    array = self.memories['local']['local'].int[addr1]
                    # print(array)
                    self.aritmeticArray(op,array,addr2,dim1,dim2,addr3,True)
                else:
                    self.aritmeticArray(op,addr1,addr2,dim1,dim2,addr3,False)
                stepOne = False
                current +=2
            elif operation in ['+','-','*','/','&','||','>','<','==']:
                left = self.getValue(addr1)
                right = self.getValue(addr2)

                result = self.aritmetic(operation,left,right)

                self.setValue(addr3,result)
            elif operation == 'ret':
                value = self.getValue(addr1)
                if addr3 == 'arreglo':
                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3
                    arreglo = self.tempArray(addr1,dim1,dim2)
                    self.memories['global'].int[addr2] = arreglo
                else:
                    self.setValue(addr2,value)
                stepOne = False
                current = stackPointers.pop()
                self.currentFunction = stackNameFunctions.pop()
                self.memories['local'] = stackMemories.pop()
            elif operation == '=':
                assignationType = addr3
                if assignationType == 'arreglo':
                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3

                    if addr1 >= 55000:
                        array = self.memories['local']['local'].int[addr1]
                        self.copyArray(array,addr2,dim1,dim2,True)
                    else:
                        self.copyArray(addr1,addr2,dim1,dim2,False)
                    stepOne = False
                    current +=2
                elif assignationType == 'retArray':
                    array = self.memories['global'].int[addr1]
                    if quadruples[current+1].op == '=':
                        addr2 = quadruples[current+1].addr2
                        dim1 = quadruples[current+2].addr2
                        dim2 = quadruples[current+2].addr3
                        self.copyArray(array,addr2,dim1,dim2,True)
                        stepOne = False
                        current +=3
                    elif quadruples[current+1].op == 'print':
                        print(array)
                        stepOne = False
                        current +=2
                    else:
                        self.memories['local']['local'].int[addr2] = array
                elif assignationType == 'arrWhole':
                    valor = self.getValue(addr1)

                    dim1 = quadruples[current+1].addr2
                    dim2 = quadruples[current+1].addr3
                    self.asignArray(addr2,valor,dim1,dim2)
                    stepOne = False
                    current +=2
                elif assignationType == 'arrSingle':
                    # print("si entreaaaa")
                    realAddr = self.memories['local']['temps'].int[addr2]
                    value = self.getValue(addr1)
                    self.setValue(realAddr,value)
                else:
                    value = self.getValue(addr1)
                    self.setValue(addr2,value)
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
        if addr < 15000:
            varName = self.addrNames['global'][addr]['var']
            pos1 = self.addrNames['global'][addr].get('pos1', None)
            pos2 = self.addrNames['global'][addr].get('pos2', None)
        else:
            varName = self.addrNames[self.currentFunction][addr]['var']
            pos1 = self.addrNames[self.currentFunction][addr].get('pos1', None)
            pos2 = self.addrNames[self.currentFunction][addr].get('pos2', None)
        if type == 1:
            if pos1 == None and pos2 == None:
                var = varName
            elif pos1 != None and pos2 == None:
                var = "{}[{}]".format(varName,pos1)
            elif pos1 != None and pos2 != None:
                var = "{}[{}][{}]".format(varName,pos1,pos2)
            msg = "Variable '{}' no asignada.".format(var)
        elif type == 2:
            msg = "Arreglo '{}' fuera de los límites.".format(varName)
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

    def aritmetic(self,operation,left,right):
        """Función que hace realiza las operaciones artimeticas de un elemento normal (no arreglo/matriz)

        Arguments:
            operation {string} -- Tipo de operación a realizar
            left {int|float|bool|char} -- Operando izquierdo
            right {int|float|bool|char} -- Operando derecho

        Returns:
            int|float|bool|char -- Resultado de la operación
        """
        if operation == '+':
            result = left + right
        elif operation == '-':
            result = left - right
        elif operation == '*':
            result = left * right
        elif operation == '/':
            try:
                result = left / right
            except ZeroDivisionError:
                print('Error -> División entre 0.')
                exit()
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
        return result

    def aritmeticArray(self,op,arr1,arr2,dim1,dim2,res,isArray):
        """Función que ayuda a que se puedan realizar operaciones aritmeticas con los arreglos/matrices

        Arguments:
            op {string} -- El tipo de operación a realizar
            arr1 {int|npArray} -- La dirección base del arreglo1 o el arreglo ya en numpy
            arr2 {int} -- La dirección base del arreglo 2
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior
            res {int} -- La dirección donde se va a guardar el resultado
            isArray {bool} -- Te dice si uno de los arreglos ya se transformó en un npArray previamente
        """
        np.seterr(all = "raise")
        if isArray:
            npArray1 = arr1
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

        if op == '+':
            matrizResultado = np.add(npArray1, npArray2)
        elif op == '-':
            matrizResultado = np.subtract(npArray1, npArray2)
        elif op == '*':
            try:
                matrizResultado = np.multiply(npArray1, npArray2)
            except:
                print("Error -> No se puede multiplicar una matriz por una constante.")
                exit()
        elif op == '/':
            try:
                matrizResultado = np.divide(npArray1, npArray2)
            except FloatingPointError:
                print("Error -> No se puede dividir una matriz entre 0.")
                exit()
        self.memories['local']['local'].int[res] = matrizResultado
        # print("aqui",memories['local']['local'].int[res])

    def specialArray(self,op,addr,dim1,dim2,res=False):
        """Función que ayuda a que se puedan realizar las operaciones especiales sobre los arreglos

        Arguments:
            op {string} -- El tipo de operación a realizar
            addr {int} -- La dirección base del arreglo
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior

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
            try:
                result = np.linalg.inv(npArray)
            except np.linalg.LinAlgError as err:
                if 'Singular matrix' in str(err):
                    print("Error -> No se puede calcular la inversa de una singular matrix.")
                    exit()
                else:
                    raise
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
            self.memories['local']['local'].int[res] = result

    def copyArray(self,arr1,arr2,dim1,dim2,isArray):
        """Copia todos los elementos de un arreglo a otro, sirve para la asignación de un arreglo a otro

        Arguments:
            arr1 {int} -- La dirección base del arreglo 1 (de donde se copia)
            arr2 {int} -- La dirección base del arreglo 2 (a donde se copia)
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior
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
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior
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

    def asignArray(self,addr,value,dim1,dim2):
        """Función que asigna un valor a todo un arreglo/matriz en la memoria

        Arguments:
            addr {int} -- Dirección base del arreglo
            value {int|float|char} -- Valor a asignar a toda la matriz
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior
        """
        if dim2 == False:
            for i in range(dim1):
                self.setValue(addr+i,value)
        else:
            for i in range(dim1):
                for j in range(dim2):
                    relativeAddr = i * dim2 + j
                    self.setValue(addr+relativeAddr,value)

    def tempArray(self,addr,dim1,dim2):
        """Función que toma un arreglo y lo pone en un arreglo de numpy, sirve para cuando tienes
        que pasar como parametro un arreglo/matriz o regresar un arreglo/matriz

        Arguments:
            addr {int} -- Dirección base del arreglo
            dim1 {int} -- Limite superior de la dim1
            dim2 {int|bool} -- Falso si no tiene dim2 o un int con el limite superior

        Returns:
            npArray -- Arreglo/matriz en formato numpy
        """
        array1 = []
        if dim2 == False:
            for i in range(dim1):
                array1.append(self.getValue(addr+i))
            npArray = np.array(array1)
        else:
            for i in range(dim1):
                for j in range(dim2):
                    relativeAddr = i * dim2 + j
                    array1.append(self.getValue(addr+relativeAddr))
            npArray = np.array(array1).reshape(dim1, dim2)
        return npArray


def main():
    """Función que toma el nombre del archivo y se lo pasa a una instancia de la VM
    """
    arch = sys.argv[1]
    vm = VirtualMachine(arch)
    vm.execute()

if __name__ == '__main__':
    main()
