
nome=input('digite seu nome')
peso=float(input('digite seu peso em quilogramas (kg)'))
print(peso)
altura=float(input('digite sua altura em metros (m)'))
print(altura)
imc=peso/ (altura * altura)
print()
if imc  >18.5:
   print('abaixo do peso, anemico')
elif imc <18.5 and imc >24.9:
   print('peso normal, saradão brow')
elif imc <25.0 and imc >29.9:
      print('sobrepeso amigão, academia existe em')
elif imc <30.0 and imc >34.9:
       print('Obesidade grau 1...ta com uma obesidade pesada(se é que me entende)')
elif imc >35.0 and imc <39.9:
          print('Obesidade grau 2. geladeira ta pedindo socorro')
else:
  print('Obesidade grau 3. Quilos mortais(prrgrama de TV legal)...')

print(f' {nome} | {imc} | {peso}')
    

          

