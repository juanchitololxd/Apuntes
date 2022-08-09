# Libreria de simulacion de lo clasico a lo cuantico 


## Resumen
Esta libreria contiene las siguientes operaciones de cuantica basica:

* Funcion que calcula la probabilidad de encontrar una particula cuantica en una linea con posiciones discretas representada por un ket
* Funcion que calcula la probabilidad de transitar de un ket a otro. En otras palabras la amplitud de transicion.
* Funcion que calcula el valor esperado de una particula al realizar varias mediciones
* Funcion que calcula la varianza de los posibles valor que puede tomar un sistema al realizar una medida
* Funcion que calcula los valores propios de una matriz
* Funcion que calcula la probavilidad de que luego de medir un observable el estado del sistema colaspse a uno de los vectores propios del sistema
* Funcion que calcula el estado final de un sistema, dado su estado inicial y las dinamicas

## Comenzando
Para poder correr correctamente la libreria es importante fijarse que se descargen los siguientes archivos:

* basicQuantumTheory.py
* supportFunctions.py
* testBasicQuantumTheory.py

Es importante que se encuentren todos estos archivos pues los primeros 2 juntos completan la libreria que se pidio y el ultimo, es el archivo de puebas de la libreria

## Instalación
1. Para instalar python solo debe ir al sitio web oficial de python.
2. Debe ir a la sección de "Downloads" y descargar la última versión que le recomienda. 
3. Una vez que lo tenga descargado, ejecuta el archivo y le da a instalar.
4. Para Pycharm debe hacer lo mismo, ir al sitio web y buscar la opción "descargar".
5. Ejecuta el archivo y acepta términos y condiciones, para despues darle en instalar.
6. Al tener descargado python, ejecuta Pycharm y abre la carpeta de la libreria de los sistemas.
7. Verá que en un panel de la derecha de Pycharm tendrá todos los archivos de la carpeta que se usaran.
8. Si abre el archivo basicQuantumTheory.py, junto con supportFunctions.py podrá ver todas las operaciones que contiene la librería.
9. Luego si abre el archivo testBasicQuantumTheory.py podra ver las puebas que se hicieron para validar las funciones

## Ejecutar el test
Para ejecutar el test solo debe abrir el archivo testBasicQuantumTheory.py y ejecuta el modulo presionando "ctrl + shift + f10" si esta en Windows, si esta en mac solo debe presionar "shift + control + r".

## Prerequisitos
* Python 3.8
* Un editor de texto 

## Discusion ejercicio 4.5.2

Primero el vector generico para una particula con spin seria 

<p align="center">
  <img src="/images/1.png">
</p>

por tanto el vector generico que representaria el spin de otra particula, digamos que sea

<p align="center">
  <img src="/images/2.png">
</p>

Luego el vector que me representara el ensamblamiento de ambos sistemas sera

<p align="center">
  <img src="/images/3.png">
</p>

Luego de esta analogia podemos inferir que para un sistema de n particulas el vector sera 

<p align="center">
  <img src="/images/4.png">
</p>

Es muy largo el escribir varios terminos de la ecuacion pero a la larga se veria que para un sistema de n particulas, los coeficientes de los vectores serian las multiplicaciones de todas las posibles convinaciones de coeficientes del resto de vectores, y lo mismo con los vectores enlazados, estos serian todas las posibles combinaciones que hayan con n vectores. 

## Discusion ejercicio 4.5.3

Si se parte del sistema dado por el libro

<p align="center">
  <img src="/images/5.png">
</p>

se puede deconstruir la ecuacion de estado del ket phi y llegar a 

<p align="center">
  <img src="/images/6.png">
</p>

El sistema aneterior de ecuaciones tendria infinitas soluciones, pero la que considero mas sencilla de todas seria en la que el vector phi fuera el enzamblamiento de los vectores psi y tao como se muestra a continuacion

<p align="center">
  <img src="/images/7.png">
</p>

## Hecho con
* Python - Lenguaje de Programación
* Pycharm - IDE
* Git - Control de versiones
* GitHub - Aloja las versiones de Git


## Autor 
Daniel Sebastian Ochoa Urrego 

## Agradecimientos
Gracias a todos lo que utilicen esta libreria, ojala les sirva <3
