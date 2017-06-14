import datetime
import shutil
from mount import *

a = 0
path = "/home/stage/"

while True:

    a += 1
    text = str(datetime.datetime.now()) + "  " + str(a) + "\n"
    documento = open(path + "localfile.txt" ,"a")


    if a<100:
        documento.write(text)

    else:



        documento.close()


        def get_partition(device):
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

        if not devices:
            a=0
            documento = open(path + "localfile.txt", "r+")

            if a < 100:
                documento.write(text)



