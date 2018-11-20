T = input("")
try:
    if int(T) < 11:
        for i in range(int(T)):
            S = input("")
            contenedor1 = []
            contenedor2 = []
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
                    for j in range(len(contenedor3)):
                        for k in range(j, len(contenedor3) - 1):  
                            temp = len(contenedor3)
                            if k == int(temp - 2):
                                print("Not")                                   
                                break                                                
                            else:
                                if int(contenedor3[k + 1] + contenedor3[j]) in contenedor3:
                                    print("Dynamic")
                                    break 
                            
                        break
                else:
                    print("La longitu de la candena no puede se mayor a 10^5")
    else:
        print("El número de casos de prueba no puede ser mayor a 10")    
except ValueError:
    print("Entrada Inválida")    

    
                
            
    