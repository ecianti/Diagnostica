import datetime
import shutil

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

def mount(device, name=None):

    if not name:
        name = get_device_name(device)
    mount_partition(get_partition(device), name)





devices = list_media_devices()
if devices:
    device = devices[0]
    path = get_media_path(device)
    mount(device)

    if is_mounted(device):
        print device, "\nsalva sulla chiavetta"
        datetime.datetime.now()
        print datetime.datetime.now()
        shutil.copy2('/home/stage/cartellafatta/localfile.txt', path)  # copia il file da dispositivo a usb
        if path + 'localfile.txt':

            os.remove('/home/stage/cartellafatta/localfile.txt')
            os.rmdir('/home/stage/cartellafatta/')

        with open(path + "/file-usb.txt", "w") as f:  # e' il file principale
            f.write("Hello World")
            f.close()

        unmount(device)



else:

    print("salva in locale")
    datetime.datetime.now()
    print datetime.datetime.now()
    path = "/home/stage/cartellafatta/"
    os.system("mkdir -p " + path)
    with open(path + "localfile.txt", "w") as f:  # file temporaneo
        f.write("Hello World")

