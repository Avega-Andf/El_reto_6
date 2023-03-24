# EL RETO 6
### Dado la figura de la imagen, desarrolle:
[![imagen-2023-03-23-191541403.png](https://i.postimg.cc/135P7bNg/imagen-2023-03-23-191541403.png)](https://postimg.cc/3d6PdS17)

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*


```python
import math
#Para la esfera
def calcular_area_esfera( radio:float) -> float:
  area_esfera = 4*math.pi*(radio**2)
  return area_esfera

def calcular_volumen_esfera(radio:float) -> float:
  volumen_esfera = (4/3)*math.pi*(radio**3)
  return volumen_esfera

#Para el cono
def calcular_area_cono(radio2:float, altura:float) -> float:
  altura_inclinada = (radio2**2 + altura**2)**0.5
  area_cono = math.pi*radio2*(radio2+altura_inclinada)
  return area_cono

def calcular_volumen_cono(radio2:float, altura:float) -> float:
  volumen_cono = (1/3)*math.pi*(radio2**2)*altura
  return volumen_cono

if __name__ == "__main__":
  #esfera
  radio = float(input("Ingrese el radio de la esfera:"))
  areaesfera = calcular_area_esfera(radio)
  volumenesfera = calcular_volumen_esfera(radio)
  #cono
  radio2 = float(input("Ingrese el radio del cono:"))
  altura = float(input("Ingrese la altura del cono:"))
  areacono = calcular_area_cono(radio2,altura)
  volumencono = calcular_volumen_cono(radio2,altura)
 
  #total
  areatotal = (areacono + areaesfera)
  volumentotal = (volumenesfera + volumencono)
  
  print("El area de la esfera es " + str(areaesfera))
  print("El volumen de la esfera es " + str(volumenesfera))
  print("El area del cono es " + str(areacono))
  print("El volumen del cono es " + str(volumencono))
  print("El area total de la figura es " + str(areatotal))
  print("El volumen total de la figura es " + str(volumentotal))
```
Para este punto se realizo las siguientes operaciones para hallar el area y volumen total de la figura:
+ Se calculo el area de la esfera
+ Se calculo el area del cono
+ Se suma ambas areas para hallar el area total
+ Se calcula el volumen de la esfera
+ Se calcula el volumen del cono
+ Se suma ambos volumens para hallar el volumen total
+ Al final el codigo imprime el valor de el volumen total y el de las dos figuras, y el area total y el de las 2 figuras.
+ Ademas se investigo y se empleo la forma de usar `import math` y de `math.py`, para no tener que definir el valor de pi a mano.

### Dado la figura de la imagen, desarrolle:
[![imagen-2023-03-23-191646497.png](https://i.postimg.cc/02Z1SZH9/imagen-2023-03-23-191646497.png)](https://postimg.cc/PPL7sbj7)
```python
import math
#Para el rectangulo
def calcular_area_rectangulo(base:float, altura:float) -> float:
  area_rectangulo = base*altura
  return area_rectangulo

def calcular_perimetro_rectangulo(base:float, altura:float) -> float:
  perimetro_rectangulo = 2*base+2*altura
  return perimetro_rectangulo

#Para los circulos
def calcular_area_circulos(radio:float) -> float:
  area_circulos = math.pi*radio**2
  return area_circulos

def calcular_perimetro_circulos(radio:float) -> float:
  perimetro_circulos = 2*math.pi*radio
  return perimetro_circulos

if __name__ == "__main__":
  #rectangulo
  base = float(input("Ingrese la base del rectangulo:"))
  altura = float(input("Ingrese la altura del rectangulo:"))
  arearectangulo = calcular_area_rectangulo(base,altura)
  perimetrorectangulo = calcular_perimetro_rectangulo(base,altura)
  #circulos
  radio = float(input("Ingrese un radio para los circulos:"))
  areacirculos = calcular_area_circulos(radio)
  perimetrocirculos = calcular_perimetro_circulos(radio)
 
  #total
  areatotal = (arearectangulo + areacirculos+areacirculos)
  perimetrototal = (perimetrocirculos + perimetrorectangulo+perimetrocirculos)
  
  print("El area del rectangulo es " + str(arearectangulo))
  print("El perimetro del rectangulo es " + str(perimetrorectangulo))
  print("El area de los circulos " + str(areacirculos))
  print("El perimetro de los circulos es " + str(perimetrocirculos))
  print("El area total de la figura es " + str(areatotal))
  print("El perimetro total de la figura es " + str(perimetrototal))
```
Para este punto se realizo las siguientes operaciones para hallar el area y perimetro total de la figura:
+ Se calculo el area del rectangulo
+ Se calculo el area de los 2 circulos (Ya que se tuvo en cuenta que los circulos eran iguales por la figura)
+ Se suma ambas areas para hallar el area total
+ Se calcula el perimetro del rectangulo
+ Se calcula el perimetro de los circulos
+ Se suma ambos perimetros para hallar el perimetro total
+ Al final el codigo imprime el valor de el perimetro total, el perimetro de las tres figuras, el area total y el area de las 3 figuras.
+ Ademas se investigo y se empleo la forma de usar `import math` y de `math.py`, para no tener que definir el valor de pi a mano.

### Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen `N` gallinas, `M` gallos y `K` pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def calcularKilodeaves(gallinas : float, gallos : float, pollitos : float):
    kiloaves = 6 * gallinas + 7*gallos + pollitos
    return kiloaves

if __name__ == "__main__":
    N = float(input("ingrese la cantidad de gallinas:"))
    M = float(input("ingrese la cantidad de gallos:"))
    K = float(input("ingrese la cantidad de pollitos:"))
    kilototal = calcularKilodeaves(N, M, K)
    print("La cantidad de kilos totales entre todas las aves es: " + str(kilototal))
```
Este es un codigo simple que define la forma de calcular la cantidad de kilos que hay entre las 3 aves, luego se piden los valores y se realiza la operación.

### Mi mamá me manda a comprar `P` panes a 300 cada uno, `M` bolsas de leche a 3300 cada una y `H` huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de `B` pesos.


```python
def Calcularpreciototal (panes:float, leche:float, huevos:float, dinero:float):
    preciototal = dinero - 300*panes - 3300 * leche - 350*huevos 
    return preciototal

if __name__ == "__main__":
    P=float(input("Ingrese la cantidad de panes que te pidieron comprar:"))
    M=float(input("Ingrese la cantidad de bolsas de leche que te pidieron comprar:"))
    H=float(input("Ingrese la cantidad de huevos que te pidieron comprar:"))
    B=float(input("Ingresa la cantidad de dinero que te dieron"))
    G = Calcularpreciototal(P, M, H, B)
    if G>0:
        print("La cantidad que te sobra es " +str(G)+ " pesos" )
    elif G<0:
        print("la cantidad que te falta es: " +str(-G)+ " pesos") 
    else:
        print("No te sobra ni te falta nada de dinero")
```
### Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.


```python
def Calcularinteres (Dineroinicial:float, Interes : float, Meses : float ):
    Dinerofinal = Dineroinicial * (1+ Interes/100)**Meses
    return Dinerofinal

if __name__ == "__main__":
    C = float(input("Ingresa el dinero incial prestado:"))
    I = float(input("Ingresa el interes:"))
    N = float(input("Ingresa la cantidad de meses:"))
    D = Calcularinteres(A,B,C)
    print("El dinero final es: " + str(D))
```
La operacion de intesres compuesto que se uso es, donde `Cf` es la cantidad final, `Ci` es la cantidad inicial, y `n` es la cantidad de meses :
$$Cf = Ci * (1 + interes)^n$$ 

### El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.


```python
def calcularcontagiados(personas:int, dias:float )-> int:
    contagiados =int(personas * (2 ** dias))
    return contagiados

if __name__ == "__main__":
    C = int(input("ingrese la cantidad inicial de contagiados"))
    D = float(input("ingrese la cantidad de dias a evaluar"))
    T = calcularcontagiados(C,D)
    print("La cantidad de contagiados en Nuncalandia despues de " + str(D) + " dias es: " + str(T))
```
### Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
+ El promedio
+ La mediana
+ El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
+ Ordenar los números de forma ascendente
+ Ordenar los números de forma descendente
+ La potencia del mayor número elevado al menor número
+ La raíz cúbica del menor número

```python
def calcularpromedio(a:float, b:float, c:float, d:float, e:float) -> float:
    promedio = (a+b+c+d+e)/5
    return promedio

def mediana(a:float, b:float, c:float, d:float, e:float) -> float:
    if (a >= b and a >= c and a <= d and a <= e) or (a >= b and a <= c and a >= d and a <= e) or (a >= b and a <= c and a <= d and a >= e) or (a <= b and a >= c and a >= d and a <= e) or ((a <= b and a >= c and a <= d and a >= e)) or ((a <= b and a <= c and a >= d and a >= e)):
        tercero = a
    elif (b >= a and b >= c and b <= d and b <= e) or (b >= a and b <= c and b >= d and b <= e) or (b >= a and b <= c and b <= d and b >= e) or (b <= a and b >= c and b >= d and b <= e) or ((b <= a and b >= c and b <= d and b >= e)) or ((b <= a and b <= c and b >= d and b >= e)):
        tercero = b
    elif (c >= b and c >= a and c <= d and c <= e) or (c >= b and c <= a and c >= d and c <= e) or (c >= b and c <= a and c <= d and c >= e) or (c <= b and c >= a and c >= d and c <= e) or ((c <= b and c >= a and c <= d and c >= e)) or ((c <= b and c <= a and c >= d and c >= e)):
        tercero = c
    elif (d >= b and d >= c and d <= a and d <= e) or (d >= b and d <= c and d >= a and d <= e) or (d >= b and d <= c and d <= a and d >= e) or (d <= b and d >= c and d >= a and d <= e) or ((d <= b and d >= c and d <= e and d >= e)) or ((d <= b and d <= c and d >= e and d >= e)):
        tercero = d
    else:
        tercero = e
    return tercero

def calcularprommultiplicatico(a:float, b:float, c:float, d:float, e:float) -> float:
    prommulti = (a*b*c*d*e)**(1/5)
    return prommulti

def ordenar(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        primero = a
    elif b <= a and b <= c and b <= d and b <= e :
        primero = b
    elif c <= a and c <= b and c <= d and c <= e :
        primero = c
    elif d <= a and d <= b and d <= c and d <= e :
        primero = d
    else :
        primero = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        segundo = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
        segundo = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        segundo = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        segundo = d
    else:
        segundo = e

    if (a >= b and a >= c and a <= d and a <= e) or (a >= b and a <= c and a >= d and a <= e) or (a >= b and a <= c and a <= d and a >= e) or (a <= b and a >= c and a >= d and a <= e) or ((a <= b and a >= c and a <= d and a >= e)) or ((a <= b and a <= c and a >= d and a >= e)):
        tercero = a
    elif (b >= a and b >= c and b <= d and b <= e) or (b >= a and b <= c and b >= d and b <= e) or (b >= a and b <= c and b <= d and b >= e) or (b <= a and b >= c and b >= d and b <= e) or ((b <= a and b >= c and b <= d and b >= e)) or ((b <= a and b <= c and b >= d and b >= e)):
        tercero = b
    elif (c >= b and c >= a and c <= d and c <= e) or (c >= b and c <= a and c >= d and c <= e) or (c >= b and c <= a and c <= d and c >= e) or (c <= b and c >= a and c >= d and c <= e) or ((c <= b and c >= a and c <= d and c >= e)) or ((c <= b and c <= a and c >= d and c >= e)):
        tercero = c
    elif (d >= b and d >= c and d <= a and d <= e) or (d >= b and d <= c and d >= a and d <= e) or (d >= b and d <= c and d <= a and d >= e) or (d <= b and d >= c and d >= a and d <= e) or ((d <= b and d >= c and d <= e and d >= e)) or ((d <= b and d <= c and d >= e and d >= e)):
        tercero = d
    else:
        tercero = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        cuarto = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        cuarto = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        cuarto = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        cuarto = d
    else:
        cuarto = e

    if a >= b and a >= c and a >= d and a >= e :
        quinto = a
    elif b >= a and b >= c and b >= d and b >= e :
        quinto = b
    elif c >= a and c >= b and c >= d and c >= e :
        quinto = c
    elif d >= a and d >= b and d >= c and d >= e :
        quinto = d
    else:
        quinto = e
    menoramayor=(primero,segundo,tercero,cuarto,quinto)
    return menoramayor


def ordenar2(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        primero = a
    elif b <= a and b <= c and b <= d and b <= e :
        primero = b
    elif c <= a and c <= b and c <= d and c <= e :
        primero = c
    elif d <= a and d <= b and d <= c and d <= e :
        primero = d
    else :
        primero = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        segundo = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
        segundo = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        segundo = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        segundo = d
    else:
        segundo = e

    if (a >= b and a >= c and a <= d and a <= e) or (a >= b and a <= c and a >= d and a <= e) or (a >= b and a <= c and a <= d and a >= e) or (a <= b and a >= c and a >= d and a <= e) or ((a <= b and a >= c and a <= d and a >= e)) or ((a <= b and a <= c and a >= d and a >= e)):
        tercero = a
    elif (b >= a and b >= c and b <= d and b <= e) or (b >= a and b <= c and b >= d and b <= e) or (b >= a and b <= c and b <= d and b >= e) or (b <= a and b >= c and b >= d and b <= e) or ((b <= a and b >= c and b <= d and b >= e)) or ((b <= a and b <= c and b >= d and b >= e)):
        tercero = b
    elif (c >= b and c >= a and c <= d and c <= e) or (c >= b and c <= a and c >= d and c <= e) or (c >= b and c <= a and c <= d and c >= e) or (c <= b and c >= a and c >= d and c <= e) or ((c <= b and c >= a and c <= d and c >= e)) or ((c <= b and c <= a and c >= d and c >= e)):
        tercero = c
    elif (d >= b and d >= c and d <= a and d <= e) or (d >= b and d <= c and d >= a and d <= e) or (d >= b and d <= c and d <= a and d >= e) or (d <= b and d >= c and d >= a and d <= e) or ((d <= b and d >= c and d <= e and d >= e)) or ((d <= b and d <= c and d >= e and d >= e)):
        tercero = d
    else:
        tercero = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        cuarto = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        cuarto = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        cuarto = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        cuarto = d
    else:
        cuarto = e

    if a >= b and a >= c and a >= d and a >= e :
        quinto = a
    elif b >= a and b >= c and b >= d and b >= e :
        quinto = b
    elif c >= a and c >= b and c >= d and c >= e :
        quinto = c
    elif d >= a and d >= b and d >= c and d >= e :
        quinto = d
    else:
        quinto = e

    ordenar2 = (quinto, cuarto, tercero, segundo, primero)

    return ordenar2

def calcularpotencia(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        primero = a
    elif b <= a and b <= c and b <= d and b <= e :
        primero = b
    elif c <= a and c <= b and c <= d and c <= e :
        primero = c
    elif d <= a and d <= b and d <= c and d <= e :
        primero = d
    else :
        primero = e

    if a >= b and a >= c and a >= d and a >= e :
        quinto = a
    elif b >= a and b >= c and b >= d and b >= e :
        quinto = b
    elif c >= a and c >= b and c >= d and c >= e :
        quinto = c
    elif d >= a and d >= b and d >= c and d >= e :
        quinto = d
    else:
        quinto = e

    elevado = quinto**primero


    return elevado

def calcularraiz(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        primero = a
    elif b <= a and b <= c and b <= d and b <= e :
        primero = b
    elif c <= a and c <= b and c <= d and c <= e :
        primero = c
    elif d <= a and d <= b and d <= c and d <= e :
        primero = d
    else :
        primero = e

    raiz = (primero)**0.5
    return raiz
    


if __name__ == "__main__":
    m1 = float(input("ingrese el primer numero"))
    m2 = float(input("ingrese el segundo numero"))
    m3 = float(input("ingrese el tercer numero"))
    m4 = float(input("ingrese el cuarto numero"))
    m5 = float(input("ingrese el quinto numero"))
    orden = ordenar(m1, m2, m3, m4, m5)
    orden2 = ordenar2(m1, m2, m3, m4, m5)
    median = mediana(m1, m2, m3, m4, m5)
    promedio = calcularpromedio(m1, m2, m3, m4, m5)
    promulti = calcularprommultiplicatico(m1, m2, m3, m4, m5)
    potencia = calcularpotencia(m1, m2, m3, m4, m5)
    raiz = calcularraiz(m1, m2, m3, m4, m5)
    print("los numeros ordenados de menor a mayor son: " +str(orden))
    print("los numeros ordenados de mayor a menor son: " +str(orden2))
    print("la mediana de los numeros es: " +str(median))
    print("el promedio es: " +str(promedio))
    print("el promedio multiplicativo es: " +str(promulti))
    print("El numero mayor elevado al menor es: " +str(potencia) )
    print ("la raiz del numero menor es:" +str(raiz))
```
### Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

Se guardaron las funciones en el archivo:
[![imagen-2023-03-23-191107783.png](https://i.postimg.cc/wBQvRDJJ/imagen-2023-03-23-191107783.png)](https://postimg.cc/kVD9k6TX)
Se adjunta imagenes del codigo (pero de forma minimizada para que se vea completp)
[![imagen-2023-03-23-190940190.png](https://i.postimg.cc/hGLJ8kFX/imagen-2023-03-23-190940190.png)](https://postimg.cc/kV5XqhgC)
[![imagen-2023-03-23-191026724.png](https://i.postimg.cc/2yK38mWK/imagen-2023-03-23-191026724.png)](https://postimg.cc/LgjmNcNt)
Y en el archivo:
[![imagen-2023-03-23-191246596.png](https://i.postimg.cc/mDcgXJJ3/imagen-2023-03-23-191246596.png)](https://postimg.cc/hzBnhySh)
Se escribio:
[![imagen-2023-03-23-191346166.png](https://i.postimg.cc/HWyLQGQd/imagen-2023-03-23-191346166.png)](https://postimg.cc/G9brC575)
Y se evidencio que funciono al ejecutarlo:
[![imagen-2023-03-23-191444350.png](https://i.postimg.cc/fycZ1NKd/imagen-2023-03-23-191444350.png)](https://postimg.cc/64pDGFF6)








### PIP (Paquete de Instalación de Python)
Es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 

Estos paquetes son una forma de compartir y reutilizar el código en diferentes proyectos y comunidades.

PIP funciona a través de la línea de comandos de la terminal de Python. 



### Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

Para instalar un paquete con PIP, debe escribir "pip install" seguido del nombre del paquete que desea instalar.
PIP buscará el paquete en su repositorio central y lo descargará e instalará automáticamente en su sistema.
Unos ejemplos de los que se pueden instalar son:

NumPy: un paquete para realizar cálculos numéricos en Python.
Para instalarlo: 
```
pip install numpy
```
Pandas: una biblioteca para el análisis de datos en Python.
Para instalarlo:
```
pip install pandas
```

Matplotlib: una biblioteca para visualización de datos en Python.
Para instalarlo:
```
pip install matplotlib
```
Scikit-learn: una biblioteca de aprendizaje automático para Python.
Para instalarlo:
```
pip install scikit-learn
```
TensorFlow: una biblioteca de aprendizaje automático de código abierto desarrollada por Google.
Para instalarlo: 
```
pip install tensorflow
```
Pygame: una biblioteca para desarrollar videojuegos en Python.
Para instalarlo:
```
pip install pygame
```
Pillow: una biblioteca para procesamiento de imágenes en Python.
Para instalarlo: 
```
pip install pillow
```

Flask: un marco web ligero para Python.
Para instalarlo: 
```
pip install flask
```
Django: un marco web completo para Python.
Para instalarlo: 
```
pip install django
```
Requests: una biblioteca para hacer solicitudes HTTP en Python.
Para instalarlo: 
```
pip install requests
```
Ejemplo:
[![imagen-2023-03-23-192127906.png](https://i.postimg.cc/L5wfQjx5/imagen-2023-03-23-192127906.png)](https://postimg.cc/9wPrrw5H)
Gracias por leer :D.