lista=[10,20,30]
try:
 print(lista[40])

except:
 lista.append(40)
 print('erro')