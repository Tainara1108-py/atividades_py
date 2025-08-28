
def classificar_numero(n1):
    if n1 <0:
     return 'numero negativo'
    
    elif n1 <0 and n1>10 :
        return 'numero positivo'
    
    elif n1 <10 and n1 >100:
       return 'entre 0 e 100'
    else:
        return 'maior que 100'
    
print(classificar_numero(-9))
  
     

    

    



