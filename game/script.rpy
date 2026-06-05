# Coloca el codigo de tu juego en este archivo.


screen correo_convocatoria():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 980
        padding (36, 30)
        background "#071b34dd"

        vbox:
            spacing 14

            text "DE: Editorial \"Nuevo Horizonte\"" size 34 color "#ffffff" bold True
            text "ASUNTO: Convocatoria Literaria Anual" size 34 color "#ffffff" bold True
            text "CUERPO: Estimados autores, recordamos que el plazo final para la recepcion de manuscritos es el 14 de abril. El ganador recibira la publicacion de su obra bajo nuestro sello y un adelanto en concepto de regalias. No se aceptaran historias fuera de termino.":
                size 30
                color "#ffffff"
                line_spacing 8

    textbutton "Continuar":
        xalign 0.5
        yalign 0.86
        action Return()


# El juego comienza aqui.

label start:

    scene black

    narrador "DIA 1"
    narrador "Fondo: Oficina gris, luz fluorescente parpadeante. Sonido de teclados y telefonos de fondo."
    narrador "Se observa a Gabriel, sentado frente a la PC en su cubiculo de la oficina."
    narrador "(Se abre una ventana emergente en la pantalla de la PC: un correo electronico.)"

    call screen correo_convocatoria

    pensamiento "Faltan siete dias. Solo siete dias."

    narrador "(Entra Daniel, el jefe, caminando con paso pesado. Se apoya en el escritorio de Gabriel, invadiendo su espacio.)"

    daniel "Gabi, querido. Escuchame, surgio un problema con la carga de los remitos de la zona sur. Necesito que te quedes un par de horas mas para cerrar el balance hoy."
    gabriel "Pero Daniel, hoy tenia que..."
    daniel "Dale, no me falles. Sabes que la mano viene dura y necesito gente comprometida. Te quedas, no?"

    menu:
        "Aceptar":
            narrador "Gabriel acepta quedarse."

        "Excusarse":
            narrador "Gabriel intenta excusarse."

    return
