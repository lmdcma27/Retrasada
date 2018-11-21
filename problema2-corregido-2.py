T = input("")
try:
    if int(T) < 11:
        for i in range(int(T)):
            S = input("")
            contenedor1 = []
            contenedor2 = []
            contenedor3 = []
            if len(str(S)) < 3:
                print("Not")
            else:
                if len(S) < 100001:
                    for x in str(S):
                        if x in contenedor1:
                            contenedor2[int(contenedor1.index(x))] += 1
                        else:
                            contenedor1.append(x)
                            contenedor2.append(int(1))
                    contenedor3 = sorted(contenedor2)
                    if len(contenedor3) < 3:
                        print("Not")                   
                    else:
                        aux = False
                        for j in range(len(contenedor3)):
                            if j == len(contenedor3) - 2:
                                print("Not")
                            else:
                                for k in range(j+1, len(contenedor3)):
                                    temp = contenedor3[j] + contenedor3[k]
                                    if temp in contenedor3:
                                        aux = True
                                        print("Dynamic")
                                        break
                                if aux == True:
                                    break
                                elif j == len(contenedor3) - 2:
                                    print("Not")
                                    break
                                else:
                                    pass
                else:
                    print("La longitu de la candena no puede se mayor a 10^5")
    else:
        print("El número de casos de prueba no puede ser mayor a 10")    
except ValueError:
    print("Entrada Inválida")     

    
                
            
    