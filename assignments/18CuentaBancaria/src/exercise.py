def main():
    #escribe tu código abajo de esta línea
    mes=float(input("Dame el saldo del mes anterior: "))
    ingreso=float(input("Dame los ingresos: "))
    egreso=float(input("Dame los egresos: "))
    cheque=int(input("Dame el número de cheques: "))
    cheque1=cheque*13
    total=(mes+(ingreso-egreso))-cheque1
    interes=total*0.075
    total1=total-interes
    print("El saldo final de la cuenta es: "+str(total1))
    pass

if __name__ == '__main__':
    main()
