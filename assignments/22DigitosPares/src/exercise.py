def main():
    #escribe tu código abajo de esta línea
    digitos=int(input("Dame un número: "))
    par=0
    if digitos>-10000 and digitos<=-1000 or digitos>=1000 and digitos<10000:
        while (digitos>0):
            if digitos%2==0:
                par=par+1
            else: 
                par=par+0
            digitos=digitos//10
        print("El número de dígitos pares es: "+ str(par))
    pass
if __name__ == '__main__':
    main()
