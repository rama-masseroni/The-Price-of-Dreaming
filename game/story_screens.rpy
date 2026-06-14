# Pantallas narrativas reutilizables.


screen correo_convocatoria():
    modal True
    zorder 200

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
            text "CUERPO: Estimados autores, recordamos que el plazo final para la recepción de manuscritos es el 14 de abril. El ganador recibirá la publicación de su obra bajo nuestro sello y un adelanto en concepto de regalías. No se aceptarán historias fuera de término.":
                size 30
                color "#ffffff"
                line_spacing 8

            textbutton "Continuar":
                xalign 0.5
                top_margin 18
                action Return(True)

    key "dismiss" action Return(True)


screen documento_aviso(titulo, cuerpo, sello=None):
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 940
        padding (40, 34)
        background "#f2f0e8ee"

        vbox:
            spacing 18

            text titulo:
                size 36
                color "#202020"
                bold True
                xalign 0.5

            text cuerpo:
                size 30
                color "#202020"
                line_spacing 8

            if sello:
                text sello:
                    size 44
                    color "#8f1d1d"
                    bold True
                    xalign 0.5

            textbutton "Continuar":
                xalign 0.5
                top_margin 18
                action Return(True)

    key "dismiss" action Return(True)
