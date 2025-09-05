pessoa=input('olha tudo bem? Seja bem-vindo ao meu programa')
print('sim/nao')
nome= input('digite o nome:')
email= input('digite o email:')
with open ('pessoa.txt', 'a') as arquivo:
  arquivo.write (nome + "|" + email + "\n")