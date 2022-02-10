"""
                          𝒹ℯ𝓈𝒶𝓇ℴ𝓁𝓁𝒶𝒹ℴ 𝓅ℴ𝓇


███╗░░░███╗░█████╗░██╗░░██╗██╗░░██╗████████╗████████╗██╗░░██╗░█████╗░███╗░░░███╗
████╗░████║██╔══██╗╚██╗██╔╝╚██╗██╔╝╚══██╔══╝╚══██╔══╝██║░░██║██╔══██╗████╗░████║
██╔████╔██║███████║░╚███╔╝░░╚███╔╝░░░░██║░░░░░░██║░░░███████║██║░░██║██╔████╔██║
██║╚██╔╝██║██╔══██║░██╔██╗░░██╔██╗░░░░██║░░░░░░██║░░░██╔══██║██║░░██║██║╚██╔╝██║
██║░╚═╝░██║██║░░██║██╔╝╚██╗██╔╝╚██╗░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝

+++++++++10 de febrero de 2022++++++++++++

ESTE PRPGRAMA ES DESAROLLADO POR MAXXTTHOM
CON FINES DE PROTEGER OBRAS DE PORGRAMACION

ESTE PRPGRAMA GARATIZA ULTIZACION EN UN SOLO PC
PARA NO PODER SER REVENDIDO POR PERSONAS INESCRUPOLOSAS TRABAJO QUE NO REALIZARON ELLOS


no se debe utilizar tal como esta tienes que ingenciarte donde esconger codigo que genera este programa

path_us = este es nombre de la ruta donde se guardara el codigo generado
'ojo' solo se genera 1 soles ves el codigo. una vez se genero todas las vecs que se usa el porgrama ara consulta a ese dorectorio y emviara el codigo al servidor
en el servidor ala consulta si ese codigo esta en la lista y si encuentra responder con la clave designado en el sevidor

antes de ejecutar este porgram debes ejecutar primero el server.py

ATTE: Telegram @Maxxthon https://t.me/Maxxthon
"""


import base64
from pathlib import Path
import platform
import socket
from random import randint
from colorama import Fore
import requests, time, json, os
from fake_headers import Headers

if __name__ == "__main__":
    header = Headers(
        browser="chrome",
        os="win",
        headers=True
        )
    for i in range(1):
        header.generate()

#  ROJO red           AMARILLO yellow         CELESTE  cyan           BLANCO reset          VERDE green
red = Fore.RED;   yellow = Fore.YELLOW;     cyan = Fore.CYAN;     reset = Fore.RESET;     green = Fore.GREEN

result = requests.get('http://worldtimeapi.org/api/timezone/America/Lima', headers=header.generate()).text
responseData = json.loads(result); general_fecha = responseData['utc_datetime'].replace('T', ' ').replace('.', ' ').replace(':', '-').replace('+', '-').split()
fecha = general_fecha[0]; hora = general_fecha[1]
tiempo = '{}  {}'.format(fecha, hora)
os.system('cls')




cliente = 'maxx'.upper()#--------->>NOMBRE DE CLIENTE
idbot = 'ORBIDATA movistar'.upper()#--------->>NOMBRE DE BOT/PROGRAMA

host = '192.168.56.1'; port = 5025# AQUI PUERTO ESCUCHA DE SERVIDOR

######################################################
######################################################
######################################################
######################################################
cliente = cliente.replace(' ', '=')
idbot = idbot.replace(' ', '=')






def gen():
    ran = randint(1000, 9999); num =str(ran).rstrip(); return num

path_us = 'D:\\g\\g\\g\\g\\g\\code'
def busqueda_ubicacion():
    d = Path('D:/')#
    try:
        path = Path(d / '\\g\\g\\g\\g\\g\\documentos'); path_data = Path(d / '\\g\\g\\g\\g\\g\\cualquercosa'); path_cache = Path(d / '\\g\\g\\g\\g\\g\\documentos\\origin')# aqui creas 3 diretorios en un lugar donde sea dificil de conseguir
        path.mkdir(parents=True); path_data.mkdir(parents=True); path_cache.mkdir(parents=True); print('Datos Registrado')#si ejecutas por primera ves el programa ciente crea automatico los directorios y en pantalla muestra un mensje 'Datos Registrado'
    except: pass
    path_existe = os.path.exists(path_us)# Comprueba si esite el caprta y el directorio que tiene codigo de licencia
    if path_existe == False:# si no existe crea  nuevo codigo
        f = open(path_us, 'w'); f.write('CODE-{}-{}-{}-{}'.format(gen(), gen(), gen(), gen())); f.close()
    else: pass
    
def leer():
    #busqueda_ubicacion()
    with open(path_us, 'r') as file:
        lines = file.read().replace('-', ' '); x = str(lines.rstrip()); g = x.split()
        try:
            kt = g[2]
        except:#reiscribir code
            print(Fore.YELLOW+'la licencia se desactivo vuelve a solicitar nueva lincia al administrador')
            file = open(path_us, 'w'); file.write('CODE-{}-{}-{}-{}'.format(gen(), gen(), gen(), gen())); file.close()
            with open(path_us, 'r') as file:
                lines = file.read().replace('-', ' '); x = str(lines.rstrip()); g = x.split(); kt = g[2]; time.sleep(5)
        return kt
if __name__ == '__main__':
    busqueda_ubicacion()
    leer()

#DATA
pc = platform.node().rstrip(); machine_id = pc.replace('-', '=').split(); hostname = socket.gethostname()
data = (machine_id[0]+'-'+leer()+'-'+idbot+'-'+cliente).upper()

#HOST SERVER
try:
    sock = socket.socket(); sock.connect((host, port)); time.sleep(0.15); auto_server = 'live'
except: auto_server = 'die'



if auto_server == 'die':# SERVER LOOCAL
    print(Fore.RESET +'Servidor automatico fuerra de servicio')
    try:
        f = open('server.txt', 'r'); xnet = f.read(); f.close()
        xxnet = xnet.split(); host = xxnet[0]; port = int(xxnet[1])
        sock = socket.socket(); sock.connect((host, port)); time.sleep(0.15)
        print(); print('conexion local exitoso')
    except Exception:
        s = """
                                                                            
                  ▒▒▓▓      ▒▒▒▒▒▒▒▒            ▒▒                          
              ░░▒▒▒▒██    ▒▒    ░░▒▒▒▒        ▒▒▒▒                          
            ▒▒▓▓  ▒▒██    ▒▒  ▒▒▒▒  ▒▒    ░░▒▒  ▒▒                          
          ▒▒▒▒    ▒▒▓▓    ▒▒  ▒▒▒▒  ▒▒  ▓▓▓▓    ▒▒                          
          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒                      
                  ▒▒▒▒    ▒▒▒▒▒▒    ▒▒          ▒▒                          
                  ▒▒▓▓      ▒▒▒▒▒▒▒▒            ▒▒                          
                                                                                                
                                                                                                
      """
        print(Fore.GREEN +'', s)  
        print('Servidor no disponible intente mas tarde y si el ERROR persiste'); print('comunicate con el admin por')
        print('Telegram  @Maxxthon  o https://t.me/Maxxthon'); input('ENTER: ')

elif auto_server == 'live':
    pass
# tiempo y dato
sock.send(tiempo.encode('utf-8')); time.sleep(0.15); sock.send(data.encode('utf-8'))
server = sock.recv(1024).decode('utf-8')

# Mensaje de servidor
if server == 'AUI TU PALABRA CLAVE':
    premium = True
    correr = """
                        .aoon.             d
                "^vaondAHHHHHP"      dHb  dT
                    "~^SHHHHH       n.YP,dP
                    .adHHHHHHh,     HHAUHP
             dAHbmnnao."^VHHHP.Abn.dHHHP"
            ]MHHHHHHHHHAh."VP.AHUHHHHP"
            AHHP"  "~VHHHHb.aHP"  "~"
           ]HHHL     `ACTIVATE
           AHHHh      UHHHHHH'
          ]HP"dHD     "^YP^~".adAHHHHb
          P"   ~     dHhnoadAHHHHUYHHH
                     UHHHHHHHUP" dAHHP
                    ."^VHUP^"  .dHHHB"
                    HAbnnr   .dAHHHH'
       .nadAHHAban.dHHHHP   Telegram: -@Maxxtthon >>
    .adUHHHHHHHHHUHHHHP"   dHHHHHHP
           "^HUHHHHUP"    dHP^" HHAbnao
           dAHU^VP^"    .dP"    VHP^~"
           HH}          ~
           HP
           "
      ----BIENVENIDOS A USER PREMIUM----
    """; print(Fore.CYAN+correr); time.sleep(0.55)

elif server != 'AUI TU PALABRA CLAVE':
    premium = False
    stop = """
      ____________________
     /       ERROR        |
     |SIN lICENCIA DE USO |
     \____________________/
              !  !
              !  !
              L_ !
             / _)!
            / /__L
      _____/ (____)
             (____)
      _____  (____)
           \_(____)
              !  !
              !  !
              \__/

    """; print(Fore.GREEN + stop)


if premium == True:
    # DENTRO DE ESTE PONER TODO EL CODIGO DE ESCRIP OJO SE RECOMIENDO OFUSCACION DE CODIGO PARA MAYOR SEGURIDAD DEL CODIGO POR EVITAR POSIBLES DESINCRIPTADORES
   activado = """

    ██╗░░░██╗░██████╗██╗░░░██╗░█████╗░██████╗░██╗░█████╗░  ██████╗░██████╗░███████╗███╗░░░███╗██╗██╗░░░██╗███╗░░░███╗
    ██║░░░██║██╔════╝██║░░░██║██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗██╔════╝████╗░████║██║██║░░░██║████╗░████║
    ██║░░░██║╚█████╗░██║░░░██║███████║██████╔╝██║██║░░██║  ██████╔╝██████╔╝█████╗░░██╔████╔██║██║██║░░░██║██╔████╔██║
    ██║░░░██║░╚═══██╗██║░░░██║██╔══██║██╔══██╗██║██║░░██║  ██╔═══╝░██╔══██╗██╔══╝░░██║╚██╔╝██║██║██║░░░██║██║╚██╔╝██║
    ╚██████╔╝██████╔╝╚██████╔╝██║░░██║██║░░██║██║╚█████╔╝  ██║░░░░░██║░░██║███████╗██║░╚═╝░██║██║╚██████╔╝██║░╚═╝░██║
    ░╚═════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝
        """


    print(f'{cyan}{activado}')



elif premium == False:
    print(Fore.RED +' ---------------------------------------------')
    print(Fore.RED +'{}'.format(server))
    print(Fore.GREEN + '******************************************************')
    print(Fore.CYAN + '       P O W E R    B Y :   M A X X T T H O M')
    print(Fore.GREEN + '******************************************************')
    input()