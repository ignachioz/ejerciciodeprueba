palabra=input("Ingrese una palabra por teclado: ").upper()

diccionario_puntaje={1:["A","E","I","O","U","L","N","R","S","T"],2:["D","G"],3:["B","C","M","P"],4:["F","H","V","W","Y"],5:["K"],8:["J","X"],10:["Q","Z"]}
puntaje=0

puntajes=[1,2,3,4,5,8,10]

valores_puntajes=[["A","E","I","O","U","L","N","R","S","T"],["D","G"],["B","C","M","P"],["F","H","V","W","Y"],["K"],["J","X"],["Q","Z"]]
puntaje=0
for letra in palabra:
    i=0
    while(not letra in valores_puntajes[i]):
        i+=1
    puntaje=puntaje + puntajes[i]
print(puntaje)