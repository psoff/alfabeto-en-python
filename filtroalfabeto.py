texto = 'funeraria jaramillo'

def get_vowels(frase):
    vocales = 'aeiou'

    return [c for c in frase if c in vocales ]

print(get_vowels(texto))

def get_letters(frase):
    letras = 'bcdfghjklmnpqrstvwxyz'

    return [c for c in frase if c in letras ]

print(get_letters(texto))

