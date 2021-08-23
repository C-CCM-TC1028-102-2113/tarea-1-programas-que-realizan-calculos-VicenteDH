def main():
    #escribe tu código abajo de esta línea
   nuevo=int(input("Dame la cantidad de juegos nuevos: "))
   usado=int(input("Dame la cantidad de juegos usados: ")) 
   nuevo1= nuevo*1000
   usado1= usado*350
   total= nuevo1+usado1
   print("El total de la compra es: "+str(total))
   pass

if __name__ == '__main__':
    main()
