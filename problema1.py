
T = input("")
if int(T) < 11:
    for i in range(int(T)):
        contenedor = []
        N = input("")
        S = input("")
        r = 0
        g = 0
        b = 0
        if int(N) < 100001 and int(N) == len(S):
            for x in str(S):
                if x == "R":
                    r += 1
                elif x == "G":
                    g += 1
                else:
                    b += 1
            contenedor.append(str(r))
            contenedor.append(str(g))
            contenedor.append(str(b))
            contenedor = int(sorted(contenedor)[0]) + int(sorted(contenedor)[1])
            print(contenedor)
        else:
            print("El núero de puertas no puede exceder a 10^5 y el número de puertas debe coincidir con la longitud de la cadena")
else: 
    print("El número de casos de prueba no puede ser mayor a 10")   
    