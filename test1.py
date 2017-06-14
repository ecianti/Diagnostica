import shutil
from mount import *


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



a = 0
while a < 150:
    a += 1
    file_local_path = "/home/stage/Prova.txt"
    #x = open(file_local_path, "w")
    devices = list_media_devices()

    if not devices:
        with open(file_local_path, "w+") as x:
            for j in range(100):
                x.write("Ciao" + str(j) + "\n")
            x.close()
    else:

        device = devices[0]
        path_chiavetta = get_media_path(device)
        mount(device)

        if is_mounted(device):
            shutil.copy2(file_local_path, path_chiavetta)

        os.remove(file_local_path)

