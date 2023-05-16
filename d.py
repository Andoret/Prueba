import sys
filas=int(input ("filas de todas las matrices"))
columnas=int(input("columnas de todas las matrices"))
if filas<=0 :
    sys.exit("Bro, no existen las filas negativas, a la proxima digita un numero mayor a 0 pls ")
elif columnas<=0:
    sys.exit("Bro, no existen las columnas negativas, a la proxima digita un numero mayor a 0 pls ")
else:
    matriz=[]
    while filas!=columnas:
        print("Las filas y columnas no son iguales, por lo tanto no es una matriz cuadrada")
        filas=int(input ("filas de  la matriz"))
        columnas=int(input("columnas de  la matriz"))
    for i in range (filas):
        matriz.append([0]*columnas)
    for i in range (filas):
        for j in range(columnas):
            print("Digite el dato: ",(i,j))
            matriz[i][j]=int(input())
    print(matriz)
    
    
def first(filas,columnas,matriz):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j+1]=matriz[i][j]
        
