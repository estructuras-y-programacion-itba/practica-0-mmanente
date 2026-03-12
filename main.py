# Tu implementacion va aqui

def main():
    jugador = 1
    planilla = crear_planilla()
    generala_servida = False
    while planilla_completa(planilla) == False and generala_servida == False:
        print("Turno jugador:", jugador)
        listado_final , ronda = rondas()
        print(listado_final)
        print(["Escalera","Full","Poker", "Generala", 1,2,3,4,5,6]) 
        jugada = (que_es(listado_final) + numeros(listado_final))
        if ronda == 1:
            cont = 0
            for i in range(len(jugada)):
                if 50>jugada[i] > 0 and cont<4:
                    jugada[i] +=5
                elif jugada[i] == 50:
                    jugada[i] +=30
                cont+=1
        print(jugada)
        if ronda == 1 and jugada[3] >= 50:
            print("GENERALA SERVIDA")
            generala_servida = True
        else:
            categoria = elegir_categoria()  
            while categoria_disponible(planilla, jugador, categoria) == False:
                print("Categoria ya usada")
                categoria = elegir_categoria()
            categorias = ["E","F","P","G","1","2","3","4","5","6"]
            i = 0
            pos = -1
            while i < len(categorias):
                if categorias[i] == categoria:
                    pos = i
                i += 1
            puntos = jugada[pos]
            actualizar_planilla(planilla,jugador,categoria,puntos)
            guardar_csv(planilla)
            if jugador == 1:
                jugador = 2
            else:
                jugador = 1
    p1, p2 = sumar_puntos(planilla)
    print("Puntos jugador 1:", p1)
    print("Puntos jugador 2:", p2)

    if p1 > p2:
        print("Gana jugador 1")
    elif p2 > p1:
        print("Gana jugador 2")
    else:
        print("Empate")
def tirar(x):
    import random 
    lista = []
    for i in range(x):
        lista.append((random.randint(1,6)))
    return lista
def elegir (lista):
    elegidas = input("Posiciones elegidas")
    mantenidas = []
    for elem in elegidas:
        i = 0
        while i < len(lista):
            if elem.isdigit():
                if int(elem )==  i+1:
                    mantiene = lista[i] 
                    mantenidas.append(mantiene)
            i+=1
    return mantenidas
def rondas():
    lista = tirar(5) 
    print(lista)
    terminar = input("Desea terminar s es si")
    if terminar == 's':
        return lista , 1
    else:
        mantenidas = (elegir(lista))
        print(mantenidas)
        segunda = (tirar(5-(len(mantenidas))))
        print (segunda)
        nueva = mantenidas + segunda
        print(nueva)
        terminar = input("Desea terminar s es si")
        if terminar == 's':
            return nueva , 2
        else:
            mantenidas = (elegir(nueva))
            print(mantenidas)
            tercera = (tirar(5-(len(mantenidas))))
            print (tercera)
            final = mantenidas + tercera
            print(final) 
            return final  , 3
def que_es(lista):
    d = sorted(lista)
    resultados = []
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista) or (2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista):
        resultados.append(20)
    else:
        resultados.append(0)
    trio_inicial = (d[0]==d[1]==d[2]) and (d[3]==d[4])
    trio_final = (d[2]==d[3]==d[4]) and (d[0]==d[1])
    son_distintos = d[0]!=d[4]
    if (trio_inicial or trio_final) and son_distintos:
        resultados.append(30)
    else:
        resultados.append(0)
    poker_inicial = (d[0]==d[1]==d[2]==d[3])
    poker_final = (d[1]==d[2]==d[3]==d[4])
    if poker_inicial or poker_final:
        resultados.append(40)
    else:
        resultados.append(0)
    generala = (d[0]==d[1]==d[2]==d[3]==d[4])
    if generala:
        resultados.append(50)
    else:
        resultados.append(0)
    return resultados
def numeros(lista):
    puntajes = [0]*6 
    for elem in lista:
        if 1 <= elem <= 6: 
            puntajes[elem-1] += elem  
    return puntajes

def crear_planilla():
    planilla = [
    ["E",None,None],
    ["F",None,None],
    ["P",None,None],
    ["G",None,None],
    ["1",None,None],
    ["2",None,None],
    ["3",None,None],
    ["4",None,None],
    ["5",None,None],
    ["6",None,None]
    ]
    return planilla
def guardar_csv(planilla):
    with open("jugadas.csv","w") as f:
        f.write("jugada,j1,j2\n")
        i = 0
        while i < len(planilla):
            fila = planilla[i]
            j1 = fila[1]
            j2 = fila[2]
            if j1 == None:
                j1 = ""
            if j2 == None:
                j2 = ""
            linea = str(fila[0]) + "," + str(j1) + "," + str(j2) + "\n"
            f.write(linea)
            i += 1

def elegir_categoria():
    print("Categorias: E F P G 1 2 3 4 5 6")
    cat = input("Elegir categoria: ")
    return cat
def actualizar_planilla(planilla,jugador,categoria,puntos):
    i = 0
    while i < len(planilla):
        if planilla[i][0] == categoria:
            if jugador == 1:
                planilla[i][1] = puntos
            else:
                planilla[i][2] = puntos
        i += 1
def categoria_disponible(planilla, jugador, categoria):
    i = 0
    while i < len(planilla):
        if planilla[i][0] == categoria:
            if jugador == 1 and planilla[i][1] == None:
                return True
            if jugador == 2 and planilla[i][2] == None:
                return True
            return False
        i += 1
def planilla_completa(planilla):
    i = 0
    while i < len(planilla):
        if planilla[i][1] == None or planilla[i][2] == None:
            return False
        i += 1
    return True
def sumar_puntos(planilla):
    p1 = 0
    p2 = 0
    i = 0
    while i < len(planilla):
        if planilla[i][1] != None:
            p1 += planilla[i][1]
        if planilla[i][2] != None:
            p2 += planilla[i][2]
        i += 1
    return p1, p2  
    
# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

