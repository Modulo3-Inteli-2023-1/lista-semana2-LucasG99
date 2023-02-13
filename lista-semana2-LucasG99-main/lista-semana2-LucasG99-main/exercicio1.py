#  Se achar necessario, faça import de outras bibliotecas





def conta_palavras_unicas(frase):
    palavras = frase.split()
    
    conjunto_palavras = set(palavras)
    
    return len(conjunto_palavras)
frase = "Inteli é a melhor faculdade de Tecnologia da América Latina"

print(conta_palavras_unicas(frase)) 









# Teste a sua função aqui (caso ache necessário)











