#riconoscimento tipo di oggetto (usb)

import os
from mount import *

devices = list_media_devices()
device = None

partitionsFile = open("/proc/partitions")
lines = partitionsFile.readlines()[2:]  # Skips the header lines

#for check_device in devices:

   # device = check_device
   # break

for line in lines:
    words = [x.strip() for x in line.split()]
    minorNumber = int(words[1])
    deviceName = words[3]
    if minorNumber % 16 == 0:
        path = "/sys/class/block/" + deviceName
        if os.path.islink(path) and os.path.realpath(path).find("/usb") > 0:

            print "/dev/%s" % deviceName #stampa nome usb connessa



if device:
    path = get_media_path(device)

    mount(device)