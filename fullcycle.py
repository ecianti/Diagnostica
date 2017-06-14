
import shutil
from mount import *



def get_partition(device):   #restituisce  una partizione della chiavetta
    partitionsFile = open("/proc/partitions")
    lines = partitionsFile.readlines()[2:]
    partitionsFile.close()
    partitions = ["/dev/" + line.split()[-1] for line in lines]
    return_partitions = []
    for p in partitions:
        if device in p and p != device:
            return_partitions.append(p)
    return return_partitions[0]

def mount( device , name=None ):    #definisce la funzione di mount
    if not name:
        name = get_device_name(device)
    mount_partition(get_partition(device), name)


flag = True

devices = list_media_devices()

while True:

    file_local_path = "/home/stage/Prova.txt"


    if flag:
        x = open(file_local_path, "w")          #apre e scrive un file in locale
        for j in range(100):
            x.write("Ciao " + str(j) + "\n")
        x.close()
        flag = False

    else:

        if devices:  # controlla se c'e' la chiavetta
            device = devices[0]
            path_chiavetta = get_media_path(device)
            mount(device)  #monta la chiavetta

            if is_mounted(device): #controlla se e' montata la usb
                shutil.copy2(file_local_path, path_chiavetta)      #copia il file da locale a chiavetta



            os.remove(file_local_path) #dove va messo, cancellerebbe il file da locale

            flag = True

        else:  # se non c'e' la chiavetta continua a scrivere ciclicamente sul file locale
            x = open("file_local_path", "r+")
            for j in range(100):
                x.write("Ciao" + str(j))
            flag = False
            x.close()
