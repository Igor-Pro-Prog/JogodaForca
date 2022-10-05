palavra_secreta = 'UFCA'

Letras_acertadas = ['_', '_','_','_']

acertou= False
enforcou= False
erros = 0
while(not acertou and not enforcou): 
    chute=input("Qual a letra")
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(letra == chute):
                Letras_acertadas[posicao] = letra
            posicao +=1 
    else:
        erros+=1    
    if (erros == 6):
        enforcou = True
    if ('_' not in Letras_acertadas):  
        acertou = True   
    print (Letras_acertadas)   
if (acertou):
    print ('Parabéns!!!')
if (enforcou):
    print ("Errou")
