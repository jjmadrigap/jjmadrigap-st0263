from redis import StrictRedis
import sys

hostname=sys.argv[1]
password=sys.argv[2]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

try:
    print("Se va a escribir en redis pofavor ingrese los datos")
    llave= input("Ingrese la llave/key para la escritura: ")
    valor= input("Ingrese el el dato/value que quiera escribir: ")
    r.set(llave,valor)
    print("Se logro escribir correctamente")
except:
    print("Hubo un error al intentar escribir")