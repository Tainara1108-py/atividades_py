
try:
 
 with open ('pessoa.txt', 'r') as arquivo:
      email = arquivo.read()
      print(email)
except:
   with open ('pessoa.txt', 'a') as arquivo:
     email = arquivo.write(email +'|'+ arquivo+'|'+ '\n')
     print("error")
 
