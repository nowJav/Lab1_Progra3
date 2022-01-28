inv=float(input("Cantidad que desea empezar a invertir: "))
inte=float(input("Interes anual: "))
dur=int(input("Cantidad de años que desea hacer la inversion: "))

t=str(((inv*inte/100))*dur)
print("El total de intereses generados en",dur," años es de: ",t)