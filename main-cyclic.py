import datetime
import shutil
a = 0
from mount import *


def get_partition(device):
    """ Restituisce tutte le partizioni per il dispositivo """
    partitionsFile = open("/proc/partitions")
    lines = partitionsFile.readlines()[2:]
    partitionsFile.close()
    partitions = ["/dev/" + line.split()[-1] for line in lines]
    return_partitions = []
    for p in partitions:
        if device in p and p != device:
            return_partitions.append(p)
    return return_partitions[0]


file_path = "/media/sdb"  # definisce il path della chiavetta


def mount(device, name=None):  # definisce la funzione mount
    if not name:
        name = get_device_name(device)
    mount_partition(get_partition(device), name)


devices = list_media_devices()
if devices:  # controlla se e' presente la chiavetta
    device = devices[0]
    path = get_media_path(device)
    mount(device)

    if is_mounted(device):  # controlla se e' montata la chiavetta
        print device, "\nsalva sulla chiavetta"
        datetime.datetime.now()
        print datetime.datetime.now()
        shutil.copy2('/home/stage/cartellafatta/localfile.txt', path)  # copia il file da dispositivo a usb
        if path + 'localfile.txt':

            os.remove('/home/stage/cartellafatta/localfile.txt')  # cancella il file da locale
            os.rmdir('/home/stage/cartellafatta/')  # cancella la cartella che conteneva il file in locale

            a = 0  # ciclo di cyclic che scrive in usb un file
            while a <= 100:
                a += 1
                text = "riga nuova" + str(a) + "\n"

                if a <= 10:
                    documento = open(file_path + "/file-usb.txt", "a")
                    documento.write(text)
                    documento.close()
                else:
                    data = None

                    with open(file_path + "/file-usb.txt", 'r') as fin:
                        data = fin.readlines()

                    with open(file_path + "/file-usb.txt", 'w') as fout:
                        fout.writelines(data[1:])

                    documento = open(file_path + "/file-usb.txt", "a")
                    documento.write(text)
                    documento.close()

        unmount(device)



else:  # se non e' presente la chiavetta crea una cartella con file in locale

    print("salva in locale")
    datetime.datetime.now()
    print datetime.datetime.now()
    path = "/home/stage/cartellafatta/"
    os.system("mkdir -p " + path)

    a = 0  # ciclo che scrive nel file in locale

    while a <= 100:
        a += 1
        text = "riga nuova" + str(a) + "\n"

        if a <= 10:
            documento = open(path + "localfile.txt", "a")
            documento.write(text)
            documento.close()
        else:
            data = None

            with open(path + "localfile.txt", 'r') as fin:
                data = fin.readlines()

            with open(path + "localfile.txt", 'w') as fout:
                fout.writelines(data[1:])

            documento = open(path + "localfile.txt", "a")
            documento.write(text)
            documento.close()
