#El menú tendrá minimo 5 opciones (una de ellas será 'salir')
#Pedir valores por pantalla, tanto numeros como cadenas (para escribir el nombre del anime, ponerle nota o actualizar los episodios)
#Usar sentencias if y bucles
#Usar minimo 2 listas para almacenar y mostrar informacion
#Utilizar funciones y llamarlas en cada una de las opciones del menu

# control + alt + flechitas


# Para obtener un numero aleatorio hace falta importar la libreria 
from random import randint



#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------# VARIABLES PARA USAR EN EL PROGRAMA #--------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

salir = False #Condición booleana con la que se saldrá del bucle y finalizará el programa

terminar = False #Condición booleana para la opcion 3 (editar)

#manga [0] = titulo || manga [1] = autor || manga [2] = año de publicacion 
manga = [["One Piece", "Eiichiro Oda", 1997], ["Gintama", "Hideaki Sorachi", 2003], ["Fullmetal Alchemist", "Hiromu Arakawa", 2009],
         ["Jojo no Kimyou na Bouken: Ougon no Kaze", "Hirohiko Araki", 1995], ["Dragon Ball", "Akira Toriyama", 1984], ["Kimi wa Houkago Insomnia", "Makoto Ojiro", 2019]]

recomendacion = [["DanDaDan", "Tatsu Yukinobu", 2021], ["Slam Dunk", "Takehiko Inoue", 1990], ["Monster", "Naoki Urasawa", 1994], ["Akatsuki no Yona", "Mizuho Kusanagi", 2009],
                ["Spy x Family", "Tatsuya Endou", 2019], ["Yubisaki to Renren", "Morishita Tsuu", 2019], ["Barakamon", "Yoshino Satsuki", 2008], ["Wotaku ni Koi wa Muzukashii", "Fujita", 2015],
                ["Meitantei Conan", "Gosho Aoyama", 1994], ["Arte", "Kei Ookubo", 2013], ["Shingeki no Kyojin", "Hajime Isayama", 1994], ["Ansatsu Kyoushitsu", "Yuusei Matsui", 2012],
                ["Gokusen", "Kozueko Morimoto", 1999], ["Kimi ni Todoke", "Karuho Shiina", 2005], ["Orange", "Ichigo Takano", 2012], ["Death Note", "Tsugumi Ohba, Takeshi Obata", 2003],
                ["Haikyuu!!", "Haruichi Furudate", 2012], ["Naruto", "Masahi Kishimoto", 1999], ["Berserk", "Kentarou Miura", 1989], ["Hunter x Hunter", "Yoshihiro Togashi", 1998],
                ["Usemono Yado", "Hozumi", 2014], ["Uzumaki", "Junji Ito", 1998], ["Uchuu Kyoudai", "Chuuya Koyama", 2007], ["Planetes", "Makoto Yukimura", 1999],
                ["Jibaku Shounen Hanako-kun", "Aida Iro", 2014], ["Last Game", "Shinobu Amano", 2011], ["Bleach", "Tite Kubo", 2001], ["Ao Haru Ride", "Io Sakisaka", 2011]]

evitar_repeticion = [] #Array que va a almacenar cada una de las recomendaciones. CUando la recomendacion salga una vez, ese registro se va a guardar en el array. Se va a ir recorriendo: si ya ha salido, busca otro. Sino, saca es.

contador = 0

i = 0

k = 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------# FUNCIONES PARA USAR EN EL PROGRAMA #--------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Método con las diferentes opciones del menu. Solo se va a repetir una vez en el programa, pero quedará un codigo más limpio

def mostrar_menu():
    print("\n---------------------")
    print("|| Opciones a elegir:")
    print("--------------------------------------------------")
    print(" << OPCIÓN 1 - << MOSTRAR LISTA DE MANGA >>" )
    print(" << OPCIÓN 2 - << BUSCAR MANGA EN LA LISTA >>" )
    print(" << OPCIÓN 3 - << AÑADIR UN NUEVO MANGA >>" )
    print(" << OPCIÓN 4 - << EDITAR UN REGISTRO YA EXISTENTE >>" )
    print(" << OPCIÓN 5 - << RECOMENDACIÓN RANDOM >>" )    
    print(" << OPCIÓN 6 - << SALIR >>" )
    print("--------------------------------------------------\n\n")



# Este método comprobará en cada una de las opciones del menú que el usuario este seguro de seguir adelante con esa opcion
# Devuelve true unicamente si el usuario está seguro, sino, devolverá false y vuelve a elegirse opcion en el menu
def confirmar_opcion():
    if confirmacion.lower() == "si" or confirmacion.lower() == "s":
        return True
    elif confirmacion.lower() == "no" or confirmacion.lower() == "n":
        return False
    else:
        print("\nNo es una opción válida...")
        return False



#Voy a usar el metodo sacar_manga para las opciones 1, 2 y 3 (puede que 4 tambien). A la minima interaccion que haya con un registro, se va a sacar por pantalla,
#Asi el usuario va a tener constantemente el resultado de la "base de datos".
#Se saca por pantalla los distintos cajones del array: nombre del manga - autor - año
def sacar_manga():

    return print(contador + 1,".- ",manga[contador][0],"de",manga[contador][1],"(",manga[contador][2],")")



# Dependiendo de la opcion que se pase por parametro, la funcion entrara en distintos casos del switch
# Si se encuentra el nombre de la obra (para cambiar el nombre del manga o el año) o el autor (para cambiar el nombre del mismo), se guardará el nuevo parametro introducido.
def encontrar_manga(opcion, manga_aEditar):

    j = 0 #Se reinicia el contador a 0. Asi, cada vez que se use el metodo, va a empezar desde el principio.

    #Si el titulo se encuentra en la lista, se meterá por la opcion correspondiente a lo que se quiere editar.

    while j < len(manga):
        #Va a comparar con todas las filas de la columna 0, que es donde estan almacenados los titulos.
        if manga[j][0] == manga_aEditar:

            match opcion:

                case 2:
                    manga[j][0] = input("Nuevo nombre: ")

                case 3:
                    manga[j][1] = input("Nuevo autor: ")
                
                case 4:
                    manga[j][2] = input("Nuevo año: ")
                
            return "Se ha actualizado el registro con éxito: " + manga[j][0] + " de " + manga[j][1] + " (" + str(manga[j][2]) + ")" #str() -> castea a String, por si da problemas el numero enter
            #Si el manga estaba, va a devolver el return con el registro editado (despues se sacara el mensaje por pantalla)

        j += 1

    return "No existe ese manga, por lo que no se ha editado."
    #Si el manga no estaba, se va a devolver el return con el mensaje de edicion fallida (se sacará el mensaje por pantalla)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#




print("\n================================================")
print("|| ~ Bienvenid@ a la base de datos de manga ~ ||")
print("================================================\n")




# El bucle va a estar dando vueltas hasta que el usuario quiera salir.
while salir == False:
    mostrar_menu()
    opcion = int(input(">> ¿Qué desea hacer? -> "))
    match opcion:
        case 1:
            confirmacion = input("\n>> ¿Quiere acceder a la lista de manga? ")
            contador = 0
            if confirmar_opcion() == True:
                while contador < len(manga):
                    sacar_manga()
                    contador += 1

        
        case 2:
                confirmacion = input("\n>> ¿Desea buscar un manga en la lista? ")

                if confirmar_opcion() == True:
                    nombreBusqueda = input("\n¿Cuál es el manga que busca? ")

                    encontrado = False #Condicion booleana para ayudarme a la hora de encontrar un manga en el array bidimensional

                    while k < len(manga):
                        if nombreBusqueda == manga[k][0]:
                            encontrado = True
                            print("\nAquí están los datos del manga que buscaba!", manga[k][0],"de",manga[k][1],"que empezó a publicarse en",manga[k][2])
                            k = len(manga)
                        k += 1
                    
                    if encontrado == False:
                        print("\nLo sentimos. El manga " + nombreBusqueda + " no está en la lista.")



        
        case 3:
            confirmacion = input("\n>> ¿Quiere añadir un nuevo manga? ")
            
            if confirmar_opcion() == True:
                nombre_manga = input("Introduzca el nombre: ")
                autor_manga = input("Introduzca el autor: ")
                anio_manga = input("Introduzca el año de publicación: ")
                # El metodo append solo acepta un valor. 
                # Para introducir una fila más, se mete entre corchetes. Un valor por cada columna
                manga.append([nombre_manga,autor_manga,anio_manga]) 
                print("\nManga añadido con éxito! - " + nombre_manga + " de " + autor_manga + " (" + anio_manga + ")\n")
                
            
            
        case 4:
            confirmacion = input("\n>> ¿Quiere editar un registro? ")
            
            if confirmar_opcion() == True:
                
                # Este while va a seguir dando vueltas hasta que el usuario haya terminado de editar el registro y seleccione salir.
                # Puede editar los tres aspectos del registro tantas veces como quiera.
                while terminar == False:
                    print("1.- Eliminar un registro.")
                    print("2.- Editar nombre.")
                    print("3.- Editar autor.")
                    print("4.- Editar año.")
                    print("5.- Salir")

                    editar = int(input("\n¿Qué desea editar?: "))

                    match editar:
                        case 1:
                            manga_aEliminar = input("Introduzca el nombre del manga a eliminar: ")
                            i = 0
                            eliminado = False  #Condicion booleana cuando se encuentre el elemento. Sacará por pantalla un mensaje dependiendo de su valor final
                            # Si el nombre está incluido en el array, va a entrar en la condicion y se va a eliminar de la lista.
                            while i < len(manga):
                                if manga[i][0] == manga_aEliminar:
                                    # la funcion (del) va a borrar la fila que indique la i
                                    # Cuando encuentre el elemento, borrará toda la fila.
                                    del manga[i]
                                    i = len(manga) # Está condicion hará que se acabe el while cuando se haya encontrado el elemento, así no dara mas vueltas de las necesarias
                                    eliminado = True #Si el registro es borrado, eliminado cambia a true, y no va a sacar el print de que no existia
                                    print("El registro > [ " + manga_aEliminar + " ] < ha sido eliminado.\n") 
                                i += 1

                            if eliminado == False:
                                print("El registro > [ " + manga_aEliminar + " ] < no se encontraba en la lista, por lo que no se ha eliminado.\n")
                                #Print que saldrá si no existiese el registro, por lo que no se ha borrado.


                        case 2:
                            nombre_aEditar = input("Introduzca el nombre del manga a editar: ")
                            print(encontrar_manga(2, nombre_aEditar))
                            #Usando el metodo, se le introduce por parametros el numero de opcion y el nuevo nombre a editar
                            

                        case 3:
                            autor_aEditar = input("Introduzca el nombre del manga al que editarle el autor: ")
                            print(encontrar_manga(3, autor_aEditar))
                            #Usando el metodo, se le introduce por parametros el numero de opcion y el nuevo autor a editar


                        case 4:
                            anio_aEditar = input("Introduzca el nombre del manga al que editarle el año: ")
                            print(encontrar_manga(4, anio_aEditar))
                            #Usando el metodo, se le introduce por parametros el numero de opcion y el nuevo año a editar


                        case 5:
                            print("Volviendo al menú principal...")
                            terminar = True
                            #Condicion booleana con la que acabará el bucle y saldrá al menu principal.


                        case other:
                            print("No es una opcion válida... solo del 1 al 5.")
            

        case 5:
            confirmacion = input("\n>> ¿Desea recibir recomendación aleatoria? ")
            if confirmar_opcion() == True:
                numero_recomendacion = int(input("¿Cuántas? ")) #Recibirá el numero de recomendaciones que se quieren recibir
                contador = 0 #Variable para ir acumulando las recomendaciones, y no dar vueltas innecesarias
            
                print("Generando recomendaciones...")
                while contador < numero_recomendacion: # Se imprimirán el numero de recomendaciones que ha pedido el usuario.  
                    numeroAleatorio = randint(0, len(recomendacion) - 1)
                    if numeroAleatorio not in evitar_repeticion:
                        print(recomendacion[numeroAleatorio])
                        evitar_repeticion.append(numeroAleatorio)
                        contador += 1
                evitar_repeticion = [] #Para borrar el array cuando acabe el while, asi no habra un limite de titulos que recomendar (sino el programa se queda pillado)
            
            
        case 6:
            confirmacion = input("\n>> ¿Desea salir del programa? ")

            if confirmar_opcion() == True:
                salir = True 
                print("Vuelva pronto!! ")

        
            

        # Si el numero introducido por el usuario no se encuenta entre el 1 y el 5, se va a volver a pedir un numero.
        case other:
            print("\nNo es una opcion válida... solo del 1 al 5.\n")
            

