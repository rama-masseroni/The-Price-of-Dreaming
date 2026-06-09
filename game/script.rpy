# Coloca el código de tu juego en este archivo.


# El juego comienza aquí.

default decision_horas_extra = None
default decision_calle = None
default tono_novela = None


label start:

    scene black

    narrador "DÍA 1"
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Oficina gris, luz fluorescente parpadeante. Sonido de teclados y teléfonos de fondo."
    narrador "Se observa a Gabriel, sentado frente a la PC en su cubículo de la oficina."
    narrador "(Se abre una ventana emergente en la pantalla de la PC: un correo electrónico.)"

    call screen correo_convocatoria

    pensamiento "Faltan siete días. Solo siete días."

    narrador "(Entra Daniel, el jefe, caminando con paso pesado. Se apoya en el escritorio de Gabriel, invadiendo su espacio.)"

    daniel "Gabi, querido. Escuchame, surgió un problema con la carga de los remitos de la zona sur. Necesito que te quedes un par de horas más para cerrar el balance hoy."
    gabriel "Pero Daniel, hoy tenía que..."
    daniel "Dale, no me falles. Sabés que la mano viene dura y necesito gente comprometida. ¿Te quedás, no?"

    menu:
        "Aceptar":
            $ decision_horas_extra = "aceptar"
            jump dia1_parada_colectivo

        "Excusarse":
            $ decision_horas_extra = "excusarse"
            jump dia1_calle_temprano


label dia1_calle_temprano:

    narrador "(Tras negarse a las horas extra, Gabriel camina por el centro antes de tomar el colectivo. Se detiene frente a una florería pequeña.)"
    pensamiento "Hace mucho no tengo un gesto con Eva. El laburo me está matando."

    menu:
        "Volver a casa":
            $ decision_calle = "volver_a_casa"
            jump dia1_casa_directo

        "Comprar regalo":
            $ decision_calle = "comprar_regalo"
            jump dia1_casa_flor

label dia1_casa_directo:

    narrador "(Transición)"
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Cocina pequeña, luz fría. Eva está sentada en la mesa revisando unos papeles con el ceño fruncido. Lucas está dibujando en un rincón."

    lucas "¡Papá! Llegaste temprano."
    gabriel "(Le acaricia la cabeza a Lucas y mira a Eva con cautela). Hola."
    eva "(Levanta la vista de los papeles, extrañada) ¿Qué pasó? ¿Te dejaron salir a horario hoy de milagro?"
    gabriel "Daniel me pidió que me quede a hacer horas extra, pero le dije que no. Necesitaba volver a casa... y avanzar con la novela. Me queda una semana."
    eva "(Suspira, frotándose la frente y señalando la mesa) Gabriel... no estamos en condiciones de rechazar plata extra del laburo."
    gabriel "(Se acerca, tenso) Ya sé, Eva. Pero si termino la novela y gano el concurso, el adelanto editorial nos da un respiro en serio. Necesito este tiempo para escribir."
    eva "(Con voz dura, pragmática). Me alegra que estés acá con nosotros, pero me asusta lo que estás apostando. (Se pone de pie). Lucas, vamos a la pieza a terminar la tarea, dejá a tu papá \"trabajar\"."

    narrador "(Eva y Lucas salen de la escena. El ambiente de la cocina queda frío y envuelto en un silencio incómodo.)"
    narrador "(Transición)"
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Habitación en penumbra. Gabriel frente a la PC. El silencio de la casa pesa."
    narrador "(A un costado del teclado, se destaca el aviso de la AFIP.)"

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "No me entienden. Quizás nadie lo haga. Pero tengo que ganar esto como sea."
    jump dia1_eleccion_tono


label dia1_casa_flor:

    narrador "(Entra al local. Un vendedor mayor lo observa detrás de varios ramos de flores.)"

    vendedor "Buscás algo para pedir perdón o para que no se olviden de vos, ¿no? Se te nota en la cara."
    gabriel "(Mira los precios, preocupado) Algo sencillo. No puedo gastar mucho hoy, de verdad."
    vendedor "(Saca una única rosa) Llevate esta. El valor no está en el precio, sino en el gesto de haber pensado en el otro. Estar en paz con los que aman te ayuda a pensar. Te limpia la cabeza."
    gabriel "(Mira su billetera, sonríe levemente y paga) Gracias, me la llevo."

    narrador "(Transición)"
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Cocina. Eva está terminando de ordenar. Lucas corre a abrazar a Gabriel apenas lo ve entrar."

    lucas "¡Papá! ¡Llegaste!"
    gabriel "(Le da un beso a Lucas y se acerca a Eva, extendiendo la rosa) Tomá. Pasé por la florería y me acordé de vos."
    eva "(Sorprendida, toma la flor y la huele. Su expresión de cansancio se suaviza un segundo) Es hermosa, amor, gracias. ¿Te fue bien en la oficina hoy?"
    gabriel "No mucho. Me pidieron quedarme horas extra y le dije que no. No le gustó nada al jefe. Quería tiempo para ustedes y para escribir."
    eva "Te amamos, pero me preocupa que tu sueño de escribir te vaya a complicar el laburo."
    gabriel "Necesito el tiempo para la historia, amor. Quería que estuviéramos bien antes de sentarme a escribir. No los voy a defraudar."
    eva "(Sonríe un poco esperanzada) Te dejo a lo tuyo entonces. Voy a ayudar a Lucas con la tarea."
    lucas "¿Ahora? ¡Pero quería jugar con papá!"
    gabriel "(Riéndose) Mañana será, hijo. Ahora a estudiar con mamá."

    narrador "Eva y Lucas se van. (Transición)."
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Habitación. Gabriel frente a la PC. La rosa en el vaso de agua se ve en primer plano junto al monitor."
    pensamiento "El florista tenía razón. El ambiente se siente distinto. Menos pesado."
    narrador "(A un costado del teclado, se destaca el aviso de la AFIP.)"

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. No los puedo defraudar."
    jump dia1_eleccion_tono


label dia1_parada_colectivo:

    "Gabriel asiente en silencio. Daniel le da una palmada condescendiente en el hombro y se va."

    "Se enfoca el reloj que transiciona de 18hs a 21hs."

    "Parada de colectivo. Noche. Lluvia. Gabriel está solo, encorvado bajo el frío. Un vagabundo sentado sobre unos cartones extiende una mano."

    vagabundo "Una ayuda, jefe... para un café. Hace mucho frío."

    menu:
        "Ayudarlo":
            $ decision_calle = "ayudar"
            jump casa_ayuda

        "Ignorarlo":
            $ decision_calle = "ignorar"
            jump casa_ignora


label casa_ayuda:

    "Gabriel saca un billete de 2.000 pesos arrugado. Se lo entrega al hombre."

    vagabundo "Gracias, bendiciones. Ya me ignoraron tantos que solo me quedaba soñar."

    gabriel "Mal día. Mañana será otro."

    vagabundo "Eso decimos todos. Tené cuidado, a veces uno se pasa la vida escribiendo el prólogo y se olvida de que el libro tiene muchas páginas."

    gabriel "¿Qué? ¿Vos sabés quién soy? ¿Cómo sabés que escribo?"

    vagabundo "Te aferrás a tus cosas como si tu vida estuviera ahí. Si llevas algo que vale la pena, lo abrazas."

    gabriel "Ya llega el bondi. Me tengo que ir."

    "Llega el colectivo. Gabriel sube rápido, pero se queda mirando por la ventanilla mientras el hombre vuelve a fundirse en la oscuridad."

    gabriel "{i}Uno se pasa la vida escribiendo el prólogo. Solo yo me encuentro estos personajes.{/i}"

    "Cocina pequeña, luz cálida pero tenue. Eva está lavando un plato. Lucas no está en escena."

    eva "Lucas ya se durmió. Estuvo preguntando por qué su papá no llegaba."

    gabriel "Perdón Eva. Daniel me encajó lo de zona sur. Me tuve que quedar."

    eva "¿Te van a pagar esta vez las horas extra? ¿O es otro favor para cuidar el puesto?"

    gabriel "Probablemente no... pero no puedo decir que no ahora. No con cómo están las cosas."

    "Se enfoca a Eva que suspira en resignación. Vuelve a Gabriel."

    gabriel "Eva, me queda una semana para terminar una historia. Si gano, puedo cambiar las cosas."

    eva "¿Ahora te parece el mejor momento, Gabriel? No sé si estamos para sueños ahora."

    "Eva sale de la cocina sin decir nada más. Se escucha el cierre de una puerta."

    "Habitación en penumbra. Solo la luz del monitor ilumina la cara de Gabriel. A un costado del teclado, se destaca el aviso de la AFIP."

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. Es lo único que me queda."
    jump dia1_eleccion_tono


label casa_ignora:

    narrador "Gabriel da un paso atrás para evitar cruzar miradas con el hombre, acercándose demasiado al cordón de la vereda."
    narrador "Un taxi pasa a toda velocidad, pisando de lleno un bache gigante. Un chorro de agua sucia y barro empapa a Gabriel de pies a cabeza. El vagabundo ni se inmuta, solo se cubre con su cartón."
    narrador "Llega el colectivo. Gabriel sube rápido, chorreando agua. La gente a su alrededor lo mira con desagrado y se aparta. Se sienta junto a la ventanilla mojada."

    pensamiento "Qué locura cómo estamos. La calle no perdona a nadie."

    narrador "Entrada de la casa. Luz apagada, ambiente en completo silencio."
    narrador "Gabriel está empapado y el agua sucia gotea sobre el piso."

    pensamiento "Me tengo que sacar el barro antes de poner a lavar esto."

    narrador "(Transición)"
    narrador "Baño pequeño y azulejos viejos. Luz blanca parpadeante. Gabriel está encorvado frente a la pileta, intentando limpiar el barro de su ropa bajo el chorro de agua fría."
    narrador "En el reflejo del espejo se ve a Eva apareciendo en el marco de la puerta."

    eva "Gabriel... escuché la puerta y no venías a la cocina. ¿Qué te pasó?"
    gabriel "Un taxi. Agarró un pozo enorme en la avenida. No pasa nada, sale con agua."
    eva "Estás temblando, Gabi. Y llegaste tardísimo, Lucas te estuvo esperando para..."
    gabriel "¡Ya sé que llegué tarde, Eva! ¡Me tuve que quedar haciendo los remitos de mierda de Daniel y encima me pasa esto! ¡No me lo recuerdes!"
    eva "No me grites. Yo no tengo la culpa de que no te animes a decirle que no a tu jefe."
    gabriel "Todo esto es para nosotros. Si gano el concurso la semana que viene..."
    eva "Mirate, Gabriel. Estás lavando barro de tu única ropa decente en un baño congelado a las diez de la noche. Secate y andá a dormir, no quiero que Lucas te escuche gritar así."

    narrador "Eva sale, dejándolo solo."
    narrador "Gabriel se vuelve a mirar en el espejo salpicado: está empapado, sucio y derrotado."
    narrador "(Transición)"
    narrador "Habitación en penumbra. Solo la luz del monitor ilumina la cara de Gabriel. A un costado del teclado, se destaca el aviso de la AFIP."

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. Es lo único que me queda."
    jump dia1_eleccion_tono


label dia1_eleccion_tono:

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

    jump dia1_convergencia_final


label dia1_convergencia_final:

    narrador "(Tras elegir el tono del libro, se ve a Gabriel que saca una moneda del bolsillo. Se escucha solo la lluvia y se ve la luz del monitor reflejada.)"
    narrador "(Se enfoca la moneda y lleva a un flashback.)"
    sistema "FLASHBACK"
    narrador "(Habitación de Lucas. Lucas tiene dos juguetes en la mano. La habitación está bien iluminada. Día soleado.)"

    lucas "Me quiero llevar uno para mostrarle a mis amigos hoy, pero no sé cuál llevar, pa."
    gabriel "(Sonriendo, saca una moneda del bolsillo). Te voy a enseñar un truco. Vamos a tirarla. Cara es el auto, ceca es el dragón."
    lucas "¡Pero eso es elegir a ver cuál tiene más suerte! ¡No me gusta!"
    gabriel "Ahí está el secreto. Tirala bien alto. En el momento en que la moneda esté en el aire, antes de que caiga, vas a sentir que hay una de las dos opciones que preferís que salga."
    lucas "¿Para qué tiro la moneda entonces?"
    gabriel "Porque no importa lo que diga la moneda, solo qué sentiste mientras volaba. Vamos a probar."

    narrador "(Gabriel tira la moneda en el aire. Cae ceca.)"
    lucas "¡Vamos! ¡Llevo el dragón!"
    narrador "(Lucas le da un abrazo a Gabriel. Se enfoca la moneda en el piso.)"
    sistema "Fin del FLASHBACK"
    narrador "(Se ve a Gabriel con la moneda en la mano. Escenario anterior.)"

    pensamiento "¿Qué es lo que realmente quiero? ¿Qué tengo que hacer?"

    narrador "(Gabriel lanza la moneda. El sonido del metal girando en el aire invade todo el ambiente, tapando el ruido de la lluvia. Gabriel atrapa la moneda con un golpe seco, cubriéndola con la otra palma sobre el escritorio.)"
    narrador "(Gabriel no mira el resultado. Se lo escucha suspirar.)"
    narrador "(Pantalla a negro.)"
    sistema "FIN DEL DÍA 1"

    return

