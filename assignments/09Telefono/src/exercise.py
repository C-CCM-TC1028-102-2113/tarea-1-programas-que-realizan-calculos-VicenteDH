def main():
    #escribe tu código abajo de esta línea
    sms=int(input("Dame el número de mensajes: "))
    mega=float(input("Dame el número de megas: "))
    min=int(input("Dame el número de minutos: "))
    sms2=sms*0.80
    mega2=mega*0.80
    min2=min*0.80
    total=sms2+mega2+min2
    total=round(total,2)
    print("El costo mensual es: "+str(total))
    pass

if __name__ == '__main__':
    main()
