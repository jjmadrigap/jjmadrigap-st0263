from redis import StrictRedis
import sys

hostname=sys.argv[1]
password=sys.argv[2]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

try:
    print("Se va a borrar de redis pofavor ingrese los datos")
    llave= input("Ingrese la llave/key que quiere borrar: ")
    r.delete(llave)
    print("Se lobro borrar correctamente")
except:
    print("Hubo un error al intentar borrar")