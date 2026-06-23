# Coloca el código de tu juego en este archivo.


# El juego comienza aquí.

default decision_horas_extra = None
default decision_calle = None
default estado_animo_eva = None
default tono_novela = None


label start:

    scene bg oficina with dissolve

    play music "audio/SFX/sonidoAmbienteOficina.mp3"

    narrador "DÍA 1"
    scene bg reloj_18hs with dissolve
    $ renpy.pause(2)
    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Ya casi son las seis. Por fin me puedo ir a casa. Reviso este mail y me voy."
    play sound "audio/SFX/mouseclick.mp3"

    scene bg oficina with dissolve
    call screen correo_convocatoria

    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Faltan siete días. Solo siete días."

    show daniel normal at busto_derecha with dissolve
    daniel "Gabi, querido. Escuchame, surgió un problema con la carga de los remitos de la zona sur. Necesito que te quedes un par de horas más para cerrar el balance hoy."
    gabriel "Pero Daniel, hoy tenía que..."

    show daniel enojado at busto_derecha with dissolve

    daniel "Dale, no me falles. Sabés que la mano viene dura y necesito gente comprometida. ¿Te quedás, no?"

    menu:
        "Aceptar":
            $ decision_horas_extra = "aceptar"
            gabriel "Está bien, Daniel. Me quedo a terminar los remitos."
            show daniel normal at busto_derecha with dissolve
            daniel "¡Así me gusta! Sabía que podía contar con tu compromiso. Yo me voy a casa, pero confío en que vas a dejar todo lo que falta cerrado."
            show gabriel enojado at busto_izquierda with dissolve
            gabriel "Nos vemos mañana, Daniel."
            hide daniel with dissolve
            play sound "audio/SFX/closedoor.mp3"
            $ renpy.pause(1.0)
            stop music fadeout 2.0
            jump dia1_parada_colectivo

        "Excusarse":
            $ decision_horas_extra = "excusarse"
            gabriel "Te pido disculpas, Daniel, pero hoy me es imposible. Tengo un compromiso familiar que no puedo postergar."
            daniel "Bueno... Una lástima. Pensé que estabas más comprometido con el equipo. Podés irte."
            hide daniel enojado with dissolve
            pensamiento "Espero no habérmela mandado. Mejor me voy yendo antes de que cambie de opinión."
            stop music fadeout 2.0
            jump dia1_calle_temprano


label dia1_calle_temprano:

    scene bg centro_floreria with dissolve
    show gabriel normal at busto_izquierda with dissolve

    pensamiento "Le dije que no a Daniel. Eva me va a matar por jugármela así. Pero hoy, por una vez, prioricé volver a casa temprano para estar con ellos y avanzar con el libro."

    pensamiento "Hace mucho no tengo un gesto con Eva. ¿Servirá de algo a esta altura? ¿O va a pensar que le llevo algo nada más para que no se enoje?"

    menu:
        "Volver a casa":
            $ decision_calle = "volver_a_casa"
            jump dia1_casa_directo

        "Comprar regalo":
            $ decision_calle = "comprar_regalo"
            $ estado_animo_eva = "calido"
            jump dia1_casa_flor

label dia1_casa_directo:

    scene bg cocina_fria with dissolve
    play music "audio/MUSICA/tango cocina.mp3"
    show gabriel normal at busto_izquierda with dissolve
    show eva normal at busto_derecha with dissolve
    lucas "¡Papá! Llegaste temprano."
    gabriel "(Le acaricia la cabeza a Lucas y mira a Eva con cautela). Hola."
    eva "(Levanta la vista de los papeles, extrañada) ¿Qué pasó? ¿Te dejaron salir a horario hoy de milagro?"
    gabriel "Daniel me pidió que me quede a hacer horas extra, pero le dije que no. Necesitaba volver a casa... y avanzar con la novela. Me queda una semana."
    eva "(Suspira, frotándose la frente y señalando la mesa) Gabriel... no estamos en condiciones de rechazar plata extra del laburo."
    gabriel "(Se acerca, tenso) Ya sé, Eva. Pero si termino la novela y gano el concurso, el adelanto editorial nos da un respiro en serio. Necesito este tiempo para escribir."
    eva "(Con voz dura, pragmática). Me alegra que estés acá con nosotros, pero me asusta lo que estás apostando. (Se pone de pie). Lucas, vamos a la pieza a terminar la tarea, dejá a tu papá \"trabajar\"."

    show lucas normal at busto_derecha with dissolve

    stop music fadeout 1.0
    scene bg habitacion_gabriel_oscuro with dissolve
    scene bg papeles_escritorio with dissolve

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "No me entienden. Quizás nadie lo haga. Pero tengo que ganar esto como sea."
    jump dia1_eleccion_tono


label dia1_casa_flor:

    scene bg interior_floreria with dissolve
    play music "audio/MUSICA/tango florería.mp3"

    show vendedor normal at busto_derecha with dissolve
    vendedor "Buscás algo para pedir perdón o para que no se olviden de vos, ¿no? Se te nota en la cara."
    
    show gabriel normal at busto_izquierda with dissolve
    gabriel "Un poco de las dos cosas, creo. Busco algo sencillo. No puedo gastar mucho hoy."
    show vendedor feliz at busto_derecha with dissolve
    vendedor "Entran muchos muchachos como vos acá. Corriendo, mirando el reloj, con la cabeza llena de cuentas y problemas del laburo. En el camino se van desconectando de los que los esperan en casa."
    gabriel "Es que hace tanto que no le llevo nada. No sé. Tengo miedo de que piense que se lo llevo nada más para tapar mi culpa."
    
    scene bg primer_plano_flor with dissolve
    vendedor "Llevate esta rosa sola entonces."
    scene bg interior_floreria with dissolve
    
    show vendedor normal at busto_derecha with dissolve
    show gabriel normal at busto_izquierda with dissolve
    vendedor "Si le caés con un ramo gigante y caro, va a pensar que te mandaste una macana o que querés comprarla. Pero una sola flor dice: frené un segundo mi día sólo para acordarme de vos."
    gabriel "¿Frenar un segundo? No lo había pensado de esa forma."
    vendedor "Exacto. El valor no está en el precio, sino en el gesto de haber pensado en el otro. Estar en paz con los que te aman te ayuda a pensar. Te limpia la cabeza. Y se nota que necesitás despejar la cabeza."
    show gabriel feliz at busto_izquierda with dissolve
    gabriel "Tenés razón. Gracias, me la llevo."
    vendedor "Gran decisión. Espero que le vaya muy bien."
    gabriel "Muchas gracias por el consejo. Hasta luego."

    show vendedor feliz at busto_derecha with dissolve
    stop music fadeout 2.0
    $ renpy.pause(1)

    scene bg cocina_calida with dissolve
    play music "audio/MUSICA/tango_rosa.mp3"
    $ renpy.pause(1)
    show gabriel normal at busto_izquierda with dissolve

    $ renpy.pause(1)
    show lucas feliz at busto_derecha with dissolve
    lucas "¡Papá! ¡Llegaste!"
    
    show gabriel feliz at busto_izquierda with dissolve
    gabriel "¡Hola campeón!"
    hide lucas feliz
    show eva normal at busto_derecha with dissolve
    gabriel "Tomá. Pasé por la florería y me acordé de vos."

    eva "Es hermosa, amor, gracias."
    
    show eva feliz at busto_derecha with dissolve
    gabriel "No tanto como vos."
    eva "Que romántico que estas hoy. ¿Cómo estuvo tu día? ¿Te fue bien en la oficina hoy?"
    gabriel "No mucho. Me pidieron quedarme horas extra y le dije que no. No le gustó nada al jefe. Quería tiempo para ustedes y para escribir."
    eva "Te amamos, pero me preocupa que tu sueño de escribir te vaya a complicar el laburo."
    gabriel "Necesito el tiempo para la historia, amor. Quería que estuviéramos bien antes de sentarme a escribir. No los voy a defraudar."
    eva "Te dejo a lo tuyo entonces. Voy a ayudar a Lucas con la tarea."
    hide gabriel feliz
    show lucas normal at busto_izquierda with dissolve
    lucas "¿Ahora? ¡Pero quería jugar con papá!"

    hide eva feliz
    show gabriel feliz at busto_derecha with dissolve
    gabriel "Mañana será, hijo. Ahora a estudiar con mamá."

    hide lucas normal with dissolve
    stop music fadeout 0.5
    scene bg habitacion_gabriel with dissolve
    show gabriel feliz at busto_izquierda with dissolve
    pensamiento "El florista tenía razón. El ambiente se siente distinto. Menos pesado."
    scene bg papeles_escritorio with dissolve

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. No los puedo defraudar."
    jump dia1_eleccion_tono


label dia1_parada_colectivo:

    scene bg reloj_18hs with dissolve
    play sound "audio/SFX/slow clock ticking.mp3"
    $ renpy.pause(1)
    scene bg reloj_21hs with dissolve
    $ renpy.pause(2)
    stop sound fadeout 0.4
    scene black with dissolve
    scene bg parada_lluvia with dissolve
    play music "audio/SFX/lluviaGeneral.mp3"

    show gabriel triste at busto_izquierda with dissolve
    show vagabundo normal at busto_derecha with dissolve
    vagabundo "Una ayuda, jefe... para un café. Hace mucho frío."

    menu:
        "Ayudarlo":
            $ decision_calle = "ayudar"
            $ estado_animo_eva = "frio"
            jump casa_ayuda

        "Ignorarlo":
            $ decision_calle = "ignorar"
            $ estado_animo_eva = "agresivo"
            jump casa_ignora


label casa_ayuda:

    "Gabriel saca un billete de 2.000 pesos arrugado. Se lo entrega al hombre."

    show gabriel normal at busto_izquierda with dissolve
    show vagabundo feliz at busto_derecha with dissolve
    vagabundo "Gracias, bendiciones. Ya me ignoraron tantos que solo me quedaba soñar."

    gabriel "Mal día. Mañana será otro."

    vagabundo "Eso decimos todos. Tené cuidado, a veces uno se pasa la vida escribiendo el prólogo y se olvida de que el libro tiene muchas páginas."

    gabriel "¿Qué? ¿Vos sabés quién soy? ¿Cómo sabés que escribo?"

    vagabundo "Te aferrás a tus cosas como si tu vida estuviera ahí. Si llevas algo que vale la pena, lo abrazas."

    gabriel "Ya llega el bondi. Me tengo que ir."

    scene bg bondi_primer_plano with dissolve
    $ renpy.pause(2)

    hide vagabundo feliz with dissolve
    scene bg bondi_llegando with dissolve
    play sound "audio/SFX/sonidoColectivo.mp3"

    scene bg interior_colectivo with dissolve
    show gabriel normal at busto_izquierda with dissolve
    gabriel "{i}Uno se pasa la vida escribiendo el prólogo. Solo yo me encuentro estos personajes.{/i}"

    scene bg cocina_calida with dissolve
    stop sound fadeout 0.5
    stop music fadeout 0.5
    
    play music "audio/MUSICA/tango cocina.mp3"

    show eva normal at busto_derecha with dissolve

    show gabriel normal at busto_izquierda with dissolve
    eva "Lucas ya se durmió. Estuvo preguntando por qué su papá no llegaba."

    show gabriel triste at busto_izquierda with dissolve
    gabriel "Perdón Eva. Daniel me encajó lo de zona sur. Me tuve que quedar."

    show eva triste at busto_derecha with dissolve
    eva "¿Te van a pagar esta vez las horas extra?"
    show eva enojada at busto_derecha with dissolve
    eva "¿O es otro favor para cuidar el puesto?"

    show gabriel normal at busto_izquierda with dissolve
    gabriel "Probablemente no... pero no puedo decir que no ahora. No con cómo están las cosas."

    show eva normal at busto_derecha with dissolve
    gabriel "Eva, me queda una semana para terminar una historia. Si gano, puedo cambiar las cosas."

    show eva enojada at busto_derecha with dissolve
    eva "¿Ahora te parece el mejor momento, Gabriel? No sé si estamos para sueños ahora."
    play sound "audio/SFX/mujersuspiro.mp3"
    stop music fadeout 0.5
    $ renpy.pause(2)
    hide eva with dissolve
    play sound "audio/SFX/closedoor.mp3"
    

    if estado_animo_eva not in ("frio", "agresivo"):
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve
    $ renpy.pause(2.0, hard=True)
    scene bg papeles_escritorio with dissolve

    $ renpy.pause(1.0, hard=True)
    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. Es lo único que me queda."
    jump dia1_eleccion_tono


label casa_ignora:

    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Mejor me alejo un poco."
    hide vagabundo with dissolve

    play sound "audio/SFX/autocharco.mp3"
    scene bg auto_charco with dissolve
    
    $ renpy.pause(4)

    scene bg parada_lluvia with dissolve
    show gabriel enojado at busto_izquierda with dissolve
    gabriel "¡No lo puedo creer! ¡¿Es joda?!"

    pensamiento "Me embarró todo. Qué asco. Ahí viene el bondi encima."

    scene bg bondi_primer_plano with dissolve
    $ renpy.pause(2)

    scene bg interior_colectivo with dissolve
    play sound "audio/SFX/sonidoColectivo.mp3"
    show gabriel enojado at busto_izquierda with dissolve
    pensamiento "Qué locura cómo estamos. La calle no perdona a nadie."
    

    stop music fadeout 0.5

    scene bg entrada_casa with dissolve
    stop sound fadeout 0.7
    

    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Me tengo que sacar el barro antes de poner a lavar esto."
    play music "audio/MUSICA/musicaDiscusion.mp3"

    scene bg banio with dissolve
    show gabriel enojado at busto_izquierda with dissolve
    

    show gabriel enojado at busto_izquierda with dissolve
    show eva triste at busto_derecha with dissolve
    eva "Gabriel... escuché la puerta y no venías a la cocina. ¿Qué te pasó?"
    show gabriel enojado at busto_izquierda with dissolve
    gabriel "Un taxi. Agarró un pozo enorme en la avenida. No pasa nada, sale con agua."
    show eva triste at busto_derecha with dissolve
    eva "Estás temblando, Gabi. Y llegaste tardísimo, Lucas te estuvo esperando para..."
    show gabriel enojado at busto_izquierda with dissolve
    gabriel "¡Ya sé que llegué tarde, Eva! ¡Me tuve que quedar haciendo los remitos de mierda de Daniel y encima me pasa esto! ¡No me lo recuerdes!"
    show eva enojada at busto_derecha with dissolve
    eva "No me grites. Yo no tengo la culpa de que no te animes a decirle que no a tu jefe."
    show gabriel enojado at busto_izquierda with dissolve
    gabriel "Todo esto es para nosotros. Si gano el concurso la semana que viene..."
    show eva enojada at busto_derecha with dissolve
    eva "Mirate, Gabriel. Estás lavando barro de tu única ropa decente en un baño congelado a las diez de la noche. Secate y andá a dormir, no quiero que Lucas te escuche gritar así."

    

    hide eva with dissolve
    show gabriel triste at busto_izquierda with dissolve
    $ renpy.pause(3)
    scene bg habitacion_gabriel_oscuro with dissolve
    $ renpy.pause(2)
    scene bg papeles_escritorio with dissolve

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    show gabriel triste at busto_izquierda with dissolve
    pensamiento "Tengo que escribir. Es lo único que me queda."
    jump dia1_eleccion_tono


label dia1_eleccion_tono:

    scene bg cursor_pantalla with dissolve

    narrador "(El cursor parpadea sobre la hoja en blanco. Lo vivido durante el día todavía pesa, pero Gabriel debe decidir qué voz tendrá la novela.)"
    narrador "(El inconsciente de Gabriel lo inclina a escribir con un tono...)"

    menu:
        "Melancólico":
            $ tono_novela = "melancolico"
            narrador "Gabriel empieza a escribir desde la melancolía."

        "Cínico/Agresivo":
            $ tono_novela = "cinico_agresivo"
            narrador "Gabriel empieza a escribir con una voz cínica y agresiva."

        "Esperanzador":
            $ tono_novela = "esperanzador"
            narrador "Gabriel empieza a escribir aferrándose a la esperanza."
    stop music fadeout 2.0
    jump dia1_convergencia_final


label dia1_convergencia_final:

    if estado_animo_eva not in ("frio", "agresivo"):
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve

    $ renpy.pause(2.0, hard=True)
    scene bg moneda_escritorio with dissolve

    $ renpy.pause(2.0, hard=True)

    scene black with dissolve
    $ renpy.pause(2.0, hard=True)
    scene bg habitacion_lucas with dissolve
    play music "audio/MUSICA/musicaflashback.mp3"
    show lucas feliz at busto_izquierda with dissolve
    $ renpy.pause(2.0, hard=True)
    scene bg juguetes_lucas with dissolve
    $ renpy.pause(2.0, hard=True)
    show lucas feliz at busto_izquierda with dissolve
    $ renpy.pause(2.0, hard=True)
    scene bg habitacion_lucas with dissolve
    show lucas normal at busto_izquierda with dissolve
    lucas "Me quiero llevar uno para mostrarle a mis amigos hoy, pero no sé cuál llevar, pa."

    scene bg juguetes_lucas with dissolve
    $ renpy.pause(2)

    scene bg habitacion_lucas with dissolve
    show lucas normal at busto_izquierda with dissolve
    show gabriel normal at busto_derecha with dissolve

    gabriel "(Sonriendo, saca una moneda del bolsillo). Te voy a enseñar un truco. Vamos a tirarla. Cara es el auto, ceca es el dragón."
    
    show lucas triste at busto_izquierda with dissolve
    lucas "¡Pero eso es elegir a ver cuál tiene más suerte! ¡No me gusta!"

    show gabriel normal at busto_derecha with dissolve    
    gabriel "Ahí está el secreto. Tirala bien alto. En el momento en que la moneda esté en el aire, antes de que caiga, vas a sentir que hay una de las dos opciones que preferís que salga."

    show lucas enojado at busto_izquierda with dissolve
    lucas "¿Para qué tiro la moneda entonces?"

    show gabriel feliz at busto_derecha with dissolve
    gabriel "Porque no importa lo que diga la moneda, solo qué sentiste mientras volaba. Vamos a probar."

    scene bg moneda_volando_flashback with dissolve
    play sound "audio/SFX/coin flip.mp3"
    $ renpy.pause(2.0, hard=True)
    show gabriel feliz at busto_derecha with dissolve
    show lucas enojado at busto_izquierda with dissolve
    $ renpy.pause(2.0, hard=True)
    scene black with dissolve
    scene bg habitacion_lucas with dissolve
    show lucas feliz at busto_izquierda with dissolve
    lucas "¡Vamos! ¡Llevo el dragón!"
    show gabriel feliz at busto_derecha with dissolve
    narrador "(Lucas le da un abrazo a Gabriel.)"
    $ renpy.pause(1.0, hard=True)
    stop music fadeout 2.0
    scene black with dissolve
    $ renpy.pause(2.0, hard=True)

    play music "audio/MUSICA/Carlos-Gardel-Por-una-cabeza.mp3"
    scene bg moneda_escritorio with dissolve
    $ renpy.pause(3.0)
    

    scene  bg mone
    if estado_animo_eva not in ("frio", "agresivo"):
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve
    if estado_animo_eva not in ("frio", "agresivo"):
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve

    $ renpy.pause(2.0, hard=True)
    show gabriel triste at busto_izquierda with dissolve
    pensamiento "¿Qué es lo que realmente quiero? ¿Qué tengo que hacer?"
    scene bg moneda_escritorio with dissolve
    $ renpy.pause(2.0, hard=True)
    show gabriel triste at busto_izquierda with dissolve
    $ renpy.pause(2.0, hard=True)

    scene bg moneda_volando with dissolve
    play sound "audio/SFX/coin flip.mp3"
    $ renpy.pause(2.0, hard=True)
   
    play sound "audio/SFX/hombresuspiro.mp3"
    if estado_animo_eva not in ("frio", "agresivo"):
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve
    narrador "(Gabriel no mira el resultado.)"
    scene black with dissolve
    sistema "FIN DEL DÍA 1"

    return

