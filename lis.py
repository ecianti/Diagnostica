import usb
busses = usb.busses()
for bus in busses:
    devices = bus.devices

    for dev in devices:
        dev += 1

        if dev < 3:
            print "porta attiva", dev.filename

        else
            print "cia0"

        ""''''
        documento = open("/media/stage/F8D0-7695/pippo/nuovodoc.txt", "w")
        documento.write("testo scritto")
        documento.close()

        doc = open("/media/stage/F8D0-7695/pippo/nuovodoc.txt", "r")
        text = doc.read()
        print(text)
        doc.close()
        ""
        #print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
        #print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)""'''