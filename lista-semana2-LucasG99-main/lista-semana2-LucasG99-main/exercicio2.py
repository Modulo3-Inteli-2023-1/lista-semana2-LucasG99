#  Se achar necessario, faça import de outras bibliotecas





def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(list(s1)) == sorted(list(s2))

print(is_anagram("amigo", "maigo")) 
print(is_anagram("casa", "asac")) 
print(is_anagram("feliz", "infeliz")) 





# Teste a sua função aqui (caso ache necessário)











