
import os
import sys
import fileinput





# Declaramos el nombre del archivo que vamos a abrir
filename = "n_files.txt"
# Abre en modo reading el archivo 
f = open(filename, "r+")


# Almacena el numero de archivos que hay en la carpeta
read_n_files = f.read()

# Convierte y renombra el numero de archivos a un integer
n_files = int(read_n_files)
# Almacena el numero de archivos que hay
replacement = n_files
# Convierte en un string el numero de archivos que hay 
replacement = str(replacement)


n_files = n_files + 1
final_n_files = str(n_files)
# Busca el numero que ponia antes de archivos y lo remplaza por el nuevo numero
final_replaced_n_files = read_n_files.replace(replacement, final_n_files)
        
# Vuelve a abrir el archivo en writing mode
writing_mode = open(filename, "w")
# Escribe el numero de actual de archivos
f.write(final_replaced_n_files)

# Abre la carpeta donde estan todos los archivos para imprimir e impresos
os.chdir(r'C:\\Users\GGFERCAS13\Desktop\TEST-IMPRESION\PARA-IMPRIMIR')
# Imprime la ruta para que podamos comprobar que esta bien
print(os.getcwd())

# Hace una lista con todos los archivos en la carpeta de impresion
filecount = os.listdir()
# Mide y convierte en un integer el numero de archivos que coge de la anterior lista
filecount = int(len(filecount))


print('read_n_files: ', read_n_files)
print('final_n_files: ', final_n_files)
print('replacement: ', replacement)
print('writing_mode: ', writing_mode)
        

    

#print(filecount)
