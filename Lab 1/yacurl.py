#
# Trabajo creado Por Juan Jose Madrigal Palacio / 1000059306
# Para ejecutar el programa usar un comando por el estilo (windows) python .\yacurl.py -h 3.217.183.77 -p 80
#
from email import charset, header
from email.header import Header
from importlib import resources
from posixpath import split
import socket
import sys, getopt
from urllib import response
from wsgiref import headers

# "Menu" de usuario mediante el cual se reciben al ejecutar el programa datos del host(pagina web) y el port(puesto) a usar para conectarse
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"Hh:p:",["host=","port="])
    except getopt.GetoptError:
        print ('yacurl.py -h <host> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-H':
            print ('yacurl.py -h <host> -p <port>')
            sys.exit()
        elif opt in ("-h", "--host"):
            host = str(arg)
        elif opt in ("-p", "--port"):
            port = int(arg)
    return host,port

#funcion para separar la la respuesta que se recibe del host en los headers(cabeceras) y el cuerpo con el archivo html
#ademas de aguardar el cuerpo de la respuesta en un archivo
def decodificar(respuesta):
    splitaux1 = respuesta.split(b'\r\n\r\n') #se dibide los headers y el body
    headers = splitaux1[0]
    cuerporsp = splitaux1[1]
    splitaux2 =headers.split(b'\r\n') #se dividen los headers
    estadorespuesta = splitaux2[0]
    heads=dict() #disccionario/lista de los headers
    #se pone el nombre de cada cabecera y sus respectivos datos
    for cabecera in splitaux2[1:]:
        if cabecera == b'':
            continue
        else:
            splitaux3= cabecera.split(b':')
            heads[splitaux3[0].decode()]=':'.join([i.decode() for i in splitaux3[1:]])
    #se guarda el tipo de de dato con el cual se desencriptara el body y si no se da se usa UTF-8
    if 'Content-Type' in heads:
        if 'charset' in heads['Content-Type']:
            ct=heads['Content-Type']
            charset=ct[ct.find('charset=')+len('charset='):]
        else:
            charset= 'UTF-8'
    else:
        charset= 'UTF-8'
    #se decodifica el body y se imprimen tanto los headers y el cuerpo
    cuerporsp = cuerporsp.decode(charset)
    print('Headers',heads)
    print(cuerporsp)
    #se gun el tipo de archivo que se tenga ya sea un html, jpg o pdf segun difa el tipo que diga el host se guarda el archivo localmente
    content_type=heads['Content-Type'].split(';')[0]
    if(content_type==' text/html'):
        with open('Pagina.html','w',encoding='UTF-8') as archivodl:
            archivodl.write(cuerporsp)
    elif(content_type==' application/pdf'):
        with open('UnPDF.pdf','w') as archivodl:
            archivodl.write(cuerporsp)
    elif(content_type==' image/jpeg'):
        with open('UnaImagenJPG.jpg','w') as archivodl:
            archivodl.write(cuerporsp)

#Funcion principal para correr la app
if __name__ == "__main__":
    #se reciben los datos y se imprimen los datos del mensaje que se envia al host
    host,port=main(sys.argv[1:])
    print ('Host ', host)
    print ('Port ', port)
    #se envian los datos al host por el puerto especificado y se recibe el mensaje del mismo el cual luego se pasa por la funcion decodificar
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        naisu= f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
        s.sendall(naisu)
        data = b''
        respuesahost = s.recv(1024)
        while respuesahost:
            data += respuesahost
            respuesahost = s.recv(1024)
        decodificar(data)