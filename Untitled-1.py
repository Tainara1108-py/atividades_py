
idade=int(input('digite sua idade'))
print('vc é um estudante?/nao/sim')
aluno=input("estudante ")
if aluno=='Sim':
    print()
    
elif  idade <12:
    print('seu ingresso custará R$8,00')
elif idade>65:
    print('vc é senhor dentadura e paga R$10,00')
elif idade>12 and aluno=='n':
    print('vc tera que pagar R$20,00')
elif idade>12 and aluno=='s':
    print('vc tera que pagar R$8,00')
elif idade <13 or 64:
    print('vc vai sacar do bolso só R$10,00')
























