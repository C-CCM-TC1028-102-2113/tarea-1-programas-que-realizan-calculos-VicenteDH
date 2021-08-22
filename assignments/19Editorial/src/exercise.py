def main():
    #escribe tu código abajo de esta línea
    palabras=int(input("Dame el número de palabras: "))
    pag=palabras/475
    total=pag*60
    descuento=total*.1
    total1=total-descuento
    total1=round(total1,1)
    print("El costo de la publicación es: "+str(total1))
    pass

if __name__ == '__main__':
    main()
