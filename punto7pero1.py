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
    