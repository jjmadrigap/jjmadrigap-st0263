from redis import StrictRedis
import sys

hostname=sys.argv[1]
password=sys.argv[2]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

try:
    print("Se va a leer de redis pofavor ingrese los datos")
    llave= input("Ingrese la llave/key que quiere leer: ")
    valor= r.get(llave)
    print("Key: " + str(llave) + ", valor= " + str(valor))
    print("Se leyo correctamente")
except:
    print("Hubo un error al intentar leer")