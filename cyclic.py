import sys
a = 0

file_path = "/home/stage/Documents/aa.txt"

while a <= 100:
    a += 1
    text = "riga nuova" + str(a) + "\n"

    if a <= 10:
       documento = open(file_path, "a")
       documento.write(text)
       documento.close()
    else:
        data = None

        with open(file_path, 'r') as fin:
            data = fin.readlines()

        with open(file_path, 'w') as fout:
            fout.writelines(data[1:])

        documento = open(file_path, "r")
        documento.write(text)
        documento.close()



