# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define narrador = Character("Narrador")
define emir = Character("Emir")
define albedo = Character("Albedo")
define amelia = Character("Amelia")

image fondoNegro = "fondo_negro.jpg"
image biblioteca1 = "biblioteca.png"
image salidaSchool = "escuela.jpg"
image calle = "calle.png"
image casa = "casa.jpg"

# El juego comienza aquí.

label start:
    #Acto 1
    #Escena 1 Ruta Main
    label escena1RutaMain:
        jump escena_1_RM

    #Escena 2 Ruta Main
    label escena2RutaMain:
        jump escena_2_RM

    #Decision 1
    label decicion1:
        menu:
            "Ir al centro comercial con Albedo":
                #Escena 3 Ruta Main
                jump escena_3_RM
            "No ir al centro comercial con Albedo":
                #Escena 1 Ruta Neutral
                jump escena_1_RN
    
    #Decicion 2
    label decicion2:
        menu:
            "Quedarse y escuchar el plan de Albedo":
                #Escena 4 Ruta Main
                jump escena_4_RM
            "Huir del lugar he ir a casa":
                #Escena 1 Ruta Neutral
                jump escena_1_RN