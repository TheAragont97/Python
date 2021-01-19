import random
temps=[[27.4, 26.6, 26.2, 25.7, 24.9, 23.8, 24.0, 25.7, 27.6, 29.0, 30.4, 31.6, 32.3, 29.0, 29.6, 29.9, 30.0, 29.8, 29.4, 28.4 ,27.2, 25.6, 24.5, 23.8],
[22.6, 21.7, 20.4, 19.2, 18.4, 17.9, 17.9, 17.1, 17.2, 19.2, 21.6, 23.4, 24.9, 25.3, 26.0, 26.4, 26.7, 26.7, 26.5, 26.0, 23.9, 21.8, 20.2, 19.0],
[18.1, 17.5, 16.9, 16.2, 15.7, 15.4, 15.9, 17.1, 18.5, 20.0, 21.2, 22.3, 24.3, 24.6, 25.5, 26.4, 26.6, 26.8, 26.6, 26.2, 25.0, 22.3, 20.4, 19.2],
[17.9, 16.5, 15.2, 14.2, 13.4, 13.0, 13.6, 14.9, 16.3, 18.0, 20.2, 22.8, 24.6, 25.7, 26.6, 27.2, 27.4, 27.3, 27.0, 26.2, 24.4, 22.4, 21.0, 20.1],
[19.3, 18.6, 18.4, 18.4, 18.1, 17.7, 18.0, 19.1, 20.8, 22.4, 24.0, 25.4, 26.7, 28.8, 29.6, 30.1, 30.4, 30.2, 29.6, 28.6, 26.8, 25.4, 23.6, 22.0],
[20.7, 20.0, 20.2, 20.0, 19.6, 18.8, 18.7, 20.2, 22.7, 25.3, 27.5, 29.4, 30.7, 30.8, 31.9, 32.2, 31.9, 29.8, 29.2, 28.3, 27.3, 26.2, 24.9, 21.6],
[18.9, 19.1, 18.5, 18.7, 19.2, 19.3, 19.1, 19.8, 21.4, 23.2, 25.7, 25.3, 25.3, 25.4, 25.7, 25.5, 25.9, 25.5, 25.0, 24.7, 23.4, 21.8, 21.1, 19.6],
[18.1, 17.2, 15.9, 15.5, 16.0, 15.6, 15.1, 15.9, 17.5, 18.9, 19.1, 18.1, 18.7, 19.3, 20.6, 20.0, 20.5, 20.8, 20.7, 20.3, 19.4, 17.7, 16.4, 15.4],
[14.5, 13.9, 13.2, 12.4, 11.5, 10.9, 11.5, 12.9, 14.4, 16.5, 18.5, 19.7, 20.7, 22.2, 22.7, 22.5, 22.5, 22.1, 21.6, 20.6, 19.1, 18.2, 17.8, 17.2],
[14.9, 12.6, 12.4, 11.9, 10.5, 10.2, 10.7, 12.1, 14.2, 16.9, 18.8, 19.8, 20.6, 21.8, 22.7, 23.3, 23.5, 23.5, 23.1, 22.5, 21.3, 19.6, 18.3, 17.6],
[17.1, 16.6, 16.7, 16.0, 15.7, 15.1, 15.6, 17.1, 17.9, 19.3, 20.1, 20.9, 20.7, 19.2, 20.2, 21.2, 21.8, 22.2, 22.4, 22.0, 21.4, 21.1, 20.4, 18.9],
[17.9, 17.3, 16.6, 16.3, 16.1, 15.9, 16.5, 18.4, 19.7, 21.7, 23.6, 25.1, 24.5, 23.2, 22.5, 22.0, 22.4, 22.2, 21.6, 21.9, 20.9, 20.0, 19.5, 18.1],
[17.4, 17.1, 16.9, 16.8, 16.7, 16.5, 16.0, 16.0, 16.4, 17.3, 18.2, 19.2, 20.2, 21.1, 21.3, 21.5, 22.5, 22.6, 22.3, 21.5, 20.5, 19.2, 18.0, 17.0],
[16.2, 15.7, 15.3, 14.8, 14.6, 14.4, 14.7, 15.8, 16.4, 17.8, 18.2, 18.6, 18.7, 20.6, 20.9, 20.9, 20.6, 20.2, 19.8, 18.9, 18.8, 18.2, 17.4, 16.6],
[15.7, 14.9, 14.0, 13.1, 11.8, 11.6, 12.1, 12.9, 14.7, 17.2, 19.5, 20.0, 21.4, 22.2, 23.0, 22.8, 23.6, 23.6, 23.3, 23.0, 22.5, 21.8, 20.1, 18.6],
[17.4, 16.4, 15.4, 14.5, 13.8, 12.8, 13.3, 14.3, 15.9, 17.9, 20.1, 22.0, 23.3, 24.1, 24.9, 25.4, 25.7, 25.6, 25.2, 24.7, 23.6, 22.5, 21.2, 20.5],
[19.9, 18.6, 17.4, 17.0, 16.9, 16.4, 16.6, 18.0, 19.9, 21.9, 23.6, 24.9, 25.8, 25.9, 26.6, 27.1, 27.3, 27.3, 26.9, 26.1, 24.4, 22.8, 21.6, 20.2],
[18.9, 18.0, 17.6, 17.7, 18.2, 18.0, 18.1, 19.5, 21.8, 24.0, 26.0, 26.9, 27.2, 27.4, 27.6, 27.6, 27.5, 27.2, 26.9, 26.2, 25.0, 23.8, 22.7, 21.5],
[21.0, 19.9, 19.3, 19.5, 19.7, 18.5, 19.2, 20.6, 21.7, 23.0, 24.6, 26.0, 26.5, 26.1, 26.4, 26.6, 26.8, 26.8, 26.6, 26.1, 25.3, 24.6, 22.5, 21.1],
[20.2, 19.2, 18.6, 18.4, 18.3, 18.2, 18.7, 20.3, 22.9, 25.6, 28.0, 29.2, 30.7, 31.5, 32.0, 32.1, 32.1, 31.4, 29.9, 28.2, 27.4, 26.5, 25.3, 24.6],
[23.0, 22.3, 22.8, 22.4, 21.3, 20.7, 21.2, 22.8, 23.6, 24.8, 25.8, 26.8, 27.7, 25.1, 25.9, 26.5, 26.9, 27.0, 26.9, 26.5, 25.8, 24.9, 22.6, 21.3],
[20.3, 19.4, 18.7, 18.0, 17.7, 17.2, 17.5, 19.8, 22.2, 24.6, 26.4, 27.4, 28.1, 28.8, 29.5, 29.8, 29.9, 29.6, 29.1, 28.1, 26.2, 24.4, 23.2, 22.8],
[22.2, 21.5, 21.1, 20.6, 20.2, 19.5, 19.1, 20.6, 23.2, 25.7, 27.7, 29.3, 30.2, 31.8, 32.6, 33.0, 33.2, 33.0, 32.5, 31.6, 30.0, 28.1, 26.1, 24.9],
[24.1, 23.5, 23.3, 22.5, 21.1, 20.7, 20.6, 22.2, 24.9, 27.1, 29.1, 31.1, 32.4, 33.5, 34.5, 35.1, 35.3, 35.3, 35.0, 34.2, 33.0, 31.5, 29.3, 27.9],
[26.7, 25.4, 23.4, 22.3, 21.4, 20.7, 21.1, 23.3, 27.0, 29.2, 30.9, 32.7, 33.7, 34.1, 35.0, 35.4, 35.5, 35.2, 34.8, 34.1, 32.6, 30.9, 28.8, 27.8],
[27.2, 27.0, 26.9, 26.1, 26.1, 26.0, 25.8, 26.2, 27.4, 29.2, 30.3, 31.6, 32.1, 29.1, 30.9, 31.9, 32.1, 32.2, 32.1, 31.6, 30.7, 30.5, 29.4, 27.3],
[25.4, 24.0, 23.4, 22.5, 21.5, 21.6, 21.4, 21.8, 22.6, 22.0, 21.5, 21.3, 21.4, 21.3, 22.4, 22.6, 23.2, 22.9, 22.7, 22.4, 21.5, 20.1, 19.7, 19.5],
[19.1, 18.8, 18.3, 17.4, 17.1, 17.6, 17.7, 18.1, 17.9, 18.0, 18.8, 19.5, 19.8, 18.7, 17.9, 17.8, 19.3, 20.1, 20.9, 20.4, 20.1, 19.4, 18.0, 16.6],
[16.0, 15.5, 15.6, 15.9, 16.6, 16.4, 16.4, 17.0, 18.3, 20.0, 21.9, 23.3, 24.2, 24.2, 24.9, 25.4, 25.6, 25.5, 25.3, 24.7, 23.8, 22.8, 21.8, 21.0],
[20.6, 19.9, 19.1, 18.7, 18.6, 18.3, 17.7, 19.3, 21.7, 23.7, 25.4, 26.1, 26.5, 26.9, 27.2, 27.3, 27.4, 27.2, 26.4, 25.2, 22.9, 20.4, 19.9, 19.7],
[19.2, 18.7, 18.8, 18.5, 17.5, 17.3, 17.2, 17.1, 17.9, 18.4, 18.9, 20.4, 21.1, 22.1, 23.4, 23.7, 23.9, 23.8, 23.7, 23.4, 22.3, 21.3, 20.1, 19.0]]
#for x in range(31):
#    dia=[num for x in range(24)]
#    temps.append(dia)
#print(temps)
#otra manera es hacer dos bucles uno para temps y otro para los dias hasta 11
suma=0
promedio=0
max=0
for dia in temps:
    promedio+=dia[11]
print("Promedio: "+str((promedio/31)))
for dia in temps:
    for x in range(24):
        if(dia[x]>max):
            max=dia[x]
print("Dia de máxima temperatura: "+str(max))
for dia in temps:
    if(dia[11]>20):
        suma+=1
print("Dias mas calurosos: "+str(suma))
for dia in temps:
    print("Temperatura a las 8:00AM: "+str(dia[8]))

