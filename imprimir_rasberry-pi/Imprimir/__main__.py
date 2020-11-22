
import os
import sys
import fileinput
import time


# ONEDRIVE

def OpenFile(filename, Mode):
    f = open(filename, mode=Mode)
    return f

def Read_Values(f):
    read_n_files = f.read()
    n_files = int(read_n_files)
    replacement = n_files
    replacement = str(replacement)
    f.close()

    return read_n_files, replacement, n_files

def Replace_Numer(read_n_files, final_n_files, replacement, ):
    os.system('cls')
    final_replaced_n_files = read_n_files.replace(replacement, final_n_files)
    return final_replaced_n_files

def Write(final_replaced_n_files, filename):
    f = open(filename, "w")
    write = f.write(final_replaced_n_files)
    return write

def Compare(read_n_files, filecount):
    state = ''
    read_n_files = int(read_n_files)
    
    if read_n_files == filecount:
        state = 'Todo Correcto!'
    elif read_n_files > filecount:
        state = 'Es mas grande'
    elif read_n_files < filecount:
        state = 'Es mas pequeño'

    return str(state)

def Filecount(path):
    os.chdir(path)
    filecount = os.listdir()
    filecount = len(filecount)

    return filecount

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def Pull_Usb(path):
    pass

def FinalWork():
    filecount = Filecount(r'C:\Users\GGFERCAS13\Documents\GitHub\Impresion_Rasberry-Pi\imprimir_rasberry-pi\PARA-IMPRIMIR')
    reader_mode = OpenFile("n_files.txt", "r+")
    values = Read_Values(reader_mode)
    read_n_files = values[0]
    replacement = str(values[1])
    n_files = int(values[2])
    check = Compare(read_n_files, filecount)
 
    if check == 'Es mas pequeño':
        os.system('cls')
        n_files = n_files + 1
        final_n_files = str(n_files)
        formula_replacing = Replace_Numer(read_n_files, final_n_files, replacement)
        Write(formula_replacing, 'n_files.txt')
        check = Compare(read_n_files, filecount)
        latest_file = newest(r'C:\Users\GGFERCAS13\Documents\GitHub\Impresion_Rasberry-Pi\imprimir_rasberry-pi\PARA-IMPRIMIR')
        time.sleep(2)

    elif check == 'Es mas grande':
        os.system('cls')
        n_files = n_files - 1
        final_n_files = str(n_files)
        formula_replacing = Replace_Numer(read_n_files, final_n_files, replacement)
        Write(formula_replacing, 'n_files.txt')

    elif check == 'Todo Correcto!':
        os.system('cls')
        print()
        print("Todo Correcto!") 
        time.sleep(2)


while True:
    FinalWork()


