from redis import StrictRedis
import sys

hostname=sys.argv[1]
password=sys.argv[2]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

try:
    print("Se va a actualizar un valor en redis pofavor ingrese los datos")
    llave= input("Ingrese la llave/key a actualizar: ")
    valor= input("Ingrese el el dato/value con el que lo quiere actualizar: ")
    r.set(llave,valor)
    print("Se logro actualizar correctamente")
except:
    print("Hubo un error al intentar actualizar")