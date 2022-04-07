# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

ayuda = ''' ¿Còmo usar el còdigo ASCII?

Muy sencillo, para eso presionamos 'ALT' + 'NUMBER'.
Automaticamente, se imprimirà el caracter que deseas

¿Quieres hacer una prueba?
 
'''

def tutorial():
    print(ayuda)
    
    flag = True
    while flag:
        prueba = input("\nPresione 'ALT' + '61' {=} : ")
    
        if prueba != '=':
            print("\n--> Intentemos de vuelta :)")
            continue
        else:
            print("\n--> ¡Felicidades, ya sabes como hacerlo!")
            completado = 1
            break
        
    return completado

