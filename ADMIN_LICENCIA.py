#ADMIN LICENCE V.3
import platform
import socket
import time, os, sys
from colorama import Fore, Back, Style
from _thread import *
#  ROJO red           AMARILLO yellow         CELESTE  cyan           BLANCO reset          VERDE green
red = Fore.RED;   yellow = Fore.YELLOW;     cyan = Fore.CYAN;     reset = Fore.RESET;     green = Fore.GREEN; magenta = Fore.MAGENTA
os.system('cls'); print(Fore.GREEN +'')



"""
                          𝒹ℯ𝓈𝒶𝓇ℴ𝓁𝓁𝒶𝒹ℴ 𝓅ℴ𝓇


███╗░░░███╗░█████╗░██╗░░██╗██╗░░██╗████████╗████████╗██╗░░██╗░█████╗░███╗░░░███╗
████╗░████║██╔══██╗╚██╗██╔╝╚██╗██╔╝╚══██╔══╝╚══██╔══╝██║░░██║██╔══██╗████╗░████║
██╔████╔██║███████║░╚███╔╝░░╚███╔╝░░░░██║░░░░░░██║░░░███████║██║░░██║██╔████╔██║
██║╚██╔╝██║██╔══██║░██╔██╗░░██╔██╗░░░░██║░░░░░░██║░░░██╔══██║██║░░██║██║╚██╔╝██║
██║░╚═╝░██║██║░░██║██╔╝╚██╗██╔╝╚██╗░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝
Telegram @Maxxthon https://t.me/Maxxthon

"""

def data_Premium():
    data_client = []
    with open('.\\Data Premium\\Licencias.txt', 'r') as f:
        for lines in f:
            data_P = lines.split(); data_client.append(data_P[0])
    return data_client




#Server Start
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 5025; ThreadCount = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port)); sock.listen(9)



print (Fore.GREEN +"Conexion")
print(Fore.RESET +'Puerto {}{}{} en escucha y host: {}{}'.format(Fore.YELLOW, port, Fore.RESET, Fore.YELLOW,host)); print(Fore.RESET)


def multi_threaded_client(connection):
    for i in range(1):
        count = 1
        try:
            user = conn.recv(1024).decode('utf-8').split(); Serial_keys = user[0]# recibe codigo de cliente
            dot = user[0].replace('-', ' ').split(); verify = Serial_keys.split(); rango = verify[0].replace('-', ' ').split()

            if Serial_keys in data_Premium():#3-------------------------------COMPRUEBA SI EXITE EN LA LISTA DE CLAVES EL KEY QUE ACABA DE RECIBIR
                print(f'{green}Cliente: {yellow}{Serial_keys}     {reset}<------------------|{magenta}key')
                print(f'{green}PC: {yellow}{dot[0]} {green}CODE: {yellow}{dot[1]} {green}BOT: {yellow}{dot[2]} {green}Client: {yellow}{dot[3]}')
                conn.send('AQUI TU PALABRA CLAVE'.encode('utf-8'))#---------------------------------------------------------------------------------------------> CUANDO EXISTE EN LA LISTA DE KEYS MANDA UN MENSJE QUE ASEPTA EL CLIENTE  > elige la palabra clave < que aseptara tu programa
                print(Fore.CYAN +'          PREMIUM'); print()
                operdador = user.replace('-', ' ').split()


            else:
                print(f'{green}Cliente: {yellow}{Serial_keys}     {reset}<------------------|{magenta}key')
                messag = """
Mensaje que sale cuando el cliente no tiene licencia
contactame via telegram el los siguentes enlaces
    ------------ATE: admin -------------------

  @Maxxtthon     o        https://t.me/Maxxtthon
  ---------------------------------------------
                                """
                conn.send(messag.encode('utf-8'))#----------------------------------------------------------------------------------------------> cuando no tiene licnecia manda un mensaje indicando que no tiene lincencia
                print(f'{green}PC:{yellow}{dot[0]} {green}CODE {yellow}{dot[1]} {green}BOT {yellow}{dot[2]} {green}Client {yellow}{dot[3]}')
                print(Fore.RED +'          Sin licencia')
                conn.close()
                connection.close()# CIERRA CONEXIONES




        except Exception:
            try:
                if count > 1:
                    conn.close()
                    print(count)
                else:
                    pass
            except:
                pass
        count += 1



while True:
    try:
        # INICIA EL CONEXION 
        conn, addr = sock.accept() # ASEPTA CONEXION
        hora = conn.recv(1024).decode('utf-8').split() # RECIBE PRIMER MENSAJE DE CLIENTE Y ESTE DEBE SER UN FECHA Y HORA
        print(f'{green}CONEXION: {red}[{reset}{ThreadCount}{red}]{reset} {green}IP: {reset}{addr[0]} {green}Fecha:{reset} {hora[0]} {green}Hora:{reset} {hora[1]}')# imprime  ip fecha y hora de conexion
        start_new_thread(multi_threaded_client, (conn, ))
        ThreadCount += 1
    except Exception:
        pass
conn.close()