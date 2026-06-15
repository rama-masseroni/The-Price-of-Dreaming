# Coloca el código de tu juego en este archivo.


# El juego comienza aquí.

default decision_horas_extra = None
default decision_calle = None
default tono_novela = None


label start:

    scene black

    scene bg oficina with dissolve

    narrador "DÍA 1"
    narrador "Se observa a Gabriel, sentado frente a la PC en su cubículo de la oficina."
    narrador "(Se abre una ventana emergente en la pantalla de la PC: un correo electrónico.)"

    call screen correo_convocatoria

    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Faltan siete días. Solo siete días."
    narrador "(Entra Daniel, el jefe, caminando con paso pesado. Se apoya en el escritorio de Gabriel, invadiendo su espacio.)"

    show daniel normal at busto_derecha with dissolve
    daniel "Gabi, querido. Escuchame, surgió un problema con la carga de los remitos de la zona sur. Necesito que te quedes un par de horas más para cerrar el balance hoy."
    gabriel "Pero Daniel, hoy tenía que..."

    hide daniel normal with dissolve
    show daniel enojado at busto_derecha with dissolve

    daniel "Dale, no me falles. Sabés que la mano viene dura y necesito gente comprometida. ¿Te quedás, no?"

    menu:
        "Aceptar":
            $ decision_horas_extra = "aceptar"
            jump dia1_parada_colectivo

        "Excusarse":
            $ decision_horas_extra = "excusarse"
            jump dia1_calle_temprano


label dia1_calle_temprano:

    scene bg centro_floreria with dissolve

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

    scene bg cocina_fria with dissolve

    narrador "Eva está sentada en la mesa revisando unos papeles con el ceño fruncido. Lucas está dibujando en un rincón."

    lucas "¡Papá! Llegaste temprano."
    gabriel "(Le acaricia la cabeza a Lucas y mira a Eva con cautela). Hola."
    eva "(Levanta la vista de los papeles, extrañada) ¿Qué pasó? ¿Te dejaron salir a horario hoy de milagro?"
    gabriel "Daniel me pidió que me quede a hacer horas extra, pero le dije que no. Necesitaba volver a casa... y avanzar con la novela. Me queda una semana."
    eva "(Suspira, frotándose la frente y señalando la mesa) Gabriel... no estamos en condiciones de rechazar plata extra del laburo."
    gabriel "(Se acerca, tenso) Ya sé, Eva. Pero si termino la novela y gano el concurso, el adelanto editorial nos da un respiro en serio. Necesito este tiempo para escribir."
    eva "(Con voz dura, pragmática). Me alegra que estés acá con nosotros, pero me asusta lo que estás apostando. (Se pone de pie). Lucas, vamos a la pieza a terminar la tarea, dejá a tu papá \"trabajar\"."

    narrador "(Eva y Lucas salen de la escena. El ambiente de la cocina queda frío y envuelto en un silencio incómodo.)"
    scene bg habitacion_gabriel_oscuro with dissolve
    narrador "Gabriel se sienta frente a la PC. El silencio de la casa pesa."
    scene bg papeles_escritorio with dissolve
    narrador "(A un costado del teclado, se destaca el aviso de la AFIP.)"

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "No me entienden. Quizás nadie lo haga. Pero tengo que ganar esto como sea."
    jump dia1_eleccion_tono


label dia1_casa_flor:

    scene bg interior_floreria with dissolve

    narrador "(Entra al local. Un vendedor mayor lo observa detrás de varios ramos de flores.)"

    show vendedor normal at busto_derecha with dissolve
    vendedor "Buscás algo para pedir perdón o para que no se olviden de vos, ¿no? Se te nota en la cara."
    
    show gabriel normal at busto_izquierda with dissolve
    gabriel "(Mira los precios, preocupado) Algo sencillo. No puedo gastar mucho hoy, de verdad."
    vendedor "(Saca una única rosa) Llevate esta. El valor no está en el precio, sino en el gesto de haber pensado en el otro. Estar en paz con los que aman te ayuda a pensar. Te limpia la cabeza."
    gabriel "(Mira su billetera, sonríe levemente y paga) Gracias, me la llevo."

    scene bg cocina_calida with dissolve
    show gabriel normal at busto_izquierda with dissolve
    narrador "Eva está terminando de ordenar. Lucas corre a abrazar a Gabriel apenas lo ve entrar."

    show lucas feliz at busto_derecha with dissolve
    lucas "¡Papá! ¡Llegaste!"
    
    show gabriel feliz at busto_izquierda with dissolve
    gabriel "(Le da un beso a Lucas)"
    hide lucas feliz
    show eva normal at busto_derecha with dissolve
    gabriel "Tomá. Pasé por la florería y me acordé de vos."

    eva "(Sorprendida, toma la flor y la huele.)"
    show eva feliz at busto_derecha with dissolve
    eva "(Su expresión de cansancio se suaviza un segundo)"
    eva "Es hermosa, amor, gracias. ¿Te fue bien en la oficina hoy?"
    gabriel "No mucho. Me pidieron quedarme horas extra y le dije que no. No le gustó nada al jefe. Quería tiempo para ustedes y para escribir."
    eva "Te amamos, pero me preocupa que tu sueño de escribir te vaya a complicar el laburo."
    gabriel "Necesito el tiempo para la historia, amor. Quería que estuviéramos bien antes de sentarme a escribir. No los voy a defraudar."
    eva "(Sonríe un poco esperanzada) Te dejo a lo tuyo entonces. Voy a ayudar a Lucas con la tarea."
    hide gabriel feliz
    show lucas normal at busto_izquierda with dissolve
    lucas "¿Ahora? ¡Pero quería jugar con papá!"

    hide eva feliz
    show gabriel feliz at busto_derecha with dissolve
    gabriel "(Riéndose) Mañana será, hijo. Ahora a estudiar con mamá."

    hide lucas normal with dissolve
    narrador "Eva y Lucas se van."
    scene bg habitacion_gabriel with dissolve
    show gabriel feliz at busto_izquierda with dissolve
    pensamiento "El florista tenía razón. El ambiente se siente distinto. Menos pesado."
    scene bg papeles_escritorio with dissolve
    narrador "(A un costado del teclado, se destaca el aviso de la AFIP.)"

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. No los puedo defraudar."
    jump dia1_eleccion_tono


label dia1_parada_colectivo:

    scene bg oficina

    show gabriel enojado at busto_izquierda with dissolve
    show daniel normal at busto_derecha with dissolve
    "Gabriel asiente en silencio. Daniel le da una palmada condescendiente en el hombro y se va."
    hide daniel normal with dissolve
    
    "Se enfoca el reloj que transiciona de 18hs a 21hs."

    scene bg parada_lluvia with dissolve
    "Gabriel está solo, encorvado bajo el frío. Un vagabundo sentado sobre unos cartones extiende una mano."

    show gabriel triste at busto_izquierda with dissolve
    show vagabundo normal at busto_derecha with dissolve
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

    show gabriel normal at busto_izquierda with dissolve
    show vagabundo feliz at busto_derecha with dissolve
    vagabundo "Gracias, bendiciones. Ya me ignoraron tantos que solo me quedaba soñar."

    gabriel "Mal día. Mañana será otro."

    vagabundo "Eso decimos todos. Tené cuidado, a veces uno se pasa la vida escribiendo el prólogo y se olvida de que el libro tiene muchas páginas."

    gabriel "¿Qué? ¿Vos sabés quién soy? ¿Cómo sabés que escribo?"

    vagabundo "Te aferrás a tus cosas como si tu vida estuviera ahí. Si llevas algo que vale la pena, lo abrazas."

    gabriel "Ya llega el bondi. Me tengo que ir."

    hide vagabundo feliz with dissolve
    "Llega el colectivo. Gabriel sube rápido, pero se queda mirando por la ventanilla mientras el hombre vuelve a fundirse en la oscuridad."

    scene bg interior_colectivo with dissolve
    gabriel "{i}Uno se pasa la vida escribiendo el prólogo. Solo yo me encuentro estos personajes.{/i}"

    scene bg cocina_calida with dissolve
    show eva normal at busto_derecha with dissolve
    "Eva está lavando un plato. Lucas no está en escena."

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

    hide gabriel with dissolve
    "Se enfoca a Eva que suspira en resignación. Vuelve a Gabriel."

    show gabriel normal at busto_izquierda with dissolve
    show eva normal at busto_derecha with dissolve
    gabriel "Eva, me queda una semana para terminar una historia. Si gano, puedo cambiar las cosas."

    show eva enojada at busto_derecha with dissolve
    eva "¿Ahora te parece el mejor momento, Gabriel? No sé si estamos para sueños ahora."

    hide eva with dissolve
    "Eva sale de la cocina sin decir nada más. Se escucha el cierre de una puerta."

    scene bg habitacion_gabriel with dissolve
    "Solo la luz del monitor ilumina la cara de Gabriel."
    scene bg papeles_escritorio with dissolve
    "A un costado del teclado, se destaca el aviso de la AFIP."

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

    pensamiento "Tengo que escribir. Es lo único que me queda."
    jump dia1_eleccion_tono


label casa_ignora:

    show gabriel normal at busto_izquierda with dissolve
    narrador "Gabriel da un paso atrás para evitar cruzar miradas con el hombre, acercándose demasiado al cordón de la vereda."
    hide vagabundo with dissolve
    narrador "Un taxi pasa a toda velocidad, pisando de lleno un bache gigante. Un chorro de agua sucia y barro empapa a Gabriel de pies a cabeza. El vagabundo ni se inmuta, solo se cubre con su cartón."
    show gabriel enojado at busto_izquierda with dissolve
    narrador "Llega el colectivo. Gabriel sube rápido, chorreando agua. La gente a su alrededor lo mira con desagrado y se aparta. Se sienta junto a la ventanilla mojada."

    scene bg interior_colectivo with dissolve
    show gabriel enojado at busto_izquierda with dissolve
    pensamiento "Qué locura cómo estamos. La calle no perdona a nadie."

    scene bg entrada_casa with dissolve
    narrador "Gabriel está empapado y el agua sucia gotea sobre el piso."

    show gabriel normal at busto_izquierda with dissolve
    pensamiento "Me tengo que sacar el barro antes de poner a lavar esto."

    scene bg banio with dissolve
    show gabriel enojado at busto_izquierda with dissolve
    narrador "Gabriel está encorvado frente a la pileta, intentando limpiar el barro de su ropa bajo el chorro de agua fría."
    narrador "En el reflejo del espejo se ve a Eva apareciendo en el marco de la puerta."

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

    narrador "Eva sale, dejándolo solo."
    hide eva with dissolve
    show gabriel triste at busto_izquierda with dissolve
    narrador "Gabriel se vuelve a mirar en el espejo salpicado: está empapado, sucio y derrotado."
    scene bg habitacion_gabriel_oscuro with dissolve
    narrador "Solo la luz del monitor ilumina la cara de Gabriel."
    scene bg papeles_escritorio with dissolve
    narrador "A un costado del teclado, se destaca el aviso de la AFIP."

    call screen documento_aviso("ARCA/AFIP - NOTIFICACIÓN DE DEUDA", "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.", "EMBARGO PREVENTIVO")

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

    jump dia1_convergencia_final


label dia1_convergencia_final:

    if decision_calle == "comprar_regalo":
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve

    narrador "(Tras elegir el tono del libro, se ve a Gabriel que saca una moneda del bolsillo. Se escucha solo la lluvia y se ve la luz del monitor reflejada.)"
    narrador "(Se enfoca la moneda y lleva a un flashback.)"
    scene black with dissolve
    scene bg habitacion_lucas with dissolve
    show lucas feliz at busto_izquierda with dissolve
    narrador "(Lucas tiene dos juguetes en la mano.)"
    hide lucas feliz
    show lucas normal at busto_izquierda with dissolve
    lucas "Me quiero llevar uno para mostrarle a mis amigos hoy, pero no sé cuál llevar, pa."

    show gabriel normal at busto_derecha with dissolve
    gabriel "(Sonriendo, saca una moneda del bolsillo). Te voy a enseñar un truco. Vamos a tirarla. Cara es el auto, ceca es el dragón."
    
    hide lucas normal with dissolve
    show lucas triste at busto_izquierda with dissolve
    lucas "¡Pero eso es elegir a ver cuál tiene más suerte! ¡No me gusta!"

    hide gabriel feliz
    show gabriel normal at busto_derecha with dissolve    
    gabriel "Ahí está el secreto. Tirala bien alto. En el momento en que la moneda esté en el aire, antes de que caiga, vas a sentir que hay una de las dos opciones que preferís que salga."

    hide lucas triste with dissolve
    show lucas enojado at busto_izquierda with dissolve
    lucas "¿Para qué tiro la moneda entonces?"

    hide gabriel normal
    show gabriel feliz at busto_derecha with dissolve
    gabriel "Porque no importa lo que diga la moneda, solo qué sentiste mientras volaba. Vamos a probar."

    narrador "(Gabriel tira la moneda en el aire. Cae ceca.)"
    hide lucas enojado with dissolve
    hide gabriel feliz
    show lucas feliz at busto_izquierda with dissolve
    lucas "¡Vamos! ¡Llevo el dragón!"
    narrador "(Lucas le da un abrazo a Gabriel. Se enfoca la moneda en el piso.)"
    scene black with dissolve
    if decision_calle == "comprar_regalo":
        scene bg habitacion_gabriel with dissolve
    else:
        scene bg habitacion_gabriel_oscuro with dissolve
    narrador "(Se ve a Gabriel con la moneda en la mano.)"

    show gabriel triste at busto_izquierda with dissolve
    pensamiento "¿Qué es lo que realmente quiero? ¿Qué tengo que hacer?"

    narrador "(Gabriel lanza la moneda. El sonido del metal girando en el aire invade todo el ambiente, tapando el ruido de la lluvia. Gabriel atrapa la moneda con un golpe seco, cubriéndola con la otra palma sobre el escritorio.)"
    narrador "(Gabriel no mira el resultado. Se lo escucha suspirar.)"
    scene black with dissolve
    sistema "FIN DEL DÍA 1"

    return

