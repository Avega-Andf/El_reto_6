from punto7pero1 import*
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