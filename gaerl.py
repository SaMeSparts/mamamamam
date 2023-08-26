hello = "e"

lista={"uva":20,"naranja":40}
lista["manzana"]=30
lista["limon"]=90
for listaf in lista.items():
    print(listaf)

propio=str(input("¿Qué producto quieres? "))
if propio.lower()=="uva" or propio.lower()=="naranja" or propio.lower()=="manzana" or propio.lower()=="limon":
    propios=str(input("¿Qué producto quieres?, si no quieres mas escribe (n) "))
    if propios.lower()=="uva" or propio.lower()=="naranja" or propio.lower()=="manzana" or propio.lower()=="limon":
        print("Ahorita le damos el precio")
    elif propios.lower()=="n":
        print("Ahorita le damos el precio")
    else:
        print("Escribe algo de la lista")
elif propio.lower()=="n":
    print("Ahorita le damos el precio")
else:
    print("Escribe algo de la lista")



if propio.lower()=="uva" and propios.lower()=="uva":
    print("el precio de tu compra es de:{}".format({lista["uva"]+lista["uva"]}))
elif propio.lower()=="uva" and propios.lower()=="manzana":
    print("el precio de tu compra es de:{}".format({lista["uva"]+lista["manzana"]}))
elif propio.lower()=="uva" and propios.lower()=="limon":
    print("el precio de tu compra es de:{}".format({lista["uva"]+lista["limon"]}))
elif propio.lower()=="uva" and propios.lower()=="naranja":
    print("el precio de tu compra es de:{}".format({lista["uva"]+lista["naranja"]}))
elif propio.lower()=="uva" and propios.lower()=="n":
    print("el precio de tu compra es de:{}".format({lista["uva"]}))
elif propio.lower()=="n" and propios.lower()=="uva":
    print("el precio de tu compra es de:{}".format({lista["uva"]}))

if propio.lower()=="limon" and propios.lower()=="uva":
    print("el precio de tu compra es de:{}".format({lista["limon"]+lista["uva"]}))
elif propio.lower()=="limon" and propios.lower()=="manzana":
    print("el precio de tu compra es de:{}".format({lista["limon"]+lista["manzana"]}))
elif propio.lower()=="limon" and propios.lower()=="limon":
    print("el precio de tu compra es de:{}".format({lista["limon"]+lista["limon"]}))
elif propio.lower()=="limon" and propios.lower()=="naranja":
    print("el precio de tu compra es de:{}".format({lista["limon"]+lista["naranja"]}))
elif propio.lower()=="limon" and propios.lower()=="n":
    print("el precio de tu compra es de:{}".format({lista["limon"]}))
elif propio.lower()=="n" and propios.lower()=="limon":
    print("el precio de tu compra es de:{}".format({lista["limon"]}))

if propio.lower()=="manzana" and propios.lower()=="uva":
    print("el precio de tu compra es de:{}".format({lista["manzana"]+lista["uva"]}))
elif propio.lower()=="manzana" and propios.lower()=="manzana":
    print("el precio de tu compra es de:{}".format({lista["manzana"]+lista["manzana"]}))
elif propio.lower()=="manzana" and propios.lower()=="limon":
    print("el precio de tu compra es de:{}".format({lista["manzana"]+lista["limon"]}))
elif propio.lower()=="manzana" and propios.lower()=="naranja":
    print("el precio de tu compra es de:{}".format({lista["manzana"]+lista["naranja"]}))
elif propio.lower()=="manzana" and propios.lower()=="n":
    print("el precio de tu compra es de:{}".format({lista["manzana"]}))
elif propio.lower()=="n" and propios.lower()=="manzana":
    print("el precio de tu compra es de:{}".format({lista["manzana"]}))

if propio.lower()=="naranja" and propios.lower()=="uva":
    print("el precio de tu compra es de:{}".format({lista["naranja"]+lista["uva"]}))
elif propio.lower()=="naranja" and propios.lower()=="manzana":
    print("el precio de tu compra es de:{}".format({lista["naranja"]+lista["manzana"]}))
elif propio.lower()=="naranja" and propios.lower()=="limon":
    print("el precio de tu compra es de:{}".format({lista["naranja"]+lista["limon"]}))
elif propio.lower()=="naranja" and propios.lower()=="naranja":
    print("el precio de tu compra es de:{}".format({lista["naranja"]+lista["naranja"]}))
elif propio.lower()=="naranja" and propios.lower()=="n":
    print("el precio de tu compra es de:{}".format({lista["naranja"]}))
elif propio.lower()=="n" and propios.lower()=="naranja":
    print("el precio de tu compra es de:{}".format({lista["naranja"]}))