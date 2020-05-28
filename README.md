

# Patito++

 - Proyecto final - Diseño de compiladores
 - Febrero - Junio 2020
 - Equipo 14

## README Index

 - [Quick Reference Manual](#quick-reference-manual)
	 - [Programa](#programa)
	 - [Variables](#variables)
	 - [Funciones](#funciones)
	 - [Ejemplos](#ejemplos)
  - [Instalación](#instalación)
  -  [Equipo](#equipo)

# Quick Reference Manual
## Programa
Para generar un programa en `Patito++` se necesita la siguiente sintaxis

    programa nombrePrograma;


Seguido por su declaración de variables y funciones.

## Variables
Las variables son definidas después de la declaración del programa o de la función.

### Tipos
`Patito++` cuenta con los tipos tradicionales definidos:
* int
* float
* char

### Arreglos y matrices
`Patito++` cuenta con una declaración de arreglos/matrices de tipo C por lo que todos inician en 0 y terminan en un numero entero definido por el usuario.

### Ejemplo

    var
	    tipo : nombre;
	    tipo : nombre[5];
	    tipo : nombre[5][3];

## Funciones
Dentro de `Patito++` se pueden definir 0 o más funciones para cada programa.

Las funciones no pueden tomar como parámetros variables dimensionadas.

Los tipos de retorno de una función son los previamente mencionados y void.

    funcion tipoRetorno nombreFuncion(tipoParametro : nombre)
    {
	    estatuto;
    }

### Lectura
Se pueden leer una o más variables(con o sin dimensiones) separadas por comas.

    lee(nombreVar,nombreVar[dim]);

### Escritura
Se pueden escribir tanto letreros(strings constantes) y/o expresiones separadas por comas.

    escribe("letrero",100*2,"otro letrero");

### Expresiones
`Patito++` soporta las siguientes expresiones aritméticas:

**Normales**
| Operación | Operando |
|--|--|
| Suma | `+` |
| Resta | `-` |
| Multiplicación | `*` |
| División | `/` |
| Comparación | `==` |
| Mayor que | `*` |
| Menor que | `/` |
| AND | `==` |
| OR | `||`|


**Matrices**


| Operación | Operando |
|--|--|
| Suma | `+` |
| Resta | `-` |
| División | `/` |
| Multiplicación | `*` |
| Transpuesta | `!` |
| Inversa | `?` |
| Determinante | `$` |
| Mínimo | `~` |
| Máximo | `#` |
| Sumatoria | `@` |
| Promedio | `%` |

### Asignación
A una variable (con o sin dimensiones)  le puedes asignar una expresión.
A una matriz se le puede asignar otra si sus dimensiones lo permiten.

    nombre = 100 * 100;
    nombre[10] = 40;
    matriz = otraMatriz;
    nombre = llamadaFuncion(param,param) + 100;

### Ciclos
`Patito++` soporta ciclos condicionales y no condicionales.

**Condicionales**


    mientras (expresion) haz
    {
	    estatuto;
    }
**No condicionales**

    desde variable=expresion hasta expresion hacer
    {
	    estatuto;
    }

### Decisiones
Puede o no tener un camino alternativo(else).

    si (expresion) entonces
    {
	    estatuto;
    }
    sino
    {
	    estatuto;
    }

### Llamadas a funciones
Los parámetros de una llamada están conformados por expresiones.

    nombreFuncion(expresion,expresion);

### Retorno
Si una función no es void tiene que regresar un valor en la forma de una expresión.

    regresa(expresion);


### Ejemplos
**Función normal**

    funcion tipo nombreFuncion(tipo nombre);
    var
	    tipo : nombreVar;
	{
		lee(nombreVar);
		escribe("letrero",nombreVar);
		si (nombreVar > 5) entonces {
			nombre = 100 * 2;
		}
		sino {
			nombre = 100 / 2;
		}
		escribe("resultado:",nombre);
	}

**Función main**

    principal()
    {
	    nombreFuncion(param1,param2);
	    variable = 100 * 50 - 10 / 5;
	    escribe(variable);
    }

# Instalación

Para instalar este lenguaje es necesario contar con Python 3 instalado. Esto se puede verificar corriendo el comando `python3` en la terminal.

Una vez instalado Python 3 podemos proceder a instalar el lenguaje.

    git clone https://github.com/DianaBarrios/PatitoMasMas.git
    pip install -r requirements.txt


# Equipo

|  **Alberto Juarez** | **Diana Barrios** |
| :---: |:---:|
|  ![foto1](https://avatars3.githubusercontent.com/u/21068627?v=3&s=200) | ![foto2](https://avatars3.githubusercontent.com/u/21281689?v=3&s=200)  |
|  A0128913 | A00819792 |
