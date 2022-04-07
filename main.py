#ASCII code
# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

'''
Programa para ver la lista de caracteres del còdigo ASCII
(American Standard Code for Information Interchange)
'''

#Modules
import os
import webbrowser
import mysql.connector
from decouple import config
from historia import history
from tutorial import tutorial
from colorama import Fore, init

#To change the text color in the cmd
init()

#To clean the screen
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#cnn Connector Object and Cur Cursor
host = os.environ.get('HOST')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
cnn = mysql.connector.connect(host = host, user = user, passwd = password, database = "codascii")
cur = cnn.cursor()

#Option menu
menu = '''\n************
Còdigo ASCII
************

1. Ver lista de Caracteres
2. Historia
3. Pàginas Web
4. ¿Como imprimir los Caracteres?
5. Finalizar Programa

'''

menu_caracteres = '''\n***************************
Caracteres del còdigo ASCII
***************************

C. Caracteres de Control
I. Caracteres Imprimibles
E. Extendido
S. Salir

'''

flag = True
while flag:
    clearConsole()
    print(Fore.GREEN + menu)
    opcion = int(input("\n¿Que desea hacer? : "))
    
    #Character list
    if opcion == 1:
        salir = 0
        while salir != 1:
            clearConsole()
            print(menu_caracteres)
            caracter = input("\n¿Que desea ver? : ")
            caracter = caracter.upper()
            
            #Control
            if caracter == 'C':
                #We ask about the control table
                sql = "SELECT * FROM control"
                cur.execute(sql)
                tabla = cur.fetchall()
                
                #We print the control table
                for row in tabla:
                    print(row)
                
                input("\n\n--> Presione ENTER para continuar...")
            
            #Printable      
            elif caracter == 'I':
                #We ask about the printable table
                sql = "SELECT * FROM imprimibles"
                cur.execute(sql)
                tabla = cur.fetchall()
                
                #We print the printable table
                for row in tabla:
                    print(row)
                    
                input("\n\n--> Presione ENTER para continuar...")
            
            #Extended     
            elif caracter == 'E':
                #We ask about the extended table
                sql = "SELECT * FROM extendido"
                cur.execute(sql)
                tabla = cur.fetchall()
                
                #We print the extended table
                for row in tabla:
                    print(row)
                
                input("\n\n--> Presione ENTER para continuar...")
            
            elif caracter == 'S':
                salir = 1
            
            else:
                print('\n--> Esa opciòn no existe')
                input("\n\n--> Presione ENTER para continuar...")
    
    #History
    elif opcion == 2:
        clearConsole()
        historia = history()
        print(historia)
        input("\n\n--> Presione ENTER para continuar...")
        continue
    
    #Websites
    elif opcion == 3:
        while flag:
            clearConsole()
            print("***Paginas Web***\n\n")
            print("\n1. Pàgina de los caracteres ASCII")
            print("2. Pàgina de la historia ASCII")
            ver = int(input("\n¿Què dèsea abrir? "))
            
            #Character page
            if ver == 1:
                webbrowser.open('https://elcodigoascii.com.ar/')
                break
            #History page
            elif ver == 2:
                webbrowser.open('http://informatica.dgenp.unam.mx/recomendaciones/codigo-ascii')
                break
            else:
                print('\n--> Esa opciòn no existe')
                input("\n\n--> Presione ENTER para continuar...")
                continue
            
    #Tutorial
    elif opcion == 4:
        clearConsole()
        c = tutorial()
        input("\n\n--> Presione ENTER para continuar...")
        continue
        
    #End Program
    elif opcion == 5:
        print("\n--> Programa Finalizado")
        flag = False
        break
    
    #Invalid option
    else:
        print("\n--> Esa opciòn no existe")
        continue
