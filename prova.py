import usb
busses = usb.busses()
for bus in busses:
    devices = bus.devices

    for dev in devices:


        print "porta attiva", dev.filename

        documento = open("/media/stage/F8D0-7695/pippo/nuovodoc.txt", "w")
        documento.write("testo scritto")
        documento.close()

        doc = open("/media/stage/F8D0-7695/pippo/nuovodoc.txt", "r")
        text = doc.readline()
        doc.close()
        print(text)


        #print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
        #print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)""'''